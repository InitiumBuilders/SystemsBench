#!/usr/bin/env bash
# rollback-run.sh — revert EXACTLY one SenseRun's APPLY commit. Nothing more.
# Reads apply_commit from .state/runs/run-<N>.json (recorded by apply-commit.sh),
# verifies that commit touches only SystemsBench/ paths, then produces ONE atomic
# rollback commit: the revert diff + a CHANGELOG entry documenting the rollback.
#
# Usage:
#   rollback-run.sh <N>
#
# Guarantees:
#   - reverts the run's recorded commit only — never `git reset`, never a range
#   - refuses if the commit touches paths outside SystemsBench/ (wrong commit)
#   - refuses on a dirty SystemsBench tree (uncommitted work is not mine to eat)
#   - on revert conflict: aborts cleanly, leaves the tree untouched, exits 1
#   - never pushes
set -uo pipefail

BENCH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(git -C "$BENCH" rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR: not inside a git repo" >&2; exit 2; }
REL="${BENCH#"$ROOT"/}"

n="${1:-}"
[ -z "$n" ] && { echo "usage: rollback-run.sh <N>" >&2; exit 1; }
state="$BENCH/.state/runs/run-$n.json"
[ -f "$state" ] || { echo "ERROR: no run state $state" >&2; exit 4; }

hash="$(python3 -c "import json;print(json.load(open('$state')).get('apply_commit') or '')")"
[ -z "$hash" ] && { echo "ERROR: run $n has no recorded apply_commit — nothing to roll back" >&2; exit 5; }
already="$(python3 -c "import json;print(json.load(open('$state')).get('rollback_commit') or '')")"
[ -n "$already" ] && { echo "ERROR: run $n already rolled back in $already" >&2; exit 5; }

git -C "$ROOT" cat-file -e "$hash^{commit}" 2>/dev/null || { echo "ERROR: commit $hash not found in this repo" >&2; exit 6; }

# The commit we revert must be a pure SystemsBench commit.
outside="$(git -C "$ROOT" show --name-only --format= "$hash" | grep -v -e '^$' -e "^$REL/" || true)"
[ -n "$outside" ] && { echo "ERROR: $hash touches paths outside $REL/ — refusing to revert:"$'\n'"$outside" >&2; exit 7; }

# Clean tree under SystemsBench (runtime records exempt — they churn by design).
dirty="$(git -C "$ROOT" status --porcelain -- "$REL" | grep -v -e " $REL/.state/" -e " $REL/logs/" || true)"
[ -n "$dirty" ] && { echo "ERROR: uncommitted changes under $REL/ — commit or stash them first:"$'\n'"$dirty" >&2; exit 8; }

echo "--- Reverting SenseRun #$n APPLY commit $hash:"
git -C "$ROOT" show --stat --format="%h %s" "$hash" | head -20

if ! git -C "$ROOT" revert --no-commit --no-edit "$hash" 2>&1; then
  git -C "$ROOT" revert --abort 2>/dev/null
  echo "ERROR: revert conflicts with later changes — tree left untouched." >&2
  echo "Resolve manually: a later commit built on top of run #$n's diff." >&2
  exit 9
fi

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf '\n## [rollback] — %s\n- **ROLLBACK SenseRun #%s** — reverted APPLY commit `%s` via engine/rollback-run.sh. Reversibility exercised as a property, not a promise.\n' "$ts" "$n" "$hash" >> "$BENCH/CHANGELOG.md"
git -C "$ROOT" add -- "$REL/CHANGELOG.md"

git -C "$ROOT" commit -q -m "SenseRun #$n ROLLBACK: revert $hash

SenseRun-Rollback: $n" || { echo "ERROR: rollback commit failed" >&2; exit 10; }

rhash="$(git -C "$ROOT" rev-parse HEAD)"
STATE="$state" HASH="$rhash" python3 - <<'PY'
import json, os, tempfile
f = os.environ["STATE"]
d = json.load(open(f))
d["rollback_commit"] = os.environ["HASH"]
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(f), suffix=".tmp")
with os.fdopen(fd, "w") as fh: json.dump(d, fh, indent=2)
os.replace(tmp, f)
PY
"$BENCH/engine/phase-mark.sh" note "$n" APPLY "ROLLED BACK: $hash reverted in $rhash" >/dev/null 2>&1 || true

echo "OK: run #$n rolled back — revert commit $rhash (local only — not pushed)"
