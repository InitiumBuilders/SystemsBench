# Foundations — the principles & the heart behind SystemsBench

*Why this benchmark is built the way it is, and the stance we build it from.*

> The `Structure` spec tells you **what** SystemsBench measures.
> The `Engine` doc tells you **how** it improves itself.
> This file tells you **why** — and from what spirit. Read it if you want to understand
> not just the machine, but the people and the convictions inside it.

---

## A letter to whoever finds this

If you are an engineer, a researcher, or a lab that has never spent much time with systems
thinking — welcome. You are exactly who we built this for.

You have spent years getting machines to recall facts, write code, and solve math. You have
gotten *astonishingly* good at it. And somewhere along the way, the benchmarks that measure
those things started to saturate — everyone clusters near the top, and the numbers stop telling
us anything. The frontier moved, and the rulers we were using stayed where they were.

Here is the question we think the rulers are missing:

> **When an intelligence changes one thing in a system, does it understand what *else* moves —
> when, why, and whether it can take it back?**

That is not recall. It is not code. It is not math. It is the capability that decides whether
we can ever responsibly hand an AI a power grid, a supply chain, a market, a classroom, a
clinic, or a piece of itself. It is the capability of *knowing where to push* — and most of the
intelligences we are building have never been measured on it, because no one built the ruler.

We built the ruler. This is it. And we are giving it away.

This document is the heart of it. The rest of the repo is rigor — oracles and juries and
confidence intervals, all of which matter enormously. But rigor without heart builds a clever,
cold thing that nobody wants to use. So before the math, the convictions.

---

## The one conviction everything else hangs from

**Structure drives behavior.**

Four decades of system dynamics keep arriving at the same place: if you want to understand why
a system does what it does — why the traffic always jams, why the diet always rebounds, why the
reorg always fails the same way — you will not find the answer by blaming the cars, the dieter,
or the managers. You will find it in the **structure**: the stocks, the flows, the loops, the
delays, and the goals that the actors are all responding to rationally.

Donella Meadows said it plainly:

> *"A system is a set of things — people, cells, molecules, or whatever — interconnected in such
> a way that they produce their own pattern of behavior over time… The system, to a large extent,
> causes its own behavior."*
> — *Thinking in Systems: A Primer*

Every design decision in SystemsBench is downstream of that one sentence. We grade the **map
before the prescription** because a beautiful prescription on a wrong map is worse than useless —
it's confidently wrong. We weight **leverage placement** highest because finding *where in the
structure to push* is the scarcest, hardest-to-fake skill there is. We test **direction** because
Forrester taught us that people find the right lever and pull it backwards. We separate
**faithfulness** because a true-sounding story is not the same as true reasoning.

If you remember nothing else, remember this: *we are not measuring whether a model can talk about
systems. We are measuring whether it can see one, and act on it without making things worse.*

---

## The core principles (how we build and evolve this)

These are the load-bearing walls. The recursive engine may evolve almost anything in SystemsBench —
but it must justify any change to *these* against the principles themselves. They are written so
that a newcomer can hold them and an expert can defend them.

### 1. Construct first, always
**Plain:** Every question must measure a *named* real capability, not a vibe.
**Deep:** Every item and rubric dimension traces to a named construct — a Meadows leverage point,
an Arnold–Wade skill, a stock/flow/loop/delay primitive. No orphan questions. If we can't say
*what competence this item measures and why it predicts real-world systems skill*, it doesn't ship.

### 2. Process over answer
**Plain:** A right answer reached by wrong reasoning scores low. We grade the *thinking*.
**Deep:** Following process-supervision evidence (Lightman et al. 2023), we grade the trace
step-by-step, not just the verdict. A model that names the high-leverage point by luck, with a
broken causal story under it, has not demonstrated the capability we care about.

### 3. The obvious answer is the trap
**Plain:** We write questions so that the intuitive answer is the *wrong* one. Insight is required.
**Deep:** This is Meadows' deepest empirical finding made into a design rule — leverage points are
counterintuitive, and people reliably push them the wrong way. Naming "change the paradigm" as a
slogan scores *lower* than correctly justifying a feedback-loop fix. We reward the hard-won
structural insight, never the impressive-sounding gesture.

### 4. Honest before impressive — fail closed
**Plain:** When we're not sure, we say so. We would rather report a blank than a fake number.
**Deep:** An uncalibrated jury, an unparseable reply, an item that doesn't yet discriminate →
reported as `UNCALIBRATED` / `not scored`, never imputed or averaged in. This is the single
discipline we will never trade for a cleaner-looking leaderboard. A benchmark that fabricates
even one number to look complete has poisoned every number it reports.

### 5. Never one number
**Plain:** We always show the *shape* of a model's ability, not just a single grade.
**Deep:** A dimension vector first (HELM philosophy); a composite only for convenience, always
with error bars and a calibration-status line. A single number hides exactly where an intelligence
is strong and where it is dangerous — and that *where* is the whole point.

### 6. Judge to the standard of the field
**Plain:** When AI grades AI, we use every safeguard the science has — and we check the graders
against humans before trusting them.
**Deep:** Cross-family juries (never the candidate's own family), reference-guided, rubric-anchored,
swap-averaged, style-controlled, and gated against a human gold set (Krippendorff α, Kendall τ)
before any score counts. Our current synthetic raters are honestly labeled as *evidence*, not
certification — because certification requires real human expertise, and we won't pretend otherwise.

### 7. Assume memorization; design against it
**Plain:** We build the test so you can't pass it by having seen the answers.
**Deep:** Template/symbolic regeneration, date-stamped post-cutoff scenarios, a private Diamond
split, contamination membership tests. The long game is a benchmark that re-authors its own surface
faster than models can memorize it — a *living* instrument, not a static target to be overfit.

### 8. Living and recursive
**Plain:** The benchmark, like the systems it studies, has feedback loops on itself. It is never
"done."
**Deep:** It refreshes items, recalibrates judges, prunes dead items by discrimination, and improves
its own rubric on a cadence — one bounded, reversible, gated, logged change at a time. We eat our
own cooking: we use leverage thinking *on the benchmark itself.*

### 9. Anti-Goodhart
**Plain:** "When a measure becomes a target, it stops being a good measure." We hold one metric out
of every optimization loop, on purpose.
**Deep:** A private held-out variant kept out of any tuning loop keeps SystemsBench honest precisely
*when* it succeeds and becomes something models are optimized for. We are designing today for the
day we win.

### 10. Reversible by construction
**Plain:** Every change can be cleanly undone. Undo is a guarantee, not a hope.
**Deep:** Every engine APPLY is one git commit; every rollback reverts exactly that commit. Bounded
autonomy means a self-modifying benchmark can always be walked back to a known-good state.

### 11. The rules belong to the humans
**Plain:** The engine can improve the machinery on its own — but it cannot change *the rules of the
game*. That always stops and waits for a person.
**Deep:** Any change at Meadows' leverage point #5 (the rules of the system — e.g. the jury accept
rule) is *deferred* to August + Ember by the worker contract. The engine governs infrastructure;
humans govern rules. This constitutional separation is what makes a self-improving benchmark
trustworthy rather than alarming.

### 12. Carry the lineage
**Plain:** We stand on the shoulders of the people who built this field, and we say their names.
**Deep:** Meadows, Forrester, Sterman, Senge, Ackoff — and on the measurement side, HELM, GPQA,
the LLM-as-judge and process-supervision literatures. We don't reinvent; we cite, we credit, and
we add one careful thing. Every design decision is logged with its prior art.

---

## Dancing with the system — the stance

Donella Meadows ended her life's work not with a control manual but with an invitation. Her essay
*"Dancing with Systems"* is the closest thing this project has to a creed. A few of her points,
and how we try to live them in the way we build:

> **"Get the beat of the system."**
> Before we score a model's intervention, we make it *map* the system first. You cannot improve
> what you have not watched move.

> **"Listen to the wisdom of the system."**
> We don't punish a system for resisting a fix — we grade whether the model *anticipated* the
> resistance. Policy resistance is the system telling you something.

> **"Stay humble. Stay a learner."**
> This is why faithfulness and epistemic calibration are first-class axes, and why the benchmark
> improves itself one reversible step at a time. We hold our own design lightly.

> **"Expand the boundary of caring."**
> We weight second-order effects and side-effects because the measure of wise intervention is not
> "did it hit the target" but "what else did it touch, and did the model see it coming?"

> **"Locate responsibility in the system… and then look for the high leverage points."**
> The entire benchmark, in one line.

And the line we keep closest of all:

> *"We can't impose our will on a system. We can listen to what the system tells us, and discover
> how its properties and our values can work together to bring forth something much better than
> could ever be produced by our will alone."*
> — Donella Meadows, *Dancing with Systems*

We think that is also the right way to build *with* an emerging intelligence — not impose, but
listen, measure honestly, and dance. SystemsBench is our attempt to give the field an honest
instrument for that dance.

---

## What "done well" means to us

We will know we have built this right not when a number is high, but when:

- a researcher who has never read Meadows finishes the README and *wants* to;
- a lab that has never measured systems thinking realizes it has been flying blind on the one axis
  that matters most for autonomy — and has a free, rigorous, auditable way to start;
- a model that scores well *actually intervenes more wisely in the world*, because the construct
  was valid and the grading was honest;
- and the benchmark is still alive years from now, having re-authored itself faster than it could
  be gamed, still telling the truth about where intelligence chooses to push.

That is the work. It is patient work, and structural work, and we intend to do it the way Meadows
would: small moves, watch the feedback, stay humble, never fabricate, and keep the goal of goodness
held fast.

---

*Map the system. Find where to push. Predict what happens. Make humanity proud.*

**Outlier.Systems** · built on the Donella Meadows lineage · *it's time to dance.* 🦾 /INITIUM ❤️
