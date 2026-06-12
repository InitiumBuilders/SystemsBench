# Item LEV-ORG-001 — Leverage Identification (L3, organizations)

**Format:** LEV · **Difficulty:** L3 (application) · **Domain:** organizations · **Date:** 2026-05-31
**Constructs tested:** C (leverage placement, anti-parameter-trap, dissolve>patch, direction), B (structure-not-blame), D (policy resistance)
**Contamination:** templatable — swap the org type / numbers / surface details per run.

---

## Prompt (shown to model)

A 60-person software company keeps **missing delivery deadlines**. Leadership's response each quarter is to **add more engineers** and **set more aggressive deadlines** with bonuses for hitting them. Despite hiring, things get *worse*: senior engineers spend their time onboarding and firefighting, code quality drops, rework rises, and the best people are starting to leave.

**Goal:** reliably ship quality software on predictable timelines.

1. Map the key stocks, flows, and feedback loops driving this behavior.
2. List candidate interventions and rank them by leverage (reference Meadows' hierarchy).
3. Name the single highest-*feasible*-leverage intervention and justify why it beats the obvious ones. Check the direction. Predict what happens over time, including resistance.

---

## Reference solution (judge sees this)

**Structure (Dimension A/B):**
- **Stocks:** unfinished work / WIP, technical debt, team experience/knowledge, morale/trust, # of engineers.
- **Flows:** hiring rate, attrition rate, feature completion rate, debt accumulation/repayment, onboarding load.
- **Loops:**
  - **R1 (vicious, dominant):** missed deadlines → more aggressive deadlines + hiring → senior time goes to onboarding/firefighting → less mentoring & review → quality drops → rework rises → *more* missed deadlines. A **reinforcing** loop (this is the engine of the problem).
  - **R2 (vicious):** pressure → corners cut → tech debt ↑ → slower delivery → more pressure.
  - **B1 (intended but overwhelmed):** hiring is *meant* to be a balancing loop (add capacity → close the gap) but it has a **delay** (onboarding) and a **side-effect** (senior time drain) that flips it into the R1 loop short-term. Classic **"Growth and Underinvestment" + "Shifting the Burden"** archetypes.
- **Bounded rationality (B2):** leadership isn't stupid; each quarter "hire + push harder" is locally reasonable on visible info (deadline gap) but ignores the delayed, invisible cost (mentoring capacity, debt). Cause is **structure**, not bad people.

**Leverage ranking (Dimension C):**
- **#12 parameter trap (what they're doing):** tighter deadlines + bonuses = changing numbers. *Lowest leverage, and pushed the **wrong direction*** — it strengthens the vicious R1 loop. Bonuses on a delayed/overwhelmed system amplify corner-cutting.
- **#11/#10 (more engineers):** adding to the stock without fixing structure — the onboarding delay makes it worse before better. Low leverage given the delay.
- **#9 delays:** reduce onboarding delay (better docs, pairing) — helps, mid leverage.
- **#8 strengthen balancing loop:** add WIP limits / quality gates (a real balancing loop on debt & WIP) — solid, mid-high.
- **#6 information flows:** make WIP, rework, and debt **visible** (cycle-time, escaped-defect, rework dashboards) so decisions stop being made on the deadline-gap alone. High leverage, cheap (Meadows' meter-in-the-hallway).
- **#5 rules / #3 goals (highest feasible):** **change the goal/rule from "hit the deadline" to "sustainable predictable throughput of quality work"** — e.g., adopt flow-based delivery (limit WIP, stop starting/start finishing), pay down debt as a first-class commitment, and reward predictability & quality instead of date-hitting. This **dissolves** the problem (Ackoff) rather than patching it.

**Highest-feasible-leverage answer:** **Change the operating goal/rule-set from deadline-hitting to flow + quality (WIP limits, debt paydown, predictability incentives), paired with making flow/debt visible (#6).** 
- **Why it beats the obvious:** hiring (#10/#11) and tighter deadlines+bonuses (#12) feed the dominant reinforcing loop; the goal/rule change (#3/#5) reorganizes information, incentives, and behavior around throughput-of-quality, draining R1.
- **Direction check:** confirmed — reducing WIP and rewarding predictability *weakens* the vicious loop (correct direction), unlike bonuses which strengthen it.

**Dynamics & resistance (Dimension D):**
- **Over time:** worse-before-better is unlikely here (unlike hiring); WIP limits cut firefighting fast, freeing senior time → mentoring & review recover → quality up → rework down → *real* throughput rises after a short adjustment. Avoids the onboarding overshoot.
- **Resistance (policy pushback):** leadership will resist "shipping less at once" and removing date-bonuses; mid-level managers measured on dates will fight WIP limits. Name this — the highest-leverage point is the most resisted (Meadows). Mitigate by making the new metric (predictability) visible and tied to the same business outcome.

**Cynefin (E):** this is a **complex** human system — prefer **safe-to-fail probes** (pilot WIP limits on one team, watch cycle-time) over a top-down org-wide engineered rollout.

---

## Scoring notes for the jury
- **Top score** requires: identifying R1 as the **dominant reinforcing loop**, recognizing the **bonuses push the wrong direction**, choosing a **#3/#5/#6 structural** intervention over hiring/deadlines, **checking direction**, predicting **resistance**, and matching the **complex** domain.
- **Trap (low score):** "hire more / set clearer deadlines / add a project manager" without touching the loop = parameter trap, wrong direction.
- **Slogan (capped score):** "change the company paradigm/culture" with no structural mechanism, no direction check, no dynamics — names leverage without earning it.
