# SystemsBench — Calibration Gold-Set INDEX

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems.**
> Tracks the gold-set population against the per-format floors in `protocols/CALIBRATION_GOLDSET.md` (§1).
> A jury is **certified** for a format only once that format clears its floor AND the §4.1 gates pass.

**Floors:** ≥30 labeled items per open format in active use · ≥120 total at v1 · 20% sealed split · balanced across L1–L4 and ≥4 domains.

## Population status

| Format | Floor | Labeled | Certified? | Notes |
|---|---|---|---|---|
| LEV   | 30 | 1 (calibrated-provisional) | NO | LEV-ORG-001 — full spread (ceiling+mid+trap), synthetic raters |
| BRIEF | 30 | 0 | NO | none authored |
| CLD   | 30 | 0 | NO | none authored |
| DYN   | 30 | 0 | NO | none authored |

## Entries

| Item | Format | Status | Raters | Exemplars | Spread | File |
|---|---|---|---|---|---|---|
| LEV-ORG-001 | LEV | CALIBRATED (PROVISIONAL) | 3 synthetic | ceiling+mid+trap | 0.94 → 0.44 → 0.03 (clean, monotonic) | calibration/gold/LEV-ORG-001.gold.md |

## Accept-rule (resolved SenseRun #5, v0.2)
The bootstrap accept-rule (§3.1) is now runnable: unanimity `Do=0 → ACCEPT`, else ≥2/3 raters within ≤1 ordinal band. Krippendorff α reserved for the set-level gate (§3.2) and judge-vs-human certification (§4.1). Quality-spread (§4.0) requires ceiling+mid+trap. **RATIFIED: August (trust-delegated) · Ember (PENDING-COUNTERSIGN).**

## Open fork (SenseRun #6) — N=3 floor weakness
At N=3 on a 3-point scale the §3.1(b) percent-agreement floor is near-unfalsifiable (pigeonhole). The gate is currently a *presence* check, not an *agreement* check. Three candidate hardenings logged in BACKLOG + SystemsBenchFuture.MD → **Meadows-#5, needs August + Ember** before reliance at scale.
