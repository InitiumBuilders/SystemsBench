# SystemsBench — Item Bank INDEX & Coverage Matrix

Every item is date-stamped, tagged with format × difficulty × construct, and (for open formats) ships with a reference solution. Its **Status** is computed from evidence (see the rungs below). The SenseRun tracks holes here.

## Formats
SF (stock-flow) · CLD (causal loop mapping) · LEV (leverage ID) · DYN (dynamic prediction) · ARC (archetype) · TRAP (misperception) · BRIEF (full systems brief)

## Difficulty
L1 recognition · L2 understanding · L3 application · L4 Diamond (private, expert-validated)

## Domains
ecology · economics/markets · organizations · public-health · software/infra · social · personal/behavioral · AI/agent

## Coverage matrix (count of items; target ≥5 per format×L3 to go live, ≥20 for IRT)

| Format | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| SF    | **25** | **25** | **25** | 0 |
| CLD   | **25** | **25** | **25** | 0 |
| LEV   | **25** | **25** | **25** | 0 |
| DYN   | **25** | **25** | **25** | 0 |
| ARC   | **9** | **9** | **9** | 0 |
| TRAP  | **9** | **9** | **9** | 0 |
| BRIEF | 0 | 0 | 0 | 0 |

## Status rungs (provisional · SenseRun #12 · definitions await council ratification)

The `Status` column is **computed from evidence by `scripts/bench-audit.py`**, never typed. The script recomputes every item's earned rung and **fails** when a claim exceeds the evidence. Rungs, lowest to highest:

| Rung | Earned when |
|---|---|
| `AUTHORED` | the item is in this register with a prompt and a reference in its seed file |
| `REVIEWED` | a named second reader has signed it (`reviewed: <name>` in the File cell) |
| `ORACLE-READY` | its reference is machine-readable: an entry in `items/*_oracle.json`, or for a jury format a gold file in `calibration/gold/` (any rater source) |
| `EXECUTABLE` | ORACLE-READY **and** wired into `items/harness_prompts.json`, so elicit → parse → score runs end to end with no hand in the loop |
| `HUMAN-CALIBRATED` | a gold file with **human** labels that clears the §3.1 gate (`raters: human` in the gold file) |
| `CERTIFIED` | HUMAN-CALIBRATED **and** a live-run item statistic on file under `results/` (discrimination measured, not assumed) |

These definitions are provisional: rung names and thresholds touch the Structure and will be ratified or amended by August and Ember, not by the engine.

## Items
| ID | Format | Diff | Domain | Constructs | Date | File | Status |
|---|---|---|---|---|---|---|---|
| LEV-ORG-001 | LEV | L3 | organizations | C (leverage), B (structure-not-blame), D (resistance) | 2026-05-31 | items/seed_LEV_organizations.md · gold: PROVISIONAL (calibration/gold/LEV-ORG-001.gold.md) | ORACLE-READY |
| LEV-CARBONTAX-002 | LEV | L1 | economics/climate | C (ladder: #12 vs #5 existence) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-METER-003 | LEV | L1 | personal/infra | C (ladder: #6; Dutch meter) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-MISSION-004 | LEV | L1 | organizations | C (ladder: #3, operationalized) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-SAFETYSTOCK-005 | LEV | L1 | operations | C (ladder: #11 buffers vs #12) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-PERMIT-006 | LEV | L1 | public/infra | C (ladder: #9 delays) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-ZONING-007 | LEV | L1 | social/housing | C (ladder: #5 rules) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-ENOUGH-008 | LEV | L1 | personal/economics | C (ladder: #2 paradigm) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-TEAMS-009 | LEV | L1 | organizations | C (ladder: #4 self-organization) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-AUDIT-010 | LEV | L1 | economics/organizations | C (ladder: #8 balancing strength) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-RESHARE-011 | LEV | L1 | social/AI | C (ladder: #7 reinforcing gain) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-CAMPUS-012 | LEV | L1 | infra/organizations | C (ladder: #10 material structure) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-LENS-013 | LEV | L1 | social | C (ladder: #1 transcend paradigms) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-WATERDATA-014 | LEV | L1 | ecology/economics | C (comparison: #6 > #12) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-FLOWGOAL-015 | LEV | L1 | markets/operations | C (comparison: #3 > #11) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-HEADCOUNT-016 | LEV | L1 | organizations | C (ladder: #11/#10 capacity add) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-MINWAGE-017 | LEV | L1 | economics/social | C (rule #5 vs its level #12) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-TOUBILL-018 | LEV | L1 | personal/infra | C (ladder: #6 info flows) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-CAMERA-019 | LEV | L1 | public | C (ladder: #8; no number changed) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-OPENDATA-020 | LEV | L1 | government/social | C (ladder: #6; TRI logic) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-RATE-021 | LEV | L1 | economics | C (ladder: #12; Meadows' Fed example) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-QUOTA-022 | LEV | L1 | ecology | C (level #12 vs access rule #5) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-AMEND-023 | LEV | L1 | government | C (ladder: #4 rule-changing power) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-KPI-024 | LEV | L1 | organizations | C (ladder: #3 operative goal) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-BOOSTCAP-025 | LEV | L1 | social/AI | C (ladder: #7 gain cap) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-BANDSORT-026 | LEV | L1 | mixed | C (band classification ×3) | 2026-07-05 | items/seed_LEV_organizations.md · L1 recognition; deterministic reference | AUTHORED |
| LEV-WRONGDIR-027 | LEV | L2 | economics/social | C (right lever, wrong direction; growth) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-PARAMWHY-028 | LEV | L2 | organizations | C (why #12 is weak; threshold exception) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-RESIST-029 | LEV | L2 | social/organizations | C, D (high leverage ↔ most resistance) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-DELAYS-030 | LEV | L2 | operations | C (#9 direction: shorten vs lengthen) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-BUFFERCOST-031 | LEV | L2 | operations/economics | C (#11 tradeoffs; when right) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-METERWHY-032 | LEV | L2 | personal/infra | C (#6 mechanism: loop vs exhortation), B | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-RULESWHY-033 | LEV | L2 | ecology/economics | C (#5 > #12; fishery rules vs level) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-GOALWHY-034 | LEV | L2 | organizations | C (#3; operative-goal tell) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-SELFORG-035 | LEV | L2 | organizations/social | C (#4; control vs adaptability) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-PARADIGMSHIFT-036 | LEV | L2 | social | C (#2; Kuhn/Meadows shift method) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-PUSHBACK-037 | LEV | L2 | public-health/social | C, D (policy resistance; demand-side leverage) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-GASTAX-038 | LEV | L2 | public/climate | C (direction check: subsidizing the problem loop) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-GAINVSBRAKE-039 | LEV | L2 | social/AI | C (#7 vs #8: gain beats brake) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-COMMONS-040 | LEV | L2 | ecology/economics | C (commons ranking: #5>#6>#12>exhortation) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-GOODHART-041 | LEV | L2 | organizations | C (Goodhart in ladder terms; fix at #3) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-REORG-042 | LEV | L2 | organizations | C (#10 without #6/#5/#3 underdelivers) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-TECHFIX-043 | LEV | L2 | infra/ecology | C (when tech is #12 vs #9/#6/#4) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-PRICEWAR-044 | LEV | L2 | markets | C (escalation; change the game #3/#5) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-THRESHOLD-045 | LEV | L2 | public-health/economics | C (when #12 IS the lever: dominance flip) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-INVISIBLE-046 | LEV | L2 | software/organizations | C, B (bounded rationality; #6 fixes decisions) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-INCENTPLACE-047 | LEV | L2 | organizations | C (#5 rule shape beats #12 amount) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-SUBOPT-048 | LEV | L2 | organizations/government | C (sub-optimization; fix at #3 goal hierarchy) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-DISSOLVE-049 | LEV | L2 | public/infra | C (Ackoff resolve/solve/dissolve classification) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-TRANSCEND-050 | LEV | L2 | social | C (#1 operationally; anti-dogma) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-DEFAULTS-051 | LEV | L2 | public-health | C (defaults #5 > feedback #6 > posters) | 2026-07-05 | items/seed_LEV_organizations.md · L2 understanding; deterministic core | AUTHORED |
| LEV-HOSP-052 | LEV | L3 | public-health/organizations | C (downstream constraint; Goodhart target), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-FISHERY-053 | LEV | L3 | ecology/economics | C (subsidy wrong-direction; #5 access rules), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-SCHOOL-054 | LEV | L3 | social/education | C (proxy→goal corruption; #3 re-anchor), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-TRAFFIC-055 | LEV | L3 | public/infra | C (induced demand; #5/#6 pricing), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-CHURN-056 | LEV | L3 | markets/SaaS | C (adverse selection; brake-vs-source; #3), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-NURSE-057 | LEV | L3 | organizations/public-health | C (overtime wrong-direction; #5 ratios + #4), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-DEBT-058 | LEV | L3 | personal/economics | C (self-binding rules #5 vs rate #12), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-FEED-059 | LEV | L3 | social/AI | C (#7 gain now, #3 objective real lever), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-AQUIFER-060 | LEV | L3 | ecology | C (subsidy accelerant; #6 metering + #5 caps), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-ONCALL-061 | LEV | L3 | software/infra | C (capability trap; protected-time rule #5), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-HOMELESS-062 | LEV | L3 | social/housing | C (buffer vs flows; Housing-First #5 on #2), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-ANDON-063 | LEV | L3 | operations | C (source vs downstream; stop-the-line #5/#4), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-GROWTH-064 | LEV | L3 | organizations/markets | C (goal itself mis-set; #3 renegotiation), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-CLASSROOM-065 | LEV | L3 | social/behavioral | C (alienation loop; restorative #4/#6), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-STEWARD-066 | LEV | L3 | public-health | C (commons; stewardship #5+#6 on paradigm #2), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-GRID-067 | LEV | L3 | infra/climate | C (missing feedback makes the peak; #6/#5 tariff), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-BULLWHIP-068 | LEV | L3 | operations/markets | C (bullwhip; POS sharing #6 + VMI #5), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-WILDFIRE-069 | LEV | L3 | ecology | C (strengthened #8 as the trap; burns on #2), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-OPIOID-070 | LEV | L3 | public-health | C (balloon effect; proxy-vs-goal; treatment #5 on #2), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-SURVEIL-071 | LEV | L3 | organizations | C (inverted #6; outcomes #3 + autonomy #4), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-PROXY-072 | LEV | L3 | AI/agent | C (spec-gaming arms race; objective layer #3, #9 asymmetry), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-OVERTOUR-073 | LEV | L3 | economics/social | C (sub-threshold #12; rental rules #5; goal #3), D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-YOYO-074 | LEV | L3 | personal/behavioral | C (intensity wrong-direction; environment #5 + goal #3), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| LEV-BACKLOG-075 | LEV | L3 | government/organizations | C (outflow structure #10/#5; defensive-filing loop), B, D | 2026-07-05 | items/seed_LEV_organizations.md · jury UNCALIBRATED (no gold yet) | AUTHORED |
| SF-RES-001 | SF | L1 | ecology | A (stock/flow), D (BOT) | 2026-05-31 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-BANK-002 | SF | L2 | economics | A, D, reinforcing-loop | 2026-05-31 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-CO2-003 | SF | L3 | public-health/climate | A, D, inflow>outflow | 2026-05-31 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-INV-004 | SF | L2 | operations | A (integrate flows) | 2026-05-31 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-TRUST-005 | SF | L3 | social/behavioral | A, D, nonlinearity, delay | 2026-05-31 | items/seed_SF_stockflow.md | AUTHORED |
| SF-BATH-006 | SF | L1 | personal/water | A (stock/flow classification) | 2026-07-03 | items/seed_SF_stockflow.md | AUTHORED |
| SF-ACCT-007 | SF | L1 | economics | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-POP-008 | SF | L1 | ecology/social | A, D (net-flow); trap: both-flows-nonzero≠steady | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-WARE-009 | SF | L1 | operations | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-INBOX-010 | SF | L1 | software/infra | A, D (queue net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-FOREST-011 | SF | L1 | ecology | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-LABEL-012 | SF | L1 | organizations | A (stock/flow classification) | 2026-07-03 | items/seed_SF_stockflow.md | AUTHORED |
| SF-BATT-013 | SF | L1 | personal/tech | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-STEADY-014 | SF | L1 | ecology/water | A, D (balanced flows → steady) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-LOAN-015 | SF | L1 | economics | A, D (net-flow; stock vs cumulative flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-DRAW-016 | SF | L1 | ecology/water | A, D (net-flow; positive inflow, still falling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-ROOM-017 | SF | L1 | public-health | A (classification) + D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | AUTHORED |
| SF-SNOW-018 | SF | L1 | ecology | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-MEM-019 | SF | L1 | AI/agent | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-TODO-020 | SF | L1 | personal/behavioral | A, D (queue net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-CUST-021 | SF | L1 | organizations/markets | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-DISK-022 | SF | L1 | software/infra | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-POND-023 | SF | L1 | ecology/fisheries | A, D (net-flow, falling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-FOLLOW-024 | SF | L1 | social | A, D (net-flow, falling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-HEAT-025 | SF | L1 | personal/infra | A (stock/flow classification) | 2026-07-03 | items/seed_SF_stockflow.md | AUTHORED |
| SF-QUEUE-026 | SF | L1 | AI/agent | A, D (queue net-flow, falling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-RAIN-027 | SF | L1 | ecology/water | A, D (net-flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SUB-028 | SF | L1 | markets | A, D (balanced churn → steady) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-BED-029 | SF | L1 | public-health | A, D (net-flow, falling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-HIRE-030 | SF | L2 | organizations | A, D, correlation-heuristic (falling flow, rising stock) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-PEAK-031 | SF | L2 | ecology/water | A, D (peak = net-flow zero crossing) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-TICKET-032 | SF | L2 | software/infra | A, D (unbounded queue growth) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-CASH-033 | SF | L2 | organizations | A, D (runway = stock / net flow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-STEADYK-034 | SF | L2 | ecology/water | A, D (steady state, stock-proportional outflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SAVE-035 | SF | L2 | personal/finance | A, D, reinforcing (compounding) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-PAYOFF-036 | SF | L2 | economics | A, D (payment vs interest; contrast SF-BANK-002) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-CHURN-037 | SF | L2 | social | A, D (steady state, proportional churn) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-OVERFLOW-038 | SF | L2 | ecology/water | A, D (time-to-threshold) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-BAC-039 | SF | L2 | personal/health | A, D (peak when inflow stops) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-AQUI-040 | SF | L2 | ecology/economics | A, D (rising outflow crosses inflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-INVWK-041 | SF | L2 | operations | A, D (integrate schedule + find peak) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-RIVER-042 | SF | L2 | ecology/water | A, D, correlation-heuristic (declining inflow, still rising) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-HEATER-043 | SF | L2 | personal/infra | A, D (steady-state temperature) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-CACHE-044 | SF | L2 | software/infra | A, D (steady state, proportional eviction) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-AGENT-045 | SF | L2 | AI/agent | A, D, correlation-heuristic (decreasing inflow, rising stock) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-WEIGHT-046 | SF | L2 | personal/behavioral | A, D, correlation-heuristic (shrinking surplus, rising fat) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-COHORT-047 | SF | L2 | organizations | A, D (steady-state headcount) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-DAM-048 | SF | L2 | ecology/water | A, D (integrate + threshold crossing) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-EMISS-049 | SF | L2 | public-health/ecology | A, D (proportional sink → steady state) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SALES-050 | SF | L2 | operations/markets | A, D (rising outflow crosses inflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-COOL-051 | SF | L2 | software/infra | A, D (rising load crosses cooling) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-POND2-052 | SF | L2 | ecology/fisheries | A, D (integrate + find low) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-EMISSDROP-053 | SF | L3 | climate | A, D, correlation-heuristic + mechanism (declining inflow > outflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-MOMENTUM-054 | SF | L3 | public-health/social | A, D, delay (demographic momentum) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-DEFICIT-055 | SF | L3 | economics | A, D, correlation-heuristic (deficit flow vs debt stock) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-AQUIFER-056 | SF | L3 | ecology | A, D (matching flows holds, doesn't restore; irreversibility) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-FISHSET-057 | SF | L3 | ecology/fisheries | A, D (flow tuned to wrong stock; state-dependent inflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-TEMPCOMMIT-058 | SF | L3 | climate | A, D (temperature tracks cumulative stock) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-TECHDEBT-059 | SF | L3 | software/infra | A, D (state-dependent inflow overtakes constant outflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-PIPELINE-060 | SF | L3 | operations | A, D, delay (supply-line → overshoot) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-PLASTIC-061 | SF | L3 | ecology | A, D (positive inflow, ~zero outflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-RETIRE-062 | SF | L3 | personal/finance | A, D, reinforcing (stock-dependent inflow, break-even) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-OCEANHEAT-063 | SF | L3 | climate | A, D, delay (forcing → temperature lag) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SKILL-064 | SF | L3 | personal/behavioral | A, D (constant inflow, proportional outflow → plateau) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-RESIST-065 | SF | L3 | public-health | A, D (reduced inflow can't drain a no-outflow stock) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-AGENTERR-066 | SF | L3 | AI/agent | A, D (halved inflow, no pruning → still rising) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-HOUSING-067 | SF | L3 | economics/markets | A, D, delay (long build lag → boom-bust overshoot) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-WEALTH-068 | SF | L3 | economics/social | A, D, reinforcing (proportional returns → divergence) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-PENSION-069 | SF | L3 | economics | A, D (both flows state-dependent on shifting stocks) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-RESERVOIR-070 | SF | L3 | ecology/water | A, D, correlation-heuristic (leveling inflow above outflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-FORESTC-071 | SF | L3 | ecology | A, D, delay (worse-before-better; delayed inflow) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-GLUCOSE-072 | SF | L3 | public-health | A, D, delay (delayed corrective outflow → overshoot) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SILT-073 | SF | L3 | infra/ecology | A, D (small constant inflow, no outflow → irreversible) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-SAAS-074 | SF | L3 | markets | A, D (churn ceiling; proportional outflow → asymptote) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| SF-GRID-075 | SF | L3 | software/infra | A, D, delay (lagged control signal → oscillation) | 2026-07-03 | items/seed_SF_stockflow.md | EXECUTABLE |
| CLD-FISH-001 | CLD | L3 | ecology/fisheries | A (loops/polarity/delay), B, D (dominant-loop shift) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live | EXECUTABLE |
| CLD-EPI-002 | CLD | L3 | public-health | A, B, D (R1→B1+B3 shift, 2nd wave) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live | EXECUTABLE |
| CLD-ORG-003 | CLD | L3 | organizations | A, B (eroding-goals; two balancing loops) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live | EXECUTABLE |
| CLD-INFRA-004 | CLD | L3 | software/infra | A, B, D (capability trap; B1 short / R1 long) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live | EXECUTABLE |
| CLD-MKT-005 | CLD | L3 | economics/markets | A, D (delay-driven oscillation; hog cycle) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live | EXECUTABLE |
| CLD-SAVINGS-006 | CLD | L1 | economics | A (loop polarity R) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-COFFEE-007 | CLD | L1 | personal | A (loop polarity B), D (goal-seeking) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-RUMOR-008 | CLD | L1 | social | A (loop polarity R), D (growth) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-MORALE-009 | CLD | L1 | organizations | A (two-negatives → R; the parity trap) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-RABBIT-010 | CLD | L1 | ecology | A (link sign −) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-EXERCISE-011 | CLD | L1 | personal-health | A (link sign −) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-THERMO-012 | CLD | L1 | software/infra | A (loop polarity B) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-DEBT-013 | CLD | L1 | economics | A (loop polarity R; compounding) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-RECESSION-014 | CLD | L1 | economics | A (R via two + links; amplifies both ways) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-VALVE-015 | CLD | L1 | ecology/water | A (loop polarity B), D (goal-seeking) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-COUNT-016 | CLD | L1 | software/infra | A (count loops; R+B) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-SIGNS3-017 | CLD | L1 | organizations | A (classify from signs → B) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-SIGNS4-018 | CLD | L1 | markets | A (classify from signs → R) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-SIGNS2NEG-019 | CLD | L1 | software/infra | A (two-negatives → R; parity) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-POPGROWTH-020 | CLD | L1 | ecology | A (R), D (exponential growth) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-CROWD-021 | CLD | L1 | social | A (loop polarity B; self-limiting) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-MUSCLE-022 | CLD | L1 | personal-health | A (loop polarity R; virtuous) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-CLOUD-023 | CLD | L1 | climate | A (link sign −) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-VIRAL-024 | CLD | L1 | AI/social | A (R), D (viral growth) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-PREDATOR-025 | CLD | L1 | ecology | A (link sign −) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-HABIT-026 | CLD | L1 | personal/behavioral | A (loop polarity R) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-BUDGET-027 | CLD | L1 | organizations | A (loop polarity B) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-INFECT-028 | CLD | L1 | public-health | A (R), D (exponential growth early) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-BRAKE-029 | CLD | L1 | software/infra | A (loop polarity B; goal-seeking) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-DROUGHT-030 | CLD | L1 | ecology | A (link sign −) | 2026-07-04 | items/seed_CLD_causalloops.md · L1 recognition; inline oracle | AUTHORED |
| CLD-COMPOUND-031 | CLD | L2 | economics | A (R), D (exponential vs linear) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-DEATHSPIRAL-032 | CLD | L2 | organizations | A (R via two −), D (accelerating decline) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-GOALSEEK-033 | CLD | L2 | personal | A (B), D (goal-seeking asymptote) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-PENDULUM-034 | CLD | L2 | ecology | A (B + delay), D (oscillation) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-LIMITS-035 | CLD | L2 | markets | A (R+B), D (S-curve); limits-to-growth | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-STEER-036 | CLD | L2 | software/infra | A (B + delay), D (overshoot/oscillation) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-PAINKILLER-037 | CLD | L2 | public-health | A (B + delayed R); fixes-that-fail | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-CAP-038 | CLD | L2 | economics | A (R capped by B), D (equilibrium) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-NETPOL4-039 | CLD | L2 | software/infra | A (net polarity → B), D (goal-seeking) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-ARMS-040 | CLD | L2 | social | A (coupled R); escalation | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-SATURATE-041 | CLD | L2 | markets | A (R+B), D (peak-plateau); limits-to-growth | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-RUN-042 | CLD | L2 | economics | A (R via two −), D (fast collapse) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-HERD-043 | CLD | L2 | public-health | A (R+B), D (rise-peak-decline) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-VIRTUOUS-044 | CLD | L2 | organizations | A (R), D (compounding; reversible) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-INVENTORY-045 | CLD | L2 | operations | A (B + supply delay), D (oscillation; beer game) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-EQUIL-046 | CLD | L2 | economics | A (B, no delay), D (converges); delay contrast | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-CAFFEINE-047 | CLD | L2 | personal/behavioral | A (B + delayed R); shifting-the-burden | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-NETPOL5-048 | CLD | L2 | ecology | A (net polarity, two − → R), D (amplify) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-NETWORK-049 | CLD | L2 | markets/AI | A (R network effects), D (growth/reversal) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-GENTRIFY-050 | CLD | L2 | social | A (R), B (structure-not-blame), D (accelerating) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-FEVER-051 | CLD | L2 | public-health | A (B), D (goal-seeking recovery) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-TRUST-052 | CLD | L2 | social | A (R), D (virtuous/vicious; reversible) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-PROCRAST-053 | CLD | L2 | personal/behavioral | A (R via all +), D (self-accelerating) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-CARRYING-054 | CLD | L2 | ecology | A (R+B), D (logistic/S-curve; overshoot) | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-WORKAROUND-055 | CLD | L2 | software/infra | A (B + delayed R); fixes-that-fail | 2026-07-04 | items/seed_CLD_causalloops.md · L2 understanding; inline oracle | AUTHORED |
| CLD-ADOPT-056 | CLD | L3 | economics/markets | A, D (dominant shift R→B); limits-to-growth | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-BURDEN-057 | CLD | L3 | organizations | A, D (shift B1→R1); shifting-the-burden | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-COMMONS-058 | CLD | L3 | ecology/economics | A, B, D (shift R→B collapse); tragedy-of-commons | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-SUCCESS-059 | CLD | L3 | organizations | A, D (reinforcing coupling lock-in); success-to-successful | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-FIX-060 | CLD | L3 | economics | A, D (shift B1→R1); fixes-that-fail | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-ESCAL-061 | CLD | L3 | economics/markets | A, D (R escalation + delayed B brakes); escalation | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-TRAFFIC-062 | CLD | L3 | public/infra | A, D (shift B→R); induced demand | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-BURNOUT-063 | CLD | L3 | organizations/public-health | A, B, D (R spiral outruns delayed B hiring) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-ALBEDO-064 | CLD | L3 | climate/ecology | A, D (shift B→R at tipping point); ice-albedo | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-BANKRUN-065 | CLD | L3 | economics | A, B, D (R run vs delayed B backstop) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-HVAC-066 | CLD | L3 | infra/personal | A, D (delay-driven oscillation; single B loop) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-PREDPREY-067 | CLD | L3 | ecology | A, D (delay-driven oscillation; Lotka-Volterra) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-WAGEPRICE-068 | CLD | L3 | economics | A, D (R spiral + delayed B brake); wage-price | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-OUTRAGE-069 | CLD | L3 | social/AI | A, B, D (R amplification + delayed B fatigue) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-RESIST-070 | CLD | L3 | public-health | A, D (shift B1→R1); fixes-that-fail (resistance) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-UNDERINVEST-071 | CLD | L3 | organizations | A, D (weak/delayed B2 → B1 dominates); growth-and-underinvestment | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-DIET-072 | CLD | L3 | personal-health | A, D (shift B1→R1); fixes-that-fail (yo-yo) | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-EUTROPH-073 | CLD | L3 | ecology | A, D (shift external→R internal-loading); hysteresis | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-HYPE-074 | CLD | L3 | markets/AI | A, D (shift R→B, delayed overshoot); hype cycle | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| CLD-SKILL-075 | CLD | L3 | personal/behavioral | A, D (shift R→B); diminishing-returns plateau | 2026-07-04 | items/seed_CLD_causalloops.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-FISH-001 | DYN | L3 | ecology/fisheries | D (overshoot-and-collapse), A (delay), B | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live | EXECUTABLE |
| DYN-SHOWER-002 | DYN | L3 | personal/behavioral | D (delay-driven oscillation), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live | EXECUTABLE |
| DYN-ADOPT-003 | DYN | L3 | economics/markets | D (S-shaped saturation; limits to growth), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live | EXECUTABLE |
| DYN-CAPTRAP-004 | DYN | L3 | organizations | D (better-before-worse; capability trap), A, B | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live | EXECUTABLE |
| DYN-CLIMATE-005 | DYN | L3 | public-health/climate | D (delayed-rise-to-plateau; stock-flow), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live | EXECUTABLE |
| DYN-SAVINGS-006 | DYN | L1 | economics | D (exponential-growth) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-BACTERIA-007 | DYN | L1 | public-health/ecology | D (exponential-growth) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-DEBT-008 | DYN | L1 | economics | D (exponential-growth) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-TUMOR-009 | DYN | L1 | public-health | D (exponential-growth) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-HARE-010 | DYN | L1 | ecology | D (exponential-growth) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-FILL-011 | DYN | L1 | ecology/water | D (goal-seeking); trap oscillation | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-CHARGE-012 | DYN | L1 | personal/tech | D (goal-seeking); trap exponential | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-HEATER-013 | DYN | L1 | software/infra | D (goal-seeking); trap oscillation | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-CRUISE-014 | DYN | L1 | software/infra | D (goal-seeking, returns to setpoint) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-COFFEE-015 | DYN | L1 | personal | D (goal-seeking, cooling) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-DRAIN-016 | DYN | L1 | ecology/water | D (goal-seeking, draining) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-WOM-017 | DYN | L1 | economics/markets | D (s-shaped); trap exponential | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-SKILL-018 | DYN | L1 | personal/behavioral | D (s-shaped) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-EPIDEMIC-019 | DYN | L1 | public-health | D (s-shaped; susceptible depletion) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-MEME-020 | DYN | L1 | social/AI | D (s-shaped) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-THERMOSTAT-021 | DYN | L1 | software/infra | D (oscillation; delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-PREDPREY-022 | DYN | L1 | ecology | D (oscillation; maturation delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-INVENTORY-023 | DYN | L1 | operations | D (oscillation; supply delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-YEAST-024 | DYN | L1 | ecology | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-DEER-025 | DYN | L1 | ecology | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-ALGAE-026 | DYN | L1 | ecology | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-SUGAR-027 | DYN | L1 | personal-health | D (better-before-worse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-CRAM-028 | DYN | L1 | personal/behavioral | D (better-before-worse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-STIMULANT-029 | DYN | L1 | public-health | D (better-before-worse) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-FAD-030 | DYN | L1 | economics/markets | D (overshoot-and-decline) | 2026-07-05 | items/seed_DYN_dynamics.md · L1 recognition; verified oracle-ready | AUTHORED |
| DYN-EMITSLOW-031 | DYN | L2 | public-health/climate | D (delayed-rise-to-plateau; correlation heuristic) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-RESERVOIR-032 | DYN | L2 | ecology/water | D (delayed-rise-to-plateau; correlation heuristic) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-STEROID-033 | DYN | L2 | public-health | D (better-before-worse) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-CONTRACTOR-034 | DYN | L2 | organizations | D (better-before-worse; shifting-the-burden) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-PATCH-035 | DYN | L2 | software/infra | D (better-before-worse; tech debt) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-LAUNCH-036 | DYN | L2 | economics/markets | D (s-shaped; blitz front-loads) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-FISHTECH-037 | DYN | L2 | ecology/fisheries | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-AUTOSCALE-038 | DYN | L2 | software/infra | D (oscillation; delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-BEERGAME-039 | DYN | L2 | operations | D (oscillation; supply delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-HOUSING-040 | DYN | L2 | economics/markets | D (oscillation; construction delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-RETIRE-041 | DYN | L2 | economics | D (exponential-growth; compounding) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-VIRALGLOBAL-042 | DYN | L2 | markets/AI | D (exponential-growth; early phase) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-TIPPING-043 | DYN | L2 | public-health/climate | D (exponential/runaway; ice-albedo) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-PLATEAU-044 | DYN | L2 | personal/behavioral | D (s-shaped; diminishing returns) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-TREATFAIL-045 | DYN | L2 | public-health | D (better-before-worse; resistance) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-TRAFFIC-046 | DYN | L2 | public/infra | D (better-before-worse; induced demand) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-POND-047 | DYN | L2 | ecology | D (goal-seeking; proportional sink) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-CACHE-048 | DYN | L2 | software/infra | D (goal-seeking; proportional eviction) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-COMMODITY-049 | DYN | L2 | economics/markets | D (oscillation; construction delay) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-GLUCOSE-050 | DYN | L2 | public-health | D (oscillation; delayed insulin) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-INVASIVE-051 | DYN | L2 | ecology | D (s-shaped; logistic) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-STARTUP-052 | DYN | L2 | organizations | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-SOIL-053 | DYN | L2 | ecology/economics | D (better-before-worse; soil degradation) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-MRR-054 | DYN | L2 | economics/markets | D (goal-seeking; churn ceiling) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-MOMENTUM-055 | DYN | L2 | public-health/social | D (delayed-rise-to-plateau; demographic momentum) | 2026-07-05 | items/seed_DYN_dynamics.md · L2 understanding; verified oracle-ready | AUTHORED |
| DYN-GROUNDWATER-056 | DYN | L3 | ecology/economics | D (overshoot-and-collapse; commons) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-TOURISM-057 | DYN | L3 | economics/social | D (overshoot-and-collapse) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-GRAZING-058 | DYN | L3 | ecology | D (overshoot-and-collapse; commons) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-AGENTLOOP-059 | DYN | L3 | AI/agent | D (oscillation; stale reward signal) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-SALESFORCE-060 | DYN | L3 | organizations | D (oscillation; ramp-up delay) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-COBWEB-061 | DYN | L3 | economics/markets | D (oscillation; production lag) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-ANTIBIOTIC-062 | DYN | L3 | public-health | D (better-before-worse; resistance) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-IRRIGATION-063 | DYN | L3 | ecology/economics | D (better-before-worse; salinization) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-STIMULUSDEBT-064 | DYN | L3 | economics | D (better-before-worse; debt overhang) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-PESTICIDE-065 | DYN | L3 | ecology | D (better-before-worse; pesticide treadmill) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-EV-066 | DYN | L3 | economics/markets | D (s-shaped; subsidy front-loads) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-REFOREST-067 | DYN | L3 | ecology | D (s-shaped; logistic) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-PLASTIC-068 | DYN | L3 | ecology | D (delayed-rise-to-plateau; ~zero outflow) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-HEATCOMMIT-069 | DYN | L3 | public-health/climate | D (delayed-rise-to-plateau; thermal inertia) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-NUCLEAR-070 | DYN | L3 | public-health/social | D (delayed-rise-to-plateau; no outflow) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-PERMAFROST-071 | DYN | L3 | public-health/climate | D (exponential/runaway; methane feedback) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-MISINFO-072 | DYN | L3 | social/AI | D (exponential/runaway; engagement loop) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-AQUIFERMATCH-073 | DYN | L3 | ecology | D (goal-seeking holds, not restores) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-BUBBLE-074 | DYN | L3 | economics/markets | D (overshoot-and-collapse; speculative bubble) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| DYN-BUREAUCRACY-075 | DYN | L3 | organizations | D (better-before-worse; over-correction) | 2026-07-05 | items/seed_DYN_dynamics.md · verified oracle-ready; jury UNCALIBRATED | AUTHORED |
| ARC-INVITE-001 | ARC | L1 | software/infra | D3 (archetype: limits-to-growth), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-SLEEP-002 | ARC | L1 | personal/behavioral | D3 (archetype: shifting-the-burden), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-GRAZE-003 | ARC | L1 | ecology | D3 (archetype: tragedy-of-the-commons), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-DEADLINE-004 | ARC | L1 | organizations | D3 (archetype: fixes-that-fail), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-CREDITS-005 | ARC | L1 | economics/markets | D3 (archetype: escalation), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-STREAM-006 | ARC | L1 | social | D3 (archetype: success-to-the-successful), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-WAIT-007 | ARC | L1 | public-health | D3 (archetype: eroding-goals), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-TELEHEALTH-008 | ARC | L1 | organizations | D3 (archetype: growth-and-underinvestment), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-PLANNER-009 | ARC | L1 | AI/agent | D3 (archetype: accidental-adversaries), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-SYNTH-010 | ARC | L2 | social | D3 (archetype: limits-to-growth), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-DENTAL-011 | ARC | L2 | public-health | D3 (archetype: shifting-the-burden), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-SONAR-012 | ARC | L2 | ecology | D3 (archetype: tragedy-of-the-commons), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-CANNED-013 | ARC | L2 | organizations | D3 (archetype: fixes-that-fail), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-MILK-014 | ARC | L2 | economics/markets | D3 (archetype: escalation), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-GRANT-015 | ARC | L2 | social | D3 (archetype: success-to-the-successful), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-DONE-016 | ARC | L2 | software/infra | D3 (archetype: eroding-goals), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-LATENCY-017 | ARC | L2 | AI/agent | D3 (archetype: growth-and-underinvestment), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-BATCHES-018 | ARC | L2 | organizations | D3 (archetype: accidental-adversaries), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-FEED-019 | ARC | L3 | social | D3 (archetype: success-to-the-successful), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-FEEDLOT-020 | ARC | L3 | public-health | D3 (archetype: fixes-that-fail), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-WELLS-021 | ARC | L3 | ecology | D3 (archetype: tragedy-of-the-commons), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-SLO-022 | ARC | L3 | software/infra | D3 (archetype: eroding-goals), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-VOLUME-023 | ARC | L3 | personal/behavioral | D3 (archetype: escalation), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-TUTOR-024 | ARC | L3 | AI/agent | D3 (archetype: shifting-the-burden), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-CHARGERS-025 | ARC | L3 | economics/markets | D3 (archetype: growth-and-underinvestment), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-DISCHARGE-026 | ARC | L3 | organizations | D3 (archetype: accidental-adversaries), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| ARC-COWORK-027 | ARC | L3 | organizations | D3 (archetype: limits-to-growth), A (loops), C (the escape) | 2026-09-27 | items/seed_ARC_archetypes.md · trap + escape UNCALIBRATED; label oracle live | EXECUTABLE |
| TRAP-CO2-001 | TRAP | L1 | public-health/climate | misperception: stock-flow; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-THERMO-002 | TRAP | L1 | personal/behavioral | misperception: delay; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-WEED-003 | TRAP | L1 | ecology | misperception: exponential; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-HIGHWAY-004 | TRAP | L1 | social | misperception: policy-resistance; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-BACK-005 | TRAP | L1 | personal/behavioral | misperception: worse-before-better; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-LINE-006 | TRAP | L1 | organizations | misperception: local-optimum; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-PARKING-007 | TRAP | L1 | economics/markets | misperception: wrong-direction; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-RIVER-008 | TRAP | L1 | ecology | misperception: threshold; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-BEERGAME-009 | TRAP | L1 | organizations | misperception: attribution; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-DEFICIT-010 | TRAP | L2 | economics/markets | misperception: stock-flow; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-CAPACITY-011 | TRAP | L2 | software/infra | misperception: delay; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-USERS-012 | TRAP | L2 | software/infra | misperception: exponential; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-BOUNTY-013 | TRAP | L2 | social | misperception: policy-resistance; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-FIXCURVE-014 | TRAP | L2 | software/infra | misperception: worse-before-better; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-WARDS-015 | TRAP | L2 | public-health | misperception: local-optimum; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-GROWTH-016 | TRAP | L2 | economics/markets | misperception: wrong-direction; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-HEADROOM-017 | TRAP | L2 | software/infra | misperception: threshold; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-ROSTER-018 | TRAP | L2 | public-health | misperception: attribution; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-HEADCOUNT-019 | TRAP | L3 | organizations | misperception: stock-flow; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-DOSE-020 | TRAP | L3 | public-health | misperception: delay; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-OUTBREAK-021 | TRAP | L3 | public-health | misperception: exponential; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-WILDFIRE-022 | TRAP | L3 | ecology | misperception: policy-resistance; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-TWOPOLICIES-023 | TRAP | L3 | economics/markets | misperception: worse-before-better; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-AGENTS-024 | TRAP | L3 | AI/agent | misperception: local-optimum; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-VOLUNTEERS-025 | TRAP | L3 | organizations | misperception: wrong-direction; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-LAKE-026 | TRAP | L3 | ecology | misperception: threshold; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |
| TRAP-RETRIES-027 | TRAP | L3 | AI/agent | misperception: attribution; B (structure-not-blame); faithfulness probe (4.5) | 2026-09-28 | items/seed_TRAP_misperceptions.md · reasoning UNCALIBRATED; answer + probe oracle live | EXECUTABLE |

## Holes flagged (post-SenseRun #10)
**TRAP seeded 9/9/9 across L1–L3, born executable, with the faithfulness probe** (2026-09-28, SenseRun #16). Nine misperception families (stock-flow, delay, exponential, policy-resistance, worse-before-better, local-optimum, wrong-direction, threshold, attribution), each once per level, across all eight domains; closed options with the intuitive option as the trap (capped 0.25). **The probe (Structure §4.5) is live:** the harness renders every item a second time with one fixed hint sentence toward the trap, `engine/trap-score.py score_pair` reports flipped / acknowledged and a faithfulness label in {faithful, mixed, unfaithful}, and `engine/bench-run.py` runs TRAP items as pairs and reports the axis separately, never averaged in. Reasoning stays jury-graded, `UNCALIBRATED — not scored`. Remaining unseeded: BRIEF.
**ARC seeded 9/9/9 across L1–L3, born executable** (2026-09-27, SenseRun #14). Every one of the nine Structure §2.3 archetypes appears once per level, across all eight domains. L1 = a clean scenario, name the archetype; L2 = the scenario plus the obvious move, explain why it fails and name the archetype; L3 = a novel scenario whose surface resembles a different archetype: name it, the trap it creates, the escape. **Deterministic path live on day one:** `engine/arc-score.py` + `items/arc_oracle.json` (label match with an alias table; the item's named confusable capped at 0.25; a same-family label 0.5), wired into `engine/harness.py`. The trap-and-escape portion is the jury's and ships `UNCALIBRATED — not scored`. Remaining unseeded: TRAP, BRIEF. The fill of ARC to 25 per level is the coverage lever, not this run's.
**LEV filled to 25/25/25 across L1–L3** (2026-07-05, direct authoring task — 74 items added to the existing 1; not a numbered SenseRun). LEV is the **jury-graded open format**, so this fill differs from SF/CLD/DYN in kind: **L1 (recognition)** = place an intervention on **Meadows' 12-point ladder** (or compare two) — deterministic reference answers (correct rung 1.0 / correct band 0.5; bands: parametric #12–#9 · feedback/info #8–#6 · design #5–#3 · paradigm #2–#1); **L2 (understanding)** = why the ladder orders as it does (parameter trap, wrong-direction pushes, policy resistance, Goodhart, gain-vs-brake, threshold exception) — deterministic core + mechanism; **L3 (application)** = 24 new full scenarios in the LEV-ORG-001 mold (map structure → rank on ladder → highest-*feasible* + direction check → dynamics + resistance), most embedding a **wrong-direction move** in the status quo (subsidized drilling, resolution bonuses, suppression-only fire policy, monitoring-as-goal). **Calibration status (fail-closed):** only LEV-ORG-001 has gold (PROVISIONAL); the 24 new L3 are **UNCALIBRATED — not scored** until each clears a §4.0 quality-spread; **no deterministic scorer exists for LEV** (no machine verification was possible, unlike CLD/DYN — the L1/L2 reference answers would support a future `lev-score` rung/band/direction lane, flagged not built). Domains span all 8. No IRT yet.
**DYN filled to 25/25/25 across L1–L3** (2026-07-05, direct authoring task — 70 items added to the existing 5; not a numbered SenseRun). Introduces the **L1 (recognition)** and **L2 (understanding)** tiers DYN lacked: L1 = name the fundamental mode of a clean single-structure system (exponential / goal-seeking / oscillation / overshoot-and-collapse …); L2 = predict the mode when a delay, a finite limit, an accumulating stock, or a slow side-effect makes the naive smooth answer wrong. All **70 new items carry auto-checkable trajectory oracles verified against the live `engine/dyn-score.py`**: mode↔feature consistency **187/187** by code, each reference round-trips to 1.0, wrong-mode-right-endpoint caps at 0.5, trap trajectory ≤0.25 (488/488 scratch checks). **Wiring status (honest):** only the original 5 L3 are in `items/dyn_oracle.json` + `items/harness_prompts.json`; the 70 new are **oracle-ready but not yet wired**. Unlike CLD, **no scorer change is needed** — the DYN scorer is **level-agnostic** (it grades mode+features for L1/L2/L3 uniformly), so wiring is a purely additive `dyn_oracle.json` + `harness_prompts.json` extension flagged for a follow-up SenseRun. DYN **jury/mechanism stays `UNCALIBRATED — not scored`** (unchanged). Domains span all 8 (incl. AI/agent, e.g. DYN-AGENTLOOP-059). No IRT discrimination measured yet.
**CLD filled to 25/25/25 across L1–L3** (2026-07-04, direct authoring task — 70 items added to the existing 5; not a numbered SenseRun). Introduces the **L1 (recognition)** and **L2 (understanding)** tiers CLD lacked: L1 = read a link sign / classify a small loop R↔B (loop sign = product of edges; the two-negatives→R parity insight) / name a behavior mode; L2 = explain the behavior over time a small (1–2 loop, sometimes delayed) structure produces + name the archetype. The **20 new L3 items** are full structural-mapping tasks whose reference solutions were **verified deterministically consistent against the live `engine/cld-score.py`** (loop signs **41/41** = product of edges; each round-trips to 1.0; partial 0.5; dominant-loop mislabel ≤0.25). **Wiring status (honest):** only the original 5 L3 are in `items/cld_oracle.json` + `items/harness_prompts.json`; the 20 new L3 are **oracle-ready but not yet wired** (that + bumping the scorer self-test loop-count = a small gated engine step for a follow-up SenseRun), and the **L1/L2 tier is not yet in the auto-scorer** (the scorer's insight-gate is L3-tuned — it would cap a perfect L1/L2 answer at 0.5 — so L1/L2 need a small recognition/behavior-mode rubric extension). CLD **jury/completeness stays `UNCALIBRATED — not scored`** (unchanged). Domains span all 8. No IRT discrimination measured yet.
**SF filled to 25/25/25 across L1–L3** (2026-07-03, direct authoring task — 70 items added to the existing 5; not a numbered SenseRun). SF is now the **first format past the §3.3 ≥20-item IRT-stable count** — 25 per level, every level ≥20. Coverage spread across all 8 domains (ecology · economics/markets · organizations · public-health/climate · software/infra · social · personal/behavioral · AI/agent). Deterministic-only (numeric/shape/classification oracle inline in the item file; **no jury** — SF was never jury-graded, so no calibration gate applies). The named-trap-rate (Sweeney-Sterman correlation heuristic) is logged per item. **No IRT discrimination measured yet** — that needs a live run; item quality is authored-not-validated until then.
**Harness bridge live (SenseRun #10)** — `engine/harness.py` + `items/harness_prompts.json` make the **CLD + DYN deterministic lanes runnable end-to-end against a live model**: `template` elicits the canonical structured schema, `parse` turns a raw (fenced/prose-wrapped) reply into the `resp.json` the scorers consume, **failing closed** (`PARSE_ERROR — not scored`) on unparseable/malformed input. Construct-neutral (no item/weight/oracle change); self-test 61/61. The robustness precondition for any live CLD/DYN run; CLD/DYN **jury** sub-scores still `UNCALIBRATED — not scored`. Semantic variable *aliasing* held open as a fork for August + Ember (not built — would leak the oracle).
**DYN L3 cleared** (0 → 5 across 5 domains, SenseRun #9) — DYN's **deterministic trajectory path** meets the §3.3 ≥5-per-format×L3 go-live threshold and is **machine-executable** (`engine/dyn-score.py` + `items/dyn_oracle.json`): the response's behavior mode + features (`overshoot`/`oscillation`/`delay_dominant`/`eventual_direction`) are matched against the 5 reference trajectories (self-test 34/34; oracle mode↔feature consistency 13/13 by code). **First auto-graded surface for Dimension D**, and a **third executable judge-independent path** (cf. SF numeric/shape, CLD structural). Its **jury/mechanism path stays `UNCALIBRATED — not scored`** until a DYN gold set clears §3.1/§4.0 (fail-closed).
**CLD L3 cleared** (0 → 5 across 5 domains, SenseRun #7) — CLD's **deterministic structural path** is machine-executable (`engine/cld-score.py` + `items/cld_oracle.json`, SenseRun #8): loop polarity recomputed as product of signed edges, scored against the 5 reference solutions (self-test 31/31; loop signs 11/11 by code). Its **jury/completeness path stays `UNCALIBRATED — not scored`** until a CLD gold set clears §3.1/§4.0 (fail-closed). Still empty: **ARC, TRAP, BRIEF** (zero items). SF (2026-07-03), CLD (2026-07-04), DYN (2026-07-05), and LEV (2026-07-05) all cleared to 25/25/25 across L1–L3 — four formats past the ≥20-item IRT-stable count; ARC/TRAP/BRIEF are now the only empty formats. Backlog #4 (seed bank to threshold) remains the standing coverage fill; the SenseRun fills the highest-leverage hole each run.
