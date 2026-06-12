# SystemsBench — Calibration Gold-Set Protocol

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems** (R&D DAO).
> The rule that makes a jury-graded SystemsBench score *defensible*. Referenced by Structure §5.1, §4.6, §4.2.

**Version:** v0.2 · **Status:** living · accept-rule resolved SenseRun #5 (2026-05-31)
> **RATIFIED: August (trust-delegated 2026-05-31) · Ember (PENDING-COUNTERSIGN).** §3/§4 carry a Meadows-#5 structural rule change (the per-item accept-rule). Reversible until Ember countersigns.

---

## 0. Why this exists (the one-line claim)

A SystemsBench score on an **open format** (`LEV`, `BRIEF`, open parts of `CLD`/`DYN`) is only trustworthy if the LLM-jury that produces it has been **proven to agree with expert humans** on a held-out set *before* it touches the live bank. This document specifies that gold set and the numeric gate. Until the gate is cleared, **open-format dimensions are reported as `UNCALIBRATED — not scored`, never silently averaged into a composite** (the fail-closed rule).

Deterministic formats (`SF`, and any format with an exact oracle) do **not** require this gate — they have no jury.

---

## 1. The gold set — composition

| Property | Requirement |
|---|---|
| **Size** | ≥ 120 items at v1; grows with the bank. |
| **Per-format floor** | ≥ 30 labeled items for *each* open format in active use (`LEV`, `BRIEF`, …). A jury is only certified for formats that clear their floor. |
| **Stratification** | Balanced across difficulty (L1–L4) and ≥ 4 domains, so α is not inflated by easy/homogeneous items. |
| **Sealed split** | 20% of the gold set is **sealed** — never shown to any judge config during tuning. Used once per gate check to detect overfitting of the judge to the visible calibration items. |
| **Date-stamping** | Every gold item carries an authored-on date and a template seed, inheriting the bench's anti-contamination discipline. |

## 2. Labels — what a human rater produces

- Each rater scores the candidate trace on **the exact same A–E anchored rubric the jury uses** (`rubrics/`). No holistic 1–10 — anchored per-dimension only.
- Raters are **blind to model identity** and to each other's labels (independent first pass).
- Each item also gets a **reference solution / gold trace** authored by the item's owner (Ember Seoni or delegate), which the jury will later see (reference-guided judging, Zheng et al. 2023).

## 3. Rater design & adjudication — the per-item acceptance rule

**RATIFIED: August (trust-delegated 2026-05-31) · Ember (PENDING-COUNTERSIGN)**

- **≥ 3 expert raters per item** (systems-thinking literate; Outlier.Systems council or vetted contributors).
- Raters score on the exact A–E anchored sub-criterion rubric (`rubrics/`), at the sub-criterion grain ({0, 0.5, 1.0}), blind and independent.

Acceptance is regime-dependent, because Krippendorff's α is a **set-level estimator** and is un-runnable as a per-item gate at bootstrap N (SenseRun #4: α is undefined when observed disagreement = 0, so perfect-agreement dimensions get *rejected*; and the ordinal-α prevalence paradox lets a 67%-unanimous dimension score below a 33%-unanimous one). The fix splits the gate by what α can honestly measure at the available N.

### 3.1 Bootstrap regime — per-item DUAL acceptance rule (used until a format clears its ≥30-item floor, §1)

For each item, evaluate **per sub-criterion** across the ≥3 raters:

- **(a) Unanimity special-case.** If observed disagreement `Do = 0` (all raters identical on the sub-criterion) → **ACCEPT** that sub-criterion. Perfect agreement is the strongest possible signal; an undefined α must never reject it.
- **(b) Percent-agreement floor.** Otherwise the sub-criterion **ACCEPTS** iff **≥ 2/3 of raters fall within a single contiguous window of ≤ 1 ordinal band** (i.e. at least ⌈2N/3⌉ raters whose scores span ≤ 0.5). With N=3, ≥ 2 raters within one band.
- A sub-criterion that clears **neither** (a) nor (b) is an **AMBIGUOUS ANCHOR** signal — revise the rubric anchor and log it as a self-learning improvement, or retire the item. **Never average away a real disagreement** (preserves the original §3 principle).

A **dimension** is accepted at bootstrap iff *every* sub-criterion under it clears (a) or (b). The accepted human labels are aggregated **median per sub-criterion → mean per dimension** to form the gold label. Any dimension with an unresolved ambiguous-anchor sub-criterion is held `UNCALIBRATED` for that item (§5), not scored.

### 3.2 Set-level regime — α as the reliability estimator (only once a format clears its ≥30-item floor)

Once a format has ≥ 30 accepted gold items (§1), compute **inter-rater Krippendorff's α (ordinal), per dimension, over the whole format set**. The standing human–human α is the **reliability ceiling** reported alongside every judge-certification check (§4). Krippendorff's α is reserved for this set-level use and for judge-vs-human certification (§4) — it is **never** used as a per-item accept gate.

## 4. The gates — item calibration & jury certification

**RATIFIED: August (trust-delegated 2026-05-31) · Ember (PENDING-COUNTERSIGN)**

### 4.0 When an ITEM is CALIBRATED — the quality-spread requirement (Fork 2b)

A single ceiling-anchor label calibrates the judge only at the top of the score range. An item is **CALIBRATED** only when it carries a labeled **quality spread** — three exemplar traces, each independently rater-labeled and each clearing the §3.1 bootstrap acceptance rule:

1. a **CEILING** exemplar (the reference / near-perfect solution),
2. a **MID** exemplar (partially correct — some dimensions strong, some weak), and
3. a **TRAP-FALLING** exemplar (takes the item's counterintuitive bait — e.g. the obvious low-leverage or wrong-direction answer).

An item with fewer than all three labeled exemplars is `PARTIALLY-CALIBRATED` and does not count toward the format's ≥30 floor. This calibrates the judge across the full range it will actually score, not just at the ceiling.

### 4.1 When a JURY config may score the live bank — certification gates

A judge/jury configuration is **certified** for a format only when, on that format's CALIBRATED gold items (visible split, then re-confirmed on the sealed split, §1):

1. **Agreement gate:** Krippendorff's α (judge vs human-gold, ordinal, per dimension) ≥ **0.667**, AND judge–human α is within a reasonable margin of the **human–human α ceiling** from §3.2 (a judge cannot be more reliable than its own gold; report both, always).
2. **Ranking gate:** Kendall's τ ≥ **0.7** between the judge-produced model ranking and a human spot-check ranking on a small model panel. (Per-item agreement and rank-preservation are different failures; we gate on both.)
3. **Sealed-split confirmation:** the agreement gate must also hold on the 20% sealed split (drop ≤ 0.05 α). A large visible-vs-sealed gap = the judge overfit the calibration set → not certified.

If **any** gate fails → the jury is **not certified** for that format → fail-closed (§5).

## 5. The fail-closed rule (non-negotiable)

- If a format's jury is **uncertified**, every report card shows that format's dimensions as **`UNCALIBRATED — not scored`**.
- An uncalibrated dimension is **never** imputed, defaulted, or averaged into the composite. The composite is reported over calibrated dimensions only, with an explicit `coverage: {calibrated dims}` field.
- A bare scalar is never emitted under any circumstance (Structure §4.2). A card that hides calibration status is a defect.

## 6. Rotation & drift (the living part)

- **Re-check cadence:** re-run the gate whenever (a) the rubric anchors change, (b) the judge model/config changes, or (c) every evolution cadence tick regardless (Structure §8.3).
- **Drift alarm:** if a previously-certified jury drops below threshold on the standing gold set, auto-decertify that format (fall back to `UNCALIBRATED`) and open a BACKLOG item. This is the `CALIBRATE` step's auto-rollback (Structure §7, step 7).
- **Gold-set refresh:** rotate in fresh date-stamped items as the bank grows; retire saturated/low-discrimination items per IRT.

## 7. Roles

- **Ember Seoni** — owns rubric anchors, adjudicates anchor revisions when inter-rater α is low, certifies jury configs.
- **August Domanchuk** — product gate; approves threshold changes (the thresholds here are *rules of the system* — Meadows #5 — and changing them changes the whole benchmark's meaning).
- **Outlier.Systems council** — the expert rater pool.
- **Davara (EI)** — runs the computation each SenseRun, logs α/τ deltas, fires the drift alarm.

## 8. Source lineage

Zheng et al. 2023 (LLM-as-judge agreement vs human ceiling); Verga et al. 2024 "Replacing Judges with Juries" (panels reduce intra-family bias); Kim et al. "Prometheus" 2024 (anchored reference-guided absolute grading); Krippendorff (α for multi-rater ordinal/missing data); Kendall (τ rank correlation). See `SystemsBenchResearch.MD` for the full ledger.
