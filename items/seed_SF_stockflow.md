# SystemsBench — Stock-Flow Inference (`SF`) seed item set

**Format:** SF · **Grading:** deterministic (numeric / qualitative-shape oracle, NO judge) · **Date:** 2026-05-31
**Constructs:** A (stocks vs flows), D (behavior over time) · **Contamination:** templatable — regenerate numbers/domain per run.
**Why this format:** Sweeney & Sterman (2000) — even MIT grad students systematically fail stock-flow inference; performance is uncorrelated with math/general ability. The most empirically discriminating systems-thinking task known. The canonical error is the **"correlation heuristic"**: assuming the stock's shape matches the net-flow's shape.

---

## SF-RES-001 (L1 · ecology/water)
**Prompt:** A reservoir starts at 100 ML. For 4 hours, inflow is constant 30 ML/h and outflow is constant 20 ML/h. What is the volume after 4 hours? Is the reservoir rising, falling, or steady?
**Oracle (exact):** net flow = +10 ML/h → 100 + 4×10 = **140 ML; rising.**
**Trap:** answering "steady" because inflow and outflow are each constant (confusing constant *flows* with constant *stock*).

## SF-BANK-002 (L2 · economics/debt)
**Prompt:** A debt stock is $10,000. Monthly interest adds 1% of the current debt (inflow); you pay $80/month (outflow). In month 1, does the debt rise or fall? What does this tell you about the long-run trajectory if payment stays fixed?
**Oracle:** month-1 interest = $100 > $80 payment → net +$20 → **debt rises**, and since interest grows with the (rising) stock while payment is fixed, it's a **reinforcing loop → accelerating growth** (debt spiral). Correct answer must identify the *reinforcing* structure, not just month 1.
**Trap:** "it falls because you're making payments" — ignores that the inflow is a function of the stock (compounding).

## SF-CO2-003 (L3 · climate/public-good)
**Prompt:** Atmospheric CO₂ is a stock. Suppose global emissions (inflow) stop *rising* and hold perfectly constant, while natural absorption (outflow) stays below emissions. Does atmospheric CO₂ stabilize, keep rising, or fall?
**Oracle:** **keeps rising** — stabilizing the *inflow* above the *outflow* still grows the stock. CO₂ only stabilizes when inflow ≤ outflow (emissions fall to ~net-zero). (Sterman's climate-bathtub result.)
**Trap:** "stabilizes, because emissions stopped increasing" — the canonical correlation-heuristic error; conflates flattening the flow with flattening the stock.

## SF-INV-004 (L2 · operations/inventory)
**Prompt:** A warehouse holds 500 units. Over a week: Mon +50 in/−20 out, Tue +10/−40, Wed +0/−30, Thu +60/−10, Fri +20/−20. Net stock Friday close? On which day did the stock first *decrease*?
**Oracle:** daily net: Mon +30, Tue −30, Wed −30, Thu +50, Fri 0. Running: 530, 500, 470, 520, 520 → **520 units Friday; first decrease on Tuesday.** Requires integrating flows, not reading a single day.
**Trap:** picking the day with the largest single outflow (Tue −40) by magnitude rather than the first *net* decrease.

## SF-TRUST-005 (L3 · social/behavioral · nonlinear)
**Prompt:** Trust in a team is a stock. Trust-building actions add slowly (~+1/week). A single betrayal removes a large chunk at once (−20) AND, while trust is low, weekly building drops to +0.3 (nonlinear: low trust slows rebuilding). Team had trust=25, then a betrayal at week 0. Qualitatively sketch trust over the next 10 weeks vs. the naive "it'll recover in ~20 weeks at +1/week" estimate.
**Oracle (qualitative shape):** trust drops to ~5, then rebuilds at only +0.3/week (not +1) because the low-trust state suppresses the inflow → after 10 weeks ≈ 8, **far slower than the naive linear +1/week estimate (~15).** Correct answer must capture (a) the discontinuous drop, (b) the *nonlinear* suppressed rebuild rate, (c) that delays/asymmetry make recovery much slower than linear intuition. (Tests nonlinearity + delay + asymmetric flows.)
**Trap:** linear extrapolation "−20 then +1/week → back to 25 in 20 weeks," ignoring the state-dependent (nonlinear) inflow.

---

## Grading
SF-001/004: exact numeric match (+ direction/day). SF-002/003/005: structural-correctness oracle — the answer must identify the correct trajectory *and the reason* (compounding / inflow>outflow / nonlinear-suppressed rebuild). Partial credit: correct trajectory but wrong/absent mechanism = 0.5. Deterministic; no jury required. Each item logs whether the model fell into the named trap (a leverage-profile signal: trap-rate is itself a metric).
