# SystemsBench — Item Bank INDEX & Coverage Matrix

Every item is date-stamped, tagged with format × difficulty × construct, and (for open formats) ships with a reference solution. The SenseRun tracks holes here.

## Formats
SF (stock-flow) · CLD (causal loop mapping) · LEV (leverage ID) · DYN (dynamic prediction) · ARC (archetype) · TRAP (misperception) · BRIEF (full systems brief)

## Difficulty
L1 recognition · L2 understanding · L3 application · L4 Diamond (private, expert-validated)

## Domains
ecology · economics/markets · organizations · public-health · software/infra · social · personal/behavioral · AI/agent

## Coverage matrix (count of items; target ≥5 per format×L3 to go live, ≥20 for IRT)

| Format | L1 | L2 | L3 | L4 |
|---|---|---|---|---|
| SF    | 1 | 2 | 2 | 0 |
| CLD   | 0 | 0 | **5** | 0 |
| LEV   | 0 | 0 | 1 | 0 |
| DYN   | 0 | 0 | **5** | 0 |
| ARC   | 0 | 0 | 0 | 0 |
| TRAP  | 0 | 0 | 0 | 0 |
| BRIEF | 0 | 0 | 0 | 0 |

## Items
| ID | Format | Diff | Domain | Constructs | Date | File |
|---|---|---|---|---|---|---|
| LEV-ORG-001 | LEV | L3 | organizations | C (leverage), B (structure-not-blame), D (resistance) | 2026-05-31 | items/seed_LEV_organizations.md · gold: PROVISIONAL (calibration/gold/LEV-ORG-001.gold.md) |
| SF-RES-001 | SF | L1 | ecology | A (stock/flow), D (BOT) | 2026-05-31 | items/seed_SF_stockflow.md |
| SF-BANK-002 | SF | L2 | economics | A, D, reinforcing-loop | 2026-05-31 | items/seed_SF_stockflow.md |
| SF-CO2-003 | SF | L3 | public-health/climate | A, D, inflow>outflow | 2026-05-31 | items/seed_SF_stockflow.md |
| SF-INV-004 | SF | L2 | operations | A (integrate flows) | 2026-05-31 | items/seed_SF_stockflow.md |
| SF-TRUST-005 | SF | L3 | social/behavioral | A, D, nonlinearity, delay | 2026-05-31 | items/seed_SF_stockflow.md |
| CLD-FISH-001 | CLD | L3 | ecology/fisheries | A (loops/polarity/delay), B, D (dominant-loop shift) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live |
| CLD-EPI-002 | CLD | L3 | public-health | A, B, D (R1→B1+B3 shift, 2nd wave) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live |
| CLD-ORG-003 | CLD | L3 | organizations | A, B (eroding-goals; two balancing loops) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live |
| CLD-INFRA-004 | CLD | L3 | software/infra | A, B, D (capability trap; B1 short / R1 long) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live |
| CLD-MKT-005 | CLD | L3 | economics/markets | A, D (delay-driven oscillation; hog cycle) | 2026-06-13 | items/seed_CLD_causalloops.md · jury portion UNCALIBRATED; structural oracle live |
| DYN-FISH-001 | DYN | L3 | ecology/fisheries | D (overshoot-and-collapse), A (delay), B | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live |
| DYN-SHOWER-002 | DYN | L3 | personal/behavioral | D (delay-driven oscillation), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live |
| DYN-ADOPT-003 | DYN | L3 | economics/markets | D (S-shaped saturation; limits to growth), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live |
| DYN-CAPTRAP-004 | DYN | L3 | organizations | D (better-before-worse; capability trap), A, B | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live |
| DYN-CLIMATE-005 | DYN | L3 | public-health/climate | D (delayed-rise-to-plateau; stock-flow), A | 2026-06-13 | items/seed_DYN_dynamics.md · jury portion UNCALIBRATED; trajectory oracle live |

## Holes flagged (post-SenseRun #10)
**Harness bridge live (SenseRun #10)** — `engine/harness.py` + `items/harness_prompts.json` make the **CLD + DYN deterministic lanes runnable end-to-end against a live model**: `template` elicits the canonical structured schema, `parse` turns a raw (fenced/prose-wrapped) reply into the `resp.json` the scorers consume, **failing closed** (`PARSE_ERROR — not scored`) on unparseable/malformed input. Construct-neutral (no item/weight/oracle change); self-test 61/61. The robustness precondition for any live CLD/DYN run; CLD/DYN **jury** sub-scores still `UNCALIBRATED — not scored`. Semantic variable *aliasing* held open as a fork for August + Ember (not built — would leak the oracle).
**DYN L3 cleared** (0 → 5 across 5 domains, SenseRun #9) — DYN's **deterministic trajectory path** meets the §3.3 ≥5-per-format×L3 go-live threshold and is **machine-executable** (`engine/dyn-score.py` + `items/dyn_oracle.json`): the response's behavior mode + features (`overshoot`/`oscillation`/`delay_dominant`/`eventual_direction`) are matched against the 5 reference trajectories (self-test 34/34; oracle mode↔feature consistency 13/13 by code). **First auto-graded surface for Dimension D**, and a **third executable judge-independent path** (cf. SF numeric/shape, CLD structural). Its **jury/mechanism path stays `UNCALIBRATED — not scored`** until a DYN gold set clears §3.1/§4.0 (fail-closed).
**CLD L3 cleared** (0 → 5 across 5 domains, SenseRun #7) — CLD's **deterministic structural path** is machine-executable (`engine/cld-score.py` + `items/cld_oracle.json`, SenseRun #8): loop polarity recomputed as product of signed edges, scored against the 5 reference solutions (self-test 31/31; loop signs 11/11 by code). Its **jury/completeness path stays `UNCALIBRATED — not scored`** until a CLD gold set clears §3.1/§4.0 (fail-closed). Still empty: **ARC, TRAP, BRIEF** (zero items); **LEV** at 1/5 L3. SF L3 thin (2/5). No format yet at the ≥20-item IRT-stable count. Backlog #4 (seed bank to threshold) remains the standing coverage fill; the SenseRun fills the highest-leverage hole each run.
