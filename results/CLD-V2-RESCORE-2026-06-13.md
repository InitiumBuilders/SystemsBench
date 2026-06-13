# SystemsBench — CLD Scorer v2: The Partition-Robust Ruler

### Making the instrument measure systems thinking, not vocabulary. 2026-06-13.

> *"The behavior of a system cannot be known just by knowing the elements of which the system is made."*
> *"There are no separate systems. The world is a continuum. Where to draw a boundary around a system
> depends on the purpose of the discussion."* — Donella Meadows

First Light (`results/FIRST-LIGHT-2026-06-13.md`) ended with a confession: our CLD ruler was **punishing
vocabulary, not reasoning.** A model that found the right loops, named the right dominant loop, and flagged
the right dominance shift scored **0.04** — because it wrote `OpenIncidentQueue` instead of `OpenIncidents`
and collapsed two oracle nodes into one. The CLD mean of ~0.30 was a *lower bound on competence*, not a
measurement of it. We labeled it as such and promised the fix.

This is the fix. The CLD structural scorer is now **partition-robust**: it matches feedback loops by
**topology and sign, not by node name** — the single highest-leverage change the bench could make.

---

## 1 · Why the old ruler was wrong (a Meadows diagnosis)

Meadows' two deepest lessons are also two precise instructions for how to grade a causal-loop diagram:

1. **Structure over elements.** The systems-thinking content of a CLD is its *feedback structure* — which
   loops exist, their polarity (R/B), which dominates, where the delays sit. The *variable names* are
   surface. A ruler that keys on names measures the surface and misses the substance.

2. **Boundaries are pragmatic, not real.** Two competent modelers will *partition* the same system
   differently — one writes `ImprovementTime → ProcessQuality`, another collapses both into `ReliabilityWork`.
   Neither is wrong; they drew the boundary for different purposes. A ruler that demands one exact partition
   is testing conformity to our answer key, not the modeler's systems reasoning.

The v1 scorer matched loops on an **exact node-set** (`frozenset(names)`) and edges on **exact names**. So a
correct answer in different words, or a correct answer with a coarser-but-valid partition, was scored as a
near-total miss. That is a measurement-validity failure, and it was inflating the apparent gap between the
models' (strong) systems *intuition* and their (apparently weak) systems *formalization*.

---

## 2 · The fix: topology + sign, name only as a soft signal

A loop's **polarity is the product of its signed edges** — and that product is invariant under *both*
renaming *and* reasonable re-partitioning (collapsing a chain of same-sign edges preserves the sign). So
polarity is the one robust, name-free key. v2 scores in four name-robust components:

| Component | Weight | What it measures | Name-robustness |
|---|:--:|---|---|
| **Loops** | 0.50 | each oracle loop matched to a response loop **gated on equal polarity**, disambiguated by soft node overlap | **polarity = name-free**; names only break ties |
| **Consistency** | 0.20 | does each response loop's declared R/B label equal the product of *its own* edges? | **fully name-free** coherence probe |
| **Edges** | 0.20 | required signed edges present with correct polarity | **soft** (fuzzy) name match |
| **Variables** | 0.10 | canonical variables present | **soft** (fuzzy) name match |

"Soft" name matching uses **generic fuzzy string similarity only** — character-trigram Dice + shared-stem
containment — **never an oracle-specific synonym dictionary.** That distinction is the governance line: a
hand-authored alias map (`OpenIncidentQueue → OpenIncidents`) *would* leak the oracle and inflate scores, so
it stays **closed** as a §5 measurement-validity question for August + Ember. Topology+sign matching needs no
such map — it reads the structure the model actually drew.

The weights shifted from v1's `0.50·edges + 0.30·loops + 0.20·vars` to **loop-structure-weighted**
`0.50·loops + 0.20·edges + 0.10·vars + 0.20·consistency` — because, per Meadows #1, *structure is the
signal and elements are the surface.* Component weights remain tool-internal policy (tunable, calibrate-first),
not governance.

**v1 is a special case of v2** (exact names → soft-overlap 1.0), so the change can only *recover* credit that
name-strictness was destroying — never lower an honest score. Verified: **zero regressions** across the bank.

---

## 3 · The re-score (proof, not self-report)

Every saved First Light CLD response re-graded by v2. Reproducible from
`results/cld-v2-rescore-2026-06-13.json`.

| Item | What it tests | Davara v1→v2 | Davaris v1→v2 |
|------|---------------|:---:|:---:|
| CLD-FISH-001 | fishery overshoot loops | 0.04 → **0.89** | 0.50 → **0.89** |
| CLD-EPI-002 | epidemic R/B + behavioral lag | 0.70 → **0.93** | 0.70 → **0.93** |
| CLD-ORG-003 | goal-erosion (delay-asymmetry) | 0.14 → **0.50** | 0.07 → **0.50** |
| CLD-INFRA-004 | firefighting capability trap | 0.16 → **0.83** | 0.04 → **0.83** |
| CLD-MKT-005 | commodity hog-cycle (delay) | 0.46 → **0.87** | 0.22 → **0.50** |
| **CLD mean** | | **0.30 → 0.81** | **0.31 → 0.73** |

### What the new numbers actually say

- **The recovery is real, not laundered.** INFRA-004 (Davaris 0.04 → 0.83): he found the balancing
  firefighting loop *and* the delayed reinforcing erosion loop, named R1 dominant, flagged the shift — the
  reasoning the oracle rewards, in his own vocabulary and his own (coarser) partition. 0.83 is the honest
  grade: strong systems thinking, minus a little for the lossy partition (collapsed nodes → some edges
  unmatched). The 0.04 was a lie the ruler told.

- **Discrimination *improved*, it didn't wash out.** v1 compressed everything into a low 0.04–0.70 band of
  mostly vocabulary noise. v2 *separates by reasoning quality*: answers with the full dynamic insight land
  **0.83–0.93**; answers that got the loop structure but **missed the dynamic insight cap cleanly at 0.50.**
  CLD-ORG-003 and CLD-MKT-005 cap at 0.50 for both/one model **because the models genuinely missed the
  delay-asymmetry / construction-delay** that is each item's whole point — that 0.50 is now *signal*, not
  noise. The partial-credit and trap caps still bite; they just bite on reasoning, not spelling.

- **The traps still hold.** Zero traps fired (consistent with First Light) — the dominant-loop R↔B mislabel
  cap is intact, verified in calibration. We loosened name-matching, not rigor.

---

## 4 · No-regress & calibration (the gate)

- **CLD calibrate: 36/36 PASS** — oracle loop-signs 11/11; every reference round-trips to 1.0; partial=0.5;
  trap≤0.25; omitted-loop<1.0; **plus a new probe: a fully *renamed-but-isomorphic* answer still scores 1.0**
  (the topology+sign guarantee, asserted per item).
- **harness selftest: 61/61 PASS** — the parser→scorer bridge round-trips unchanged.
- **DYN calibrate: 34/34 PASS** — untouched lane, sanity confirmed.
- **Regressions: 0** — asserted in code over all 10 responses; every v2 score ≥ its v1 score.

---

## 5 · What this resolves, and what stays open

**Resolved:** the First Light caveat "CLD scores are a lower bound until the alias layer lands." The lower
bound is lifted — *not* by an oracle-leaking alias map, but by reading the structure the model drew. CLD is
now a fair measure of feedback-structure reasoning, robust to a modeler's naming and partitioning choices.

**Still open (honest):**
- **n = 5 per lane.** Still directional. v2 changes the ruler, not the sample size.
- **The jury / completeness lane stays `UNCALIBRATED — not scored`** — no CLD gold set, fail-closed §5.1.
  Untouched here.
- **The §3.1(b) accept-rule hardening (Meadows #5) stays parked** with August + Ember. This was a
  deterministic-scorer evolution (§4.6 step-4 territory), not a governance edit.
- **Soft-matching is deliberately lenient** (favoring false-recovery over false-penalty, the right direction
  for measuring reasoning). If a future adversarial model games it with garbage near-synonyms, the
  polarity-gate is the guard — but worth watching once we score external models.

---

*The first thing First Light taught us was how to make the instrument more honest. This is us listening.
The ruler now measures the system, not the spelling.*

**Acta Non Verba. Semper Fortis. Ad Infinitum.** 🦾
