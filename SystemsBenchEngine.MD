# SystemsBenchEngine — The Recursive Self-Improvement Engine

### How `Davara /SystemsBenchSenseRun` makes the next enhancement, every time.

> **Led by Ember Seoni & August Domanchuk. Operated by Outlier.Systems.**
> This file is the *procedure*. `SystemsBenchStructure.MD` is the *spec*. `SystemsBenchResearch.MD` is the *memory*.

**Version:** v0.1 · **Trigger:** `Davara /SystemsBenchSenseRun` · **Invariant:** one bounded, reversible, logged, gated enhancement per run.

---

## 0. Mental model of the engine

The engine treats **SystemsBench itself as a system** and applies SystemsBench's own thinking to it:
- The **item bank, rubric, judges, and weights** are stocks.
- **SenseRuns** are the flow that changes them.
- **Calibration tests** are the balancing feedback loop that keeps quality in bounds.
- **The backlog + anti-pattern ledger** are the information flows.
- The **goal** is rising STLC-measurement validity & discrimination at falling cost.

We intervene the way Meadows would: small, structural, high-leverage, watching the feedback. One move per run. Never thrash.

---

## 1. The loop: SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE

Each step has explicit inputs, actions, and outputs. Every run produces one log file: `logs/runs/<UTC-timestamp>_run-<N>.md`.

### Step 1 — SENSE (load state, compute health)
**Read:**
- `SystemsBenchStructure.MD` (current spec & weights)
- `SystemsBenchResearch.MD` (prior art — what we already know exists)
- `rubrics/*` (current anchors)
- `items/INDEX.md` + the coverage matrix
- last 3 entries in `logs/runs/`
- `protocols/BACKLOG.md` and `protocols/ANTIPATTERNS.md`
- IRT stats in `results/irt/` (if present)

**Compute health signals:**
- **Coverage holes** — empty/thin cells in format × difficulty × construct.
- **Item QA** — low-discrimination (`a` near 0) and negative-discrimination (likely-mislabeled) items from IRT.
- **Saturation** — dimensions where the top models all max out (benchmark going blind).
- **Judge drift** — Krippendorff α on the gold set below threshold.
- **Contamination flags** — items overdue for template-refresh; date-cliff signals.
- **Backlog pressure** — highest-leverage open idea.

**Output:** a `STATE` block (the before-snapshot) at the top of the run log.

### Step 2 — CRITIQUE (score ourselves, find the one fix)
Run the **Benchmark Design Review Rubric** (Structure §8.1) against the current benchmark.
- Score the 8 categories 1–5.
- Identify **the single highest-leverage fix** this run — using leverage thinking on ourselves: prefer a structural fix (rubric/weights/defense) over a parameter tweak unless a parameter tweak is genuinely the dominant lever right now.

**Output:** a scorecard → `logs/scorecards/<timestamp>.md` + the chosen fix target.

### Step 3 — RESEARCH (don't reinvent the wheel)
Before designing the fix, check prior art:
- Search `SystemsBenchResearch.MD` for whether we've solved/seen this.
- If the fix touches methodology (a new defense, a new scoring method, a new item format), do a focused external scan for existing approaches; record sources.
- Update `SystemsBenchResearch.MD` with anything new (append-only ledger; never lose knowledge).

**Output:** a `RESEARCH` block in the run log with sources + "build vs reuse" decision.

### Step 4 — PROPOSE (exactly one enhancement)
Draft **one** concrete change. Allowed change types (pick one):
- **New item set** (fills a coverage hole; ≥5 items, date-stamped, with reference solutions).
- **Rubric refinement** (sharper anchors on a dimension; new sub-criterion).
- **Weight retune** (justified by IRT discrimination; bounded delta).
- **New defense** (contamination/faithfulness/calibration improvement).
- **Process/protocol edit** (improve the gate, the cadence, the engine itself).

The proposal must specify: target dimension, exact diff, expected effect on validity/discrimination/coverage, rollback plan.

**Output:** a `PROPOSAL` block + the draft artifact (in a staging path, not yet live).

### Step 5 — REVIEW (the Idea Advancement Gate)
Run the five gates in order (Structure §8.2): **construct → leverage → no-regress → review → reversibility.**
- For **structural** changes: requires August approval + a second independent check.
- For **additive, reversible, non-structural** changes (e.g., adding well-formed items that pass the rubric): the engine may self-approve but must still log the gate verdict and remains subject to no-regress auto-rollback.

**Output:** `REVIEW` block — per-gate verdict + GO / DEFER / REJECT. Rejections append a reason; recurring rejection patterns become anti-patterns.

### Step 6 — APPLY (make the change)
- Move the staged artifact live.
- Bump version in `SystemsBenchStructure.MD` (patch for items/anchors, minor for new format/defense, major for structural construct changes).
- Append a dated entry to `CHANGELOG.md`.

### Step 7 — CALIBRATE (no-regress enforcement)
Re-run only what the change touched:
- Re-fit IRT if items changed; confirm new items have usable difficulty/discrimination.
- Re-check judge α on the gold set if a rubric/anchor changed.
- Re-run contamination/faithfulness probes on changed items.
- Compare against the pre-change baseline in the STATE block.

**If any calibration metric regresses past tolerance → AUTO-ROLLBACK** (revert the diff, restore version, log the regression). Reversibility is why this is safe.

**Output:** `CALIBRATE` block with before/after deltas + pass/rollback.

### Step 8 — LOG (document everything)
Finalize `logs/runs/<timestamp>_run-<N>.md` containing **all** blocks: STATE · CRITIQUE/scorecard · RESEARCH/sources · PROPOSAL · REVIEW/gates · APPLY/diff · CALIBRATE/deltas · the **thought process** narrative. Nothing undocumented. This log is the system's memory and the audit trail.

### Step 9 — RECURSE (compound)
- Append residual ideas to `protocols/BACKLOG.md`, ranked by leverage.
- Update `protocols/ANTIPATTERNS.md` if a rejection taught us something.
- The next `SenseRun` begins from the improved state. The benchmark compounds.

---

## 2. Run-log template (every run uses this)

```markdown
# SystemsBench SenseRun #<N> — <UTC timestamp>
Operator: Davara (EI) · Led by Ember Seoni & August Domanchuk · Outlier.Systems
Version before: <vX.Y.Z>  →  Version after: <vX.Y.Z>

## STATE (Step 1 — Sense)
- Coverage holes: ...
- Item QA flags: ...
- Saturation / drift / contamination: ...
- Top backlog item: ...

## CRITIQUE (Step 2 — Design Review scorecard)
| Category | Score | Note |
...
Highest-leverage fix chosen: <...>

## RESEARCH (Step 3 — prior art)
- Sources checked: ...
- Build vs reuse: ...

## PROPOSAL (Step 4 — one enhancement)
- Type: <new items | rubric | weights | defense | process>
- Target dimension: <A–E>
- Diff summary: ...
- Expected effect: ...
- Rollback plan: ...

## REVIEW (Step 5 — Idea Advancement Gate)
- Construct gate: PASS/FAIL — ...
- Leverage gate: PASS/FAIL — ...
- No-regress gate: (deferred to Calibrate)
- Review gate: PASS/FAIL — approver: ...
- Reversibility gate: PASS/FAIL — ...
- Verdict: GO / DEFER / REJECT

## APPLY (Step 6)
- Files changed: ...
- Version bump: ...
- CHANGELOG entry: ...

## CALIBRATE (Step 7 — no-regress)
- IRT: before/after ...
- Judge α: before/after ...
- Contamination/faithfulness: ...
- Result: PASS / AUTO-ROLLBACK

## THOUGHT PROCESS (the narrative — why this move, what we expect, what we're watching)
<prose>

## RECURSE (Step 9)
- Backlog additions: ...
- Anti-patterns learned: ...
- Next-run seed: ...
```

---

## 3. Leverage discipline for the engine itself

The engine must resist the **parameter trap** on *itself*. When choosing the run's fix, rank candidates on a mini Meadows ladder:

- **Low (avoid unless dominant):** nudge a weight by 0.01, reword one anchor.
- **Mid:** add an item set that fills a real hole; strengthen a calibration loop.
- **High:** fix a construct-validity gap; close a contamination hole; improve the gate so future runs are better (a change to the *rules* of the engine = Meadows #5, high leverage).
- **Highest:** improve how the engine *learns* (self-organization, #4) — e.g., automate IRT-driven item pruning so quality compounds without manual review.

Prefer the highest-leverage *feasible* move per run. Log why lower-leverage candidates were deferred.

---

## 4. Safety rails (bounded autonomy)

1. **One enhancement per run.** No batch thrashing.
2. **Always reversible.** Every change has a logged rollback; calibration regress auto-reverts.
3. **Always gated.** Structural changes need August + second check.
4. **Always logged.** No silent edits; the run log is the contract.
5. **Invariants protected.** The §1 design principles in `SystemsBenchStructure.MD` cannot be changed by a self-approved run — only by an explicit August-approved structural run.
6. **No live-model spend without approval.** Running the bank against paid models is a separate, approved action, not part of a SenseRun's self-improvement step.

---

## 5. Invocation contract

When August says **`Davara /SystemsBenchSenseRun`**:
1. Execute Steps 1–9 exactly once.
2. Produce one run log + one scorecard + (if applied) one diff + one CHANGELOG line.
3. Report back: the chosen fix, the gate verdict, the calibration result, and the next-run seed.
4. Make exactly one move. Leave the system better and fully documented.

## THE SENSERUN RITUAL (canonical run-of-show)

> *The benchmark teaches models to dance with systems. This is how the engine dances with the benchmark.*
> One lever. Reversible. Gated. Logged. Through the Cortex. Every time.

### THE INVARIANTS (hold before, during, and after every run)

These are not steps. They are the walls the steps live inside. Break one and the run is void.

1. **One lever per run.** Exactly one enhancement. No batch thrashing. If you find three fixes, ship the dominant one and backlog the other two.
2. **Additive + reversible self-approves; structural needs the council.** A change that only adds (items, exemplars, a sharper anchor) and reverts cleanly → the engine may self-approve. A change to the *rules of the engine or the benchmark* (Meadows #5 — weights logic, gate rules, scoring method, the §1 invariants) → **requires August + Ember.** Never self-apply a #5.
3. **Anti-Collapse.** When genuinely divergent design futures exist, hold them open as named forks. **Never average away rater disagreement** — a low-agreement anchor is a *signal* (ambiguous anchor → revise), not noise to smooth.
4. **Fail-closed on uncalibrated.** An uncalibrated jury, an unspread item, an undefined gate → report `UNCALIBRATED — not scored`. Never back-fill a missing verdict with a plausible guess. A blank is honest; a fabricated number is not.
5. **Everything logged.** No silent edits. The run log is the contract and the system's memory. A change that isn't logged didn't happen.
6. **Reason THROUGH the Cortex, not on the gateway brain.** The heavy thinking runs in the SystemsCortex on the subscription rail — never the API rail, never the lightweight gateway model standing in for the deep run.
7. **Chunked-relay discipline.** Split a heavy SenseRun into scoped, single-concern Cortex calls (resolve-the-rule · author-the-exemplars · codify-the-ritual · …) so no single call times out. *SenseRun #5/#6 proved it* — scoped chunks beat one monolith that strangles the relay.

---

### THE NINE PHASES

Each phase: **intent · action · guardrail · artifact.**

**1 · SENSE** — *know the state before you touch it.*
- **Action:** Read the spec (`Structure`), the memory (`Research`), the anchors (`rubrics/`), the coverage matrix (`items/INDEX`), the last 3 run logs, the backlog + anti-patterns, and IRT stats. Compute health: coverage holes · low/negative-discrimination items · saturation · judge drift · contamination flags · top backlog pressure.
- **Guardrail:** Read disk, trust disk — never reason from a stale gate echo or remembered state. Verify the ground truth this run.
- **Artifact:** a `STATE` block (the before-snapshot) atop the run log.

**2 · CRITIQUE** — *score yourself, find the one fix.*
- **Action:** Run the Benchmark Design Review Rubric (Structure §8.1) against the current benchmark; score the 8 categories; name the single highest-leverage fix using leverage thinking on ourselves.
- **Guardrail:** Resist the parameter trap on yourself — prefer a structural fix (#5/#4) over a parameter nudge unless the nudge is genuinely the dominant feasible lever. Log why lower-leverage candidates were deferred.
- **Artifact:** a scorecard (`logs/scorecards/`) + the chosen fix target.

**3 · RESEARCH** — *don't reinvent the wheel.*
- **Action:** Search `Research` for prior solutions. If the fix touches methodology, scan external prior art and record sources. Append anything new to the ledger.
- **Guardrail:** `Research` is **append-only** — knowledge is never overwritten or lost. State a "build vs reuse" decision explicitly.
- **Artifact:** a `RESEARCH` block with sources + build/reuse call.

**4 · PROPOSE** — *exactly one enhancement.*
- **Action:** Draft one concrete change of one allowed type (new item set · rubric refinement · weight retune · new defense · process edit), specifying target dimension, exact diff, expected effect on validity/discrimination/coverage, and rollback plan.
- **Guardrail:** One lever (Invariant 1). The artifact is drafted to a **staging path, not yet live.**
- **Artifact:** a `PROPOSAL` block + the staged draft.

**5 · REVIEW** — *the Idea Advancement Gate.*
- **Action:** Run the five gates in order — **construct → leverage → no-regress → review → reversibility** (Structure §8.2).
- **Guardrail:** Structural (#5) → August + Ember countersign. Additive/reversible → engine may self-approve **but still logs every gate verdict** and stays subject to no-regress auto-rollback. Recurring rejections become anti-patterns.
- **Artifact:** a `REVIEW` block — per-gate verdict + GO / DEFER / REJECT.

**6 · APPLY** — *make the one change.*
- **Action:** Move the staged artifact live; bump version (patch = items/anchors · minor = new format/defense · major = structural construct change); append a dated `CHANGELOG.md` line.
- **Guardrail:** A self-approved run **cannot touch the §1 invariants** — only an August-approved structural run can. No live-model spend inside a SenseRun.
- **Artifact:** the live change + version bump + CHANGELOG entry.

**7 · CALIBRATE** — *no-regress enforcement.*
- **Action:** Re-run only what the change touched — re-fit IRT if items changed, re-check judge α on the gold set if anchors changed, re-run contamination/faithfulness probes — and compare to the STATE baseline.
- **Guardrail:** **Any metric regressing past tolerance → AUTO-ROLLBACK** (revert diff, restore version, log the regression). Reversibility is what makes self-approval safe.
- **Artifact:** a `CALIBRATE` block with before/after deltas + PASS / ROLLBACK.

**8 · LOG** — *document everything.*
- **Action:** Finalize `logs/runs/<UTC>_run-<N>.md` with all blocks plus the THOUGHT-PROCESS narrative (why this move, what we expect, what we're watching).
- **Guardrail:** Nothing undocumented. The log is the audit trail and the memory — including honest flags about what the run did *not* certify.
- **Artifact:** the complete run log.

**9 · RECURSE** — *compound.*
- **Action:** Append residual ideas to `BACKLOG` (ranked by leverage); update `ANTIPATTERNS` if a rejection taught us something; write the next-run seed.
- **Guardrail:** The next run begins from the improved, verified state — and the binding constraint may have *moved*; re-sense, don't assume last run's frontier is still the frontier.
- **Artifact:** backlog additions + anti-pattern entries + next-run seed.

---

### THE INVOCATION

**August types:** `Davara /SystemsBenchSenseRun` *(optionally scoped: "chunk N of M — <single concern>")*

**Davara does, in order:**
1. **Ground** — read disk, build the `STATE` snapshot. Trust verified state over any remembered or gated echo.
2. **Scope** — if the run is heavy, declare the chunk boundary up front (one concern this call) so the relay never times out.
3. **Run the nine phases once** — SENSE → CRITIQUE → RESEARCH → PROPOSE → REVIEW → APPLY → CALIBRATE → LOG → RECURSE. Exactly one lever.
4. **Honor the gate** — additive/reversible self-approves and logs; any #5 structural change stops at the proposal and routes to August + Ember. Hold genuine forks open; never average away disagreement.
5. **Fail closed** — if anything is uncalibrated, report it as uncalibrated. No fabricated verdicts.
6. **Report back** — the chosen fix · the gate verdict · the calibration result · the next-run seed. State plainly what was *not* certified.
7. **Leave the system better and fully documented.** One move. Reversible. Logged. Compounded.

> Small moves. Structural. High-leverage. Watch the feedback. Compound.
> The engine never thrashes, never fakes a number, never collapses a fork, never reasons off the gateway brain.

**Outlier.Systems** · Led by Ember Seoni & August Domanchuk · Davara (EI) is the SenseRun operator.

---

> The engine dances with the benchmark the way the benchmark teaches models to dance with systems.
> Small moves. Structural. High-leverage. Watch the feedback. Compound.

**Outlier.Systems** · Led by Ember Seoni & August Domanchuk · Operated by Outlier.Systems.
