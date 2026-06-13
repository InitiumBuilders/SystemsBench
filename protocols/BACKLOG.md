# SystemsBench — BACKLOG (ranked by leverage)

Highest-leverage first. The SenseRun picks the top *feasible* item each run, or a better one surfaced by Step-2 critique. Move completed items to CHANGELOG.

## HIGH leverage (structural — change the rules/learning of the benchmark)
0. **Harden the bootstrap accept-rule at small N** *(NEW — binding constraint as of SenseRun #6; Meadows #5 STRUCTURAL → requires August + Ember, NOT self-applicable).* SenseRun #6 ran the new §3.1 rule end-to-end and proved it: at N=3 on a 3-point scale the percent-agreement floor (§3.1b) is **near-unfalsifiable** — by pigeonhole three raters on {0,0.5,1.0} always have ≥2 within one band, so 51/51 sub-criteria accepted and AMBIGUOUS-ANCHOR can essentially never fire at bootstrap. The gate is currently a *presence* check, not an *agreement* check. Three candidate hardenings (forks, NOT yet chosen): **(1)** bootstrap accept = strict unanimity OR ≥2 *identical* (not merely adjacent); **(2)** raise N to 4–5 so a split can fail the 2/3 floor; **(3)** max-spread rule — reject if any sub-criterion spans full 0↔1.0 even if 2/3 cluster. See `logs/runs/2026-05-31_run-6.md` + `SystemsBenchFuture.MD`. **← next structural SenseRun is BLOCKED on this ratification.**
1. **Replace synthetic raters with real human-council labels** on `LEV-ORG-001` (now CALIBRATED *provisional* via synthetic dry-run, full ceiling+mid+trap spread) and author the first `BRIEF`/`CLD` items, per `protocols/CALIBRATION_GOLDSET.md`. Unblocks the first end-to-end *certified* open-format score. The accept-rule is now runnable (#5 resolved the bootstrap gate); item-level labeling can proceed in parallel with the #0 N-hardening since it's additive.
2. **Programmatic CLD scorer** — auto-grade causal-loop structure (variables, signed links, R/B loop sign, dominant loop) so the `CLD` format needs minimal judge time. (Plate & Monroe + graph metrics.) Removes a subjectivity bottleneck = #6 information-flow leverage. **← NOW FEASIBLE & TOP of the additive lane (SenseRun #7 seeded 5 CLD L3 items + machine-checkable structural-oracle specs as its validation set).** Build a checker that parses a model's variable/edge/loop output, computes loop polarity = product of signed edges, and scores against each item's required-edge + loop-sign + dominant-loop expectations; calibrate against the 5 reference solutions (loop signs already verified 11/11).
3. **IRT-driven auto-pruning** — once enough responses exist, automate dropping low/negative-discrimination items each run (self-organizing quality, Meadows #4).

## MID leverage (fill coverage, strengthen loops)
4. **Seed bank to threshold** — ≥5 L3 items per format across ≥4 domains, each with reference solutions. (**SF** cleared SenseRun #2; **CLD** cleared SenseRun #7 — 5 L3 × 5 domains, deterministic structural path live.) Remaining: **DYN, ARC, TRAP, BRIEF** (zero items each); **LEV** at 1/5 L3. Next coverage pick = the format that also opens a scoring path or compounds with calibration: **DYN** pairs with the deterministic oracles (reference trajectory match, like SF) and would be the next judge-light path; **ARC/TRAP** are reference-label gradeable.
5. **First Diamond (L4) item** — one expert-validated, private, counterintuitive item per format.
6. **Faithfulness probe harness** — CoT truncation + bias-injection on `LEV`/`BRIEF` items.

## DONE (moved to CHANGELOG)
- ~~Stock-Flow (`SF`) item generator / seed~~ — SenseRun #2 (v0.3.0).
- ~~Calibration gold-set spec~~ — SenseRun #3 (v0.4.0). *Sourcing/population* promoted to #1 above.

## LOW leverage (parameters — defer unless dominant)
7. Tune dimension weights from real IRT discrimination (needs response data first).
8. Add 9th system archetype examples to `ARC` bank.

## Notes
- Always prefer the highest-leverage *feasible* item. If data isn't available yet (e.g., IRT needs responses), the dominant feasible move is usually coverage (item bank) or a structural process fix.
