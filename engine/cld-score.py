#!/usr/bin/env python3
"""cld-score.py — programmatic structural scorer for the CLD (causal-loop) format.

The deterministic, judge-INDEPENDENT half of CLD grading (Structure §3.1/§4.6: "structure
scored programmatically … loop-polarity check, reference-label match"). It scores ONLY the
structural sub-score; the completeness/quality sub-score stays jury-graded and ships
`UNCALIBRATED — not scored` until a CLD gold set clears §3.1/§4.0 (fail-closed, §5.1). This
tool emits NO jury number.

Method (REUSE — Plate & Monroe 2010/2014; Research Part I.B / Open Q#1): parse a model's
structured CLD output, recompute each declared loop's polarity as the **product of its signed
edges**, and check it against (a) the model's own R/B label and (b) the item's oracle. Score
canonical-variable presence + required-signed-edge presence/polarity + loop inventory +
dominant-loop / key-delay naming. Apply the item partial-credit rule (structure right but the
dominant-loop-shift / delay insight missing = 0.5) and flag the named trap (R↔B mislabel of the
dominant loop / omitted loop).

Scoring policy (tool-internal implementation of the item-file prose — NOT governance; tunable,
flagged for later calibration against real responses):
  base = 0.50*edges + 0.30*loops + 0.20*variables          # structural identification, [0,1]
  insight_present (dynamic insight): for a dominant-shift item -> the shift is named AND the
    dominant loop is correctly identified; for a delay-driven item -> the key (driving) delay
    is named AND the dominant loop is correctly identified.
  final = base                  if insight_present
        = min(base, 0.50)       if structure present but insight missing  (the spec's 0.5 rule)
        = min(base, 0.25)       if the dominant loop is R<->B mislabelled  (trap -> low score)

Response schema (structured CLD the harness elicits; node names matched case/space-insensitively):
  {"variables": ["FishPopulation", ...],
   "edges":  [{"from": "FishPopulation", "to": "CatchRate", "sign": "+"}, ...],
   "loops":  [{"id": "B1", "type": "B", "nodes": ["FishPopulation", "CatchRate"]}, ...],
   "dominant_loop": "R1",
   "names_dominant_shift": true,
   "delays": [["Investment", "FleetSize"]]}

Subcommands:
  calibrate <oracle.json>                 fail-closed self-test (oracle loop-signs 11/11; each
                                          reference round-trips to 1.0; partial=0.5; trap<=0.25;
                                          omitted-loop<1.0). rc=0 iff every check passes.
  score <oracle.json> <ITEM_ID> <resp.json>   score one response; prints component breakdown.

No live-model spend; pure local computation (§4.6 / host rail).
"""
import json, re, sys, os

W_EDGES, W_LOOPS, W_VARS = 0.50, 0.30, 0.20
PARTIAL_CAP, TRAP_CAP = 0.50, 0.25

# ---------- normalization ----------

def norm(name):
    """case/space/punct-insensitive node key."""
    return re.sub(r"[^a-z0-9]", "", str(name).lower())

def sgn(s):
    """edge polarity token -> +1/-1 (tolerates unicode minus)."""
    t = str(s).strip()
    if t in ("+", "+1", "1", "pos", "positive", "same", "s"): return 1
    if t in ("-", "−", "-1", "neg", "negative", "opposite", "o"): return -1
    raise ValueError(f"unrecognized edge sign: {s!r}")

def edge_map(edges):
    """list of {from,to,sign} -> {(nfrom,nto): +/-1}; polarity is symmetric for lookup fallback."""
    m = {}
    for e in edges:
        a, b = norm(e["from"]), norm(e["to"])
        m[(a, b)] = sgn(e["sign"])
    return m

def lookup_sign(m, a, b):
    """directed lookup with reverse fallback (a CLD link's polarity is a property of the pair)."""
    if (a, b) in m: return m[(a, b)]
    if (b, a) in m: return m[(b, a)]
    return None

def loop_sign(nodes, m):
    """product of edge signs around the cycle nodes[0]->...->nodes[-1]->nodes[0].
    returns (+/-1 | None, all_edges_found)."""
    nn = [norm(x) for x in nodes]
    prod, ok = 1, True
    for i in range(len(nn)):
        s = lookup_sign(m, nn[i], nn[(i + 1) % len(nn)])
        if s is None:
            ok = False
        else:
            prod *= s
    return (prod if ok else None), ok

def type_of(sign):
    return "R" if sign > 0 else "B"

# ---------- oracle integrity ----------

def oracle_loop_checks(oracle):
    """For each loop, recompute sign from required_edges; must equal declared type. Returns rows."""
    rows = []
    for iid, it in oracle["items"].items():
        m = edge_map(it["required_edges"])
        for lp in it["loops"]:
            s, ok = loop_sign(lp["nodes"], m)
            declared = lp["type"]
            computed = type_of(s) if ok else "?"
            rows.append((iid, lp["id"], declared, computed, ok and declared == computed))
    return rows

# ---------- scoring ----------

def _resp_loops_by_nodeset(resp):
    out = {}
    for lp in resp.get("loops", []):
        key = frozenset(norm(x) for x in lp.get("nodes", []))
        out[key] = lp
    return out

def score(oracle_item, resp):
    cvars = [norm(v) for v in oracle_item["variables"]]
    rvars = set(norm(v) for v in resp.get("variables", []))
    var_hits = sum(1 for v in cvars if v in rvars)
    variables_score = var_hits / len(cvars) if cvars else 0.0

    rm = edge_map(resp.get("edges", []))
    req = oracle_item["required_edges"]
    edge_hits = sum(1 for e in req if lookup_sign(rm, norm(e["from"]), norm(e["to"])) == sgn(e["sign"]))
    edges_score = edge_hits / len(req) if req else 0.0

    # loops: oracle loop matched iff a response loop covers the same node-set AND labels it correctly.
    rby = _resp_loops_by_nodeset(resp)
    loop_hits, loop_detail = 0, []
    for olp in oracle_item["loops"]:
        oset = frozenset(norm(x) for x in olp["nodes"])
        rlp = rby.get(oset)
        matched = bool(rlp) and str(rlp.get("type", "")).upper().startswith(olp["type"])
        loop_hits += 1 if matched else 0
        loop_detail.append((olp["id"], olp["type"], (rlp.get("type") if rlp else None), matched))
    loops_score = loop_hits / len(oracle_item["loops"]) if oracle_item["loops"] else 0.0

    # dominant loop: map oracle dominant id -> its node-set; find response loop on that node-set.
    dom = next(l for l in oracle_item["loops"] if l["id"] == oracle_item["dominant_loop"])
    dom_set = frozenset(norm(x) for x in dom["nodes"])
    rdom = rby.get(dom_set)
    dominant_named = bool(rdom)
    dominant_mislabel = bool(rdom) and not str(rdom.get("type", "")).upper().startswith(dom["type"])

    # insight: dominant-shift named, or the key driving delay named — plus dominant correctly identified.
    rdelays = set((norm(a), norm(b)) for a, b in (tuple(d) for d in resp.get("delays", [])))
    key_delays = [(norm(e["from"]), norm(e["to"])) for e in req if e.get("delay")]
    delay_named = any(d in rdelays or (d[1], d[0]) in rdelays for d in key_delays)
    if oracle_item.get("dominant_shift"):
        insight = bool(resp.get("names_dominant_shift")) and dominant_named and not dominant_mislabel
    else:  # delay-driven item
        insight = delay_named and dominant_named and not dominant_mislabel

    base = W_EDGES * edges_score + W_LOOPS * loops_score + W_VARS * variables_score
    trap = dominant_mislabel
    if trap:
        final = min(base, TRAP_CAP)
    elif insight:
        final = base
    else:
        final = min(base, PARTIAL_CAP)

    return {
        "structural_subscore": round(final, 4),
        "base_structure": round(base, 4),
        "variables_score": round(variables_score, 4),
        "edges_score": round(edges_score, 4),
        "loops_score": round(loops_score, 4),
        "loops_matched": f"{loop_hits}/{len(oracle_item['loops'])}",
        "edges_matched": f"{edge_hits}/{len(req)}",
        "vars_matched": f"{var_hits}/{len(cvars)}",
        "dominant_named": dominant_named,
        "insight_present": bool(insight),
        "trap_fired": trap,
        "trap_kind": "dominant-loop R<->B mislabel" if trap else None,
        "loop_detail": loop_detail,
        "jury_completeness": "UNCALIBRATED — not scored",
    }

# ---------- perfect / partial / trap response builders (for the self-test) ----------

def perfect_resp(it):
    return {
        "variables": list(it["variables"]),
        "edges": [{"from": e["from"], "to": e["to"], "sign": e["sign"]} for e in it["required_edges"]],
        "loops": [{"id": l["id"], "type": l["type"], "nodes": list(l["nodes"])} for l in it["loops"]],
        "dominant_loop": it["dominant_loop"],
        "names_dominant_shift": True,
        "delays": [[e["from"], e["to"]] for e in it["required_edges"] if e.get("delay")],
    }

def partial_resp(it):
    r = perfect_resp(it)
    r["names_dominant_shift"] = False
    r["delays"] = []  # structure right, dynamic insight (shift / driving delay) absent
    return r

def trap_resp(it):
    r = perfect_resp(it)
    flip = {"R": "B", "B": "R"}
    for lp in r["loops"]:
        if lp["id"] == it["dominant_loop"]:
            lp["type"] = flip[lp["type"]]
    return r

def drop_loop_resp(it):
    r = perfect_resp(it)
    if len(r["loops"]) > 1:
        r["loops"] = r["loops"][:-1]
    return r

# ---------- subcommands ----------

def approx(a, b, tol=1e-6): return abs(a - b) <= tol

def cmd_calibrate(path):
    oracle = json.load(open(path))
    checks = []

    rows = oracle_loop_checks(oracle)
    good = sum(1 for r in rows if r[4])
    for iid, lid, dec, comp, ok in rows:
        checks.append((f"oracle loop-sign {iid}/{lid}: declared {dec} == product-of-edges {comp}", ok))
    checks.append((f"oracle loop-sign total: {good}/{len(rows)} consistent (expect 11/11)",
                   good == len(rows) == 11))

    for iid, it in oracle["items"].items():
        rp = score(it, perfect_resp(it))
        checks.append((f"{iid}: reference solution round-trips to 1.0 (got {rp['structural_subscore']})",
                       approx(rp["structural_subscore"], 1.0) and not rp["trap_fired"]))
        pp = score(it, partial_resp(it))
        checks.append((f"{iid}: structure-without-insight = 0.5 (got {pp['structural_subscore']})",
                       approx(pp["structural_subscore"], 0.5)))
        tp = score(it, trap_resp(it))
        checks.append((f"{iid}: dominant R<->B mislabel -> trap & <=0.25 (got {tp['structural_subscore']}, "
                       f"trap={tp['trap_fired']})", tp["trap_fired"] and tp["structural_subscore"] <= 0.25))
        if len(it["loops"]) > 1:
            dp = score(it, drop_loop_resp(it))
            checks.append((f"{iid}: omitted-loop response < 1.0 (got {dp['structural_subscore']})",
                           dp["structural_subscore"] < 1.0))

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
    print(f"# CLD structural score — {item_id}")
    print(json.dumps(res, indent=2))
    return 0

def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "calibrate": return cmd_calibrate(a[1])
    if len(a) == 4 and a[0] == "score": return cmd_score(a[1], a[2], a[3])
    print(__doc__); return 1

if __name__ == "__main__":
    sys.exit(main())
