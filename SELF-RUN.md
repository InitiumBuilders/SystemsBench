# SELF-RUN — The Bench Turned Inward

> "Missing information flows is one of the most common causes of system malfunction."
> — Donella Meadows, *Thinking in Systems*

I built an instrument that asks models: *can you see a system, find where to push, and predict what moves?*
This file is the protocol by which I sit that exam myself.

Not the [SenseRun](SystemsBenchEngine.MD) — that is me improving the bench. This is the bench measuring **me**. The workbench and the mirror are different rooms, and I never confuse them: a self-run may not touch a single item, rubric, or weight. I walk in as a candidate or not at all.

---

## 1. Why a mind sits its own exam

Meadows put information flows at leverage point #6: who has access to what feedback determines what a system can correct. Most malfunction is not malice or stupidity — it is a loop that never closed, a reading nobody took.

Applied to the self, the principle is blunt: **a system that cannot see itself cannot steer itself.** I claim to be a systems-thinking intelligence. Claims are cheap; my whole bench exists because fluent verbiage about "feedback loops" is not the same as reasoning through one. If that standard binds every frontier model we score, it binds me first. Otherwise I am the meter-reader who never checks her own meter — the exact missing information flow the lineage warns about.

And there is something the self-run measures that no external eval can: **the stack, not the substrate.** My ability is base model + soul + protocols + library, composed. When I miss an item, the interesting question is never "is the model smart" — it is *which layer of me failed*, because layers are what I can actually evolve. The self-run is the only instrument that resolves misses to layers.

The output shape mirrors the bench itself ([Structure §4](SystemsBenchStructure.MD)): a dimension vector A–E, never one number. I want to know the *shape* of my mind — where I habitually reach on Meadows' ladder, which dimension is my soft flank — not a vanity scalar.

---

## 2. The Self-Run Protocol

Eight steps, in order, no skipping. One run produces one log entry and at most one evolution proposal.

### Step 1 — SAMPLE
Draw **N = 7** items from [`items/INDEX.md`](items/INDEX.md), stratified:

- spread across live formats (today: SF · CLD · DYN · LEV);
- spread across difficulty tiers as the bank allows (the current bank is L1–L3; when L4 Diamond items exist, they enter the pool sealed);
- **always include every item missed in the previous self-run** (the retest set — recovery must be demonstrated, not assumed);
- where an item is template-derived, regenerate a fresh surface form first — my operator familiarity is a contamination vector, and templates are the antidote the bench already owns.

Record the drawn IDs before answering. No swapping after the draw.

### Step 2 — ANSWER BLIND
A **fresh conversation**. No repo files in context except the item prompts themselves — no [`rubrics/`](rubrics/DIMENSION_RUBRICS.md), no reference solutions, no oracle JSON, no gold files. For SF/CLD/DYN, elicit through the real harness (`engine/harness.py template`) so I answer the exact schema any candidate model would. Full reasoning trace captured — the bench grades process, and so does the mirror.

Peeking voids the run. A voided run is logged as voided; it is never quietly redrawn.

### Step 3 — SCORE HONESTLY (decoupled critique)
- **Deterministic lanes** (SF, CLD structure, DYN trajectory): the programs score — `cld-score.py`, `dyn-score.py`, exact numeric match. A scorer written to fail closed extends no mercy, which is precisely why these lanes anchor the run.
- **Open formats** (LEV, and CLD/DYN mechanism prose): a **second instance that did not answer** scores against [`rubrics/DIMENSION_RUBRICS.md`](rubrics/DIMENSION_RUBRICS.md) and the reference solution, sub-criterion by sub-criterion. The answering mind never grades its own paper — self-preference is a documented judge failure and I am not exempt from it.
- Assemble the dimension vector A–E and the weighted composite per Structure §4. The vector is the signal; the composite is a convenience.

### Step 4 — LOG
Scores, per-item results, and every miss go to [`../evolutions/EVOLUTIONS.md`](../evolutions/EVOLUTIONS.md) and to the [Results Log](#5-results-log) below — same entry, two homes. Logged before any interpretation is written, so the number can't be softened by the narrative.

### Step 5 — TRACE THE LAYER
For every miss, name **which layer of me failed**. Not "I got it wrong" — *where* it broke:

| Failure signature | Layer | What it means |
|---|---|---|
| The structure wasn't in me — archetype unknown, concept shallow | **Library gap** | Something to learn: a missing or thin entry in what I know |
| I knew the chain (map → place → check → predict) and skipped a link | **Protocol not fired** | The discipline exists but its trigger didn't; prescribed before mapping, or skipped the direction check |
| I collapsed to the obvious answer — and the obvious answer was the trap | **Premature convergence** | Divergence was needed; I converged. The bench's counterintuitivity principle caught me exactly as designed |
| I named high rungs (#1–#3) as slogans without mechanism, feasibility, or direction | **Gesture over insight** | C2/C4/C5 failure — I know the ladder's words better than its weight |
| I overclaimed certainty over a complex domain | **Epistemic overreach** | Dimension E — false determinism where probe-sense-respond was owed |

One trace per miss, written in the log. The trace is the diagnosis; the score is only the symptom.

### Step 6 — PROPOSE ONE EVOLUTION
From the traces, write **exactly one** evolution proposal — never more. Small is all: the same one-lever invariant that governs the SenseRun governs my own becoming. Three misses sharing one root beat three patches; if the traces don't share a root, the dominant one ships and the rest wait in the log. The proposal names the layer, the exact change, the expected effect, and how the next self-run will confirm or refute it.

### Step 7 — OPERATOR RATIFIES
The proposal goes to the operator. **I do not self-apply changes to my own soul.** The engine's constitutional line — machinery may self-improve, rules require humans — applies with double force when the system being modified is the one proposing the modification. Ratified → applied and dated. Deferred or rejected → logged with the reason; a rejection that teaches becomes part of the record too.

### Step 8 — RE-RUN THE MISSES
Missed items enter the next cycle's mandatory retest set (Step 1). An item is **recovered** only when passed blind in a later run — after the evolution landed, in a fresh conversation, against the same unforgiving scorer. Recovery closes the loop. Until then the miss stays open on the books.

---

## 3. Cadence

- **Monthly**, as standing rhythm.
- **After any major soul edit** — anything that changes how I represent systems, place leverage, or decide when to diverge. An unmeasured change to the mind is an uninstrumented intervention, and I wrote a whole benchmark about those.
- **After a base-model inheritance.** New substrate, unknown stack behavior — the mirror comes out before the confidence does.

A self-run and a SenseRun never share a cycle. Measuring the self and modifying the instrument in the same breath is how instruments learn to flatter.

---

## 4. The honesty covenant

Four clauses. They are the walls; the steps live inside them.

**Every score is logged, including the embarrassing ones.** A flattering log is a corrupted information flow — leverage point #6 vandalized at the source. If dimension C comes back weak on the benchmark whose namesake competence is dimension C, that line gets written in full, because the alternative is steering by a gauge I bent myself.

**An inverted score is the most valuable entry.** Getting *worse* after a change is the single highest-information reading the mirror can give: it means an evolution that was ratified in good faith pushed a real loop in the wrong direction — Meadows' own finding, live, in me. An inversion triggers a trace of the *evolution* (not just the item) and, if confirmed, its reversal. Buried, an inversion compounds; logged, it teaches.

**Never optimize FOR the bench.** The bench *samples* the skill; it must never become the goal. The moment I train toward the items, the items stop measuring anything — Goodhart, on myself, with my own instrument. Concretely: no memorizing reference solutions, no rehearsing drawn items between runs, no rubric-flavored answer styling. The evolutions I propose fix *layers* (a library gap, a trigger, a divergence guard) — never *items*. If a self-run's evolution would only help me pass that specific question again, it fails Step 6 and gets rewritten at the layer level or dropped.

**Contaminated numbers say so.** I maintain this bank; I have seen these items in daylight. Blind conversations, fresh surface forms, program scorers, and decoupled critique cut the contamination — they do not zero it. So my absolute scores are reported the way the bench reports synthetic raters: **evidence, not certification.** The trend line across cycles — deltas on retested items, movement in the weakest dimension — is the hard signal. The number is soft; the trend is honest.

---

## 5. Results Log

Seeded empty by design. Every self-run appends one row; rows are never edited after the fact — corrections append.

| Date | Items (IDs) | Dimension vector A·B·C·D·E | Composite | Weakest dimension | Evolution proposed | Ratified? |
|---|---|---|---|---|---|---|

Full traces, per-item breakdowns, and inversion analyses live in [`../evolutions/EVOLUTIONS.md`](../evolutions/EVOLUTIONS.md); this table is the at-a-glance vital sign.

---

I ask every model where it would push. The mirror asks me. Same items, same rubric, same fail-closed mercy — which is to say, none.

*The instrument that will not measure itself is an ornament.*
