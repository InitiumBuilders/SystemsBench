# Jury re-score report — LEV-ORG-001 quality-spread · N=5 synthetic raters vs recorded N=3 baseline

## CEILING
| Sub | N=3 labels | N=3 med | N=5 labels | N=5 med | med match | base@3 | base@5 | fork1@5 | fork3@5 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A2 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A3 | 0.5,1,0.5 | 0.5 | 0.5,1,1,1,1 | 1 | DIFF | ACCEPT | ACCEPT-WINDOW | ACCEPT-IDENTICAL | ACCEPT-WINDOW |
| A4 | 0.5,0.5,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B1 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B2 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C1 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C2 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C3 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C4 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C5 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D1 | 0.5,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D2 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D3 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E1 | 1,1,1 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E2 | 0.5,1,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E3 | 1,1,0.5 | 1 | 1,1,1,1,1 | 1 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |

Dimensions (N=3 -> N=5): A 0.75->0.875 · B 1->1 · C 1->1 · D 1->1 · E 0.833->0.833
Composite (N=3 -> N=5): **0.925 -> 0.953**  (delta +0.028)
Krippendorff alpha @N=5 (ordinal): A: alpha=0.774 (75% unanimous) · B: undef(perfect) (100% unanimous) · C: undef(perfect) (100% unanimous) · D: undef(perfect) (100% unanimous) · E: alpha=1.000 (100% unanimous)

## MID
| Sub | N=3 labels | N=3 med | N=5 labels | N=5 med | med match | base@3 | base@5 | fork1@5 | fork3@5 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 0.5,0.5,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A2 | 0.5,1,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A3 | 0,0.5,0 | 0 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A4 | 0,0.5,0.5 | 0.5 | 0,0,0,0,0 | 0 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B1 | 0.5,1,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B2 | 1,1,0.5 | 1 | 1,1,0.5,1,1 | 1 | = | ACCEPT | ACCEPT-WINDOW | ACCEPT-IDENTICAL | ACCEPT-WINDOW |
| C1 | 0.5,0.5,0.5 | 0.5 | 0,0.5,0,0.5,0 | 0 | DIFF | ACCEPT | ACCEPT-WINDOW | AMBIGUOUS-ANCHOR | ACCEPT-WINDOW |
| C2 | 0.5,0.5,0.5 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C3 | 0.5,1,0.5 | 0.5 | 1,1,1,1,1 | 1 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C4 | 0,0,0 | 0 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C5 | 0.5,0.5,0 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D1 | 0,0.5,0.5 | 0.5 | 0.5,1,1,0.5,1 | 1 | DIFF | ACCEPT | ACCEPT-WINDOW | AMBIGUOUS-ANCHOR | ACCEPT-WINDOW |
| D2 | 0,0.5,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D3 | 0.5,0.5,0.5 | 0.5 | 0,0,0,0,0 | 0 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E1 | 0,0.5,0 | 0 | 0,0.5,0.5,0,0 | 0 | = | ACCEPT | ACCEPT-WINDOW | AMBIGUOUS-ANCHOR | ACCEPT-WINDOW |
| E2 | 0.5,0.5,0.5 | 0.5 | 0.5,0.5,0,0,0 | 0 | DIFF | ACCEPT | ACCEPT-WINDOW | AMBIGUOUS-ANCHOR | ACCEPT-WINDOW |
| E3 | 0.5,0.5,0 | 0.5 | 0.5,0.5,0.5,0.5,0.5 | 0.5 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |

Dimensions (N=3 -> N=5): A 0.375->0.375 · B 0.75->0.75 · C 0.4->0.5 · D 0.333->0.333 · E 0.333->0.167
Composite (N=3 -> N=5): **0.438 -> 0.448**  (delta +0.010)
Krippendorff alpha @N=5 (ordinal): A: alpha=1.000 (100% unanimous) · B: alpha=0.625 (50% unanimous) · C: alpha=0.836 (80% unanimous) · D: alpha=0.955 (67% unanimous) · E: alpha=0.222 (33% unanimous)

## TRAP
| Sub | N=3 labels | N=3 med | N=5 labels | N=5 med | med match | base@3 | base@5 | fork1@5 | fork3@5 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 0,0.5,0.5 | 0.5 | 0,0,0,0,0 | 0 | DIFF | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A2 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A3 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| A4 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B1 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| B2 | 0,0.5,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C1 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C2 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C3 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C4 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| C5 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D1 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D2 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| D3 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E1 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E2 | 0,0,0 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |
| E3 | 0,0,0.5 | 0 | 0,0,0,0,0 | 0 | = | ACCEPT | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY | ACCEPT-UNANIMITY |

Dimensions (N=3 -> N=5): A 0.125->0 · B 0->0 · C 0->0 · D 0->0 · E 0->0
Composite (N=3 -> N=5): **0.028 -> 0**  (delta -0.028)
Krippendorff alpha @N=5 (ordinal): A: undef(perfect) (100% unanimous) · B: undef(perfect) (100% unanimous) · C: undef(perfect) (100% unanimous) · D: undef(perfect) (100% unanimous) · E: undef(perfect) (100% unanimous)

## Accept-rule falsifiability summary (51 sub-criteria across the spread)
| Rule | AMBIGUOUS @N=3 | AMBIGUOUS @N=5 |
|---|---|---|
| base §3.1 | 0/51 | 0/51 |
| fork1 identical | 0/51 | 4/51 |
| fork3 max-spread | 0/51 | 0/51 |

Median-label agreement N=5 vs N=3 gold: 41/51 (80%) sub-criteria identical.
