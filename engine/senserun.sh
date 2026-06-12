#!/usr/bin/env bash
# senserun.sh — detached-builder launcher for SystemsBench SenseRuns.
# INFRASTRUCTURE ONLY: all governance (invariants, gates, one-lever, fail-closed) lives in
# SystemsBenchEngine.MD and is enforced BY THE WORKER reading that doc. This script just
# launches, tracks, resumes, and verifies — it cannot approve anything.
#
# Pattern: heavy runs ride a detached `claude -p` builder job (subscription rail, API key
# stripped), never conversational relay turns. Per-phase checkpoints (.state/runs/) +
# a session UUID mean any death resumes mid-phase with context, never from zero.
#
# Usage:
#   senserun.sh start <N> ["scope note"]   launch SenseRun #N detached
#   senserun.sh resume <N>                 relaunch a dead/incomplete run at its next phase
#   senserun.sh status <N>                 phase progress + worker liveness + log tail
#   senserun.sh abort <N>                  stop the worker, mark run aborted
#   senserun.sh verify <N>                 self-verification (delegates to verify-run.sh)
#
# Env overrides:
#   SENSERUN_MODEL=...      model pin (default: engine/local.env wiring, else claude-opus-4-7)
#   SENSERUN_MAX_TURNS=200  worker turn budget (big: a full nine-phase run with subagents)
#   SENSERUN_TOOLS="Read Write Edit Bash Glob Grep Task TodoWrite WebFetch WebSearch"
#   SENSERUN_DRY=1          print the launch command instead of executing (test mode)
#
# Host-specific wiring (private rails, model-pin source, paths) lives in engine/local.env —
# UNTRACKED by design: tracked files stay host-agnostic and publishable.
set -uo pipefail

BENCH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENGINE="$BENCH/engine"
RUNS_DIR="$BENCH/.state/runs"
WLOG_DIR="$BENCH/logs/workers"
[ -f "$ENGINE/local.env" ] && . "$ENGINE/local.env"

cmd="${1:-}"; n="${2:-}"
[ -z "$cmd" ] || [ -z "$n" ] && { sed -n '12,18p' "${BASH_SOURCE[0]}"; exit 1; }
mkdir -p "$RUNS_DIR" "$WLOG_DIR"

state="$RUNS_DIR/run-$n.json"
pidf="$RUNS_DIR/run-$n.pid"
sidf="$RUNS_DIR/run-$n.sid"
wlog="$WLOG_DIR/run-$n.log"

# Subscription rail only — never the paid API.
unset ANTHROPIC_API_KEY || true

resolve_model() { echo "${SENSERUN_MODEL:-claude-opus-4-7}"; }

worker_alive() { [ -f "$pidf" ] && kill -0 "$(cat "$pidf")" 2>/dev/null; }

launch_worker() { # launch_worker <prompt> <fresh|resume>
  local prompt="$1" mode="$2" model turns tools sid
  model="$(resolve_model)"
  turns="${SENSERUN_MAX_TURNS:-200}"
  tools="${SENSERUN_TOOLS:-Read Write Edit Bash Glob Grep Task TodoWrite WebFetch WebSearch}"

  if [ "$mode" = "resume" ] && [ -s "$sidf" ]; then
    sid="$(cat "$sidf")"
    if [ "${SENSERUN_DRY:-0}" = "1" ]; then
      echo "DRY-RUN: claude -p --resume $sid --model $model --max-turns $turns --allowedTools \"$tools\"  (cwd=$BENCH)"
      return 0
    fi
    ( cd "$BENCH" && printf '%s' "$prompt" | nohup claude -p \
        --resume "$sid" --model "$model" --max-turns "$turns" \
        --allowedTools "$tools" >>"$wlog" 2>&1 & echo $! > "$pidf" )
  else
    sid="$(uuidgen 2>/dev/null || cat /proc/sys/kernel/random/uuid)"
    if [ "${SENSERUN_DRY:-0}" = "1" ]; then
      echo "DRY-RUN: claude -p --session-id $sid --model $model --max-turns $turns --allowedTools \"$tools\"  (cwd=$BENCH)"
      return 0
    fi
    echo "$sid" > "$sidf"
    ( cd "$BENCH" && printf '%s' "$prompt" | nohup claude -p \
        --session-id "$sid" --model "$model" --max-turns "$turns" \
        --allowedTools "$tools" >>"$wlog" 2>&1 & echo $! > "$pidf" )
  fi
  echo "SenseRun #$n worker launched ($mode) · pid $(cat "$pidf" 2>/dev/null || echo '?') · model $model · log: $wlog"
}

case "$cmd" in
  start)
    [ -f "$state" ] && { echo "ERROR: run $n already has state — use resume/status, or pick a new N" >&2; exit 4; }
    scope="${3:-}"
    [ "${SENSERUN_DRY:-0}" = "1" ] || "$ENGINE/phase-mark.sh" init "$n"
    prompt="You are the SenseRun worker for SystemsBench. Execute SenseRun #$n.
Read and follow engine/SENSERUN-WORKER.md in this directory EXACTLY — it binds you to
SystemsBenchEngine.MD (the governance; you may not alter or bypass it).
$( [ -n "$scope" ] && printf 'Operator scope note for this run: %s\n' "$scope" )Begin at phase SENSE."
    launch_worker "$prompt" fresh
    ;;
  resume)
    [ -f "$state" ] || { echo "ERROR: no state for run $n" >&2; exit 4; }
    worker_alive && { echo "ERROR: worker for run $n is still alive (pid $(cat "$pidf")) — not resuming over it" >&2; exit 5; }
    next="$("$ENGINE/phase-mark.sh" next "$n")"
    [ -z "$next" ] && { echo "Run $n: all phases complete — nothing to resume. Try: verify $n" ; exit 0; }
    prompt="RESUME SenseRun #$n. The previous worker died. Checkpoint says the next incomplete phase is: $next.
Re-read engine/SENSERUN-WORKER.md, re-read your own partial run log and the phase state
(.state/runs/run-$n.json), verify on disk what the completed phases actually produced
(trust disk, not memory), then continue from phase $next. Do not redo completed phases."
    launch_worker "$prompt" resume
    ;;
  status)
    if worker_alive; then echo "worker: ALIVE (pid $(cat "$pidf"))"; else echo "worker: not running"; fi
    "$ENGINE/phase-mark.sh" show "$n" 2>/dev/null || echo "(no phase state for run $n)"
    if [ -f "$wlog" ]; then echo "--- last 15 lines of $wlog:"; tail -15 "$wlog"; fi
    ;;
  abort)
    if worker_alive; then kill "$(cat "$pidf")" 2>/dev/null; echo "worker pid $(cat "$pidf") killed"; fi
    [ -f "$state" ] && "$ENGINE/phase-mark.sh" finish "$n" aborted
    ;;
  verify)
    exec "$ENGINE/verify-run.sh" "$n"
    ;;
  *) sed -n '12,18p' "${BASH_SOURCE[0]}"; exit 1 ;;
esac
