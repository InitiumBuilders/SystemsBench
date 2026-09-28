# DRY RUN — adapter `reference` — 2026-09-28

**This measures the instrument, not any AI.** The `reference` adapter replays the scorers' own builders through the real template → parse → score path. Every item must score 1.0 with zero parse errors; anything less is a defect in the harness or a scorer.

Instrument at run time: CLD calibrate calibrate: 36/36 checks passed · DYN calibrate calibrate: 34/34 checks passed · SF calibrate calibrate: 450/450 checks passed · ARC calibrate calibrate: 334/334 checks passed · harness selftest selftest: 649/649 checks passed · spec v0.15.0 · after SenseRun #14.

## By lane

| lane | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| `CLD` | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| `DYN` | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| `SF` | 70 | 70 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| `ARC` | 27 | 27 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| **all** | 107 | 107 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |

## By level

| level | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| L1 | 30 | 30 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| L2 | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| L3 | 43 | 43 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |

## By domain

| domain | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| AI/agent | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| climate | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| ecology | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| ecology/economics | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| ecology/fisheries | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| ecology/social | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| ecology/water | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| economics | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| economics/markets | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| economics/social | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| infra/ecology | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| markets | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| operations | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| operations/markets | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| organizations | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| organizations/markets | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/behavioral | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/finance | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/health | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/infra | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/tech | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| public-health | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| public-health/climate | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| public-health/ecology | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| public-health/social | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| social | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| software/infra | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |

Jury dimensions: `UNCALIBRATED — not scored`. Files: `scores.csv` (per item), `replies/` (raw replies), `run.json`.
