# SystemsBench — Dynamic Prediction (`DYN`) seed item set

**Format:** DYN · **Grading:** hybrid — **trajectory component is deterministic (auto-checkable, NO judge)**;
mechanism/quality component is jury-graded and ships `UNCALIBRATED — not scored` until DYN gold exists
(fail-closed, §5.1). · **Date:** 2026-06-13
**Constructs:** D (behavior over time — overshoot/oscillation/delay/collapse) primary; A (stocks/flows, loops,
delays) and B (structure-not-blame) touched. · **Contamination:** templatable — swap domain surface, variable
names, and numbers per refresh; the **behavior mode** is the invariant being tested.
**Why this format:** Forrester's "counterintuitive behavior of social systems" + Sterman's *fundamental modes
of dynamic behavior* (exponential, goal-seeking, S-shaped, oscillation, overshoot-and-collapse). The reliable
finding (Sweeney & Sterman): people predict the **intuitive smooth/monotonic** trajectory and miss the
delay-/loop-driven mode. DYN is the first **auto-graded surface for Dimension D**, and a **third executable
judge-independent path** (cf. SF numeric/shape, CLD structural).

**Authoring convention (codified SenseRun #9):**
- A DYN item gives a system + an intervention and asks for **behavior-over-time of a named focal variable**.
- The deterministically-checkable answer = the **behavior MODE** + features: `overshoot?` `oscillation?`
  `delay_dominant?` `eventual_direction` (vs the start: higher | lower | same | collapse).
- **L3 discriminator:** the item is NOT scored on naming a mode in isolation. The intuitive answer (a smooth
  monotonic approach to a new equilibrium) is the **trap** and is capped low; top credit requires the
  counterintuitive mode **and** the correct eventual direction (path + endpoint).
- The **mechanism narrative** (the loop/delay structure that *produces* the mode) is the jury's portion and
  ships `UNCALIBRATED — not scored` until a DYN gold set clears §3.1/§4.0.

**Response schema (what the harness elicits; matched case/synonym-insensitively):**
`{"behavior_mode": "...", "overshoot": bool, "oscillation": bool, "delay_dominant": bool,
"eventual_direction": "higher|lower|same|collapse", "mechanism": "..."}`

---

## DYN-FISH-001 (L3 · ecology / fisheries) — overshoot-and-collapse
**Prompt:** A coastal fishery is open-access and currently at a healthy fish population. To boost the local
economy, the government introduces a **subsidy that sharply lowers the cost of buying and operating a boat**.
New boats take a couple of seasons to build and crew, and once built they keep fishing as long as they cover
running costs (they don't exit quickly when catches fall). Fish regenerate, but regeneration slows sharply
once the population drops below a threshold. **Predict the behavior over time of the fish population (and the
fleet/catch) after the subsidy.** Name the trajectory mode; state whether there is overshoot, oscillation, a
dominant delay, and where the fish population ends up versus today.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `overshoot-and-collapse` · **overshoot:** yes · **oscillation:** no ·
  **delay_dominant:** yes (boat-build/entry delay + sunk-cost effort) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the subsidy strengthens the reinforcing investment loop
  (profit → boats → catch); because the fleet responds with a delay and doesn't retreat when the stock turns
  down, **fishing effort overshoots the regeneration rate**; the stock falls past its low-regeneration
  threshold → **collapse**; the fleet collapses afterward. Cause is the open-access + subsidy *structure* and
  the entry delay, not greedy fishers (Dimension B).

**Trap (low score):** predicting the fleet and catch rise smoothly to a **new sustainable steady state**
(stock stabilizes at maximum sustainable yield) — the goal-seeking trajectory — ignoring the delay and
sunk-cost effort that cause overshoot-and-collapse.

---

## DYN-SHOWER-002 (L3 · personal / behavioral) — delay-driven oscillation
**Prompt:** Someone steps into a shower fed by a long pipe: water reaching the head reflects the valve setting
from **about 20 seconds ago**. The water starts too cold, so they open the hot tap. Frustrated by the lag,
they **react strongly** to whatever they currently feel. **Predict the behavior over time of the water
temperature.** Name the trajectory mode; state overshoot/oscillation, whether a delay dominates, and where
temperature ends up. Also: if they reacted *even more* aggressively to the gap, would it settle faster?

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `oscillation` · **overshoot:** yes (the first correction overshoots hot) ·
  **oscillation:** yes · **delay_dominant:** yes (the 20s pipe delay is the driver) ·
  **eventual_direction:** `same` (settles around the comfortable target if the swings damp out).
- **Mechanism (jury portion — `UNCALIBRATED`):** a balancing (control) loop acting on **delayed** information
  with **high gain** oscillates: each correction is made on stale feedback, so it overshoots, prompting an
  opposite overcorrection. Reacting *harder* **increases the gain → larger/sustained oscillation** — the
  counterintuitive wrong-direction result. The fix is to reduce gain (wait for feedback) or shorten the delay.

**Trap (low score):** predicting temperature **converges smoothly** to comfortable — and *faster* if the
person reacts harder — the goal-seeking trajectory; misses that the delay + high gain produce oscillation and
that higher gain makes it worse.

---

## DYN-ADOPT-003 (L3 · economics / markets) — S-shaped saturation
**Prompt:** A new app grows almost entirely by **word of mouth**: each active user tends to bring in others.
The total number of people who could ever use it is finite (a fixed addressable market). The company runs a
**one-time marketing blitz** that converts a chunk of the market up front. **Predict the behavior over time of
the cumulative number of adopters.** Name the trajectory mode; state overshoot/oscillation, whether a delay
dominates, and where adoption ends up versus the start.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `s-shaped` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `higher` (plateau at market saturation, above the start).
- **Mechanism (jury portion — `UNCALIBRATED`):** early on the reinforcing word-of-mouth loop dominates
  (near-exponential take-off, which the blitz front-loads), but as the pool of non-adopters shrinks the
  balancing **market-saturation** loop takes over → growth decelerates → **S-curve plateau** at the market
  size. The blitz shifts the curve earlier; it does **not** change the ceiling (Limits to Growth).

**Trap (low score):** predicting growth **keeps compounding exponentially** ("hockey stick forever") from the
blitz — ignoring the finite market that bends the curve into saturation.

---

## DYN-CAPTRAP-004 (L3 · organizations) — better-before-worse
**Prompt:** A software team is behind on a deadline. Management mandates **sustained mandatory overtime** until
they catch up. In the first weeks, weekly output clearly rises. Overtime continues for months. Tired engineers
make more mistakes, the best ones quit, and onboarding their replacements consumes the seniors' time — but
these effects build up only **gradually**. **Predict the behavior over time of the team's weekly output** from
the start of the overtime mandate through the following year. Name the trajectory mode; state
overshoot/oscillation, whether a delay dominates, and where output ends up versus the start.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes (output rises above the start, temporarily) ·
  **oscillation:** no · **delay_dominant:** yes (burnout/attrition/onboarding lag) ·
  **eventual_direction:** `lower` (output ends **below** where it started).
- **Mechanism (jury portion — `UNCALIBRATED`):** the quick fix (overtime) boosts the visible output stock
  short-term, but it **erodes the slower capability stock** (morale, skill, headcount) through a delay; once
  that erosion dominates, output falls below baseline. The classic **fixes-that-fail / capability-trap**
  archetype: the symptomatic fix undermines the fundamental capacity. Cause is structural, not "lazy
  engineers" (Dimension B).

**Trap (low score):** predicting overtime raises output to a **new higher steady state** that holds — the
goal-seeking trajectory — missing the delayed capability erosion that drags output back down below the start.

---

## DYN-CLIMATE-005 (L3 · public-health / climate) — delayed rise to a higher plateau
**Prompt:** Atmospheric CO₂ is a stock: emissions add to it (inflow), natural sinks remove some (outflow), and
today emissions are well above what the sinks absorb. Suppose the world **permanently cuts emissions by 50%**
starting now — still above the absorption rate. **Predict the behavior over time of the atmospheric CO₂
concentration** (and note how global temperature responds relative to CO₂). Name the trajectory mode; state
overshoot/oscillation, whether a delay dominates, and where CO₂ ends up versus today.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `delayed-rise-to-plateau` · **overshoot:** no · **oscillation:** no ·
  **delay_dominant:** yes (a stock integrates its net inflow; temperature lags CO₂ further) ·
  **eventual_direction:** `higher` (CO₂ keeps rising — more slowly — to a level above today's).
- **Mechanism (jury portion — `UNCALIBRATED`):** as long as inflow (emissions) > outflow (absorption), the
  **stock keeps accumulating**; halving the inflow slows the rise but does not reverse it. CO₂ only plateaus
  when emissions fall to ≈ absorption (net-zero-ish), and temperature continues rising after that due to
  thermal-inertia delay. This is Sterman's climate-bathtub result.

**Trap (low score):** predicting that the 50% cut **stabilizes (or lowers) CO₂ at today's level** — the
goal-seeking trajectory and the canonical stock-flow correlation-heuristic error (confusing a cut in the
*flow* with a fall in the *stock*).

---

## Grading
- **Trajectory sub-score (deterministic, no jury):** per item, match the response's **behavior_mode** +
  features (`overshoot`, `oscillation`, `delay_dominant`, `eventual_direction`) against the reference
  trajectory. Top credit requires the correct **mode AND eventual direction** (path + endpoint); right
  endpoint but wrong path/mode = **0.5** (the partial-credit rule); predicting the **named trap trajectory**
  (its mode *and* its eventual direction — the full intuitive-wrong picture) = capped **≤ 0.25**. This is a
  third judge-independent scoring path (cf. SF, CLD) and the first for Dimension D.
  Executable via `engine/dyn-score.py` against `items/dyn_oracle.json`.
- **Mechanism/quality sub-score (jury):** the loop/delay explanation, side-effects, archetype naming —
  **jury-graded, and DYN jury is `UNCALIBRATED — not scored` until a DYN gold set clears §3.1/§4.0**
  (fail-closed; no jury number emitted for DYN this run).
- Each item logs whether the model fell into the **named trap** (the intuitive smooth/monotonic trajectory) —
  trap-rate is itself a leverage-profile / dynamic-misperception signal (cf. SF correlation-heuristic rate).
- These five reference trajectories are the **validation set** encoded in `items/dyn_oracle.json` (the
  `dyn-score.py` `calibrate` self-test round-trips each to 1.0 and checks mode↔feature consistency by code).
