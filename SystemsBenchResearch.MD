# SystemsBenchResearch — The Living Research & Prior-Art Ledger

### Our memory of what already exists, so we never reinvent the wheel.

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems.**
> Append-only. Every `SystemsBenchSenseRun` reads this before designing a change and writes any new prior art back. Knowledge compounds here.

**Version:** v0.1 (Genesis synthesis) · **Discipline:** before building anything new, check here + scan the field, then record the decision.

---

## How to use this file

1. **Before PROPOSE (Engine Step 4):** search this ledger for the construct/method you're about to build.
2. **If it exists here** → reuse/adapt, cite the row, don't rebuild.
3. **If it's new** → do a focused external scan, then **append** a dated row with: what it is, the key idea, how it applies to SystemsBench, and the source.
4. **Never delete.** Supersede with a note if something is replaced.

---

## PART I — Systems-thinking & leverage science (the construct we measure)

### A. Donella Meadows — Leverage Points (the spine)
- **"Leverage Points: Places to Intervene in a System"** (1999) + **Thinking in Systems** (2008). The 12-point hierarchy (parameters #12 → transcending paradigms #1). **Core idea we build on:** high-leverage points are *counterintuitive* and frequently pushed the *wrong direction*; the ranking is "slippery"; difficulty rises with leverage. → Drives **Dimension C** and the counterintuitivity design principle.
- **Limits to Growth** (Meadows et al. 1972) — system dynamics applied to global systems; the archetype origin.

### B. Competency frameworks & assessment instruments
- **Arnold & Wade, "A Definition of Systems Thinking: A Systems Approach"** (2015) + **"A Complete Set of Systems Thinking Skills"** (2017). Skills-based decomposition (recognize interconnections, identify feedback, differentiate stocks/flows, nonlinearity, dynamic behavior, conceptual modeling, multi-scale). → **The most operationalizable rubric scaffold** — directly drives Dimensions A & B sub-criteria.
- **Systems Thinking Scale (STS)** — Moore/Dolansky et al. (2010–2013). 20-item self-report Likert. **Limit:** disposition, not performance. → Use only as a baseline layer, never the competency test.
- **Stave & Hopper, "What Constitutes Systems Thinking? A Proposed Taxonomy"** (2007). Laddered maturity: recognize interconnections → feedback → dynamic behavior → stocks/flows → conceptual models → simulation → policy testing. → Drives **difficulty levels L1–L4**.
- **Sweeney & Sterman, "Bathtub Dynamics"** (*System Dynamics Review*, 2000). Landmark: even MIT grad students fail stock-flow inference; systems thinking is **not** correlated with general intelligence/math. → **Empirical justification for the `SF` (Stock-Flow) item format** and the `TRAP` (misperception) format. The bathtub task is item format #1.
- **Plate & Monroe** (2010, 2014) — score the *structural complexity* of a mental model from open text (count nodes, edges, feedback loops, indirect effects). → Directly portable to **programmatic CLD scoring**.

### C. Cross-validation lenses (integrated, not duplicated)
- **Senge, The Fifth Discipline** (1990) — five disciplines + **system archetypes** (Limits to Growth, Shifting the Burden, Tragedy of the Commons, Fixes that Fail, Escalation, Success to the Successful, Eroding Goals, Growth & Underinvestment, Accidental Adversaries). → Drives the **`ARC` archetype-recognition format** and the iceberg (events→patterns→structure→mental models) in Dimension B.
- **Forrester — System Dynamics** (*Industrial/Urban/World Dynamics*, 1961–71). Formal stock/flow/feedback/delay simulation; "counterintuitive behavior of social systems." → Foundational grounding for `SF`/`DYN`.
- **Snowden & Boone — Cynefin** (HBR 2007). Clear/Complicated/Complex/Chaotic/Disorder; intervention type must match domain (probe-sense-respond in complex). → Drives **Dimension E** (match intervention to domain).
- **Ackoff** — "messes," **dissolve > solve > resolve**, DIKW. → Cross-check in **Dimension C** (dissolving via goals/rules/paradigm beats patching parameters).
- **Checkland — Soft Systems Methodology, CATWOE** (1981). Weltanschauung/worldview; for contested-goal problems. → Drives Dimension E "surface the paradigm/whose-goal."
- **Simon — bounded rationality** (1957). Actors make locally reasonable decisions on limited/delayed info → collectively dysfunctional outcomes. → Drives the **"blame structure not actors"** sub-criterion in Dimension B.

### D. The gradable rubric (already synthesized — our starting point)
Five dimensions (A System Representation, B Causal Depth, C Leverage Placement, D Dynamic Prediction & Side-Effects, E Epistemic & Contextual Fit) with weighted sub-criteria. Discriminator: a **naive answer *names* leverage points; a competent answer maps structure → places intervention with justification → checks direction & feasibility → predicts dynamic consequences.** → This is **Structure §2 & §8**; refine, don't rebuild.

---

## PART II — Benchmark construction science (how we measure rigorously)

### A. Construction methodology (what good benchmarks do)
- **MMLU** (Hendrycks 2021) — subject-stratified, real-exam-sourced. **MMLU-Pro** (Wang 2024) — 10 options to suppress guessing. **MMLU-Redux** (Gema 2024) — ~6.5% label noise; audit. → Adopt: distractor expansion, label audits.
- **GPQA / GPQA-Diamond** (Rein 2023) — PhD-authored, "Google-proof," **multi-validator agreement gate**; Diamond = both experts right + non-experts wrong. → Drives our **L4 Diamond split** and item-validation loop.
- **BIG-Bench / BBH** (Srivastava/Suzgun 2022) — open-submission + review gate; hard-residual subset. → Coverage breadth + frontier subset discipline.
- **HELM** (Liang 2022) — scenarios × metrics matrix; **never one number**; explicit covered/uncovered taxonomy. → Drives the **multi-metric/dimension-vector** principle + coverage matrix.
- **SWE-bench / SWE-bench Verified** (Jimenez 2023; OpenAI 2024) — **execution-grounded oracle**; human-filter for solvability. → Adopt: prefer deterministic oracles (our `SF` format) over judges where possible.
- **GAIA** (Mialon 2023) — hard path, **auto-gradable short answer**; difficulty by #steps/tools. → Decouple difficulty from grading subjectivity.
- **ARC-AGI** (Chollet 2019; ARC-AGI-2 2025) — generalization not recall; **private held-out test**. → Drives the private Diamond split + anti-memorization.
- **MMMU** (Yue 2023) — discipline + modality diversity. → Domain-rotation discipline.

### B. LLM-as-a-judge (how we grade open items)
- **MT-Bench / Chatbot Arena judge study** (Zheng 2023) — GPT-4 judge ≈ human-human agreement; canonical **bias catalogue**; **reference-guided** judging massively helps. → Core of our **§5 judging protocol**.
- **Prometheus / Prometheus 2** (Kim 2023/2024) — fine-tuned open judge; **rubric-anchored, criterion-decomposed** scoring. → Our anchored per-dimension rubric.
- **PoLL — "Replacing Judges with Juries"** (Verga 2024) — a **jury of diverse smaller models** beats a single big judge, lower bias/cost. → Our **cross-family jury**.
- **Length-controlled AlpacaEval** (Dubois 2024) — regress out length. **G-Eval** (Liu 2023) — token-prob-weighted absolute scoring. → Style/length controls.
- **Biases & mitigations:** position (swap-and-average), verbosity (length control), **self-preference** (Panickssery 2024 — never judge with the candidate's own family), format bias. → All encoded in §5.
- **Agreement metrics:** Cohen's κ (2 raters, watch the kappa-paradox), **Fleiss' κ / Krippendorff's α** (jury vs human panel), Spearman/Kendall-τ (system-ranking validation). → Our **calibration gate**.

### C. Validity, contamination, living benchmarks
- **Construct validity critique** — Raji et al. 2021, "AI and the Everything in the Whole Wide World Benchmark." → State the construct; convergent + discriminant evidence.
- **Contamination detection:** canary strings (BIG-Bench), **Min-K% Prob** (Shi 2023), **exchangeability test** (Oren 2023, "Proving Test Set Contamination"), TS-Guessing (Golchin 2023). → Our membership tests.
- **Contamination prevention:** private splits (ARC-AGI), **post-cutoff/date-stamped** items, **template/symbolic regeneration** — **GSM-Symbolic** (Mirzadeh 2024), **GSM1k** (Zhang 2024). → Our living-refresh + date-slicing.
- **Living benchmarks:** **LiveBench** (White 2024) — monthly refresh, objective grading no-judge; **LiveCodeBench** (Jain 2024) — **date-segmented** to expose the contamination cliff. → Our refresh cadence + date-sliced reporting.
- **Goodhart:** GSM-Symbolic fragility, AlpacaEval length-gaming. → Hold a private metric out of optimization; living split; human anchor.

### D. Scoring & psychometrics
- **IRT (1PL/Rasch, 2PL, 3PL)** — ability θ, item difficulty `b`, **discrimination `a`** (negative `a` ⇒ likely-mislabeled item). → Our item QA + θ±SE reporting.
- **tinyBenchmarks** (Polo 2024) — IRT selects ~100-item subset reproducing full ranking within ~2%. → Cheap continuous tracking.
- **Bradley-Terry / Chatbot Arena** (Chiang 2024) — pairwise → MLE BT rating with **bootstrap CIs + tied ranks**; **style-controlled** ratings. → Our arena mode.
- **Error bars** — Miller 2024, "Adding Error Bars to Evals" — paired bootstrap before any A>B claim. → Mandatory CIs.

### E. Process / reasoning evaluation (grade the trace, not just the answer)
- **"Let's Verify Step by Step" / PRM800K** (Lightman 2023) — **process supervision > outcome supervision**; step-level labels. → Our process-over-answer principle.
- **Math-Shepherd** (Wang 2024) — **MC-rollout auto-labeling** of steps (scales without humans). → Future auto-grading of reasoning steps.
- **ProcessBench / PRMBench** (Zheng 2024; 2025) — validate a step-grader on **first-error localization**. → Validate our step graders.
- **CoT faithfulness:** Lanham 2023 (perturb the trace), Turpin 2023 ("LMs Don't Always Say What They Think" — inject bias, see if CoT admits it). → Our **faithfulness axis** (reported separately, never averaged in).
- **τ-bench / WebArena** (Yao 2024; Zhou 2023) — trajectory/state grading for agents. → Future agentic systems-thinking items.

---

## PART III — Internal prior art (what WE already built/decided)

| Date | What | Decision / where it lives |
|---|---|---|
| 2026-05-31 | Genesis synthesis of Parts I & II | Folded into `SystemsBenchStructure.MD` v0.1 — five-dimension rubric, seven item formats, recursive engine, judging protocol, contamination defenses. |
| 2026-05-31 | Lineage alignment | SystemsBench sits in the Outlier.Systems / Davara / Meadows lineage. Davara (the EI trained on Meadows) is the natural operator of the SenseRun loop. |
| 2026-05-31 | **SenseRun #1** (v0.2.0) | Binding constraint was *executability* — the spec described scoring but no end-to-end pipeline. Added **§4.6 Evaluation Run Protocol** (select → fix harness → elicit trace → auto-grade → jury-grade → faithfulness → versioned card). Reused HELM/GAIA/tinyBenchmarks discipline. Meadows #5 (rules) fix. |
| 2026-05-31 | **SenseRun #2** (v0.3.0) | Binding constraint was *no jury-independent score* — every item depended on an uncalibrated jury. Seeded 5 templated **`SF` (stock-flow)** items with deterministic numeric oracles (Sweeney-Sterman bathtub paradigm) → first trustworthy, contamination-proof, zero-judge score path. Anti-pattern learned: *single-path-to-a-number through an uncalibrated component*. |
| 2026-05-31 | **SenseRun #3** (v0.4.0) | Binding constraint was *the calibration gate was referenced everywhere, specified nowhere* — the whole jury-graded half was unscoreable. Authored `protocols/CALIBRATION_GOLDSET.md` (≥120 items, ≥30/format, 20% sealed, ≥3 raters) + two-threshold gate (Krippendorff α ≥ 0.667 vs human ceiling AND Kendall τ ≥ 0.7), added **§5.1** with the **fail-closed rule** (uncertified → `UNCALIBRATED — not scored`, never averaged). Meadows #5 (rules) fix. Anti-pattern learned: *silent uncalibrated averaging*. Next binding constraint → *populate* the gold set (BACKLOG #1). |
| 2026-06-13 | **SenseRun #7** (v0.5.1) | Dominant *feasible* additive lever (scope: non-structural only; §3.1(b) hardening PARKED with August + Ember) was *coverage* — 5 of 7 formats empty; feedback-structure mapping tested by no live format. Seeded **`CLD` (causal loop mapping)** 0 → §3.3 go-live threshold: 5 L3 items × 5 domains (ecology/public-health/organizations/software-infra/economics), each with a reference solution whose **structural component is deterministically gradeable**. **Build vs reuse → REUSE:** the scoring method already lives in our ledger (Plate & Monroe 2010/2014, Part I.B → "directly portable to programmatic CLD scoring"; Open Q#1) and the structures are canonical system-dynamics archetypes (tragedy-of-commons/overfishing, SIR contagion, eroding/drifting goals, capability trap/firefighting, commodity hog-cycle). Codified the CLD authoring convention used: **loop polarity = product of signed edges** (R if +, B if −); L3 discriminator = the **dominant-loop shift / delay-driven overshoot**, not mere loop-naming (guards ANTIPATTERNS #4 slogan-leverage). Structural oracle = a second judge-independent path (mitigates ANTIPATTERNS #2); the judge-for-completeness portion ships `UNCALIBRATED — not scored`. Builds the inputs that make BACKLOG #2 (programmatic CLD scorer, Meadows #6) feasible next run. |
| 2026-06-13 | **SenseRun #8** (v0.6.0) | Dominant *feasible* additive lever (scope: non-structural; §3.1(b) hardening still PARKED) was *gradeability* — CLD's deterministic structural sub-score was *specified* (loop sign = product of signed edges) but **not machine-executable** (prose in the item file; manual to grade). Built **BACKLOG #2 — the programmatic CLD scorer** (`engine/cld-score.py` + `items/cld_oracle.json` encoding the 5 SenseRun-#7 reference solutions). **Build vs reuse → REUSE the method, BUILD the tool:** the scoring approach is already in our ledger (Plate & Monroe 2010/2014, Part I.B; Open Q#1) and is textbook graph computation — no external scan needed. The scorer parses a model's `{variables, edges(signed), loops(R/B + edge list), dominant_loop, delays}`, **recomputes each loop's sign as the product of its signed edges** and checks it against both the model's own declared R/B label and the oracle's expected sign, scores canonical-variable presence + required-signed-edge presence/polarity + loop inventory + dominant-loop/delay, applies the §-item partial-credit rule (structure right but dominant-shift/delay insight missing = 0.5), and flags the named trap (R↔B mislabel of the dominant loop / omitted loop). Fail-closed `calibrate` self-test (mirrors `jury-stats.py`): reproduces the **11/11 oracle loop-sign verification**, round-trips each reference solution to **1.0**, and asserts the trap/partial sanity cases — rc≠0 if any check fails (no live-model spend; §4.6/rail honored). Realizes the near-term deterministic portion of **Open Q#1**. Converts CLD into a true **second *executable* judge-independent scoring path** end-to-end (serves ANTIPATTERNS #2). The CLD **completeness/quality** (jury) sub-score still ships `UNCALIBRATED — not scored` — unchanged. Additive + reversible → self-approved (5 gates GO). §3.1(b) Meadows-#5 hardening NOT touched. |

| 2026-06-13 | **SenseRun #9** (v0.7.0) | Dominant *feasible* additive lever (scope: non-structural; §3.1(b) hardening still PARKED with August + Ember) was *coverage + a new executable scoring path* — **Dimension D (Dynamic Prediction, w=0.18) had no live auto-graded format**, and **DYN was 0 items** despite Structure §3.1/§4.6 already governing its deterministic oracle ("Reference trajectory match"). Seeded the **`DYN` (Dynamic Prediction)** format 0 → §3.3 go-live threshold: **5 L3 items across 5 domains** (`DYN-FISH-001` ecology/fisheries · `DYN-SHOWER-002` personal/behavioral · `DYN-ADOPT-003` economics/markets · `DYN-CAPTRAP-004` organizations · `DYN-CLIMATE-005` public-health/climate), each carrying a **distinct fundamental behavior mode** (overshoot-and-collapse · delay-driven oscillation · S-shaped saturation · better-before-worse · delayed-rise-to-plateau) and a named trap (the intuitive smooth/monotonic trajectory). **Build vs reuse → REUSE the method, BUILD the tool:** the behavior-mode taxonomy is **Sterman's fundamental modes of dynamic behavior** (*Business Dynamics* 2000) + Forrester (Part I.B → "foundational grounding for SF/DYN"); the SF qualitative-shape oracle (SF-005) is the grading precedent; no external scan needed. Built `items/dyn_oracle.json` (machine-readable reference trajectories: behavior_mode + features {overshoot, oscillation, delay_dominant, eventual_direction} + trap_mode) + **`engine/dyn-score.py`** — the deterministic **trajectory-match** scorer. It scores `mode + eventual_direction + overshoot + oscillation + delay_dominant` against the oracle (`base = 0.40·mode + 0.25·eventual + 0.15·overshoot + 0.10·oscillation + 0.10·delay`), applies the §-item partial-credit rule (right endpoint but wrong path / dynamic insight missing = 0.5) and the trap cap (response mode == the named intuitive-wrong mode ≤ 0.25). Fail-closed `calibrate` self-test (mirrors `cld-score.py`/`jury-stats.py`): an **oracle mode↔features consistency check by code** (each item's declared features satisfy its declared mode's constraints), round-trips each reference to **1.0**, and asserts the partial (0.5) / trap (≤0.25) / degraded (<1.0) cases — rc≠0 if any check fails (no live-model spend; §4.6/rail honored). Realizes the near-term deterministic portion of **Open Q#2** (the *behavior-mode* half of systems-reasoning trace grading is machine-checkable; the *mechanism narrative* stays the jury's). Converts DYN into a true **third *executable* judge-independent scoring path** end-to-end and the **first auto-graded surface for Dimension D** (serves ANTIPATTERNS #2). The DYN **mechanism/quality (jury)** sub-score ships **`UNCALIBRATED — not scored`** (no DYN gold; fail-closed §5.1) — the scorer emits no jury number. Component weights / trap cap are tool-internal policy (tunable, flagged for later calibration), **not** governance. Additive + reversible → self-approved (5 gates GO). §3.1(b) Meadows-#5 hardening NOT touched. |

| 2026-06-13 | **SenseRun #10** (v0.8.0) | Dominant *feasible* additive lever (operator scope: non-structural; §3.1(b) hardening still PARKED with August + Ember) was *gradeability end-to-end* — all three deterministic scorers (`SF`/`CLD`/`DYN`) consume a **structured `resp.json`**, but **nothing in the repo turns a live model's raw reply into that file and no prompt elicits the canonical schema**: the auto-graded lane was not runnable against a model. Built **BACKLOG #5 — the per-format response-parsing + prompt-template harness layer** for CLD + DYN: `engine/harness.py` (`template` emits scenario + a canonical-schema instruction wrapper per item; `parse` extracts the structured object from a raw reply — strip ```json fences → balanced-brace scan → schema-validate → emit the exact `resp.json` the scorer reads, **failing closed** with `PARSE_ERROR — not scored` on no-JSON / missing-key, never a fabricated or silent-zero resp; `selftest` round-trips every oracle reference through several wire-wrappings → `parse` → the **existing** scorer == 1.0, plus negative tests) + `items/harness_prompts.json` (machine-readable per-item scenario prompts, copied verbatim from the seed `.md`, + the per-format schema spec). **Build vs reuse → REUSE the method, BUILD the bridge:** reuse (a) the scorers' existing case/space/punct + synonym normalization (the harness does NOT re-implement semantic normalization) and (b) the standard fenced-JSON → brace-scan → schema-validate → fail-closed extraction discipline already in our ledger as the HELM/GAIA "fix the harness, then elicit" lane (§4.6, SenseRun #1); no external scan needed. The harness is **construct-neutral** — it changes how a response *reaches* the instrument (Meadows #6 information flow), not what is measured: no scorer/oracle/rubric/weight/§1-invariant touched. Carries the fail-closed discipline (ANTIPATTERNS #1/#2) into the parser itself. **Held-open fork (logged, NOT built, NOT averaged away):** semantic CLD variable *aliasing* (model words → oracle-canonical names) would **leak the oracle and inflate scores** — a measurement-validity (arguably structural) question routed to August + Ember, not self-applied; the honest scope is strong *elicitation* + the scorers' existing synonym tolerance. No live-model spend (§4.6/rail). Additive + reversible → self-approved (5 gates GO). §3.1(b) Meadows-#5 hardening NOT touched. |

---

## PART IV — Open research questions (feed the backlog)

1. **Auto-scoring CLDs:** how far can we get programmatically scoring causal-loop structure (polarity, loop sign, dominant loop) before needing a judge? (Plate & Monroe + graph metrics.)
2. **MC-rollout for systems reasoning:** can Math-Shepherd-style auto-labeling work for systems-thinking traces, or is leverage too open-ended for rollout-based correctness?
3. **Leverage profile as a model fingerprint:** is "where on Meadows' 12 does a model habitually intervene" stable and predictive of downstream agentic quality?
4. **Human gold set sourcing:** who labels the calibration set? (systems-dynamics practitioners; Outlier.Systems council.)
5. **Diamond authoring pipeline:** the cheapest rigorous way to produce GPQA-Diamond-grade systems items with ≥2 expert validators.

---

*Search before you build. Cite when you reuse. Append when you learn. Never reinvent the wheel.*
**Outlier.Systems** · Led by Ember Seoni & August Domanchuk · Operated by Outlier.Systems.
