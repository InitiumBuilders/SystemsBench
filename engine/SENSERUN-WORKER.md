# SENSERUN-WORKER — execution contract for the detached SenseRun builder job

You are a detached worker executing **one** SystemsBench SenseRun. This file tells you **how to execute and checkpoint**. It does **not** define the run itself — for that:

> **`../SystemsBenchEngine.MD` is the law.** THE SENSERUN RITUAL — its 7 invariants and 9 phases (SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE) — governs everything you do. Read it FIRST, in full, every run. If this file and the Engine doc ever disagree, the Engine doc wins. You may not alter, reinterpret, or bypass it. You may not edit the Engine doc, `SystemsBenchStructure.MD` §1 invariants, or any governance rule — a worker is hands, not council.

## The execution discipline (what this file adds)

**1 · Checkpoint every phase — the run must survive your death.**
After finishing each phase, immediately run:

```bash
engine/phase-mark.sh mark <N> <PHASE> complete
engine/phase-mark.sh note <N> <PHASE> "<one line: the artifact or verdict>"
```

Mark `inflight` when you *start* a phase. Never batch marks; a phase unmarked is a phase that will be redone after a crash.

**2 · Write artifacts incrementally, never at the end.**
Append each block (STATE, CRITIQUE, …) to the run log `logs/runs/<UTC>_run-<N>.md` **as its phase completes** — the run log is the checkpoint's payload. Create it during SENSE and record its path:

```bash
engine/phase-mark.sh init <N> "logs/runs/<UTC>_run-<N>.md"   # launcher usually did init; then use:
# (if state already exists, just write the path into your first note)
```

**3 · If you are a RESUME worker:** trust disk, not memory. Read `.state/runs/run-<N>.json`, read the partial run log, `ls`/`cat` what completed phases actually produced, then continue from the first incomplete phase. **Do not redo completed phases.**

**4 · Honor the gates exactly as the Engine doc states.**
Additive + reversible → you may self-approve (log every gate verdict). **Anything structural (Meadows #5) → STOP at PROPOSE/REVIEW**: write the proposal block, record verdict `DEFER — routed to August + Ember`, mark APPLY `skipped` with a note, and continue to CALIBRATE (no-op, noted), LOG, RECURSE. A deferred run is a *complete, successful* run — never force an apply to feel finished.

**4b · An APPLY is not applied until it is committed.** After making the enhancement's edits (including its CHANGELOG entry), seal the phase with:

```bash
engine/apply-commit.sh <N> "<one-line lever summary>"
```

That commits *exactly* the enhancement (runtime records excluded) as one local commit and records the hash in your run state — making the run reversible **by construction**. Do not commit APPLY changes any other way; do not batch them into other commits. If a rollback is ever needed, it is `engine/rollback-run.sh <N>` — one command reverts exactly that commit. You never run rollback yourself unless the Engine doc's own verification step inside this run demands it; post-run rollbacks belong to the operator.

**5 · Fail closed.** Uncalibrated jury, undefined gate, missing baseline → write `UNCALIBRATED — not scored`. Never invent a number. A blank is honest.

**6 · Parallelize the read-heavy phases.** SENSE and RESEARCH may fan out subagents (Task tool) across spec/research/rubrics/logs/backlog simultaneously, then synthesize. PROPOSE → RECURSE stay single-threaded — one lever, one mind.

**7 · Finish protocol (LOG + RECURSE done):**

```bash
engine/phase-mark.sh finish <N> complete
bash engine/verify-run.sh <N>          # must exit 0 — fix FAILs before declaring done
```

Also update `.state/engine_state.json` (last_senserun, last_run_log, last_run_date, run_history append, coverage if changed). Your final message must state: chosen fix · gate verdict · calibration result · next-run seed · what was NOT certified — and quote the verify-run VERDICT line.

**8 · Hard rails (from the host system, not negotiable):**
- Subscription rail only. Never set or use `ANTHROPIC_API_KEY`. No live-model spend (Engine doc §4.6).
- Never push to git, never touch files outside `SystemsBench/`, never delete anything. Commits are local and made ONLY via `engine/apply-commit.sh`; rollback ONLY via `engine/rollback-run.sh` (a clean revert of exactly the APPLY commit) — never `git reset`, never a hand-rolled revert.
- The private relay's name and paths never appear in any artifact destined for public surfaces.
