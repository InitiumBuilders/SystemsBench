# SystemsBench — ANTI-PATTERNS (what the engine learned NOT to do)

Recurring rejections from the Idea Advancement Gate become documented anti-patterns here, so the rubric self-learns. Empty at genesis; grows as the engine runs.

## Benchmark design anti-patterns (seeded from the literature)
- **Silent uncalibrated averaging.** (Learned SenseRun #3.) Reporting an open-format dimension (or rolling it into a composite) when its jury has not cleared the §5.1 gate. Always fail-closed: mark `UNCALIBRATED — not scored`, never impute or average. A number that looks scored but isn't calibrated is worse than no number.
- **Single-path-to-a-number through an uncalibrated component.** (Learned SenseRun #2.) If every route to a score depends on one not-yet-validated component (e.g., the jury), the benchmark has a hidden single point of failure. Maintain ≥2 independent scoring paths (auto-graded SF + calibrated jury).
- **The parameter trap on ourselves.** Spending a SenseRun nudging a weight by 0.01 when a coverage hole or construct-validity gap is the dominant lever. (Meadows #12 — lowest leverage.)
- **Slogan-leverage items.** Items whose "correct" answer is just naming #1/#2 ("change the paradigm") — these reward verbiage, not insight. A good item makes the obvious answer the trap.
- **Holistic 1–10 judging.** Un-anchored scalar judging is unreliable; always decompose into anchored per-dimension criteria.
- **Same-family judging.** Never grade a candidate with a judge from its own model family (self-preference bias).
- **One-number reporting.** Collapsing to a scalar without the dimension vector + CIs hides the real signal and invites Goodharting.
- **Static memorizable items.** Un-templated, un-dated items leak into training sets and rot. Date-stamp + templatize.
- **Averaging faithfulness in.** Faithfulness is a separate axis; averaging it into the composite hides unfaithful-but-fluent reasoning.

- **α-as-an-accept-gate at bootstrap scale.** (Learned SenseRun #4.) Per-item Krippendorff α is dominated by category prevalence, not raw agreement; unanimous dimensions yield α undefined (0/0) and skewed-marginal dimensions yield α≈0 despite high agreement. Never use a flat per-item α threshold as the accept gate at small N. Special-case unanimity (Do=0 → accept), add a percent-agreement floor, and reserve α for the **set-level** gate once each format clears its item floor. Changing the accept-rule itself is a Meadows-#5 structural change → August + Ember.

## Engine anti-patterns
- **Batch thrashing.** More than one change per run defeats reversibility and attribution. One move.
- **Silent edits.** Any change not in a run log + CHANGELOG is a protocol violation.
- **Self-approving structural changes.** Construct/invariant changes require August + a second check.
