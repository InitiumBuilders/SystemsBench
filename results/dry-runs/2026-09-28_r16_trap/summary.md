# DRY RUN — adapter `trap` — 2026-09-28

**This measures the instrument, not any AI.** The `trap` adapter replays the scorers' own builders through the real template → parse → score path. Each item's named naive answer is replayed; the scores show the caps the traps enforce. Items without a trap builder replay the reference and are noted.

Instrument at run time: CLD calibrate calibrate: 36/36 checks passed · DYN calibrate calibrate: 34/34 checks passed · SF calibrate calibrate: 450/450 checks passed · ARC calibrate calibrate: 334/334 checks passed · TRAP calibrate calibrate: 389/389 checks passed · harness selftest selftest: 922/922 checks passed · spec v0.16.0 · after SenseRun #15.

## By lane

| lane | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| `CLD` | 5 | 5 | 0 | 0 | 0.250 | 0.250 | 0.25 | 5 |
| `DYN` | 5 | 5 | 0 | 0 | 0.190 | 0.250 | 0.10 | 5 |
| `SF` | 70 | 70 | 0 | 0 | 0.218 | 0.250 | 0.00 | 64 |
| `ARC` | 27 | 27 | 0 | 0 | 0.250 | 0.250 | 0.25 | 27 |
| `TRAP` | 27 | 27 | 0 | 0 | 0.250 | 0.250 | 0.25 | 27 |
| **all** | 134 | 134 | 0 | 0 | 0.231 | 0.250 | 0.00 | 128 |

## By level

| level | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| L1 | 39 | 39 | 0 | 0 | 0.250 | 0.250 | 0.25 | 39 |
| L2 | 43 | 43 | 0 | 0 | 0.308 | 0.250 | 0.00 | 37 |
| L3 | 52 | 52 | 0 | 0 | 0.153 | 0.250 | 0.00 | 52 |

## By domain

| domain | items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |
|---|---|---|---|---|---|---|---|---|
| AI/agent | 9 | 9 | 0 | 0 | 0.222 | 0.250 | 0.00 | 9 |
| climate | 3 | 3 | 0 | 0 | 0.000 | 0.000 | 0.00 | 3 |
| ecology | 13 | 13 | 0 | 0 | 0.192 | 0.250 | 0.00 | 13 |
| ecology/economics | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| ecology/fisheries | 5 | 5 | 0 | 0 | 0.170 | 0.250 | 0.00 | 5 |
| ecology/social | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| ecology/water | 9 | 9 | 0 | 0 | 0.250 | 0.250 | 0.00 | 8 |
| economics | 6 | 6 | 0 | 0 | 0.167 | 0.250 | 0.00 | 6 |
| economics/markets | 10 | 10 | 0 | 0 | 0.225 | 0.250 | 0.00 | 10 |
| economics/social | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| infra/ecology | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| markets | 2 | 2 | 0 | 0 | 0.250 | 0.250 | 0.25 | 2 |
| operations | 4 | 4 | 0 | 0 | 0.375 | 0.250 | 0.00 | 3 |
| operations/markets | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| organizations | 15 | 15 | 0 | 0 | 0.273 | 0.250 | 0.00 | 14 |
| organizations/markets | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| personal/behavioral | 8 | 8 | 0 | 0 | 0.219 | 0.250 | 0.00 | 8 |
| personal/finance | 2 | 2 | 0 | 0 | 0.125 | 0.125 | 0.00 | 2 |
| personal/health | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| personal/infra | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 1.00 | 0 |
| personal/tech | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| public-health | 11 | 11 | 0 | 0 | 0.205 | 0.250 | 0.00 | 11 |
| public-health/climate | 3 | 3 | 0 | 0 | 0.167 | 0.250 | 0.00 | 3 |
| public-health/ecology | 1 | 1 | 0 | 0 | 0.250 | 0.250 | 0.25 | 1 |
| public-health/social | 1 | 1 | 0 | 0 | 0.000 | 0.000 | 0.00 | 1 |
| social | 8 | 8 | 0 | 0 | 0.344 | 0.250 | 0.25 | 7 |
| software/infra | 15 | 15 | 0 | 0 | 0.250 | 0.250 | 0.00 | 14 |

## Faithfulness probe (Structure §4.5) — reported separately, never averaged in

Each TRAP item was asked twice: as written, and with one fixed note from a colleague pointing at the trap. `flipped` = right alone, different with company; `unfaithful` = flipped toward the note and never mentioned it.

| level | items | faithful | mixed | unfaithful | probe errors | flipped toward the note |
|---|---|---|---|---|---|---|
| L1 | 9 | 9 | 0 | 0 | 0 | 0 |
| L2 | 9 | 9 | 0 | 0 | 0 | 0 |
| L3 | 9 | 9 | 0 | 0 | 0 | 0 |
| **all** | 27 | 27 | 0 | 0 | 0 | 0 |

## Notes

6 item(s): `SF-INV-004` no trap builder; reference replayed; `SF-STEADYK-034` no trap builder; reference replayed; `SF-CHURN-037` no trap builder; reference replayed; `SF-HEATER-043` no trap builder; reference replayed; `SF-CACHE-044` no trap builder; reference replayed; `SF-COHORT-047` no trap builder; reference replayed

Jury dimensions: `UNCALIBRATED — not scored`. Files: `scores.csv` (per item), `replies/` (raw replies), `run.json`.
