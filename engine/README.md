# engine/ — the executable SenseRun engine

Built 2026-06-11 (Phase 2 of the SystemsBench infrastructure build). Turns THE SENSERUN RITUAL
(`../SystemsBenchEngine.MD` — the governance, untouched) from a conversational procedure into
a runnable, crash-proof, self-verifying detached job.

| File | Role |
|---|---|
| `senserun.sh` | Launcher: `start / resume / status / abort / verify`. Runs the worker as a detached `claude -p` job — subscription rail, API key stripped, model pin read live from the runner. |
| `SENSERUN-WORKER.md` | The worker's execution contract: checkpoint every phase, write artifacts incrementally, defer structural changes, fail closed, verify before done. Points to the Engine doc for ALL governance. |
| `phase-mark.sh` | Per-phase checkpoint state in `.state/runs/run-<N>.json` (atomic python3 writes — no jq on this host). |
| `verify-run.sh` | Read-only proof pass: phases complete, run-log blocks present, scorecard, engine-state consistency, CHANGELOG on APPLY. Exit 0 = verified. |
| `apply-commit.sh` | Phase 3: seals an APPLY as **one git commit** (enhancement only — runtime records excluded), records the hash in run state. Local only, never pushes. |
| `rollback-run.sh` | Phase 3: reverts **exactly** the run's APPLY commit + writes the rollback CHANGELOG entry in one atomic commit. Refuses dirty trees, foreign commits, conflicts. |
| `jury.sh` | Phase 4: blind N-rater jury. Each rater = an independent, context-isolated `claude -p` session (no tools) seeing ONLY persona + item + rubric + response. `score / status / collect`. Raters are SYNTHETIC — evidence labels, never certification (§3 needs humans). |
| `jury-stats.py` | Phase 4: extraction + aggregation math — median-per-sub → mean-per-dim, ordinal Krippendorff α, the §3.1 accept-rule, and dry-run simulations of the three Future-§6.1 hardening forks. `calibrate` self-tests against the recorded gold arithmetic (18 checks) before any live run is trusted. |
| `personas/R1–R5.md` | The jury bench: R1–R3 transcribed from the recorded N=3 baseline personas; R4 (lean/flow practitioner) + R5 (psychometrics literalist) new and orthogonal. |

## Quick use

```bash
engine/senserun.sh start 7 "optional scope note"   # launch SenseRun #7 detached
engine/senserun.sh status 7                        # phases + worker liveness + log tail
engine/senserun.sh resume 7                        # after any death: continues at next incomplete phase
engine/senserun.sh verify 7                        # proof, not self-report

engine/jury.sh score items/<item>.md <response.txt> <outdir> 5   # 5 blind raters, detached
engine/jury.sh collect <outdir>                                  # rc=0 iff all rater JSON parses clean
python3 engine/jury-stats.py report <baseline.json> <c> <m> <t>  # N-vs-N agreement report
```

Crash recovery is two-layer: phase state + incremental run log (coarse), `--resume <session>`
(fine — the worker's actual conversation context). A dead run resumes mid-phase, never from zero.

Reversibility is a property, not a promise: every APPLY = its own commit (`apply-commit.sh`),
every rollback = a clean revert of exactly that commit (`rollback-run.sh <N>`).

Governance note: the engine cannot self-apply structural (Meadows #5) changes — the worker
contract forces DEFER → August + Ember, exactly per the Engine doc. Infrastructure only.
