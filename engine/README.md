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

## Quick use

```bash
engine/senserun.sh start 7 "optional scope note"   # launch SenseRun #7 detached
engine/senserun.sh status 7                        # phases + worker liveness + log tail
engine/senserun.sh resume 7                        # after any death: continues at next incomplete phase
engine/senserun.sh verify 7                        # proof, not self-report
```

Crash recovery is two-layer: phase state + incremental run log (coarse), `--resume <session>`
(fine — the worker's actual conversation context). A dead run resumes mid-phase, never from zero.

Reversibility is a property, not a promise: every APPLY = its own commit (`apply-commit.sh`),
every rollback = a clean revert of exactly that commit (`rollback-run.sh <N>`).

Governance note: the engine cannot self-apply structural (Meadows #5) changes — the worker
contract forces DEFER → August + Ember, exactly per the Engine doc. Infrastructure only.
