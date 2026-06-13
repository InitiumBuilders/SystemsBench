# SystemsBench — BACKLOG (ranked by leverage)

Highest-leverage first. The SenseRun picks the top *feasible* item each run, or a better one surfaced by Step-2 critique. Move completed items to CHANGELOG.

## HIGH leverage (structural — change the rules/learning of the benchmark)
0. **Harden the bootstrap accept-rule at small N** *(NEW — binding constraint as of SenseRun #6; Meadows #5 STRUCTURAL → requires August + Ember, NOT self-applicable).* SenseRun #6 ran the new §3.1 rule end-to-end and proved it: at N=3 on a 3-point scale the percent-agreement floor (§3.1b) is **near-unfalsifiable** — by pigeonhole three raters on {0,0.5,1.0} always have ≥2 within one band, so 51/51 sub-criteria accepted and AMBIGUOUS-ANCHOR can essentially never fire at bootstrap. The gate is currently a *presence* check, not an *agreement* check. Three candidate hardenings (forks, NOT yet chosen): **(1)** bootstrap accept = strict unanimity OR ≥2 *identical* (not merely adjacent); **(2)** raise N to 4–5 so a split can fail the 2/3 floor; **(3)** max-spread rule — reject if any sub-criterion spans full 0↔1.0 even if 2/3 cluster. See `logs/runs/2026-05-31_run-6.md` + `SystemsBenchFuture.MD`. **← next structural SenseRun is BLOCKED on this ratification.**
1. **Replace synthetic raters with real human-council labels** on `LEV-ORG-001` (now CALIBRATED *provisional* via synthetic dry-run, full ceiling+mid+trap spread) and author the first `BRIEF`/`CLD` items, per `protocols/CALIBRATION_GOLDSET.md`. Unblocks the first end-to-end *certified* open-format score. The accept-rule is now runnable (#5 resolved the bootstrap gate); item-level labeling can proceed in parallel with the #0 N-hardening since it's additive.
3. **IRT-driven auto-pruning** — once enough responses exist, automate dropping low/negative-discrimination items each run (self-organizing quality, Meadows #4).

## MID leverage (fill coverage, strengthen loops)
4. **Seed bank to threshold** — ≥5 L3 items per format across ≥4 domains, each with reference solutions. (**SF** cleared SenseRun #2; **CLD** cleared SenseRun #7 — 5 L3 × 5 domains, deterministic structural path live + auto-graded since #8.) Remaining: **DYN, ARC, TRAP, BRIEF** (zero items each); **LEV** at 1/5 L3. Next coverage pick = the format that also opens a scoring path or compounds with calibration: **DYN** pairs with the deterministic oracles (reference trajectory match, like SF) and would be the next judge-light path; **ARC/TRAP** are reference-label gradeable. **← top of the additive lane now that the CLD scorer is built.**
5. **CLD response-parsing / node-alias layer + harness prompt template** *(NEW — SenseRun #8).* The programmatic CLD scorer (`engine/cld-score.py`) grades a *structured* response and normalizes case/space/punctuation + tolerates reverse-direction edges and full-word loop types, but a live model may emit synonym variable names ("fish stock" vs "FishPopulation") that undercount variable/edge recall. Build a prompt template that elicits the canonical structured schema and an alias-mapping step before scoring — the robustness step before a live CLD run.
6. **First Diamond (L4) item** — one expert-validated, private, counterintuitive item per format.
7. **Faithfulness probe harness** — CoT truncation + bias-injection on `LEV`/`BRIEF` items.

## DONE (moved to CHANGELOG)
- ~~Stock-Flow (`SF`) item generator / seed~~ — SenseRun #2 (v0.3.0).
- ~~Calibration gold-set spec~~ — SenseRun #3 (v0.4.0). *Sourcing/population* promoted to #1 above.
- ~~Programmatic CLD scorer~~ — SenseRun #8 (v0.6.0). `engine/cld-score.py` + `items/cld_oracle.json`: loop polarity = product of signed edges, scored against the 5 reference solutions; fail-closed self-test 31/31 (loop signs 11/11 by code). CLD is now a second *executable* judge-independent path; jury/completeness still `UNCALIBRATED`.

## LOW leverage (parameters — defer unless dominant)
8. Tune dimension weights from real IRT discrimination (needs response data first).
9. Add 9th system archetype examples to `ARC` bank.
10. **Calibrate the CLD scorer's policy constants** *(NEW — SenseRun #8)* — the component weights (0.50/0.30/0.20) and the dominant-mislabel trap cap (0.25) in `engine/cld-score.py` are defaults implementing the item-file prose; tune against a real score distribution once a live-model CLD run exists.

## Notes
- Always prefer the highest-leverage *feasible* item. If data isn't available yet (e.g., IRT needs responses), the dominant feasible move is usually coverage (item bank) or a structural process fix.
