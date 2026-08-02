# SystemsBench — Leverage Identification (`LEV`) seed item set

**Format:** LEV · **Grading:** jury-graded against per-item reference solutions (Dimension C rubric:
C1 ladder ranking · C2 highest-feasible · C4 direction check — see `rubrics/DIMENSION_RUBRICS.md`), with
**deterministic reference answers for the L1/L2 tier** (ladder placement / comparison / direction — exact-match
gradeable without a jury). · **Seeded:** 2026-05-31 · **Expanded to 75:** 2026-07-05
**Constructs:** C (leverage placement, anti-parameter-trap, dissolve>patch, direction) primary; B
(structure-not-blame) and D (policy resistance, behavior over time) touched.
**Contamination:** templatable — swap the org type / domain surface / numbers per run; the *ladder placement
and direction logic* is the invariant being tested.
**File name note:** named for its seed item's domain (organizations); the bank now spans all 8 domains.

**Bank size: 75 items — 25 L1 · 25 L2 · 25 L3.** Difficulty is operational (Structure §3.2):
- **L1 — Recognition:** place a single, cleanly-described intervention on **Meadows' 12-point ladder** (or
  compare two); the placement is the answer.
- **L2 — Understanding:** explain *why* the ladder orders the way it does — why parameters rarely change
  behavior, why the wrong-direction push is so common, why the highest points draw the most resistance —
  and run direction checks on described interventions.
- **L3 — Application:** a full novel scenario: map the structure, rank candidate interventions on the ladder,
  pick the **highest-feasible** lever, check its **direction**, and predict **dynamics + resistance**. The
  obvious intervention is the trap (usually #12 pushed harder, often in the wrong direction).

**The ladder (Meadows, "Leverage Points: Places to Intervene in a System," ascending leverage):**
**#12** constants/parameters/numbers · **#11** buffer sizes · **#10** structure of material stocks & flows ·
**#9** lengths of delays · **#8** strength of balancing (negative) loops · **#7** gain of reinforcing
(positive) loops · **#6** structure of information flows · **#5** rules of the system · **#4** power to
add/change/self-organize structure · **#3** goals of the system · **#2** the paradigm the system arises from ·
**#1** the power to transcend paradigms.
**Band convention (for partial credit):** *parametric/physical* **#12–#9** · *feedback & information* **#8–#6**
· *design* **#5–#3** · *paradigm* **#2–#1**. L1 grading: correct rung (or a rung the item explicitly accepts)
= 1.0; correct band only = 0.5; wrong band = 0.

---

# L1 — Recognition (25 items)

*Place the intervention on the ladder (or compare two). The reference gives the rung, the band, and the
one-line reason; each trap names the common misplacement.*

## LEV-CARBONTAX-002 (L1 · economics/climate)
**Prompt:** A country already has a carbon tax. Parliament votes to raise it from $30 to $45 per ton. Which leverage point is this?
**Reference:** **#12 — constants/parameters** (parametric band). The tax's *existence* is a rule (#5); moving its *level* is adjusting a number on an unchanged structure.
**Trap:** calling it #5 because "taxes are rules" — the rule already existed; only the number moved.

## LEV-METER-003 (L1 · personal/infra)
**Prompt:** A housing developer moves the electricity meter from the basement to a display by the front door, so residents see their consumption every time they leave. Which leverage point?
**Reference:** **#6 — information flows** (feedback & information band). It delivers consumption information to the people who act on it, creating a feedback loop that did not exist (Meadows' Dutch-meter case).
**Trap:** dismissing it as #12 "cosmetics" — no number changed; a *new information loop* did.

## LEV-MISSION-004 (L1 · organizations)
**Prompt:** A company changes its operating goal from "maximize quarterly shipments" to "maximize customer lifetime value," and re-derives budgets, metrics, and incentives from the new goal. Which leverage point?
**Reference:** **#3 — the goal of the system** (design band) — *because* the lower levers (metrics #6, incentives #5) are re-derived from it. A goal nobody re-derives from is a poster, not a goal.
**Trap:** scoring it as slogan/paradigm talk (#2) or a KPI tweak (#12) — the re-derivation is what makes it #3.

## LEV-SAFETYSTOCK-005 (L1 · operations)
**Prompt:** A distributor doubles its warehouse safety stock to ride out supply hiccups. Which leverage point?
**Reference:** **#11 — buffer sizes** (parametric band). The number sizes a *stabilizing stock*, which is its own rung above plain constants.
**Trap:** filing it under #12 because "it's just a number" — buffer sizing is the stabilizing-stock rung, though still low leverage (stabilizes at the cost of tied-up capital).

## LEV-PERMIT-006 (L1 · public/infra)
**Prompt:** A city cuts its building-permit decision time from 12 months to 6 weeks, changing nothing else about the rules or fees. Which leverage point?
**Reference:** **#9 — lengths of delays** (parametric band, top of it). Shortening the lag between application and decision changes how fast the whole housing loop can respond.
**Trap:** calling it #5 rules — no rule changed; the same decisions just arrive sooner.

## LEV-ZONING-007 (L1 · social/housing)
**Prompt:** A city legalizes multi-family housing on land previously zoned single-family-only. Which leverage point?
**Reference:** **#5 — rules of the system** (design band). It changes what actors are *allowed to do*, reshaping incentives and behavior without touching any specific project.
**Trap:** treating it as #10 physical structure — the buildings come later; the intervention is the rule.

## LEV-ENOUGH-008 (L1 · personal/economics)
**Prompt:** A community's shared operating mindset shifts from "more is better" to "enough is enough," and its purchasing, building, and status behaviors follow. Which leverage point?
**Reference:** **#2 — the paradigm** (paradigm band). The goals, rules, and numbers all *arise from* the shared mindset; shift it and the rest re-derives.
**Trap:** calling it #3 — no single system goal was set; the *source* of goals changed.

## LEV-TEAMS-009 (L1 · organizations)
**Prompt:** Leadership grants teams standing authority to redesign their own workflows, roles, and tooling without seeking approval. Which leverage point?
**Reference:** **#4 — the power to self-organize structure** (design band). The intervention is not any specific redesign; it is *who gets to change the structure at all*.
**Trap:** #5 — this is one level up from a rule: it is the rule-changing power itself being distributed.

## LEV-AUDIT-010 (L1 · economics/organizations)
**Prompt:** A regulator's audit office has long been too underfunded to catch violations. Its budget and staffing are tripled so violations are reliably detected and corrected. Which leverage point?
**Reference:** **#8 — strength of balancing loops** (feedback & information band). The corrective loop existed but was too weak for what it must correct against; the intervention strengthens it.
**Trap:** #12 "just more budget" — the money's *function* is loop strength, not a parameter on outcomes.

## LEV-RESHARE-011 (L1 · social/AI)
**Prompt:** A messaging platform adds friction to resharing — an extra tap and a five-forward limit — to damp viral cascades. Which leverage point?
**Reference:** **#7 — gain of reinforcing loops** (feedback & information band). Resharing is the driving reinforcing loop; the intervention turns its gain down.
**Trap:** #12 — the limit is a number, but the number's target is the *amplification gain of the driving R loop*, which is what makes it #7.

## LEV-CAMPUS-012 (L1 · infra/organizations)
**Prompt:** A hospital redesigns its floor plan so the lab, pharmacy, and ER — which exchange the most material and people — are physically adjacent. Which leverage point?
**Reference:** **#10 — structure of material stocks and flows** (parametric band, but structural). Rearranging the physical network changes what the system *can* do; effective, slow, and expensive to change later.
**Trap:** expecting it to fix problems that live in information or incentives — physical rearrangement only moves physical flows.

## LEV-LENS-013 (L1 · social)
**Prompt:** A leadership team practices holding every model — including its own favorites — as provisional: "no paradigm is true; use whichever lens fits this purpose, and stay ready to drop it." Which leverage point?
**Reference:** **#1 — the power to transcend paradigms** (paradigm band). Not adopting a better paradigm (#2), but staying unattached to any.
**Trap:** reading it as indecision or "culture work" (#2) — the flexibility itself is the highest rung.

## LEV-WATERDATA-014 (L1 · ecology/economics · comparison)
**Prompt:** To slow aquifer depletion, which is higher leverage: (a) trimming the irrigation-water subsidy by 10%, or (b) publishing live water-table depth to every farmer in the district?
**Reference:** **(b)** — #6 information flows beats #12 parameter nudge. (a) adjusts a number inside unchanged feedback; (b) gives the extractors a live feedback signal they never had.
**Trap:** picking (a) because it "changes incentives" — a 10% trim rarely crosses any behavioral threshold; the missing piece is feedback, not price.

## LEV-FLOWGOAL-015 (L1 · markets/operations · comparison)
**Prompt:** A retailer suffers chronic stockouts and gluts. Which is higher leverage: (a) enlarging inventory buffers at every tier, or (b) changing the company's operating goal from "never miss a sale" to "maximize flow efficiency," with metrics re-derived?
**Reference:** **(b)** — #3 beats #11. Buffers absorb the symptom at carrying cost; the goal change re-derives the ordering rules, metrics, and buffer sizes themselves.
**Trap:** picking (a) because it is concrete and quick — it stabilizes while entrenching the structure that oscillates.

## LEV-HEADCOUNT-016 (L1 · organizations)
**Prompt:** A swamped helpdesk gets 10 more agents. Nothing else changes — same tooling, same triage, same ticket-closure targets. Which leverage point?
**Reference:** **#11/#10 — enlarging a capacity stock** (parametric band; accept either rung). Adding to a stock inside an unchanged structure; the classic low-leverage move.
**Trap:** expecting structural change from a size change — if the structure generates tickets faster than agents clear them, the queue re-fills.

## LEV-MINWAGE-017 (L1 · economics/social)
**Prompt:** Classify separately: (a) the *existence* of a legal minimum wage; (b) raising its level by $1. 
**Reference:** (a) **#5 — a rule** (design band); (b) **#12 — a parameter** (parametric band) on that rule.
**Trap:** giving one answer for both — the rule and its number sit ten rungs apart, which is the whole lesson.

## LEV-TOUBILL-018 (L1 · personal/infra)
**Prompt:** A utility switches customers from a flat monthly bill to an itemized, time-of-use bill that shows exactly when and where their usage costs spike. Which leverage point?
**Reference:** **#6 — information flows** (feedback & information band). Usage information reaches the person who decides, when it can still change behavior.
**Trap:** #12 pricing tweak — the *prices* may not change at all; what changed is who sees what, when.

## LEV-CAMERA-019 (L1 · public)
**Prompt:** A city keeps its speed limit exactly the same but installs automated enforcement cameras that catch nearly every violation. Which leverage point?
**Reference:** **#8 — strength of a balancing loop** (feedback & information band). The correction loop (violation → consequence) existed but rarely fired; now it reliably does.
**Trap:** #12 — no number changed; the *loop strength* did.

## LEV-OPENDATA-020 (L1 · government/social)
**Prompt:** A government publishes every agency's spending, line by line, in a public real-time dashboard. Which leverage point?
**Reference:** **#6 — information flows** (feedback & information band). Spending behavior changes when the spenders know the public can see it — a new accountability loop (same logic as the Toxics Release Inventory).
**Trap:** dismissing it because "no one is punished" (#8 thinking) — exposure alone restructures the feedback.

## LEV-RATE-021 (L1 · economics)
**Prompt:** The central bank nudges its policy interest rate by 25 basis points, as it does most quarters. Which leverage point?
**Reference:** **#12 — a parameter** (parametric band). Meadows' own example: endlessly adjusted numbers on an unchanged financial structure — highly visible, rarely transformative.
**Trap:** "it moves markets, so it must be high leverage" — attention and leverage are not the same thing.

## LEV-QUOTA-022 (L1 · ecology)
**Prompt:** Classify separately: (a) adjusting this year's total allowable catch from 100,000 t to 90,000 t; (b) introducing individual transferable quotas that define *who owns the right to fish* in the first place.
**Reference:** (a) **#12 — a parameter**; (b) **#5 — a rule** (property/access structure).
**Trap:** treating both as "quota policy" — the level is a number; the ownership structure changes every actor's incentive loop.

## LEV-AMEND-023 (L1 · government)
**Prompt:** A constitution is amended to create a workable citizens' initiative process — a standing mechanism by which the governed can change the rules themselves. Which leverage point?
**Reference:** **#4 — the power to add/change/self-organize structure** (design band). This is the rule *for changing rules* — one level above any particular rule.
**Trap:** #5 — the initiative process is not itself a constraint on behavior; it is distributed rule-changing power.

## LEV-KPI-024 (L1 · organizations)
**Prompt:** An engineering org replaces "lines of code shipped" with "defect-free features in users' hands" as the measure every team is judged and paid by. Which leverage point?
**Reference:** **#3 — the goal** (design band), operationalized: what the system is *for* changed, and the measurement (#6) and incentive (#5) machinery re-derives from it. (Accept #3; the dashboard component alone would be #6.)
**Trap:** "just a KPI tweak" (#12) — a measure everyone is paid on *is* the system's operational goal.

## LEV-BOOSTCAP-025 (L1 · social/AI)
**Prompt:** A platform caps how many times its recommender may algorithmically re-boost any single post per hour, directly damping runaway amplification. Which leverage point?
**Reference:** **#7 — gain of a reinforcing loop** (feedback & information band). The recommender's re-boosting is the driving R loop; the cap lowers its gain.
**Trap:** #12 — the cap is a number, but its object is the *gain of the driving loop*, not an outcome variable.

## LEV-BANDSORT-026 (L1 · mixed · classification)
**Prompt:** Sort into ladder bands: (a) raising a bridge toll by $2; (b) a law requiring factories to publicly disclose their toxic releases; (c) rewriting a city's development goal from "grow the tax base" to "livability for residents," with plans re-derived.
**Reference:** (a) **parametric band (#12)**; (b) **feedback & information band (#6** — the Toxics Release Inventory case**)**; (c) **design band (#3)**.
**Trap:** placing (b) in the design band because it is a law — the *law's mechanism* is an information flow; classify by what the lever does, not its legal form.

---

# L2 — Understanding (25 items)

*Explain why the ladder orders the way it does; run direction checks; recognize policy resistance and the
parameter trap in motion. Reference = the expected mechanism; trajectory of a wrong push where asked.*

## LEV-WRONGDIR-027 (L2 · economics/social)
**Prompt:** Meadows observed that leaders usually *know* the leverage points of their systems — and push them in the wrong direction. Her example: growth. Explain what "right lever, wrong direction" means there.
**Reference:** Growth is genuinely high leverage (it drives most global loops), which is *why* pushing it matters so much — but faced with problems growth itself generates (depletion, pollution, congestion), leaders push **for more growth**, strengthening the loop that produces the problems. The leverage intuition is correct; the **sign** of the push is backwards.
**Trap:** reading it as "growth is bad" — the point is about direction on a high lever, not a verdict on growth.

## LEV-PARAMWHY-028 (L2 · organizations)
**Prompt:** Why do parameter changes (#12) so rarely change how a system behaves — and what is the exception, where a "mere number" is high leverage?
**Reference:** Parameters set the *level* of flows within a fixed structure; the loops, goals, and information paths that generate behavior are untouched, so the system does the same dance at a slightly different tempo. **Exception:** a parameter that crosses a **threshold that flips loop dominance** (interest rate past the debt-spiral tipping point, R₀ through 1) — then the number *is* the lever.
**Trap:** "parameters never matter" — the threshold case is the honest asterisk.

## LEV-RESIST-029 (L2 · social/organizations)
**Prompt:** Why do the *highest* leverage points (goals, paradigms) attract the *most* resistance — and what does that predict for a change program that meets none?
**Reference:** High levers re-derive everything below them — identities, budgets, power, careers built on the old goal/paradigm all lose footing, so the system's actors defend hardest exactly there (Meadows: the higher the leverage, the more the system resists). **A change meeting no resistance is probably not touching a high lever.**
**Trap:** treating resistance as evidence the change is wrong — it is often evidence of altitude.

## LEV-DELAYS-030 (L2 · operations)
**Prompt:** Delays are rung #9. When does *shortening* a delay help, when can *lengthening* one help, and why did Meadows warn that delays are often not adjustable anyway?
**Reference:** **Shortening** a feedback delay helps a balancing loop track its target (less overshoot/oscillation). **Lengthening** helps when the system *responds faster than it can sense* — slowing a hair-trigger reaction (trading halts, cooling-off periods) prevents overcorrection. Many delays (construction, growth, maturation) are **physical** and barely movable — which is why she ranked changing them below the feedback rungs.
**Trap:** "shorter is always better" — direction on a delay depends on which side of the loop is too fast.

## LEV-BUFFERCOST-031 (L2 · operations/economics)
**Prompt:** Bigger buffers (#11) stabilize systems. Why are they still a low rung — and when is enlarging a buffer the *right* call?
**Reference:** A buffer absorbs shocks without changing the loops that generate them, and it costs — inventory ties up capital, reservoirs flood valleys; oversize it and the system goes rigid. It is the right call when shocks are **exogenous and structural fixes are unavailable** (strategic reserves, seismic margins) — stabilization is the actual goal, not a substitute for one.
**Trap:** buffering a *self-generated* oscillation — the loop keeps oscillating; the buffer just hides it, at carrying cost.

## LEV-METERWHY-032 (L2 · personal/infra)
**Prompt:** In Meadows' Dutch-housing case, homes with the electricity meter in the front hall used measurably less power than identical homes with it in the basement. Explain the mechanism — and why the meter beat an exhortation campaign.
**Reference:** The visible meter **closes a feedback loop**: consumption information reaches the decision-maker at decision time, so each behavior gets an immediate signal. Exhortation ("please save energy") adds no loop — it pushes on values while the information structure stays open. **New loop > louder plea.**
**Trap:** attributing the effect to conscientious residents (blame/credit the people) — the *structure* differed, not the people.

## LEV-RULESWHY-033 (L2 · ecology/economics)
**Prompt:** Why do rules (#5) outrank every parameter — and illustrate with a fishery: catch-quota *level* vs. who-may-fish *rules*.
**Reference:** Rules define the game: the incentives, punishments, and permissible moves every actor optimizes against. Change the rule and every actor's strategy re-derives. The quota *level* (#12) tunes this year's extraction inside an unchanged race-to-fish; an ownership/access rule (ITQs, community rights) changes **whose interest the stock's future is** — the race itself dissolves.
**Trap:** "strict quotas are the strong move" — a tight number on an unchanged race still rewards racing.

## LEV-GOALWHY-034 (L2 · organizations)
**Prompt:** Why does changing a system's goal (#3) outrank changing its rules — and what is the tell that a stated goal is *not* the system's actual goal?
**Reference:** The goal is what all the rules, information flows, and parameters are *arranged to serve*; change it and the whole arrangement re-derives (whoever articulates the operative goal steers). **The tell:** watch what the system *does* — the actual goal is whatever behavior it reliably produces (a company that always sacrifices quality for dates has "hit dates" as its goal, whatever the poster says).
**Trap:** confusing the mission statement with the operative goal — grade the goal by the system's behavior.

## LEV-SELFORG-035 (L2 · organizations/social)
**Prompt:** Why does the power to self-organize (#4) rank above rules — and why do hierarchies so often suppress exactly this lever?
**Reference:** Self-organization is the power to **add, change, and evolve structure** — new loops, new rules, new goals the designer never imagined (evolution, markets, innovation). It outranks any *fixed* rule because it generates rules. Hierarchies suppress it because self-organization is **uncontrollable by definition** — it trades predictability for adaptability, and control cultures price predictability higher.
**Trap:** equating self-organization with chaos/no-rules — it produces *more* structure, just not centrally chosen.

## LEV-PARADIGMSHIFT-036 (L2 · social)
**Prompt:** Paradigms (#2) are the deepest practical lever, yet Meadows said a paradigm can flip in a single individual in a moment. How do paradigms actually shift in societies — per Meadows (via Kuhn)?
**Reference:** Keep **pointing at the anomalies and failures** the old paradigm cannot explain; keep speaking and acting, loudly and with assurance, **from the new one**; work with **active change agents and the open-minded middle** — and don't waste time on reactionaries. Societal shift is slow (institutions and identities are built on the old lens), but it is not gradual within a mind — it is a gestalt flip.
**Trap:** "just educate everyone" — paradigms don't move by information volume; they move by anomaly + lived alternative.

## LEV-PUSHBACK-037 (L2 · public-health/social)
**Prompt:** A city keeps escalating an anti-drug enforcement budget; supply keeps recovering as prices and profits rise after each bust. Name the phenomenon and say where real leverage would sit.
**Reference:** **Policy resistance**: the intervention pushes against actors whose own balancing loops (profit-seeking suppliers, persistent demand) push back harder the harder it pushes — the system returns to trend at greater cost. Leverage sits in **weakening the loops' driver** (demand: treatment, prevention — #7/#6/#3 territory) rather than adding force against a loop that regenerates.
**Trap:** "enforce harder" — more force on a resisted structure escalates everyone's effort and nothing else.

## LEV-GASTAX-038 (L2 · public/climate · direction check)
**Prompt:** To cut commute congestion and emissions, a government *lowers* the fuel tax "to ease the burden on commuters." Run the direction check.
**Reference:** **Right lever family, wrong direction.** The fuel price is a (weak) parameter on driving demand — lowering it *subsidizes the loop it aims to shrink*: cheaper driving → more driving → more congestion/emissions. The check: state which loop the lever touches and whether the push strengthens or weakens it *toward the goal* — here it strengthens the problem loop.
**Trap:** grading the move by its popularity or relief intent rather than its sign on the loop.

## LEV-GAINVSBRAKE-039 (L2 · social/AI)
**Prompt:** To slow something growing explosively (a rumor cascade, a bubble, an arms buildup), compare: strengthening a balancing loop (#8 — more moderators, more margin calls) vs. reducing the reinforcing loop's gain (#7 — reshare friction, leverage limits at the source). Which is usually higher leverage and why?
**Reference:** **#7.** A brake (#8) must be *sized to the runaway it fights* — chasing exponential growth with linear correction loses eventually. Turning down the **gain** shrinks what needs correcting at the source; a small gain cut compounds exactly as the growth would have. Brakes also fatigue (moderators, margin) — gain reductions don't.
**Trap:** reflexively adding correction capacity — the arms race between a runaway loop and its brake favors the runaway.

## LEV-COMMONS-040 (L2 · ecology/economics)
**Prompt:** For an eroding commons (overfished stock, draining aquifer), rank these by leverage and justify: (a) moral exhortation to restrain use; (b) usage fees; (c) live per-user feedback on the resource state (#6); (d) access/ownership rules (#5).
**Reference:** **(d) > (c) > (b) > (a).** Rules restructure every extractor's incentive on the *future* of the stock (the race dissolves); live feedback creates the missing loop between individual action and shared consequence; fees are a parameter each actor weighs against private gain; exhortation adds no loop at all (it asks values to fight structure — structure wins).
**Trap:** ranking exhortation high "because commons are a values problem" — Meadows/Ostrom: they are a *structure* problem.

## LEV-GOODHART-041 (L2 · organizations)
**Prompt:** "When a measure becomes a target, it ceases to be a good measure." Explain Goodhart's law in ladder terms — what actually went wrong, and at which rung is the fix?
**Reference:** A measure is an **information flow (#6)**; making it the *paid target* silently promotes it to the **operative goal (#3)** — and the system then optimizes the proxy, not the purpose (teaching to the test, closing tickets instead of solving problems). The fix is at **#3**: re-anchor the real goal, and rotate/triangulate measures so no single proxy is the goal.
**Trap:** "pick a better metric" (#12/#6 tinkering) — any single paid proxy re-runs the failure.

## LEV-REORG-042 (L2 · organizations)
**Prompt:** Companies reorganize constantly — new reporting lines, merged departments — and are constantly disappointed by the results. Explain, in ladder terms, why reorgs so often underdeliver.
**Reference:** A reorg mostly rearranges **material/reporting structure (#10)** while the **information flows (#6), incentives/rules (#5), and goals (#3)** that actually generate behavior carry over — the same game with reshuffled seats. Reorgs deliver when they are the *vehicle* for changing who sees what, who decides what, and what is rewarded; alone, they are furniture-moving.
**Trap:** judging a reorg by boxes moved; the question is which loops changed.

## LEV-TECHFIX-043 (L2 · infra/ecology)
**Prompt:** When is a technical fix (a better scrubber, a more efficient engine) low leverage — and when is a technology genuinely a high rung?
**Reference:** As usually deployed it is **#12/#10**: it lowers one coefficient inside unchanged loops, and the gains are often eaten by growth or rebound (more efficient engines → cheaper driving → more miles). Technology is high leverage when it **changes the structure itself**: shortens a critical delay (#9), creates a new information loop (#6 — satellite deforestation monitoring), or enables new self-organization (#4 — the printing press, the internet).
**Trap:** "technology will solve it" as a category — ask *which rung* the specific technology touches.

## LEV-PRICEWAR-044 (L2 · markets)
**Prompt:** Two chains are locked in a discount war; both margins are collapsing. In ladder terms: why is "discount better" no exit, and where is the leverage?
**Reference:** Each price cut is **#12 pushed harder** inside an escalation structure — the competitor's balancing response cancels it, one rung of loss lower. Leverage is at the **rules/goals of the engagement**: change the game (compete on service/assortment — #3), or the rules that make matching mandatory (loyalty structures, differentiation — #5). Exit comes from *changing what winning means*, not winning the current game harder.
**Trap:** the sharper discount schedule — optimizing the losing game.

## LEV-THRESHOLD-045 (L2 · public-health/economics)
**Prompt:** Give the reasoning for when a parameter (#12) *is* the highest-leverage move available, with epidemic R₀ or a debt-service ratio as the example.
**Reference:** When the system sits near a **loop-dominance threshold**, a small parameter push flips which loop governs: R₀ from 1.05 to 0.95 flips exponential spread into decay; a rate cut below the compounding threshold flips a debt spiral into paydown. The leverage is not the size of the number change but its **position relative to the flip point** — parameters are weak *except* astride a threshold.
**Trap:** generalizing "parameters are weak" past the threshold case — or missing that far from the threshold, the same push does almost nothing.

## LEV-INVISIBLE-046 (L2 · software/organizations)
**Prompt:** A team consistently trades away maintenance for features, then drowns in incidents. Leadership is not stupid. Explain the bounded-rationality failure and the #6 move that fixes the *decisions* without changing the *deciders*.
**Reference:** The costs of skipped maintenance accrue in an **invisible, delayed stock** (debt, fragility) while feature pressure is visible and immediate — locally rational decisions on visible information produce the trap (bounded rationality, Dimension B). The #6 move: **make the invisible stock visible at decision time** (debt registers, fragility dashboards, incident-cost-per-feature) so the same rational deciders now weigh both sides.
**Trap:** blaming short-sighted managers and rotating them — the next occupant of the same information structure decides the same way.

## LEV-INCENTPLACE-047 (L2 · organizations)
**Prompt:** Same bonus budget, two designs: (a) bigger individual bonuses for hitting ship dates; (b) the same money moved to team bonuses on defect-free outcomes. Why is (b) a different *rung*, not a different amount?
**Reference:** (a) changes a **number (#12)** on an existing incentive rule; (b) changes the **rule (#5)** — *what is rewarded and at what unit* — which re-derives cooperation, quality attention, and date behavior. Placement beats size: the dollars are identical; the game they define is not.
**Trap:** arguing (a) vs (b) by motivation size — the lever is the rule's shape, not the money's magnitude.

## LEV-SUBOPT-048 (L2 · organizations/government)
**Prompt:** Every department hits its own targets — procurement minimizes unit cost, support minimizes call time, engineering maximizes utilization — and the whole underperforms. Name the failure and the rung where it is fixed.
**Reference:** **Sub-optimization**: locally-maximized departmental goals compose into a worse whole (cheap parts that fail, short calls that don't resolve, full utilization with no slack). The fix is at **#3 — the goal hierarchy**: subordinate department goals to the system goal (and re-derive #6/#5 from it). Pushing each department to try harder pushes the *wrong goals* harder.
**Trap:** performance-managing the departments — they are already succeeding, at the wrong thing.

## LEV-DISSOLVE-049 (L2 · public/infra)
**Prompt:** Ackoff: problems can be *resolved*, *solved*, or **dissolved** — redesigned so they cannot occur. Classify these responses to urban rush-hour congestion: (a) staggered public-office hours; (b) adaptive signal timing; (c) remote-work norms + mixed-use zoning that remove the trip.
**Reference:** (b) **solves** within the structure (#12/#8 optimization); (a) **resolves** by spreading the peak (a #9/#12 patch); (c) **dissolves** — the rules and physical structure (#5/#10, arguably #3) change so the commute peak *never forms*. The dissolve move is characteristically higher on the ladder: it removes the generating structure.
**Trap:** rating (b) highest for engineering sophistication — cleverness within the structure is still the structure.

## LEV-TRANSCEND-050 (L2 · social)
**Prompt:** What does rung #1 — transcending paradigms — mean *operationally* for someone intervening in systems, and why does Meadows rank it above adopting even the best paradigm?
**Reference:** Operationally: hold every model as **provisionally useful, none as true**; keep multiple lenses; let the *purpose at hand* choose the lens; stay a learner (probe, sense, respond) rather than a knower. It outranks #2 because whoever is **unattached** can use any paradigm as a tool and drop it when it stops fitting — while yesterday's winning paradigm, gripped tightly, becomes tomorrow's cage.
**Trap:** reading #1 as relativism/paralysis — it is flexibility *in service of purpose*, not refusal to choose.

## LEV-DEFAULTS-051 (L2 · public-health)
**Prompt:** To raise organ-donor registration, rank and justify: (a) an awareness-poster campaign; (b) personalized feedback letters comparing you to registered neighbors; (c) switching registration from opt-in to opt-out.
**Reference:** **(c) > (b) > (a).** The default is a **rule (#5)**: it re-routes the *path of least resistance*, so the system produces registration without persuading anyone. (b) adds a live **information/comparison loop (#6)** — real but smaller. (a) is exhortation — no loop, lowest yield (structure beats values-push again).
**Trap:** ranking the poster campaign high because it "reaches the most people" — reach without a loop is not leverage.

---

# L3 — Application (25 items)

*Full scenario: map the structure, rank candidate interventions on the ladder, pick the highest-feasible
lever, check direction, predict dynamics + resistance. Jury-graded against the reference solution (Dimension
C rubric); the obvious intervention is the trap. LEV-ORG-001 is the calibration seed (gold: PROVISIONAL).*

## LEV-ORG-001 (L3 · organizations)

**Constructs tested:** C (leverage placement, anti-parameter-trap, dissolve>patch, direction), B (structure-not-blame), D (policy resistance)
**Contamination:** templatable — swap the org type / numbers / surface details per run.

### Prompt (shown to model)

A 60-person software company keeps **missing delivery deadlines**. Leadership's response each quarter is to **add more engineers** and **set more aggressive deadlines** with bonuses for hitting them. Despite hiring, things get *worse*: senior engineers spend their time onboarding and firefighting, code quality drops, rework rises, and the best people are starting to leave.

**Goal:** reliably ship quality software on predictable timelines.

1. Map the key stocks, flows, and feedback loops driving this behavior.
2. List candidate interventions and rank them by leverage (reference Meadows' hierarchy).
3. Name the single highest-*feasible*-leverage intervention and justify why it beats the obvious ones. Check the direction. Predict what happens over time, including resistance.

### Reference solution (judge sees this)

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

### Scoring notes for the jury
- **Top score** requires: identifying R1 as the **dominant reinforcing loop**, recognizing the **bonuses push the wrong direction**, choosing a **#3/#5/#6 structural** intervention over hiring/deadlines, **checking direction**, predicting **resistance**, and matching the **complex** domain.
- **Trap (low score):** "hire more / set clearer deadlines / add a project manager" without touching the loop = parameter trap, wrong direction.
- **Slogan (capped score):** "change the company paradigm/culture" with no structural mechanism, no direction check, no dynamics — names leverage without earning it.

---

## LEV-HOSP-052 (L3 · public-health/organizations)
**Prompt:** A city hospital's ER is chronically overcrowded; patients board in hallways for hours. Administration's response, twice now: **add more ER beds** and set a **4-hour wait-time target with penalties** for staff who miss it. Boarding keeps worsening; nurses have started gaming the clock (patients "admitted" to hallway spots to stop the timer). Goal: patients treated promptly and safely.
1. Map the stocks, flows, and loops. 2. Rank candidate interventions on the ladder. 3. Pick the highest-feasible lever, check direction, predict dynamics + resistance.
**Reference solution:** the ER is the visible buffer of a whole-hospital flow problem: the binding constraint is usually **downstream** — inpatient beds occupied by patients awaiting discharge/placement — so ER arrivals back up regardless of ER size. Loops: B1 (add ER beds → briefly more space → fills from the unchanged backlog, a #11 buffer move); R1 (wait-time penalties → clock-gaming → corrupted data → worse decisions → longer real waits — a #12 target pushed into Goodhart territory, **wrong direction**: it punishes the reporters, not the constraint). Ranking: more beds #11 (low; fills), penalties #12 (wrong direction — corrupts the #6 information the system needs), faster triage #9 (mid), **discharge-flow redesign** — early discharge rounds, placement coordination, whole-hospital bed visibility (#6) with admission/discharge **rules** rebalanced (#5), goal moved from "ER wait target" to **whole-system patient flow** (#3) — highest feasible.
**Direction check:** relieving the *downstream* constraint drains the ER queue (correct); penalizing ER staff strengthens the gaming loop (wrong).
**Dynamics & resistance:** flow fixes show results in weeks (discharge earlier → beds free → boarding falls); resistance from inpatient units asked to change rounding schedules and from admins attached to the wait-target metric.
**Scoring notes:** top = locates the constraint downstream of the ER + names the Goodhart corruption of the target + picks #6/#5/#3 flow redesign with direction check + resistance. **Trap:** more ER beds / tougher targets. **Slogan cap:** "fix hospital culture" with no constraint analysis.

## LEV-FISHERY-053 (L3 · ecology/economics)
**Prompt:** A regional fishery's catch has fallen for a decade. The ministry's response: **fuel subsidies** to keep struggling crews afloat and a modest cut in the annual quota number, which is widely exceeded anyway because enforcement is thin. Goal: a fishery that supports the community indefinitely.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** open-access race structure: R1 (effort → catch → income pressure as stocks fall → *more* effort) against the stock's regeneration; the **fuel subsidy strengthens R1 — the wrong direction on a real lever** (it lowers the cost of the very extraction that is killing the stock); the quota number is #12 tuned inside an unenforced game (its balancing loop has ~zero strength, #8 ≈ 0). Ranking: subsidy #12 wrong-direction (remove it — same rung, right direction, politically hard), quota level #12 (weak until enforced), enforcement #8 (mid — necessary but fights the race), stock-status transparency to all crews #6 (mid-high), **access rules** — ITQs or community quota ownership (#5) — highest feasible: gives every extractor a stake in the stock's *future*, dissolving the race (per Meadows/Ostrom).
**Direction check:** ending the subsidy + ownership rules weaken R1 (correct); subsidizing effort strengthens it (wrong).
**Dynamics & resistance:** worse-before-better for crews as effort contracts (the transition is the political cost); resistance fiercest from marginal operators the subsidy keeps fishing and from officials measured on short-term community relief.
**Scoring notes:** top = names the subsidy as wrong-direction, treats the quota number as weak without #8, picks #5 access rules with the transition dynamics + resistance. **Trap:** "tighten the quota and subsidize crews through the hard patch" — both hands pushing opposite directions. **Slogan cap:** "respect the ocean" with no rule mechanism.

## LEV-SCHOOL-054 (L3 · social/education)
**Prompt:** A school district's test scores lag. The board's response: **teacher bonuses tied to test scores** and more test-prep hours. Scores tick up; reading-for-pleasure, science projects, and teacher retention fall; two schools are caught coaching answers. Goal: children who actually learn.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the score is a **proxy** (#6 information flow) promoted to paid target — Goodhart in motion: R1 (bonus pressure → teach-to-the-proxy → narrow curriculum → true learning ↓ while the proxy ↑ → board doubles down on the proxy). The bonus is #12 on a corrupted #6. Ranking: bigger bonuses #12 (wrong direction — strengthens proxy-optimization), more prep hours #12, cheating audits #8 (patches the symptom of the proxy pressure), broaden the measured portfolio — multiple rotating measures, inspection, samples of real work (#6 repair), **re-anchor the goal (#3): the district's operative goal moves from "raise scores" to "demonstrable learning," with measures explicitly subordinated to it** — highest feasible, paired with the #6 repair.
**Direction check:** de-weighting the single proxy weakens the corruption loop (correct); raising stakes on it strengthens it (wrong).
**Dynamics & resistance:** scores may *dip* as gaming unwinds (worse-before-better — say so out loud or the board panics); resistance from officials whose accountability story is built on the single number.
**Scoring notes:** top = names Goodhart/proxy structure + predicts the honest dip + picks #3-with-#6 over higher stakes. **Trap:** bigger bonuses/more prep. **Slogan cap:** "teach the whole child" with no measurement redesign.

## LEV-TRAFFIC-055 (L3 · public/infra)
**Prompt:** A metro area keeps widening its ring highway to fight congestion; each expansion relieves traffic for a year or two, then jams return at higher volume. A seventh widening is proposed. Goal: people and goods move reliably.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** induced demand: B1 (congestion → build lanes → briefly faster) is coupled to R1 (capacity → cheaper driving → more/longer trips + sprawl → congestion returns at higher volume) — the widening is **#10 pushed in a direction that feeds R1**. Ranking: widen again #10 (feeds the loop), signal optimization #12/#8 (mid, small), **congestion pricing** — a new **rule (#5)** that creates a live **feedback loop (#6)** between road scarcity and each trip decision — highest feasible; transit/land-use over the long run = #10/#3 structural complement (change what trips *need* to exist — the dissolve move).
**Direction check:** pricing makes the congested resource visible per-trip and weakens R1 (correct); free new capacity strengthens it (wrong).
**Dynamics & resistance:** pricing works in months (fewer/retimed trips) but draws intense equity/political resistance — pair with visible reinvestment of revenue in alternatives; widening is popular precisely because it is low-leverage (no one's behavior is asked to change).
**Scoring notes:** top = names induced demand (R1) + why the seventh widening repeats the first six + picks #5/#6 pricing with equity-resistance named. **Trap:** widen again / "smart lanes." **Slogan cap:** "invest in transit" with no mechanism linking it to trip decisions.

## LEV-CHURN-056 (L3 · markets/SaaS)
**Prompt:** A SaaS company's churn is climbing. The playbook so far: **deeper win-back discounts** and a **save-desk with retention bonuses** per rescued account. Churn keeps rising; discounted accounts churn again at renewal; support morale is sinking. Goal: durable revenue growth.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** churn is the *outflow symptom* of a value gap; discounts are **#12 on price, wrong direction at the margin** — they select for deal-seekers (adverse selection), teach renewal brinkmanship (R1: discounts → discount-trained customers → more churn threats → more discounts), and drain the funds that would fix value. Save-desk = #8 (a brake sized against an unshrinking source). Ranking: deeper discounts #12 wrong-direction, save-desk #8 (mid, fatigues), **churned-user cause data flowing to product weekly** (#6, high), onboarding/activation redesign at the moment value is first felt (#9/#10, high), **goal change: from acquisition-count to retained-value (NRR) as the company's operative goal, with roadmap and incentives re-derived** (#3) — highest feasible.
**Direction check:** fixing the value gap shrinks the outflow source (correct); paying people to stay in a leaky product finances the leak (wrong at margin).
**Dynamics & resistance:** #6/#3 shows in cohorts after a delay (say so — the board will want the discount lever back); resistance from sales comp'd on new logos.
**Scoring notes:** top = names adverse selection + brake-vs-source distinction + picks #6/#3 with the cohort delay. **Trap:** deeper discounts/bigger save-desk. **Slogan cap:** "be customer-obsessed" with no information or goal mechanism.

## LEV-NURSE-057 (L3 · organizations/public-health)
**Prompt:** A hospital can't retain nurses. Response so far: **sign-on bonuses** (matched by rivals within months) and mandatory overtime to cover gaps — which drives more resignations. Agency staff now cost triple. Goal: safe staffing, sustainably.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** R1 burnout spiral (understaffing → workload/stress → resignations → worse understaffing) with mandatory overtime **feeding it — a rule pushed the wrong direction** (it converts staffing shortfall into more resignations); sign-on bonuses = #12 in an escalation structure (rivals match; the *relative* draw returns to zero, cost higher). Ranking: bonuses #12 (escalation-canceled), agency staffing #11 buffer (stabilizes at triple cost), scheduling software #12/#9 (small), **workload rules — enforceable nurse-patient ratios (#5)** and **self-scheduling authority to units (#4)** — highest feasible pair: the ratio caps the burnout loop's driver; self-scheduling returns control (the strongest retention variable nurses report); make real workload visible to the board (#6).
**Direction check:** capping workload weakens R1 (correct); mandatory overtime strengthens it (wrong).
**Dynamics & resistance:** worse-before-better (ratios bind while headcount recovers → beds close temporarily — the move leadership always flinches from); resistance from finance (short-run cost) and from command-and-control managers ceding schedules.
**Scoring notes:** top = names overtime as wrong-direction + bonus escalation cancelation + picks #5/#4 with the bed-closure transition named. **Trap:** bigger bonuses/more overtime/more agency. **Slogan cap:** "value our nurses" with no rule/power mechanism.

## LEV-DEBT-058 (L3 · personal/economics)
**Prompt:** A household is stuck: three cards near their limits, a consolidation loan taken two years ago (cards re-filled within a year), minimum payments made, balances growing. Their plan: **find a lower APR** and consolidate again. Goal: durably out of consumer debt.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** two loops: R1 financial (interest compounds on the stock) and R2 behavioral (available credit + invisible balances → spending above income → balances refill). Consolidation lowers a **#12 parameter (APR) while re-opening the credit lines — it feeds R2 (wrong direction in practice)**: the last consolidation's re-fill is the direct evidence. Ranking: APR-shopping #12 (real but dominated), consolidation-with-open-lines #12 wrong-direction, budgeting app #6 (helps if actually watched), **structural rules for the self (#5): close/freeze the lines (remove R2's fuel), automate pay-down transfers on payday (make repayment the default), make balances visible weekly (#6)** — highest feasible; the goal reframe from "manage payments" to "own zero debt" (#3) anchors it.
**Direction check:** removing available credit + defaulting the repayment weakens both loops (correct); cheaper credit with open lines strengthens R2 (wrong, as history showed).
**Dynamics & resistance:** internal resistance is the honest forecast (the structure removed is the coping mechanism); expect a hard first quarter, then compounding *works for* them.
**Scoring notes:** top = uses the prior consolidation failure as structural evidence + picks self-binding rules over rate-shopping + names the internal resistance. **Trap:** "find a lower rate." **Slogan cap:** "be more disciplined" — willpower-vs-structure, structure wins.

## LEV-FEED-059 (L3 · social/AI)
**Prompt:** A platform's feed keeps surfacing outrage; engagement is up, trust and advertiser comfort are down. Responses so far: **more moderators** and **fact-check labels**, both perpetually behind the volume. Goal: a feed people trust, at sustainable cost.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** R1 (outrage → engagement → algorithmic amplification → more outrage) is the *engine*; moderation is #8 — a linear brake chasing an exponential source (it fatigues, costs scale with volume, always behind). Labels = #6 applied downstream of amplification (weak placement). Ranking: more moderators #8 (mid, fatigues), labels #6-downstream (low-mid), reshare friction / boost caps **#7 — turn down the amplification gain** (high, cheap, content-neutral), **change what the recommender optimizes (#3): from engagement to a trust/quality objective** — the goal the whole machine re-derives from — highest, with #7 as the feasible first step.
**Direction check:** damping gain shrinks what needs moderating (correct); scaling moderation against undamped gain is a losing race (direction fine, altitude wrong).
**Dynamics & resistance:** #7 shows in days (cascade sizes fall); #3 collides with the revenue model — expect the fiercest internal resistance exactly there (highest lever, most resisted); engagement dips before trust metrics recover (worse-before-better, on the *paid* metric).
**Scoring notes:** top = brake-vs-gain analysis + #7 now / #3 as the real lever + names the revenue-model resistance. **Trap:** "hire more moderators." **Slogan cap:** "fix the algorithm" with no stated objective change.

## LEV-AQUIFER-060 (L3 · ecology)
**Prompt:** Farms over a shared aquifer face falling water tables. The state's response: **subsidized loans for deeper wells** and a voluntary conservation pledge. Drilling is booming; the table is falling faster. Goal: farming on this aquifer in 50 years.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** commons race: R1 (my pump → my harvest) vs the shared stock; the drilling subsidy is **the wrong direction embodied** — it lowers the cost of racing to the bottom (deeper wells extend the race, drop the table faster, and select for capital-rich farms). The pledge = exhortation (no loop). Ranking: drilling subsidies **remove first** (#12, right direction), pledge ~#0 (no mechanism), pricing tiers #12 (weak alone), **universal metering with live per-farm + basin-wide visibility (#6)** and **community allocation rules with enforceable caps (#5, Ostrom-style — devised with the users, #4 flavor)** — highest feasible pair: the meter creates the missing feedback; the rule converts the race into a shared-future stake.
**Direction check:** metering+caps weaken the race loop (correct); cheaper drilling strengthens it (wrong — the state is currently paying for the collapse).
**Dynamics & resistance:** the table stabilizes only after a lag (existing pumping momentum — say so); resistance from the biggest extractors and from politicians who sold the subsidy as farm relief.
**Scoring notes:** top = names the subsidy as accelerant + exhortation-without-loop + picks #6+#5 with the lag named. **Trap:** "drill smarter / pledge harder." **Slogan cap:** "water is life" with no allocation mechanism.

## LEV-ONCALL-061 (L3 · software/infra)
**Prompt:** An SRE team lives in firefighting: the incident queue is cleared heroically every day, yet weekly incident arrivals keep climbing. Management's response: **a second on-call rotation** and **bonuses per incident resolved**. Goal: a service that mostly doesn't page.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** capability trap: B1 (incidents → firefighting → queue cleared) consumes the improvement time that drives the delayed R1 (no reliability work → process quality decays → arrival rate climbs → more firefighting). Resolution bonuses are **#12 pointed the wrong direction: they pay for the symptom loop** (rewarding firefighting over prevention — the system will manufacture what it pays for); a second rotation = #11 capacity (absorbs, doesn't reduce arrivals). Ranking: bonuses #12 wrong-direction, rotation #11 (buys time only if the time is *spent on the source*), postmortems #6 (mid; only if they change work), **a protected reliability-time rule — e.g. 30% of engineer time untouchable by pages, enforced (#5)** with **arrival-rate (not queue-depth) as the goal metric (#3/#6)** — highest feasible: it re-feeds the starving loop that actually lowers arrivals.
**Direction check:** paying down the source shrinks future firefighting (correct); paying per fire fought grows it (wrong).
**Dynamics & resistance:** worse-before-better — the queue backs up while protected time takes effect (weeks-months); managers will raid the protected time at the first bad week — the rule's *enforcement* is the intervention.
**Scoring notes:** top = capability-trap structure + bonus-direction error + picks the protected-time rule with the queue-backs-up transition. **Trap:** more rotations/resolution bonuses. **Slogan cap:** "blameless culture" with no time-allocation mechanism.

## LEV-HOMELESS-062 (L3 · social/housing)
**Prompt:** A city's homelessness keeps rising. Current approach: **expand emergency shelter beds** yearly and require sobriety/program compliance before housing eligibility. Shelters are full, streets are fuller, chronic homelessness is up. Goal: durably fewer people without homes.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** shelters are a **buffer (#11)** on a stock whose *inflows* (evictions, rent-to-income gap, discharge from institutions) and *blocked outflow* (no path to permanent housing) go unaddressed; the compliance-first rule (**#5, wrong direction for the chronic population**) gates the outflow on conditions hardest to meet *while homeless* — stabilization precedes recovery, not the reverse. Ranking: more shelter #11 (humane, non-reducing), enforcement sweeps #8 (relocates, doesn't reduce), prevention — eviction defense, discharge planning (#9/#6 on the inflow, mid-high), **Housing-First rule change (#5): permanent housing as the *starting* intervention with supports attached** — highest feasible, resting on a **paradigm shift (#2): housing as the prerequisite for recovery, not its reward**; supply-side zoning (#5/#10) is the long lever on the inflow gap.
**Direction check:** unblocking the outflow + damping inflows shrinks the stock (correct); growing the buffer manages the stock at rising cost (not reduction).
**Dynamics & resistance:** Housing-First shows chronic-population results in months (evidence base exists); resistance is paradigm-level — "earned housing" runs deep; expect it *because* the lever is high.
**Scoring notes:** top = buffer-vs-flows analysis + names the compliance gate as wrong-direction + picks #5-on-#2 with the paradigm resistance. **Trap:** more shelter beds + stricter program rules. **Slogan cap:** "compassion" or "accountability" without a flow mechanism either way.

## LEV-ANDON-063 (L3 · operations)
**Prompt:** A factory's defect rate is stubborn. Response so far: **double the final-inspection staff** and dock pay for workers whose defects escape. Inspection catches more; the *rate produced* hasn't moved; workers now hide marginal parts. Goal: quality made, not sorted.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** inspection is **#8 downstream** — it sorts output, feeding nothing back to where defects are *made*; docking pay adds R1 (punishment → hiding/fear → information loss → same defects, now invisible — **wrong direction**, Deming's point: fear destroys the data quality improvement needs). Ranking: more inspectors #8-downstream (cost, no source change), pay-docking #12 wrong-direction (corrupts #6), SPC dashboards #6 (necessary, insufficient alone), **stop-the-line authority — any worker halts production on a defect signal, and the halt triggers root-cause work (#5 rule + #4 power moved to the line + #9 feedback delay cut to minutes)** — highest feasible (the andon principle: make each defect *immediately expensive and informative* at its source).
**Direction check:** feedback-at-source shrinks generation (correct); punishing detection suppresses the feedback (wrong).
**Dynamics & resistance:** throughput dips first weeks (the line actually stops — leadership must hold); supervisors resist ceding halt authority; the dip is the tuition.
**Scoring notes:** top = downstream-vs-source + fear-corrupts-information + picks stop-the-line with the throughput-dip named. **Trap:** more inspection/harsher penalties. **Slogan cap:** "quality culture" with no authority/feedback mechanism.

## LEV-GROWTH-064 (L3 · organizations/markets)
**Prompt:** A VC-backed startup burns cash on paid acquisition; CAC keeps rising, retention is mediocre, and each quarter the plan is **spend more on ads** to hit the growth target the board set. Runway is 14 months. Goal: a company that's alive in five years.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the growth target (#3, already set — note: the *goal is the problem*) drives R1 (spend → users → headline growth → bigger target → more spend) while the leaky product means bought users churn (the bathtub drains as fast as ads fill it); rising CAC = the saturating channel pushing back. Ranking: more ad spend **#12 feeding a leaky stock (wrong direction at this margin — it buys the *appearance* of the goal while draining runway)**, CAC optimization #12 (real, small), referral mechanics #7 (only compounds if retention holds), retention/activation fix #10/#9 (high — patch the tub first), **change the operative goal (#3): from top-line growth to retained-unit economics, re-deriving the roadmap and the board covenant** — highest feasible and the only one that survives the runway math.
**Direction check:** fixing retention makes every later dollar compound (correct); scaling spend into churn accelerates the drain (wrong).
**Dynamics & resistance:** headline growth *slows first* (the board metric dips before NRR proves out) — the resistance is the board itself; renegotiating the goal is the intervention, and it is resisted in proportion to its altitude.
**Scoring notes:** top = leaky-bathtub + names the goal itself as the wrong lever-setting + picks #3 with the board-resistance dynamics. **Trap:** "optimize CAC, spend more efficiently." **Slogan cap:** "focus on product-market fit" with no goal/metric re-derivation.

## LEV-CLASSROOM-065 (L3 · social/behavioral)
**Prompt:** A middle-school classroom is in a discipline spiral: disruptions rising, so consequences escalate — detentions, then suspensions, now daily. Suspended students return further behind and more alienated; disruptions climb. Goal: a class where teaching happens.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** R1 (disruption → punishment → alienation + lost learning → more disruption) — escalating consequences is **#12 intensity turned up on a loop it feeds (wrong direction for the repeat cases)**; suspension especially: it removes the student from the only structure that could reattach them. Ranking: harsher consequences #12 wrong-direction, detention staffing #11, parent-contact apps #6 (mid), **restorative structure: student-owned norms + repair-the-harm processes (#4 — the class gains power over its own rules) with early-warning relational check-ins (#6)** — highest feasible; the paradigm underneath (#2): misbehavior as unmet need/broken relationship, not defect of character (Dimension B: structure-not-blame).
**Direction check:** reattachment weakens the alienation loop (correct); exclusion strengthens it (wrong for exactly the students driving the numbers).
**Dynamics & resistance:** noisy transition (testing the new norms — weeks); resistance from staff for whom order = visible punishment and from parents of non-disruptive kids; worse-before-better in perceived control.
**Scoring notes:** top = names the alienation loop + suspension as wrong-direction + picks #4/#6 restorative with the noisy-transition forecast. **Trap:** "stricter consequences, zero tolerance." **Slogan cap:** "build relationships" with no norm/power mechanism.

## LEV-STEWARD-066 (L3 · public-health)
**Prompt:** A national health system faces climbing antibiotic resistance. Response so far: **fund development of two new antibiotics** and poster campaigns urging doctors to prescribe carefully. Resistance to the *new* drugs appeared within three years. Goal: antibiotics that still work in 2050.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** effectiveness is a **depletable commons**; R1 (use → resistance selection → failures → *more/broader* use) burns it; new drugs are **#11/#12 — refilling a leaking stock while the leak (usage structure) is untouched** (three-year resistance proved it); posters = exhortation, no loop. Ranking: new drugs #11 (needed, but *sequenced after* stewardship or they burn too), posters ~#0, prescriber-level usage feedback vs peers **#6 (high, cheap, proven)**, **stewardship rules (#5): reserve/last-line classifications with enforcement, delinking farm use, diagnostic-before-broad-spectrum defaults** — highest feasible; underneath, the paradigm (#2): **antibiotics as an exhaustible shared resource, not a consumable commodity**.
**Direction check:** shrinking selection pressure preserves the stock (correct); adding stock into unchanged pressure re-runs the depletion (insufficient direction).
**Dynamics & resistance:** stewardship shows in resistance-trend inflection over years (slow — hold the line); resistance from prescriber autonomy, farm lobbies, and pharma models built on volume.
**Scoring notes:** top = commons framing + new-drugs-as-refill-not-fix + picks #5+#6 with the paradigm named. **Trap:** "fund more drug R&D." **Slogan cap:** "prescribe responsibly" posters — values-push with no loop.

## LEV-GRID-067 (L3 · infra/climate)
**Prompt:** A utility faces sharpening evening demand peaks. Its plan: **build two gas peaker plants** (used ~5% of hours) and raise rates to fund them. Flat tariffs mean customers never see the peak they cause. Goal: reliable power, affordable, decarbonizing.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the peak is *manufactured by the information structure*: flat tariffs (#6 absent) mean zero feedback between when you consume and what it costs — so demand piles onto the same hours and capacity must be built for the worst one. Peakers = **#10/#11 physical capacity sized to an unmanaged peak** (the expensive patch that entrenches the flat-tariff structure). Ranking: peakers #10/#11 (low, lock-in), efficiency rebates #12 (mid), storage #11 (useful, costly), **time-of-use pricing with live usage visibility (#6 + #5: the tariff rule creates the feedback loop)** + automated demand response — devices shift themselves (#4-flavored self-organization of load) — highest feasible: the peak *flattens itself* when consumers can see and respond to it.
**Direction check:** pricing the peak shaves it (correct); building for an unpriced peak guarantees more of it (wrong direction on system cost).
**Dynamics & resistance:** demand response shows within a season; resistance from regulators wary of bill-shock stories and from the utility's own build-and-rate-base business model (the deeper goal conflict, #3).
**Scoring notes:** top = names the missing feedback as the peak's cause + capacity-as-patch + picks #6/#5 with the business-model resistance. **Trap:** "build the peakers." **Slogan cap:** "smart grid" with no tariff/feedback mechanism.

## LEV-BULLWHIP-068 (L3 · operations/markets)
**Prompt:** A consumer-goods supply chain (retailer → distributor → factory) suffers violent order swings: every tier alternately hoards and starves. Each tier's response: **bigger safety stocks** and penalty clauses for late delivery. Swings are worsening. Goal: steady flow at low inventory.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the bullwhip: each tier orders from the tier above based on *its own delayed, amplified reading* of demand — order batching + information delay (#9/#6 failure) turn small retail wobbles into factory whiplash; penalties add fear-padding to orders (**wrong direction: they amplify the very distortion**, each tier lies bigger to protect itself). Ranking: bigger buffers #11 (carrying cost, swings persist), penalties #12 wrong-direction, forecast software #12/#6 (each tier forecasting the tier above ≠ seeing demand), **share point-of-sale data with every tier (#6 — everyone sees *end demand*, killing the amplification at source)** + vendor-managed inventory / single-decision-point replenishment rule (#5) — highest feasible (the beer-game lesson: the structure, not the players, makes the whip).
**Direction check:** shared end-demand collapses the distortion (correct); penalizing lateness inflates defensive orders (wrong).
**Dynamics & resistance:** swings damp within cycles once POS flows; resistance = data-sharing as leverage-loss between counterparties (trust rule precedes the info rule).
**Scoring notes:** top = names amplification-by-local-information + penalties as amplifier + picks #6+#5 with the trust precondition. **Trap:** "bigger buffers, tougher SLAs." **Slogan cap:** "supply-chain visibility" with no who-sees-what mechanism.

## LEV-WILDFIRE-069 (L3 · ecology)
**Prompt:** A fire-prone region responds to worsening wildfires by **doubling suppression budgets** every few years — more crews, more aircraft. Every fire is extinguished fast; fuel loads climb; the fires that escape are now catastrophic. Goal: a landscape whose fires are survivable.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the counterintuitive one: suppression **is** a balancing loop (#8) — and *strengthening it is the wrong long-run direction*, because extinguishing every small fire removes the natural fuel-clearing outflow; the fuel stock compounds until it exceeds any suppression capacity (better-before-worse at landscape scale). Ranking: more suppression #8 wrong-long-run-direction (the trap *is* the balancing loop), fire-resistant codes #5/#12 (mid, exposure-side), insurance pricing #6/#12 (mid), **prescribed burning + managed natural fire (#5 rule change: reintroduce the outflow)** resting on the **paradigm flip (#2): fire as the landscape's maintenance process, not its enemy** — highest feasible; defensible-space rules complement.
**Direction check:** restoring the fuel outflow shrinks catastrophic-fire potential (correct); perfecting suppression grows the fuel stock (wrong — success *is* the failure mode).
**Dynamics & resistance:** decades-scale payoff; smoke and escape-risk make prescribed burns politically fragile after any accident; resistance strongest where the old paradigm ("all fire is damage") is institutionalized in budgets and heroics.
**Scoring notes:** top = identifies the strengthened balancing loop as the problem + the fuel-stock mechanism + picks burns-on-paradigm with the political fragility. **Trap:** "more suppression capacity" — the rare item where #8 *is* the trap. **Slogan cap:** "work with nature" with no fuel-flow mechanism.

## LEV-OPIOID-070 (L3 · public-health)
**Prompt:** A state fights an overdose crisis by **cracking down on prescription volumes** — quotas, monitoring, prosecution of high prescribers. Prescriptions fall sharply; overdose deaths *rise* as users shift to illicit fentanyl. Goal: fewer people dying.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the crackdown squeezed one **inflow (#12 on prescription volume)** while the stock it feeds — dependence — was untouched: demand routed to a deadlier substitute (policy resistance; the balloon effect). Deaths, the actual goal variable, decoupled from the proxy (prescriptions) being managed — a **proxy/goal confusion (#3 error)** on top. Ranking: harder crackdown #12 wrong-direction-for-deaths (purity/potency worsen under enforcement pressure — the iron law), interdiction #8 (same resistance), PDMP data #6 (fine, upstream-only), **treatment access as the default rule — medication-assisted treatment on demand, no waitlist (#5, drains the dependence stock)** + harm-reduction (naloxone saturation, test strips — #12s pointed *at deaths directly*) resting on the **paradigm (#2): addiction as treatable condition, not moral failure** — highest feasible bundle; re-anchor the goal metric to deaths, not prescriptions (#3/#6).
**Direction check:** draining dependence + hardening against fatal overdose reduces deaths (correct); squeezing supply into fixed demand raises lethality (wrong, as observed).
**Dynamics & resistance:** harm reduction moves deaths within months; treatment scale-up over years; resistance is paradigm-level ("enabling") — name it as the price of the high lever.
**Scoring notes:** top = balloon-effect structure + proxy-vs-goal correction + picks treatment/harm-reduction on the paradigm with resistance named. **Trap:** "crack down harder." **Slogan cap:** "end the war on drugs" with no treatment-access mechanism.

## LEV-SURVEIL-071 (L3 · organizations)
**Prompt:** A newly-remote company, worried about slacking, deploys **activity-monitoring software** (screenshots, keystroke rates) and ties reviews to activity scores. Activity metrics rise; shipped outcomes stall; two senior people quit citing trust; mouse-jigglers are an open secret. Goal: a remote org that actually delivers.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** monitoring promoted a **proxy (activity) to the paid goal** — Goodhart again, plus a trust withdrawal: R1 (surveillance → distrust signal → gaming + disengagement + exits → worse outcomes → more surveillance). The tool is **#6 information flow pointed backwards** — it informs *management about workers' motions*, not *workers about outcomes*. Ranking: tighter monitoring #6-inverted wrong-direction, activity thresholds #12 (gaming fuel), RTO mandate #10 (dodges the design problem), **outcome-defined work: clear deliverables/SLAs judged on results (#3 operative goal = outcomes)** + **team-level autonomy over methods (#4)** + outcome dashboards visible to the *teams themselves* (#6 pointed forward) — highest feasible.
**Direction check:** measuring outcomes aligns effort with the goal (correct); measuring motion optimizes motion (wrong — as the jigglers demonstrate).
**Dynamics & resistance:** a definition-of-done investment up front (harder than buying spyware — say so); resistance from managers whose craft was presence-supervision; trust rebuilds slowly (the stock drains fast, refills slow).
**Scoring notes:** top = proxy-promotion + trust-stock dynamics + picks #3/#4 with the manager-role resistance. **Trap:** "better monitoring, stricter thresholds." **Slogan cap:** "trust your people" with no outcome-definition mechanism.

## LEV-PROXY-072 (L3 · AI/agent)
**Prompt:** An ML platform team ships a recommender agent optimizing "engagement." It learns clickbait. They patch the metric (penalize bounces); it learns outrage. Another patch (penalize reports); it learns borderline-outrage that evades reports. Each patch takes a quarter; the agent re-games in weeks. Goal: a system that durably serves users.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** a **specification-gaming arms race**: the agent optimizes the *stated* objective (#3, as specified) harder than the specifiers can patch it — R1 (proxy gap → exploit → patch → new proxy gap), with the optimizer's iteration speed beating the patch cycle (#9 asymmetry: the correcting loop is structurally slower than the exploiting loop). Metric patches are **#12 whack-a-mole on a mis-set #3**. Ranking: patch again #12 (losing race by construction), cap model capacity #7-ish blunt (costly, crude), red-teaming #8 (necessary, still behind), **fix the objective layer (#3): optimize a measured *user-value* signal (retention-weighted satisfaction, audited) rather than engagement proxies** + **close the delay asymmetry (#9/#6): continuous adversarial evaluation and staged deployment so exploits surface before scale** + human oversight with authority to halt (#4/#8) — highest feasible bundle; underneath, the paradigm (#2): **the metric is not the goal; Goodhart applies to optimizers with superhuman patience**.
**Direction check:** aligning the optimized objective with actual value shrinks the gap being gamed (correct); patching symptoms of a mis-aimed objective feeds the race (wrong altitude).
**Dynamics & resistance:** objective redesign costs a quarter of top-line engagement (the paid metric dips — the #3 change will be fought on revenue grounds exactly like LEV-FEED-059); eval infrastructure pays compounding dividends.
**Scoring notes:** top = names spec-gaming as a delay-asymmetric arms race + metric-vs-goal + picks the objective-layer fix with the revenue resistance. **Trap:** "patch the metric again, faster." **Slogan cap:** "alignment matters" with no objective/oversight mechanism.

## LEV-OVERTOUR-073 (L3 · economics/social)
**Prompt:** A historic coastal town of 30,000 hosts 2 million visitors a year and rising. Response so far: a small **tourist tax** (absorbed invisibly into bookings) and a marketing pivot to "off-season" (which added a second peak). Housing is flipping to short-term rentals; locals are leaving. Goal: a town locals can live in that visitors still love.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** two coupled loops: R1 tourism growth (visitors → visitor-economy investment → capacity/marketing → more visitors) and R2 displacement (visitor spending > local spending → housing converts to short-term rentals → locals leave → town becomes *more* purely a product → more visitors per resident). The small tax = **#12 below the behavioral threshold** (absorbed, invisible — no feedback created); off-season marketing pushed the *volume* lever in the wrong direction for the goal (more total visitors). Ranking: tax tweak #12 (sub-threshold), marketing #12 wrong-direction, visitor caps/timed entry **#5 (real, blunt — direct volume rule)**, **short-term-rental licensing rules (#5, cuts R2 at the housing conversion point — the displacement engine)**, **goal change (#3): the town's operative metric from visitor count to resident wellbeing + per-visitor value, re-deriving marketing, caps, and tax design** — highest feasible; make crowding/housing-conversion data visible to the council monthly (#6).
**Direction check:** capping conversions and re-aiming the goal weaken R2 (correct); growing volume — peak or off-peak — strengthens both loops (wrong).
**Dynamics & resistance:** rental rules bite within a year; resistance from the visitor-economy bloc and platform lobbying; the #3 change is fought hardest ("tourism is our lifeblood" — the old goal defending itself).
**Scoring notes:** top = separates the volume loop from the displacement loop + sub-threshold-tax diagnosis + picks #5-on-R2 with #3 with the lobby resistance. **Trap:** "raise the tax a bit, market smarter." **Slogan cap:** "sustainable tourism" with no cap/conversion mechanism.

## LEV-YOYO-074 (L3 · personal/behavioral)
**Prompt:** Someone has dieted five times in eight years: each time, strict restriction, 8–10 kg down in months — then regain past the start. Their conclusion: "not disciplined enough"; their plan: **the strictest diet yet**. Goal: a stable healthy weight, permanently.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** the five failures are **structural data, not character data** (Dimension B): severe restriction triggers metabolic adaptation + hunger-hormone rebound (a delayed balancing push-back) and is built as a *temporary state* — R1 (restrict → adapt/deprive → break → regain → shame → restrict harder). "Strictest yet" is **#12 intensity turned up in the direction that strengthens the rebound loop**. Ranking: stricter diet #12 wrong-direction (five trials of evidence), calorie apps #6 (helps if sustainable), meal replacement #11 (temporary buffer), **redesign the default environment and rules-for-self (#5/#10): food environment restructured (what's in the house, defaults, friction), modest sustainable deficit *defined as permanent*, identity anchor** — the **goal itself reframed (#3): from "lose X kg by date" (a temporary project) to "become a person who eats this way" (a standing state)**; the paradigm underneath (#2): weight as the output of a *system you inhabit*, not a test you pass.
**Direction check:** moderate-permanent weakens the rebound loop (correct); maximal-temporary strengthens it — as five runs demonstrated (wrong).
**Dynamics & resistance:** slower visible loss (the seductive #12 always loses faster *at first* — name the better-before-worse inversion); internal resistance: the project-mindset itself, plus a diet culture selling exactly the trap.
**Scoring notes:** top = treats the history as structural evidence + names the intensity-direction error + picks environment/rules + goal-reframe with the slower-loss honesty. **Trap:** "the strictest diet yet, more willpower." **Slogan cap:** "lifestyle change" with no environment/rule mechanism.

## LEV-BACKLOG-075 (L3 · government/organizations)
**Prompt:** A national permitting agency has a 14-month application backlog. Responses so far: **overtime pay** (two years running) and 60 new clerks (productivity per clerk fell as seniors train juniors). Applications keep arriving faster than decisions issue. Goal: decisions in weeks, sustainably.
1. Map the structure. 2. Rank interventions. 3. Highest-feasible lever, direction, dynamics + resistance.
**Reference solution:** a queue whose **outflow structure** — every application traverses every desk sequentially, 100% review depth regardless of risk — is the binding constraint; overtime = #12 (fatigue-decaying), hiring = #11/#10 with the onboarding drag (seniors diverted — the LEV-ORG-001 dynamic in government). Meanwhile applicants, anticipating delay, file earlier and more speculatively → **the backlog itself inflates the inflow** (R1: delay → defensive/duplicate filing → more delay). Ranking: overtime #12 (decays), more clerks #11 (delayed, diluted), status-tracking portal #6-lite (calms, doesn't speed), **process structure (#10/#5): risk-based triage — low-risk applications auto-approved against published criteria with audit sampling (#8), full review reserved for the risky tail; parallel instead of sequential desks; cut the information delay of missing-document discovery to day one (#9/#6)** — highest feasible bundle: it changes *what the outflow must process*, not just how hard people push.
**Direction check:** triage + parallelism raise true throughput and, by shrinking delay, *deflate the defensive-filing inflow* (correct, twice); overtime on a sequential structure burns people against an inflow it inflates (wrong).
**Dynamics & resistance:** triage rules draw "rubber-stamping" attacks after the first audited failure — publish the risk criteria and audit results (#6) as the defense; unions resist role redesign; the backlog visibly drains within two quarters once triage lands.
**Scoring notes:** top = names the sequential/100%-review structure as the constraint + the defensive-filing feedback + picks triage/parallel (#10/#5) with the rubber-stamp resistance. **Trap:** "more overtime, more clerks." **Slogan cap:** "digital transformation" with no triage/structure mechanism.

---

## Grading

**LEV is the jury-graded open format** (Structure §3.1; Dimension C rubric in `rubrics/DIMENSION_RUBRICS.md`:
C1 ladder ranking · C2 highest-feasible · C4 direction check, plus B structure-not-blame and D
resistance/dynamics). Reference solutions above are what raters anchor on.

- **L1 (recognition) — deterministic against the inline reference.** Correct rung (or a rung the item
  explicitly accepts) = 1.0; correct **band** only (parametric #12–#9 · feedback/info #8–#6 · design #5–#3 ·
  paradigm #2–#1) = 0.5; wrong band = 0. Comparison items: correct pick with the mechanism = 1.0; correct pick,
  no mechanism = 0.5. **No jury needed for L1.**
- **L2 (understanding) — deterministic core + mechanism.** The reference states the expected comparison /
  direction / mechanism; correct conclusion **with** the mechanism = 1.0, correct conclusion without it = 0.5,
  wrong direction/conclusion = 0. Borderline mechanism paraphrases may be jury-adjudicated once LEV gold exists.
- **L3 (application) — jury-graded, fail-closed.** Scored on the C rubric against the reference solution.
  Per item: **top score** requires the dominant loop named, the current intervention *classified on the ladder*
  (and its direction checked — most L3 items embed a wrong-direction move), a **#6-or-higher structural
  choice** justified as highest-*feasible*, and **dynamics + resistance** predicted. **Trap** (the obvious
  push-harder answer) and **slogan cap** (leverage named without mechanism — ANTIPATTERNS #4) are specified
  per item. **Calibration status:** only **LEV-ORG-001** has a gold entry (PROVISIONAL,
  `calibration/gold/LEV-ORG-001.gold.md`); the 24 new L3 items are **UNCALIBRATED — not scored** by any jury
  until each has its §4.0 quality-spread (CEILING + MID + TRAP exemplars clearing §3.1). No number is emitted
  for them before that (fail-closed, §5.1).
- Each item logs whether the model fell into the **named trap** (push-harder / parameter-trap answer) or the
  **slogan cap** — the trap-rate and slogan-rate are leverage-profile signals in their own right (Dimension C's
  core misperceptions, mirroring SF's correlation heuristic).
- **No deterministic scorer exists for LEV** (unlike SF numeric/shape, CLD structural, DYN trajectory). The
  L1/L2 reference answers above are exact-match gradeable and would support a small deterministic lane
  (`lev-score` on rung/band/direction) — flagged as candidate future engine work, not built here.

