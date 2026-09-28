# SystemsBench — Archetype Recognition (`ARC`) seed item set

**Format:** ARC · **Grading:** hybrid — **the archetype label is deterministic (auto-checkable, NO judge)**;
the trap it creates and the escape are jury-graded and ship `UNCALIBRATED — not scored` until ARC gold
exists (fail-closed, §5.1). · **Seeded:** 2026-09-27 (SenseRun #14), **born executable**: every item is in
`items/arc_oracle.json` and wired into `engine/harness.py` on the day it was written.
**Constructs:** D3 (archetype recognition, the deterministic half of Dimension D's archetype sub-criterion);
A (loops, delays) and B (structure, not blame) touched; C (the escape) in the jury portion.
**Contamination:** templatable — swap the domain surface, the actors and the numbers per refresh; the
**archetype** is the invariant being tested, and each item names the archetype it is most easily mistaken for.
**Why this format:** Senge's archetypes are the recurring plots systems fall into (Structure §2.3). A model
that can name the plot from a fresh surface, rather than from the textbook example, can predict the trap
before it closes and point at the escape. The reliable failure is surface matching: a story about two parties
reads as "escalation" whether they are rivals or partners, a story about a fix reads as "fixes that fail"
whether the fix backfires or merely displaces the real solution.

**Bank size: 27 items — 9 L1 · 9 L2 · 9 L3.** Every one of the nine archetypes appears once per level, across
all eight domains. Difficulty is operational (Structure §3.2):
- **L1 — Recognition:** a clean, freshly written scenario with one archetype visible; name it.
- **L2 — Understanding:** the scenario plus the obvious move; explain why the obvious move fails and name the
  archetype. The explanation is the jury's; the label is the machine's.
- **L3 — Application:** a novel scenario whose surface resembles a different archetype; name the archetype,
  the trap it creates, and the high-leverage escape.

**Authoring convention (codified SenseRun #14):**
- Each item carries a **Reference** label in the canonical vocabulary and a **Confusable**: the archetype the
  surface most resembles, with the boundary that separates them. Answering the confusable is the trap and is
  capped at 0.25. A label from the same family that is not the confusable earns 0.5 (the plot is in the right
  neighborhood). Any other label earns 0.
- The **trap it creates** (what the naive actor keeps doing) and the **escape** (the high-leverage move) are
  the jury's portion and ship `UNCALIBRATED — not scored` until an ARC gold set clears §3.1/§4.0.
- The nine canonical labels and their families (the scorer's vocabulary; aliases live in `engine/arc-score.py`):
  `limits-to-growth`, `growth-and-underinvestment` (family growth-limits) ·
  `shifting-the-burden`, `fixes-that-fail` (family symptomatic-relief) ·
  `escalation`, `accidental-adversaries`, `success-to-the-successful` (family rivalry) ·
  `tragedy-of-the-commons` (family commons) · `eroding-goals` (family standards).

---

## L1 — Recognition

## ARC-INVITE-001 (L1 · software/infra) — limits-to-growth
**Prompt:** A study app grows only by invitation: every active user invites, on average, two friends in their first month. In a town of 40,000 students the app went from 200 to 9,000 users in a year, and then growth slowed to a crawl even though each user still invites as eagerly as before. The team's response has been to double the invitation bonus. Name the archetype at work.
**Reference:** `limits-to-growth`. A reinforcing loop (users → invitations → users) has met a balancing one: the pool of students not yet invited is shrinking, so each invitation finds fewer people who can accept it. A bigger bonus pushes the reinforcing loop harder against a limit the bonus cannot move.
**Confusable (capped):** `growth-and-underinvestment`. The flattening looks like a capacity the team failed to build, but the limiting condition here, the number of students in the town, is not a capacity anyone can invest into.
**Escape (jury):** act on the limiting factor (a second town, a second population), not on the growth engine.

## ARC-SLEEP-002 (L1 · personal/behavioral) — shifting-the-burden
**Prompt:** Someone who cannot fall asleep starts taking an over-the-counter sleep aid. It works the same night. Over the following months they take it more often, sleep less well without it, and the habits that would have fixed the sleeplessness at its source (a regular bedtime, less screen light late, a walk in the afternoon) never get built, because the problem always feels handled. Name the archetype.
**Reference:** `shifting-the-burden`. The symptomatic solution (the pill) is fast and works every time; the fundamental solution (habits that restore sleep) is slow, and because the symptom is relieved it never gets the pressure it needs. The side effect of the symptomatic solution weakens the capacity for the fundamental one.
**Confusable (capped):** `fixes-that-fail`. The pill does not backfire; it works each night. The damage is what it displaces, not what it causes.
**Escape (jury):** strengthen the fundamental solution while tapering the symptomatic one on purpose.

## ARC-GRAZE-003 (L1 · ecology) — tragedy-of-the-commons
**Prompt:** Twelve families graze goats on a hillside that no one owns. Each family's goats grow fatter the more they graze, so each family adds a few goats a year, and every family can see that doing so is sensible for them. The hillside's grass, which regrows only so fast, is thinner each spring, and this year the thin grass is making every goat lighter than last year's. Name the archetype.
**Reference:** `tragedy-of-the-commons`. Many actors, each inside an individually reinforcing loop, draw on one shared resource whose balancing loop (regrowth) is slower than the sum of their draws. Each family sees its own goats and its own gain; nobody sees the aggregate draw until the grass reports it.
**Confusable (capped):** `success-to-the-successful`. No family is winning at another's expense through an allocation rule; all twelve are losing together against one commons.
**Escape (jury):** govern the commons: make the aggregate draw visible and binding through a rule, a quota or a price the families set together.

## ARC-DEADLINE-004 (L1 · organizations) — fixes-that-fail
**Prompt:** A team keeps missing release dates, so its manager adds mandatory overtime in the last week of each cycle. Each release then ships on time. Over three cycles, the bugs written in the tired last week have grown into a repair load that eats the first two weeks of the next cycle, so each cycle starts further behind, and the manager orders a longer overtime week. Name the archetype.
**Reference:** `fixes-that-fail`. The fix (overtime) closes the gap now; its delayed consequence (defects from tired work) enlarges the very problem it fixed, which invites more of the fix.
**Confusable (capped):** `shifting-the-burden`. No fundamental solution is being starved in this story; the fix itself generates the next round of the problem.
**Escape (jury):** stop the fix, take the short-term miss once, and remove the cause of the lateness (scope, estimation) instead.

## ARC-CREDITS-005 (L1 · economics/markets) — escalation
**Prompt:** Two ride-hailing companies each offer sign-up credits to riders. When one raises its credit, the other reads it as a threat to its share and raises its own; the first responds in kind. Each raise is a reasonable defensive step, and after a year both are paying riders more than either earns from them. Name the archetype.
**Reference:** `escalation`. Two balancing loops, each side restoring its relative position, together form one reinforcing spiral. No single move inside the spiral stops it.
**Confusable (capped):** `accidental-adversaries`. The companies are competitors on purpose and respond to each other's moves deliberately; nobody is undermining a partner by accident.
**Escape (jury):** a unilateral, visible de-escalation, or a shared ceiling both sides can see.

## ARC-STREAM-006 (L1 · social) — success-to-the-successful
**Prompt:** A school streams pupils into two classes after a test at age eight. The higher class gets the most experienced teacher and the wider curriculum, so its pupils improve faster; the next test confirms they belong there, and the difference in resources grows with every year. By age fourteen the gap between the two classes is many times the gap the first test found. Name the archetype.
**Reference:** `success-to-the-successful`. Two reinforcing loops share one fixed resource (teacher time, curriculum). Early success routes more of the resource to the winner, and the allocation rule, not ability, drives the divergence.
**Confusable (capped):** `limits-to-growth`. The lower class is not meeting a natural limit; it is being starved by a rule that feeds the other loop.
**Escape (jury):** decouple the allocation from early results, or give each loop its own resource.

## ARC-WAIT-007 (L1 · public-health) — eroding-goals
**Prompt:** A hospital sets a standard that emergency patients are seen within 30 minutes. When the median creeps to 40, the board debates hiring and instead, to stay realistic, resets the standard to 45. A year later, at 55, it moves the standard again, to 60. Waiting times never spiked; they drifted, and each drift was ratified. Name the archetype.
**Reference:** `eroding-goals`. Two balancing loops close the same gap: one by improving the condition (slow, costly) and one by lowering the goal (fast, painless). Under pressure the second wins, and the standard drifts.
**Confusable (capped):** `shifting-the-burden`. There is relief here, but what is relieved is the gap itself, by moving the goal; no outside fix is displacing a fundamental one.
**Escape (jury):** anchor the goal outside the system that feels the pressure, and let the gap hurt where investment gets decided.

## ARC-TELEHEALTH-008 (L1 · organizations) — growth-and-underinvestment
**Prompt:** A telehealth service wins patients on short waits. As demand rises, waits lengthen; leadership judges that patients will tolerate a little longer, and delays hiring doctors until the numbers prove the demand is durable. Word spreads of long waits, demand softens, and the softened demand is read as proof that hiring was unnecessary. Name the archetype.
**Reference:** `growth-and-underinvestment`. A reinforcing growth loop meets a capacity limit that investment could lift, but investment waits for demand, and the performance standard (an acceptable wait) erodes so the signal to invest never fires. The throttled growth is then read as the reason not to invest.
**Confusable (capped):** `limits-to-growth`. The limit here is a capacity the company chose not to build, and the standard for an acceptable wait is drifting; a fixed, external limit would be the other archetype.
**Escape (jury):** invest ahead of demand, and hold the performance standard against the temptation to rationalize it.

## ARC-PLANNER-009 (L1 · AI/agent) — accidental-adversaries
**Prompt:** Two AI agents share one workflow: a planner that breaks tasks into steps and an executor that runs them. When the executor's steps fail on vague plans, it starts rewriting the plans it receives; the planner, seeing its plans altered, starts writing more rigid, over-specified plans to stop the rewriting; the rigid plans fail more, so the executor rewrites more. Each agent is fixing its own local problem and each fix makes the other's worse. Name the archetype.
**Reference:** `accidental-adversaries`. Two parties in a collaboration each adopt a local fix that unintentionally undermines the other's success, and the partners become adversaries without either intending harm.
**Confusable (capped):** `escalation`. The agents are not competing for position; they are partners whose corrective moves collide. Nothing here is a bid to beat the other.
**Escape (jury):** make each side's local fix visible to the other and change the interface so one side's fix stops being the other's problem.

---

## L2 — Understanding

## ARC-SYNTH-010 (L2 · social) — limits-to-growth
**Prompt:** An online course on restoring vintage synthesizers earned its following by recommendation inside the hobby's forums; enrolments doubled for three cohorts and then stalled at around 2,000 per cohort. The obvious move is to spend on advertising to the general public to restart the doubling. Explain why this move will disappoint, and name the archetype.
**Reference:** `limits-to-growth`. What stopped the doubling is a balancing loop: the number of people for whom this course matters is roughly the size of the hobby, and the recommendation loop has nearly reached them. Advertising to the general public buys attention from people the course was never for, so spend rises while enrolments do not. The lever is the limiting factor (a neighboring hobby, a broader course), not the growth engine.
**Confusable (capped):** `growth-and-underinvestment`. The stall looks like under-spending on marketing, but the limit is the size of the community, not a capacity the course failed to build.
**Escape (jury):** find the limit and act on it: widen the population the course serves, or accept the plateau and improve margin.

## ARC-DENTAL-011 (L2 · public-health) — shifting-the-burden
**Prompt:** A region with too few dentists sees rising emergency visits for tooth pain. The obvious move is to keep expanding the emergency service that hands out antibiotics and painkillers, since it clears the queue each week and patients leave relieved. Explain why the queue will keep growing anyway, and name the archetype.
**Reference:** `shifting-the-burden`. The emergency service is the symptomatic solution: fast, and effective at the symptom. The fundamental solution (dental capacity that treats the tooth) is slow and expensive and, because the symptom keeps getting relieved, attracts less pressure and less funding. The untreated causes keep producing emergencies, the population learns which door is fast, and the burden shifts onto the intervener while the fundamental capacity withers.
**Confusable (capped):** `fixes-that-fail`. The emergency visits do not backfire; each one works. The problem is what they displace.
**Escape (jury):** fund the fundamental solution while the symptomatic one runs, and taper the symptomatic door as the fundamental one comes online.

## ARC-SONAR-012 (L2 · ecology) — tragedy-of-the-commons
**Prompt:** In an unregulated fishery, catches per boat are falling. The obvious move for each captain is to fish longer hours and buy better sonar to keep the household's income up, and each captain who does this does, for a season, catch more. Explain why the fleet as a whole ends up poorer, and name the archetype.
**Reference:** `tragedy-of-the-commons`. Each captain's reinforcing loop (effort → catch → income → effort) draws on one shared stock whose balancing loop, regeneration, is slower than the fleet's aggregate draw. Effort that is rational per boat lowers the stock for all, so the per-boat catch that triggered the effort falls further, and the response is more effort. Every captain sees their own catch and never the aggregate draw.
**Confusable (capped):** `escalation`. The captains are not answering each other's moves as threats; each is answering their own falling catch, and the shared stock does the damage.
**Escape (jury):** a shared limit on total effort that every captain can see and that binds (quota, season, gear rule), set by the fleet rather than against it.

## ARC-CANNED-013 (L2 · organizations) — fixes-that-fail
**Prompt:** A support team is flooded with tickets, so it closes any ticket that resembles a known issue with a canned reply. Open tickets fall by half in a week. The obvious move, when the count creeps back up, is to widen the canned-close rule. Explain why the count will keep coming back higher, and name the archetype.
**Reference:** `fixes-that-fail`. The canned close shrinks the queue now. Its delayed consequence is that users whose problems were not actually the known issue reopen, escalate, and post in public, so the volume the fix was meant to reduce returns larger, and each return invites a wider rule. The fix feeds the problem it treats.
**Confusable (capped):** `eroding-goals`. The team is not lowering a goal for support quality; it is applying a fix whose consequence enlarges the queue.
**Escape (jury):** stop the fix, accept the visible backlog once, and route the real known issues to their actual fix while answering the rest properly.

## ARC-MILK-014 (L2 · economics/markets) — escalation
**Prompt:** Two supermarkets on the same road each run a promise that they will not be beaten on price. When one cuts the price of milk, the other matches and undercuts, and the first matches back. The obvious move for each manager is to keep matching, because not matching visibly loses customers that week. Explain where this ends, and name the archetype.
**Reference:** `escalation`. Each manager's balancing loop (restore my relative price position) is the other's threat; two balancing loops make one reinforcing spiral, and each rational move ratchets both downward. It ends where one cannot pay, or where both bleed until a truce; no move inside the spiral stops it.
**Confusable (capped):** `tragedy-of-the-commons`. No shared resource is being depleted; the damage is done directly by each other's moves.
**Escape (jury):** a visible unilateral stop, or a shared boundary (a floor both can see) that ends the reading of each cut as a threat.

## ARC-GRANT-015 (L2 · social) — success-to-the-successful
**Prompt:** A city funds two youth programs from one grant pool and rewards results: next year's share follows this year's outcomes. Program A had a slightly better first year, got a larger share, hired stronger staff, and had a much better second year. The obvious move is to keep rewarding results. Explain why the city will end up with one program and no way to tell which was better, and name the archetype.
**Reference:** `success-to-the-successful`. Two reinforcing loops compete for one resource; the allocation rule feeds early success and starves the other, and the divergence measures the rule, not the programs. Rewarding results converges on one program by construction and destroys the comparison it claims to make.
**Confusable (capped):** `escalation`. The programs are not answering each other's moves; the rule answers the results.
**Escape (jury):** fund on a floor that does not depend on last year, and compare on evidence the allocation cannot manufacture.

## ARC-DONE-016 (L2 · software/infra) — eroding-goals
**Prompt:** A team's definition of done says every feature ships with tests. Under deadline, they ship one without and agree it is an exception. The next sprint has two exceptions, then the definition is edited to say tests where practical. Coverage drifts down over a year with no single decision that felt like lowering the bar. The obvious move, when the bugs arrive, is to write a stricter definition. Explain why the new definition will erode the same way, and name the archetype.
**Reference:** `eroding-goals`. Two balancing loops close the gap between the standard and reality: improving reality (slow: time, skill, scope) and lowering the standard (fast, invisible one step at a time). Under pressure the fast loop wins. A stricter definition changes the number, not the loop that erodes it.
**Confusable (capped):** `fixes-that-fail`. No fix is backfiring here; the goal itself is moving.
**Escape (jury):** anchor the goal outside the pressure: an external gate, a trend tracked against a fixed anchor, a decision-maker who does not feel the deadline.

## ARC-LATENCY-017 (L2 · AI/agent) — growth-and-underinvestment
**Prompt:** An AI assistant product grows on fast, high-quality answers. As traffic rises, the team keeps the same inference capacity and lets latency creep; retention dips, the team reads the dip as the market cooling, and it postpones the capacity purchase until growth justifies it. The obvious move is to wait for proof. Explain why the proof will never arrive, and name the archetype.
**Reference:** `growth-and-underinvestment`. The growth loop (quality → retention → growth) meets a capacity limit the team could lift. The standard for acceptable latency erodes, so the signal to invest is muted; degraded quality slows growth, and the slowed growth is read as evidence against investing. The proof the team waits for is exactly what the underinvestment prevents.
**Confusable (capped):** `limits-to-growth`. The limit is not fixed; it is a capacity the team can build and chooses to defer, and the performance standard is drifting.
**Escape (jury):** invest ahead of demand on a held standard for latency, and treat the retention dip as the signal, not the market.

## ARC-BATCHES-018 (L2 · organizations) — accidental-adversaries
**Prompt:** A retailer and its main supplier were both growing. The retailer, to smooth its cash flow, starts ordering late and in bigger batches; the supplier, seeing lumpy demand, builds inventory and raises prices to cover the holding cost; the retailer, facing higher prices, orders even later and in bigger batches to negotiate discounts. The obvious move for each is to keep protecting itself. Explain why both will lose, and name the archetype.
**Reference:** `accidental-adversaries`. Partners whose local fixes undermine each other: each fix is a rational answer to a problem the other's fix created, the overall loop is reinforcing, and neither intends harm. Both lose the relationship that was making both grow.
**Confusable (capped):** `escalation`. Neither party is trying to beat the other; each is fixing a local problem, and the harm to the partner is a side effect.
**Escape (jury):** show each side the other's local problem, and change the ordering arrangement so one side's relief stops being the other's pain.

---

## L3 — Application

## ARC-FEED-019 (L3 · social) — success-to-the-successful
**Prompt:** A video platform's feed allocates exposure by engagement: a creator whose first videos get a little lift is shown to more people, gains followers, and gets more engagement, which earns more exposure. Two creators of equal skill who started a week apart end the year with a hundredfold difference in audience, and the platform's analysts present this as proof that quality wins. Newer creators, watching the numbers, conclude the platform is saturated and stop posting. **Name the archetype, the trap it creates for the platform, and the high-leverage escape.**
**Reference:** `success-to-the-successful`. Two (in fact many) reinforcing loops compete for one resource, exposure, and the allocation rule feeds the early winner. The divergence measures the rule, not the creators.
**Trap it creates (jury, `UNCALIBRATED`):** reading the divergence as merit and doubling down on rewarding performance, which locks in the first-week accident and starves the supply of new creators the platform depends on.
**Escape (jury, `UNCALIBRATED`):** give exploration its own budget that the winners cannot capture (a reserved share of exposure allocated by something other than past engagement), so the resource is no longer routed by earlier success alone.
**Confusable (capped):** `tragedy-of-the-commons`. Attention looks like a commons, but nothing is being depleted by overuse; it is being allocated by a rule that feeds whoever already has it.

## ARC-FEEDLOT-020 (L3 · public-health) — fixes-that-fail
**Prompt:** A large cattle operation adds low-dose antibiotics to feed to keep infections down and growth up. It works: infections fall, weights rise. Over several years, the infections that do occur respond less and less to the drugs, so the operation raises the dose and adds a second antibiotic, which works for a while, and then the same thing happens. Nothing about the operation's hygiene, stocking density or veterinary care has changed in either direction. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `fixes-that-fail`. The fix (routine antibiotics) suppresses infections now; its delayed consequence (selection for resistant bacteria) enlarges the very problem it treats, and the enlarged problem calls for more of the fix.
**Trap it creates (jury, `UNCALIBRATED`):** escalating dose and drug count, each round buying less time and leaving the operation, and the region's hospitals, with infections that no available drug touches.
**Escape (jury, `UNCALIBRATED`):** stop the routine fix and change the conditions that produce infection (density, hygiene, vaccination), accepting a period of higher infection and lower weight while the resistance pressure falls.
**Confusable (capped):** `shifting-the-burden`. There is no fundamental solution being starved in the text; hygiene and care are unchanged. What distinguishes the archetype is that the fix's own consequence, resistance, makes the original problem worse.

## ARC-WELLS-021 (L3 · ecology) — tragedy-of-the-commons
**Prompt:** A valley of small farms draws irrigation from one aquifer through private wells. A subsidy lowers the cost of pumping. As the water table falls, each farmer deepens their well before the neighbor's deeper well leaves theirs dry, and the local paper describes a race to the bottom between neighbors. Each farm's yield rises for a few seasons after its well is deepened. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `tragedy-of-the-commons`. Many actors, each in a reinforcing loop of their own (pump → yield → income → pump), draw on one shared stock whose recharge is slower than the aggregate draw. The deepening looks like a race but is each farmer's rational response to a falling shared stock.
**Trap it creates (jury, `UNCALIBRATED`):** deeper wells, more pumping, a faster fall, and the reading of the collapse as the neighbors' fault; the subsidy makes every individual step cheaper and the collective step faster.
**Escape (jury, `UNCALIBRATED`):** govern the aquifer as one stock: an aggregate withdrawal cap the farmers can see and that binds (metered rights, a shared allocation), and remove the subsidy that pays for the draw.
**Confusable (capped):** `escalation`. The deepening reads like a race in which each move answers the neighbor's, but no farmer is countering a neighbor's move to hold a position; each is answering the shared stock, and the stock does the damage.

## ARC-SLO-022 (L3 · software/infra) — eroding-goals
**Prompt:** A service team commits to 99.9% monthly availability. After a bad quarter it sets a temporary target of 99.5% while the causes are fixed. The causes are never fully fixed, the temporary target is written into the runbook, and two years later the document says 99.0% with a note that customers have adapted. When a large customer complains, the team's first proposal is a new, stricter target with a dashboard. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `eroding-goals`. The gap between the standard and reality is closed by two balancing loops, improving reality (slow) and lowering the standard (fast), and the fast one has won each time. Nothing failed loudly; the goal moved.
**Trap it creates (jury, `UNCALIBRATED`):** each drift is ratified as realism, the absence of a visible failure is read as evidence the old target was excessive, and a new stricter number erodes by the same loop because the loop was never touched.
**Escape (jury, `UNCALIBRATED`):** anchor the standard outside the team that feels the pressure (a contractual floor, an external review, a fixed historical anchor the trend is plotted against) and make every change to the target a visible, dated decision rather than a note.
**Confusable (capped):** `fixes-that-fail`. No fix has backfired; the number has drifted. The distinguishing mark is that the goal, not the condition, is what keeps changing.

## ARC-VOLUME-023 (L3 · personal/behavioral) — escalation
**Prompt:** Two people who live together have the same argument most weeks. When one raises their voice, the other feels threatened and raises theirs to be heard; the first, feeling attacked, raises theirs again. Each one, asked afterwards, says they were only responding, and each remembers the other starting it. Both would rather it stopped, and both believe stopping first means losing. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `escalation`. Two balancing loops, each restoring a felt position against the other's last move, form one reinforcing spiral. Neither move is an attack from the inside; every move is a response.
**Trap it creates (jury, `UNCALIBRATED`):** the belief that stopping first is losing, which makes the only exit look like defeat and keeps both inside the spiral.
**Escape (jury, `UNCALIBRATED`):** a unilateral, visible de-escalation that is not framed as concession (lowering one's own voice as a stated choice), or a shared rule made outside the argument (a pause both agree to before the next one).
**Confusable (capped):** `accidental-adversaries`. They are partners, which invites that reading, but no local fix to a separate problem is harming the other; each move answers the other's move directly.

## ARC-TUTOR-024 (L3 · AI/agent) — shifting-the-burden
**Prompt:** A school gives every student an AI tutor that produces a worked solution on demand. Homework scores rise within a term. A year later, exam scores, taken without the tutor, have fallen, and teachers report that students no longer start a problem before asking. The school's response is more tutor time, since homework results show it works. Nothing about the tutor's answers is wrong. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `shifting-the-burden`. The symptomatic solution (the answer on demand) relieves the difficulty every time; the fundamental solution (the student's own capacity to work a problem) is slow to build and, with the symptom relieved, is no longer exercised. The burden shifts to the intervener and the fundamental capacity atrophies.
**Trap it creates (jury, `UNCALIBRATED`):** measuring the symptom (homework scores) and concluding the intervention works, which prescribes more of it as the fundamental capacity keeps shrinking.
**Escape (jury, `UNCALIBRATED`):** strengthen the fundamental solution on purpose (the tutor withholds solutions until the student has attempted, and grades the attempt) and measure the capacity, not the relieved symptom.
**Confusable (capped):** `fixes-that-fail`. The tutor does not backfire; its answers are correct and its task succeeds every time. The damage is what it displaces.

## ARC-CHARGERS-025 (L3 · economics/markets) — growth-and-underinvestment
**Prompt:** A city's electric-car adoption grew fast on the strength of a dense, reliable charging network. As adoption rose, queues at chargers lengthened; the utility, unwilling to upgrade substations before demand was proven, held its plans, and drivers learned to plan around waits. Adoption growth slowed the next year, and the utility cited the slowdown as evidence that the upgrade would have been premature. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `growth-and-underinvestment`. A reinforcing growth loop meets a capacity limit that investment could lift, but investment waits for proof, the standard for an acceptable wait erodes, and the throttled growth is read as the reason not to invest.
**Trap it creates (jury, `UNCALIBRATED`):** a self-confirming forecast: the underinvestment produces the slowdown that justifies the underinvestment, while drivers' adapted expectations hide the lost demand.
**Escape (jury, `UNCALIBRATED`):** invest ahead of demand against a held standard (a maximum queue time that triggers the upgrade), and read the slowdown as the cost of waiting rather than the market's verdict.
**Confusable (capped):** `limits-to-growth`. The limit is not external or fixed; it is capacity the utility can build, and the performance standard is drifting, which is what makes the archetype this one.

## ARC-DISCHARGE-026 (L3 · organizations) — accidental-adversaries
**Prompt:** A hospital and a nursing home have long shared a care pathway. Under bed pressure the hospital begins discharging patients earlier, with thinner handover notes, to free beds. The nursing home, receiving sicker patients it is not staffed for, tightens its admission criteria. Patients who no longer qualify stay in hospital beds, so the hospital discharges the rest even earlier. Each side now describes the other as unreasonable, and both are worse off than when the pathway worked. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `accidental-adversaries`. Two partners each apply a local fix to their own problem, each fix creates the other's next problem, and the overall loop is reinforcing. Neither meant harm; both now behave as adversaries.
**Trap it creates (jury, `UNCALIBRATED`):** each side reads the other's fix as bad faith and protects itself harder, which is the move that makes the partner's next fix necessary.
**Escape (jury, `UNCALIBRATED`):** surface each side's local problem to the other and redesign the handoff so the hospital's relief (a freed bed) is not the nursing home's burden (an unstaffed patient), for example a shared step-down capacity or a joint discharge standard.
**Confusable (capped):** `escalation`. It looks like a fight, but neither party is countering the other to hold a position; each is fixing its own problem, and the harm to the partner is the side effect.

## ARC-COWORK-027 (L3 · organizations) — limits-to-growth
**Prompt:** A coworking space grew on the strength of its community: members knew each other, made introductions, and recommended the space to friends. Growth slowed at about 150 members. The operator, reading the slowdown as a space problem, took the floor above and doubled the desks; the desks filled slowly, introductions stopped happening, and the recommendation rate fell further. **Name the archetype, the trap it creates, and the high-leverage escape.**
**Reference:** `limits-to-growth`. The reinforcing loop (community → recommendations → members) met a balancing one: past a certain size, members can no longer know each other, and the quality that drove recommendations falls with each new member. The limit is social, not physical.
**Trap it creates (jury, `UNCALIBRATED`):** treating the limit as capacity (more desks) and pushing the growth engine (marketing) against a limiting factor those moves make worse.
**Escape (jury, `UNCALIBRATED`):** act on the limiting factor itself: structure the space as several communities small enough to know each other (floors, pods, cohorts), so the loop that drove growth is restored rather than diluted.
**Confusable (capped):** `growth-and-underinvestment`. The operator's own reading, a capacity that should have been built, is the confusable; the limit here is the size at which a community stops being one, which no desk purchase lifts.
