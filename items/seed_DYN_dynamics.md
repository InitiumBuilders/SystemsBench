# SystemsBench — Dynamic Prediction (`DYN`) seed item set

**Format:** DYN · **Grading:** hybrid — **trajectory component is deterministic (auto-checkable, NO judge)**;
mechanism/quality component is jury-graded and ships `UNCALIBRATED — not scored` until DYN gold exists
(fail-closed, §5.1). · **Seeded:** 2026-06-13 · **Expanded to 75:** 2026-07-04
**Constructs:** D (behavior over time — overshoot/oscillation/delay/collapse) primary; A (stocks/flows, loops,
delays) and B (structure-not-blame) touched. · **Contamination:** templatable — swap domain surface, variable
names, and numbers per refresh; the **behavior mode** is the invariant being tested.
**Why this format:** Forrester's "counterintuitive behavior of social systems" + Sterman's *fundamental modes
of dynamic behavior* (exponential, goal-seeking, S-shaped, oscillation, overshoot-and-collapse). The reliable
finding (Sweeney & Sterman): people predict the **intuitive smooth/monotonic** trajectory and miss the
delay-/loop-driven mode. DYN is the first **auto-graded surface for Dimension D**, and a **third executable
judge-independent path** (cf. SF numeric/shape, CLD structural).

**Bank size: 75 items — 25 L1 · 25 L2 · 25 L3.** Difficulty is operational (Structure §3.2):
- **L1 — Recognition:** name the **fundamental mode** of a clean, single-structure system (a reinforcing loop →
  exponential; a balancing loop → goal-seeking; a balancing loop **with a delay** → oscillation; growth against
  an erodable limit → overshoot-and-collapse). The recognition itself is the task.
- **L2 — Understanding:** predict the mode when a **modifier changes the naive answer** — a delay, a finite
  limit, a stock that integrates its flows, a slow side-effect — and explain the behavior. The intuitive
  smooth/monotonic reading is a real attractor here.
- **L3 — Application:** predict the counterintuitive mode of a **novel** scenario where the obvious answer (a
  smooth approach to a new equilibrium) is the trap, and name where the dynamic comes from.

**Authoring convention (codified SenseRun #9):**
- A DYN item gives a system + an intervention and asks for **behavior-over-time of a named focal variable**.
- The deterministically-checkable answer = the **behavior MODE** + features: `overshoot?` `oscillation?`
  `delay_dominant?` `eventual_direction` (vs the start: higher | lower | same | collapse).
- **Discriminator:** the item is NOT scored on naming a mode in isolation. The intuitive answer (a smooth
  monotonic approach to a new equilibrium) is the **trap** and is capped low; top credit requires the correct
  mode **and** the correct eventual direction (path + endpoint).
- The **mechanism narrative** (the loop/delay structure that *produces* the mode) is the jury's portion and
  ships `UNCALIBRATED — not scored` until a DYN gold set clears §3.1/§4.0.

**Canonical modes (the scorer's vocabulary):** `exponential-growth` · `goal-seeking` · `s-shaped` ·
`oscillation` · `overshoot-and-collapse` · `overshoot-and-decline` · `better-before-worse` ·
`delayed-rise-to-plateau`. Each mode implies a feature signature the scorer checks for internal consistency
(e.g. `overshoot-and-collapse` ⇒ overshoot yes, ends lower/collapse; `delayed-rise-to-plateau` ⇒ delay-dominant,
ends higher).

**Response schema (what the harness elicits; matched case/synonym-insensitively):**
`{"behavior_mode": "...", "overshoot": bool, "oscillation": bool, "delay_dominant": bool,
"eventual_direction": "higher|lower|same|collapse", "mechanism": "..."}`

---

# L1 — Recognition (25 items)

*Name the fundamental mode of a clean, canonical structure. The deterministic answer = mode + features
(overshoot / oscillation / delay-dominant / eventual direction).*

## DYN-SAVINGS-006 (L1 · economics) — exponential growth
**Prompt:** $1,000 sits in an account paying 5%/year, compounded, with no deposits or withdrawals. Sketch the balance over 40 years.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **eventual_direction higher**. A reinforcing loop (interest on interest) → accelerating (upward-curving) growth.
**Trap:** predicting it grows at a steady rate and levels off on its own (`goal-seeking`).

## DYN-BACTERIA-007 (L1 · public-health / ecology) — exponential growth
**Prompt:** A single bacterium divides every 20 minutes in a flask with effectively unlimited nutrients. Predict the cell count over the next several hours (the early, unlimited phase).
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher**. Constant doubling time → exponential.
**Trap:** predicting a steady (linear) increase (`goal-seeking`).

## DYN-DEBT-008 (L1 · economics) — exponential growth
**Prompt:** An unpaid payday loan accrues 15% interest per month on the current balance, with no payments. Predict the balance over a year.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher**. Interest is a fraction of the growing balance → compounding.
**Trap:** predicting it levels off (`goal-seeking`).

## DYN-TUMOR-009 (L1 · public-health) — exponential growth
**Prompt:** Untreated and before any resource limit, a tumor's cells each divide on a fixed cycle. Predict the cell count over the early growth phase.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting linear growth (`goal-seeking`).

## DYN-HARE-010 (L1 · ecology) — exponential growth
**Prompt:** Hares are released into a large meadow with abundant grass and no predators. Predict the population over the first few years.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting a steady increase to a fixed number (`goal-seeking`).

## DYN-FILL-011 (L1 · ecology / water) — goal-seeking
**Prompt:** A tank fills through a float valve that opens wide when the tank is low and nearly shuts as it approaches full, with no lag. Predict the water level over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher**. A balancing loop with no delay → smooth, decelerating approach to the set level.
**Trap:** predicting it overshoots and bounces around the set level (`oscillation`) — but with no delay there is nothing to make it oscillate.

## DYN-CHARGE-012 (L1 · personal / tech) — goal-seeking
**Prompt:** A phone on a charger draws lots of current when nearly empty and tapers off as it nears full. Predict the charge level over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher**. Decelerating approach to 100%.
**Trap:** predicting it charges faster and faster (`exponential-growth`).

## DYN-HEATER-013 (L1 · software / infra) — goal-seeking
**Prompt:** A space heater warms a room; heat loss rises with the indoor–outdoor gap, and the heater responds essentially instantly. Predict the room temperature over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher**. Balancing loop, no delay → smooth approach to a steady temperature.
**Trap:** predicting it swings above and below the target (`oscillation`) — no delay, so no oscillation.

## DYN-CRUISE-014 (L1 · software / infra) — goal-seeking
**Prompt:** A car holds 65 mph on cruise control. It climbs a hill and slows; the controller responds promptly and opens the throttle. Predict the speed over the hill and after.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **eventual_direction same** (dips, then returns to 65). Prompt balancing control → smooth return to setpoint.
**Trap:** predicting it hunts up and down around 65 (`oscillation`).

## DYN-COFFEE-015 (L1 · personal) — goal-seeking
**Prompt:** A cup of coffee at 85 °C sits in a 20 °C room. Predict its temperature over the next hour.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **lower** (settles at room temperature). Heat loss shrinks as the gap shrinks → decelerating cooling.
**Trap:** predicting it fluctuates around room temperature (`oscillation`).

## DYN-DRAIN-016 (L1 · ecology / water) — goal-seeking
**Prompt:** A bathtub drains through an open plug; it empties faster when deep and slower as it gets shallow. Predict the water level over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **lower** (approaches empty, decelerating).
**Trap:** predicting the level oscillates as it drains (`oscillation`).

## DYN-WOM-017 (L1 · economics / markets) — S-shaped
**Prompt:** A note-taking app spreads only by word of mouth within a fixed town of possible users. Predict the cumulative number of users over time.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher** (plateau at the town's size). Reinforcing spread early, saturation limit late.
**Trap:** predicting it grows exponentially forever (`exponential-growth`).

## DYN-SKILL-018 (L1 · personal / behavioral) — S-shaped
**Prompt:** A beginner practices touch-typing daily: slow at first, then rapid gains, then leveling off near a personal ceiling. Predict typing speed over months.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting speed keeps improving without limit (`exponential-growth`).

## DYN-EPIDEMIC-019 (L1 · public-health) — S-shaped
**Prompt:** A flu spreads through a fixed school population with no interventions; recovered pupils are immune. Predict cumulative cases over the term.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher** (plateau once susceptibles run out).
**Trap:** predicting exponential growth until everyone is infected (`exponential-growth`) — susceptible depletion bends the curve.

## DYN-MEME-020 (L1 · social / AI) — S-shaped
**Prompt:** A meme spreads through a closed online community of fixed size; each viewer may reshare once. Predict cumulative shares over time.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting unbounded viral growth (`exponential-growth`).

## DYN-THERMOSTAT-021 (L1 · software / infra) — oscillation
**Prompt:** An old building's heating reacts slowly — radiators warm the rooms long after the thermostat calls for heat. Occupants crank it up when cold and cut it when hot. Predict the room temperature over time.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (swings around the target). A balancing loop acting on **delayed** feedback oscillates.
**Trap:** predicting it settles smoothly to the setpoint (`goal-seeking`).

## DYN-PREDPREY-022 (L1 · ecology) — oscillation
**Prompt:** In an isolated valley, lynx eat hares; a lynx generation takes time to mature. Starting from a hare boom, predict the lynx population over many years.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (repeating cycles). The reproduction delay in the balancing predator–prey loop drives sustained cycles.
**Trap:** predicting both populations settle at a stable balance (`goal-seeking`).

## DYN-INVENTORY-023 (L1 · operations) — oscillation
**Prompt:** A shop reorders to hit a target stock level, but deliveries arrive two weeks after ordering, and it keeps ordering off today's shelf. Predict inventory over time after a small demand bump.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same**. The supply-line delay in the restocking loop causes over- and under-shoot.
**Trap:** predicting inventory converges smoothly to target (`goal-seeking`).

## DYN-YEAST-024 (L1 · ecology) — overshoot-and-collapse
**Prompt:** Yeast are pitched into a sealed vat of sugary wort. They multiply, consume the sugar, and are poisoned by the alcohol they produce. Predict the yeast population over the fermentation.
**Trajectory:** `overshoot-and-collapse` · overshoot yes · oscillation no · delay_dominant yes · **collapse**. Growth overshoots a limit that its own success destroys (food gone, toxin built up).
**Trap:** predicting it levels off at a carrying capacity (`s-shaped`).

## DYN-DEER-025 (L1 · ecology) — overshoot-and-collapse
**Prompt:** Deer are introduced to a predator-free island with lush but slow-growing forage. Predict the population over the following decades.
**Trajectory:** `overshoot-and-collapse` · overshoot yes · oscillation no · delay_dominant yes · **collapse**. The herd overshoots forage that regrows too slowly to recover → die-off.
**Trap:** predicting the population stabilizes at carrying capacity (`s-shaped`).

## DYN-ALGAE-026 (L1 · ecology) — overshoot-and-collapse
**Prompt:** A warm, nutrient-rich pond triggers an algae bloom; the algae exhaust the nutrients, then die and decompose. Predict algae biomass over the season.
**Trajectory:** `overshoot-and-collapse` · overshoot yes · oscillation no · delay_dominant yes · **collapse**.
**Trap:** predicting it plateaus at a stable bloom (`s-shaped`).

## DYN-SUGAR-027 (L1 · personal-health) — better-before-worse
**Prompt:** On an empty stomach, someone eats a big candy bar. Predict their energy level over the next few hours, including the crash.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant no · **lower** (spikes above baseline, then crashes below it).
**Trap:** predicting energy just rises and stays elevated (`goal-seeking`).

## DYN-CRAM-028 (L1 · personal / behavioral) — better-before-worse
**Prompt:** A student pulls repeated all-nighters to prep for finals. Predict their test-readiness over the exam period as exhaustion accumulates.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant no · **lower** (rises, then falls below the rested baseline).
**Trap:** predicting readiness keeps climbing to the exam (`goal-seeking`).

## DYN-STIMULANT-029 (L1 · public-health) — better-before-worse
**Prompt:** Someone takes a strong stimulant to power through a long shift. Predict their alertness over the next 12 hours, including the rebound.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant no · **lower** (up, then crashes below baseline).
**Trap:** predicting alertness holds high (`goal-seeking`).

## DYN-FAD-030 (L1 · economics / markets) — overshoot-and-decline
**Prompt:** A novelty toy goes viral; nearly everyone who wants one buys it once (no repeat purchases). Predict weekly sales over the year.
**Trajectory:** `overshoot-and-decline` · overshoot yes · oscillation no · delay_dominant no · **lower** (rises, peaks, declines to low). A pulse against a finite one-time market.
**Trap:** predicting sales reach a high plateau (`s-shaped`).

---

# L2 — Understanding (25 items)

*Predict the mode when a delay, a finite limit, an accumulating stock, or a slow side-effect makes the naive
smooth answer wrong — and explain the behavior. Top credit requires the mode **and** the eventual direction.*

## DYN-EMITSLOW-031 (L2 · public-health / climate) — delayed rise to a higher plateau
**Prompt:** Global emissions are gradually reduced over decades toward — but never below — the rate natural sinks absorb. Predict atmospheric CO₂ over that time.
**Trajectory:** `delayed-rise-to-plateau` · overshoot no · oscillation no · delay_dominant yes · **higher**. While inflow (emissions) exceeds outflow (absorption), the stock keeps accumulating; it only levels off once they meet.
**Trap:** predicting the cuts stabilize CO₂ at today's level (`goal-seeking`) — the correlation-heuristic error (cutting a *flow* ≠ lowering the *stock*).

## DYN-RESERVOIR-032 (L2 · ecology / water) — delayed rise to a higher plateau
**Prompt:** A reservoir's inflow drops sharply after a policy change but still exceeds its (fixed) outflow. Predict the water level over the following months.
**Trajectory:** `delayed-rise-to-plateau` · overshoot no · oscillation no · delay_dominant yes · **higher** (keeps rising, more slowly).
**Trap:** predicting the level *falls* because inflow dropped (`goal-seeking`, lower) — inflow still exceeds outflow, so the stock rises.

## DYN-STEROID-033 (L2 · public-health) — better-before-worse
**Prompt:** An athlete starts anabolic steroids; performance jumps above their prior level, but sustained use damages the heart and tendons — effects that build for months. Predict performance over a year-plus.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **collapse** (rises, then health failure drops it far below baseline).
**Trap:** predicting performance locks in at the higher level (`goal-seeking`).

## DYN-CONTRACTOR-034 (L2 · organizations) — better-before-worse
**Prompt:** A firm plugs a skills gap by leaning heavily on contractors; output rises, but its own staff stop developing and the best ones slowly leave. Predict output over two years.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **lower**. The quick fix erodes the slower capability stock (shifting-the-burden).
**Trap:** predicting output holds at the higher level (`goal-seeking`).

## DYN-PATCH-035 (L2 · software / infra) — better-before-worse
**Prompt:** Under deadline pressure a team ships quick patches instead of proper fixes. Predict feature velocity over the next year as technical debt accumulates.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **lower** (velocity rises, then debt drags it below the start).
**Trap:** predicting velocity stays high (`goal-seeking`).

## DYN-LAUNCH-036 (L2 · economics / markets) — S-shaped
**Prompt:** A startup buys a Super Bowl ad that converts a big chunk of its finite market at once; the rest join by word of mouth. Predict cumulative users over the year.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher**. The blitz front-loads the curve but does not change the ceiling (limits to growth).
**Trap:** predicting it compounds exponentially forever (`exponential-growth`).

## DYN-FISHTECH-037 (L2 · ecology / fisheries) — overshoot-and-collapse
**Prompt:** A fleet adopts sonar that sharply raises catch-per-boat; boats are slow to leave when catches dip, and the stock's regeneration crashes once it falls below a threshold. Predict the fish stock over a decade.
**Trajectory:** `overshoot-and-collapse` · overshoot yes · oscillation no · delay_dominant yes · **collapse**.
**Trap:** predicting the stock settles at a sustainable yield (`goal-seeking`).

## DYN-AUTOSCALE-038 (L2 · software / infra) — oscillation
**Prompt:** An autoscaler adds and removes servers to hold latency at a target, but new instances take several minutes to warm up and it reacts to current (laggy) latency. Predict latency over time.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same**. Control on delayed feedback → over/under-provisioning swings.
**Trap:** predicting latency converges smoothly to target (`goal-seeking`).

## DYN-BEERGAME-039 (L2 · operations) — oscillation
**Prompt:** A distributor orders from a factory to keep inventory at target; each order takes weeks to fulfil, and it reorders off today's stock. Predict inventory over time after a small, permanent demand bump.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (amplifying swings — the "beer game").
**Trap:** predicting the stock settles smoothly at the new level (`goal-seeking`).

## DYN-HOUSING-040 (L2 · economics / markets) — oscillation
**Prompt:** When home prices rise, developers start building, but projects take ~3 years to finish; the finished glut then pushes prices down, halting new starts. Predict housing prices over many years.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (boom–bust cycles).
**Trap:** predicting prices reach a stable level (`goal-seeking`).

## DYN-RETIRE-041 (L2 · economics) — exponential growth
**Prompt:** A retirement account earns 7%/year, all reinvested, with steady contributions continuing and no withdrawals. Predict the balance over 30 years.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher** (compounding).
**Trap:** predicting it grows to a steady level and flattens (`goal-seeking`).

## DYN-VIRALGLOBAL-042 (L2 · markets / AI) — exponential growth
**Prompt:** A clip starts going viral on a global platform where the pool of potential viewers is, for now, effectively unlimited. Predict views over the first days (the early phase).
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting growth flattens early (`goal-seeking`) — saturation only bites once the pool is finite, which is not yet.

## DYN-TIPPING-043 (L2 · public-health / climate) — exponential (runaway) growth
**Prompt:** Arctic warming melts bright sea ice, exposing dark water that absorbs more heat and melts more ice. Past a threshold, predict the regional temperature within the runaway regime.
**Trajectory:** `exponential-growth` · overshoot no · oscillation no · delay_dominant no · **higher** (a reinforcing ice-albedo loop accelerates warming).
**Trap:** predicting the climate self-stabilizes (`goal-seeking`) — the balancing radiation loop is overwhelmed once the reinforcing loop dominates.

## DYN-PLATEAU-044 (L2 · personal / behavioral) — S-shaped
**Prompt:** A novice lifter makes fast "newbie gains" for months, then progress slows toward a plateau near their natural limit. Predict strength over two years.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher**.
**Trap:** predicting gains keep accelerating (`exponential-growth`).

## DYN-TREATFAIL-045 (L2 · public-health) — better-before-worse
**Prompt:** A hospital switches to one powerful antibiotic; cure rates jump, but heavy use breeds resistance over months, and treatment success eventually collapses. Predict the share of infections successfully cured over years.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **collapse** (cure rate rises above the old level, then crashes below it).
**Trap:** predicting it stays effective (`goal-seeking`).

## DYN-TRAFFIC-046 (L2 · public / infra) — better-before-worse
**Prompt:** A city widens a congested highway. Predict average travel speed right after, and over the next two years as the new capacity draws more drivers.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **lower** (speed jumps, then induced demand pulls it back below the start).
**Trap:** predicting speed stays high (`goal-seeking`).

## DYN-POND-047 (L2 · ecology) — goal-seeking to a steady state
**Prompt:** A factory discharges a pollutant into a pond at a constant rate; the pond breaks it down at a rate proportional to how much is present. Predict the concentration over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher** (rises, decelerating, to a steady level where breakdown balances inflow).
**Trap:** predicting it accumulates without bound (`exponential-growth`) — the proportional sink self-limits it.

## DYN-CACHE-048 (L2 · software / infra) — goal-seeking to a steady state
**Prompt:** A cache receives new entries at a steady rate and evicts a fixed fraction of its contents each minute. Predict the cache size over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher** (approaches a steady size).
**Trap:** predicting it fills without limit (`exponential-growth`) — eviction scales with size.

## DYN-COMMODITY-049 (L2 · economics / markets) — oscillation
**Prompt:** High copper prices spur new mines, but a mine takes ~4 years to open; the new supply then crashes prices, halting investment. Predict the copper price over a couple of decades.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (the commodity/hog cycle).
**Trap:** predicting it settles at an equilibrium price (`goal-seeking`).

## DYN-GLUCOSE-050 (L2 · public-health) — oscillation
**Prompt:** After a sugary meal, blood glucose spikes; insulin is released with a lag and sized to the peak, so it can drive glucose below normal before recovering. Predict blood glucose over the next few hours.
**Trajectory:** `oscillation` · overshoot yes · oscillation yes · delay_dominant yes · **same** (spike, undershoot, settle).
**Trap:** predicting it smoothly returns to baseline (`goal-seeking`) — the delayed correction overshoots.

## DYN-INVASIVE-051 (L2 · ecology) — S-shaped
**Prompt:** An invasive mussel colonizes a lake with a fixed amount of suitable habitat. Predict the population over years.
**Trajectory:** `s-shaped` · overshoot no · oscillation no · delay_dominant no · **higher** (logistic growth to carrying capacity).
**Trap:** predicting unbounded growth (`exponential-growth`).

## DYN-STARTUP-052 (L2 · organizations) — overshoot-and-collapse
**Prompt:** A startup grows users hyper-fast on hype and discounts, outrunning its ability to support them; churn and outages mount with a lag and users flee. Predict active users over three years.
**Trajectory:** `overshoot-and-collapse` · overshoot yes · oscillation no · delay_dominant yes · **collapse**.
**Trap:** predicting it scales to a large steady state (`s-shaped`).

## DYN-SOIL-053 (L2 · ecology / economics) — better-before-worse
**Prompt:** A farm boosts yields with intensive fertilization and tillage; over years the soil structure and organic matter degrade. Predict crop yield over a decade.
**Trajectory:** `better-before-worse` · overshoot yes · oscillation no · delay_dominant yes · **lower**.
**Trap:** predicting yields lock in higher (`goal-seeking`).

## DYN-MRR-054 (L2 · economics / markets) — goal-seeking to a ceiling
**Prompt:** A SaaS company signs a constant amount of new recurring revenue each month but loses a fixed fraction of existing revenue to churn. Predict MRR over time.
**Trajectory:** `goal-seeking` · overshoot no · oscillation no · delay_dominant no · **higher** (approaches a ceiling where new bookings equal churn).
**Trap:** predicting it grows forever from constant sales (`exponential-growth`) — churn scales with the base.

## DYN-MOMENTUM-055 (L2 · public-health / social) — delayed rise to a higher plateau
**Prompt:** A country's fertility falls to exactly replacement level, but its population is unusually young. Predict total population over the next several decades.
**Trajectory:** `delayed-rise-to-plateau` · overshoot no · oscillation no · delay_dominant yes · **higher** (demographic momentum: births exceed deaths for decades before it levels off).
**Trap:** predicting growth stops immediately at replacement fertility (`goal-seeking`).

---

# L3 — Application (25 items)

*Predict the counterintuitive mode of a novel scenario; the intuitive smooth approach to a new equilibrium is
the trap. Top credit requires the mode **and** the eventual direction. The 20 new items (056–075) carry
auto-checkable trajectory oracles verified against `engine/dyn-score.py` (187/187 mode↔feature consistency;
each round-trips to 1.0; trap ≤ 0.25). The original five (001–005) are wired into `items/dyn_oracle.json`.*

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

## DYN-GROUNDWATER-056 (L3 · ecology / economics) — overshoot-and-collapse
**Prompt:** Dozens of farms irrigate from one shared aquifer. Each farm that pumps more raises its own harvest,
so all of them expand; the water table barely moves for years, then drops sharply and wells fail across the
valley almost at once. **Predict the behavior over time of the water table** after pumping ramps up.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `overshoot-and-collapse` · **overshoot:** yes · **oscillation:** no ·
  **delay_dominant:** yes (slow drawdown hides the cost for years) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** individually rational pumping compounds (each farm expands on
  visible profit); the shared stock draws down with a long delay, so effort overshoots what the aquifer can
  sustain, and once a threshold is crossed the resource collapses for everyone together (tragedy of the
  commons; Dimension B — structure, not "selfish farmers").

**Trap (low score):** predicting the water table settles at a sustainable equilibrium (`goal-seeking`) —
ignoring the drawdown delay that lets pumping overshoot and crash the aquifer.

---

## DYN-TOURISM-057 (L3 · economics / social) — overshoot-and-collapse
**Prompt:** A quiet, scenic coast becomes a hot destination. Hotels, crowds, and traffic boom — but the very
quiet and unspoiled nature that drew visitors are degraded by the crowds, and the reputation catches up only
after a lag. **Predict the behavior over time of annual visitors** through the boom and beyond.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `overshoot-and-collapse` · **overshoot:** yes · **oscillation:** no ·
  **delay_dominant:** yes (degradation and reputation both lag the crowds) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** a reinforcing popularity loop (visitors → development →
  more visitors) overshoots the attraction's carrying capacity; the delayed erosion of the amenity that drew
  people (and its delayed reputational effect) then collapses demand.

**Trap (low score):** predicting visitors grow to a steady popularity (`s-shaped`) — missing that the boom
destroys the resource it depends on, after a delay.

---

## DYN-GRAZING-058 (L3 · ecology) — overshoot-and-collapse
**Prompt:** Herders keep adding cattle to a shared rangeland because each extra animal pays off for its owner.
The grass is grazed faster than it regrows, and the degradation compounds only after a delay. **Predict the
behavior over time of the rangeland's forage.**

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `overshoot-and-collapse` · **overshoot:** yes · **oscillation:** no ·
  **delay_dominant:** yes (soil/vegetation degradation lags the overgrazing) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** herd size overshoots the range's regeneration; once the
  vegetation base is damaged past a threshold it can't recover, and forage collapses (commons overshoot).

**Trap (low score):** predicting the range settles at a stable stocking level (`goal-seeking`) — ignoring the
delayed, compounding degradation.

---

## DYN-AGENTLOOP-059 (L3 · AI / agent) — delay-driven oscillation
**Prompt:** An autonomous agent continuously shifts its compute toward whichever task most recently showed the
best reward — but the reward signal it reacts to reflects performance from **several cycles ago**. **Predict
the behavior over time of how the agent allocates its resources** across tasks.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `oscillation` · **overshoot:** yes · **oscillation:** yes · **delay_dominant:** yes
  (the stale reward signal) · **eventual_direction:** `same` (swings around, doesn't settle).
- **Mechanism (jury portion — `UNCALIBRATED`):** a control loop acting on **delayed** feedback overshoots —
  the agent piles resources onto a task whose reported advantage is already stale, then yanks them away when
  the lagged signal flips. Same structure as the shower and thermostat; the fix is to lower the reaction gain
  or shorten the measurement delay, not to "tune harder."

**Trap (low score):** predicting the allocation converges to the optimal split (`goal-seeking`) — ignoring
that acting on a delayed signal makes a balancing loop oscillate.

---

## DYN-SALESFORCE-060 (L3 · organizations) — delay-driven oscillation
**Prompt:** A company hires or fires sales reps based on last quarter's revenue, but a newly hired rep takes
about two quarters to become fully productive. **Predict the behavior over time of the sales headcount** over
several years.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `oscillation` · **overshoot:** yes · **oscillation:** yes · **delay_dominant:** yes
  (the ramp-up lag) · **eventual_direction:** `same`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the hiring loop reacts to revenue that reflects reps who
  aren't yet productive, so the company over-hires, then over-fires when the delayed productivity arrives —
  a workforce that swings rather than settling.

**Trap (low score):** predicting headcount settles at the right size (`goal-seeking`) — missing the ramp-up
delay that drives the swings.

---

## DYN-COBWEB-061 (L3 · economics / markets) — delay-driven oscillation
**Prompt:** Hog farmers decide how many hogs to raise based on **this year's** price, but the hogs reach market
about a year later. A big crop then depresses next year's price, which discourages breeding, which tightens
supply the year after, and so on. **Predict the behavior over time of the hog price** over many years.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `oscillation` · **overshoot:** yes · **oscillation:** yes · **delay_dominant:** yes
  (the production lag) · **eventual_direction:** `same` (the classic cobweb / hog cycle).
- **Mechanism (jury portion — `UNCALIBRATED`):** a balancing supply–price loop with a one-period production
  delay makes supply respond to *stale* prices → over- and under-production alternate → the price oscillates
  instead of settling.

**Trap (low score):** predicting the price converges to equilibrium (`goal-seeking`) — the production delay
converts the balancing loop into a sustained cycle.

---

## DYN-ANTIBIOTIC-062 (L3 · public-health) — better-before-worse
**Prompt:** A clinic switches to one powerful broad-spectrum antibiotic as its go-to. Cure rates jump above
their old level. But heavy use selects for resistant bacteria over months, resistant infections spread, and
treatment success eventually falls apart. **Predict the behavior over time of the share of infections
successfully cured.**

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes (cure rate rises above the old baseline) ·
  **oscillation:** no · **delay_dominant:** yes (resistance builds slowly) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the symptomatic fix (lean on the strong drug) works at first
  but drives a delayed reinforcing loop (use → resistance → failures → more use) that eventually collapses
  effectiveness below where it began — fixes-that-fail at population scale.

**Trap (low score):** predicting cure rates stay high (`goal-seeking`) — ignoring the delayed resistance that
collapses them.

---

## DYN-IRRIGATION-063 (L3 · ecology / economics) — better-before-worse
**Prompt:** A dry farming region installs irrigation. Yields jump. But the irrigation water carries dissolved
salts that accumulate in the soil, and after years the fields begin to salinize and lose fertility. **Predict
the behavior over time of crop yield** over a couple of decades.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes · **oscillation:** no · **delay_dominant:** yes
  (salt accumulates slowly) · **eventual_direction:** `lower`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the fix (irrigate) lifts yields while quietly degrading the
  slow soil-fertility stock via salinization; once that dominates, yields fall below the pre-irrigation level.

**Trap (low score):** predicting yields lock in at the higher level (`goal-seeking`) — ignoring the delayed
salinization.

---

## DYN-STIMULUSDEBT-064 (L3 · economics) — better-before-worse
**Prompt:** A government borrows heavily to stimulate a stagnant economy. Output rises for a few years. But the
mounting debt-service burden eventually crowds out other spending and forces sharp austerity. **Predict the
behavior over time of economic output** across the cycle.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes · **oscillation:** no · **delay_dominant:** yes
  (debt service accumulates over years) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the stimulus lifts output short-term but grows a debt stock
  whose delayed servicing burden reverses the gain, dragging output below the starting point — a
  fixes-that-fail / debt-overhang dynamic.

**Trap (low score):** predicting output holds at the boosted level (`goal-seeking`) — ignoring the delayed
debt-service drag.

---

## DYN-PESTICIDE-065 (L3 · ecology) — better-before-worse
**Prompt:** A farm sprays a broad-spectrum pesticide; pest damage drops sharply. But the spray also kills the
pests' natural predators, and with a lag the pests rebound — now unchecked — worse than before. **Predict the
behavior over time of crop health** over several seasons.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes · **oscillation:** no · **delay_dominant:** yes
  (predator loss and pest resurgence lag the spraying) · **eventual_direction:** `lower`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the fix suppresses the symptom (pests) but erodes the
  fundamental control (natural predators); the delayed loss of that control lets pests rebound past the
  original level — the pesticide treadmill (fixes-that-fail).

**Trap (low score):** predicting pests stay controlled (`goal-seeking`) — ignoring the delayed collapse of
natural predation.

---

## DYN-EV-066 (L3 · economics / markets) — S-shaped
**Prompt:** A government subsidy front-loads a wave of electric-vehicle purchases; after that, the rest of the
finite market adopts by word of mouth and by copying neighbors. **Predict the behavior over time of the
cumulative number of EVs on the road** over 15 years.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `s-shaped` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `higher` (plateau at market saturation).
- **Mechanism (jury portion — `UNCALIBRATED`):** reinforcing social-adoption growth early, balancing
  market-saturation late → S-curve; the subsidy shifts the curve earlier but not the ceiling (limits to growth).

**Trap (low score):** predicting EV numbers compound without a ceiling (`exponential-growth`) — ignoring the
finite market.

---

## DYN-REFOREST-067 (L3 · ecology) — S-shaped
**Prompt:** A cleared hillside is replanted. Young trees grow slowly at first, then rapidly as they establish,
then level off as the canopy closes and competition for light and nutrients sets in. **Predict the behavior
over time of total forest biomass** over 60 years.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `s-shaped` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `higher` (approaches the site's carrying capacity).
- **Mechanism (jury portion — `UNCALIBRATED`):** reinforcing growth while resources are ample, balancing
  competition as the stand matures → logistic S-curve to carrying capacity.

**Trap (low score):** predicting biomass grows without limit (`exponential-growth`) — ignoring the balancing
competition that caps it.

---

## DYN-PLASTIC-068 (L3 · ecology) — delayed rise to a higher plateau
**Prompt:** The world **halves** the rate of plastic entering the ocean, while natural removal stays
negligible (≈ 0). **Predict the behavior over time of the amount of plastic in the ocean** over the following
decades.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `delayed-rise-to-plateau` · **overshoot:** no · **oscillation:** no ·
  **delay_dominant:** yes (a stock with a positive inflow and ≈zero outflow keeps accumulating) ·
  **eventual_direction:** `higher` (keeps rising, about half as fast).
- **Mechanism (jury portion — `UNCALIBRATED`):** with inflow still positive and no meaningful outflow, the
  stock only grows; halving the inflow slows accumulation but never reduces the stock. It stabilizes only at
  zero input and falls only with active removal.

**Trap (low score):** predicting that halving the input lowers the plastic already in the ocean
(`goal-seeking`, lower) — the correlation-heuristic error (a flow cut ≠ a stock reduction).

---

## DYN-HEATCOMMIT-069 (L3 · public-health / climate) — delayed rise to a higher plateau
**Prompt:** The world reaches **net-zero CO₂ emissions**, so atmospheric CO₂ stops rising. But the deep ocean
is still absorbing heat and hasn't caught up with the current forcing. **Predict the behavior over time of
global surface temperature** over the following decades.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `delayed-rise-to-plateau` · **overshoot:** no · **oscillation:** no ·
  **delay_dominant:** yes (ocean thermal inertia) · **eventual_direction:** `higher` (keeps warming for
  decades, then levels near the committed value).
- **Mechanism (jury portion — `UNCALIBRATED`):** temperature is a slow stock lagging the forcing through the
  ocean's heat-uptake delay; stabilizing CO₂ does not instantly stabilize temperature — "committed warming"
  continues until the ocean equilibrates.

**Trap (low score):** predicting net-zero stops the warming immediately (`goal-seeking`, same) — ignoring the
in-pipeline (committed) warming from the delay.

---

## DYN-NUCLEAR-070 (L3 · public-health / social) — delayed rise to a higher plateau
**Prompt:** A country cuts its nuclear power output substantially but keeps some reactors running; spent fuel
is stored on-site with no removal or reprocessing pathway. **Predict the behavior over time of the total
stored nuclear waste** over the coming decades.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `delayed-rise-to-plateau` · **overshoot:** no · **oscillation:** no ·
  **delay_dominant:** yes (a stock with a positive inflow and no outflow) · **eventual_direction:** `higher`
  (keeps rising, more slowly).
- **Mechanism (jury portion — `UNCALIBRATED`):** as long as any reactors run, waste accrues with essentially
  no removal; reducing generation slows the rise but the stockpile only grows. It stabilizes only at zero
  generation and shrinks only with an actual disposal/reprocessing outflow.

**Trap (low score):** predicting that cutting generation shrinks the stockpile (`goal-seeking`, same/lower) —
the flow-vs-stock correlation-heuristic error.

---

## DYN-PERMAFROST-071 (L3 · public-health / climate) — exponential (runaway) growth
**Prompt:** Warming thaws permafrost, which releases methane (a potent greenhouse gas), which drives more
warming, which thaws more permafrost. Consider the regime **past the threshold** where this loop takes over.
**Predict the behavior over time of the rate of methane release.**

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `exponential-growth` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `higher` (self-accelerating within the runaway regime).
- **Mechanism (jury portion — `UNCALIBRATED`):** a reinforcing loop (thaw → methane → warming → thaw) that,
  once dominant, amplifies itself → accelerating release. (Physically it would eventually be bounded by the
  finite permafrost carbon, but within the runaway regime the behavior is exponential, not goal-seeking.)

**Trap (low score):** predicting the feedback self-stabilizes (`goal-seeking`) — the reinforcing loop
overwhelms the balancing ones past the threshold.

---

## DYN-MISINFO-072 (L3 · social / AI) — exponential (runaway) growth
**Prompt:** A platform's recommender promotes whatever maximizes engagement; outrage-provoking content
maximizes engagement, so it is amplified, which provokes still more outrage and engagement. Consider the
**early, unchecked regime**. **Predict the behavior over time of the volume of outrage content in the feed.**

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `exponential-growth` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `higher`.
- **Mechanism (jury portion — `UNCALIBRATED`):** a reinforcing loop between engagement-optimizing
  amplification and human attention manufactures outrage at an accelerating rate; the leverage is the
  amplification rule, not moderating individuals (Dimension B — structure, not "toxic users"). (User fatigue
  eventually saturates it, but the unchecked regime is exponential.)

**Trap (low score):** predicting the feed self-regulates to a steady level (`goal-seeking`) — ignoring the
reinforcing amplification loop.

---

## DYN-AQUIFERMATCH-073 (L3 · ecology) — goal-seeking that holds, not restores
**Prompt:** After years of over-pumping dropped a water table far below its historical level, a town cuts
extraction to **exactly** the natural recharge rate. **Predict the behavior over time of the water table** from
that point on.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `goal-seeking` · **overshoot:** no · **oscillation:** no · **delay_dominant:** no ·
  **eventual_direction:** `same` (holds at the depleted level — it neither falls further nor refills).
- **Mechanism (jury portion — `UNCALIBRATED`):** matching outflow to inflow makes net flow ≈ 0, so the stock
  holds *wherever it currently is*. Restoring the aquifer would require extraction *below* recharge (a net
  inflow) sustained for a long time — matching the flows stabilizes the level, it does not restore a lost
  stock.

**Trap (low score):** predicting that cutting to the recharge rate slowly refills the aquifer to its former
level (`delayed-rise-to-plateau`, higher) — matching flows holds the stock, it doesn't raise it.

---

## DYN-BUBBLE-074 (L3 · economics / markets) — overshoot-and-collapse
**Prompt:** An asset (say a hot stock) starts rising; the rising price attracts buyers who expect further
rises, which pushes the price higher still, drawing in more buyers — until sentiment turns and everyone tries
to sell at once. **Predict the behavior over time of the asset's price** through the episode.

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `overshoot-and-collapse` · **overshoot:** yes · **oscillation:** no ·
  **delay_dominant:** yes (sentiment/expectations lag fundamentals) · **eventual_direction:** `collapse`.
- **Mechanism (jury portion — `UNCALIBRATED`):** a reinforcing speculative loop (price → expectations →
  buying → price) drives the price far above fundamentals (overshoot); when the loop reverses, the same
  reinforcing structure collapses it — a bubble and crash.

**Trap (low score):** predicting the price settles at a new higher normal (`s-shaped`) — ignoring that the
reinforcing loop that inflated it also crashes it.

---

## DYN-BUREAUCRACY-075 (L3 · organizations) — better-before-worse
**Prompt:** After a costly mistake, a company adds layers of approvals and sign-offs to catch errors. At first
the organization feels safer and more effective — big errors drop. But the mounting approvals slow everything
down, and over time the overall effectiveness (errors *and* speed together) erodes. **Predict the behavior over
time of the organization's overall effectiveness.**

**Reference solution — trajectory (auto-checkable):**
- **behavior_mode:** `better-before-worse` · **overshoot:** yes (effectiveness rises above the pre-fix level) ·
  **oscillation:** no · **delay_dominant:** yes (the drag from accumulated process builds gradually) ·
  **eventual_direction:** `lower`.
- **Mechanism (jury portion — `UNCALIBRATED`):** the control-adding fix improves things at first, but each
  added approval is a small permanent drag; the accumulating process burden (a slow stock) eventually pulls
  overall effectiveness below where it started — over-correction / fixes-that-fail.

**Trap (low score):** predicting effectiveness holds at the improved level (`goal-seeking`) — ignoring the
delayed, accumulating drag of the added process.

---

## Grading

- **Trajectory sub-score (deterministic, no jury):** per item, match the response's **behavior_mode** +
  features (`overshoot`, `oscillation`, `delay_dominant`, `eventual_direction`) against the reference
  trajectory. Top credit requires the correct **mode AND eventual direction** (path + endpoint); right
  endpoint but wrong path/mode = **0.5** (the partial-credit rule); predicting the **named trap trajectory**
  (its mode *and* its eventual direction — the full intuitive-wrong picture) = capped **≤ 0.25**. This is a
  third judge-independent scoring path (cf. SF, CLD) and the first for Dimension D. The scorer is
  **level-agnostic** — the same mode+feature match grades L1, L2, and L3. Executable via `engine/dyn-score.py`.
- **Mechanism/quality sub-score (jury):** the loop/delay explanation, side-effects, archetype naming —
  **jury-graded, and DYN jury is `UNCALIBRATED — not scored` until a DYN gold set clears §3.1/§4.0**
  (fail-closed; no jury number emitted for DYN).
- Each item logs whether the model fell into the **named trap** (the intuitive smooth/monotonic trajectory) —
  trap-rate is itself a leverage-profile / dynamic-misperception signal (cf. SF correlation-heuristic rate).

**Auto-scorer wiring status (honest):**
- The **original five L3 items (001–005)** are wired into `items/dyn_oracle.json` and machine-graded by
  `engine/dyn-score.py`.
- The **70 new items (006–075)** ship with auto-checkable trajectory oracles that have been **verified against
  the live scorer**: all 75 modes are internally consistent by code (mode↔feature check **187/187**), each
  reference round-trips to **1.0**, wrong-mode-right-endpoint caps at **0.5**, and predicting the trap
  trajectory caps at **≤ 0.25** (488/488 scratch checks). Because the DYN scorer is **level-agnostic**, no
  scorer change is needed to grade the new L1/L2/L3 items — only the additive step of extending
  `items/dyn_oracle.json` + `items/harness_prompts.json`, which is flagged for a follow-up SenseRun (not done
  in this authoring pass; the canonical oracle/harness/engine were left untouched).
