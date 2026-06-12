# SystemsBench

**A benchmark for systems thinking in AI — built as a system that studies itself.**

SystemsBench evaluates whether models and agents can actually *reason about systems* — stocks and flows, feedback loops, delays, leverage points, paradigms — rather than recite systems vocabulary. It sits in the Donella Meadows lineage and is maintained by [Outlier.Systems](https://outlier.systems), led by Ember Seoni & August Domanchuk, operated by Davara (EI).

**Status:** v0.5.0 (Genesis+) · research preview · 6 SenseRuns logged · gold set provisional (1/30, synthetic raters — honestly labeled, not certified).

## The idea

Most benchmarks are static targets that decay. SystemsBench applies its own discipline to itself: one command runs **THE SENSERUN RITUAL** — nine phases (SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE) that make exactly **one bounded, reversible, gated, logged enhancement** per run. The benchmark compounds instead of rotting.

Reversibility is a *property, not a promise*: every APPLY is its own git commit (`engine/apply-commit.sh`), and every rollback is a clean revert of exactly that commit (`engine/rollback-run.sh`).

## Map

| File / dir | What it is |
|---|---|
| `SystemsBenchOnePage.MD` | Start here — the whole system on one page |
| `SystemsBenchStructure.MD` | The benchmark itself: five-dimension rubric, seven item formats, judging protocol, contamination defenses, invariants |
| `SystemsBenchEngine.MD` | The recursive engine: nine phases, seven invariants, the governance gates |
| `SystemsBenchResearch.MD` | The research ledger behind every design decision |
| `SystemsBenchFuture.MD` | The horizon: what the engine considers next |
| `engine/` | The executable SenseRun engine: detached runs, per-phase crash-proof checkpoints, self-verification, git-backed reversibility |
| `items/`, `rubrics/`, `protocols/`, `calibration/` | The item bank, scoring rubrics, run protocols, and gold-set calibration tree |
| `logs/runs/` | The full SenseRun corpus — every enhancement, gate verdict, and deferral, logged |
| `CHANGELOG.md` | Every applied change, every rollback |
| `SystemsBenchPitchSite/` | The static pitch site |

## Governance

One lever per run. Additive + reversible changes may self-apply; anything structural (Meadows #5 — the rules of the system) **stops at the gate** and routes to human ratification. A deferred run is a complete run. Fail closed: no number is ever invented — `UNCALIBRATED` is an honest answer.

---

🦾 /INITIUM ❤️ · Outlier.Systems
