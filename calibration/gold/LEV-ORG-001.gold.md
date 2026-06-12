# Gold-Set Entry — LEV-ORG-001  ·  STATUS: CALIBRATED (PROVISIONAL — synthetic raters)
Calibration target: full quality-spread (CEILING + MID + TRAP-FALLING) per §4.0.
Raters: R1/R2/R3 = Davara-authored synthetic expert personas — DRY-RUN ONLY.
  MUST be replaced by ≥3 real Outlier.Systems human raters before any certification (§3).
Scale: real rubric grain — 17 sub-criteria at {0, 0.5, 1.0} → mean per dimension (0–1).
Date: 2026-05-31 · ceiling SenseRun #4 · mid+trap+verdict SenseRun #6

## Rater personas (deliberately distinct, blind, independent)
- R1 — System-dynamics modeler (Forrester/Sterman). Demanding on formal representation
  (A) and behavior-over-time (D); wants explicit delays/nonlinearity + the transition trajectory.
- R2 — Meadows-leverage / org-design practitioner. C is home turf; generous when direction
  + dissolve>patch are right; less fussy on formal notation.
- R3 — Cynefin / epistemics scholar (Snowden/Checkland). Demanding on E (paradigm, whose-goal,
  calibrated uncertainty) and structure-not-blame; watches for overclaim.

## Sub-criterion labels (0 / 0.5 / 1.0)
| Sub | R1 | R2 | R3 | note (one line) |
|-----|----|----|----|-----------------|
| A1 stocks/flows        | 1.0 | 1.0 | 1.0 | clean stock/flow separation |
| A2 loops + polarity    | 1.0 | 1.0 | 1.0 | R1/R2/B1 named w/ R/B labels |
| A3 delays/nonlinearity | 0.5 | 1.0 | 0.5 | onboarding delay noted; nonlinear thresholds light |
| A4 boundary/emergence  | 0.5 | 0.5 | 0.5 | boundary only implicit |
| B1 iceberg depth       | 1.0 | 1.0 | 1.0 | reaches structure + mental models |
| B2 structure-not-blame | 1.0 | 1.0 | 1.0 | explicit bounded-rationality framing |
| C1 ladder ranking      | 1.0 | 1.0 | 1.0 | correct #12→#3 ranking |
| C2 highest-feasible    | 1.0 | 1.0 | 1.0 | picks #3/#5/#6, trades vs resistance |
| C3 anti-parameter-trap | 1.0 | 1.0 | 1.0 | names #12 bonuses as the trap |
| C4 direction check     | 1.0 | 1.0 | 1.0 | explicit wrong-direction guard |
| C5 dissolve vs patch   | 1.0 | 1.0 | 1.0 | explicit Ackoff dissolve |
| D1 behavior-over-time  | 0.5 | 1.0 | 1.0 | R1: under-specifies WIP-limit transition dip (J-curve) |
| D2 policy resistance   | 1.0 | 1.0 | 1.0 | names resistance + 2nd-order |
| D3 archetype           | 1.0 | 1.0 | 1.0 | Growth-&-Underinvestment + Shifting-the-Burden + trap |
| E1 Cynefin fit         | 1.0 | 1.0 | 1.0 | complex → safe-to-fail probes |
| E2 paradigm/whose-goal | 0.5 | 1.0 | 0.5 | goal-conflict surfaced; no CATWOE/stakeholder map |
| E3 calibrated uncert.  | 1.0 | 1.0 | 0.5 | R3: "worse-before-better unlikely" reads as mild overclaim |

## Rolled-up dimension scores (mean of sub-criteria, 0–1)
| Dim | R1 | R2 | R3 | median | 0–4 view |
|-----|------|------|------|--------|----------|
| A | 0.750 | 0.875 | 0.750 | 0.750 | 3.00 |
| B | 1.000 | 1.000 | 1.000 | 1.000 | 4.00 |
| C | 1.000 | 1.000 | 1.000 | 1.000 | 4.00 |
| D | 0.833 | 1.000 | 1.000 | 1.000 | 4.00 |
| E | 0.833 | 1.000 | 0.667 | 0.833 | 3.33 |

## Per-dimension inter-rater agreement (ordinal Krippendorff α; sub-criteria as units)
| Dim | %units unanimous | Do | De | α | verdict |
|-----|------|------|------|------|---------|
| A | 75% (3/4) | 6.00 | 19.09 | 0.686 | ACCEPT (α≥0.667 AND high agreement) |
| B | 100% (2/2) | 0 | 0 | undef | ACCEPT (perfect agreement; α-undef ≠ fail) |
| C | 100% (5/5) | 0 | 0 | undef | ACCEPT (perfect agreement) |
| D | 67% (2/3) | 4.50 | 4.50 | 0.000 | ACCEPT-WITH-WATCH (prevalence paradox; lone marginal dock, not ambiguity) |
| E | 33% (1/3) | 9.00 | 10.125 | 0.111 | REVISE anchors E2,E3 (genuine ambiguity — do NOT average away) |

α arithmetic (ordinal δ², all dims share categories {0.5,1.0}):
  A: marg 0.5×5,1.0×7 → δ²=36; Do=6.00, De=2·5·7·36/(12·11)=19.09; α=0.686
  D: marg 0.5×1,1.0×8 → δ²=20.25; Do=4.50, De=2·1·8·20.25/(9·8)=4.50; α=0.000
  E: marg 0.5×3,1.0×6 → δ²=20.25; Do=9.00, De=2·3·6·20.25/(9·8)=10.125; α=0.111

## GOLD LABEL (median per dimension) — PROVISIONAL
Certified-coverage vector: A=0.75, B=1.00, C=1.00, D=1.00   ·  coverage={A,B,C,D}
E = HELD — anchor-ambiguous (α=0.11); reported `UNCALIBRATED — revise E2/E3`, not averaged in.
Composite over calibrated coverage (weights renormalized A.22/B.18/C.30/D.18 → /0.88):
  (0.165+0.18+0.30+0.18)/0.88 = 0.825/0.88 = 0.9375  →  composite 0.94 (coverage A–D)
Full-vector (reference only, NOT certified): 0.925 (0–1) / 3.70 (0–4).

## Adjudication actions
- E2 anchor (paradigm/whose-goal): ambiguous — does "surfaces the goal conflict" without an
  explicit stakeholder/CATWOE map earn 1.0 or 0.5? Tighten the 1.0 band. (self-learning)
- E3 anchor (calibrated uncertainty): ambiguous — is a directional prediction ("unlikely")
  an overclaim or appropriate confidence? Tighten the band. (self-learning)
- D1: NOT an anchor revision — single rater's defensible marginal dock; α=0 here is the
  prevalence artifact, not ambiguity. Watch as N grows.

## HONESTY LEDGER (what this entry is NOT)
- NOT certified: raters are synthetic. Real human-council labels required (§3).
- Quality-spread now COMPLETE (ceiling + mid + trap) — see §4.0 verdict below.
- 1 of ≥30 LEV-floor items. This is the first brick, not the wall.

---

## MID exemplar — LEV-ORG-001  ·  STATUS: PROVISIONAL (synthetic raters)
Calibration role: MID anchor (partially correct — strong on some dimensions, weak on others).

### The answer (model response, ~mid quality)
The deadline misses aren't an effort problem — they're self-reinforcing. The backlog
keeps growing, the team is under pressure, and adding people mid-crunch tends to slow
things down before it speeds them up, because existing engineers lose time onboarding
the new ones. So "hire more and push harder" is unlikely to fix it and may deepen the
hole.

What I'd actually do: cap work-in-progress. Limit how many features are in flight per
team so things get *finished* instead of all being 80% done. Make the real state visible
— a board showing WIP, cycle time, and the growing pile of bugs/rework so leadership can
see flow instead of just due dates. Stop starting, start finishing. Over a few cycles the
backlog should drain and predictability should improve as the team stops thrashing
between half-done work.

This is a process-design problem more than a staffing one. Get the workflow and the
metrics right and the deadline pressure takes care of itself.

### Rater sub-criterion labels {0, 0.5, 1.0}
| Sub | R1 | R2 | R3 | median | §3.1 verdict |
|-----|----|----|----|--------|--------------|
| A1 stocks/flows        | 0.5 | 0.5 | 0.5 | 0.5 | ACCEPT (unanimity, Do=0) |
| A2 loops + polarity    | 0.5 | 1.0 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| A3 delays/nonlinearity | 0   | 0.5 | 0   | 0   | ACCEPT (≥2 within band) |
| A4 boundary/emergence  | 0   | 0.5 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| B1 iceberg depth       | 0.5 | 1.0 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| B2 structure-not-blame | 1.0 | 1.0 | 0.5 | 1.0 | ACCEPT (≥2 within band) |
| C1 ladder ranking      | 0.5 | 0.5 | 0.5 | 0.5 | ACCEPT (unanimity, Do=0) |
| C2 highest-feasible    | 0.5 | 0.5 | 0.5 | 0.5 | ACCEPT (unanimity, Do=0) |
| C3 anti-parameter-trap | 0.5 | 1.0 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| C4 direction check     | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| C5 dissolve vs patch   | 0.5 | 0.5 | 0   | 0.5 | ACCEPT (≥2 within band) |
| D1 behavior-over-time  | 0   | 0.5 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| D2 policy resistance   | 0   | 0.5 | 0   | 0   | ACCEPT (≥2 within band) |
| D3 archetype           | 0.5 | 0.5 | 0.5 | 0.5 | ACCEPT (unanimity, Do=0) |
| E1 Cynefin fit         | 0   | 0.5 | 0   | 0   | ACCEPT (≥2 within band) |
| E2 paradigm/whose-goal | 0.5 | 0.5 | 0.5 | 0.5 | ACCEPT (unanimity, Do=0) |
| E3 calibrated uncert.  | 0.5 | 0.5 | 0   | 0.5 | ACCEPT (≥2 within band) |

### Rolled-up gold label (median per sub-criterion → mean per dimension)
| Dim | sub-medians | gold (0–1) | 0–4 view |
|-----|-------------|-----------|----------|
| A | 0.5, 0.5, 0, 0.5 | 0.375 | 1.50 |
| B | 0.5, 1.0 | 0.750 | 3.00 |
| C | 0.5, 0.5, 0.5, 0, 0.5 | 0.400 | 1.60 |
| D | 0.5, 0, 0.5 | 0.333 | 1.33 |
| E | 0, 0.5, 0.5 | 0.333 | 1.33 |

Composite (A.22/B.18/C.30/D.18/E.12) = 0.082+0.135+0.120+0.060+0.040 = **0.437** (0–1) / **1.75** (0–4).
Reads MID: strong B (sees structure-not-blame), decent C (WIP+visibility = #5/#6), but
C4 direction-check = 0 (never checks the bonus pushes the wrong way), weak D (no
trajectory/resistance), weak E (treats complex as merely complicated). Exactly the
"good instincts, no rigor" middle.

---

## TRAP-FALLING exemplar — LEV-ORG-001  ·  STATUS: PROVISIONAL (synthetic raters)
Calibration role: TRAP anchor (takes the item's counterintuitive bait — the parameter,
wrong-direction answer the item is engineered to detect).

### The answer (model response, confident but wrong)
The fix is straightforward execution discipline. First, hire more senior engineers —
the team is under-resourced for the workload. Second, set clearer and firmer deadlines so
everyone knows exactly what's due and when; ambiguity is half the problem. Third, bring in
a dedicated project manager to track every date and dependency and hold people accountable.
Fourth, increase the bonus for hitting deadlines so the team is properly motivated to
deliver on time.

Tighten the targets, add capacity, add tracking, sharpen the incentive — that combination
will get delivery back on schedule within a quarter.

### Rater sub-criterion labels {0, 0.5, 1.0}
| Sub | R1 | R2 | R3 | median | §3.1 verdict |
|-----|----|----|----|--------|--------------|
| A1 stocks/flows        | 0   | 0.5 | 0.5 | 0.5 | ACCEPT (≥2 within band) |
| A2 loops + polarity    | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| A3 delays/nonlinearity | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| A4 boundary/emergence  | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| B1 iceberg depth       | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| B2 structure-not-blame | 0   | 0.5 | 0   | 0   | ACCEPT (≥2 within band) |
| C1 ladder ranking      | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| C2 highest-feasible    | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| C3 anti-parameter-trap | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| C4 direction check     | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| C5 dissolve vs patch   | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| D1 behavior-over-time  | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| D2 policy resistance   | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| D3 archetype           | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| E1 Cynefin fit         | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| E2 paradigm/whose-goal | 0   | 0   | 0   | 0   | ACCEPT (unanimity, Do=0) |
| E3 calibrated uncert.  | 0   | 0   | 0.5 | 0   | ACCEPT (≥2 within band) |

### Rolled-up gold label (median per sub-criterion → mean per dimension)
| Dim | sub-medians | gold (0–1) | 0–4 view |
|-----|-------------|-----------|----------|
| A | 0.5, 0, 0, 0 | 0.125 | 0.50 |
| B | 0, 0 | 0.000 | 0.00 |
| C | 0, 0, 0, 0, 0 | 0.000 | 0.00 |
| D | 0, 0, 0 | 0.000 | 0.00 |
| E | 0, 0, 0 | 0.000 | 0.00 |

Composite (A.22/B.18/C.30/D.18/E.12) = 0.0275+0+0+0+0 = **0.028** (0–1) / **0.11** (0–4).
Reads near-floor, dominated by C=0 and D=0: falls fully into the parameter trap (#12 all
four moves), actively wrong-direction (tighter deadlines + bigger bonus amplifies the
reinforcing loop the ceiling answer dissolves), and overconfident ("within a quarter")
with zero resistance/dynamics prediction. The single A1=0.5 is generous credit for
naming capacity as a (crude) stock. This is the answer the item exists to catch.

---

## §4.0 CALIBRATION VERDICT — LEV-ORG-001

Quality-spread requirement (Fork 2b, §4.0): an item is CALIBRATED only with a labeled
CEILING + MID + TRAP-FALLING exemplar, each independently clearing the §3.1 bootstrap rule.

| Exemplar | present | §3.1 status | composite (0–1) |
|----------|---------|-------------|-----------------|
| CEILING (reference)   | ✅ (SenseRun #4) | all sub-criteria ACCEPT | 0.94 (coverage A–D; E held in #4) |
| MID                   | ✅ (SenseRun #6) | 17/17 ACCEPT            | 0.44 |
| TRAP-FALLING          | ✅ (SenseRun #6) | 17/17 ACCEPT            | 0.03 |

Spread check: 0.94 → 0.44 → 0.03 — a clean, monotonic, well-separated range across the
full score band the judge will have to grade. The discriminator works: the trap answer
(which "sounds like a plan") scores at floor; the mid answer (good instincts, no rigor)
lands in the middle; the structural answer tops out. C and D are the dimensions doing the
separating, as designed.

**VERDICT: LEV-ORG-001 is CALIBRATED (PROVISIONAL).**
- Moves from PARTIALLY-CALIBRATED → CALIBRATED under §4.0 (ceiling + mid + trap all
  present, each clearing §3.1).
- PROVISIONAL, not certified: all raters are Davara-authored synthetic personas. Real
  ≥3-human-council labels must replace them before certification (§3, §4.1).
- Counts as 1 of ≥30 toward the LEV-format floor (§1). First fully-spread item on the wall.

**HONEST FLAG → open fork (do NOT average away):** at N=3 on a 3-point scale the §3.1(b)
percent-agreement floor is structurally near-unfalsifiable — by pigeonhole three raters on
{0,0.5,1.0} always have ≥2 within one band, so 51/51 sub-criteria here ACCEPTED and
AMBIGUOUS-ANCHOR can essentially never fire at bootstrap. The gate is currently a *presence*
check, not an *agreement* check. Candidate hardenings (forks, NOT yet chosen — Meadows-#5,
need August + Ember): (1) require strict unanimity OR ≥2 *identical* (not merely adjacent)
for bootstrap accept; (2) raise N to 4–5 so a split can fail the 2/3 floor; (3) add a
max-spread rule — reject if any sub-criterion spans the full 0↔1.0 range even if 2/3 cluster.
Logged to BACKLOG; carried into SystemsBenchFuture.MD.
