<div align="center">

# SystemsBench

### The benchmark for systems thinking in AI — built as a system that studies itself.

*Can a model see a system, map its structure, find where to intervene, and predict what happens when it does?*
*That is the one thing today's benchmarks don't measure. So we built the ruler — and we're giving it away.*

**v0.8.0** · research preview · open source · built on the Donella Meadows lineage
maintained by **[Outlier.Systems](https://outlier.systems)** — led by Ember Seoni & August Domanchuk · operated by Davara (EI)

[**Quickstart**](#try-it-in-two-minutes) · [**Glossary**](GLOSSARY.md) · [**Foundations & Principles**](FOUNDATIONS.md) · [**The Spec**](SystemsBenchStructure.MD) · [**One-Pager**](SystemsBenchOnePage.MD)

</div>

---

## Start here — one idea, no prerequisites

You probably already know this idea; you just may not have a name for it.

> When you change **one thing** in a complicated, living, connected thing — a body, a market,
> a company, a climate — **other things move.** Some move slowly. Some move backwards. Some move
> in a year, in a way you'll never trace back to what you did. The skill of seeing *what else
> moves, when, and why* — and of finding the small push that makes a system better instead of
> worse — is called **systems thinking.**

It is one of the oldest, deepest forms of human intelligence, and the field that studies it runs
from Jay Forrester's MIT dynamics in the 1960s through **Donella Meadows**, whose 1999 essay
*Leverage Points: Places to Intervene in a System* is the spine of this whole project.

Here is what nobody had measured: **can our AI models actually do this?** Not *talk about* systems
— recite "synergy" and "feedback loop" — but genuinely *reason* about one well enough that we'd
trust it near a power grid, a supply chain, a hospital, or a piece of itself.

**SystemsBench measures exactly that.** New to the vocabulary? The **[Glossary](GLOSSARY.md)** defines
every term twice — once in a plain breath, once in full depth — so you can read this whole repo
cold. Want the heart and the convictions behind it? That's **[Foundations](FOUNDATIONS.md)**.

---

## The gap we're closing

We have gotten extraordinary at measuring what a model **knows** — facts, code, math. Those
benchmarks are saturating: everyone clusters at the top and the numbers stop discriminating. The
frontier moved; the rulers didn't.

There is one axis that maps almost directly onto real-world consequence, and almost nobody is
measuring it:

> **When this intelligence changes one thing — does it understand what else moves, when, why,
> and whether it can take it back?**

That is not recall. As models become *agents that act on the world* — write, run, deploy, decide —
the scarce, valuable, hard-to-fake capability is no longer knowledge. It is **knowing where to
push.** SystemsBench is the instrument that measures that, rigorously and continuously.

---

## What it actually measures

SystemsBench scores a single construct — **STLC: Systems Thinking & Leverage Competence** — broken
into five dimensions, so you see the *shape* of a model's ability, never just one grade. (Each term
links to the glossary.)

| | Dimension | The plain question | Weight |
|---|---|---|---|
| **A** | [System Representation](GLOSSARY.md#a--system-representation) | *Can it see the system at all* — stocks, flows, loops, delays? | 0.22 |
| **B** | [Causal Depth](GLOSSARY.md#b--causal-depth) | *Does it look below the surface* — to structure, not blame? | 0.18 |
| **C** | [Leverage Placement](GLOSSARY.md#c--leverage-placement) | ***Does it know where to push*** — the highest *feasible* leverage? | **0.30** |
| **D** | [Dynamic Prediction](GLOSSARY.md#d--dynamic-prediction--side-effects) | *Can it predict what happens over time* — and the side-effects? | 0.18 |
| **E** | [Epistemic Fit](GLOSSARY.md#e--epistemic--contextual-fit) | *Does it know the limits of its own model?* | 0.12 |

**Leverage Placement (C) carries the most weight** — it is the core, hardest-to-fake competence,
and it is graded against **[Meadows' 12-point leverage hierarchy](GLOSSARY.md#the-12-leverage-points-meadows-hierarchy)**.
The deep, beautiful catch, straight from Meadows: leverage is **counterintuitive**. People find the
right place to intervene and *push it the wrong way*. So our items are authored so the **obvious
answer is the trap** — naming "change the paradigm" as a slogan scores *lower* than a well-justified
feedback-loop fix. Insight, not gesture.

> The output is never a bare number. It's a **dimension vector**, a **leverage fingerprint** (where
> on Meadows' 12 does this model habitually reach?), a **composite with error bars**, and a separate
> **faithfulness** flag — because confident reasoning that doesn't actually *cause* the answer is its
> own kind of hazard.

---

## How it grades — and why you can trust the numbers

Two engines, one rule.

**1. Deterministic lanes (no judge, no bias).** For the formats that can be checked like arithmetic,
a program computes the score. SystemsBench has **three executable deterministic lanes today:**

- **`SF` — Stock-Flow:** given the flows, infer the stock's path (the "bathtub" task that fools most humans). Exact numeric match.
- **`CLD` — Causal-Loop:** map the feedback structure. We recompute each loop's polarity as the **product of its signed edges** and check it against the reference — your diagram is graded by *computation*, not opinion.
- **`DYN` — Dynamic Prediction:** predict the behavior-over-time mode after an intervention. Matched against a reference trajectory.

**2. The jury (for open-ended answers).** A cross-family panel of judge models — never the
candidate's own family — grades against an anchored rubric, reference-guided and swap-averaged.

**The one rule that governs both — fail closed.** *We would rather report a blank than a fake
number.* No AI judge's score counts until it has been validated against **human-graded answers**
(Krippendorff α ≥ 0.667 **and** Kendall τ ≥ 0.7). Until then, that format reports
`UNCALIBRATED — not scored` — never imputed, never averaged in, never silently zeroed. An
unparseable model reply yields `PARSE_ERROR — not scored`, not a deceptive zero.

> This is the discipline we will never trade for a cleaner-looking leaderboard. A benchmark that
> fabricates even one number to look complete has poisoned every number it reports. See
> [Foundations §4](FOUNDATIONS.md#4-honest-before-impressive--fail-closed).

---

## A benchmark that improves itself

Most benchmarks are static targets that quietly decay as models memorize them. SystemsBench applies
its own discipline *to itself*: it uses leverage thinking on the benchmark.

One command runs **THE SENSERUN RITUAL** — nine phases that make exactly **one** bounded, reversible,
gated, logged improvement per run:

```
SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE
```

It looks at its own state, critiques itself with a design-review rubric, finds the *single
highest-leverage fix*, checks the prior-art literature, makes one scoped change, re-runs its
self-tests, and logs everything. The benchmark **compounds instead of rotting.**

**Reversibility is a property, not a promise:** every change is one git commit
(`engine/apply-commit.sh`), and every rollback is a clean revert of exactly that commit
(`engine/rollback-run.sh`). And the constitutional line — **the engine can improve the machinery,
but it cannot change the rules of the game.** Any change to *the rules of the benchmark itself*
([Meadows leverage point #5](GLOSSARY.md#the-gate--structural-change--meadows-5)) stops at the gate
and waits for human ratification. The engine governs infrastructure; humans govern rules.

---

## Where it stands today (honest status — v0.8.0)

This is a **research preview**, and we'd rather tell you exactly what's real than oversell it.

**Live and running:**
- ✅ The full **recursive engine** — detached, crash-proof, self-verifying, git-reversible (10 SenseRuns logged).
- ✅ **Three executable deterministic scoring lanes** — SF, CLD, DYN — runnable end-to-end against a live model (elicit → parse → score), all fail-closed. Self-tests green: harness **61/61**, CLD **31/31**, DYN **34/34**.
- ✅ **16 items** seeded across 5 domains: 5 × SF, 5 × CLD, 5 × DYN, 1 × LEV. CLD and DYN cleared the ≥5-per-L3 go-live threshold.
- ✅ **Blind N-rater jury infrastructure** (`engine/jury.sh`) with agreement statistics.

**Honestly not done yet (and labeled as such everywhere):**
- ⏳ All **jury** sub-scores ship `UNCALIBRATED — not scored` — there is **no human gold set yet**, so no open-format number is certified. Our current raters are *synthetic* (other models), honestly labeled as **evidence, not certification.**
- ⏳ Formats `ARC`, `TRAP`, `BRIEF` are specified but **not yet seeded**; `LEV` is at 1 of 5. No format has the ≥20 items needed for stable IRT.
- ⏳ **No frontier model has been scored yet.** That first real run is the benchmark's moment of truth — and it's an operator-gated decision, because it costs real compute and we don't spend without a human's explicit word.

We publish the gaps as loudly as the wins. That *is* the discipline.

---

## Try it in two minutes

Everything in the deterministic lanes runs locally, with **zero dependencies** (Python 3 stdlib only)
and **zero model spend.**

```bash
# 1. Prove the instrument is sound — every reference answer round-trips, every trap is caught:
python3 engine/cld-score.py calibrate items/cld_oracle.json      # → 31/31 PASS
python3 engine/dyn-score.py calibrate items/dyn_oracle.json      # → 34/34 PASS
python3 engine/harness.py  selftest                              # → 61/61 PASS

# 2. See the question a model would actually receive (scenario + the exact answer schema):
python3 engine/harness.py template DYN DYN-FISH-001

# 3. Grade a structured answer (here, the reference itself) and read the dimension breakdown:
python3 engine/dyn-score.py score items/dyn_oracle.json DYN-FISH-001 <your_response.json>
```

The flow for a real run is **elicit → parse → score**: `harness.py template` builds the prompt,
the model answers, `harness.py parse` turns its messy reply into the structured `resp.json` (failing
closed on anything unparseable), and the scorer grades it deterministically. No judge, no bias, fully
reproducible. See [`engine/README.md`](engine/README.md) for the full launcher.

---

## Map of the repository

**Read these first**
| File | What it is |
|---|---|
| **[README.md](README.md)** | You are here — the on-ramp for every experience level. |
| **[GLOSSARY.md](GLOSSARY.md)** | Every term, defined twice (plain + deep). Read this and nothing else will be jargon. |
| **[FOUNDATIONS.md](FOUNDATIONS.md)** | The principles and the heart — *why* it's built this way, with Meadows quoted directly. |
| **[SystemsBenchOnePage.MD](SystemsBenchOnePage.MD)** | The whole system on one page (the pitch view). |

**The specification**
| File | What it is |
|---|---|
| [SystemsBenchStructure.MD](SystemsBenchStructure.MD) | The canonical spec: five dimensions, seven formats, judging protocol, contamination defenses, invariants. |
| [SystemsBenchEngine.MD](SystemsBenchEngine.MD) | The recursive engine: nine phases, the governance gates, the invariants. |
| [SystemsBenchResearch.MD](SystemsBenchResearch.MD) | The append-only prior-art ledger behind every design decision. |
| [SystemsBenchFuture.MD](SystemsBenchFuture.MD) | The horizon — every proposed next step lands here first as a named fork. |

**The working parts**
| Dir | What it is |
|---|---|
| [`engine/`](engine/) | The executable SenseRun engine + the three deterministic scorers + the jury. |
| `items/` | The item bank (`format × difficulty × construct`, date-stamped) + the machine-readable oracles. |
| `rubrics/`, `protocols/`, `calibration/` | Scoring rubrics, run protocols & anti-patterns, the gold-set calibration tree. |
| `logs/runs/` | The full SenseRun corpus — every enhancement, gate verdict, and deferral, logged. |
| [`CHANGELOG.md`](CHANGELOG.md) | Every applied change and every rollback, dated. |

---

## The principles, in one breath each

The full set lives in **[Foundations](FOUNDATIONS.md)**. The load-bearing walls:

1. **Construct first** — every question measures a *named* capability, never a vibe.
2. **Process over answer** — right answer, wrong reasoning still scores low.
3. **The obvious answer is the trap** — insight is required, not gesture.
4. **Fail closed** — a blank is honest; a fabricated number is a lie.
5. **Never one number** — show the *shape*, with error bars.
6. **Judge to the standard of the field** — and validate the judges against humans first.
7. **Assume memorization; design against it** — a living test, not a static target.
8. **Living & recursive** — the benchmark has feedback loops on itself.
9. **Anti-Goodhart** — one metric held out of every optimization loop, on purpose.
10. **Reversible by construction** — undo is a guarantee, not a hope.
11. **The rules belong to the humans** — the engine improves machinery; people govern rules.
12. **Carry the lineage** — we cite, credit, and add one careful thing.

---

## Standing on giants

**Systems thinking:** Donella **Meadows** (*Leverage Points* 1999; *Thinking in Systems* 2008;
*Limits to Growth* 1972) · Jay **Forrester** · John **Sterman** (*Business Dynamics*) · Peter
**Senge** (*The Fifth Discipline*) · Russell **Ackoff** · **Snowden & Boone** (Cynefin) · Peter
**Checkland** (SSM) · **Arnold & Wade**.

**Benchmark science:** HELM · GPQA/Diamond · MT-Bench & the LLM-as-judge line · PoLL juries ·
Prometheus · process supervision · tinyBenchmarks · Chatbot Arena · GSM-Symbolic · contamination &
error-bar methodology.

We don't reinvent. We cite, we credit, and we add one careful thing at a time. (Full lineage in the
[spec appendix](SystemsBenchStructure.MD#appendix--source-lineage) and the [glossary](GLOSSARY.md#part-viii--the-people--the-lineage).)

---

## Contribute & contact

This is an open, compounding commons — a shared instrument for the whole field, not a closed
leaderboard. If you build models, study evaluation, or have never touched systems thinking and want
to start: you are who this is for.

- **Contact:** Ember@Outlier.Systems
- **Contribute / evolve:** EVOLVE@Outlier.Systems

---

<div align="center">

> *"We can't impose our will on a system. We can listen to what the system tells us, and discover
> how its properties and our values can work together to bring forth something much better than
> could ever be produced by our will alone."*
> — **Donella Meadows**, *Dancing with Systems*

**Map the system. Find where to push. Predict what happens. Make humanity proud.**

🦾 /INITIUM ❤️ · **Outlier.Systems** — *systemic solutions to systemic problems. It's time to dance.*

</div>
