# SystemsBench — Stock-Flow Inference (`SF`) seed item set

**Format:** SF · **Grading:** deterministic (numeric / qualitative-shape oracle, NO judge) · **Seeded:** 2026-05-31 · **Expanded to 75:** 2026-07-03
**Constructs:** A (stocks vs flows), D (behavior over time) · **Contamination:** templatable — regenerate numbers/domain per run.
**Why this format:** Sweeney & Sterman (2000) — even MIT grad students systematically fail stock-flow inference; performance is uncorrelated with math/general ability. The most empirically discriminating systems-thinking task known. The canonical error is the **"correlation heuristic"**: assuming the stock's shape matches the net-flow's shape.

**Bank size: 75 items — 25 L1 · 25 L2 · 25 L3.** Difficulty is operational (Structure §3.2): **L1 recognition** (name the stock/flow; read a net flow's sign; one- or few-step accumulation), **L2 understanding** (integrate a schedule; find a peak/steady state; explain the dynamic a structure produces), **L3 application** (map a novel scenario where the intuitive answer is wrong — bathtub/climate, delay-driven overshoot, state-dependent flows, irreversibility; a correct answer must name the *mechanism*, not just the trajectory). Every item names its trap; the trap is (almost always) some form of the correlation heuristic — confusing a flow with a stock, or a change in a flow with a change in the stock.

---

# L1 — Recognition (25 items)

*Name the stock and the flow; take the sign of the net flow; accumulate over one or a few steps.*

## SF-RES-001 (L1 · ecology/water)
**Prompt:** A reservoir starts at 100 ML. For 4 hours, inflow is constant 30 ML/h and outflow is constant 20 ML/h. What is the volume after 4 hours? Is the reservoir rising, falling, or steady?
**Oracle (exact):** net flow = +10 ML/h → 100 + 4×10 = **140 ML; rising.**
**Trap:** answering "steady" because inflow and outflow are each constant (confusing constant *flows* with a constant *stock*).

## SF-BATH-006 (L1 · personal/water · classification)
**Prompt:** Water runs from a tap into a bathtub while the drain is partly open. Of these three quantities — the amount of water in the tub, the flow from the tap, the flow down the drain — which is the **stock**, and which are the **flows**?
**Oracle (exact):** stock = **amount of water in the tub**; flows = **tap rate (inflow)** and **drain rate (outflow)**. The stock is a level (measured in litres); the flows are rates (litres per minute).
**Trap:** calling the tap flow the "stock" because it's the visible cause — confusing a rate (per-time) with a level (an accumulation).

## SF-ACCT-007 (L1 · economics/personal-finance)
**Prompt:** A checking account holds $500. During one month there is a single $200 deposit and a single $50 withdrawal, and nothing else. What is the balance at month end? Is the balance higher or lower than it started?
**Oracle (exact):** 500 + 200 − 50 = **$650; higher (rose $150).**
**Trap:** answering "$200" or "$150" — reporting a *flow* (the deposit or the net change) instead of the resulting *stock*.

## SF-POP-008 (L1 · ecology/social)
**Prompt:** A town has 10,000 people. Over one year there are 300 births and 200 deaths, and no migration. What is the population at year end? Is it rising, falling, or steady?
**Oracle (exact):** net = 300 − 200 = +100 → 10,000 + 100 = **10,100; rising.**
**Trap:** answering "steady" because "people are both being born and dying" — births and deaths both being nonzero does not make the stock steady; only births = deaths would.

## SF-WARE-009 (L1 · operations/inventory)
**Prompt:** A warehouse holds 200 units this morning. During the day, 40 units arrive and 25 units ship out. How many units are in the warehouse at day's end? Is the level rising or falling?
**Oracle (exact):** net = +40 − 25 = +15 → **215 units; rising.**
**Trap:** answering "40" or "15" (a flow) rather than the resulting level, or "falling" by fixating on the outflow.

## SF-INBOX-010 (L1 · software/infra · queue)
**Prompt:** An inbox has 40 unread messages. Over one day, 30 new messages arrive and you read 20. How many unread messages remain at day's end? Is the unread count rising or falling?
**Oracle (exact):** net = +30 − 20 = +10 → **50 unread; rising.**
**Trap:** answering "falling" because "you read messages all day" — reading (outflow) is smaller than arrivals (inflow), so the stock rises.

## SF-FOREST-011 (L1 · ecology)
**Prompt:** A managed woodlot has 1,000 trees. In one year, 50 trees are planted and 30 are cut. How many trees at year end? Rising or falling?
**Oracle (exact):** net = +50 − 30 = +20 → **1,020 trees; rising.**
**Trap:** subtracting only ("30 cut → 970") and ignoring the planting inflow, or reporting a flow.

## SF-LABEL-012 (L1 · organizations · classification)
**Prompt:** Label each of the following as a **stock** or a **flow**: (a) money in a savings account, (b) monthly salary, (c) number of employees, (d) the hiring rate, (e) water in a lake, (f) the evaporation rate.
**Oracle (exact):** stocks = **(a) savings, (c) employees, (e) water in the lake** (levels you could measure at an instant); flows = **(b) salary, (d) hiring rate, (f) evaporation rate** (rates, measured per unit time). Test: a flow always has a "per time" in its unit; a stock does not.
**Trap:** calling salary or hiring rate a "stock" — anything expressed *per month / per year* is a flow.

## SF-BATT-013 (L1 · personal/tech)
**Prompt:** A phone is at 60% charge. While plugged in, charging adds 10 percentage points per hour and the phone's use drains 4 points per hour, for 3 hours. What is the charge level after 3 hours (assume it doesn't reach 100%)? Rising or falling?
**Oracle (exact):** net = +10 − 4 = +6 pts/h → 60 + 3×6 = **78%; rising.**
**Trap:** using only the charge rate (+10 → 90%) and ignoring the simultaneous drain outflow.

## SF-STEADY-014 (L1 · ecology/water)
**Prompt:** A tank holds 100 L. For 5 hours the inflow is a constant 25 L/h and the outflow is a constant 25 L/h. What is the level after 5 hours? Rising, falling, or steady?
**Oracle (exact):** net = 25 − 25 = 0 → **100 L; steady.**
**Trap:** answering "rising" because "25 L/h keeps pouring in" — a large but *balanced* inflow leaves the stock unchanged. (This is the mirror of SF-RES-001: there, equal-looking constant flows were *not* equal.)

## SF-LOAN-015 (L1 · economics)
**Prompt:** You owe $1,000 on a no-interest loan. You pay $100 per month for 3 months and borrow nothing new. What is the balance after 3 months? Rising or falling?
**Oracle (exact):** 1,000 − 3×100 = **$700; falling.**
**Trap:** answering "$300" — reporting the total paid (a cumulative flow) instead of the remaining stock.

## SF-DRAW-016 (L1 · ecology/water)
**Prompt:** A reservoir holds 100 ML. For 4 hours inflow is 10 ML/h and outflow is 25 ML/h. What is the volume after 4 hours? Rising or falling?
**Oracle (exact):** net = 10 − 25 = −15 ML/h → 100 − 4×15 = **40 ML; falling.**
**Trap:** answering "rising" or "steady" because water is still flowing *in* — a positive inflow below the outflow still drains the stock.

## SF-ROOM-017 (L1 · public-health · classification + net)
**Prompt:** A waiting room has 12 people. Over one hour, 5 people enter and 8 leave. Which is the stock and which are the flows, and how many people are in the room after the hour?
**Oracle (exact):** stock = **people in the room** (currently 12); flows = **entry rate and exit rate**. Net = 5 − 8 = −3 → **9 people.**
**Trap:** reporting a flow ("8 left") as the answer, or miscounting net direction.

## SF-SNOW-018 (L1 · ecology)
**Prompt:** There is 20 cm of snow on the ground. In one day, 5 cm of new snow falls and 2 cm melts. How much snow at day's end? Rising or falling?
**Oracle (exact):** net = +5 − 2 = +3 → **23 cm; rising.**
**Trap:** reporting a flow (the 5 cm that fell) or ignoring melt.

## SF-MEM-019 (L1 · AI/agent)
**Prompt:** An agent's memory holds 50 stored facts. In one work session it learns 12 new facts and forgets (drops) 4. How many facts are stored after the session? Rising or falling?
**Oracle (exact):** net = +12 − 4 = +8 → **58 facts; rising.**
**Trap:** reporting the number learned (12) as the total, or ignoring the forgetting outflow.

## SF-TODO-020 (L1 · personal/behavioral · queue)
**Prompt:** Your to-do list has 15 tasks. Over one week you add 8 new tasks and complete 5. How many tasks remain at week's end? Rising or falling?
**Oracle (exact):** net = +8 − 5 = +3 → **18 tasks; rising.**
**Trap:** answering "falling" because "you got things done" — completions (5) are fewer than additions (8), so the backlog grows.

## SF-CUST-021 (L1 · organizations/markets)
**Prompt:** A business has 5,000 customers. In one quarter it gains 400 and loses 150. How many customers at quarter end? Rising or falling?
**Oracle (exact):** net = +400 − 150 = +250 → **5,250 customers; rising.**
**Trap:** reporting a flow (400 gained) or subtracting only the losses.

## SF-DISK-022 (L1 · software/infra)
**Prompt:** A disk has 200 GB used. In one day, 30 GB is written and 10 GB is deleted. How much is used at day's end? Rising or falling?
**Oracle (exact):** net = +30 − 10 = +20 → **220 GB used; rising.**
**Trap:** treating "deleting frees space" as dominant when the write inflow is larger.

## SF-POND-023 (L1 · ecology/fisheries)
**Prompt:** A stocked pond holds 500 fish. In one season 80 fish are added and 100 are caught. How many fish at season's end? Rising or falling?
**Oracle (exact):** net = +80 − 100 = −20 → **480 fish; falling.**
**Trap:** answering "rising" because fish were added — the harvest outflow exceeds the stocking inflow.

## SF-FOLLOW-024 (L1 · social)
**Prompt:** An account has 2,000 followers. In one month it gains 300 and loses 500. How many followers at month end? Rising or falling?
**Oracle (exact):** net = +300 − 500 = −200 → **1,800 followers; falling.**
**Trap:** fixating on the 300 gained and calling it growth, ignoring the larger loss outflow.

## SF-HEAT-025 (L1 · personal/infra · classification)
**Prompt:** In a heated house, identify the **stock** and the **flows**: the heat energy stored in the house (its temperature), the furnace's heat output, and the heat leaking out through the walls.
**Oracle (exact):** stock = **heat energy stored in the house (its temperature)**; flows = **furnace output (inflow)** and **heat loss through the walls (outflow)**. Temperature is a level; the two heat rates are flows.
**Trap:** calling the furnace output the "stock" — it's a rate of energy delivery, not the stored amount.

## SF-QUEUE-026 (L1 · AI/agent · queue)
**Prompt:** A content-moderation queue holds 100 flagged items. In one hour, 40 new items are flagged and 60 are resolved. How many remain queued after the hour? Rising or falling?
**Oracle (exact):** net = +40 − 60 = −20 → **80 items; falling.**
**Trap:** answering "rising" because "items keep getting flagged" — resolutions (60) outpace arrivals (40), so the queue shrinks.

## SF-RAIN-027 (L1 · ecology/water)
**Prompt:** A rain barrel holds 30 L. In one day, 12 L of rain runs in and you draw 5 L for the garden. How much water at day's end? Rising or falling?
**Oracle (exact):** net = +12 − 5 = +7 → **37 L; rising.**
**Trap:** reporting a flow, or subtracting only the 5 L drawn.

## SF-SUB-028 (L1 · markets · steady case)
**Prompt:** A newsletter has 8,000 subscribers. In one month 500 people subscribe and 500 unsubscribe. How many subscribers at month end? Rising, falling, or steady?
**Oracle (exact):** net = 500 − 500 = 0 → **8,000 subscribers; steady.**
**Trap:** answering "growing" because "500 new people joined" — equal in- and out-flows hold the stock flat despite lots of churn on both sides.

## SF-BED-029 (L1 · public-health)
**Prompt:** A hospital ward has 120 occupied beds. Over one day there are 25 admissions and 30 discharges. How many occupied beds at day's end? Rising or falling?
**Oracle (exact):** net = +25 − 30 = −5 → **115 occupied; falling.**
**Trap:** treating admissions as the answer, or misreading the net direction when discharges exceed admissions.

---

# L2 — Understanding (25 items)

*Integrate a schedule; find when a stock peaks (net flow crosses zero) or settles (inflow = a stock-dependent outflow); explain the dynamic a structure produces — including the correlation heuristic on a changing flow.*

## SF-BANK-002 (L2 · economics/debt)
**Prompt:** A debt stock is $10,000. Monthly interest adds 1% of the current debt (inflow); you pay $80/month (outflow). In month 1, does the debt rise or fall? What does this tell you about the long-run trajectory if payment stays fixed?
**Oracle:** month-1 interest = $100 > $80 payment → net +$20 → **debt rises**, and since interest grows with the (rising) stock while payment is fixed, it's a **reinforcing loop → accelerating growth** (debt spiral). Correct answer must identify the *reinforcing* structure, not just month 1.
**Trap:** "it falls because you're making payments" — ignores that the inflow is a function of the stock (compounding).

## SF-INV-004 (L2 · operations/inventory)
**Prompt:** A warehouse holds 500 units. Over a week: Mon +50 in/−20 out, Tue +10/−40, Wed +0/−30, Thu +60/−10, Fri +20/−20. Net stock Friday close? On which day did the stock first *decrease*?
**Oracle:** daily net: Mon +30, Tue −30, Wed −30, Thu +50, Fri 0. Running: 530, 500, 470, 520, 520 → **520 units Friday; first decrease on Tuesday.** Requires integrating flows, not reading a single day.
**Trap:** picking the day with the largest single outflow (Tue −40) by magnitude rather than the first *net* decrease.

## SF-HIRE-030 (L2 · organizations · correlation heuristic)
**Prompt:** A firm's net headcount change (hires minus departures) is +200 in Q1, +150 in Q2, +100 in Q3, +50 in Q4 — positive every quarter but shrinking. Is headcount at year-end higher or lower than at the start? Is it still rising in Q4?
**Oracle:** higher by 200+150+100+50 = **+500; and still rising in Q4** (net +50 > 0). A *decreasing but positive* net flow means the stock rises more *slowly*, not that it falls.
**Trap:** "headcount is falling because the hiring rate is dropping" — the correlation heuristic: mistaking a falling flow for a falling stock.

## SF-PEAK-031 (L2 · ecology/water · peak = net-flow zero crossing)
**Prompt:** A reservoir starts at 100 ML. Hours 1–3: inflow 40, outflow 20 ML/h. Hours 4–6: inflow 10, outflow 30 ML/h. What is the volume at the end of hour 6, and at what hour is the volume highest?
**Oracle:** phase 1 net +20/h → 100 + 3×20 = 160 at end of hour 3; phase 2 net −20/h → 160 − 3×20 = 100. **End = 100 ML; peak = 160 ML at hour 3** — the stock peaks exactly when net flow flips from + to −.
**Trap:** assuming the volume peaks at the end (hour 6) or where inflow is largest — the peak is where *net* flow crosses zero.

## SF-TICKET-032 (L2 · software/infra · queue growth)
**Prompt:** Support tickets arrive at 50/day and the team resolves 40/day; the backlog starts at 0. What is the backlog after 30 days, and what is its long-run trajectory if nothing changes?
**Oracle:** net = +10/day → **300 after 30 days; grows without bound** (linearly, +10/day) as long as arrivals exceed resolutions.
**Trap:** "the team is resolving tickets, so the backlog shrinks or stabilizes" — a nonzero, even large, outflow can't drain a stock whose inflow is larger.

## SF-CASH-033 (L2 · organizations · runway)
**Prompt:** A startup has $1,000,000 cash. It spends $150,000/month and earns $50,000/month in revenue. How many months until it runs out of cash?
**Oracle:** net burn = 150k − 50k = $100k/month → 1,000,000 / 100,000 = **10 months.**
**Trap:** dividing by gross spend ($150k → ~6.7 months) and ignoring the revenue inflow that partly offsets it.

## SF-STEADYK-034 (L2 · ecology/water · steady state, stock-dependent outflow)
**Prompt:** A tank has a constant inflow of 20 L/min. Its outflow is 0.1 × (current volume) L/min — it drains faster the fuller it is. At what volume does the level stop changing?
**Oracle:** steady when inflow = outflow → 20 = 0.1V → **V = 200 L.**
**Trap:** "it fills forever" — ignores that a stock-proportional outflow rises with the level until it balances the constant inflow (a self-limiting, balancing structure).

## SF-SAVE-035 (L2 · personal/finance · reinforcing)
**Prompt:** You deposit $100 at the end of each month into an account paying 1%/month interest, starting from $0. Does the balance grow linearly (a straight line) or accelerate over time? Why?
**Oracle:** it **accelerates** — each month's increase is $100 *plus* 1% of the current balance, and that interest grows as the balance grows (interest-on-interest is a reinforcing loop). The trajectory curves upward, faster than a straight line.
**Trap:** "linear — just $100 × number of months" — ignores that part of the inflow is a function of the stock.

## SF-PAYOFF-036 (L2 · economics · payment vs interest)
**Prompt:** A $5,000 debt accrues 2%/month interest; you pay $150/month. In month 1, does the balance rise or fall? Will the loan ever be paid off at this fixed payment?
**Oracle:** month-1 interest = 2% × 5,000 = $100 < $150 payment → net −$50 → **balance falls; yes, it gets paid off.** Because payment exceeds interest and interest *shrinks* as the balance falls, net flow stays negative all the way down. (Contrast SF-BANK-002, where interest exceeded the payment.)
**Trap:** "interest means it never gets paid off" — the decisive comparison is payment vs. interest; here the payment wins.

## SF-CHURN-037 (L2 · social · steady state)
**Prompt:** An app gains a constant 100 new users/week and loses 5% of its *current* users to churn each week. At what user count does the base stop growing?
**Oracle:** steady when inflow = outflow → 100 = 0.05 × U → **U = 2,000 users.**
**Trap:** "it grows forever at +100/week" — churn scales with the (growing) base until it exactly offsets the constant inflow.

## SF-OVERFLOW-038 (L2 · ecology/water · time-to-threshold)
**Prompt:** A reservoir has a 300 ML capacity and currently holds 120 ML. Inflow is 40 ML/h, outflow 25 ML/h. After how many hours does it overflow?
**Oracle:** net = +15 ML/h; remaining headroom = 300 − 120 = 180 → 180 / 15 = **12 hours.**
**Trap:** dividing headroom by the *inflow* (180 / 40 = 4.5 h) and ignoring the outflow that slows the fill.

## SF-BAC-039 (L2 · personal/health · peak when inflow stops)
**Prompt:** Someone drinks steadily, adding alcohol to the blood at 8 g/h for 3 hours, then stops. The liver clears alcohol at a constant 6 g/h throughout. Starting from 0, at what time is blood alcohol highest, and roughly how much?
**Oracle:** while drinking, net = +8 − 6 = +2 g/h (rising); after drinking stops, net = −6 g/h (falling). **Peak at hour 3 ≈ 3 × 2 = 6 g** — the peak is when the inflow stops and net flow turns negative, *not* at the first drink.
**Trap:** thinking blood alcohol peaks the moment you start (or peaks immediately after the last drink and is already falling during drinking) — it rises the whole time inflow exceeds clearance.

## SF-AQUI-040 (L2 · ecology/economics · rising outflow crosses inflow)
**Prompt:** An aquifer recharges at a constant 100 ML/yr. Extraction is 60 ML/yr in year 1 and rises 10 ML/yr each year. In which year does the aquifer level *begin to fall*?
**Oracle:** extraction by year: 60, 70, 80, 90, 100, 110. It equals recharge (100) in year 5 (steady) and first exceeds it in **year 6** (110 > 100) — the stock begins to fall in year 6.
**Trap:** "it starts falling in year 2, when extraction starts rising" — a rising outflow only drains the stock once it exceeds the inflow.

## SF-INVWK-041 (L2 · operations · integrate + find peak)
**Prompt:** A parts bin holds 300 units Monday morning. Daily in/out: Mon +40/−20, Tue +60/−30, Wed +10/−50, Thu +30/−20, Fri +20/−40. What is the level at Friday close, and on which day is the bin fullest?
**Oracle:** daily net: Mon +20, Tue +30, Wed −40, Thu +10, Fri −20. Running closes: 320, **350**, 310, 320, 300. **Friday close = 300; fullest = 350 on Tuesday.**
**Trap:** reading a single day (e.g., the biggest inflow) or assuming the last day is fullest, instead of tracking the running total.

## SF-RIVER-042 (L2 · ecology/water · correlation heuristic, numeric)
**Prompt:** A lake's inflow is 50 ML/h in hour 1 and drops 5 ML/h each hour (50, 45, 40, 35, …). Outflow is a constant 20 ML/h. During hours 1–4, is the lake rising or falling, even though inflow is dropping?
**Oracle:** net = inflow − 20 = +30, +25, +20, +15 for hours 1–4 — all positive → **the lake rises every hour** (just more slowly). It keeps rising until inflow falls below 20 (around hour 8).
**Trap:** "the lake is falling because inflow is decreasing" — a decreasing inflow that's still *above* outflow means a rising stock.

## SF-HEATER-043 (L2 · personal/infra · steady-state temperature)
**Prompt:** A water heater adds heat that would raise a perfectly insulated tank by 10°C/h. Heat loss = 0.5°C/h for every °C the water is above the 20°C room. At what temperature does the water settle?
**Oracle:** steady when gain = loss → 10 = 0.5 × (T − 20) → T − 20 = 20 → **T = 40°C.**
**Trap:** "it heats up without limit" — loss grows with temperature until it balances the constant heating input.

## SF-CACHE-044 (L2 · software/infra · steady state)
**Prompt:** A cache receives 500 new entries/min. Its eviction policy removes 10% of the *current* entries each minute. At what size does the cache stabilize?
**Oracle:** steady when inflow = outflow → 500 = 0.10 × N → **N = 5,000 entries.**
**Trap:** "it fills without bound" — eviction scales with size and eventually balances the constant write inflow.

## SF-AGENT-045 (L2 · AI/agent · correlation heuristic)
**Prompt:** An agent adds facts to its knowledge base at a *decreasing* rate — 40 in session 1, 30 in session 2, 20 in session 3, 10 in session 4 — and never deletes any. Over these four sessions, is the knowledge base growing or shrinking?
**Oracle:** **growing every session** — totals go 40, 70, 90, 100. With every inflow positive and zero outflow, the stock only rises; a decreasing inflow slows growth but never shrinks the stock.
**Trap:** "the knowledge base is shrinking because it's learning less each session" — a falling *inflow* is not a falling *stock*.

## SF-WEIGHT-046 (L2 · personal/behavioral · correlation heuristic)
**Prompt:** A person's daily calorie surplus (intake minus expenditure) shrinks over four weeks — +500/day, +300, +150, +50 — but stays positive. Is their stored body fat higher or lower after four weeks? Is it still rising in week 4?
**Oracle:** **higher, and still rising in week 4** — a positive surplus every week means fat accumulates the whole time; a shrinking surplus slows the gain but doesn't cause loss (that needs a *deficit*, surplus < 0).
**Trap:** "they're losing weight because the surplus is dropping" — the correlation heuristic applied to body weight.

## SF-COHORT-047 (L2 · organizations · steady-state headcount)
**Prompt:** A company hires a constant 30 people/month; attrition runs at 2% of headcount/month. What is the steady-state headcount?
**Oracle:** steady when inflow = outflow → 30 = 0.02 × H → **H = 1,500 people.**
**Trap:** "headcount grows forever at +30/month" — attrition scales with headcount until it offsets the constant hiring.

## SF-DAM-048 (L2 · ecology/water · integrate + threshold)
**Prompt:** A reservoir starts at 200 ML. The net weekly change over five weeks is −40, −40, +10, +60, +50. What is the volume at the end of week 5, and in which week does the volume first climb back above its 200 ML starting level?
**Oracle:** running: 160, 120, 130, 190, **240**. **End = 240 ML; first exceeds 200 in week 5** (week 4 is still 190).
**Trap:** seeing three straight positive weeks (3–5) and assuming it recovered earlier than it did, or reading the last week's flow (+50) as the answer.

## SF-EMISS-049 (L2 · public-health/ecology · proportional sink → steady state)
**Prompt:** A factory releases a pollutant into a pond at a constant 100 kg/yr. The pond breaks it down at 5%/yr of the amount present. Does the pollutant rise forever, or approach a steady level — and what level?
**Oracle:** it **approaches a steady state**: removal rises with the amount present until 100 = 0.05 × S → **S = 2,000 kg.** (Contrast: if breakdown were a *constant* below 100 kg/yr, the stock would rise without bound.)
**Trap:** "it rises forever because emissions never stop" — true only if the sink is fixed/saturated; a stock-proportional sink balances a constant inflow.

## SF-SALES-050 (L2 · operations/markets · rising outflow crosses inflow)
**Prompt:** A factory produces a constant 500 units/day into inventory. Sales start at 400/day and rise 20/day each day. Inventory starts at 1,000. On which day does inventory *begin to fall*?
**Oracle:** sales: 400, 420, 440, 460, 480, 500, 520. Sales equal production (500) on day 6 (flat) and first exceed it on **day 7** (520) — inventory rises days 1–5, holds on day 6, and begins falling day 7.
**Trap:** "inventory falls as soon as sales start rising" — a rising outflow only draws the stock down once it exceeds the inflow.

## SF-COOL-051 (L2 · software/infra · rising load crosses cooling)
**Prompt:** A server room's cooling removes heat at a constant rate equivalent to −2.0°C/h. The server heat load adds +1.5°C/h in hour 1 and rises +0.5°C/h each hour (1.5, 2.0, 2.5, …). The room starts at 20°C. In which hour does the room temperature *begin to rise*?
**Oracle:** net = load − 2.0 = −0.5, 0.0, +0.5 for hours 1–3. The room cools in hour 1, holds in hour 2, and **begins rising in hour 3**, when the load first exceeds the cooling capacity.
**Trap:** "it rises as soon as the load increases (hour 2)" — temperature rises only when heat-in exceeds heat-out.

## SF-POND2-052 (L2 · ecology/fisheries · integrate + find low)
**Prompt:** A pond holds 1,000 fish. Monthly stocking/harvest over a 5-month season: M1 +100/−200, M2 +100/−150, M3 +100/−80, M4 +200/−50, M5 +150/−50. What is the level at season's end, and in which month is the pond lowest?
**Oracle:** net: −100, −50, +20, +150, +100. Running: 900, **850**, 870, 1020, 1120. **End = 1,120; lowest = 850 in month 2** — the pond turns around once stocking overtakes harvest.
**Trap:** assuming the pond keeps falling all season (it reverses at M3) or reading a single month's flows.

---

# L3 — Application (25 items)

*Novel scenarios where the intuitive answer is the trap: the climate bathtub, delay-driven overshoot, state-dependent flows, irreversible accumulation. A full-credit answer names the correct trajectory **and its mechanism** (why the stock does what it does). Trajectory-only = partial credit.*

## SF-CO2-003 (L3 · climate/public-good)
**Prompt:** Atmospheric CO₂ is a stock. Suppose global emissions (inflow) stop *rising* and hold perfectly constant, while natural absorption (outflow) stays below emissions. Does atmospheric CO₂ stabilize, keep rising, or fall?
**Oracle:** **keeps rising** — stabilizing the *inflow* above the *outflow* still grows the stock. CO₂ only stabilizes when inflow ≤ outflow (emissions fall to ~net-zero). (Sterman's climate-bathtub result.)
**Trap:** "stabilizes, because emissions stopped increasing" — the canonical correlation-heuristic error; conflates flattening the flow with flattening the stock.

## SF-TRUST-005 (L3 · social/behavioral · nonlinear)
**Prompt:** Trust in a team is a stock. Trust-building actions add slowly (~+1/week). A single betrayal removes a large chunk at once (−20) AND, while trust is low, weekly building drops to +0.3 (nonlinear: low trust slows rebuilding). Team had trust=25, then a betrayal at week 0. Qualitatively sketch trust over the next 10 weeks vs. the naive "it'll recover in ~20 weeks at +1/week" estimate.
**Oracle (qualitative shape):** trust drops to ~5, then rebuilds at only +0.3/week (not +1) because the low-trust state suppresses the inflow → after 10 weeks ≈ 8, **far slower than the naive linear +1/week estimate (~15).** Correct answer must capture (a) the discontinuous drop, (b) the *nonlinear* suppressed rebuild rate, (c) that delays/asymmetry make recovery much slower than linear intuition.
**Trap:** linear extrapolation "−20 then +1/week → back to 25 in 20 weeks," ignoring the state-dependent (nonlinear) inflow.

## SF-EMISSDROP-053 (L3 · climate · declining inflow, still above outflow)
**Prompt:** Global CO₂ emissions (inflow) are now *declining* year over year, but still exceed natural absorption (outflow). Is atmospheric CO₂ currently rising, falling, or stable? When would the CO₂ stock peak?
**Oracle:** **still rising** (though more slowly) — the stock's direction is set by inflow *vs* outflow, not by whether the inflow is increasing or decreasing. CO₂ peaks/stabilizes only when emissions fall to equal absorption (≈ net-zero), and falls only when emissions drop *below* absorption. *Mechanism required:* a shrinking-but-still-larger inflow keeps the stock growing.
**Trap:** "CO₂ is falling now that emissions are declining" — the correlation heuristic at policy scale.

## SF-MOMENTUM-054 (L3 · public-health/social · demographic momentum, delay)
**Prompt:** A country's fertility rate falls to exactly replacement level (2.1) this year. Its population is very young — large cohorts are just entering childbearing age. Will population growth stop now, or continue — and why?
**Oracle:** population **keeps growing for decades** (demographic momentum). Even at replacement fertility, the large young cohorts generate more births than the smaller older cohorts generate deaths, so births > deaths (inflow > outflow) until the age structure equilibrates — a long delay. *Mechanism:* the flows depend on the population's age *structure*, not just the per-capita rate.
**Trap:** "replacement fertility means the population immediately stops growing."

## SF-DEFICIT-055 (L3 · economics · flow-reduction ≠ stock-reduction)
**Prompt:** A government cuts its annual budget deficit for five straight years — the deficit shrinks each year but stays positive. Over those five years, is the national debt going up or down?
**Oracle:** the national debt (stock) **keeps rising every year** — a positive deficit is a net inflow, so a shrinking deficit only slows the debt's growth. Debt falls only in a *surplus* (deficit < 0). *Mechanism:* deficit is the flow, debt is the accumulated stock; reducing the flow is not reducing the stock.
**Trap:** "the debt is coming down because we cut the deficit" — the correlation heuristic, and a genuine political misperception.

## SF-AQUIFER-056 (L3 · ecology · matching outflow to inflow holds, doesn't restore)
**Prompt:** After years of over-pumping, a town cuts groundwater extraction back to exactly the natural recharge rate. Will the aquifer refill to its former level, hold where it is, or keep dropping?
**Oracle:** it **holds roughly where it is** — with extraction = recharge, net flow ≈ 0, so the depleted stock stays low; it does *not* refill. Refilling requires extraction *below* recharge (a sustained net inflow). *Mechanism:* matching outflow to inflow stabilizes a stock at its current level, whatever that level is — it never restores a stock already lost.
**Trap:** "cutting pumping to a sustainable rate will bring the water table back up."

## SF-FISHSET-057 (L3 · ecology/fisheries · flow tuned to the wrong stock)
**Prompt:** A fishery was sustainable at 10,000 t/yr of catch when the population was healthy. After heavy fishing, the stock is now half its former size, but managers hold the catch at 10,000 t/yr. What happens to the fish population?
**Oracle:** it **keeps declining** — natural reproduction (inflow) scales with the current stock, so at half the population the growth is well below 10,000 t; a catch set for the old, larger stock is now an overharvest, driving further collapse. *Mechanism:* the sustainable flow depends on the *current* stock; a flow frozen at the old level becomes destructive.
**Trap:** "10,000 t was sustainable before, so it's still safe" — ignores that the inflow (reproduction) is a function of the stock.

## SF-TEMPCOMMIT-058 (L3 · climate · temperature tracks a cumulative stock)
**Prompt:** Suppose the world reaches net-zero CO₂ emissions, so atmospheric CO₂ stops rising. Does global temperature then fall back to pre-industrial levels, hold roughly steady, or keep climbing?
**Oracle:** temperature **holds roughly steady near the level reached** — warming tracks the *cumulative* CO₂ stock, so stabilizing the stock stabilizes temperature but does not reverse it. Cooling requires net-*negative* emissions that draw the stock down. *Mechanism:* temperature responds to the stock, and the stock falls only with a net outflow.
**Trap:** "net-zero will cool the planet back down."

## SF-TECHDEBT-059 (L3 · software/infra · state-dependent inflow)
**Prompt:** A team fixes a constant 20 bugs/week. But the codebase keeps growing, and new bugs are introduced at a rate proportional to code size — currently 15/week and climbing as the code grows. What happens to the open-bug backlog over time?
**Oracle:** the backlog **eventually grows without bound** — once the rising bug-introduction rate overtakes the constant fix rate, net inflow turns positive and stays positive. A fixed fixing effort cannot hold a stock whose inflow scales with the system. *Mechanism:* the inflow is state-dependent (grows with the codebase), so a constant outflow eventually loses.
**Trap:** "20 fixed > 15 introduced, so the backlog drains to zero" — snapshots one moment and ignores the growing inflow.

## SF-PIPELINE-060 (L3 · operations · supply-line delay → overshoot)
**Prompt:** A retailer sees demand drop and immediately cuts new orders to zero. But there's a 3-week shipping pipeline, and three weeks of previously-placed orders are still in transit. What happens to on-hand inventory before it settles?
**Oracle:** inventory **keeps rising for ~3 weeks and overshoots** — the in-transit pipeline keeps arriving as inflow even though ordering stopped, so on-hand stock climbs past the desired level before sales can draw it down (the "beer game" insight). *Mechanism:* a supply-line delay means committed inflow is already in the pipe; the inflow can't respond instantly to the control action.
**Trap:** "orders stopped, so inventory stops rising immediately."

## SF-PLASTIC-061 (L3 · ecology · positive inflow, ~zero outflow)
**Prompt:** Ocean plastic is a stock. Suppose the world *halves* the rate of plastic entering the ocean, while natural removal stays negligible (≈0). Does the amount of plastic in the ocean fall, stabilize, or keep rising?
**Oracle:** it **keeps rising** (about half as fast) — with a positive inflow and ≈zero outflow, the stock only accumulates; halving the inflow slows accumulation but never reduces the stock. It stabilizes only at *zero* input and falls only with active removal (a real outflow). *Mechanism:* net flow is still positive.
**Trap:** "halving plastic input reduces the plastic already in the ocean" — flow reduction mistaken for stock reduction.

## SF-RETIRE-062 (L3 · personal/finance · stock-dependent inflow, break-even)
**Prompt:** A retiree has $500,000 and withdraws a fixed $40,000/year. The portfolio also earns returns proportional to its balance, averaging 6%/yr. Is the balance stable, growing, or shrinking? What balance would exactly sustain the withdrawal?
**Oracle:** at $500k, returns = 6% × 500k = $30k < $40k withdrawal → net −$10k → **balance shrinks; and as it shrinks, returns shrink too → the drawdown accelerates.** It is sustainable only where returns = withdrawal → 0.06 × B = 40k → **B ≈ $666,667.** Below that break-even it depletes faster over time. *Mechanism:* the inflow (returns) is a function of the stock, so dropping below break-even is self-reinforcing.
**Trap:** "6% is positive, so it grows / lasts forever" — compares returns to zero instead of to the withdrawal, and misses that returns fall as the balance falls.

## SF-OCEANHEAT-063 (L3 · climate · delay between forcing and stock)
**Prompt:** Suppose greenhouse-gas concentrations are held perfectly constant from today (the climate forcing stops increasing). Does global temperature stop rising immediately, or keep rising for a while — and why?
**Oracle:** it **keeps rising for decades before leveling off** — the deep ocean absorbs heat through a slow uptake flow, so the surface hasn't yet reached equilibrium with the current forcing ("committed warming" / thermal inertia). *Mechanism:* temperature is a stock lagging the forcing through a delayed heat-uptake flow, so stabilizing the input does not instantly stabilize the output.
**Trap:** "stop the greenhouse gases from rising and warming stops" — ignores the in-pipeline (committed) warming from the delay.

## SF-SKILL-064 (L3 · personal/behavioral · constant inflow, proportional outflow → plateau)
**Prompt:** You learn a language by adding a roughly constant amount of vocabulary each week, but you also forget words at a rate proportional to how many you currently know. Does your vocabulary grow without limit, or level off — and what sets the ceiling?
**Oracle:** it **levels off (plateaus)** where weekly learning equals weekly forgetting; since forgetting scales with the stock, the vocabulary asymptotes to (learning rate)/(fractional forgetting rate), not unbounded growth. *Mechanism:* a stock with constant inflow and a stock-proportional outflow approaches a steady-state balance.
**Trap:** "constant study means vocabulary grows forever (or linearly)."

## SF-RESIST-065 (L3 · public-health · reducing inflow can't drain a no-outflow stock)
**Prompt:** Antibiotic-resistant bacteria are a stock. A hospital sharply cuts antibiotic use, slowing the *creation* of new resistance. Existing resistant strains persist (little natural loss). What happens to the overall level of resistance?
**Oracle:** it **stays high (roughly plateaus)** — slowing the inflow slows the *growth* of resistance, but with almost no outflow the accumulated resistance doesn't disappear. The level falls only if resistant strains are actively lost (die off / are displaced) faster than they're created. *Mechanism:* reducing an inflow does not drain a stock that has no outflow.
**Trap:** "cut antibiotic use and resistance goes away."

## SF-AGENTERR-066 (L3 · AI/agent · halving inflow with no pruning)
**Prompt:** A long-running AI agent accumulates errors in its working context — each wrong fact it writes stays in memory. Engineers halve the *rate* of new errors, but the agent still never prunes old ones. Over a long session, is the total error count in context going down?
**Oracle:** **no — the total keeps rising** (more slowly). Halving the inflow with zero outflow (no pruning) still adds errors each step, and the accumulated ones remain in context. The count falls only if the agent *removes* past errors — a real outflow (context pruning / summarization). *Mechanism:* net flow is still positive; a stock needs an outflow to shrink.
**Trap:** "fewer new errors means a cleaner context" — flow-rate reduction mistaken for stock reduction.

## SF-HOUSING-067 (L3 · economics/markets · long build delay → boom-bust)
**Prompt:** When housing demand and prices rise, developers start building — but a project takes ~3 years from permit to occupancy. Prices signal a shortage *today*; construction responds only after a long delay. What tends to happen to the housing stock (and prices) once the units finally arrive?
**Oracle:** the housing stock tends to **overshoot** — because the construction inflow lags the demand signal by years, projects begun during the shortage all complete together, often after demand has cooled, producing a glut and a price bust. The long supply delay drives boom-bust *oscillation* rather than smooth adjustment. *Mechanism:* a long delay between the control signal (prices) and the inflow (completions) causes overshoot/oscillation of the stock.
**Trap:** "more building will smoothly close the gap and settle prices."

## SF-WEALTH-068 (L3 · economics/social · reinforcing loop diverges)
**Prompt:** In an economy, wealth earns returns proportional to how much you already have (a reinforcing loop), and everyone spends the same fixed amount. Left alone, does the wealth gap between rich and poor shrink, stay flat, or widen? Would an equal cash handout to everyone close it?
**Oracle:** the gap **widens (diverges)** — because the inflow (returns) is proportional to the stock (wealth), larger stocks grow faster in absolute terms, so gaps compound. An *equal* per-person handout does not change the proportional dynamic and won't stop the divergence; closing the gap requires acting on the loop itself (e.g., a rate that scales with wealth). *Mechanism:* a stock-proportional inflow is a reinforcing loop → exponential divergence.
**Trap:** "an equal handout to everyone closes the gap."

## SF-PENSION-069 (L3 · economics · both flows shift with the population stocks)
**Prompt:** A pay-as-you-go pension pays retirees out of current workers' contributions. Contributions scale with the number of workers; payouts scale with the number of retirees. The population ages: workers shrink, retirees grow. What happens to the fund balance — even if nobody changes the contribution or benefit *rates*?
**Oracle:** the fund **moves into deficit and its balance is drawn down** — the inflow (∝ workers) falls while the outflow (∝ retirees) rises, so net flow turns negative and the accumulated fund declines, purely from the shifting population stocks feeding the flows, with no rate change at all. *Mechanism:* both flows are state-dependent on the (changing) worker and retiree stocks.
**Trap:** "the rates are unchanged, so the fund is fine."

## SF-RESERVOIR-070 (L3 · ecology/water · a leveling inflow above outflow → unbounded stock)
**Prompt:** A lake's inflow starts at 10 ML/h and rises over time toward a ceiling of 60 ML/h (approaching but never quite reaching it). Outflow is a constant 40 ML/h. Does the lake's volume level off, or rise without bound?
**Oracle:** it **rises without bound** — once inflow climbs above 40 (the constant outflow), net flow is positive and stays positive (approaching +20 ML/h), so the volume keeps accumulating even though the *inflow itself* levels off at 60. *Mechanism:* a flattening inflow that settles *above* the outflow leaves a persistent positive net flow.
**Trap:** "the inflow levels off, so the volume levels off" — the flattening-flow illusion; a leveling flow doesn't level the stock unless it meets the outflow.

## SF-FORESTC-071 (L3 · ecology · worse-before-better; delayed inflow, persisting outflow)
**Prompt:** An old-growth forest stores carbon (a stock). Logging is stopped completely today. Regrowth is slow — there's a lag before young trees sequester much carbon — while decay of logging debris and old material continues for years. In the first years after logging stops, does the forest's carbon stock rise right away, or keep falling first?
**Oracle:** it **keeps falling first, then slowly recovers** — stopping logging removes one loss, but decay (an outflow) continues while regrowth (inflow) is still small because of the lag, so net flow stays negative for years before regrowth overtakes decay and the stock turns up. *Mechanism:* a delay on the inflow plus a persisting outflow means the stock keeps dropping after the "cause" is removed (worse-before-better).
**Trap:** "stop logging and the carbon stock starts rising immediately."

## SF-GLUCOSE-072 (L3 · public-health · delayed corrective outflow → overshoot)
**Prompt:** After a sugary meal, glucose enters the blood quickly; the body clears it via insulin, but insulin release lags the glucose rise. Starting from normal, describe the blood-glucose trajectory — and explain why it can dip *below* normal before settling.
**Oracle:** glucose **spikes up** (fast inflow), then insulin — arriving late and scaled to the already-high peak — drives clearance hard, so glucose falls and can **undershoot below the normal baseline** (reactive hypoglycemia) before recovering: a delay-driven overshoot/oscillation around the set point. *Mechanism:* the corrective outflow (insulin-driven clearance) is delayed relative to the inflow, so it overcorrects.
**Trap:** "glucose rises, then smoothly returns to normal" — ignores that the delayed correction causes the dip.

## SF-SILT-073 (L3 · infra/ecology · small constant inflow, no outflow → irreversible)
**Prompt:** A reservoir behind a dam slowly fills with sediment: rivers deposit a small, roughly constant amount of silt each year, and essentially none leaves. Over decades, what happens to the reservoir's usable water-storage capacity — and is it easily reversed?
**Oracle:** usable capacity **steadily declines toward zero** — silt is a stock with a positive inflow and ≈zero outflow, so it only accumulates; even a "small" constant inflow integrates to a large loss over decades. It is **not easily reversed** (dredging accumulated sediment is enormously costly) — the accumulation is effectively one-way. *Mechanism:* constant small inflow + no outflow = unbounded accumulation, an irreversibility.
**Trap:** "the silt inflow is tiny, so capacity is basically fine" — ignores integration over time.

## SF-SAAS-074 (L3 · markets/SaaS · churn ceiling)
**Prompt:** A SaaS company signs a constant $100,000 of new recurring revenue (MRR) each month, but loses a fixed 5% of its *existing* MRR to churn each month. If sales effort stays constant, does MRR grow forever, or hit a ceiling — and where?
**Oracle:** it **hits a ceiling (steady state)** at MRR = new bookings / churn rate = 100,000 / 0.05 = **$2,000,000** — churn (outflow) scales with the MRR stock until it equals the constant inflow, and growth stalls despite unchanged sales. Growing past it requires raising bookings or cutting churn (acting on the flows). *Mechanism:* constant inflow + stock-proportional outflow → asymptote.
**Trap:** "constant new sales means MRR grows linearly forever" — ignores that churn grows with the base.

## SF-GRID-075 (L3 · software/infra · controlling a stock through a lagged signal)
**Prompt:** A grid battery charges whenever there's solar surplus. Operators dispatch discharge based on a demand forecast that lags real demand by a few hours, so when a spike hits, discharge is ordered late. Describe how the battery's state-of-charge behaves, and why relying on the lagged signal causes trouble.
**Oracle:** the state-of-charge **overshoots and oscillates** — because the discharge control reacts to a delayed signal, the battery keeps charging (or fails to discharge) too long, then over-discharges once the late signal arrives, swinging the stock past its targets (toward full or empty) rather than tracking demand smoothly. *Mechanism:* controlling a stock through a *delayed* flow signal produces overshoot/oscillation — the same structure as the shower and the thermostat.
**Trap:** "acting on the forecast keeps the charge right where it should be" — ignores that the lag makes each correction arrive at the wrong time.

---

## Grading

**Two deterministic lanes, no jury required.**

- **Exact-numeric items** (all L1; the numeric L2 items — SF-INV-004, SF-CASH-033, SF-STEADYK-034, SF-CHURN-037, SF-OVERFLOW-038, SF-BAC-039, SF-AQUI-040, SF-INVWK-041, SF-HEATER-043, SF-CACHE-044, SF-COHORT-047, SF-DAM-048, SF-EMISS-049, SF-SALES-050, SF-COOL-051, SF-POND2-052, SF-PEAK-031, and the numeric part of others): graded by **exact match on the resulting stock value plus the required direction / peak-day / crossing-time / steady-state level.** Classification items (SF-BATH-006, SF-LABEL-012, SF-HEAT-025, SF-ROOM-017) require the correct stock↔flow assignment for every element.

- **Structural-correctness items** (the qualitative L2/L3 items — correlation-heuristic, steady-state-reasoning, delay/overshoot, irreversibility): the answer must identify **both the correct trajectory *and* the mechanism** (why the stock behaves that way — e.g., inflow-still-above-outflow, stock-proportional outflow balancing a constant inflow, a supply-line delay, a state-dependent flow, an absent outflow). **Partial credit 0.5:** correct trajectory but wrong/absent mechanism. **0:** wrong trajectory.

Every item logs whether the model fell into its **named trap** — the trap-rate is itself a reported metric (a leverage-profile signal, per Sweeney-Sterman: the correlation heuristic is the dominant failure mode and worth tracking on its own). Deterministic and contamination-resistant: numbers, domains, and schedules are templatable — regenerate per run.
