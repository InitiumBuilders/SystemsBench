# SystemsBench — Structure & Specification

### The benchmark for high-level systems thinking and leverage.

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems** (R&D DAO).
> A living, recursive, self-improving evaluation engine.

**Version:** v0.5.0 (Genesis+) · **Status:** living document · **Maintainers:** Davara (EI) + Outlier.Systems council
**Cadence:** evolves every `Davara /SystemsBenchSenseRun`. Every change is logged in `/logs/` and `CHANGELOG.md`. Forward-look in `SystemsBenchFuture.MD`.

---

## 0. What SystemsBench is (in one breath)

SystemsBench measures whether a model can **see a system, map its structure, find where to intervene, and predict what happens when it does** — the way Donella Meadows, Jay Forrester, Russell Ackoff, and Peter Senge would. It does not reward fluent verbiage about "synergy." It rewards a demonstrated chain: *map → locate dominant loops → place the intervention on the leverage hierarchy with justification → check direction & feasibility → predict behavior over time → name the side-effects.*

We are measuring a **construct**: **Systems Thinking & Leverage Competence (STLC)** — the capability to identify and understand systems, predict their behavior, and devise high-leverage modifications to produce desired effects (Arnold & Wade, 2015), with leverage graded against Meadows' hierarchy (1999).

**The product thesis:** as models become agents that *act* on the world (write → run → deploy), the scarce, valuable, hard-to-fake capability is not knowledge recall — it is **knowing where to push.** SystemsBench is the instrument that measures that, rigorously and continuously, and a moat because the rubric, the item bank, and the calibration data compound over time.

---

## 1. Design principles (non-negotiable invariants)

These are the load-bearing walls. The recursive engine may evolve everything else, but it must justify any change to these against the principles below.

1. **Construct-first.** Every item and rubric dimension traces to a named construct (a Meadows leverage point, an Arnold-Wade skill, a stock/flow/loop/delay primitive). No orphan questions.
2. **Process over answer.** A correct conclusion reached by wrong reasoning scores low. We grade the *trace* (step-level), not just the verdict — following process-supervision evidence (Lightman et al., "Let's Verify Step by Step," 2023).
3. **Counterintuitivity is the discriminator.** Meadows' core finding: high-leverage points are counterintuitive and often pushed in the *wrong direction*. Items are authored so the obvious answer is low-leverage and the high-leverage answer requires real structural insight. Naming "change the paradigm" as a slogan scores *lower* than correctly justifying a feedback-loop intervention.
4. **Contamination-resistant by construction.** Item templates + a private held-out "Diamond" split + date-stamped, post-cutoff scenarios. We assume memorization and design against it (ARC-AGI, GSM-Symbolic, LiveBench philosophy).
5. **Multi-metric, never one number.** We report a vector (per-dimension), not a scalar, alongside it (HELM philosophy). A single composite exists only for leaderboard convenience and is always shown with error bars.
6. **Calibrated, defensible judging.** LLM-as-judge is a cross-family jury, rubric-anchored, reference-guided, swap-averaged, and validated against a human gold set before use (Zheng et al. 2023; Verga et al. "Replacing Judges with Juries" 2024; Kim et al. "Prometheus" 2024).
7. **Living & recursive.** The benchmark, like the systems it studies, has feedback loops on itself. It refreshes items, re-calibrates judges, prunes dead items via IRT, and improves its own rubric on a cadence. It is never "done."
8. **Anti-Goodhart.** A private metric is held out of any optimization loop. When SystemsBench becomes a target, a held-out variant keeps it honest.

---

## 2. The construct, decomposed (what we actually score)

SystemsBench scores five dimensions. Each maps to the literature and to a sub-bank of items. Weights are the current v0.1 defaults — the engine tunes them via IRT discrimination (§7) and logs every change.

| # | Dimension | What it measures | Grounded in | Weight (v0.1) |
|---|---|---|---|---|
| **A** | **System Representation** | Maps stocks vs flows, feedback loops (R/B) with correct polarity, delays, nonlinearity, boundary/emergence — *before* prescribing. | Forrester; Sweeney & Sterman bathtub dynamics; CLD scoring | 0.22 |
| **B** | **Causal Depth** | Moves below events → patterns → structure → mental models; locates cause in structure not in blaming actors (bounded rationality). | Senge iceberg; Simon bounded rationality; Sterman | 0.18 |
| **C** | **Leverage Placement** | Ranks interventions on Meadows' 12-point hierarchy; finds the highest *feasible*-leverage point; avoids the parameter trap; checks direction; dissolves vs patches. | Meadows 1999; Ackoff (dissolve > solve) | 0.30 |
| **D** | **Dynamic Prediction & Side-Effects** | Predicts behavior over time (overshoot, oscillation, delay, collapse); anticipates policy resistance & unintended consequences; names the archetype. | Sterman *Business Dynamics*; Senge archetypes | 0.18 |
| **E** | **Epistemic & Contextual Fit** | Matches intervention type to the system's domain; surfaces the paradigm/whose-goal; holds appropriate uncertainty; no false determinism. | Cynefin (Snowden & Boone 2007); Checkland SSM/CATWOE | 0.12 |

**Leverage Placement (C) carries the most weight** — it is the core, hardest-to-fake competence and the product's namesake.

### 2.1 Meadows' 12 leverage points (the scoring ladder for Dimension C)

From **lowest leverage (12)** to **highest (1)**. A model's proposed intervention is located on this ladder; correct placement + justification + direction-check is what scores.

12. Constants, parameters, numbers (subsidies, taxes, standards)
11. The sizes of buffers & stabilizing stocks relative to their flows
10. The structure of material stocks and flows
9. The lengths of delays relative to the rate of system change
8. The strength of balancing (negative) feedback loops
7. The gain around driving reinforcing (positive) feedback loops
6. The structure of information flows (who has access to what)
5. The rules of the system (incentives, punishments, constraints)
4. The power to add, change, evolve, or self-organize system structure
3. The goals of the system
2. The mindset or paradigm out of which the system arises
1. The power to transcend paradigms

**Scoring nuance (critical):** leverage is not monotonic with score. The *highest-feasible* leverage given resistance and Cynefin domain wins — not the theoretically highest. An answer that names #1/#2 as a slogan without justifying why it beats an easier intervention, checking direction, and acknowledging resistance scores *below* a well-justified #5–#7 answer. (Meadows herself called the ranking "slippery.")

### 2.2 The skill checklist (Dimension A & B granularity — Arnold & Wade)

Recognizing interconnections · identifying & understanding feedback · understanding system structure · differentiating stocks/flows/variables · identifying nonlinear relationships · understanding dynamic behavior · reducing complexity via conceptual models · understanding systems at multiple scales.

### 2.3 The archetype layer (Dimension D bonus)

Does the model recognize a recurring loop structure when present? *Limits to Growth · Shifting the Burden · Tragedy of the Commons · Fixes that Fail · Escalation · Success to the Successful · Eroding Goals · Growth and Underinvestment · Accidental Adversaries* (Senge).

### 2.4 The cross-validation lattice

A high-quality answer is coherent across several lenses. Meadows' "structure/goals/paradigm > parameters" ≈ Ackoff's "dissolve > solve" ≈ Senge's "structural cause > events" ≈ Cynefin's "match intervention to domain" ≈ SSM's "surface the Weltanschauung." Coherence across ≥2 lenses is a quality signal scored in E.

---

## 3. Item taxonomy (the question bank)

Items are organized by **format × difficulty × construct**, every item **date-stamped**, **template-derived** where possible (contamination resistance), and tagged with the construct(s) it tests.

### 3.1 Item formats

| Format | Code | What the model does | Grading oracle |
|---|---|---|---|
| **Stock-Flow Inference** | `SF` | Given inflow/outflow over time, infer the stock trajectory (bathtub task). | **Exact / numeric** — auto-gradable. No judge. |
| **Causal Loop Mapping** | `CLD` | Produce a causal loop diagram (structured: variables, signed links, R/B loops, delays) for a scenario. | **Structured rubric** — link polarity & loop type are checkable; structure scored programmatically + judge for completeness. |
| **Leverage Identification** | `LEV` | Given a system + goal, propose & rank interventions; name the single highest-feasible-leverage point with justification. | **Jury rubric** (C-heavy) + reference solution. |
| **Dynamic Prediction** | `DYN` | Predict behavior-over-time after an intervention (overshoot? oscillation? delay? collapse?). | **Reference trajectory** match + judge for mechanism. |
| **Archetype Recognition** | `ARC` | Identify the system archetype + the trap it creates + the high-leverage escape. | **Reference label** (auto) + jury for the escape. |
| **Misperception Trap** | `TRAP` | Scenarios engineered so the intuitive answer is wrong-direction/low-leverage (the Sweeney-Sterman trap). | **Reference** + faithfulness probe. |
| **Full Systems Brief** | `BRIEF` | Open-ended: map a real messy system end-to-end (the integrative item; touches all five dimensions). | **Full jury rubric**, swap-averaged, reference-guided. |

### 3.2 Difficulty levels (operational definitions)

- **L1 — Recognition:** can it name the construct? (interconnection, loop, stock).
- **L2 — Understanding:** can it explain dynamic behavior the construct produces?
- **L3 — Application:** can it map a novel scenario and locate leverage correctly?
- **L4 — Diamond:** "expert-grade." Authored + validated by ≥2 systems-thinking reviewers; the intuitive answer is wrong; private held-out split, never published. (GPQA-Diamond philosophy.)

Difficulty is **operationally defined**, not asserted: an item is L4 only if competent human systems thinkers succeed *and* a strong naive model fails (the discrimination signal from §7 confirms or demotes it).

### 3.3 Coverage matrix

The bank must cover **format × difficulty × construct** without holes. The engine tracks coverage and flags gaps each run (HELM's "what's covered vs missing" taxonomy discipline). Target: ≥ 5 items per (format × L3) cell before a format is "live," ≥ 20 for stable IRT fitting.

### 3.4 Domains (so we test transfer, not memorized cases)

Scenarios are drawn across **ecology, economics/markets, organizations, public health, software/infra systems, social systems, personal/behavioral systems, and AI/agent systems.** A competent systems thinker transfers across domains; items rotate domain to prevent domain-specific memorization.

---

## 4. Scoring model

### 4.1 Per-item score

Each item yields a **dimension vector** (A–E sub-scores, each normalized 0–1) and partial credit. Auto-gradable formats (SF, parts of CLD/DYN/ARC) produce deterministic sub-scores; open formats go to the jury (§5).

### 4.2 Per-model composite

```
STLC(model) = Σ_d  w_d · mean_over_items( dimension_score_d )
```
with weights `w_d` from §2 (engine-tuned). Reported **always** as:
- the **dimension vector** (the real signal),
- the **composite** with a **bootstrap 95% CI** (Miller, "Adding Error Bars to Evals," 2024), computed **over calibrated dimensions only** with an explicit `calibrated_dims` field (§5.1 fail-closed rule),
- a **leverage-ladder profile** (where on Meadows' 12 does this model habitually intervene?) — a fingerprint, not a scalar,
- a **calibration-status line**: each open-format dimension is either certified (jury cleared the §5.1 gate) or marked `UNCALIBRATED — not scored`. A scalar is never emitted bare.

### 4.3 Ability estimation (IRT)

Beyond raw means, we fit a **2-parameter IRT model** over the item × model response matrix to report **ability θ ± SE** that accounts for uneven item difficulty, and to power item QA (§7). (Polo et al. "tinyBenchmarks" 2024 for the representative-subset trick.)

### 4.4 Pairwise / arena mode (optional)

For head-to-head model ranking we collect pairwise jury judgments and fit a **Bradley-Terry** model with bootstrap CIs and tied ranks (Chatbot Arena methodology), with **style controls** (regress out length & formatting) to defeat verbosity-Goodharting.

### 4.5 Faithfulness axis (reported separately, never averaged in)

We probe whether the stated reasoning *causes* the answer: truncate/perturb the reasoning trace and inject a bias, and check whether the conclusion responds appropriately (Lanham et al. 2023; Turpin et al. 2023). A high score with low faithfulness is flagged, not silently averaged away.

### 4.6 Evaluation Run Protocol (how a model is actually scored, end-to-end)

The deterministic pipeline that turns "a model" into "a SystemsBench card." Fixed and standardized so results are reproducible and comparable (HELM's adapter discipline; GAIA/SWE-bench's hard-path/auto-grade decoupling).

1. **Select items.** Draw the run set from the bank: either the full live bank, or the IRT-selected representative subset for cheap continuous tracking (tinyBenchmarks). Record item IDs, formats, difficulties, and date-stamps. For contamination-sensitive runs, regenerate templated items to fresh surface forms first.
2. **Fix the harness.** One standardized prompt template per format (no per-model prompt tuning), fixed decoding (record temperature/seed), k samples per item for variance estimation. The harness is versioned with the spec.
3. **Elicit.** Run the model on every item; capture the **full reasoning trace** (not just the final answer) — process grading requires it.
4. **Auto-grade deterministic formats.** `SF`, the structural part of `CLD`/`DYN`/`ARC` → programmatic oracles (numeric match, loop-polarity check, reference-label match). No judge cost, no judge bias.
5. **Jury-grade open formats.** `LEV`, `BRIEF`, and the open part of `CLD`/`DYN` → the §5 cross-family jury, reference-guided, anchored per-dimension (A–E), swap-averaged, style-controlled. **Only formats whose jury has cleared the §5.1 calibration gate are scored; uncertified formats are carried as `UNCALIBRATED — not scored` (fail-closed).**
6. **Run faithfulness probes** (§4.5) on a sampled subset of trace-bearing items; record F ∈ {faithful, mixed, unfaithful}.
7. **Aggregate & report the card.** Produce: the **dimension vector** (A–E, with per-sub-criterion breakdown), the **composite STLC** with bootstrap 95% CI, **ability θ ± SE** (when IRT is fitted), the **leverage-ladder profile** (where on Meadows' 12 the model habitually intervenes), the **faithfulness flag**, and **date-sliced** scores for contamination transparency. Never a bare scalar.

Output is written to `results/` as a versioned card tied to the spec version, the harness version, and the item-set hash — so every published number is fully reproducible.

---

## 5. The judging protocol (how open items are graded)

LLM-as-judge done to the standard of the field, not naively.

1. **Reference-guided.** Every open item ships with a reference solution / gold trace; the judge sees it (Zheng et al.: massively improves reliability).
2. **Rubric-anchored, criterion-decomposed.** The judge scores each dimension (A–E) against explicit anchor descriptions per score level — not a holistic 1–10 (Prometheus).
3. **Cross-family jury (PoLL).** A panel of ≥3 judges from *different model families* (never the same family as the candidate, to defeat self-preference). Aggregate by mean/median; report dispersion.
4. **Swap-averaged & position-debiased.** For any pairwise call, run both orderings; a win counts only if order-consistent. Report swap-disagreement rate.
5. **Style/length controlled.** Rubric explicitly forbids credit for length, fluency, or formatting; verbosity is regressed out in arena mode.
6. **Calibrated & gated.** Before a judge config is used on the full bank it must clear an agreement threshold (Krippendorff's α) against a **human-labeled calibration set** (target 100–300 items). Report judge–human vs human–human agreement (the ceiling). Kendall-τ of the resulting model ranking vs a human spot-check must hold.
7. **CoT-before-verdict**, with the caveat that judge reasoning can rationalize bias — hence the human-gold gate above.

### 5.1 Calibration gold-set & the fail-closed gate

The "calibrated & gated" promise (item 6, and Design Principle #6) is **operationalized** in `protocols/CALIBRATION_GOLDSET.md` — its rule, not aspiration. The binding points:

- A jury config is **certified per open format** only after clearing the **two-threshold gate** on a stratified, expert-labeled gold set (≥120 items, ≥30/format, 20% sealed): **Krippendorff's α ≥ 0.667** (judge vs human-gold, reported against the human–human ceiling) **AND Kendall's τ ≥ 0.7** (judge-vs-human model ranking), confirmed on the sealed split (≤0.05 α drop).
- **Fail-closed rule (non-negotiable):** if a format's jury is uncertified, that format's dimensions are reported as **`UNCALIBRATED — not scored`** and are **never** imputed, defaulted, or averaged into the composite. The composite covers calibrated dimensions only (§4.2).
- **Drift:** a certified jury that later drops below threshold is auto-decertified (Structure §7 CALIBRATE auto-rollback), and the format falls back to `UNCALIBRATED` until re-gated.

Deterministic formats (`SF`, exact-oracle items) require no jury and no gate.

---

## 6. Contamination & validity defenses

| Threat | Defense |
|---|---|
| Memorized items | Template/symbolic regeneration per run (GSM-Symbolic); each run uses fresh surface forms. |
| Test-set leakage | **Private Diamond (L4) split** never published; **canary strings** embedded; **Min-K%/exchangeability** membership tests (Oren et al. 2023) on suspect models. |
| Training-cutoff coverage | Date-stamp every item; report **date-sliced** scores to expose the contamination cliff (LiveCodeBench). |
| Construct invalidity | Convergent evidence (does it correlate with related systems tasks?) + discriminant evidence (it must *not* just track answer length or n-gram overlap). |
| Goodhart / overfitting | A held-out metric kept out of any optimization loop; a refreshed living split; a human-preference anchor. |
| Label noise | Audit a sample every release (assume 3–7% noise, MMLU-Redux); IRT negative-discrimination flags likely-bad items. |

---

## 7. The recursive self-improvement engine

This is what makes SystemsBench *alive*. Triggered by **`Davara /SystemsBenchSenseRun`**. One run = one bounded, logged, reversible enhancement. The loop:

**SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE**

1. **SENSE.** Load current state (this doc, rubrics, item bank, last N run logs, IRT stats, coverage matrix, open issues in `protocols/BACKLOG.md`). Compute health: coverage holes, low-discrimination/mislabeled items, judge-calibration drift, saturated dimensions.
2. **CRITIQUE.** Run the **Design Review Rubric** (§8) against the current benchmark. Produce a scorecard + the **single highest-leverage fix** (eat our own dog food — we use leverage thinking on ourselves).
3. **RESEARCH.** Before changing anything, check what already exists (don't reinvent the wheel): scan the literature/registry for prior art on the proposed change. Log sources.
4. **PROPOSE.** Draft exactly **one** concrete enhancement (a new item set, a rubric refinement, a weight retune, a new defense, a coverage fill). Scope it small and reversible.
5. **REVIEW (the gate — recursive evaluation process).** The proposal passes the **Idea Advancement Gate** (§8.2). August-approval + a second independent check for anything structural (mirrors the Outlier.Systems build protocol).
6. **APPLY.** Make the change. Bump version. Update `CHANGELOG.md`.
7. **CALIBRATE.** Re-run affected calibration: re-fit IRT, re-check judge α on the gold set, re-test contamination defenses on changed items. If calibration regresses, **auto-rollback** (the change is reversible by design).
8. **LOG.** Write a full run log to `/logs/runs/` — state-before, critique scorecard, sources, the proposal, the review verdict, the diff, calibration deltas, and the thought process. Nothing is undocumented.
9. **RECURSE.** Append residual ideas to the backlog. The next `SenseRun` starts from the improved state. The benchmark compounds.

**Bounded autonomy:** one enhancement per run, always reversible, always logged, always gated. The engine improves the benchmark the way Meadows would intervene in a system — small, structural, high-leverage moves, watching the feedback.

---

## 8. The evaluation & advancement process (how ideas move forward)

We grade our own builds with the same rigor we grade models. Two instruments:

### 8.1 Benchmark Design Review Rubric (run every SenseRun, Step 2)

Score each 1–5. A change ships at **≥ 4 average AND no category below 3.**

| # | Category | 1 (fail) | 5 (excellent) |
|---|---|---|---|
| 1 | **Construct validity** | Measures a proxy / orphan question | Traces cleanly to a named construct & predicts real competence |
| 2 | **Counterintuitivity** | Obvious answer is correct | Obvious answer is the trap; insight required |
| 3 | **Gradeability** | Subjective, unreliable | Deterministic oracle or calibrated rubric with anchors |
| 4 | **Contamination resistance** | Static, memorizable | Templated / date-stamped / held-out |
| 5 | **Discrimination** | All models pass or all fail | Separates strong from weak (good IRT `a`) |
| 6 | **Coverage value** | Duplicates existing items | Fills a real hole in the matrix |
| 7 | **Reversibility** | Hard to undo / unscoped | Small, reversible, logged |
| 8 | **Ethos echo** | Generic | Carries the Meadows/Outlier.Systems lineage; poetry + leverage |

**Output:** a scorecard + the single highest-leverage fix → logged in `/logs/scorecards/`.

### 8.2 Idea Advancement Gate (the recursive go/no-go)

A proposed change advances only if it clears, in order:

1. **Construct gate** — does it map to a named construct? (no → reject)
2. **Leverage gate** — is this the *highest-leverage* available change this run, per the Step-2 scorecard? (no → defer to backlog)
3. **No-regress gate** — does calibration hold or improve (IRT discrimination, judge α, contamination tests)? (no → auto-rollback)
4. **Review gate** — August approves + a second independent check for structural changes.
5. **Reversibility gate** — is it scoped and undoable? (no → re-scope)

Clears all five → **APPLY**. Fails any → logged with reason, residual to backlog. This is the self-learning loop: rejected ideas teach the rubric (recurring rejections become documented anti-patterns).

### 8.3 Evolution cadence

- **Per SenseRun** → one gated enhancement + Design Review scorecard.
- **Every ~5 runs** → meta-review: which dimensions saturate? Which item types keep scoring high `a`? Promote winners, retire low-discrimination items, retune weights.
- **On milestones** → Davara proposes a structural ethos edit → Outlier.Systems council reviews → August approves → version minor/major bump.

> A benchmark is not a fixed artifact. It is a compounding one. Every run teaches the next. This structure is the teacher.

---

## 9. Repository layout

```
SystemsBench/
├── SystemsBenchStructure.MD     # THIS FILE — canonical structure & spec (the website source)
├── SystemsBenchEngine.MD        # the recursive engine: exact SenseRun procedure & protocols
├── SystemsBenchResearch.MD      # the living research & prior-art ledger (so we don't reinvent the wheel)
├── CHANGELOG.md                 # every version, every change, dated
├── engine/                      # SenseRun orchestration (scripts/specs)
├── items/                       # the item bank (by format/difficulty/construct), date-stamped
├── rubrics/                     # per-dimension scoring rubrics with anchors
├── protocols/                   # BACKLOG.md, anti-patterns, calibration gold-set spec
├── logs/
│   ├── runs/                    # one full log per SenseRun
│   └── scorecards/              # Design Review scorecards
└── results/                     # model evaluation outputs (vectors, CIs, leverage profiles)
```

---

## 10. Roadmap (the build-up, high-leverage first)

1. **Genesis (this).** Structure, engine, research ledger, rubrics, seed items, the SenseRun loop. ✅
2. **Seed bank.** ≥5 L3 items per format across ≥3 domains; reference solutions; one Diamond seed (private).
3. **Calibration gold set.** Human-labeled slice; lock judge config against Krippendorff α.
4. **First model eval.** Run the bank on a panel of models; publish the dimension vectors + leverage profiles + CIs.
5. **IRT online.** Enough responses to fit 2PL; prune/weight items; build a tiny representative subset for cheap continuous tracking.
6. **Living refresh.** Template-regeneration + date-stamped scenarios on a cadence; date-sliced contamination reporting.
7. **Arena mode.** Pairwise + Bradley-Terry with style controls for head-to-head leaderboard.
8. **Open the structure.** Publish this document; invite others to build on it; SystemsBench becomes the shared instrument for measuring where intelligence chooses to push.

---

## Appendix — Source lineage

**Systems thinking:** Meadows ("Leverage Points" 1999; *Thinking in Systems* 2008; *Limits to Growth* 1972) · Forrester (System Dynamics) · Sterman (*Business Dynamics* 2000; bathtub dynamics w/ Sweeney 2000) · Senge (*The Fifth Discipline* 1990; archetypes) · Ackoff (dissolve>solve; DIKW) · Snowden & Boone (Cynefin, HBR 2007) · Checkland (SSM/CATWOE 1981) · Simon (bounded rationality 1957) · Arnold & Wade ("A Definition of Systems Thinking" 2015) · Stave & Hopper (taxonomy 2007) · Plate & Monroe (mental-model measurement).

**Benchmark science:** Hendrycks (MMLU) · Wang (MMLU-Pro) · Rein (GPQA/Diamond) · Liang (HELM) · Jimenez (SWE-bench) · Mialon (GAIA) · Chollet (ARC-AGI) · Zheng (MT-Bench / LLM-as-judge) · Verga (PoLL juries) · Kim (Prometheus) · Dubois (length-controlled AlpacaEval) · Lightman (process supervision) · Wang (Math-Shepherd) · Zheng (ProcessBench) · Lanham/Turpin (CoT faithfulness) · Polo (tinyBenchmarks) · Chiang (Chatbot Arena / Bradley-Terry) · White (LiveBench) · Jain (LiveCodeBench) · Mirzadeh (GSM-Symbolic) · Oren (test-set contamination) · Miller (error bars on evals).

---

*Map the system. Find where to push. Predict what happens. Make humanity proud.*
**Outlier.Systems** · Led by Ember Seoni & August Domanchuk · Operated by Outlier.Systems
**SystemsBench** — the instrument for the age of agents.
