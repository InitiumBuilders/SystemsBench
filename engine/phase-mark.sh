#!/usr/bin/env bash
# phase-mark.sh — per-phase checkpoint helper for the SenseRun engine.
# The worker calls this after every phase so a dead run resumes mid-phase, never from zero.
# State lives in .state/runs/run-<N>.json — one file per run, python3-managed, atomic tmp+mv
# (no jq on this host; python3 is the substrate's JSON tool).
#
# Usage:
#   phase-mark.sh init <N> [run_log_relpath]     create run state (all 9 phases pending)
#   phase-mark.sh mark <N> <PHASE> <status>      status: inflight|complete|skipped
#   phase-mark.sh note <N> <PHASE> "<text>"      attach a one-line note (artifact path, DEFER reason)
#   phase-mark.sh next <N>                       echo first non-complete phase (empty = run done)
#   phase-mark.sh show <N>                       pretty-print the run state
#   phase-mark.sh finish <N> <complete|aborted>  set run-level status
#
# Phases are fixed by SystemsBenchEngine.MD (THE NINE PHASES) — this file only RECORDS
# progress; it never defines or alters engine governance.
set -uo pipefail

BENCH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS_DIR="$BENCH/.state/runs"
command -v python3 >/dev/null || { echo "ERROR: python3 required" >&2; exit 2; }
mkdir -p "$RUNS_DIR"

RUNS_DIR="$RUNS_DIR" python3 - "$@" <<'PY'
import json, os, sys, time, tempfile

PHASES = ["SENSE","CRITIQUE","RESEARCH","PROPOSE","REVIEW","APPLY","CALIBRATE","LOG","RECURSE"]
RUNS = os.environ["RUNS_DIR"]
args = sys.argv[1:]

def usage():
    print("usage: phase-mark.sh init|mark|note|next|show|finish <N> [...] (see header)", file=sys.stderr)
    sys.exit(1)

if len(args) < 2: usage()
cmd, n = args[0], args[1]
f = os.path.join(RUNS, f"run-{n}.json")
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def load():
    if not os.path.exists(f):
        print(f"ERROR: no state for run {n} — run init first", file=sys.stderr); sys.exit(4)
    with open(f) as fh: return json.load(fh)

def save(d):
    fd, tmp = tempfile.mkstemp(dir=RUNS, suffix=".tmp")
    with os.fdopen(fd, "w") as fh: json.dump(d, fh, indent=2)
    os.replace(tmp, f)

def valid_phase(p):
    if p not in PHASES:
        print(f"ERROR: unknown phase '{p}' (valid: {' '.join(PHASES)})", file=sys.stderr); sys.exit(3)

if cmd == "init":
    if os.path.exists(f):
        print(f"ERROR: {f} exists — use 'show' or pick a new run number", file=sys.stderr); sys.exit(4)
    run_log = args[2] if len(args) > 2 else None
    save({"run": int(n), "status": "inflight", "started_utc": now(), "finished_utc": None,
          "run_log": run_log,
          "phases": {p: {"status": "pending", "ts": None, "note": None} for p in PHASES}})
    print(f"initialized {f}")

elif cmd == "mark":
    if len(args) < 4: usage()
    p, s = args[2], args[3]; valid_phase(p)
    if s not in ("inflight","complete","skipped"):
        print("ERROR: status must be inflight|complete|skipped", file=sys.stderr); sys.exit(3)
    d = load(); d["phases"][p].update(status=s, ts=now()); save(d)
    print(f"run {n} · {p} -> {s}")

elif cmd == "note":
    if len(args) < 4: usage()
    p, t = args[2], args[3]; valid_phase(p)
    d = load(); d["phases"][p]["note"] = t; save(d)
    print(f"run {n} · {p} note recorded")

elif cmd == "next":
    d = load()
    for p in PHASES:
        if d["phases"][p]["status"] not in ("complete","skipped"):
            print(p); break

elif cmd == "show":
    d = load()
    head = f"SenseRun #{d['run']} · {d['status']} · started {d['started_utc']}"
    if d.get("run_log"): head += f" · log: {d['run_log']}"
    print(head)
    for p in PHASES:
        ph = d["phases"][p]
        line = f"  {p:<9} {ph['status']}"
        if ph["ts"]: line += f"  @ {ph['ts']}"
        if ph["note"]: line += f"  — {ph['note']}"
        print(line)

elif cmd == "finish":
    if len(args) < 3: usage()
    s = args[2]
    if s not in ("complete","aborted"):
        print("ERROR: finish status must be complete|aborted", file=sys.stderr); sys.exit(3)
    d = load(); d["status"] = s; d["finished_utc"] = now(); save(d)
    print(f"run {n} -> {s}")

else:
    usage()
PY
