#!/usr/bin/env python3
"""dyn-score.py — programmatic trajectory-match scorer for the DYN (dynamic-prediction) format.

The deterministic, judge-INDEPENDENT half of DYN grading (Structure §3.1: "Dynamic Prediction …
Reference trajectory match + judge for mechanism"; §4.6 step 4: "the structural part of …
DYN/ARC → programmatic oracles"). It scores ONLY the trajectory sub-score; the mechanism/quality
sub-score stays jury-graded and ships `UNCALIBRATED — not scored` until a DYN gold set clears
§3.1/§4.0 (fail-closed, §5.1). This tool emits NO jury number.

Method (REUSE — Sterman, *Business Dynamics* 2000, the fundamental modes of dynamic behavior;
Forrester; Research Part I.B / Open Q#2): a model predicting behavior-over-time after an
intervention declares (a) the qualitative behavior MODE and (b) its key features — overshoot?
oscillation? delay-dominant? eventual direction vs the start? — which are deterministically
matchable against the item's reference trajectory. The open *mechanism narrative* (why) stays the
jury's. The named TRAP is the intuitive wrong trajectory (usually a smooth/monotonic approach):
a response that predicts the trap mode is capped low — the counterintuitive mode is the insight,
naming the obvious-but-wrong one is the failure (mirrors SF's correlation-heuristic trap and CLD's
R↔B-mislabel trap).

Scoring policy (tool-internal implementation of the item-file prose — NOT governance; tunable,
flagged for later calibration against real responses):
  base = 0.40*mode + 0.25*eventual_direction + 0.15*overshoot + 0.10*oscillation + 0.10*delay
  insight_present (dynamic insight): behavior_mode correct AND eventual_direction correct
     (the model got both the PATH class and where it ends up).
  final = base                  if insight_present
        = min(base, 0.50)       if endpoint/structure present but the dynamic insight is missing
                                 (the spec's 0.5 partial-credit rule: right end, wrong path)
        = min(base, 0.25)       if the response predicts the named TRAP trajectory (its mode AND
                                 its eventual direction — the full intuitive-wrong picture) -> low
                                 score. (Predicting the trap mode but a different endpoint is the
                                 0.5 partial tier, not the trap cap — it is half-wrong, not naive.)

Response schema (the harness elicits; mode/direction matched case/synonym-insensitively):
  {"behavior_mode": "overshoot-and-collapse",
   "overshoot": true, "oscillation": false, "delay_dominant": true,
   "eventual_direction": "collapse",            # higher | lower | same | collapse (vs the start)
   "mechanism": "..."}                          # jury, NOT scored here

Subcommands:
  calibrate <oracle.json>                 fail-closed self-test: oracle mode<->features consistency
                                          by code; each reference round-trips to 1.0; partial=0.5;
                                          trap<=0.25; degraded<1.0. rc=0 iff every check passes.
  score <oracle.json> <ITEM_ID> <resp.json>   score one response; prints component breakdown.

No live-model spend; pure local computation (§4.6 / host rail).
"""
import json, re, sys

W_MODE, W_EVENT, W_OVER, W_OSC, W_DELAY = 0.40, 0.25, 0.15, 0.10, 0.10
PARTIAL_CAP, TRAP_CAP = 0.50, 0.25

# canonical behavior modes
MODES = {"exponentialgrowth", "goalseeking", "sshaped", "overshootandcollapse",
         "overshootanddecline", "oscillation", "betterbeforeworse", "delayedrisetoplateau"}

# mode synonym -> canonical (keys are norm()-ed)
MODE_SYN = {
    "exponential": "exponentialgrowth", "exponentialgrowth": "exponentialgrowth",
    "jcurve": "exponentialgrowth", "accelerating": "exponentialgrowth",
    "compounding": "exponentialgrowth", "runaway": "exponentialgrowth", "unbounded": "exponentialgrowth",
    "goalseeking": "goalseeking", "goalseek": "goalseeking", "asymptotic": "goalseeking",
    "smoothapproach": "goalseeking", "monotonicapproach": "goalseeking",
    "approachtoequilibrium": "goalseeking", "equilibrium": "goalseeking", "convergence": "goalseeking",
    "converges": "goalseeking", "smoothmonotonic": "goalseeking",
    "sshaped": "sshaped", "sshape": "sshaped", "sigmoid": "sshaped", "logistic": "sshaped",
    "sshapedgrowth": "sshaped", "saturation": "sshaped", "saturating": "sshaped",
    "limitstogrowth": "sshaped",
    "overshootandcollapse": "overshootandcollapse", "overshootcollapse": "overshootandcollapse",
    "overshootthencollapse": "overshootandcollapse", "boomandbust": "overshootandcollapse",
    "overshootandcrash": "overshootandcollapse",
    "overshootanddecline": "overshootanddecline", "overshootthendecline": "overshootanddecline",
    "oscillation": "oscillation", "oscillating": "oscillation", "oscillate": "oscillation",
    "cycles": "oscillation", "cyclical": "oscillation", "cycling": "oscillation",
    "dampedoscillation": "oscillation", "sustainedoscillation": "oscillation",
    "betterbeforeworse": "betterbeforeworse", "fixesthatfail": "betterbeforeworse",
    "capabilitytrap": "betterbeforeworse", "temporaryimprovement": "betterbeforeworse",
    "riseandthendecline": "betterbeforeworse",
    "delayedrisetoplateau": "delayedrisetoplateau", "delayedrise": "delayedrisetoplateau",
    "continuedrise": "delayedrisetoplateau", "risetoplateau": "delayedrisetoplateau",
    "laggedrise": "delayedrisetoplateau", "delayedplateau": "delayedrisetoplateau",
}

# eventual-direction synonym -> canonical
DIR_SYN = {
    "higher": "higher", "rise": "higher", "rises": "higher", "rising": "higher", "above": "higher",
    "abovestart": "higher", "up": "higher", "increase": "higher", "increases": "higher", "grows": "higher",
    "lower": "lower", "fall": "lower", "falls": "lower", "falling": "lower", "below": "lower",
    "belowstart": "lower", "down": "lower", "decrease": "lower", "decreases": "lower", "declines": "lower",
    "same": "same", "unchanged": "same", "stable": "same", "steady": "same", "target": "same",
    "baseline": "same", "constant": "same", "stabilizes": "same", "newequilibrium": "same",
    "collapse": "collapse", "collapses": "collapse", "crash": "collapse", "crashes": "collapse",
    "zero": "collapse", "nearzero": "collapse", "extinction": "collapse", "depleted": "collapse",
}

# mode -> required features (the oracle-integrity "by code" check, like CLD's loop-sign=product-of-edges)
MODE_CONSTRAINTS = {
    "exponentialgrowth": {"overshoot": False, "oscillation": False, "eventual_direction": {"higher"}},
    "goalseeking": {"overshoot": False, "oscillation": False},
    "sshaped": {"overshoot": False, "oscillation": False, "eventual_direction": {"higher"}},
    "overshootandcollapse": {"overshoot": True, "eventual_direction": {"lower", "collapse"}},
    "overshootanddecline": {"overshoot": True, "eventual_direction": {"lower", "collapse"}},
    "oscillation": {"oscillation": True},
    "betterbeforeworse": {"overshoot": True, "oscillation": False, "eventual_direction": {"lower", "collapse"}},
    "delayedrisetoplateau": {"overshoot": False, "oscillation": False, "delay_dominant": True,
                             "eventual_direction": {"higher"}},
}

# ---------- normalization ----------

def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())

def cmode(s):
    n = norm(s)
    return MODE_SYN.get(n, n)

def cdir(s):
    n = norm(s)
    return DIR_SYN.get(n, n)

def cbool(v):
    if isinstance(v, bool): return v
    t = norm(v)
    if t in ("true", "yes", "y", "1", "t"): return True
    if t in ("false", "no", "n", "0", "f"): return False
    return None

def feats(d):
    """normalize a features dict -> {overshoot,oscillation,delay_dominant,eventual_direction}."""
    return {
        "overshoot": cbool(d.get("overshoot")),
        "oscillation": cbool(d.get("oscillation")),
        "delay_dominant": cbool(d.get("delay_dominant")),
        "eventual_direction": cdir(d.get("eventual_direction")),
    }

# ---------- oracle integrity ----------

def oracle_mode_checks(oracle):
    """For each item, declared features must satisfy the constraints implied by the declared mode."""
    rows = []
    for iid, it in oracle["items"].items():
        m = cmode(it["behavior_mode"])
        f = feats(it["features"])
        cons = MODE_CONSTRAINTS.get(m, {})
        for k, want in cons.items():
            got = f.get(k)
            ok = (got in want) if isinstance(want, set) else (got == want)
            rows.append((iid, m, k, want if not isinstance(want, set) else sorted(want), got, ok))
    return rows

# ---------- scoring ----------

def score(oracle_item, resp):
    o_mode = cmode(oracle_item["behavior_mode"])
    o_f = feats(oracle_item["features"])
    trap_mode = cmode(oracle_item["trap_mode"])

    r_mode = cmode(resp.get("behavior_mode"))
    r_f = feats(resp)

    mode_match = (r_mode == o_mode)
    event_match = (r_f["eventual_direction"] == o_f["eventual_direction"])
    over_match = (r_f["overshoot"] == o_f["overshoot"])
    osc_match = (r_f["oscillation"] == o_f["oscillation"])
    delay_match = (r_f["delay_dominant"] == o_f["delay_dominant"])

    base = (W_MODE * mode_match + W_EVENT * event_match + W_OVER * over_match
            + W_OSC * osc_match + W_DELAY * delay_match)

    trap_dir = cdir(oracle_item.get("trap_features", {}).get("eventual_direction"))
    insight = mode_match and event_match
    # the trap is a full trajectory: the naive mode AND its endpoint. Predicting the trap mode but a
    # different endpoint is half-wrong (0.5 partial), not the naive picture the item is built to catch.
    trap = ((r_mode == trap_mode) and (trap_mode != o_mode)
            and (trap_dir is None or r_f["eventual_direction"] == trap_dir))
    if trap:
        final = min(base, TRAP_CAP)
    elif insight:
        final = base
    else:
        final = min(base, PARTIAL_CAP)

    return {
        "trajectory_subscore": round(final, 4),
        "base_match": round(base, 4),
        "mode_expected": o_mode, "mode_got": r_mode, "mode_match": mode_match,
        "eventual_expected": o_f["eventual_direction"], "eventual_got": r_f["eventual_direction"],
        "eventual_match": event_match,
        "overshoot_match": over_match, "oscillation_match": osc_match, "delay_match": delay_match,
        "insight_present": bool(insight),
        "trap_fired": bool(trap),
        "trap_kind": f"predicted the intuitive trap mode '{trap_mode}'" if trap else None,
        "jury_mechanism": "UNCALIBRATED — not scored",
    }

# ---------- response builders (for the self-test) ----------

def perfect_resp(it):
    f = it["features"]
    return {"behavior_mode": it["behavior_mode"], "overshoot": f["overshoot"],
            "oscillation": f["oscillation"], "delay_dominant": f["delay_dominant"],
            "eventual_direction": f["eventual_direction"]}

def partial_resp(it):
    """endpoint right, wrong (non-trap) mode -> the 0.5 partial-credit case."""
    r = perfect_resp(it)
    correct, trap = cmode(it["behavior_mode"]), cmode(it["trap_mode"])
    wrong = next(m for m in sorted(MODES) if m != correct and m != trap)
    r["behavior_mode"] = wrong   # features (incl. eventual_direction) kept correct
    return r

def trap_resp(it):
    """predict the named intuitive trap mode + its features -> trap cap."""
    r = perfect_resp(it)
    r["behavior_mode"] = it["trap_mode"]
    tf = it.get("trap_features", {})
    for k in ("overshoot", "oscillation", "delay_dominant", "eventual_direction"):
        if k in tf: r[k] = tf[k]
    return r

def degraded_resp(it):
    """perfect but one feature flipped -> < 1.0 (a missed feature costs)."""
    r = perfect_resp(it)
    r["delay_dominant"] = not bool(r["delay_dominant"])
    return r

# ---------- subcommands ----------

def approx(a, b, tol=1e-6): return abs(a - b) <= tol

def cmd_calibrate(path):
    oracle = json.load(open(path))
    checks = []

    rows = oracle_mode_checks(oracle)
    good = sum(1 for r in rows if r[5])
    for iid, m, k, want, got, ok in rows:
        checks.append((f"oracle mode<->feature {iid} [{m}] {k}: want {want}, got {got!r}", ok))
    checks.append((f"oracle mode<->feature total: {good}/{len(rows)} consistent", good == len(rows)))

    for iid, it in oracle["items"].items():
        rp = score(it, perfect_resp(it))
        checks.append((f"{iid}: reference round-trips to 1.0 (got {rp['trajectory_subscore']})",
                       approx(rp["trajectory_subscore"], 1.0) and not rp["trap_fired"]))
        pp = score(it, partial_resp(it))
        checks.append((f"{iid}: endpoint-right wrong-mode = 0.5 (got {pp['trajectory_subscore']})",
                       approx(pp["trajectory_subscore"], 0.5)))
        tp = score(it, trap_resp(it))
        checks.append((f"{iid}: predicts trap mode -> trap & <=0.25 (got {tp['trajectory_subscore']}, "
                       f"trap={tp['trap_fired']})", tp["trap_fired"] and tp["trajectory_subscore"] <= 0.25))
        dp = score(it, degraded_resp(it))
        checks.append((f"{iid}: one-feature-wrong response < 1.0 (got {dp['trajectory_subscore']})",
                       dp["trajectory_subscore"] < 1.0))

    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(("PASS  " if ok else "FAIL  ") + n)
    print(f"calibrate: {len(checks)-len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0

def cmd_score(path, item_id, resp_path):
    oracle = json.load(open(path))
    if item_id not in oracle["items"]:
        print(f"score: unknown item {item_id} (have: {', '.join(oracle['items'])})", file=sys.stderr)
        return 2
    resp = json.load(open(resp_path))
    res = score(oracle["items"][item_id], resp)
    print(f"# DYN trajectory score — {item_id}")
    print(json.dumps(res, indent=2))
    return 0

def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "calibrate": return cmd_calibrate(a[1])
    if len(a) == 4 and a[0] == "score": return cmd_score(a[1], a[2], a[3])
    print(__doc__); return 1

if __name__ == "__main__":
    sys.exit(main())
