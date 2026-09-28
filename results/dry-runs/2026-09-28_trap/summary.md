# DRY RUN — adapter `trap` — 2026-09-28

**This measures the instrument, not any AI.** The `trap` adapter replays the scorers' own builders through the real template → parse → score path. Each item's named naive answer is replayed; the scores show the caps the traps enforce. Items without a trap builder replay the reference and are noted.

Instrument at run time: CLD calibrate calibrate: 36/36 checks passed · DYN calibrate calibrate: 34/34 checks passed · SF calibrate calibrate: 450/450 checks passed · ARC calibrate calibrate: 334/334 checks passed · harness selftest selftest: 649/649 checks passed · spec v0.15.0 · after SenseRun #14.

## By lane

| lane | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| `CLD` | 5 | 5 | 0 | 0 | 0.250 | 0.250 | 0.25 | 5 |
| `DYN` | 5 | 5 | 0 | 0 | 0.190 | 0.250 | 0.10 | 5 |
| `SF` | 70 | 70 | 0 | 0 | 0.218 | 0.250 | 0.00 | 64 |
| `ARC` | 27 | 27 | 0 | 0 | 0.250 | 0.250 | 0.25 | 27 |
| **all** | 107 | 107 | 0 | 0 | 0.226 | 0.250 | 0.00 | 101 |

## By level

| level | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| L1 | 30 | 30 | 0 | 0 | 0.250 | 0.250 | 0.25 | 30 |
| L2 | 34 | 34 | 0 | 0 | 0.324 | 0.250 | 0.00 | 28 |
| L3 | 43 | 43 | 0 | 0 | 0.133 | 0.250 | 0.00 | 43 |

## By domain

| domain | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| AI/agent | 7 | 7 | 0 | 0 | 0.214 | 0.250 | 0.00 | 7 |
| climate | 3 | 3 | 0 | 0 | 0.000 | 0.000 | 0.00 | 3 |
| ecology | 9 | 9 | 0 | 0 | 0.167 | 0.250 | 0.00 | 9 |
| ecology/economics | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| ecology/fisheries | 5 | 5 | 0 | 0 | 0.170 | 0.250 | 0.00 | 5 |
| ecology/social | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| ecology/water | 9 | 9 | 0 | 0 | 0.250 | 0.250 | 0.00 | 8 |
| economics | 6 | 6 | 0 | 0 | 0.167 | 0.250 | 0.00 | 6 |
| economics/markets | 6 | 6 | 0 | 0 | 0.208 | 0.250 | 0.00 | 6 |
| economics/social | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| infra/ecology | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| markets | 2 | 2 | 0 | 0 | 0.250 | 0.250 | 0.25 | 2 |
| operations | 4 | 4 | 0 | 0 | 0.375 | 0.250 | 0.00 | 3 |
| operations/markets | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| organizations | 11 | 11 | 0 | 0 | 0.282 | 0.250 | 0.00 | 10 |
| organizations/markets | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| personal/behavioral | 6 | 6 | 0 | 0 | 0.208 | 0.250 | 0.00 | 6 |
| personal/finance | 2 | 2 | 0 | 0 | 0.125 | 0.125 | 0.00 | 2 |
| personal/health | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| personal/infra | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/tech | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| public-health | 7 | 7 | 0 | 0 | 0.179 | 0.250 | 0.00 | 7 |
| public-health/climate | 2 | 2 | 0 | 0 | 0.125 | 0.125 | 0.00 | 2 |
| public-health/ecology | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| public-health/social | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| social | 6 | 6 | 0 | 0 | 0.375 | 0.250 | 0.25 | 5 |
| software/infra | 11 | 11 | 0 | 0 | 0.250 | 0.250 | 0.00 | 10 |

## Notes

6 item(s): `SF-INV-004` no trap builder; reference replayed; `SF-STEADYK-034` no trap builder; reference replayed; `SF-CHURN-037` no trap builder; reference replayed; `SF-HEATER-043` no trap builder; reference replayed; `SF-CACHE-044` no trap builder; reference replayed; `SF-COHORT-047` no trap builder; reference replayed

Jury dimensions: `UNCALIBRATED — not scored`. Files: `scores.csv` (per item), `replies/` (raw replies), `run.json`.
