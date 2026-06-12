#!/usr/bin/env bash
# jury.sh — blind N-rater jury for SystemsBench open-format responses.
#
# INFRASTRUCTURE + EVIDENCE ONLY: this script changes no governance. The §3.1 accept-rule
# and all calibration gates live in protocols/CALIBRATION_GOLDSET.md and are NOT touched
# here — jury outputs are EVIDENCE for ratification decisions, never rulings.
#
# Each rater is an INDEPENDENT, CONTEXT-ISOLATED `claude -p` call: its own fresh session,
# no tools, no shared context. A rater sees ONLY: its persona + the item (prompt +
# reference solution) + the anchored rubric + the candidate response. It never sees other
# raters, prior scores, gold labels, or the response's tier/identity.
#
# HONEST LABELING: raters launched by this script are SYNTHETIC (AI personas). Their
# labels are dry-run/evidence labels. §3 still requires >=3 real human raters before any
# certification; outputs of this script must never be presented as human-council labels.
#
# Usage:
#   jury.sh score <item.md> <response.txt> <outdir> [N]   launch N blind raters (default 5)
#   jury.sh status <outdir>                               liveness + which raters finished
#   jury.sh collect <outdir>                              extract+validate JSONs (rc=0 iff all parse)
#
# Env:
#   JURY_MODEL=...       model pin (default: engine/local.env wiring, else claude-opus-4-7)
#   JURY_MAX_TURNS=4     rater turn budget (pure text scoring task)
#   JURY_DRY=1           print launch commands instead of executing
#
# Subscription rail only — API key stripped at launch. Host wiring lives in engine/local.env
# (untracked); tracked files stay host-agnostic.
set -uo pipefail

ENGINE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCH="$(cd "$ENGINE/.." && pwd)"
RUBRIC="$BENCH/rubrics/DIMENSION_RUBRICS.md"
PERSONAS="$ENGINE/personas"
[ -f "$ENGINE/local.env" ] && . "$ENGINE/local.env"
unset ANTHROPIC_API_KEY || true

cmd="${1:-}"
usage() { sed -n '20,23p' "${BASH_SOURCE[0]}"; exit 1; }

resolve_model() { echo "${JURY_MODEL:-${SENSERUN_MODEL:-claude-opus-4-7}}"; }

build_prompt() { # build_prompt <persona-file> <rater-id> <item-file> <response-file>
  local persona="$1" rid="$2" item="$3" resp="$4"
  cat "$persona"
  cat <<'HDR'

---

You are scoring ONE candidate response to ONE SystemsBench item against an anchored rubric.

BLINDNESS CONTRACT: you see only the item, the rubric, and the candidate response below.
You have no knowledge of who or what produced the response, how good it is "supposed" to
be, or how anyone else scored it. Judge only the text against the anchors. Do not use any
tools — everything you need is in this message.

=== ITEM (prompt + reference solution; read the reference FIRST) ===
HDR
  cat "$item"
  printf '\n=== RUBRIC (anchored; score each sub-criterion on {0, 0.5, 1.0}) ===\n'
  cat "$RUBRIC"
  printf '\n=== CANDIDATE RESPONSE (the ONLY text you are scoring) ===\n'
  cat "$resp"
  cat <<EOF

=== OUTPUT CONTRACT ===
Reason carefully first, privately. Then output ONLY a single JSON object — no markdown
fences, no commentary before or after — with exactly this shape:
{"rater":"$rid","scores":{"A1":0.0,"A2":0.0,"A3":0.0,"A4":0.0,"B1":0.0,"B2":0.0,"C1":0.0,"C2":0.0,"C3":0.0,"C4":0.0,"C5":0.0,"D1":0.0,"D2":0.0,"D3":0.0,"E1":0.0,"E2":0.0,"E3":0.0},"improvement":"one sentence: the single highest-leverage improvement for this answer"}
Every score must be exactly 0, 0.5, or 1.0 per the rubric anchors.
EOF
}

case "$cmd" in
  score)
    item="${2:-}"; resp="${3:-}"; outdir="${4:-}"; n="${5:-5}"
    [ -f "$item" ] && [ -f "$resp" ] && [ -n "$outdir" ] || usage
    mkdir -p "$outdir"
    model="$(resolve_model)"; turns="${JURY_MAX_TURNS:-4}"
    for k in $(seq 1 "$n"); do
      persona="$PERSONAS/R$k.md"
      [ -f "$persona" ] || { echo "ERROR: missing persona $persona" >&2; exit 3; }
      pfile="$outdir/R$k.prompt"
      build_prompt "$persona" "R$k" "$item" "$resp" > "$pfile"
      sid="$(uuidgen 2>/dev/null || cat /proc/sys/kernel/random/uuid)"
      if [ "${JURY_DRY:-0}" = "1" ]; then
        echo "DRY-RUN R$k: claude -p --session-id $sid --model $model --max-turns $turns < $pfile > $outdir/R$k.out"
        continue
      fi
      ( cd "$BENCH" && nohup claude -p --session-id "$sid" --model "$model" \
          --max-turns "$turns" < "$pfile" > "$outdir/R$k.out" 2> "$outdir/R$k.err" \
          & echo $! > "$outdir/R$k.pid" )
      echo "rater R$k launched · pid $(cat "$outdir/R$k.pid") · model $model"
    done
    ;;
  status)
    outdir="${2:-}"; [ -n "$outdir" ] || usage
    for p in "$outdir"/R*.pid; do
      [ -f "$p" ] || continue
      k="$(basename "$p" .pid)"
      if kill -0 "$(cat "$p")" 2>/dev/null; then st="RUNNING"
      elif [ -s "$outdir/$k.out" ]; then st="FINISHED ($(wc -c < "$outdir/$k.out") bytes)"
      else st="DEAD (empty output)"; fi
      echo "$k: $st"
    done
    ;;
  collect)
    outdir="${2:-}"; [ -n "$outdir" ] || usage
    exec python3 "$ENGINE/jury-stats.py" collect "$outdir"
    ;;
  *) usage ;;
esac
