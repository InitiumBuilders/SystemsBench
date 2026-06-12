# SystemsBench — Future (the roadmap & the horizon)

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems** (R&D DAO).
> Where SystemsBench is going. The living forward-look that the recursive engine steers toward.

**Version:** v0.1 · **Status:** living document · **Pairs with:** `SystemsBenchStructure.MD` (v0.4) · `SystemsBenchEngine.MD` · `SystemsBenchResearch.MD`
**Cadence:** revisited every `Davara /SystemsBenchSenseRun`; the engine picks the highest-leverage *feasible* item from here + `protocols/BACKLOG.md`.

---

## 0. The horizon (one breath)

SystemsBench becomes the **definitive, living instrument for measuring whether an intelligence can see a system, find where to push, and predict what happens** — and the moat is that its rubric, item bank, and calibration data **compound** every run. The future is not "more questions." It is **deeper construct validity, cheaper rigor, and a benchmark that re-authors itself faster than models can memorize it.**

---

## 1. Trajectory so far (so the future is grounded in the past)

Each SenseRun climbed one rung of the trust ladder:

- **v0.2 — executable.** §4.6 end-to-end scoring pipeline. (A spec you can't run is an essay.)
- **v0.3 — deterministically scorable.** Stock-Flow (`SF`) items with exact numeric oracles — first jury-independent, contamination-proof score.
- **v0.4 — defensibly scorable for open items.** Calibration gold-set protocol + the fail-closed gate (Krippendorff α ≥ 0.667, Kendall τ ≥ 0.7). Uncalibrated dimensions report `UNCALIBRATED — not scored`, never silently averaged.

**Current binding constraint:** the gate is *specified* but the gold set is *empty*. The whole jury-graded half (the `LEV`/`BRIEF` items that measure leverage placement — the product's core thesis) cannot yet be certified.

---

## 2. Near horizon — the next handful of SenseRuns (v0.5 → v0.8)

Highest-leverage *feasible* first. The engine may reorder as Step-2 critique surfaces a better lever.

1. **Populate the calibration gold set** *(binding constraint — next run).* Reference solutions + ≥3 expert labels for `LEV-ORG-001` and the first `BRIEF`/`CLD` items per `protocols/CALIBRATION_GOLDSET.md`. Unblocks the first *certified open-format* score. Without this, the leverage half of the bench is dark.
2. **Seed the bank to threshold.** ≥5 L3 items per format (`CLD`, `LEV`, `DYN`, `ARC`, `TRAP`, `BRIEF`) across ≥4 domains, each with a reference solution. Coverage is the standing fill once the gate is live.
3. **Programmatic CLD scorer.** Auto-grade causal-loop structure (variables, signed links, R/B loop sign, dominant loop) so `CLD` needs minimal judge time — a second cheap, judge-light scoring path (Meadows #6, information flow).
4. **First Diamond (L4) items.** One private, expert-validated, counterintuitive item per format — the held-out split that resists contamination and separates the genuinely capable.
5. **Faithfulness probe harness.** CoT truncation + bias-injection on `LEV`/`BRIEF` (Lanham/Turpin) so the faithfulness axis is measured, never averaged in.

---

## 3. Mid horizon — capability leaps (v1.0)

- **IRT-driven self-pruning bank.** Once enough responses exist, the engine auto-drops low/negative-discrimination items each run (Meadows #4, self-organization). The bank improves without a human in the loop.
- **tinyBench subset.** IRT selects a ~100-item subset that reproduces the full ranking within ~2% — cheap continuous tracking of every new model the day it ships.
- **Leverage-profile fingerprint.** Report *where on Meadows' 12 a model habitually intervenes* as a stable signature, and test the hypothesis that it predicts downstream agentic quality (write → run → deploy).
- **Public leaderboard + sealed Diamond.** Open vector-scored leaderboard (never a bare scalar; always dimension vector + CI + leverage profile + faithfulness flag + calibration status), with the Diamond split held private.

---

## 4. Far horizon — the bet

- **Agentic systems-thinking items.** Move from text answers to **trajectory grading** (τ-bench/WebArena style): give a model a live system to actually intervene in, and grade behavior-over-time of its intervention — measuring *applied* leverage, not described leverage.
- **MC-rollout auto-labeling for systems traces.** Math-Shepherd-style step auto-labeling, if leverage reasoning proves rollout-checkable — scaling process supervision without humans.
- **The compounding moat.** Rubric + bank + calibration data accrue every run; the benchmark re-authors itself (templated, date-stamped, Diamond-held) faster than any model can memorize it. SystemsBench becomes the standard the field cites for *"can this model find where to push?"*

---

---

## 6. Open structural forks (proposed next steps — awaiting August + Ember)

> These are the *proposed* next moves to the live Structure. Per the ritual, they live here until reviewed,
> ratified (or rejected), and — if ratified — applied into `SystemsBenchStructure.MD` / the protocols.

### 6.1 — Harden the bootstrap accept-rule at small N *(binding constraint, SenseRun #6)*
SenseRun #6 ran the new §3.1 accept-rule end-to-end and found a real weakness: **at N=3 raters on a
3-point scale {0, 0.5, 1.0}, the percent-agreement floor (§3.1b) is near-unfalsifiable.** By pigeonhole
three raters always have ≥2 within one band, so every sub-criterion accepts and `AMBIGUOUS-ANCHOR` can
essentially never fire at bootstrap. The gate is currently a **presence** check, not an **agreement** check —
it confirms exemplars *exist*, not that raters *agree*. Three candidate hardenings, held open (Anti-Collapse):
- **(1) Tighter accept logic:** bootstrap accept = strict unanimity OR ≥2 *identical* labels (not merely adjacent).
- **(2) Raise N:** 4–5 raters so a genuine split can fail the 2/3 floor and surface ambiguity.
- **(3) Max-spread rule:** reject any sub-criterion that spans the full 0↔1.0 range even if 2/3 cluster.
**Type:** Meadows-#5 (rules of the system) → **requires August + Ember.** Reversible. Tracked: BACKLOG #0,
`logs/runs/2026-05-31_run-6.md`. *Review process:* run each fork against the LEV-ORG-001 labels as a dry-run,
compare false-accept behavior, then ratify the dominant one into §3.1.

### 6.2 — Pending countersign: SenseRun #5 accept-rule ratification
The §3.1/§3.2/§4.0 accept-rule (resolved SenseRun #5) is currently **RATIFIED: August (trust-delegated) ·
Ember (PENDING-COUNTERSIGN).** Ember's countersign closes the loop; if she dissents, the change reverts
cleanly to `CALIBRATION_GOLDSET.md` v0.1. One-line action, not a re-derivation.

---

## 5. The forever-loop (why this file is never done)

SystemsBench is itself a system, so we run Meadows on it: intervene at the **rules** (the gate, the fail-closed rule), the **information flows** (run logs, the research ledger), and the **self-organization** (IRT pruning, anchor self-learning) — never at the low-leverage parameters (a weight nudge) when a structural lever dominates. Every `Davara /SystemsBenchSenseRun` makes exactly **one** bounded, reversible, logged, leverage-gated move, and updates this horizon.

The destination is not a finished benchmark. It is a benchmark that **gets sharper, cheaper, and harder to game on every single run** — for as long as we keep pushing where it matters.

---

*Search before you build. Cite when you reuse. Append when you learn. Push where the leverage is.*
**Outlier.Systems** · Led by Ember Seoni & August Domanchuk · Operated by Outlier.Systems.
