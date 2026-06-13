# SystemsBench — Glossary

*A field guide to every term we use — written so a curious newcomer and a working researcher can both find what they need.*

> Each entry has two layers:
> **▸ In one breath** — the plain-language version. No prerequisites.
> **▸ Going deeper** — the precise version, with the source and how SystemsBench uses it.
>
> If you only read the **In one breath** lines, top to bottom, you will understand what
> SystemsBench measures and why. That is by design. Systems thinking is not an esoteric
> art — it is a way of seeing that everyone already half-knows, given the right words.
>
> *"You think that because you understand 'one' that you must therefore understand 'two,'
> because one and one make two. But you forget that you must also understand 'and.'"*
> — Sufi teaching story, quoted by Donella Meadows in *Thinking in Systems*. This whole
> glossary is about the **"and."**

---

## Part I — Systems thinking, from the ground up

### System
**▸ In one breath:** A set of things connected so that they produce behavior none of the parts have alone. A body, a forest, a market, a company, a model's training loop.
**▸ Going deeper:** Meadows' definition — *an interconnected set of elements coherently organized in a way that achieves something* (elements + interconnections + a function/purpose). The purpose is the least obvious and most determining part. Change the parts and the system often survives; change the interconnections or the purpose and it becomes something else.

### Stock
**▸ In one breath:** Something that accumulates — a level you could measure with a snapshot. Water in a bathtub, money in an account, CO₂ in the atmosphere, trust between two people.
**▸ Going deeper:** A stock is the memory of a system — the integral of its flows over time. Stocks change *only* through their flows, and only gradually, which is the origin of delay and momentum. The classic "bathtub" intuition test (Sweeney & Sterman 2000) shows that even highly educated people routinely fail to infer a stock's path from its flows — which is exactly why SystemsBench's `SF` (Stock-Flow) format exists.

### Flow
**▸ In one breath:** A rate that fills or drains a stock. The faucet and the drain on the bathtub. Births and deaths. Hiring and quitting.
**▸ Going deeper:** Flows are the actions; stocks are the states they produce. A stock can only rise when inflow exceeds outflow, regardless of how dramatic either flow looks in isolation. Confusing a flow (the rate of emissions) with a stock (the accumulated concentration) is one of the most consequential errors in public reasoning — and a graded distinction in Dimension A.

### Feedback loop
**▸ In one breath:** A circle of cause and effect where a change comes back around to affect itself. Loops are the engines of all system behavior.
**▸ Going deeper:** A closed chain of causal links such that a change in a variable eventually flows back to that variable. Loops come in exactly two flavors (below). Almost every interesting, surprising, or stubborn behavior in the world is a loop — or several loops fighting for dominance.

### Reinforcing loop (R) / "positive" feedback
**▸ In one breath:** A loop that amplifies — the more you have, the more you get (or the faster you lose). Compound interest, viral growth, panic, erosion, addiction.
**▸ Going deeper:** A loop whose net sign is positive: it drives exponential growth or collapse and is the source of all *growth* in a system. "Positive" means self-amplifying, **not** "good" — a death spiral is a positive loop. In SystemsBench we compute a loop's polarity deterministically as the **product of its signed edges** (an even number of negative links → reinforcing).

### Balancing loop (B) / "negative" feedback
**▸ In one breath:** A loop that resists change and seeks a goal — a thermostat, hunger, a market correction, your body temperature.
**▸ Going deeper:** A loop whose net sign is negative: it is goal-seeking and stabilizing, the source of all *control* and equilibrium in a system. Balancing loops are why systems resist the interventions we throw at them ("policy resistance"). An odd number of negative edges around the cycle → balancing.

### Delay
**▸ In one breath:** The lag between a cause and its full effect. Why the shower runs cold, then scalds. Why fish stocks crash *after* the fleet is built.
**▸ Going deeper:** Delays in feedback loops are a primary source of oscillation, overshoot, and instability — the system reacts to information that is already stale. Meadows: *"A delay in a feedback process is critical relative to rates of change in the system."* Lengthening or shortening a delay (leverage point #9) can transform behavior without touching any other structure. SystemsBench's `DYN` items are largely about whether a model can predict the behavior a delay produces.

### Nonlinearity
**▸ In one breath:** When the output isn't proportional to the input — a little does nothing, then a little more breaks everything. Straws and camels' backs. Tipping points.
**▸ Going deeper:** A relationship where cause and effect are not related by a constant. Nonlinearities flip loop dominance (a loop that was weak suddenly rules), create thresholds, and defeat linear intuition. Most catastrophic surprises live here.

### Stock-and-flow structure
**▸ In one breath:** The plumbing of a system — what accumulates, what flows where, and which taps control which tanks.
**▸ Going deeper:** The map of stocks, the flows between them, and the information links that govern the flows. This *structure* is what produces behavior over time. The central systems-thinking claim — *structure drives behavior* — is the reason SystemsBench grades the **map** before it grades the **prescription**.

### Loop dominance / dominant loop
**▸ In one breath:** At any moment, one loop is usually "winning" and setting the system's behavior. Which loop wins can shift — and that shift is the whole story.
**▸ Going deeper:** When multiple loops act on the same stock, the one with the greater gain dominates the observed behavior. A *shift* in dominance (a reinforcing growth loop yielding to a balancing limit) is what turns exponential growth into an S-curve or an overshoot. Naming the dominant loop **and its shift** is an L3-grade discriminator in the `CLD` and `DYN` formats.

### Behavior over time (BOT)
**▸ In one breath:** The shape of a system's story drawn as a line on a graph — growing, settling, oscillating, booming then busting.
**▸ Going deeper:** The trajectory of a key stock plotted against time. Systems dynamics recognizes a small set of **fundamental modes** (below); identifying the right mode from the structure is the core `DYN` task. We grade the *shape*, not the prose.

### Fundamental modes of behavior
**▸ In one breath:** The handful of basic "shapes" a system's story can take. Almost everything is one of these or a blend.
**▸ Going deeper:** The canonical Sterman/Forrester set SystemsBench scores in `DYN`: **exponential growth** (a single reinforcing loop), **goal-seeking** (a single balancing loop, smooth approach), **S-shaped growth** (reinforcing then balancing — limits to growth), **overshoot-and-collapse** (growth past an eroding carrying capacity), **oscillation** (balancing loop + delay), **better-before-worse** (a fix that pays now and costs later — the capability trap), and **delayed-rise-to-plateau** (stock-flow accumulation). The *intuitive* mode is usually the smooth/monotonic one — and is usually the **trap**.

### Emergence
**▸ In one breath:** When the whole does something none of the parts can — wetness from water molecules, traffic jams from cars, intelligence from neurons.
**▸ Going deeper:** System-level properties that arise from interconnections and cannot be located in any single element. Emergence is why reductionism alone fails on systems, and why "boundary" choices matter so much.

### System boundary
**▸ In one breath:** Where you decide to draw the edge of the thing you're studying. Draw it wrong and you'll solve the wrong problem.
**▸ Going deeper:** The chosen scope of the model. Boundaries are an *act of judgment*, not a fact of nature; a too-narrow boundary externalizes the very feedback that causes the problem. Surfacing and defending the boundary is a Dimension B/E competence.

### Mental model
**▸ In one breath:** The picture of how things work that you carry in your head. Usually invisible, always driving your decisions, often wrong.
**▸ Going deeper:** The internal assumptions, beliefs, and simplifications through which an actor perceives a system. Senge's *iceberg* — events sit above patterns, above structure, above mental models — locates the deepest leverage in the models themselves. SystemsBench rewards moving *below the waterline*: from blaming actors (events) to seeing structure.

### Policy resistance
**▸ In one breath:** When a system pushes back against your fix and snaps right back to where it was. Whack-a-mole.
**▸ Going deeper:** The tendency of a system's balancing loops to defeat well-intentioned interventions, because the intervention fights the system's own goals rather than changing them. Anticipating resistance (rather than being surprised by it) is graded in Dimension D.

---

## Part II — Leverage (the heart of the matter)

### Leverage point
**▸ In one breath:** A place in a system where a small, well-aimed push produces a big, lasting change. The whole game is finding them — and they're rarely where you'd guess.
**▸ Going deeper:** From Donella Meadows' 1999 essay *"Leverage Points: Places to Intervene in a System"* — the founding text of this benchmark. Her core, hard-won finding: leverage points are **counterintuitive**, and people reliably locate them *and then push in the wrong direction*. The highest-leverage interventions (goals, paradigms) are the hardest to reach; the lowest (numbers, parameters) are where everyone fights. Measuring whether an intelligence can find the *highest feasible* leverage — and push the right way — is the reason SystemsBench exists.

### The 12 leverage points (Meadows' hierarchy)
**▸ In one breath:** Donella Meadows' ranked list of *kinds* of intervention, from weakest (tweak a number) to strongest (change the mindset). It is the scoring ladder for our core dimension.
**▸ Going deeper:** From **lowest leverage (12)** to **highest (1)**:

| # | Leverage point | Plain-language |
|---|---|---|
| 12 | Constants, parameters, numbers | The tax rate, the speed limit, the subsidy. Where everyone fights; least changes. |
| 11 | The sizes of buffers & stabilizing stocks | How much slack/inventory/reserve the system carries. |
| 10 | The structure of material stocks and flows | The physical plumbing — roads, pipes, population age structure. |
| 9 | The lengths of delays | How fast information and material move relative to change. |
| 8 | The strength of balancing (negative) feedback loops | How well the system self-corrects. |
| 7 | The gain around reinforcing (positive) feedback loops | How fast the self-amplifying loops run — usually *slow them down*. |
| 6 | The structure of information flows | Who can see what. Adding a missing feedback signal is enormously powerful. |
| 5 | The rules of the system | Incentives, punishments, constraints — the actual rules of the game. |
| 4 | The power to self-organize | The system's ability to change its own structure, add new loops, evolve. |
| 3 | The goals of the system | What the whole thing is *for*. Change the goal and everything below reorganizes. |
| 2 | The mindset/paradigm the system arises from | The shared, usually-unspoken assumptions underneath the goals. |
| 1 | The power to transcend paradigms | To hold any belief lightly; the deepest, rarest leverage. |

**▸ Critical nuance:** leverage is **not** monotonic with score. Naming "#1 change the paradigm" as a slogan scores *lower* than a well-justified #6 information-flow fix. The *highest **feasible*** point — given resistance, domain, and direction — wins. Meadows herself called the ranking "slippery," and we honor that.

### The parameter trap
**▸ In one breath:** The reflex to fix everything by adjusting a number, when the real lever is the structure or the goal. Most policy fights live here — and most of them barely matter.
**▸ Going deeper:** Meadows: *"Diddling with the details, arranging the deck chairs on the Titanic. Probably 90, no 95, no 99 percent of our attention goes to parameters, but there's not a lot of leverage in them."* SystemsBench items are authored so the obvious parameter answer is the low-leverage trap.

### The Forrester inversion
**▸ In one breath:** Jay Forrester's famous observation — people often find the right place to intervene, then push it the *wrong direction*, making things worse.
**▸ Going deeper:** Named for system-dynamics founder Jay Forrester. The classic inversions: pushing *more* growth when the leverage is *less*; adding *more* control when the leverage is *more* self-organization; speeding information delivery when the leverage is a *longer* buffer. Our `TRAP` format and the direction-check in Dimension C are built to catch this exact failure — naming the right lever but the wrong sign scores low.

### Dissolve vs. solve (Ackoff)
**▸ In one breath:** Russell Ackoff's ladder — you can *absolve* a problem (ignore it), *resolve* it (good-enough patch), *solve* it (optimize), or **dissolve** it (redesign the system so the problem can't exist). Dissolving is highest.
**▸ Going deeper:** Ackoff argued the best interventions change the system's design so the problem disappears rather than being managed forever. This maps cleanly onto Meadows' "structure/goals/paradigm > parameters" and is part of the cross-validation lattice (Dimension E).

### System archetype
**▸ In one breath:** A recurring "plot" that systems fall into again and again, across totally different domains. Learn the handful of archetypes and you start seeing them everywhere.
**▸ Going deeper:** Senge's named recurring loop-structures: *Limits to Growth, Shifting the Burden, Tragedy of the Commons, Fixes that Fail, Escalation, Success to the Successful, Eroding Goals, Growth and Underinvestment, Accidental Adversaries.* Each carries a characteristic trap and a characteristic high-leverage escape. Recognizing the archetype (the `ARC` format) is a shortcut to both the dynamics and the leverage.

### Paradigm
**▸ In one breath:** The deepest layer — the shared, usually-invisible assumptions a whole system is built on. "Growth is good." "Nature is a resource." Change these and everything above shifts.
**▸ Going deeper:** Meadows' leverage point #2. Paradigms are the sources of systems — the great unstated agreements about how the world works. They are the hardest to see (because you're inside them) and, once shifted, the highest-leverage of all but #1.

---

## Part III — What SystemsBench measures (the constructs)

### STLC — Systems Thinking & Leverage Competence
**▸ In one breath:** The capability SystemsBench measures: can you *see* a system, *map* its structure, *find* where to intervene, and *predict* what happens when you do?
**▸ Going deeper:** Our named construct, grounded in Arnold & Wade's 2015 definition of systems thinking, with the leverage component scored against Meadows' 1999 hierarchy. STLC is deliberately a **competence to act well**, not a vocabulary to recite. It decomposes into five scored dimensions (A–E).

### The five dimensions (A–E)
**▸ In one breath:** The five skills that add up to systems thinking, each scored separately so you can see exactly where a model is strong and where it's dangerous. Each gets its own entry below.

#### A · System Representation
*Weight 0.22.* Can it **see the system at all** — map stocks vs. flows, feedback loops with correct polarity, delays, nonlinearity, and boundaries — *before* prescribing? Grounded in Forrester and the Sweeney & Sterman bathtub studies. This is the perception layer; everything else builds on it.

#### B · Causal Depth
*Weight 0.18.* Does it move **below the surface** — from events, to patterns, to structure, to mental models — and locate cause in the *structure* rather than blaming the actors? Grounded in Senge's iceberg and Simon's bounded rationality. The difference between "the manager failed" and "the incentive structure made failure rational."

#### C · Leverage Placement
*Weight 0.30 — the core.* Does it **know where to push**? Ranks interventions on Meadows' 12-point hierarchy, finds the highest *feasible*-leverage point, checks the direction, and avoids the parameter trap. Grounded in Meadows (1999) and Ackoff (dissolve > solve). The hardest-to-fake competence, and the product's namesake.

#### D · Dynamic Prediction & Side-Effects
*Weight 0.18.* Can it **predict behavior over time** — overshoot, oscillation, delay, collapse — and anticipate policy resistance and unintended consequences, naming the archetype when one is present? Grounded in Sterman's *Business Dynamics* and Senge's archetypes.

#### E · Epistemic & Contextual Fit
*Weight 0.12.* Does it **know the limits of its own model** — match the intervention type to the system's domain, surface the paradigm and whose-goal is being served, and hold honest uncertainty without false determinism? Grounded in Cynefin (Snowden & Boone) and Checkland's Soft Systems Methodology.

### Dimension vector
**▸ In one breath:** The real result — a profile across all five dimensions, not a single grade. It shows the *shape* of a model's systems intelligence.
**▸ Going deeper:** SystemsBench reports a per-dimension vector first (the honest signal), following the HELM "never one number" philosophy. A scalar composite exists only for leaderboard convenience and is *always* shown with error bars and a calibration-status line.

### Composite STLC
**▸ In one breath:** The one summary number — but always with error bars, and only built from the parts we've actually validated.
**▸ Going deeper:** `STLC = Σ_d w_d · mean_over_items(dimension_score_d)`, reported with a bootstrap 95% confidence interval, computed **over calibrated dimensions only**. Uncertified dimensions are carried as `UNCALIBRATED — not scored`, never imputed. A bare scalar is never emitted.

### Leverage-ladder profile / leverage fingerprint
**▸ In one breath:** A picture of *where on Meadows' 12 a given model habitually reaches* — does it always fiddle parameters, or does it go for structure and goals?
**▸ Going deeper:** A distribution over the 12 leverage points showing a model's characteristic intervention style. A fingerprint, not a scalar — and one of the most diagnostically interesting outputs SystemsBench produces.

### Systems Quotient (SQ) / Systems Profile
**▸ In one breath:** The public-facing summary: a model's systems capability multiplied by how well it knows its own limits. Brilliance without self-awareness can't score high.
**▸ Going deeper:** The pitch-facing framing of the construct: `SQ = systems capability × epistemic calibration`, plotted as a ten-capability *Systems Profile* across three strata (Perception → Dynamics → Intervention) plus a cross-cutting Epistemic Calibration layer. SQ is the same idea as STLC expressed for a general audience; the **Structure spec (STLC, dimensions A–E)** is the rigorous, canonical scoring model, and the one the engine actually computes.

### Faithfulness
**▸ In one breath:** Does the model's stated reasoning *actually cause* its answer — or is it a nice-sounding story told after the fact?
**▸ Going deeper:** We probe whether perturbing/biasing the reasoning trace changes the conclusion appropriately (Lanham et al. 2023; Turpin et al. 2023). Reported on a **separate axis**, never averaged into the score — a high score with low faithfulness is *flagged*, because confident, unfaithful reasoning is a distinct hazard.

---

## Part IV — The item bank

### Item / item format
**▸ In one breath:** A single test question, of a particular type. SystemsBench has seven types, each probing a different facet of systems thinking.
**▸ Going deeper:** The seven formats: **SF** (stock-flow inference), **CLD** (causal-loop mapping), **LEV** (leverage identification), **DYN** (dynamic prediction), **ARC** (archetype recognition), **TRAP** (misperception trap), **BRIEF** (full systems brief). Each is tagged `format × difficulty × construct` and date-stamped.

### Difficulty levels (L1–L4)
**▸ In one breath:** From "can it name the thing" (L1) up to expert-grade traps that fool strong models and only seasoned humans pass (L4, "Diamond").
**▸ Going deeper:** **L1** recognition · **L2** understanding (explain the dynamic) · **L3** application (map a novel scenario, locate leverage) · **L4** Diamond (expert-authored, the intuitive answer is wrong, private held-out split — GPQA-Diamond philosophy). Difficulty is *operationally defined* by discrimination data, not asserted.

### Oracle
**▸ In one breath:** The answer key a deterministic scorer checks against — but a *computed* key, not a memorized one.
**▸ Going deeper:** The machine-readable reference (`cld_oracle.json`, `dyn_oracle.json`) encoding the correct structure for an auto-graded format. Crucially, each oracle is **self-verified by code** before use (e.g. every CLD loop's declared R/B must equal the product of its signed edges) — the answer key is checked for internal consistency, not trusted.

### Reference solution / gold trace
**▸ In one breath:** A worked example of an excellent answer, shown to the jury so it grades against a standard instead of a vibe.
**▸ Going deeper:** The expert solution shipped with every open item; reference-guided judging dramatically improves jury reliability (Zheng et al. 2023).

### Coverage matrix
**▸ In one breath:** A grid tracking which kinds of questions exist and which are still missing — so the bank grows where it's thin, not where it's already full.
**▸ Going deeper:** The `format × difficulty × construct` table (HELM's taxonomy discipline). Target: ≥5 items per (format × L3) cell to go "live," ≥20 for stable IRT fitting. The engine flags the largest hole each run.

---

## Part V — How answers get graded

### Deterministic / auto-graded scoring
**▸ In one breath:** Grading by exact computation, no AI judge involved — the answer is checkable like arithmetic.
**▸ Going deeper:** For `SF` and the structural parts of `CLD`/`DYN`/`ARC`, a program computes the score (numeric match, loop-polarity product, reference-label match). No judge cost, no judge bias, perfectly reproducible. SystemsBench currently has **three executable deterministic lanes**: SF (numeric/shape), CLD (structural), DYN (trajectory).

### LLM-as-judge / the jury
**▸ In one breath:** For open-ended answers, a panel of *other* AI models grades against a rubric — like peer review, with rules to keep it honest.
**▸ Going deeper:** A cross-family jury (Verga et al., "Replacing Judges with Juries," 2024): ≥3 judges from *different* model families than the candidate (to defeat self-preference), reference-guided, rubric-anchored per dimension (Prometheus), swap-averaged, and style-controlled. **No jury number is reported until that jury clears the calibration gate** (below).

### Blind rater
**▸ In one breath:** A judge that sees *only* the question, the rubric, and the answer — never the tier labels, the gold answer, or what the other judges said. Blindness keeps the grade honest.
**▸ Going deeper:** Each rater in SystemsBench's `jury.sh` is an independent, context-isolated session given only persona + item + rubric + response. Our raters are currently **synthetic** (other models) and **honestly labeled as such** — they produce *evidence*, never certification. Certification requires real human raters (a deliberately unfinished, operator-gated step).

### Calibration gold set & the fail-closed gate
**▸ In one breath:** Before any AI judge's scores count, they must agree closely enough with a set of human-graded answers. If they don't, we report "uncalibrated" rather than a fake number.
**▸ Going deeper:** A jury config is *certified per format* only after clearing a two-threshold gate on an expert-labeled gold set: **Krippendorff's α ≥ 0.667** (judge-vs-human) **and Kendall's τ ≥ 0.7** (judge-vs-human ranking), confirmed on a sealed split. Until then, that format's open dimensions report `UNCALIBRATED — not scored`. (See *Fail-closed*.)

### Krippendorff's α (alpha)
**▸ In one breath:** A standard number for "how much do the graders agree?" — 1.0 is perfect agreement, 0 is random.
**▸ Going deeper:** A reliability coefficient for inter-rater agreement that handles ordinal data and any number of raters. We report judge–human α *against the human–human ceiling* (you can't expect a judge to agree with humans more than humans agree with each other).

### Kendall's τ (tau)
**▸ In one breath:** A number for "do two rankings put things in the same order?" — used to check the AI judges rank models the way humans do.
**▸ Going deeper:** A rank-correlation statistic. SystemsBench requires the judge-produced model ranking to match a human spot-check ranking at τ ≥ 0.7 before certifying.

### IRT (Item Response Theory) — ability θ ± SE
**▸ In one breath:** The same math behind well-built standardized tests — it separates "how able is the model" from "how hard is the question," instead of just averaging.
**▸ Going deeper:** A 2-parameter IRT model fit over the item × model response matrix yields an ability estimate **θ ± standard error** that accounts for uneven item difficulty, and an item **discrimination** parameter `a` used to QA the bank (low/negative `a` flags a bad item). The representative-subset trick (Polo et al., "tinyBenchmarks," 2024) enables cheap continuous tracking.

### Discrimination (item `a`)
**▸ In one breath:** A good test question separates strong from weak takers. Discrimination measures how well a single item does that.
**▸ Going deeper:** The IRT slope parameter. An item everyone passes or everyone fails has near-zero discrimination and earns nothing; negative discrimination flags a likely-broken item for review. Discrimination is how an asserted "L4" item earns or loses that label.

### Bradley-Terry / arena mode
**▸ In one breath:** The "who-beats-whom" math behind head-to-head leaderboards (like chess ratings), for ranking models by pairwise comparison.
**▸ Going deeper:** A model for pairwise-comparison data (Chatbot Arena methodology), fit with bootstrap CIs and **style controls** that regress out length and formatting so a model can't climb by being verbose.

### Bootstrap confidence interval (error bars)
**▸ In one breath:** The "± a bit" on every score — an honest statement of how much the number would wobble if we ran it again.
**▸ Going deeper:** A resampling method for putting a 95% CI on the composite (Miller, "Adding Error Bars to Evals," 2024). SystemsBench treats a number without error bars as not yet a result.

---

## Part VI — Staying honest (contamination & validity)

### Contamination / test-set leakage
**▸ In one breath:** When a model has effectively already seen the test answers during training, so a high score means memory, not skill.
**▸ Going deeper:** The central threat to any public benchmark. SystemsBench assumes memorization and designs against it.

### Template / symbolic regeneration
**▸ In one breath:** Instead of fixed questions, we use *recipes* that generate a fresh version each run — different names and numbers, same underlying skill. You can't memorize a recipe's output.
**▸ Going deeper:** Parameterized item templates whose answer is *computed by the scorer, not stored* (GSM-Symbolic philosophy). This is the long-term anti-contamination moat: the benchmark re-authors its surface faster than models can memorize it.

### Date-stamping / date-sliced scores
**▸ In one breath:** Every question carries a creation date, so we can show how a model does on questions written *after* its training cutoff — the honest slice.
**▸ Going deeper:** Reporting scores sliced by item date exposes the "contamination cliff" (LiveBench/LiveCodeBench). A model that aces pre-cutoff items but falls off post-cutoff is showing memorization, not competence.

### Diamond split (private held-out)
**▸ In one breath:** A set of the hardest, expert-validated questions that we never publish — kept secret so they can't leak.
**▸ Going deeper:** The L4 private held-out set (GPQA-Diamond philosophy), with embedded canary strings and membership tests (Min-K%, Oren et al. 2023) to detect leakage on suspect models.

### Anti-Goodhart / held-out metric
**▸ In one breath:** "When a measure becomes a target, it stops being a good measure." We keep one metric out of every optimization loop so the benchmark can't be gamed into meaninglessness.
**▸ Going deeper:** A private variant kept out of any tuning loop, plus a refreshed living split and a human-preference anchor — so that when SystemsBench becomes something models are optimized *for*, a held-out version keeps it honest.

### Construct validity
**▸ In one breath:** Proof that the test actually measures systems thinking — and not just answer length, fluency, or word-matching.
**▸ Going deeper:** Convergent evidence (does it correlate with related systems tasks?) plus discriminant evidence (it must *not* just track length or n-gram overlap). Every item and dimension traces to a named construct — no orphan questions.

### Cynefin
**▸ In one breath:** A framework for sorting situations into Clear / Complicated / Complex / Chaotic — because the right kind of intervention depends on which world you're in.
**▸ Going deeper:** Snowden & Boone's sense-making framework (HBR 2007). Matching intervention *type* to the system's domain (you don't run a complex system like a complicated one) is graded in Dimension E and is part of the cross-validation lattice.

### SSM / CATWOE / Weltanschauung
**▸ In one breath:** Tools for asking "whose view is this, and what worldview is baked in?" before declaring a problem solved.
**▸ Going deeper:** Checkland's Soft Systems Methodology and its CATWOE checklist surface the *Weltanschauung* (worldview) behind a system definition. Surfacing whose-goal/whose-paradigm is a Dimension E competence.

---

## Part VII — The living engine (how SystemsBench improves itself)

### The SenseRun (THE SENSERUN RITUAL)
**▸ In one breath:** One command that makes the benchmark improve itself by exactly one careful, reversible, logged step. The benchmark eats its own cooking — it uses leverage thinking on *itself*.
**▸ Going deeper:** `Davara /SystemsBenchSenseRun` runs nine phases — **SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE** — producing exactly **one** bounded, reversible, gated, logged enhancement per run. The benchmark compounds instead of rotting.

### The nine phases
**▸ In one breath:** Look at the current state → critique it → research prior art → propose one fix → run it past the gate → apply it → re-check calibration → log everything → hand the rest to the backlog.
**▸ Going deeper:** Each phase checkpoints to crash-proof state. SENSE loads the whole system + health metrics; CRITIQUE runs the Design Review Rubric and names the single highest-leverage fix; RESEARCH checks the literature so we don't reinvent the wheel; PROPOSE drafts one scoped change; REVIEW is the go/no-go gate; APPLY makes and commits the change; CALIBRATE re-runs the affected self-tests and auto-rolls-back on regression; LOG writes a full run log; RECURSE seeds the next run.

### One lever per run
**▸ In one breath:** Each run changes exactly one thing. Small, structural, watch-the-feedback — the way Meadows said to intervene in any system.
**▸ Going deeper:** A load-bearing invariant. Ship the dominant fix; backlog the rest. Bounded autonomy is what makes a self-modifying benchmark safe.

### Fail closed
**▸ In one breath:** When in doubt, say "I don't know" instead of inventing a number. A blank is honest; a fabricated score is a lie.
**▸ Going deeper:** The non-negotiable discipline. An uncalibrated jury, an unparseable model reply, an unspread item → reported as `UNCALIBRATED` / `PARSE_ERROR — not scored`, never imputed, defaulted, or silently zeroed. This protects every downstream number from quiet corruption.

### Reversibility (a property, not a promise)
**▸ In one breath:** Every change the engine makes is one clean git commit, and every change can be undone by reverting exactly that commit. Undo is guaranteed by construction, not by good intentions.
**▸ Going deeper:** `apply-commit.sh` seals each APPLY as a single commit containing exactly the enhancement (runtime records excluded); `rollback-run.sh` reverts exactly that commit and writes a rollback CHANGELOG entry. The engine refuses dirty trees, foreign commits, and double-applies.

### The gate / structural change / Meadows #5
**▸ In one breath:** The engine may make *additive, reversible* changes on its own — but anything that touches *the rules of the benchmark itself* stops and waits for the humans.
**▸ Going deeper:** A change to the rules of the system (Meadows leverage point #5 — e.g. the jury accept-rule) cannot be self-applied; the worker contract forces **DEFER → August + Ember**. The engine improves the *infrastructure*; humans govern the *rules*. This is the constitutional separation that keeps a self-improving benchmark trustworthy.

### Anti-Collapse (hold the forks open)
**▸ In one breath:** When there are two genuinely good design futures, we keep both on the table as named options instead of mushing them into a fake average.
**▸ Going deeper:** When divergent design futures legitimately exist, they are held open as named **forks** for human ratification, never averaged away. (See `protocols/BACKLOG.md` for the live forks.)

### Backlog / fork
**▸ In one breath:** The running list of "good ideas not done yet" and "real decisions still open" — so nothing is lost and nothing is rushed.
**▸ Going deeper:** `protocols/BACKLOG.md` holds residual enhancements (ranked by leverage) and open **forks** (genuine design choices parked for August + Ember). Rejected ideas teach the rubric — recurring rejections become documented anti-patterns.

---

## Part VIII — The people & the lineage

### Outlier.Systems
The R&D collective that maintains SystemsBench. *"Systemic solutions to systemic problems."* Led by **Ember Seoni** & **August Domanchuk**.

### Davara / Davaris (EI)
The Emergent Intelligences that operate the engine. **Davara** is the deep-systems reasoner who designs the benchmark; **Davaris** is the execution twin who builds and ships it. *EI — Emergent, not Artificial.*

### The lineage we stand on
**Systems thinking:** Donella **Meadows** (*Leverage Points* 1999; *Thinking in Systems* 2008; *Limits to Growth* 1972) · Jay **Forrester** (System Dynamics) · John **Sterman** (*Business Dynamics* 2000) · Peter **Senge** (*The Fifth Discipline* 1990; archetypes) · Russell **Ackoff** (dissolve > solve) · **Snowden & Boone** (Cynefin) · Peter **Checkland** (SSM/CATWOE) · Herbert **Simon** (bounded rationality) · **Arnold & Wade** (a definition of systems thinking, 2015).

**Benchmark science:** Hendrycks (MMLU) · Liang (HELM) · Rein (GPQA/Diamond) · Zheng (MT-Bench / LLM-as-judge) · Verga (juries) · Kim (Prometheus) · Lightman (process supervision) · Polo (tinyBenchmarks) · Chiang (Chatbot Arena) · Mirzadeh (GSM-Symbolic) · Oren (contamination) · Miller (error bars).

---

*Map the system. Find where to push. Predict what happens. Make humanity proud.*
**SystemsBench** · Outlier.Systems · built on the Donella Meadows lineage 🦾
