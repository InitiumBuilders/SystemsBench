#!/usr/bin/env bash
# verify-run.sh — self-verification for a completed SenseRun. Proof, not self-report.
# Checks the run's artifacts against what SystemsBenchEngine.MD says a run must produce.
# Exit 0 = verified · exit 1 = failures listed. Read-only; never mutates anything.
#
# Usage: verify-run.sh <N>
set -uo pipefail

BENCH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
n="${1:-}"; [ -z "$n" ] && { echo "usage: verify-run.sh <N>"; exit 1; }
command -v python3 >/dev/null || { echo "ERROR: python3 required" >&2; exit 2; }
state="$BENCH/.state/runs/run-$n.json"

jget() { # jget <file> <dotted.path>  -> value or empty
  python3 -c '
import json,sys
try:
    d=json.load(open(sys.argv[1]))
    for k in sys.argv[2].split("."): d=d[k]
    print(d if d is not None else "")
except Exception: pass' "$1" "$2"
}

fail=0
ok()  { printf '  PASS  %s\n' "$1"; }
bad() { printf '  FAIL  %s\n' "$1"; fail=1; }

echo "== verify SenseRun #$n =="

# 1. Phase state: exists, run complete, all phases complete/skipped
runlog=""
if [ -f "$state" ]; then
  ok "phase state exists: ${state#$BENCH/}"
  st="$(jget "$state" status)"
  [ "$st" = "complete" ] && ok "run status: complete" || bad "run status is '$st', not complete"
  incomplete="$(python3 -c '
import json,sys
d=json.load(open(sys.argv[1]))
print(" ".join(k for k,v in d["phases"].items() if v["status"] not in ("complete","skipped")))' "$state")"
  [ -z "$incomplete" ] && ok "all 9 phases complete/skipped" || bad "incomplete phases: $incomplete"
  runlog="$(jget "$state" run_log)"
else
  bad "no phase state at .state/runs/run-$n.json"
fi

# 2. Run log: exists and carries every required block (Engine doc §2 template)
[ -z "$runlog" ] && runlog="$(ls -1 "$BENCH"/logs/runs/*run-$n.md 2>/dev/null | head -1)"
case "$runlog" in /*) ;; "") ;; *) runlog="$BENCH/$runlog";; esac
if [ -n "$runlog" ] && [ -f "$runlog" ]; then
  ok "run log exists: ${runlog#$BENCH/}"
  for block in STATE CRITIQUE RESEARCH PROPOSAL REVIEW CALIBRATE "THOUGHT PROCESS" RECURSE; do
    grep -qi "^## .*$block" "$runlog" && ok "run log block: $block" || bad "run log missing block: $block"
  done
  # APPLY may legitimately be absent on DEFER/REJECT — require either APPLY or a non-GO verdict
  if grep -qi '^## .*APPLY' "$runlog"; then ok "run log block: APPLY"
  elif grep -qiE 'Verdict:.*(DEFER|REJECT)' "$runlog"; then ok "no APPLY block, but verdict is DEFER/REJECT (legitimate)"
  else bad "run log has neither APPLY block nor a DEFER/REJECT verdict"; fi
else
  bad "no run log found for run $n in logs/runs/"
fi

# 3. Scorecard exists
if ls "$BENCH"/logs/scorecards/*.md >/dev/null 2>&1; then
  newest_card="$(ls -1t "$BENCH"/logs/scorecards/*.md | head -1)"
  ok "scorecards present (newest: ${newest_card#$BENCH/})"
else
  bad "no scorecards in logs/scorecards/"
fi

# 4. Engine state consistency
es="$BENCH/.state/engine_state.json"
if [ -f "$es" ]; then
  last="$(jget "$es" last_senserun)"
  if [ -n "$last" ] && [ "$last" -ge "$n" ] 2>/dev/null; then ok "engine_state.json last_senserun=$last >= $n"
  else bad "engine_state.json last_senserun='$last' — run $n did not update it"; fi
else
  bad "missing .state/engine_state.json"
fi

# 5. If the run APPLIED a change, CHANGELOG must carry a dated line
if [ -n "$runlog" ] && [ -f "$runlog" ] && grep -qi '^## .*APPLY' "$runlog"; then
  if grep -q "$(date +%Y)" "$BENCH/CHANGELOG.md" 2>/dev/null; then
    ok "CHANGELOG.md has current-year entries (APPLY ran)"
  else
    bad "APPLY block present but CHANGELOG.md has no recent entry"
  fi
fi

echo
if [ "$fail" = 0 ]; then echo "VERDICT: run $n VERIFIED — artifacts complete and consistent."; else echo "VERDICT: run $n FAILED verification — fix the FAIL lines above."; fi
exit "$fail"
