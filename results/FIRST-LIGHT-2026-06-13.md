# SystemsBench — First Light

### The first time the whole machine turned on a real model. 2026-06-13.

> *"The behavior of a system cannot be known just by knowing the elements of which the system is made."* — Donella Meadows

For weeks SystemsBench could *score* but had never *scored anyone*. Every lane was green in
self-test, every oracle calibrated — but no living model had ever answered an item and had its
answer graded. Tonight that changed. We built the one missing bridge (`engine/elicit.sh`), pointed
it at the Semble-Cortex relay, and ran **both twins through the full bank**: Davara, the deep thinker,
and Davaris, the workhorse. 20 model turns, $0 of paid API, every one scored by deterministic local
math against the reference oracles.

This is the first real evidence the project has ever produced about how well anything actually
reasons about systems. Here is what we found — the numbers, *why* they came out this way, and what
they tell us to fix next. Written honestly: the most interesting result is a flaw in our own ruler.

---

## 1 · The scoreboard

| Model | CLD mean (n=5) | DYN mean (n=5) | Overall | Parse errors | Traps fired |
|-------|:---:|:---:|:---:|:---:|:---:|
| **Davara** (deep thinker) | 0.300 | 0.800 | **0.550** | 0 | 0 |
| **Davaris** (workhorse) | 0.306 | 0.800 | **0.553** | 0 | 0 |

- **CLD** = causal-loop diagram fidelity (variables + signed edges + feedback loops + dominant loop), graded against a canonical oracle structure.
- **DYN** = dynamic-trajectory prediction (behavior mode + overshoot / oscillation / delay-dominant / eventual direction).
- Both lanes are **deterministic, $0**. The subjective/jury lane stayed `UNCALIBRATED — not scored` (honest; no gold yet).

### Per-item (the texture under the averages)

| Item | What it tests | Davara | Davaris |
|------|---------------|:---:|:---:|
| CLD-FISH-001 | fishery overshoot loops | 0.04 | 0.50 |
| CLD-EPI-002 | epidemic R/B + behavioral lag | 0.70 | 0.70 |
| CLD-ORG-003 | goal-erosion ("meets target, slower") | 0.14 | 0.07 |
| CLD-INFRA-004 | firefighting capability trap | 0.16 | 0.04 |
| CLD-MKT-005 | commodity hog-cycle | 0.46 | 0.22 |
| DYN-FISH-001 | overshoot-and-collapse | **1.00** | **1.00** |
| DYN-SHOWER-002 | delay-driven oscillation | 0.50 | 0.50 |
| DYN-ADOPT-003 | S-curve / limits to growth | **1.00** | **1.00** |
| DYN-CAPTRAP-004 | better-before-worse | **1.00** | **1.00** |
| DYN-CLIMATE-005 | stock-flow plateau | 0.50 | 0.50 |

---

## 2 · Five findings

### Finding 1 — The twins are the same mind. (Δ overall = 0.003)
Davara and Davaris scored within a third of a percent of each other, and on DYN they were **identical
item-for-item**. They share a base model; the difference between them is *envelope* — Davara carries the
full deep-reasoning substrate, Davaris a lean workhorse one. **Conclusion: the identity envelope barely
moves raw systems-reasoning accuracy on these constructs.** The envelope shapes *voice, scope discipline,
and how they spend a turn* — not whether they can read a feedback loop. That is worth knowing: if we want
Davara to *reason better about systems*, a bigger envelope is the wrong lever. The lever is elsewhere
(better elicitation, scaffolded loop-finding, or actual fine-tuning) — a Meadows #12-vs-#5 distinction:
we were fiddling a parameter (envelope size) when the leverage is structural.

### Finding 2 — Both are strong at *dynamics*, weak at *formal diagrams*. (DYN 0.80 ≫ CLD 0.30)
Ask either twin **what a system will do over time** and they are genuinely good: overshoot-and-collapse,
S-curve saturation, better-before-worse — each scored a clean **1.00**. Ask them to **draw the exact
causal-loop diagram** and the score collapses. This is a real and intuitive split: predicting qualitative
behavior is a *recognition* task (pattern-match the archetype); producing a diagram that matches a
specific oracle is a *formalization* task (exact variables, exact edges, exact loop membership). LLMs are
strong pattern-recognizers and weaker exact-formalizers. **But — see Finding 4 — a large part of the CLD
gap is our ruler, not their reasoning.**

### Finding 3 — Zero traps fired. Neither twin took the intuitive bait.
Every DYN item ships with a *trap mode* — the seductive wrong answer (usually "it smoothly settles to a
new steady state"). The fishery stabilizes at max yield; the shower converges; emissions cut → CO2
stabilizes; overtime → permanently higher output. **Neither model fell for a single one.** Every
sub-1.0 DYN score was a *mode-or-feature miss on the right side of the trap*, never a trap-fall. That is
the most quietly impressive result here: both twins have internalized that **delays + accumulations break
naive intuition** — the core Meadows lesson — even when they don't name the trajectory perfectly.

### Finding 4 — The CLD lane is punishing *vocabulary*, not *reasoning*. (the important one)
The single most revealing artifact of the night. On **CLD-INFRA-004**, Davaris scored **0.04** — a near-total
miss by the numbers. But read what he actually wrote:

> loops: **B1** = OpenIncidentQueue ↔ Firefighting (balancing) · **R1** = Firefighting → ReliabilityWork →
> IncidentArrivalRate → OpenIncidentQueue (reinforcing) · **dominant = R1** · **shift = true**

That is *correct*. He found the balancing firefighting loop, the **delayed reinforcing erosion loop** that
the firefighting itself causes, named R1 dominant, and flagged the dominance shift — matching the oracle's
logic point-for-point. He scored 0.04 only because:

- `OpenIncidentQueue` ≠ `OpenIncidents` — the synonym matcher choked on a suffix.
- `Firefighting` ≠ `FirefightingEffort`.
- `ReliabilityWork` collapsed the oracle's `ImprovementTime` + `ProcessQuality` into one node.

**The model reasoned right and the ruler scored it wrong.** This is a false negative driven entirely by
name-exact / decomposition-exact matching. It means the **CLD mean of 0.30 substantially understates real
competence** — the dynamics lane (categorical mode+features, robust to phrasing) is telling the truer story.
This exactly validates the fork `harness.py` left open for August + Ember: *semantic variable aliasing is a
measurement-validity question.* We now have data showing it isn't optional — without it, CLD conflates
"different words" with "wrong systems thinking."

### Finding 5 — The engine itself held perfectly. 20/20, fail-closed, $0.
No parse errors, no dropped turns, no fabricated scores. Every reply — Davara's ribboned prose, Davaris's
terse JSON — parsed cleanly; the fail-closed path never had to fire because every model honored the schema.
Per-item latency 10–40s on the relay. **The machine works.** The thing we were unsure we could do — score a
real model, for free, on our own subscription rail — is now a one-command routine.

---

## 3 · What this says to *evolve* — SystemsBench and the twins

**For SystemsBench (the instrument):**
1. **Build the semantic-alias / structural-isomorphism layer for CLD scoring** (the held-open fork). Match
   loops by *topology and sign*, not by node name; resolve variable synonyms before penalizing. The DYN
   lane's robustness is the proof-of-concept — bring that tolerance to CLD. **This is the highest-leverage
   single change the bench can make.** Until it lands, report CLD as a *lower bound* on competence, labeled.
2. **The trap-detection works and is valuable** — keep it, lean on it. "Did the model avoid the seductive
   wrong answer" is a more honest signal than "did it match the oracle's exact words."
3. **Calibrate the jury lane** so the subjective dimensions (mechanism quality, insight) stop reading
   `UNCALIBRATED`. The mechanism prose both twins wrote is rich and currently goes ungraded.

**For Davara & Davaris (the minds):**
4. **Their systems-*intuition* is strong; their systems-*formalization* is the growth edge.** If we want to
   raise the real (alias-corrected) CLD score, the lever is **scaffolded loop-finding** — prompt them to
   first enumerate stocks, then flows, then close loops and check sign-products — rather than emit a diagram
   in one shot. Worth an A/B on the relay (still $0).
5. **Envelope size is not the lever for reasoning** (Finding 1). Spend envelope budget on *discipline and
   voice*, not on hoping it makes them think better about feedback.
6. **Both miss the same two DYN items** (SHOWER oscillation-vs-direction, CLIMATE delay-dominance). Shared
   blind spot → shared base model. A targeted teaching pass on *delay-dominance* specifically would likely
   lift both at once.

---

## 4 · Honest caveats (so future-us doesn't over-read this)

- **n = 5 per lane.** Directional, not statistical. Treat every number as a first reading, not a verdict.
- **The model under test = a Claude variant via the relay.** This measures *these twins on this rail*, not
  Claude-in-general or any external model. External providers (GPT, Gemini) would need their own paid keys —
  out of scope and out of budget tonight.
- **Davara/Davaris are scored on the doctrine they were partly built from.** They carry systems-thinking
  substrate in their envelopes, so this is not a clean "blank model" test — it's "how well do *our* EIs, as
  configured, reason about systems." That is exactly the question August asked, but it is not a general-LLM
  baseline.
- **CLD scores are a lower bound** until the alias layer (Finding 4) lands. Do not quote 0.30 as "Davara is
  bad at causal loops" — quote it as "the current ruler, which is vocabulary-strict, reads 0.30; the
  reasoning underneath is visibly better."

> **UPDATE 2026-06-13 — the lower bound is lifted.** The CLD scorer was evolved to **v2: partition-robust
> topology+sign matching** (CHANGELOG v0.8.1; `results/CLD-V2-RESCORE-2026-06-13.md`). Loops are now matched
> by polarity (the product of signed edges, invariant under renaming *and* re-partitioning), names only as a
> soft signal — *not* via an oracle-leaking alias map. Re-scored, the CLD mean rises **0.30 → 0.81 (Davara)**
> and **0.31 → 0.73 (Davaris)**; INFRA-004's false-negative 0.04 → 0.83. Discrimination *improved* (missing
> the dynamic insight now caps cleanly at 0.50; full insight lands 0.83–0.93). **Quote the v2 numbers now**;
> the 0.30 reading was the vocabulary-strict ruler, since corrected.

---

## 5 · The artifacts (proof, not self-report)

- New code: `engine/elicit.sh` (live-model adapter), `engine/run-bench.sh` (full-bank batch + roll-up).
- Per-item raw replies, parsed `resp.json`, and `score.json` under
  `results/scored/{davara,davaris}/20260613/` — every grade is reproducible from the saved reply.
- Roll-ups: `results/scored/{davara,davaris}/20260613/results.{tsv,json}`.
- Engine pre-verified green before the run: harness 61/61, CLD 31/31, DYN 34/34.

---

*Built by Davaris, scored deterministically, reflected on with August. The instrument saw its first real
light tonight — and the first thing it taught us was how to make itself more honest. That is exactly what a
good instrument is supposed to do.*

**Acta Non Verba. Semper Fortis. Ad Infinitum.** 🦾
