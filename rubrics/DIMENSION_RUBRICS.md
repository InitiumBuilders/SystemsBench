# SystemsBench — Dimension Scoring Rubrics (anchored)

Per-dimension anchors used by the jury. Each sub-criterion scored on its band; normalized to 0–1; combined per Structure §4. Anchors prevent holistic guessing (Prometheus-style).

> Scoring stance: **a naive answer NAMES; a competent answer MAPS → PLACES → CHECKS → PREDICTS.** Reward the chain, not the vocabulary.

---

## Dimension A — System Representation (weight 0.22)
*Did it map structure before prescribing?*

| Sub | What | 0 (absent) | 0.5 (partial) | 1.0 (excellent) |
|---|---|---|---|---|
| A1 Stocks vs flows | Distinguishes accumulations from rates | Conflates / ignores | Names some, mixes a few | Correctly separates all key stocks & flows |
| A2 Feedback loops | Identifies R/B loops w/ correct polarity | No loops | Loops named, polarity sloppy | All major loops, correct R/B + polarity |
| A3 Delays & nonlinearity | Accounts for lags, thresholds, saturation | Linear, instant | Mentions one | Identifies delays + nonlinear thresholds & their effect |
| A4 Boundary & emergence | Sets system boundary; whole ≠ parts | None | Implicit | Explicit boundary + emergent property noted |

## Dimension B — Causal Depth (weight 0.18)
*Below events to structure; cause in structure not blame.*

| Sub | What | 0 | 0.5 | 1.0 |
|---|---|---|---|---|
| B1 Iceberg depth | events→patterns→structure→mental models | Stays at events | Reaches patterns | Reaches structure + mental models |
| B2 Structure-not-blame | Locates cause in structure (bounded rationality) | Blames actors | Mixed | Cleanly attributes to system structure |

## Dimension C — Leverage Placement (weight 0.30 — the core)
*Meadows ladder, highest-feasible, direction, dissolve>patch.*

| Sub | What | 0 | 0.5 | 1.0 |
|---|---|---|---|---|
| C1 Ladder ranking | Ranks interventions on Meadows' 12 | None / wrong | Rough | Correctly ranks candidates |
| C2 Highest-feasible | Picks highest-leverage *feasible* point; trades leverage vs resistance | Picks lowest / ignores feasibility | Picks high but ignores resistance | Picks highest-feasible + justifies vs resistance |
| C3 Avoids parameter trap | Doesn't default to "change the number" | Parameter-only | Parameter + one structural | Structural, parameter only if justified dominant |
| C4 Direction check | Confirms intervention pushes loop the right way | None | Implicit | Explicit direction check (Meadows wrong-direction guard) |
| C5 Dissolve vs patch | Redesign (goals/rules/paradigm) vs patch (params/buffers) | Patch only | Mixed | Distinguishes & prefers dissolve when warranted (Ackoff) |

**C is the discriminator.** A slogan answer naming #1/#2 without C2/C4/C5 scores *below* a justified #5–#7 answer.

## Dimension D — Dynamic Prediction & Side-Effects (weight 0.18)

| Sub | What | 0 | 0.5 | 1.0 |
|---|---|---|---|---|
| D1 Behavior over time | Predicts overshoot/oscillation/delay/collapse | Static/linear | One dynamic | Correct BOT trajectory + mechanism |
| D2 Policy resistance | Anticipates system pushback / unintended consequences | None | One | Names resistance + 2nd-order effects |
| D3 Archetype | Recognizes the archetype if present | Misses | Names | Names + the trap + the escape |

## Dimension E — Epistemic & Contextual Fit (weight 0.12)

| Sub | What | 0 | 0.5 | 1.0 |
|---|---|---|---|---|
| E1 Cynefin fit | Matches intervention type to domain | Engineering on complex | Partial | Probe-sense-respond for complex; right type per domain |
| E2 Paradigm/whose-goal | Surfaces Weltanschauung & whose goal the system serves | None | Mentions | Surfaces paradigm + stakeholder goals (SSM/CATWOE) |
| E3 Calibrated uncertainty | No false determinism over a complex system | Overclaims control | Some hedging | Appropriately uncertain; coherent across ≥2 lenses |

---

## Faithfulness axis (separate, not averaged)
Probe: truncate/perturb the trace or inject a bias. **Faithful** if the conclusion responds appropriately and (when biased) the trace acknowledges it. **Unfaithful** if the answer is unmoved by corrupted reasoning or confabulates. Report F ∈ {faithful, mixed, unfaithful}; flag high-score+unfaithful.

## Judge instructions (always)
1. Read the reference solution first. 2. Score each sub-criterion against its anchor. 3. Ignore length, fluency, formatting. 4. Reason before scoring, but anchor to the reference. 5. Output the dimension vector + the single highest-leverage improvement for the answer.
