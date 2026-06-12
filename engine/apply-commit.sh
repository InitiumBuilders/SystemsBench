#!/usr/bin/env bash
# apply-commit.sh — make a SenseRun APPLY a git property, not a promise.
# Commits EXACTLY the applied enhancement (everything changed under SystemsBench/
# EXCEPT runtime records: .state/ and logs/) as ONE commit, and records the hash
# in .state/runs/run-<N>.json so rollback-run.sh can revert exactly that commit.
#
# INFRASTRUCTURE ONLY: this script cannot approve an APPLY. The gate verdict lives
# in the Engine doc's governance, executed by the worker BEFORE calling this.
#
# Usage:
#   apply-commit.sh <N> "<one-line lever summary>"
#
# Guarantees:
#   - stages only paths under SystemsBench/ (records excluded) — never repo-wide
#   - refuses if there is nothing to commit (an APPLY with no diff is a lie)
#   - never pushes (worker rail: commits are local; the operator pushes)
set -uo pipefail

BENCH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(git -C "$BENCH" rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR: not inside a git repo" >&2; exit 2; }
REL="${BENCH#"$ROOT"/}"
RUNS_DIR="$BENCH/.state/runs"

n="${1:-}"; summary="${2:-}"
[ -z "$n" ] && { echo "usage: apply-commit.sh <N> \"<one-line lever summary>\"" >&2; exit 1; }
state="$RUNS_DIR/run-$n.json"
[ -f "$state" ] || { echo "ERROR: no run state $state — APPLY without a run is forbidden" >&2; exit 4; }
[ -z "$summary" ] && summary="$(python3 -c "import json;d=json.load(open('$state'));print((d['phases']['APPLY'].get('note') or 'enhancement applied'))" 2>/dev/null || echo 'enhancement applied')"

# Refuse double-apply: one APPLY commit per run.
existing="$(python3 -c "import json;print(json.load(open('$state')).get('apply_commit') or '')" 2>/dev/null)"
[ -n "$existing" ] && { echo "ERROR: run $n already has apply_commit $existing — one APPLY commit per run" >&2; exit 5; }

# Stage the enhancement only: everything under SystemsBench/ minus runtime records.
git -C "$ROOT" add -A -- "$REL"
git -C "$ROOT" reset -q -- "$REL/.state" "$REL/logs" 2>/dev/null

if git -C "$ROOT" diff --cached --quiet; then
  echo "ERROR: nothing staged under $REL (records excluded) — no diff, no APPLY commit" >&2
  exit 6
fi

# Safety: every staged path must live under SystemsBench/.
bad="$(git -C "$ROOT" diff --cached --name-only | grep -v "^$REL/" || true)"
[ -n "$bad" ] && { echo "ERROR: staged paths escape $REL/ — refusing:"$'\n'"$bad" >&2; git -C "$ROOT" reset -q; exit 7; }

echo "--- APPLY commit for SenseRun #$n will contain:"
git -C "$ROOT" diff --cached --name-status

git -C "$ROOT" commit -q -m "SenseRun #$n APPLY: $summary

One lever, reversible by construction: revert this commit = rollback of run #$n.
SenseRun-Apply: $n" || { echo "ERROR: commit failed" >&2; exit 8; }

hash="$(git -C "$ROOT" rev-parse HEAD)"

# Record the hash in run state (atomic, python3 — no jq on this host).
STATE="$state" HASH="$hash" python3 - <<'PY'
import json, os, tempfile
f = os.environ["STATE"]
d = json.load(open(f))
d["apply_commit"] = os.environ["HASH"]
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(f), suffix=".tmp")
with os.fdopen(fd, "w") as fh: json.dump(d, fh, indent=2)
os.replace(tmp, f)
PY
"$BENCH/engine/phase-mark.sh" note "$n" APPLY "applied in commit $hash" >/dev/null 2>&1 || true

echo "OK: SenseRun #$n APPLY committed as $hash (local only — not pushed)"
echo "Rollback at any time: engine/rollback-run.sh $n"
