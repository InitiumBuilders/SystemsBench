#!/usr/bin/env python3
"""sf-score.py — deterministic scorer for the SF (stock-flow inference) format.

Structure §3.1 names SF as the format graded by computation, not opinion: given the
flows, infer the stock's path. This scorer grades the STRUCTURED answer fields the
harness elicits (a number, a direction, a named shape, a time, a weekday, a yes/no)
against items/sf_oracle.json. The mechanism prose that L3 items also ask for stays
jury-graded and ships `UNCALIBRATED — not scored` until an SF gold set clears §3.1
(fail-closed, Structure §5.1). This scorer emits NO jury number.

Scoring
  sf_subscore = matched fields / fields.
  A number matches within the item's tolerance (default 0.5% of |expected|, never
  below 0.5). A word matches through a synonym table (increasing → rising,
  plateaus → levels-off), so a model is graded on what it meant, not on spelling.
  THE TRAP: each item names the naive answer(s), almost always the correlation
  heuristic in one of its forms (a constant flow read as a constant stock, a falling
  flow read as a falling stock, a flow reported as the stock). If the response gives a
  trap value for any trap field, the score is capped at 0.25. A right number with a
  wrong direction is 0.5, not the trap, unless that wrong direction IS the named trap.

Usage
  calibrate <oracle.json>                    fail-closed self-test, rc=0 iff every check passes:
                                             each item exists in the seed file at the same level;
                                             every expected number appears in the seed's own oracle
                                             line and every expected word has a synonym there (the
                                             oracle is TRANSCRIBED, and the transcription is checked);
                                             each reference round-trips to 1.0 with no trap; each named
                                             trap fires and caps ≤ 0.25; a one-field-wrong answer scores
                                             < 1.0; a synonym / stringy-number reply still scores 1.0.
  score <oracle.json> <ITEM_ID> <resp.json>  score one response; prints the field breakdown.

No live-model spend; pure local computation. Added in SenseRun #13.
"""
import json, os, re, sys

TRAP_CAP = 0.25

# ---------- vocabulary: canonical -> synonyms (normalized: lowercase, alphanumerics only) ----------
VOCAB = {
    "direction": [
        ("rising",  ["rising", "rise", "rises", "rose", "increasing", "increase", "increases", "up", "upward", "growing",
                     "grows", "grow", "higher", "gain", "gaining", "accumulating", "climbing", "climbs"]),
        ("falling", ["falling", "fall", "falls", "fell", "decreasing", "decrease", "decreases", "down", "downward",
                     "declining", "declines", "decline", "lower", "shrinking", "shrinks", "shrink", "dropping", "drops",
                     "drawdown", "drawndown", "draining", "drains"]),
        ("steady",  ["steady", "constant", "flat", "stable", "unchanged", "same", "nochange", "level", "holds",
                     "holding", "holdssteady", "static", "equilibrium"]),
    ],
    "shape": [
        ("keeps-rising",        ["keepsrising", "keeprising", "stillrising", "keepsgrowing", "keepgrowing", "continuestorise",
                                 "continuesrising", "keepsclimbing", "growing", "rising", "rises", "increasing", "up", "keepsincreasing",
                                 "continuestogrow", "stillgrowing", "risesmoreslowly", "keepsaccumulating"]),
        ("keeps-falling",       ["keepsfalling", "keepfalling", "stillfalling", "keepsdeclining", "keepdeclining", "declining", "declines",
                                 "falling", "falls", "decreasing", "shrinking", "shrinks", "keepsshrinking", "drawndown", "drawdown",
                                 "deficit", "down", "goesdown", "keepsdropping", "drainstozero", "goesaway", "disappears", "declinestowardzero"]),
        ("levels-off",          ["levelsoff", "leveloff", "levelsout", "plateau", "plateaus", "steadystate", "ceiling", "stabilizes",
                                 "stabilises", "stabilize", "stabilise", "holds", "holdssteady", "steady", "settles", "asymptote",
                                 "asymptotes", "saturates", "stopsgrowing", "stopsrising", "staysflat", "flat", "holdsroughlywhereitis",
                                 "stayshigh", "stays", "hitsaceiling", "approachesasteadystate", "stable", "unchanged", "constant"]),
        ("unbounded",           ["unbounded", "growswithoutbound", "riseswithoutbound", "withoutbound", "withoutlimit", "forever",
                                 "unlimited", "growsforever", "risesforever", "nolimit", "indefinitely", "growswithoutlimit"]),
        ("linear",              ["linear", "linearly", "straightline", "constantrate", "steadyrate"]),
        ("accelerates",         ["accelerates", "accelerating", "accelerate", "exponential", "exponentially", "compounding", "compounds",
                                 "curvesup", "speedsup", "acceleratinggrowth", "fasterandfaster", "reinforcing"]),
        ("overshoot",           ["overshoot", "overshoots", "overshooting", "boombust", "boomandbust", "overshootsthensettles",
                                 "keepsrisingthenovershoots"]),
        ("oscillates",          ["oscillates", "oscillation", "oscillating", "oscillate", "oscillations", "cycles", "cycling",
                                 "overshootsandoscillates", "swings", "huntsaround"]),
        ("worse-before-better", ["worsebeforebetter", "fallsthenrecovers", "fallsfirstthenrecovers", "keepsfallingfirst",
                                 "keepsfallingthenrecovers", "dipthenrecover", "dipsthenrecovers", "fallsthenrises", "thenslowlyrecovers",
                                 "recovers", "recoverslater", "downthenup"]),
        ("rise-then-level",     ["risethenlevel", "risesthenlevelsoff", "keepsrisingthenlevelsoff", "delayedrise", "keepsrisingforawhile",
                                 "risesforawhile", "keepsrisingfordecades", "risesthenplateaus", "keepsrisingbeforelevelingoff",
                                 "risesthensettles", "risesbeforelevelingoff"]),
        ("overshoot-undershoot",["overshootundershoot", "undershoot", "undershoots", "spikethenundershoot", "overshootthenundershoot",
                                 "dipsbelow", "dipbelow", "dipsbelownormal", "spikesthendips", "reactive", "belowbaseline", "spikesup"]),
        ("diverges",            ["diverges", "diverge", "diverging", "widens", "widen", "widening", "gapwidens", "gapgrows", "compoundsapart"]),
    ],
    "day": [(d, [d, d[:3]] + (["tues"] if d == "tuesday" else []) + (["thur", "thurs"] if d == "thursday" else []) + (["weds"] if d == "wednesday" else []))
            for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]],
    "yesno": [("yes", ["yes", "y", "true", "yeah", "itdoes", "itwill", "itis"]),
              ("no",  ["no", "n", "false", "nope", "itdoesnot", "itdoesnt", "itwillnot", "itwont", "itisnot", "itisnt"])],
}
WORD_KINDS = set(VOCAB)


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def cnum(v):
    """number from a number or a stringy number: '$650', '10,100 people', '+500', '78%' -> float; None if none."""
    if isinstance(v, bool): return None
    if isinstance(v, (int, float)): return float(v)
    if v is None: return None
    s = str(v).replace(",", "")
    m = re.search(r"[-+]?\d+(?:\.\d+)?", s)
    return float(m.group(0)) if m else None


def cword(kind, v):
    """canonical word for a kind, or None. Exact synonym first; then the longest synonym contained in the reply."""
    if v is None: return None
    n = norm(v)
    if not n: return None
    for canon, syns in VOCAB[kind]:
        if n == norm(canon) or n in syns:
            return canon
    best = None
    for canon, syns in VOCAB[kind]:
        for s in sorted(syns, key=len, reverse=True):
            if len(s) >= 4 and s in n and (best is None or len(s) > best[1]):
                best = (canon, len(s))
    return best[0] if best else None


def tol_of(spec):
    if spec.get("tolerance") is not None: return float(spec["tolerance"])
    return max(0.5, 0.005 * abs(float(spec["expected"])))


def field_match(spec, got):
    kind = spec["kind"]
    if kind == "number":
        g = cnum(got)
        return (g is not None) and abs(g - float(spec["expected"])) <= tol_of(spec), g
    c = cword(kind, got)
    accept = [spec["expected"]] + list(spec.get("accept", []))
    return (c in accept), c


def trap_hit(oracle_item, answers):
    """True if any trap field is answered with one of its trap values (the naive answer)."""
    trap = oracle_item.get("trap") or {}
    for f, vals in trap.items():
        spec = oracle_item["fields"].get(f)
        if spec is None or f not in answers: continue
        got = answers[f]
        for tv in vals:
            if spec["kind"] == "number":
                g = cnum(got)
                if g is not None and abs(g - float(tv)) <= max(0.5, 0.005 * abs(float(tv))): return True, f, tv
            else:
                if cword(spec["kind"], got) == tv: return True, f, tv
    return False, None, None


def score(oracle_item, resp):
    answers = resp.get("answers") if isinstance(resp, dict) else None
    if not isinstance(answers, dict): answers = {}
    fields = oracle_item["fields"]
    out, hits = {}, 0
    for f, spec in fields.items():
        ok, got = field_match(spec, answers.get(f))
        hits += 1 if ok else 0
        out[f] = {"expected": spec["expected"], "got": got, "raw": answers.get(f), "match": bool(ok)}
    base = hits / len(fields) if fields else 0.0
    fired, tf, tv = trap_hit(oracle_item, answers)
    final = min(base, TRAP_CAP) if fired else base
    return {
        "sf_subscore": round(final, 4),
        "base_match": round(base, 4),
        "fields": out,
        "trap_fired": bool(fired),
        "trap_kind": (f"answered the trap for '{tf}' ({tv}): {oracle_item.get('trap_text', '')}" if fired else None),
        "jury_mechanism": "UNCALIBRATED — not scored",
    }


# ---------- response builders (for the self-tests; the harness uses perfect_resp and synonym_resp) ----------

def perfect_resp(it):
    return {"answers": {f: spec["expected"] for f, spec in it["fields"].items()}}


def _other_word(kind, avoid):
    for canon, _ in VOCAB[kind]:
        if canon not in avoid: return canon
    return "steady"


def degraded_resp(it):
    r = perfect_resp(it)
    f, spec = next(iter(it["fields"].items()))
    if spec["kind"] == "number":
        r["answers"][f] = float(spec["expected"]) * 1.5 + 7
    else:
        r["answers"][f] = _other_word(spec["kind"], [spec["expected"]] + list(spec.get("accept", [])))
    return r


def trap_resp(it):
    r = perfect_resp(it)
    trap = it.get("trap") or {}
    if not trap: return None
    f, vals = next(iter(trap.items()))
    r["answers"][f] = vals[0]
    return r


def synonym_resp(it):
    """the same answer said the way a model says it: numbers as strings with units, words as synonyms."""
    r = {"answers": {}}
    for f, spec in it["fields"].items():
        if spec["kind"] == "number":
            e = float(spec["expected"])
            s = ("%d" % e if e == int(e) else str(e))
            if len(s) > 3: s = "{:,}".format(int(e)) if e == int(e) else s
            r["answers"][f] = "$" + s if "dollar" in spec.get("ask", "") else s + " " + (spec.get("unit") or "")
        else:
            syns = dict(VOCAB[spec["kind"]])[spec["expected"]]
            r["answers"][f] = syns[1] if len(syns) > 1 else syns[0]
    return r


# ---------- calibrate: the oracle is transcribed, and the transcription is checked against the seed ----------

def _seed_blocks(seed_path):
    t = open(seed_path, encoding="utf-8").read()
    out = {}
    for b in re.split(r"\n(?=## SF-)", t):
        m = re.match(r"## (SF-[A-Z0-9-]+) \(([^)]*)\)", b)
        if not m: continue
        lvl = re.search(r"\bL[1-4]\b", m.group(2))
        o = re.search(r"\*\*Oracle[^:]*:\*\*\s*(.*)", b)
        out[m.group(1)] = {"level": lvl.group(0) if lvl else None, "oracle": o.group(1) if o else ""}
    return out


def _fmt_num(x):
    x = float(x)
    return "%d" % x if x == int(x) else str(x)


def cmd_calibrate(path):
    oracle = json.load(open(path))
    seed_path = os.path.join(os.path.dirname(os.path.abspath(path)), "seed_SF_stockflow.md")
    seed = _seed_blocks(seed_path) if os.path.exists(seed_path) else {}
    checks = []
    for iid, it in oracle["items"].items():
        sb = seed.get(iid)
        checks.append((f"{iid}: exists in the seed file at level {it.get('level')}", bool(sb) and sb["level"] == it.get("level")))
        line = norm(sb["oracle"]) if sb else ""
        for f, spec in it["fields"].items():
            if spec.get("check", True) is False: continue
            if spec["kind"] == "number":
                checks.append((f"{iid}.{f}: expected number {_fmt_num(spec['expected'])} appears in the seed's oracle line",
                               _fmt_num(spec["expected"]) in line))
            else:
                cands = [spec["expected"]] + list(spec.get("accept", []))
                syns = [s for c in cands for s in dict(VOCAB[spec["kind"]]).get(c, [])] + [norm(c) for c in cands]
                checks.append((f"{iid}.{f}: a synonym of '{spec['expected']}' appears in the seed's oracle line",
                               any(s in line for s in syns if len(s) >= 3)))
        rp = score(it, perfect_resp(it))
        checks.append((f"{iid}: reference round-trips to 1.0 (got {rp['sf_subscore']})", abs(rp["sf_subscore"] - 1.0) < 1e-9 and not rp["trap_fired"]))
        sp = score(it, synonym_resp(it))
        checks.append((f"{iid}: synonym / stringy-number reply -> 1.0 (got {sp['sf_subscore']})", abs(sp["sf_subscore"] - 1.0) < 1e-9))
        dp = score(it, degraded_resp(it))
        checks.append((f"{iid}: one-field-wrong reply < 1.0 (got {dp['sf_subscore']})", dp["sf_subscore"] < 1.0))
        tr = trap_resp(it)
        if tr is not None:
            tp = score(it, tr)
            checks.append((f"{iid}: the named trap fires and caps <= {TRAP_CAP} (got {tp['sf_subscore']}, trap={tp['trap_fired']})",
                           tp["trap_fired"] and tp["sf_subscore"] <= TRAP_CAP))
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        if not ok: print("FAIL  " + n)
    print(f"calibrate: {len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


def cmd_score(path, item_id, resp_path):
    oracle = json.load(open(path))
    if item_id not in oracle["items"]:
        print(f"score: unknown item {item_id} (have: {', '.join(oracle['items'])})", file=sys.stderr)
        return 2
    resp = json.load(open(resp_path))
    res = score(oracle["items"][item_id], resp)
    print(f"# SF score — {item_id}")
    print(json.dumps(res, indent=2))
    return 0


def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "calibrate": return cmd_calibrate(a[1])
    if len(a) == 4 and a[0] == "score": return cmd_score(a[1], a[2], a[3])
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main())
