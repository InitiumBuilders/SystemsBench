# SystemsBench — Causal Loop Mapping (`CLD`) seed item set

**Format:** CLD · **Grading:** hybrid — **structural component is deterministic (auto-checkable, NO judge)**;
completeness/quality component is jury-graded and ships `UNCALIBRATED — not scored` until CLD gold exists
(fail-closed, §5.1). · **Seeded:** 2026-06-13 · **Expanded to 75:** 2026-07-04
**Constructs:** A (stocks/flows, feedback loops + polarity, delays, nonlinearity) primary; B (structure-not-blame)
and D (behavior-over-time, dominant-loop shift) touched. · **Contamination:** templatable — swap domain
surface, variable names, and numbers per refresh; the loop *structure* is the invariant being tested.

**Bank size: 75 items — 25 L1 · 25 L2 · 25 L3.** Difficulty is operational (Structure §3.2):
- **L1 — Recognition:** name the construct. Read a single link's polarity (+/−), classify a small loop as
  **Reinforcing (R)** or **Balancing (B)**, count loops, or name the behavior one loop tends to produce. The
  signature L1 insight (and trap): **two negative links close into a *reinforcing* loop** — a vicious/virtuous
  cycle, not a balancing one.
- **L2 — Understanding:** explain the **behavior over time** a small (1–2 loop, sometimes delayed) structure
  produces — exponential growth vs. goal-seeking vs. S-curve vs. delay-driven oscillation/overshoot — and
  name the archetype (limits-to-growth, fixes-that-fail, shifting-the-burden, escalation).
- **L3 — Application:** map a *novel* scenario from scratch and locate the counterintuitive structural
  insight — the **dominant-loop shift over time**, or the **delay-driven overshoot/oscillation**.

**Authoring convention (codified SenseRun #7):**
- A causal link carries a polarity: **+** (same-direction) or **−** (opposite-direction).
- **Loop polarity = product of its edge polarities.** Positive product → **Reinforcing (R)**; negative →
  **Balancing (B)**. This is the deterministically checkable core (an *even* number of − links → R; *odd* → B).
- **L3 discriminator:** the item is NOT scored on naming loops alone (that would be ANTIPATTERNS #4
  "slogan-leverage"). Top credit requires identifying the **dominant loop and the dominant-loop *shift* over
  time** (or the delay-driven overshoot/oscillation) — the counterintuitive structural insight.

**Structural oracle (auto-checkable, per item):** (1) the canonical variable set is present; (2) each REQUIRED
signed edge is present with correct polarity; (3) the loop inventory matches in count and each loop's R/B sign
equals the product of its edges; (4) the dominant loop / key structural feature (delay) is named.
**Partial credit:** correct loop set + polarities but missing the dominant-loop-shift / delay insight = 0.5
(names the structure, misses the dynamic). Wrong loop polarity (R↔B mislabel) on the dominant loop = trap.

---

# L1 — Recognition (25 items)

*Read a link's sign, classify a small loop R/B (loop sign = product of edge signs), count loops, or name the
behavior a loop produces. Deterministic: the answer is the polarity/sign/type or the named behavior mode.*

## CLD-SAVINGS-006 (L1 · economics)
**Prompt:** Money in a savings account earns interest; more money earns more interest, which adds to the money. Is this a reinforcing (R) or balancing (B) loop?
**Reference:** Savings →(+) Interest · Interest →(+) Savings. Loop sign = (+)(+) = **+ → Reinforcing (R)** (compounding).
**Trap:** calling it balancing because it's "just one account" — a two-positive-link loop is reinforcing.

## CLD-COFFEE-007 (L1 · personal)
**Prompt:** A hot coffee loses heat faster the hotter it is above room temperature; losing heat lowers its temperature. Reinforcing or balancing? What behavior does it produce?
**Reference:** Temperature →(+) HeatLoss · HeatLoss →(−) Temperature. Loop sign = (+)(−) = **− → Balancing (B)**; behavior = **goal-seeking** (temperature settles to room temperature).
**Trap:** "reinforcing — losing heat leads to losing more heat"; the loop opposes the gap, so it's balancing.

## CLD-RUMOR-008 (L1 · social)
**Prompt:** People who have heard a rumor tell others, so the number who have heard it keeps producing more tellers. Reinforcing or balancing, and does it tend to grow or settle?
**Reference:** HeardIt →(+) Telling · Telling →(+) HeardIt. Loop sign = (+)(+) = **+ → Reinforcing (R)**; behavior = **spreads / grows** (exponential early on).
**Trap:** confusing "everyone eventually knows" (a later limit) with the loop's own tendency, which is growth.

## CLD-MORALE-009 (L1 · organizations)
**Prompt:** Lower morale raises absenteeism; higher absenteeism further lowers morale. Both links are "negative." Is the *loop* reinforcing or balancing?
**Reference:** Morale →(−) Absenteeism · Absenteeism →(−) Morale. Loop sign = (−)(−) = **+ → Reinforcing (R)** — a vicious cycle (a spiral down).
**Trap:** the classic error — "two negative links must make a balancing loop." **Two negatives multiply to a positive → reinforcing.**

## CLD-RABBIT-010 (L1 · ecology)
**Prompt:** The more rabbits there are, the more grass gets eaten, so the less grass remains. Is the link *from rabbits to grass* positive or negative?
**Reference:** Rabbits →(**−**) Grass (they move in opposite directions: more rabbits → less grass).
**Trap:** marking it "+" by fixating on "more grass *eaten*" — the target variable is grass remaining, which falls.

## CLD-EXERCISE-011 (L1 · personal-health)
**Prompt:** The more regularly someone exercises, the lower their resting heart rate. Is the link from exercise to resting heart rate positive or negative?
**Reference:** Exercise →(**−**) RestingHeartRate (opposite directions).
**Trap:** calling any "more X → good effect" link positive; polarity is about direction of change, not whether the effect is desirable.

## CLD-THERMO-012 (L1 · software/infra)
**Prompt:** An autoscaler adds servers when CPU load per server is high; more servers lower the load per server. Reinforcing or balancing?
**Reference:** LoadPerServer →(+) ServersAdded · ServersAdded →(−) LoadPerServer. Loop sign = (+)(−) = **− → Balancing (B)** (holds load near a target).
**Trap:** "reinforcing, because it keeps adding servers" — the loop's purpose is to close a gap, so it's balancing.

## CLD-DEBT-013 (L1 · economics)
**Prompt:** An unpaid credit-card balance accrues interest, which is added to the balance, which then accrues even more interest. Reinforcing or balancing?
**Reference:** Balance →(+) Interest · Interest →(+) Balance. Loop sign = (+)(+) = **+ → Reinforcing (R)** (compounding debt).
**Trap:** treating it as balancing because "it's a debt you're trying to reduce" — the *loop* structure is reinforcing.

## CLD-RECESSION-014 (L1 · economics)
**Prompt:** When confidence falls, people spend less; when spending falls, confidence falls further. Reinforcing or balancing — and note that both variables move *down* together.
**Reference:** Confidence →(+) Spending · Spending →(+) Confidence. Loop sign = (+)(+) = **+ → Reinforcing (R)**. Reinforcing means *amplifying in either direction* — here a downward spiral (it would spiral up just as readily).
**Trap:** assuming "reinforcing" must mean growth; a reinforcing loop amplifies whatever direction it's pushed, including collapse.

## CLD-VALVE-015 (L1 · ecology/water)
**Prompt:** A float valve fills a tank: the lower the water, the more the valve opens; more inflow raises the water. Reinforcing or balancing, and what behavior?
**Reference:** WaterLevel →(−) ValveOpening · ValveOpening →(+) WaterLevel. Loop sign = (−)(+) = **− → Balancing (B)**; behavior = **goal-seeking** to the set level.
**Trap:** "reinforcing, because water keeps rising" — it rises *toward a target and stops*, the mark of a balancing loop.

## CLD-COUNT-016 (L1 · software/infra)
**Prompt:** In this description there are two closed feedback loops: (a) high queue length → more workers → shorter queue; (b) high queue length → more errors → more rework → longer queue. **How many feedback loops are described, and is each reinforcing or balancing?**
**Reference:** **Two loops.** (a) Queue →(+) Workers →(−) Queue = **B**. (b) Queue →(+) Errors →(+) Rework →(+) Queue = **R**.
**Trap:** collapsing the two into one, or missing that (b) closes back onto the queue.

## CLD-SIGNS3-017 (L1 · organizations)
**Prompt:** A three-link loop has edge signs +, −, +. Is it reinforcing or balancing?
**Reference:** product = (+)(−)(+) = **− → Balancing (B)** (odd number of − links).
**Trap:** counting links instead of multiplying signs.

## CLD-SIGNS4-018 (L1 · markets)
**Prompt:** A four-link loop has all four edges positive (+, +, +, +). Reinforcing or balancing?
**Reference:** product = (+)(+)(+)(+) = **+ → Reinforcing (R)**.
**Trap:** assuming a longer loop must be balancing; all-positive is reinforcing regardless of length.

## CLD-SIGNS2NEG-019 (L1 · software/infra)
**Prompt:** A loop has two negative links and one positive link (−, −, +). Reinforcing or balancing?
**Reference:** product = (−)(−)(+) = **+ → Reinforcing (R)** (even number of − links).
**Trap:** "more negatives → balancing" — parity is what matters; two negatives cancel to positive.

## CLD-POPGROWTH-020 (L1 · ecology)
**Prompt:** In a population with unlimited food, more individuals produce more births, which add more individuals. Name the loop type and the behavior over time.
**Reference:** Population →(+) Births · Births →(+) Population = **Reinforcing (R)**; behavior = **exponential growth**.
**Trap:** predicting steady/linear growth — an unchecked reinforcing loop grows exponentially.

## CLD-CROWD-021 (L1 · social)
**Prompt:** A beach draws visitors, but the more crowded it gets, the less pleasant it is, so fewer new people come. Reinforcing or balancing?
**Reference:** Visitors →(+) Crowding · Crowding →(−) Visitors. Loop sign = (+)(−) = **− → Balancing (B)** (self-limiting).
**Trap:** "reinforcing, it's popular" — popularity is checked by crowding; the loop balances.

## CLD-MUSCLE-022 (L1 · personal-health)
**Prompt:** Training builds strength; being stronger lets you train harder, which builds more strength. Reinforcing or balancing?
**Reference:** Strength →(+) Training · Training →(+) Strength = **Reinforcing (R)** (a virtuous cycle).
**Trap:** calling it balancing because "there are limits" — the *loop itself* is reinforcing (limits come from a separate loop).

## CLD-CLOUD-023 (L1 · climate)
**Prompt:** More low cloud cover reflects more sunlight away, which lowers surface temperature. Is the link from cloud cover to temperature positive or negative?
**Reference:** CloudCover →(**−**) Temperature (opposite directions).
**Trap:** marking "+" because clouds "do something"; the effect lowers temperature → negative.

## CLD-VIRAL-024 (L1 · AI/social)
**Prompt:** A post's shares put it in front of more people, who share it again. Name the loop type and its early behavior.
**Reference:** Shares →(+) Reach · Reach →(+) Shares = **Reinforcing (R)**; behavior = **viral/exponential growth** early on.
**Trap:** confusing the eventual plateau (a saturation loop) with this loop's own growth tendency.

## CLD-PREDATOR-025 (L1 · ecology)
**Prompt:** The more wolves in a valley, the fewer deer survive. Is the link from wolves to deer positive or negative?
**Reference:** Wolves →(**−**) Deer (opposite directions).
**Trap:** marking "+" because "more wolves → more predation" — the target is the deer count, which falls.

## CLD-HABIT-026 (L1 · personal/behavioral)
**Prompt:** Each day you keep a streak, your motivation rises, which makes you more likely to keep the streak tomorrow. Reinforcing or balancing?
**Reference:** Streak →(+) Motivation · Motivation →(+) Streak = **Reinforcing (R)**.
**Trap:** calling it balancing; a self-feeding streak is a reinforcing loop.

## CLD-BUDGET-027 (L1 · organizations)
**Prompt:** A team spends toward a monthly budget: the more they've spent, the more spending is cut back for the rest of the month. Reinforcing or balancing?
**Reference:** SpentSoFar →(−) SpendingRate · SpendingRate →(+) SpentSoFar. Loop sign = (−)(+) = **− → Balancing (B)** (holds to the budget).
**Trap:** "reinforcing, spending keeps adding up" — the correction opposes overspending, so it's balancing.

## CLD-INFECT-028 (L1 · public-health)
**Prompt:** Early in an outbreak, each infected person infects several others, adding to the infected count. Name the loop type and early behavior (ignore recovery/immunity for now).
**Reference:** Infected →(+) NewInfections · NewInfections →(+) Infected = **Reinforcing (R)**; behavior = **exponential growth** early.
**Trap:** assuming linear spread; unchecked contagion is reinforcing → exponential.

## CLD-BRAKE-029 (L1 · software/infra)
**Prompt:** Cruise control eases off the throttle as the car exceeds the set speed, bringing speed back down toward the setpoint. Reinforcing or balancing?
**Reference:** Speed →(−) Throttle · Throttle →(+) Speed. Loop sign = (−)(+) = **− → Balancing (B)** (goal-seeking to set speed).
**Trap:** "reinforcing, it controls the engine" — control toward a target is balancing.

## CLD-DROUGHT-030 (L1 · ecology)
**Prompt:** The more rainfall a region gets, the less severe its drought. Is the link from rainfall to drought severity positive or negative?
**Reference:** Rainfall →(**−**) DroughtSeverity (opposite directions).
**Trap:** confusing the sign with the desirability of the outcome; direction of change is what defines polarity.

---

# L2 — Understanding (25 items)

*Given a small (1–2 loop, sometimes delayed) structure, give the polarities and explain the **behavior over
time** it produces — and name the archetype where one applies. The gradeable content is the behavior mode +
its mechanism, not just the loop label.*

## CLD-COMPOUND-031 (L2 · economics)
**Prompt:** An investment returns a fixed percentage each year, and the returns are reinvested. Draw the loop and explain how the balance grows over time — and why it is not a straight line.
**Reference — structure + behavior:** Balance →(+) Return · Return →(+) Balance = **R**. Behavior = **exponential growth**: because each year's return is a *fraction of the (growing) balance*, the absolute gain rises every year → an upward-curving trajectory, not linear.
**Trap:** predicting linear growth ("same amount added each year") — misses that the inflow scales with the stock.

## CLD-DEATHSPIRAL-032 (L2 · organizations)
**Prompt:** A transit agency raises fares to cover a shortfall; higher fares drive away riders; fewer riders deepen the shortfall, prompting another fare hike. Map the loop and explain the trajectory.
**Reference — structure + behavior:** Shortfall →(+) Fare · Fare →(−) Riders · Riders →(−) Shortfall. Loop sign = (+)(−)(−) = **+ → R** (a "death spiral"). Behavior = **accelerating decline** — each corrective hike worsens the very shortfall it targets.
**Trap:** treating each fare hike as a fix that stabilizes finances — it's a reinforcing collapse (a fixes-that-fail/vicious cycle); the leverage is elsewhere (cost, service, subsidy).

## CLD-GOALSEEK-033 (L2 · personal)
**Prompt:** You're learning to hit a target jog distance: each week you close part of the gap between your current and target distance. Explain the behavior over time.
**Reference — structure + behavior:** Gap →(+) Effort · Effort →(−) Gap (via CurrentDistance) = **B**. Behavior = **goal-seeking**: fast progress when the gap is large, slowing as you approach the target — an asymptotic (diminishing-returns) approach, no overshoot (no delay).
**Trap:** predicting steady linear progress all the way to target; a balancing loop's rate falls as the gap shrinks.

## CLD-PENDULUM-034 (L2 · ecology)
**Prompt:** A wildlife manager adjusts a cull to steer a deer herd toward a target size, but each adjustment's effect on the herd shows up only a season later. Explain the behavior the delay produces.
**Reference — structure + behavior:** Gap →(+) Cull · Cull →(−) Herd →(+) Gap = **B**, **with a one-season delay** on the effect. Behavior = **oscillation around the target**: because corrections act on stale information, the manager over- and under-shoots, and the herd swings above and below target rather than settling.
**Trap:** expecting a balancing loop to settle smoothly — a **delay in a balancing loop produces oscillation**.

## CLD-LIMITS-035 (L2 · markets)
**Prompt:** A new app spreads by word of mouth (adopters recruit more adopters), but the pool of people who haven't yet adopted shrinks as adoption grows. Explain the shape of the adoption curve over time.
**Reference — structure + behavior:** R1 (Adopters →(+) AdoptionRate →(+) Adopters) and B1 (AdoptionRate →(−) PotentialAdopters →(+) AdoptionRate). Behavior = **S-shaped growth**: **R1 dominates early** (near-exponential take-off), then as the pool depletes **B1 dominates** and growth slows to a ceiling — the **limits-to-growth** archetype.
**Trap:** extrapolating the early exponential to infinity — ignoring the saturation balancing loop that bends the curve over.

## CLD-STEER-036 (L2 · software/infra)
**Prompt:** An operator manually adjusts a server pool to hold latency at a target, but provisioning a new instance takes several minutes to take effect, and the operator keeps reacting to the current (laggy) latency. Explain the behavior.
**Reference — structure + behavior:** Gap →(+) Provisioning · Provisioning →(−) Latency →(+) Gap = **B**, **with a provisioning delay**. Behavior = **overshoot and oscillation**: reacting to delayed feedback, the operator over-provisions, then over-cuts — latency swings around the target instead of converging.
**Trap:** assuming more aggressive correction settles it faster; with a delay, aggressiveness *increases* the oscillation.

## CLD-PAINKILLER-037 (L2 · public-health)
**Prompt:** A patient with chronic back pain takes stronger painkillers whenever pain spikes (fast relief), but heavy use gradually weakens the muscles that would fix the pain at its root, so underlying pain slowly worsens. Explain the trajectory and name the archetype.
**Reference — structure + behavior:** B1 (Pain →(+) Painkillers →(−) Pain, fast) and R1 (Painkillers →(−) MuscleStrength →(+) UnderlyingPain →(+) Pain, delayed). Behavior = **relief then relapse to a worse state** — the **fixes-that-fail** archetype: the symptomatic fix works short-term while the delayed reinforcing side-effect erodes the fundamentals.
**Trap:** judging the painkiller effective because pain drops at first — missing the delayed reinforcing worsening it causes.

## CLD-CAP-038 (L2 · economics)
**Prompt:** A fast-growing town's population grows by attracting more residents (a reinforcing loop). Then rising housing costs, driven by the growing population, start deterring newcomers. Explain what adding the second loop does to the growth.
**Reference — structure + behavior:** R1 (Population →(+) Attractiveness →(+) Population) plus B1 (Population →(+) HousingCost →(−) Attractiveness). Behavior = the reinforcing growth is **capped**: the town approaches a **new equilibrium** where the balancing cost loop offsets the reinforcing draw — growth stalls at a plateau rather than continuing.
**Trap:** expecting unbounded growth from the reinforcing loop — a balancing loop coupled in sets the ceiling.

## CLD-NETPOL4-039 (L2 · software/infra)
**Prompt:** A four-link loop has edge signs +, +, +, −. Determine the loop polarity and describe the behavior it tends to produce.
**Reference — structure + behavior:** product = (+)(+)(+)(−) = **− → B**. Behavior = **goal-seeking / self-correcting** — it counteracts disturbances and settles toward a target (unless a delay is present, which would make it oscillate).
**Trap:** miscounting the single negative or assuming "mostly positive → reinforcing"; one negative flips the whole loop to balancing.

## CLD-ARMS-040 (L2 · social)
**Prompt:** Two rival nations each build weapons in response to the other's arsenal: A arms because B is armed, and B arms because A is armed. Explain the behavior over time.
**Reference — structure + behavior:** ArmsA →(+) ThreatToB →(+) ArmsB →(+) ThreatToA →(+) ArmsA = **R** (all positive). Behavior = **escalating spiral** (an arms race) — the **escalation** archetype: each side's rational defensive move drives the other's, amplifying without bound until an external limit (cost, treaty) intervenes.
**Trap:** reading each side's arming as stabilizing deterrence (balancing) — the coupled structure is reinforcing.

## CLD-SATURATE-041 (L2 · markets)
**Prompt:** A subscription box grows fast as happy customers refer friends, but the addressable market is finite. Sales rise, peak, and level off. Explain this shape from the loops.
**Reference — structure + behavior:** R1 (Customers →(+) Referrals →(+) Customers) + B1 (Customers →(−) RemainingMarket →(+) Referrals). Behavior = **S-curve to a plateau**: reinforcing referral growth early, balancing market-saturation later → sales *rate* peaks mid-way and total subscribers level off (limits-to-growth).
**Trap:** projecting the early growth rate forward — the finite market is a balancing loop that flattens the curve.

## CLD-RUN-042 (L2 · economics)
**Prompt:** A rumor that a bank is shaky prompts some depositors to withdraw; visible withdrawals lower confidence, prompting more withdrawals. Explain why this unfolds so fast, and where the leverage is.
**Reference — structure + behavior:** Fear →(+) Withdrawals · Withdrawals →(−) Reserves · Reserves →(−) Fear. Loop sign = (+)(−)(−) = **+ → R**. Behavior = **rapid, self-accelerating collapse** — each withdrawal is individually rational but lowers reserves and raises everyone's fear. Leverage is **structural** (deposit insurance / lender of last resort), not blaming "panicky" depositors.
**Trap:** attributing the run to irrational individuals — the reinforcing structure makes the collapse rational and fast.

## CLD-HERD-043 (L2 · public-health)
**Prompt:** In an outbreak, infected people infect susceptibles (reinforcing), but every infection also removes a susceptible from the pool. Explain why cases rise, peak, and fall — even with no behavior change.
**Reference — structure + behavior:** R1 (Infected →(+) InfectionRate →(+) Infected) + B1 (InfectionRate →(−) Susceptible →(+) InfectionRate). Behavior = **rise, peak, decline**: **R1 dominates while susceptibles are plentiful** (exponential rise); as the susceptible pool depletes, **B1 dominates** and the epidemic peaks and recedes (herd effect) — dominance shifts R1 → B1.
**Trap:** predicting monotone growth "until everyone is infected" — susceptible depletion alone bends the curve down.

## CLD-VIRTUOUS-044 (L2 · organizations)
**Prompt:** A firm reinvests profits into product quality; better quality wins reputation; reputation drives sales; sales fund more quality investment. Explain the trajectory and note the fragility.
**Reference — structure + behavior:** Quality →(+) Reputation →(+) Sales →(+) Investment →(+) Quality = **R** (a virtuous cycle). Behavior = **accelerating (compounding) success** while it turns forward — but the same reinforcing loop runs **in reverse** (a cut to quality can spiral down just as fast), which is its fragility.
**Trap:** assuming a virtuous cycle is inherently stable — reinforcing loops amplify *both* directions.

## CLD-INVENTORY-045 (L2 · operations)
**Prompt:** A retailer reorders stock to hit a target inventory, but deliveries arrive weeks after ordering, and the retailer keeps ordering based on today's shelf level. Explain the behavior of inventory over time.
**Reference — structure + behavior:** Gap →(+) Orders · Orders →(+) Inventory →(−) Gap = **B**, **with a long shipping delay**. Behavior = **oscillation / overshoot** (the "beer game"): orders placed to fill an apparent shortage keep arriving after the shelf has refilled → overshoot → cutbacks → shortage → repeat.
**Trap:** expecting inventory to converge smoothly to target — the supply-line delay in a balancing loop drives swings.

## CLD-EQUIL-046 (L2 · economics)
**Prompt:** In a market where extra supply can be produced almost immediately, high prices raise supply, and higher supply lowers price. With *no* significant delay, does price oscillate or settle? Explain — and contrast with a market that has a long production lag.
**Reference — structure + behavior:** Price →(+) Supply · Supply →(−) Price = **B**, **no delay**. Behavior = **smooth convergence to equilibrium** (price settles where supply meets demand). **With a long production lag** (contrast), the same balancing loop **oscillates** (boom-bust) — the delay, not the loop sign, is what makes the difference.
**Trap:** assuming markets always cycle, or always settle — the presence/absence of a delay in the balancing loop decides it.

## CLD-CAFFEINE-047 (L2 · personal/behavioral)
**Prompt:** Someone fights afternoon tiredness with coffee (quick alertness), but regular caffeine disrupts their sleep, so their baseline tiredness slowly rises and they lean on coffee more. Explain the behavior and name the archetype.
**Reference — structure + behavior:** B1 (Tiredness →(+) Coffee →(−) Tiredness, fast) and R1 (Coffee →(−) SleepQuality →(+) BaselineTiredness →(+) Tiredness, delayed). Behavior = **growing dependence**: the symptomatic fix works each time while the delayed reinforcing loop erodes sleep, shifting reliance onto coffee — the **shifting-the-burden** archetype.
**Trap:** seeing coffee as a harmless fix — missing that it atrophies the fundamental solution (real rest) and deepens dependence.

## CLD-NETPOL5-048 (L2 · ecology)
**Prompt:** A five-link loop has edge signs +, +, −, +, −. Determine the loop polarity and describe the behavior it tends to produce.
**Reference — structure + behavior:** product = (+)(+)(−)(+)(−) = **+ → R** (an even number — two — of negative links). Behavior = **reinforcing amplification**: self-accelerating growth or collapse depending on the direction it's pushed.
**Trap:** "there are negatives, so it balances" — count parity: two negatives multiply to positive → reinforcing.

## CLD-NETWORK-049 (L2 · markets/AI)
**Prompt:** A messaging platform is more useful the more friends are on it, and its usefulness attracts more users. Explain the growth dynamic and why a competing platform can be hard to dislodge — but also how the loop could reverse.
**Reference — structure + behavior:** Users →(+) Value →(+) Users = **R** (network effects). Behavior = **reinforcing growth → lock-in** (a leader compounds its lead — "success to the successful" flavor); but the loop is symmetric, so an exodus can trigger a **reinforcing collapse** (value falls → users leave → value falls).
**Trap:** treating a dominant network as permanently stable — the reinforcing loop can tip into decline once users start leaving.

## CLD-GENTRIFY-050 (L2 · social)
**Prompt:** A neighborhood gets trendy; new amenities raise its appeal; higher appeal raises rents and draws more investment, which adds more amenities. Explain the trajectory and who the structure (not blame) displaces.
**Reference — structure + behavior:** Appeal →(+) Investment →(+) Amenities →(+) Appeal = **R**. Behavior = **accelerating rise** in rents/appeal (a reinforcing gentrification loop); the displacement of lower-income residents is produced by the reinforcing structure, not by any single actor's intent.
**Trap:** attributing displacement to individual landlords rather than the reinforcing loop; and expecting rents to self-limit (they don't, absent a balancing loop like rent control or supply).

## CLD-FEVER-051 (L2 · public-health)
**Prompt:** When an infection load rises, the immune response ramps up and clears pathogens, lowering the load back toward zero. Explain the behavior over time (assume the response is prompt).
**Reference — structure + behavior:** PathogenLoad →(+) ImmuneResponse · ImmuneResponse →(−) PathogenLoad = **B**. Behavior = **goal-seeking recovery**: load rises, the balancing response drives it back down and settles near zero — a self-correcting return to health (no oscillation without a delay).
**Trap:** calling the immune ramp-up "reinforcing" because it grows; it's a balancing loop that opposes the load.

## CLD-TRUST-052 (L2 · social)
**Prompt:** In a partnership, keeping commitments builds trust; more trust makes each side more willing to keep commitments. Explain the behavior — and why the same loop is dangerous.
**Reference — structure + behavior:** Trust →(+) Commitment-keeping · Commitment-keeping →(+) Trust = **R**. Behavior = **a virtuous cycle** that compounds cooperation upward — but being reinforcing, a single breach can flip it into a **downward spiral** (broken commitment → less trust → more broken commitments).
**Trap:** assuming trust, once built, is self-sustaining — the reinforcing loop runs both ways and can reverse.

## CLD-PROCRAST-053 (L2 · personal/behavioral)
**Prompt:** Putting off a task raises anxiety about it; higher anxiety makes the task feel more aversive, so it's put off further. Explain the behavior and the leverage.
**Reference — structure + behavior:** Delay →(+) Anxiety · Anxiety →(+) Aversion · Aversion →(+) Delay = **R** (all positive → a vicious cycle). Behavior = **self-accelerating avoidance**. Leverage: break the loop (shrink the task, timebox a start) rather than "trying to feel less anxious," since anxiety is downstream in the loop.
**Trap:** treating it as a willpower/motivation deficit rather than a reinforcing structure — and pushing on anxiety, the wrong point in the loop.

## CLD-CARRYING-054 (L2 · ecology)
**Prompt:** A population on an island grows through reproduction, but as it nears the food supply's limit, crowding and scarcity raise the death rate. Explain the shape of the population curve and name the archetype.
**Reference — structure + behavior:** R1 (Population →(+) Births →(+) Population) + B1 (Population →(+) Scarcity →(−) Population via deaths). Behavior = **logistic / S-shaped growth** leveling at **carrying capacity**: R1 dominates while resources are ample, B1 dominates as the limit nears — dominance shifts R1 → B1 (limits-to-growth). If the delay in the death-rate response is long, it can **overshoot and then correct**.
**Trap:** projecting exponential growth to infinity, or ignoring that a delayed limit can cause overshoot before settling.

## CLD-WORKAROUND-055 (L2 · software/infra)
**Prompt:** Under deadline pressure, a team ships quick workarounds instead of proper fixes (fast relief), but each workaround adds technical debt that, over time, causes more incidents and more deadline pressure. Explain the trajectory and name the archetype.
**Reference — structure + behavior:** B1 (Pressure →(+) Workarounds →(−) Pressure, fast) and R1 (Workarounds →(+) TechDebt →(+) Incidents →(+) Pressure, delayed). Behavior = **short-term relief, long-term worsening** — the **fixes-that-fail** archetype: the workaround loop relieves pressure now while the delayed reinforcing debt loop raises the baseline incident rate.
**Trap:** judging workarounds effective because they clear the immediate crunch — missing the delayed reinforcing debt they accumulate.

---

# L3 — Application (25 items)

*Map a novel scenario from scratch; the top-credit insight is the **dominant-loop shift over time** or the
**delay-driven overshoot/oscillation** — the counterintuitive structural finding, not loop-naming. Each new
L3 reference solution below (CLD-*-056…075) is machine-checkable in the CLD structural-oracle format (variables,
signed edges, loop inventory with polarity = product of edges) and has been verified deterministically
consistent against `engine/cld-score.py` (41/41 loop signs; each round-trips to 1.0; trap ≤0.25; partial 0.5).
The original five (001–005) are already wired into `items/cld_oracle.json`.*

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

## CLD-ADOPT-056 (L3 · economics / markets)
**Prompt:** A new productivity app spreads mostly by word of mouth: current users recommend it to others. Growth
was explosive for a year, then slowed to a crawl and flattened — long before "everyone" had it — and the
company was blindsided because early growth looked unstoppable.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the take-off and the plateau from the structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Adopters (stock), AdoptionRate, PotentialAdopters (stock).
- **Required signed edges:** Adopters →(+) AdoptionRate · AdoptionRate →(+) Adopters · AdoptionRate →(−)
  PotentialAdopters · PotentialAdopters →(+) AdoptionRate.
- **Loop inventory:**
  - **R1 (word-of-mouth):** Adopters →(+) AdoptionRate →(+) Adopters. (+,+) → **+** → **Reinforcing**. ✓
  - **B1 (market saturation):** AdoptionRate →(−) PotentialAdopters →(+) AdoptionRate. (−,+) → **−** →
    **Balancing**. ✓
- **Dominant loop + shift:** early, with a large untapped pool, **R1 dominates** → near-exponential take-off.
  As Adopters grow, the PotentialAdopters pool depletes, so **B1 dominates** → the adoption *rate* peaks and
  the installed base flattens well short of the whole market. Dominance shifts **R1 → B1** (limits-to-growth).

**Trap (low score):** extrapolating the early exponential to unbounded growth — **omitting the
saturation balancing loop (finite pool)** that bends the S-curve over.

---

## CLD-BURDEN-057 (L3 · organizations)
**Prompt:** A company facing a skills gap starts hiring contractors to close it fast. Contractors do clear the
immediate work, but relying on them means the firm invests less in training its own staff, so internal
capability slowly decays — which widens the very gap that justifies more contractors. Years later the firm is
deeply dependent on expensive contractors and its own bench is thin.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the growing dependence from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** ServiceGap, ContractorUse, InternalCapability (stock), TrainingEffort.
- **Required signed edges:** ServiceGap →(+) ContractorUse · ContractorUse →(−) ServiceGap · ServiceGap →(+)
  TrainingEffort · TrainingEffort →(+) InternalCapability **[DELAY: capability builds slowly]** ·
  InternalCapability →(−) ServiceGap · ContractorUse →(−) TrainingEffort.
- **Loop inventory:**
  - **B1 (symptomatic fix):** ServiceGap →(+) ContractorUse →(−) ServiceGap. (+,−) → **−** → **Balancing**,
    fast. ✓
  - **B2 (fundamental fix):** ServiceGap →(+) TrainingEffort →(+) InternalCapability →(−) ServiceGap.
    (+,+,−) → **−** → **Balancing**, with the capability-building **delay**. ✓
  - **R1 (dependence/erosion):** ContractorUse →(−) TrainingEffort →(+) InternalCapability →(−) ServiceGap
    →(+) ContractorUse. (−,+,−,+) → product **+** → **Reinforcing**. ✓
- **Dominant loop + shift:** the fast **B1** relieves the gap now, but by starving TrainingEffort it drives the
  reinforcing **R1**, which erodes InternalCapability (the delayed B2 weakens) → the gap re-widens → still more
  contractors. Dominance shifts from the quick fix (**B1**) to the eroding-fundamentals loop (**R1**). This is
  **shifting-the-burden** (addiction to the symptomatic fix).

**Trap (low score):** treating contractor use as a clean, stable fix (only **B1**) — **missing the reinforcing
dependence loop (R1)** that atrophies internal capability and deepens reliance.

---

## CLD-COMMONS-058 (L3 · ecology / economics)
**Prompt:** Dozens of independent farms draw irrigation water from one shared aquifer. Each farm that drills
deeper and pumps more raises its own harvest, so every farm expands — the water table barely moves at first,
then, after years, drops sharply and wells start failing for everyone at once.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the delayed collapse from the structure (not from "selfish farmers"), and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** FarmActivity, TotalExtraction, AquiferLevel (stock), HarvestPerFarm.
- **Required signed edges:** FarmActivity →(+) TotalExtraction · TotalExtraction →(+) HarvestPerFarm ·
  HarvestPerFarm →(+) FarmActivity · TotalExtraction →(−) AquiferLevel **[DELAY: slow drawdown]** ·
  AquiferLevel →(+) HarvestPerFarm.
- **Loop inventory:**
  - **R1 (individual expansion):** FarmActivity →(+) TotalExtraction →(+) HarvestPerFarm →(+) FarmActivity.
    (+,+,+) → **+** → **Reinforcing**. ✓
  - **B1 (shared-resource limit):** FarmActivity →(+) TotalExtraction →(−) AquiferLevel →(+) HarvestPerFarm
    →(+) FarmActivity. (+,−,+,+) → product **−** → **Balancing**, with the drawdown **delay**. ✓
- **Dominant loop + shift:** each farm's expansion is individually rational, so **R1 dominates** early and the
  slow aquifer drawdown hides the cost (the **delay** in B1 masks it). Once the level crosses a threshold, the
  balancing/limit loop **B1** bites hard and simultaneously for all — harvests crash together. Dominance shifts
  **R1 → B1/collapse**. This is the **tragedy of the commons**.

**Trap (low score):** seeing only the individually-rational reinforcing exploitation (**R1**) and expecting
continued gains — **missing the shared-resource balancing collapse (B1)** and the drawdown **delay** that makes
the crash sudden and common.

---

## CLD-SUCCESS-059 (L3 · organizations)
**Prompt:** A firm splits a fixed R&D budget between two promising projects. Early on, Project A posts slightly
better results, so it gets a bigger next-round allocation; the extra resources help it post better results
again, while Project B — starved — falls behind despite being nearly as good. Within a year A is "obviously the
winner." Results for each lag its funding by a quarter.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain why a tiny early lead became total dominance, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** AllocationToA, SuccessA, AllocationToB, SuccessB.
- **Required signed edges:** AllocationToA →(+) SuccessA **[DELAY: results lag funding]** · SuccessA →(+)
  AllocationToA · SuccessA →(−) AllocationToB · AllocationToB →(+) SuccessB **[DELAY]** · SuccessB →(+)
  AllocationToB · SuccessB →(−) AllocationToA.
- **Loop inventory:**
  - **R1 (A compounds):** AllocationToA →(+) SuccessA →(+) AllocationToA. (+,+) → **+** → **Reinforcing**. ✓
  - **R2 (B compounds):** AllocationToB →(+) SuccessB →(+) AllocationToB. (+,+) → **+** → **Reinforcing**. ✓
  - **R3 (competition coupling):** SuccessA →(−) AllocationToB →(+) SuccessB →(−) AllocationToA →(+) SuccessA.
    (−,+,−,+) → product **+** → **Reinforcing**. ✓
- **Dominant loop + shift:** the coupling loop **R3** (plus A's own **R1**) locks in whichever project leads
  first; a marginal early edge for A is amplified into dominance while B is starved. Dominance shifts from a
  near-tie to **R1/R3 for A** — the outcome is set by the initial condition, not by true merit. This is
  **success-to-the-successful**.

**Trap (low score):** attributing A's win to genuine superiority and expecting B to catch up on equal effort —
**missing the reinforcing allocation-coupling loop (R3)** that converts a tiny lead into lock-in.

---

## CLD-FIX-060 (L3 · economics)
**Prompt:** A household facing a monthly income shortfall covers it by borrowing on credit. Borrowing closes
this month's gap, but the growing debt carries interest, and the interest payments enlarge next month's
shortfall — so they borrow again, more. Within two years the shortfall is far worse than when they started.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the worsening shortfall from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** IncomeGap, Borrowing, DebtLevel (stock), InterestBurden.
- **Required signed edges:** IncomeGap →(+) Borrowing · Borrowing →(−) IncomeGap · Borrowing →(+) DebtLevel ·
  DebtLevel →(+) InterestBurden · InterestBurden →(+) IncomeGap **[DELAY: interest accrues over time]**.
- **Loop inventory:**
  - **B1 (borrow to cover):** IncomeGap →(+) Borrowing →(−) IncomeGap. (+,−) → **−** → **Balancing**, fast. ✓
  - **R1 (debt spiral):** IncomeGap →(+) Borrowing →(+) DebtLevel →(+) InterestBurden →(+) IncomeGap.
    (+,+,+,+) → product **+** → **Reinforcing**, with the interest **delay**. ✓
- **Dominant loop + shift:** the quick **B1** appears to solve the gap each month, but every use grows DebtLevel
  and thus the delayed **R1**, whose interest burden re-opens (and enlarges) the gap. Dominance shifts from the
  fix (**B1**) to the debt spiral (**R1**). This is **fixes-that-fail**.

**Trap (low score):** reading borrowing as solving the shortfall (only **B1**) — **missing the delayed
reinforcing debt-service loop (R1)** that makes the shortfall worse over time.

---

## CLD-ESCAL-061 (L3 · economics / social)
**Prompt:** Two competing supermarket chains fight for the same town. When A cuts prices, it wins share, so B
cuts prices to win it back, prompting A to cut again. Margins spiral down for both. Meanwhile the mounting
losses eventually force each chain to pull back on cutting — but only after a lag. The price war rages, pauses,
and periodically flares again.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the spiral and the periodic pullback from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** ThreatA (share pressure on A), ArmsA (A's price-cutting), ThreatB, ArmsB, CostBurden (losses).
- **Required signed edges:** ThreatA →(+) ArmsA · ArmsA →(+) ThreatB · ThreatB →(+) ArmsB · ArmsB →(+)
  ThreatA · ArmsA →(+) CostBurden · ArmsB →(+) CostBurden · CostBurden →(−) ArmsA **[DELAY: losses bite
  later]** · CostBurden →(−) ArmsB **[DELAY]**.
- **Loop inventory:**
  - **R1 (escalation):** ThreatA →(+) ArmsA →(+) ThreatB →(+) ArmsB →(+) ThreatA. (+,+,+,+) → product **+** →
    **Reinforcing**. ✓
  - **B1 (A's cost brake):** ArmsA →(+) CostBurden →(−) ArmsA. (+,−) → **−** → **Balancing**, delayed. ✓
  - **B2 (B's cost brake):** ArmsB →(+) CostBurden →(−) ArmsB. (+,−) → **−** → **Balancing**, delayed. ✓
- **Dominant loop + shift:** the **R1** escalation dominates the active price war (each cut provokes a counter);
  only when accumulated **CostBurden** grows do the delayed balancing brakes **B1/B2** dominate and force a
  pullback. The **delay** on the cost brakes lets the reinforcing spiral overshoot before it's checked, so
  dominance oscillates **R1 ↔ B1/B2** → recurring flare-ups. This is the **escalation** archetype.

**Trap (low score):** reading each chain's price cut as a stabilizing, defensive (balancing) move and expecting
a stable low-price equilibrium — **missing the reinforcing escalation loop (R1)** that drives the spiral.

---

## CLD-TRAFFIC-062 (L3 · public / infrastructure)
**Prompt:** A city widens its main highway to cut congestion. For a few months traffic flows freely — then,
over a year or two, the extra capacity draws more people to drive (and to move farther out and commute), and
congestion returns to roughly where it was, now with more total traffic. The city considers widening again.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain why widening failed to cut congestion, and name the effect.

**Reference solution — structure (auto-checkable):**
- **Variables:** Congestion, PressureToBuild, RoadCapacity (stock), Driving.
- **Required signed edges:** Congestion →(+) PressureToBuild · PressureToBuild →(+) RoadCapacity **[DELAY:
  construction]** · RoadCapacity →(−) Congestion · RoadCapacity →(+) Driving · Driving →(+) Congestion.
- **Loop inventory:**
  - **B1 (build to relieve):** Congestion →(+) PressureToBuild →(+) RoadCapacity →(−) Congestion. (+,+,−) →
    **−** → **Balancing**, with the construction **delay**. ✓
  - **R1 (induced demand):** RoadCapacity →(+) Driving →(+) Congestion →(+) PressureToBuild →(+) RoadCapacity.
    (+,+,+,+) → product **+** → **Reinforcing**. ✓
- **Dominant loop + shift:** the balancing **B1** relieves congestion at first (capacity up → congestion down),
  but the new capacity induces more Driving, so the reinforcing **R1** refills the road and even ratchets
  capacity/driving upward over time. Dominance shifts **B1 → R1** — congestion returns while total traffic
  grows. This is **induced demand**.

**Trap (low score):** expecting road-building to permanently cut congestion (only the balancing loop **B1**) —
**missing the induced-demand reinforcing loop (R1)** that refills new capacity.

---

## CLD-BURNOUT-063 (L3 · organizations / public-health)
**Prompt:** A hospital ward is short-staffed, so each nurse carries a heavy load. The stress drives some nurses
to quit, which raises the load on those remaining, driving more to quit. Management posts new jobs, but hiring
and onboarding take months. Staffing lurches from bad to worse despite constant recruiting.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the worsening staffing from the structure, and locate the leverage.

**Reference solution — structure (auto-checkable):**
- **Variables:** WorkloadPerNurse, Stress, Turnover, StaffLevel (stock), Hiring.
- **Required signed edges:** WorkloadPerNurse →(+) Stress · Stress →(+) Turnover **[DELAY: people leave over
  time]** · Turnover →(−) StaffLevel · StaffLevel →(−) WorkloadPerNurse · WorkloadPerNurse →(+) Hiring ·
  Hiring →(+) StaffLevel **[DELAY: hiring/onboarding lag]**.
- **Loop inventory:**
  - **R1 (burnout spiral):** WorkloadPerNurse →(+) Stress →(+) Turnover →(−) StaffLevel →(−) WorkloadPerNurse.
    (+,+,−,−) → product **+** → **Reinforcing**. ✓
  - **B1 (hire to relieve):** WorkloadPerNurse →(+) Hiring →(+) StaffLevel →(−) WorkloadPerNurse. (+,+,−) →
    **−** → **Balancing**, with the hiring **delay**. ✓
- **Dominant loop + shift:** the reinforcing **R1** (understaffing → stress → turnover → worse understaffing)
  dominates because the balancing hiring loop **B1** is too slow — its **delay** means new hires arrive after
  more nurses have already left. Dominance stays with **R1** unless the loop is broken (cut workload, retention)
  faster than hiring can refill.
- **Structure-not-blame (B):** nurses leaving are responding rationally to unsustainable load; the spiral is
  structural (a fast reinforcing loop outrunning a slow balancing one).

**Trap (low score):** treating turnover as purely a recruiting problem (only **B1**) — **missing the reinforcing
burnout loop (R1)** and that the hiring **delay** lets the spiral outpace the fix.

---

## CLD-ALBEDO-064 (L3 · climate / ecology)
**Prompt:** In the Arctic, warming melts sea ice. Ice is bright and reflects sunlight; open water is dark and
absorbs it. So as ice melts, the exposed water absorbs more heat, which melts more ice. A separate effect —
warmer surfaces radiate more heat to space — pushes back toward cooling. Scientists warn of a possible tipping
point.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance can shift.
3. Explain the tipping-point risk from the structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Temperature, IceMelt, IceCover (stock), Reflectivity, OutgoingRadiation.
- **Required signed edges:** Temperature →(+) IceMelt · IceMelt →(−) IceCover · IceCover →(+) Reflectivity ·
  Reflectivity →(−) Temperature · Temperature →(+) OutgoingRadiation · OutgoingRadiation →(−) Temperature.
- **Loop inventory:**
  - **R1 (ice-albedo):** Temperature →(+) IceMelt →(−) IceCover →(+) Reflectivity →(−) Temperature.
    (+,−,+,−) → product **+** → **Reinforcing**. ✓
  - **B1 (radiative damping):** Temperature →(+) OutgoingRadiation →(−) Temperature. (+,−) → **−** →
    **Balancing**. ✓
- **Dominant loop + shift:** normally the balancing **B1** (more heat radiated as it warms) keeps temperature
  in check. But past a threshold the reinforcing **R1** (albedo feedback) can **dominate** — melting begets
  warming begets melting — running away until the ice is gone. Dominance can shift **B1 → R1** at the tipping
  point.

**Trap (low score):** assuming the climate always self-stabilizes (only the balancing radiation loop **B1**) —
**missing the reinforcing ice-albedo loop (R1)** that can dominate past a tipping threshold.

---

## CLD-BANKRUN-065 (L3 · economics)
**Prompt:** A bank is rumored to be shaky. A few depositors withdraw; seeing the withdrawals, others fear for
their money and withdraw too, draining reserves and confirming the fear. The central bank can inject liquidity,
but the paperwork and decision take a day or two. Some banks stabilize; others collapse within hours.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance can shift.
3. Explain the run from the structure (not "irrational depositors"), and locate the leverage.

**Reference solution — structure (auto-checkable):**
- **Variables:** Fear, Withdrawals, BankReserves (stock), LiquiditySupport.
- **Required signed edges:** Fear →(+) Withdrawals · Withdrawals →(−) BankReserves · BankReserves →(−) Fear ·
  BankReserves →(−) LiquiditySupport · LiquiditySupport →(+) BankReserves **[DELAY: intervention lag]**.
- **Loop inventory:**
  - **R1 (the run):** Fear →(+) Withdrawals →(−) BankReserves →(−) Fear. (+,−,−) → product **+** →
    **Reinforcing**. ✓
  - **B1 (liquidity backstop):** BankReserves →(−) LiquiditySupport →(+) BankReserves. (−,+) → **−** →
    **Balancing**, with the intervention **delay**. ✓
- **Dominant loop + shift:** the reinforcing **R1** dominates once a run starts — each rational withdrawal
  lowers reserves and raises everyone's fear, accelerating the drain. The balancing backstop **B1** can restore
  stability *only if it acts before reserves hit zero*; its **delay** is decisive — fast support flips dominance
  to **B1** (bank survives), slow support lets **R1** finish the collapse.
- **Structure-not-blame (B):** withdrawing is individually rational given the structure; the fix is structural
  (deposit insurance, a fast lender of last resort), not exhorting depositors to stay calm.

**Trap (low score):** blaming the run on irrational depositors — **missing the reinforcing run loop (R1)** in
which each rational exit lowers reserves and raises fear; and ignoring that the backstop's **delay** decides the
outcome.

---

## CLD-HVAC-066 (L3 · infrastructure / personal)
**Prompt:** An old building's heating system reacts slowly: when the thermostat calls for heat, it takes a long
while for the radiators to warm the rooms. Occupants, feeling cold, crank the thermostat way up; long after,
the rooms get uncomfortably hot, so they throw it way down; then it gets too cold again. The temperature never
holds steady.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and the structural feature driving the behavior.
3. Explain why the temperature oscillates instead of settling.

**Reference solution — structure (auto-checkable):**
- **Variables:** RoomTemp (stock), TempGap (= setpoint − RoomTemp), HeatingOutput.
- **Required signed edges:** RoomTemp →(−) TempGap · TempGap →(+) HeatingOutput · HeatingOutput →(+) RoomTemp
  **[DELAY: slow thermal response]**.
- **Loop inventory:**
  - **B1 (thermostatic control):** RoomTemp →(−) TempGap →(+) HeatingOutput →(+) RoomTemp. (−,+,+) → product
    **−** → **Balancing**, with the thermal **delay**. ✓
- **Dominant loop + key feature:** a **single balancing loop** that would settle the room to setpoint **if not
  for the long thermal delay**. The delay makes occupants act on stale (cold) readings and over-correct → the
  room overshoots hot, they over-cut → it overshoots cold. **A balancing loop with a long delay oscillates.**
  The responsible feature is the **delay in the balancing loop**, not a second loop.

**Trap (low score):** expecting the thermostat to settle smoothly to setpoint — **ignoring the control delay**,
which is exactly what turns a balancing loop into sustained oscillation. (Also: mislabeling the control loop as
reinforcing because heat "adds.")

---

## CLD-PREDPREY-067 (L3 · ecology)
**Prompt:** In an isolated valley, a lot of prey (hares) means predators (lynx) are well-fed and raise many
young — but a lynx generation takes time to mature. The growing lynx population eats down the hares; with fewer
hares, lynx starve and decline; with few lynx, hares rebound; and the cycle repeats. Trappers' records show
both populations rising and falling in a long, repeating rhythm.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and the structural feature driving the behavior.
3. Explain why the populations cycle instead of settling at a balance.

**Reference solution — structure (auto-checkable):**
- **Variables:** Prey (stock), PredatorBirths, Predators (stock), Predation.
- **Required signed edges:** Prey →(+) PredatorBirths · PredatorBirths →(+) Predators **[DELAY: maturation
  lag]** · Predators →(+) Predation · Predation →(−) Prey.
- **Loop inventory:**
  - **B1 (predator–prey regulation):** Prey →(+) PredatorBirths →(+) Predators →(+) Predation →(−) Prey.
    (+,+,+,−) → product **−** → **Balancing**, with the maturation **delay**. ✓
- **Dominant loop + key feature:** a **single balancing loop** that *would* seek a steady coexistence
  **were it not for the predator-maturation delay**. The delay makes predator numbers respond to *past*
  prey abundance, so predators keep rising after prey have already turned down (and vice versa) → sustained
  **oscillation** (the Lotka–Volterra rhythm). The responsible feature is the **delay in the balancing loop**.

**Trap (low score):** expecting predator and prey to settle at a stable equilibrium — **ignoring the
reproduction delay** that converts the balancing regulation loop into a persistent oscillation.

---

## CLD-WAGEPRICE-068 (L3 · economics)
**Prompt:** After a supply shock lifts prices, workers demand higher wages to keep up; employers grant raises
but pass the higher labor costs into prices, prompting fresh wage demands. The central bank can raise interest
rates to cool prices, but the effect lands only after a lag. Inflation, once started, proves stubborn and
persistent rather than fading.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance can shift.
3. Explain the persistence of inflation from the structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Prices, WageDemands, Wages, ProductionCosts, InterestRates.
- **Required signed edges:** Prices →(+) WageDemands · WageDemands →(+) Wages · Wages →(+) ProductionCosts ·
  ProductionCosts →(+) Prices **[DELAY: cost pass-through]** · Prices →(+) InterestRates **[DELAY: policy
  response]** · InterestRates →(−) Prices.
- **Loop inventory:**
  - **R1 (wage-price spiral):** Prices →(+) WageDemands →(+) Wages →(+) ProductionCosts →(+) Prices.
    (+,+,+,+) → product **+** → **Reinforcing**. ✓
  - **B1 (monetary brake):** Prices →(+) InterestRates →(−) Prices. (+,−) → **−** → **Balancing**, with the
    policy **delay**. ✓
- **Dominant loop + shift:** the reinforcing **R1** sustains inflation once it starts (each price rise feeds
  wage demands feeds costs feeds prices). The balancing **B1** (rate hikes) can bring dominance back to
  disinflation, but its **delay** means it must act early and firmly; until it bites, **R1 dominates** and
  inflation persists. Dominance shifts **R1 → B1** only when the brake finally lands.

**Trap (low score):** treating the initial price jump as a one-off that fades — **missing the reinforcing
wage-price loop (R1)** that keeps it going; only a balancing intervention (with its delay) breaks the spiral.

---

## CLD-OUTRAGE-069 (L3 · social / AI)
**Prompt:** A social platform's recommender promotes whatever gets the most engagement. Outrage-provoking posts
get the most clicks and shares, so the algorithm amplifies them, which provokes more outrage and engagement.
Over months the feed grows angrier — until, with a lag, many users burn out and disengage, cooling things
briefly before the cycle resumes.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the rising toxicity from the structure (not "toxic users"), and locate the leverage.

**Reference solution — structure (auto-checkable):**
- **Variables:** Outrage, Engagement, AlgorithmicAmplification, UserFatigue.
- **Required signed edges:** Outrage →(+) Engagement · Engagement →(+) AlgorithmicAmplification ·
  AlgorithmicAmplification →(+) Outrage · Engagement →(+) UserFatigue **[DELAY: burnout builds slowly]** ·
  UserFatigue →(−) Engagement.
- **Loop inventory:**
  - **R1 (outrage amplification):** Outrage →(+) Engagement →(+) AlgorithmicAmplification →(+) Outrage.
    (+,+,+) → product **+** → **Reinforcing**. ✓
  - **B1 (burnout):** Engagement →(+) UserFatigue →(−) Engagement. (+,−) → **−** → **Balancing**, with the
    fatigue **delay**. ✓
- **Dominant loop + shift:** the reinforcing **R1** dominates and ratchets the feed toward outrage, because the
  engagement-maximizing rule rewards it. The balancing **B1** (fatigue) only bites after a **delay**, briefly
  cooling engagement before **R1** resumes → cycles of escalation and burnout. Dominance mostly sits with
  **R1**; leverage is the **amplification rule** (the algorithm's goal), not moderating individual users.
- **Structure-not-blame (B):** the outrage is manufactured by the reinforcing loop between engagement-optimizing
  amplification and human attention — not caused by uniquely toxic individuals.

**Trap (low score):** blaming toxic users and prescribing more moderation of individuals — **missing that the
engagement-optimizing algorithm forms the reinforcing loop (R1)** that manufactures the outrage; the leverage
is the rule, not the people.

---

## CLD-RESIST-070 (L3 · public-health)
**Prompt:** A hospital treats infections with a powerful antibiotic; it clears most cases quickly, so usage is
high. But heavy use gradually selects for resistant bacteria; as resistance spreads (with a lag), treatments
fail more often, infections linger and spread, and clinicians respond by using even more of the antibiotic.
Over years, infection rates climb despite aggressive treatment.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the rising infections from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** Infections, AntibioticUse, Resistance (stock), TreatmentFailures.
- **Required signed edges:** Infections →(+) AntibioticUse · AntibioticUse →(−) Infections · AntibioticUse →(+)
  Resistance **[DELAY: resistance builds slowly]** · Resistance →(+) TreatmentFailures · TreatmentFailures →(+)
  Infections.
- **Loop inventory:**
  - **B1 (treat the infection):** Infections →(+) AntibioticUse →(−) Infections. (+,−) → **−** → **Balancing**,
    fast. ✓
  - **R1 (resistance spiral):** Infections →(+) AntibioticUse →(+) Resistance →(+) TreatmentFailures →(+)
    Infections. (+,+,+,+) → product **+** → **Reinforcing**, with the resistance **delay**. ✓
- **Dominant loop + shift:** the balancing **B1** clears infections in the short run and looks effective. But
  every course of antibiotics grows the Resistance stock, driving the delayed reinforcing **R1** (failures →
  more infections → more use → more resistance). Long-term **R1 dominates** — infections climb despite (because
  of) heavy use. This is **fixes-that-fail** at population scale.

**Trap (low score):** seeing antibiotics as purely curative (only the balancing loop **B1**) — **missing the
delayed reinforcing resistance loop (R1)** in which overuse breeds resistance, failures, and more use.

---

## CLD-UNDERINVEST-071 (L3 · organizations)
**Prompt:** A popular online service grows its user base. As load rises, response times slip; management is
reluctant to fund big capacity upgrades ("demand might not last"), so investment lags and stays modest. Slow
service quietly drives some would-be users away, so growth stalls — which management reads as "the market is
saturated," justifying still less investment. The service plateaus far below its potential.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the self-imposed ceiling from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** Demand, Load, ServiceQuality, Investment, Capacity (stock).
- **Required signed edges:** Demand →(+) Load · Load →(−) ServiceQuality · ServiceQuality →(+) Demand
  **[DELAY: reputation adjusts slowly]** · Load →(+) Investment · Investment →(+) Capacity **[DELAY: capacity
  build]** · Capacity →(−) Load.
- **Loop inventory:**
  - **B1 (demand-quality limit):** Demand →(+) Load →(−) ServiceQuality →(+) Demand. (+,−,+) → product **−** →
    **Balancing**, with the reputation **delay**. ✓
  - **B2 (capacity relief):** Load →(+) Investment →(+) Capacity →(−) Load. (+,+,−) → product **−** →
    **Balancing**, with the build **delay**. ✓
- **Dominant loop + shift:** as demand grows, **B1** would normally be offset by the capacity loop **B2** — but
  because investment is kept modest and delayed, **B2 is too weak/slow**, so the quality-limit loop **B1**
  dominates: load erodes ServiceQuality, which caps Demand. Dominance sits with **B1** (a self-inflicted
  ceiling), and the low growth is misread as saturation → even less investment. This is **growth-and-
  underinvestment**.

**Trap (low score):** blaming the plateau on market saturation — **missing that under-scaled, delayed capacity
investment (weak B2) lets load erode service quality (B1)**, which is what actually caps demand.

---

## CLD-DIET-072 (L3 · personal-health)
**Prompt:** Someone starts a strict crash diet. Weight drops quickly at first, which is encouraging. But
severe restriction, sustained, lowers their metabolic rate (the body adapts to conserve energy), and the
slowed metabolism — with a lag — makes further loss stall and then reverse, often overshooting the starting
weight once normal eating resumes.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the early loss and later rebound from the structure, and name the archetype.

**Reference solution — structure (auto-checkable):**
- **Variables:** Weight (stock), DietRestriction, Metabolism.
- **Required signed edges:** Weight →(+) DietRestriction · DietRestriction →(−) Weight · DietRestriction →(−)
  Metabolism **[DELAY: metabolic adaptation]** · Metabolism →(−) Weight.
- **Loop inventory:**
  - **B1 (dieting):** Weight →(+) DietRestriction →(−) Weight. (+,−) → **−** → **Balancing**, fast. ✓
  - **R1 (metabolic adaptation):** DietRestriction →(−) Metabolism →(−) Weight →(+) DietRestriction.
    (−,−,+) → product **+** → **Reinforcing**, with the adaptation **delay**. ✓
- **Dominant loop + shift:** the balancing **B1** produces the encouraging early drop. But sustained restriction
  suppresses Metabolism (delayed), and lower metabolism means the same eating adds weight → more perceived need
  to restrict: the reinforcing **R1** takes over, stalling loss and driving rebound. Dominance shifts **B1 →
  R1**. This is **fixes-that-fail** (the yo-yo effect).

**Trap (low score):** crediting the diet because weight drops at first (only **B1**) — **missing the delayed
reinforcing metabolic-adaptation loop (R1)** that drives the plateau and rebound.

---

## CLD-EUTROPH-073 (L3 · ecology)
**Prompt:** A lake receives fertilizer runoff. The nutrients feed algae, which bloom, die, and decompose —
consuming the water's oxygen. Once the deep water goes low-oxygen, the lakebed sediments start releasing their
own stored phosphorus back into the water, feeding still more algae. Regulators later cut the farm runoff
sharply, but the lake stays green and murky for years.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain why cutting external runoff didn't quickly restore the lake, and name the effect.

**Reference solution — structure (auto-checkable):**
- **Variables:** Nutrients (stock), AlgaeGrowth, Oxygen, NutrientRelease, SunlightBlocking.
- **Required signed edges:** Nutrients →(+) AlgaeGrowth · AlgaeGrowth →(−) Oxygen · Oxygen →(−) NutrientRelease
  · NutrientRelease →(+) Nutrients · AlgaeGrowth →(+) SunlightBlocking · SunlightBlocking →(−) AlgaeGrowth.
- **Loop inventory:**
  - **R1 (internal loading):** Nutrients →(+) AlgaeGrowth →(−) Oxygen →(−) NutrientRelease →(+) Nutrients.
    (+,−,−,+) → product **+** → **Reinforcing**. ✓
  - **B1 (self-shading):** AlgaeGrowth →(+) SunlightBlocking →(−) AlgaeGrowth. (+,−) → **−** → **Balancing**. ✓
- **Dominant loop + shift:** at first external runoff drives the algae. Once anoxia sets in, the reinforcing
  **R1** (sediment phosphorus release) becomes self-sustaining — the lake **feeds itself**, so cutting external
  inputs barely helps. Dominance shifts from the external nutrient source to the internal-loading loop **R1**,
  which locks in the degraded, green state (**hysteresis**); the balancing self-shading loop **B1** only caps
  peak density, not the nutrient supply.

**Trap (low score):** assuming that cutting external nutrient inputs quickly restores the lake — **missing the
reinforcing internal-loading loop (R1)** (anoxia releases sediment phosphorus) that locks in the degraded state.

---

## CLD-HYPE-074 (L3 · markets / AI)
**Prompt:** A new technology bursts into public attention: coverage begets more coverage, and excitement runs
far ahead of what the tech can yet do. Inflated expectations set everyone up for disappointment, and — after a
lag, as real results underwhelm — disillusionment sets in and attention crashes, well below the peak, before a
slower, more realistic recovery. Observers describe a predictable "hype cycle."
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the peak-and-trough from the structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Attention, Hype, Expectations, Disillusionment.
- **Required signed edges:** Attention →(+) Hype · Hype →(+) Attention · Hype →(+) Expectations ·
  Expectations →(+) Disillusionment **[DELAY: reality lags the promise]** · Disillusionment →(−) Attention.
- **Loop inventory:**
  - **R1 (hype amplification):** Attention →(+) Hype →(+) Attention. (+,+) → **+** → **Reinforcing**. ✓
  - **B1 (disillusionment correction):** Hype →(+) Expectations →(+) Disillusionment →(−) Attention →(+) Hype.
    (+,+,−,+) → product **−** → **Balancing**, with the reality **delay**. ✓
- **Dominant loop + shift:** the reinforcing **R1** drives the early spike (attention and hype feed each other).
  The balancing **B1** — inflated expectations breeding delayed disillusionment — eventually dominates, and
  because of its **delay** it doesn't gently level the curve but overshoots *downward* (the trough) before a
  realistic recovery. Dominance shifts **R1 → B1** (the Gartner-style hype cycle).

**Trap (low score):** extrapolating the early hype linearly (or expecting a smooth plateau) — **missing the
delayed disillusionment balancing loop (B1)** whose delay produces the peak-and-trough overshoot.

---

## CLD-SKILL-075 (L3 · personal / behavioral)
**Prompt:** A beginner takes up the guitar. Early practice yields fast, visible improvement, which builds
confidence and makes them want to practice more — a great start. Months in, though, the same practice yields
smaller gains (diminishing returns), and the growing ease breeds a bit of boredom, which quietly cuts practice
time. Progress stalls on a plateau, and some quit, puzzled that the early magic faded.
1. Map variables, signed links, and feedback loops (polarity R/B + delays).
2. Identify the dominant loop and how dominance shifts over time.
3. Explain the fast start and the plateau from the structure.

**Reference solution — structure (auto-checkable):**
- **Variables:** Skill (stock), Confidence, Practice, Boredom.
- **Required signed edges:** Skill →(+) Confidence · Confidence →(+) Practice · Practice →(+) Skill
  **[DELAY: skill builds with a lag]** · Skill →(+) Boredom · Boredom →(−) Practice.
- **Loop inventory:**
  - **R1 (virtuous practice):** Skill →(+) Confidence →(+) Practice →(+) Skill. (+,+,+) → product **+** →
    **Reinforcing**. ✓
  - **B1 (complacency/plateau):** Skill →(+) Boredom →(−) Practice →(+) Skill. (+,−,+) → product **−** →
    **Balancing**. ✓
- **Dominant loop + shift:** early, the reinforcing **R1** dominates — visible gains build confidence and drive
  more practice (the "fast start"). As Skill rises, diminishing returns weaken R1's payoff while the balancing
  **B1** strengthens (mastery breeds boredom → less practice), so **B1** comes to dominate → the plateau.
  Dominance shifts **R1 → B1**.

**Trap (low score):** expecting the early fast-improvement (reinforcing) phase to continue indefinitely —
**missing the balancing complacency / diminishing-returns loop (B1)** that produces the plateau.

---

## Grading

**Three tiers, one deterministic convention (loop polarity = product of signed edges); no jury for structure.**

- **L1 (recognition) — deterministic, exact.** Score the single answer required: a link's polarity (+/−), a
  loop's type (R/B, computed as the product of its edge signs), a loop count, or the named behavior mode
  (R → growth/collapse; B → goal-seeking/stabilize). The signature L1 check is the **two-negatives → reinforcing**
  parity result. Correct = 1.0; wrong = 0.

- **L2 (understanding) — deterministic structure + behavior-mode.** Require (a) correct loop polarities and
  (b) the correct **behavior over time** with its mechanism (exponential growth / accelerating collapse /
  goal-seeking asymptote / S-curve / delay-driven oscillation-or-overshoot) and, where one applies, the named
  **archetype** (limits-to-growth, fixes-that-fail, shifting-the-burden, escalation). Correct polarities but
  wrong/absent behavior = 0.5.

- **L3 (application) — structural oracle + dynamic insight (as before).** Per item, check (1) canonical
  variables present, (2) each REQUIRED signed edge present + correct polarity, (3) loop count + each R/B sign =
  product of its edges, (4) the **dominant loop / dominant-loop shift** (or the key **delay**) named. Structure
  without the dynamic insight = 0.5; R↔B mislabel of the dominant loop = trap (≤0.25).

- **Completeness/quality sub-score (jury):** clarity, parsimony, behavior-over-time narrative — **jury-graded,
  and CLD jury is `UNCALIBRATED — not scored` until a CLD gold set clears §3.1/§4.0** (fail-closed; no jury
  number emitted).

- Each item logs whether the model fell into the **named trap** (R↔B mislabel of the dominant loop, omitting a
  loop, or the two-negatives parity error at L1) — trap-rate is itself a leverage-profile signal.

**Auto-scorer wiring status (honest):**
- The **original five L3 items (001–005)** are wired into `items/cld_oracle.json` and machine-graded by
  `engine/cld-score.py` (partition-robust; topology+sign matching, v2).
- The **20 new L3 items (056–075)** ship with full auto-checkable reference solutions above and have been
  **verified deterministically consistent against the live scorer** (loop signs 41/41 = product of edges; each
  reference round-trips to 1.0; partial = 0.5; dominant-loop mislabel ≤ 0.25). They are **ready to wire into
  `cld_oracle.json` + `harness_prompts.json`**; that wiring (and bumping the scorer's self-test loop-count) is
  a small, gated engine step flagged for a follow-up SenseRun — not done in this authoring pass.
- The **L1/L2 tier** is gradeable by the same loop-polarity convention but is **not yet in the auto-scorer**:
  the current scorer's insight-gate is L3-tuned (it caps any item lacking a dominant-shift/delay insight at
  0.5), so grading L1/L2 needs a small scorer-rubric extension (recognition/behavior-mode scoring without the
  L3 insight gate). Flagged as future engine work; until then L1/L2 grade against the reference answers above.

**Partition-robust grading (scorer v2, 2026-06-13):** the L3 structural scorer matches loops by **topology +
sign (loop polarity = product of signed edges), not by node name** — so a valid *re-partition* (collapsing or
renaming nodes) that preserves the feedback structure is graded as correct systems thinking (Meadows'
"structure > elements" / "boundaries are pragmatic"). See `engine/cld-score.py`,
`results/CLD-V2-RESCORE-2026-06-13.md`.
