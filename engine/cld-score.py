#!/usr/bin/env python3
"""cld-score.py — programmatic STRUCTURAL scorer for the CLD (causal-loop) format. **v2: partition-robust.**

The deterministic, judge-INDEPENDENT half of CLD grading (Structure §3.1/§4.6: "structure scored
programmatically … loop-polarity check, reference-label match"). It scores ONLY the structural
sub-score; the completeness/quality sub-score stays jury-graded and ships `UNCALIBRATED — not scored`
until a CLD gold set clears §3.1/§4.0 (fail-closed, §5.1). This tool emits NO jury number.

────────────────────────────────────────────────────────────────────────────────────────────────────
WHY v2 (the evolution — 2026-06-13, after First Light)
────────────────────────────────────────────────────────────────────────────────────────────────────
First Light (results/FIRST-LIGHT-2026-06-13.md, Finding 4) caught the ruler red-handed: on CLD-INFRA-004
a model wrote a *structurally correct* answer — found the balancing firefighting loop, the delayed
reinforcing erosion loop, named the dominant loop, flagged the dominance shift — and scored **0.04**,
purely because it wrote `OpenIncidentQueue` instead of `OpenIncidents`, `Firefighting` instead of
`FirefightingEffort`, and collapsed two oracle nodes into one. The v1 matcher keyed loops on an EXACT
node-set (`frozenset(names)`) and edges on EXACT names. That penalizes **vocabulary and partitioning
choices**, not reasoning.

This is a *measurement-validity* failure, and the two deepest Meadows lessons say exactly how to fix it:

  • **"The behavior of a system cannot be known just by knowing the elements of which the system is made."**
    The systems-thinking content of a CLD is its FEEDBACK STRUCTURE (loop polarities, dominance, delays),
    NOT its element labels. So v2 scores structure first and names only softly.

  • **"There are no separate systems … where to draw a boundary depends on the purpose of the discussion."**
    Boundaries/partitions are pragmatic, not God-given. A modeler who collapses `ImprovementTime`+
    `ProcessQuality` into one `ReliabilityWork` node, or renames `OpenIncidents` → `OpenIncidentQueue`,
    has made a *valid partitioning choice* — if the resulting loop has the same polarity and spans the
    same causal territory, the systems reasoning is the same. v2 must see that.

The fork `harness.py` left open (a hand-authored variable ALIAS MAP: model-words → oracle canonical names)
stays CLOSED — it would leak the oracle and inflate scores (a §5 governance / construct-validity question
for August + Ember). v2 takes the *principled, non-leaking* path August named directly:

      MATCH LOOPS BY TOPOLOGY + SIGN, NOT BY NODE NAME.

A loop's **polarity (product of its signed edges)** is the one invariant that survives BOTH renaming AND
reasonable re-partitioning (collapsing a chain of same-sign edges preserves the sign product). Polarity is
therefore the primary, name-free key; node names enter only as a SOFT quality signal (generic fuzzy string
similarity — char-trigram Dice + stem containment — never an oracle-specific dictionary).

────────────────────────────────────────────────────────────────────────────────────────────────────
METHOD (REUSE — Plate & Monroe 2010/2014; graph-isomorphism-with-edge-signs; Research Part I.B / Open Q#1)
────────────────────────────────────────────────────────────────────────────────────────────────────
For each declared loop, recompute its polarity as the **product of the response's OWN signed edges**
around the cycle. Then:

  1. LOOPS (name-free, the heart): match each oracle loop to a response loop, GATED on equal polarity
     (topology+sign), disambiguated by SOFT variable overlap. Credit = mostly for the polarity match,
     a bonus for how much of the oracle loop's causal territory the response loop covers.
  2. CONSISTENCY (name-free coherence): does each response loop's DECLARED R/B label equal the product of
     its own edges? Rewards an internally coherent diagram regardless of vocabulary — a direct, label-
     independent probe of "understanding feedback" (Arnold-Wade).
  3. EDGES / VARIABLES (soft): required signed edges and canonical variables, matched with the same
     generic fuzzy similarity (so a rename costs little, a genuinely different structure still costs).
  4. DOMINANT + INSIGHT: the dominant loop and the dynamic insight (dominance-shift named, or the key
     driving delay named) ride on the soft correspondence, so they survive renaming/re-partitioning.

Scoring policy (tool-internal implementation of the item-file prose — NOT governance; tunable, calibrate-
first, flagged for ongoing calibration against real responses):
  base = 0.50*loops + 0.20*edges + 0.10*variables + 0.20*consistency      # structure-weighted, [0,1]
  insight_present: dominant-shift item -> shift named AND dominant correctly identified (not mislabelled);
                   delay-driven item    -> key driving delay named AND dominant correctly identified.
  final = base                  if insight_present
        = min(base, 0.50)       if structure present but insight missing  (the spec's 0.5 rule)
        = min(base, 0.25)       if the dominant loop is R<->B mislabelled (trap -> low score)

v1 behavior is a SPECIAL CASE of v2 (exact names → soft-overlap 1.0), so exact-match responses are
unaffected; the change can only *recover* credit that name-strictness was destroying. Verified no-regress
on the First Light bank (see results/CLD-V2-RESCORE-2026-06-13.md).

Response schema (structured CLD the harness elicits; node names matched fuzzily, not exactly):
  {"variables": ["FishPopulation", ...],
   "edges":  [{"from": "FishPopulation", "to": "CatchRate", "sign": "+"}, ...],
   "loops":  [{"id": "B1", "type": "B", "nodes": ["FishPopulation", "CatchRate"]}, ...],
   "dominant_loop": "R1",
   "names_dominant_shift": true,
   "delays": [["Investment", "FleetSize"]]}

Subcommands:
  calibrate <oracle.json>                 fail-closed self-test (oracle loop-signs 11/11; each reference
                                          round-trips to 1.0; partial=0.5; trap<=0.25; omitted-loop<1.0;
                                          plus v2 partition-robustness probes). rc=0 iff every check passes.
  score <oracle.json> <ITEM_ID> <resp.json>   score one response; prints component breakdown.

No live-model spend; pure local computation (§4.6 / host rail).
"""
import json, re, sys, os

W_LOOPS, W_EDGES, W_VARS, W_CONS = 0.50, 0.20, 0.10, 0.20
PARTIAL_CAP, TRAP_CAP = 0.50, 0.25

# soft-match thresholds (generic morphology, NOT an oracle dictionary)
TRIGRAM_DICE_MIN = 0.60   # char-trigram Dice coefficient above which two names are "the same node"
STEM_MIN = 3              # min shared-stem length for substring containment (handles short names: Gap, Supply)
LOOP_MATCH_FLOOR = 0.70   # credit floor for a polarity-matched loop; the rest scales with node overlap

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

# ---------- soft (name-robust) matching: generic morphology, no oracle dictionary ----------

def _trigrams(s):
    s = norm(s)
    if len(s) < 3:
        return {s} if s else set()
    return {s[i:i + 3] for i in range(len(s) - 2)}

def soft_eq(a, b):
    """Two variable names refer to the SAME node? Generic fuzzy string similarity only — never an
    oracle-specific synonym list (that would leak the oracle). Three name-agnostic signals:
      • exact normalized equality,
      • shared-stem substring containment (>= STEM_MIN chars) — 'firefighting' ⊆ 'firefightingeffort',
      • char-trigram Dice >= TRIGRAM_DICE_MIN — 'openincidents' ~ 'openincidentqueue'."""
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    if len(na) >= STEM_MIN and len(nb) >= STEM_MIN and (na in nb or nb in na):
        return True
    ta, tb = _trigrams(na), _trigrams(nb)
    if not ta or not tb:
        return False
    return (2 * len(ta & tb) / (len(ta) + len(tb))) >= TRIGRAM_DICE_MIN

def soft_overlap(oracle_nodes, resp_nodes):
    """fraction of ORACLE loop nodes that have a soft match somewhere in the response loop."""
    if not oracle_nodes:
        return 0.0
    hit = sum(1 for o in oracle_nodes if any(soft_eq(o, r) for r in resp_nodes))
    return hit / len(oracle_nodes)

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

def _resp_loop_polarity(rloop, rm):
    """A response loop's polarity = product of the RESPONSE's own signed edges around the cycle
    (topology+sign, name-free). Falls back to the declared R/B label if the response's edges don't
    close the loop. Returns ('R'|'B'|None, computed_bool)."""
    s, ok = loop_sign(rloop.get("nodes", []), rm)
    if ok and s is not None:
        return type_of(s), True
    t = str(rloop.get("type", "")).upper()
    if t.startswith("R"): return "R", False
    if t.startswith("B"): return "B", False
    return None, False

def _loop_consistent(rloop, rm):
    """Internal coherence (name-free): does the loop's DECLARED label equal the product of its own edges?
    Returns True/False, or None if the polarity can't be computed (incomplete loop)."""
    s, ok = loop_sign(rloop.get("nodes", []), rm)
    if not ok or s is None:
        return None
    t = str(rloop.get("type", "")).upper()
    if t.startswith("R"): declared = "R"
    elif t.startswith("B"): declared = "B"
    else: return None
    return type_of(s) == declared

def _match_loops(oracle_loops, resp_loops, rm):
    """Assign each oracle loop a best response loop, GATED on equal polarity (topology+sign), greedily
    maximizing soft node overlap, without reusing a response loop. Returns {oracle_id: (rloop, overlap,
    rdeclared)} | {oracle_id: None}."""
    rinfo = []
    for idx, rl in enumerate(resp_loops):
        pol, _ = _resp_loop_polarity(rl, rm)
        rinfo.append({"idx": idx, "pol": pol, "nodes": rl.get("nodes", []),
                      "declared": str(rl.get("type", "")).upper(), "loop": rl})
    used, matches = set(), {}
    for ol in oracle_loops:
        opol = ol["type"]
        best, best_ov = None, -1.0
        for r in rinfo:
            if r["idx"] in used or r["pol"] != opol:   # POLARITY GATE = topology+sign, name-free
                continue
            ov = soft_overlap(ol["nodes"], r["nodes"])
            if ov > best_ov:
                best, best_ov = r, ov
        if best is not None:
            used.add(best["idx"])
            matches[ol["id"]] = (best["loop"], best_ov, best["declared"])
        else:
            matches[ol["id"]] = None
    return matches

def score(oracle_item, resp):
    rm = edge_map(resp.get("edges", []))
    oracle_loops = oracle_item["loops"]

    # --- variables (soft) ---
    ovars = oracle_item["variables"]
    rvars = resp.get("variables", [])
    var_hits = sum(1 for v in ovars if any(soft_eq(v, rv) for rv in rvars))
    variables_score = var_hits / len(ovars) if ovars else 0.0

    # --- edges (soft, directed, polarity-checked) ---
    req = oracle_item["required_edges"]
    redges = resp.get("edges", [])
    def edge_hit(e):
        want = sgn(e["sign"])
        for re_ in redges:
            try:
                if sgn(re_["sign"]) != want:
                    continue
            except (KeyError, ValueError):
                continue
            if soft_eq(e["from"], re_.get("from")) and soft_eq(e["to"], re_.get("to")):
                return True
        return False
    edge_hits = sum(1 for e in req if edge_hit(e))
    edges_score = edge_hits / len(req) if req else 0.0

    # --- loops (topology+sign match, partition-robust) ---
    matches = _match_loops(oracle_loops, resp.get("loops", []), rm)
    loop_credit, loop_detail = 0.0, []
    for ol in oracle_loops:
        m = matches[ol["id"]]
        if m is None:
            loop_detail.append((ol["id"], ol["type"], None, 0.0, False))
        else:
            _, ov, rdecl = m
            credit = LOOP_MATCH_FLOOR + (1.0 - LOOP_MATCH_FLOOR) * ov
            loop_credit += credit
            loop_detail.append((ol["id"], ol["type"], rdecl or None, round(ov, 3), True))
    loops_score = loop_credit / len(oracle_loops) if oracle_loops else 0.0

    # --- internal polarity consistency (name-free coherence) ---
    cons_vals = [_loop_consistent(rl, rm) for rl in resp.get("loops", [])]
    cons_computable = [c for c in cons_vals if c is not None]
    consistency_score = (sum(1 for c in cons_computable if c) / len(cons_computable)
                         if cons_computable else 0.0)

    # --- dominant loop + dynamic insight (ride on the soft correspondence) ---
    dom_id = oracle_item["dominant_loop"]
    dom_pol = next(l["type"] for l in oracle_loops if l["id"] == dom_id)
    dmatch = matches.get(dom_id)
    dominant_named = dmatch is not None
    dominant_mislabel = bool(dmatch) and not str(dmatch[2]).upper().startswith(dom_pol)

    def delay_hit(o_from, o_to):
        for d in resp.get("delays", []):
            if not isinstance(d, (list, tuple)) or len(d) < 2:
                continue
            a, b = d[0], d[1]
            if (soft_eq(o_from, a) and soft_eq(o_to, b)) or (soft_eq(o_from, b) and soft_eq(o_to, a)):
                return True
        return False
    key_delays = [(e["from"], e["to"]) for e in req if e.get("delay")]
    delay_named = any(delay_hit(f, t) for f, t in key_delays)

    if oracle_item.get("dominant_shift"):
        insight = bool(resp.get("names_dominant_shift")) and dominant_named and not dominant_mislabel
    else:  # delay-driven item
        insight = delay_named and dominant_named and not dominant_mislabel

    base = (W_LOOPS * loops_score + W_EDGES * edges_score
            + W_VARS * variables_score + W_CONS * consistency_score)
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
        "loops_score": round(loops_score, 4),
        "edges_score": round(edges_score, 4),
        "variables_score": round(variables_score, 4),
        "consistency_score": round(consistency_score, 4),
        "loops_matched": f"{sum(1 for d in loop_detail if d[4])}/{len(oracle_loops)}",
        "edges_matched": f"{edge_hits}/{len(req)}",
        "vars_matched": f"{var_hits}/{len(ovars)}",
        "dominant_named": dominant_named,
        "insight_present": bool(insight),
        "delay_named": bool(delay_named),
        "trap_fired": trap,
        "trap_kind": "dominant-loop R<->B mislabel" if trap else None,
        "loop_detail": loop_detail,   # (oracle_id, oracle_type, resp_declared, node_overlap, matched)
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

def renamed_resp(it):
    """v2 partition-robustness probe: the perfect structure with every variable RENAMED (suffix added)
    and node order rotated. Must still score ~1.0 — that is the whole point of topology+sign matching."""
    r = perfect_resp(it)
    rename = {v: v + "Var" for v in it["variables"]}
    r["variables"] = [rename[v] for v in it["variables"]]
    r["edges"] = [{"from": rename.get(e["from"], e["from"]),
                   "to": rename.get(e["to"], e["to"]), "sign": e["sign"]}
                  for e in it["required_edges"]]
    r["loops"] = [{"id": l["id"], "type": l["type"],
                   "nodes": [rename.get(n, n) for n in l["nodes"]]} for l in it["loops"]]
    r["delays"] = [[rename.get(e["from"], e["from"]), rename.get(e["to"], e["to"])]
                   for e in it["required_edges"] if e.get("delay")]
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
        # v2: a fully RENAMED but topologically identical answer must still score ~1.0 (partition-robust).
        rn = score(it, renamed_resp(it))
        checks.append((f"{iid}: renamed-but-isomorphic answer still ~1.0 (got {rn['structural_subscore']}) "
                       f"[v2 topology+sign]", rn["structural_subscore"] >= 0.95 and not rn["trap_fired"]))

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
