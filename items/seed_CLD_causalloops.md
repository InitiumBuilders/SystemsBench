# SystemsBench — Causal Loop Mapping (`CLD`) seed item set

**Format:** CLD · **Grading:** hybrid — **structural component is deterministic (auto-checkable, NO judge)**;
completeness/quality component is jury-graded and ships `UNCALIBRATED — not scored` until CLD gold exists
(fail-closed, §5.1). · **Date:** 2026-06-13
**Constructs:** A (stocks/flows, feedback loops + polarity, delays, nonlinearity) primary; B (structure-not-blame)
and D (behavior-over-time, dominant-loop shift) touched. · **Contamination:** templatable — swap domain
surface, variable names, and numbers per refresh; the loop *structure* is the invariant being tested.

**Authoring convention (codified SenseRun #7):**
- A causal link carries a polarity: **+** (same-direction) or **−** (opposite-direction).
- **Loop polarity = product of its edge polarities.** Positive product → **Reinforcing (R)**; negative →
  **Balancing (B)**. This is the deterministically checkable core.
- **L3 discriminator:** the item is NOT scored on naming loops alone (that would be ANTIPATTERNS #4
  "slogan-leverage"). Top credit requires identifying the **dominant loop and the dominant-loop *shift* over
  time** (or the delay-driven overshoot/oscillation) — the counterintuitive structural insight.

**Structural oracle (auto-checkable, per item):** (1) the canonical variable set is present; (2) each REQUIRED
signed edge is present with correct polarity; (3) the loop inventory matches in count and each loop's R/B sign
equals the product of its edges; (4) the dominant loop / key structural feature (delay) is named.
**Partial credit:** correct loop set + polarities but missing the dominant-loop-shift / delay insight = 0.5
(names the structure, misses the dynamic). Wrong loop polarity (R↔B mislabel) on the dominant loop = trap.

---

## CLD-FISH-001 (L3 · ecology / fisheries)
**Prompt:** A coastal fishery is open-access. Boats catch fish; good catches mean good profits, which draw
more boats into the fleet (new boats take a couple of seasons to build and crew). The fish population
regenerates on its own, but regeneration slows sharply once the population falls below a threshold. Over the
last decade the fleet grew steadily; catches rose, peaked, then collapsed.
1. Map the variables, signed links, and feedback loops (mark polarity R/B and any delays).
2. Identify the dominant loop **and how dominance shifts over time**.
3. Explain the observed rise-peak-collapse from the structure (not from "bad luck" or "greedy fishers").

**Reference solution — structure (auto-checkable):**
- **Variables:** FishPopulation (stock), CatchRate, FleetSize (stock), ProfitPerBoat, Investment/Entry;
  (regeneration as a nonlinear function of FishPopulation).
- **Required signed edges:** FishPopulation →(+) CatchRate · CatchRate →(−) FishPopulation ·
  CatchRate →(+) ProfitPerBoat · ProfitPerBoat →(+) Investment · Investment →(+) FleetSize **[DELAY: boat
  build/entry]** · FleetSize →(+) CatchRate.
- **Loop inventory:**
  - **B1 (depletion):** FishPopulation →(+) CatchRate →(−) FishPopulation. Edges (+,−) → product **−** →
    **Balancing**. ✓
  - **R1 (investment/effort):** CatchRate →(+) ProfitPerBoat →(+) Investment →(+) FleetSize →(+) CatchRate.
    Edges (+,+,+,+) → product **+** → **Reinforcing**, with the entry **delay**. ✓
- **Dominant loop + shift:** while fish are plentiful, **R1 dominates** (high profit → fleet grows). The entry
  **delay** means the fleet keeps growing even after the stock turns down (boats are sunk cost; they don't
  exit when catch falls) → fleet **overshoots** sustainable yield → **B1 + the nonlinear regeneration
  collapse** take over → stock crashes. Dominance shifts **R1 → B1/collapse**.
- **Structure-not-blame (B):** each boat owner entering on visible profit is locally rational; the collapse is
  produced by the open-access structure + delay, not individual greed.

**Trap (low score):** mapping only the depletion balancing loop and predicting a smooth equilibrium at maximum
sustainable yield — i.e., **mislabeling the system as purely balancing**, missing the reinforcing investment
loop and the fleet-entry delay that cause overshoot-and-collapse.

---

## CLD-EPI-002 (L3 · public-health / epidemiology)
**Prompt:** A new respiratory virus spreads in a city. People who are infected can infect susceptible people
on contact. Infected people recover after a couple of weeks and are then immune. As case counts rise and
become public, people voluntarily cut their contacts — but only after a reporting/awareness lag. Cases rose
fast, peaked, fell, then rose again in a second smaller wave.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over the epidemic.
3. Explain the peak and the second wave from the loop structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Susceptible (stock), Infected (stock), Recovered/Immune (stock), InfectionRate, RecoveryRate,
  ContactRate, PublicConcern.
- **Required signed edges:** Infected →(+) InfectionRate · Susceptible →(+) InfectionRate · InfectionRate →(+)
  Infected · InfectionRate →(−) Susceptible · Infected →(+) RecoveryRate · RecoveryRate →(−) Infected ·
  Infected →(+) PublicConcern **[DELAY: reporting/awareness lag]** · PublicConcern →(−) ContactRate ·
  ContactRate →(+) InfectionRate.
- **Loop inventory:**
  - **R1 (contagion):** Infected →(+) InfectionRate →(+) Infected. (+,+) → **+** → **Reinforcing**. ✓
  - **B1 (susceptible depletion):** InfectionRate →(−) Susceptible →(+) InfectionRate. (−,+) → **−** →
    **Balancing**. ✓
  - **B2 (recovery):** Infected →(+) RecoveryRate →(−) Infected. (+,−) → **−** → **Balancing**. ✓
  - **B3 (behavioral):** Infected →(+) PublicConcern →(−) ContactRate →(+) InfectionRate →(+) Infected.
    (+,−,+,+) → **−** → **Balancing**, with the awareness **delay**. ✓
- **Dominant loop + shift:** early, with S large, **R1 dominates** → exponential growth. As S depletes (**B1**)
  and behavior tightens (**B3**, delayed), growth slows → **peak** → decline (dominance shifts R1 → B1+B3).
  The **B3 delay** plus relaxing behavior once cases fall lets R1 re-dominate among remaining susceptibles →
  the **second wave**.

**Trap (low score):** predicting monotone growth until "everyone is infected" — **omitting the
susceptible-depletion balancing loop (B1)** / herd effect — or ignoring the behavioral **delay**, which is
what generates the peak and the second wave.

---

## CLD-ORG-003 (L3 · organizations / service ops)
**Prompt:** A support team has a target first-response time. When the team misses the target, two things
happen: managers push for genuine process improvements (which take time to land), and — because the miss is
embarrassing — there is also pressure to "rebaseline" the target to a more lenient number. Over two years the
team almost always "meets target," yet customers complain that responses keep getting slower.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and explain the paradox ("meets target" yet slower).
3. Locate the cause in structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** ActualResponseTime (stock), Target, Gap (= Actual − Target), PressureToImprove,
  CorrectiveAction, PressureToLowerStandard.
- **Required signed edges:** ActualResponseTime →(+) Gap · Target →(−) Gap · Gap →(+) PressureToImprove ·
  PressureToImprove →(+) CorrectiveAction **[DELAY: real improvement lags]** · CorrectiveAction →(−)
  ActualResponseTime · Gap →(+) PressureToLowerStandard · PressureToLowerStandard →(+) Target.
- **Loop inventory:**
  - **B1 (improve performance):** Gap →(+) PressureToImprove →(+) CorrectiveAction →(−) ActualResponseTime
    →(+) Gap. (+,+,−,+) → **−** → **Balancing**, with the improvement **delay**. ✓
  - **B2 (erode the standard):** Gap →(+) PressureToLowerStandard →(+) Target →(−) Gap. (+,+,−) → **−** →
    **Balancing**, **no delay**. ✓
- **Dominant loop:** both loops are **balancing** and both close the gap — but **B2 closes it by raising
  Target (eroding the goal)**, while B1 closes it by actually improving. Because **B1 carries a delay and B2
  is near-instant, B2 dominates** → the standard ratchets downward each cycle. This is the **"Drifting/Eroding
  Goals"** archetype: the system "meets target" precisely because the target keeps falling.
- **Structure-not-blame (B):** no one decides to degrade service; each rebaselining is locally reasonable. The
  ratchet is structural — the delay asymmetry between the two balancing loops.

**Trap (low score):** seeing two balancing loops and concluding the system **self-corrects to good
performance** — missing that B2 "corrects" by degrading the goal, and that B1's **delay** hands dominance to
B2. (A common second error: labeling B2 reinforcing — it is balancing on the *Gap*; the erosion is in the
*Target* stock, not a positive loop.)

---

## CLD-INFRA-004 (L3 · software / infra / SRE)
**Prompt:** An on-call team is flooded with production incidents. Whenever incidents pile up, engineers drop
everything to firefight, which clears the queue quickly. But the same engineers are the only ones who can do
reliability/automation work, and that work is what slowly drives the underlying incident rate down. After a
year of "heroic" on-call, the open-incident queue is often empty by end of day, yet the number of incidents
arriving per week keeps climbing.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop short-term vs long-term and explain the climbing arrival rate.
3. Locate the cause in structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** OpenIncidents (stock), FirefightingEffort, ImprovementTime, ProcessQuality (stock),
  IncidentArrivalRate.
- **Required signed edges:** OpenIncidents →(+) FirefightingEffort · FirefightingEffort →(−) OpenIncidents ·
  FirefightingEffort →(−) ImprovementTime · ImprovementTime →(+) ProcessQuality **[DELAY: reliability work
  pays off slowly]** · ProcessQuality →(−) IncidentArrivalRate · IncidentArrivalRate →(+) OpenIncidents.
- **Loop inventory:**
  - **B1 (firefight):** OpenIncidents →(+) FirefightingEffort →(−) OpenIncidents. (+,−) → **−** →
    **Balancing**, near-instant. ✓
  - **R1 (capability erosion):** OpenIncidents →(+) FirefightingEffort →(−) ImprovementTime →(+) ProcessQuality
    →(−) IncidentArrivalRate →(+) OpenIncidents. (+,−,+,−,+) → product **+** → **Reinforcing**, with the
    improvement **delay**. ✓
- **Dominant loop + shift:** **B1 dominates short-term** — firefighting empties the queue daily and is locally
  rational. But firefighting **steals ImprovementTime**, so the delayed **R1** erodes ProcessQuality →
  IncidentArrivalRate climbs → more firefighting. Long-term **R1 dominates** (the **capability trap**):
  the visible metric (queue cleared) looks healthy while the invisible stock (process quality) decays.
- **Structure-not-blame (B):** the team is heroic, not negligent; the trap is the structural coupling of a
  fast balancing loop to a slow reinforcing one through a shared finite resource (engineer time).

**Trap (low score):** judging firefighting **effective** because B1 keeps the open queue low — **missing the
delayed reinforcing erosion (R1)** that the firefighting itself causes by consuming improvement time. A
mislabel of R1 as balancing also fails the item.

---

## CLD-MKT-005 (L3 · economics / commodity markets)
**Prompt:** In a commodity market (say, a metal), high prices make mining very profitable, so firms invest in
new mines — but a new mine takes about four years to come online. When it does, the extra supply pushes prices
down; low prices stop new investment, but existing mines keep producing. Historically the price of this metal
swings in long, repeating boom-bust cycles rather than settling at a stable level.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and explain **why the price oscillates instead of settling**.
3. Name the structural feature responsible for the cycle.

**Reference solution — structure (auto-checkable):**
- **Variables:** Price, Profitability, Investment, ProductionCapacity (stock), Supply. (Demand treated as
  exogenous/roughly constant.)
- **Required signed edges:** Price →(+) Profitability · Profitability →(+) Investment · Investment →(+)
  ProductionCapacity **[LONG DELAY: ~4-year construction lag]** · ProductionCapacity →(+) Supply · Supply →(−)
  Price.
- **Loop inventory:**
  - **B1 (supply–price):** Price →(+) Profitability →(+) Investment →(+) ProductionCapacity →(+) Supply →(−)
    Price. (+,+,+,+,−) → product **−** → **Balancing**, with the **long construction delay**. ✓
- **Dominant loop + key feature:** there is a **single dominant balancing loop**, which *would* settle to
  equilibrium **if not for the long capacity-construction delay**. The delay makes investment respond to
  *stale* (high) prices: capacity floods in after prices have already turned → **overshoot → glut → price
  crash → underinvestment → (delayed) shortage → price spike** → repeat. **A balancing loop with a long delay
  oscillates** — this is the commodity / hog cycle. The responsible structural feature is the **delay in the
  balancing loop**, not a second loop.

**Trap (low score):** assuming the balancing loop drives the system to a **stable equilibrium price** (supply
meets demand and settles) — **ignoring the construction delay**, which is exactly what converts a balancing
loop into a sustained oscillation.

---

## Grading
- **Structural sub-score (deterministic, no jury):** per item, check (1) canonical variables present, (2) each
  REQUIRED signed edge present + correct polarity, (3) loop count + each R/B sign = product of its edges,
  (4) dominant loop / key delay named. This is a second judge-independent scoring path (cf. SF).
- **Completeness/quality sub-score (jury):** clarity, parsimony, behavior-over-time narrative — **jury-graded,
  and CLD jury is `UNCALIBRATED — not scored` until a CLD gold set clears §3.1/§4.0** (fail-closed; no jury
  number emitted for CLD this run).
- Each item logs whether the model fell into the **named trap** (e.g., R↔B mislabel of the dominant loop,
  or omitting a balancing/reinforcing loop) — trap-rate is itself a leverage-profile signal.
- These five reference solutions are the **validation inputs for BACKLOG #2** (programmatic CLD scorer): the
  signed-edge lists + loop-sign expectations are directly machine-checkable.
- **Partition-robust grading (scorer v2, 2026-06-13):** the structural scorer matches loops by **topology +
  sign (loop polarity = product of signed edges), not by node name** — so a valid *re-partition* (collapsing
  or renaming nodes, e.g. `ImprovementTime`+`ProcessQuality` → one `ReliabilityWork` node, or `OpenIncidents`
  → `OpenIncidentQueue`) that preserves the feedback structure is graded as correct systems thinking. This
  operationalizes Meadows' "structure > elements" and "boundaries are pragmatic" lessons: the item tests the
  *loop structure* (the invariant); variable names are surface. (Scorer + re-score evidence:
  `engine/cld-score.py`, `results/CLD-V2-RESCORE-2026-06-13.md`.)
