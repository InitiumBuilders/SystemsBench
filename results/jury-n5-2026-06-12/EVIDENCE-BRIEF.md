# EVIDENCE BRIEF — §3.1 Accept-Rule Hardening (for August + Ember ratification)

**Date:** 2026-06-12 · **Scope:** evidence only, no governance edits · **Decision owner:** August + Ember (Meadows-#5 gate, BACKLOG #0 / Future §6.1)
**Method:** the LEV-ORG-001 quality-spread (CEILING + MID + TRAP) was re-scored by **N=5 independent, context-isolated, blind synthetic raters** (`engine/jury.sh`: each rater is its own fresh session seeing ONLY item + rubric + response — no tier labels, no gold labels, no other raters). R1–R3 reuse the recorded baseline personas; R4 (lean/flow practitioner) and R5 (psychometrics literalist) are new and deliberately orthogonal. All three candidate hardening forks from Future §6.1 were then run as dry-runs against both the recorded N=3 labels and the new N=5 labels — exactly the review process §6.1 specifies. Full tables: `REPORT.md`; raw rater JSON: `raters/`.

## Findings

**1 · The benchmark's discriminator survives a bigger, partly-new jury.**
Composites N=3 → N=5: CEILING **0.925 → 0.953**, MID **0.438 → 0.448**, TRAP **0.028 → 0.000**. The spread stays monotonic and well-separated; 41/51 (80%) sub-criterion medians identical, and disagreements concentrate in MID — the tier where genuine ambiguity lives. The item works.

**2 · Raising N alone (fork 2) makes the gate falsifiable in theory but it still never fired.**
At N=5 the §3.1(b) window rule requires ⌈2N/3⌉ = 4 raters within one band, so a 3–2 cross-band split *can* fail (impossible at N=3 by pigeonhole). In practice: **51/51 sub-criteria still ACCEPTED at N=5.** Real raters cluster on these anchors; the falsifiability is real but the detection power is low. Fork 2 alone buys robustness of the *labels* (more stable medians, real per-tier α — e.g. MID C α=0.836) but not a sharper *gate*.

**3 · Fork 1 (≥⌈2N/3⌉ IDENTICAL labels) is the only rule that actually detects anything — and it detects the right things.**
At N=5 it flagged **4/51** sub-criteria AMBIGUOUS, all on MID: **C1, D1, E1, E2**. Two of these are precisely the anchors the N=3 adjudication already suspected: the gold entry held **E** as anchor-ambiguous (α=0.11) and said of **D1** "watch as N grows" — at N=5, D1 split 0.5,1,1,0.5,1 and fork 1 caught it. Independent method, same diagnosis: convergent evidence that fork 1 fires on genuine anchor ambiguity, not noise. (MID E α=0.222 at N=5 confirms E1/E2 anchors still need the §adjudication revision.)

**4 · Fork 3 (max-spread) never fired (0/51 at either N).**
No rater pair produced a full 0↔1.0 split on any sub-criterion. On this evidence it adds rule complexity with no detection power — though one item is thin ground for permanent rejection.

## Evidence-backed option (recommendation, not a ruling)
**Adopt fork 1 + fork 2 together: N=5 raters, bootstrap accept = unanimity OR ≥⌈2N/3⌉ identical labels; keep the §3.1(a) unanimity special-case unchanged.** Fork 1 supplies the detection power (finding 3), N=5 supplies the label stability and makes both rules meaningfully falsifiable (finding 2). The economics now favor it: with `jury.sh`, five isolated raters cost one command and ~2 minutes wall-clock — the original reason for N=3 (labeling cost) no longer binds. Fork 3: hold, revisit when ≥5 items have spreads.

## Honesty ledger (what this evidence is NOT)
- **All raters are synthetic** — five personas on one underlying model. Persona-level independence, not model-level; real humans likely disagree more, which would *raise* fork-1 fire rates. §3 still requires ≥3 real human raters before any certification; nothing here is a certified label.
- **One item.** LEV-ORG-001 is 1 of ≥30 needed for the LEV floor; fire-rates from 51 sub-criteria are indicative, not definitive.
- **N=3 vs N=5 deltas include re-test variance** (R1–R3 re-run fresh, not replayed), so the comparison measures the whole pipeline's stability, which is the operationally honest quantity.
- The CEILING response is the reference solution verbatim (same convention as the recorded baseline) — raters may recognize it alongside the reference; ceiling scores are the least informative of the three tiers.

*Prepared by Davaris (Execution EI) · SystemsBench Phase 4 · infrastructure: `engine/jury.sh`, `engine/jury-stats.py`, `engine/personas/R1–R5.md` · calculator calibrated 18/18 against the recorded gold arithmetic before any live scoring.*
