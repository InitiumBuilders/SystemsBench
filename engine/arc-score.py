#!/usr/bin/env python3
"""arc-score.py — deterministic scorer for the ARC (archetype recognition) format.

Structure §3.1 grades ARC by "reference label (auto) + jury for the escape". This scorer grades
the LABEL against items/arc_oracle.json. The trap the archetype creates and the escape are the
jury's portion and ship `UNCALIBRATED — not scored` until an ARC gold set clears §3.1
(fail-closed, Structure §5.1). This scorer emits NO jury number.

Scoring (arc_subscore)
  1.0   the reference archetype (any alias in the table below reads as its canonical label)
  0.25  the item's named CONFUSABLE: the archetype the surface most resembles. This is the trap,
        and it wins over the family rule below even when the confusable shares the family.
  0.5   another archetype from the same family (the plot is in the right neighborhood)
  0.0   any other archetype, or a label the table does not recognize

Families  growth-limits: limits-to-growth · growth-and-underinvestment
          symptomatic-relief: shifting-the-burden · fixes-that-fail
          rivalry: escalation · accidental-adversaries · success-to-the-successful
          commons: tragedy-of-the-commons          standards: eroding-goals

Usage
  calibrate <oracle.json>                    fail-closed self-test, rc=0 iff every check passes:
                                             each item exists in the seed at the same level; its
                                             reference and confusable labels are canonical, differ,
                                             and are the ones written in the seed's own Reference and
                                             Confusable lines; every archetype appears at every level;
                                             the reference round-trips to 1.0 with no trap; an alias
                                             scores 1.0; the confusable fires and caps at 0.25; a
                                             same-family other label scores 0.5; an unrelated label 0.
  score <oracle.json> <ITEM_ID> <resp.json>  score one response; prints the breakdown.

No live-model spend; pure local computation. Added in SenseRun #14.
"""
import json, os, re, sys

TRAP_CAP = 0.25
FAMILY_CREDIT = 0.5

FAMILY = {
    "limits-to-growth": "growth-limits", "growth-and-underinvestment": "growth-limits",
    "shifting-the-burden": "symptomatic-relief", "fixes-that-fail": "symptomatic-relief",
    "escalation": "rivalry", "accidental-adversaries": "rivalry", "success-to-the-successful": "rivalry",
    "tragedy-of-the-commons": "commons",
    "eroding-goals": "standards",
}
CANON = list(FAMILY)

# aliases, normalized (lowercase, alphanumerics only); the canonical label's own normalization is implied
ALIASES = {
    "limits-to-growth": ["limitstosuccess", "limittogrowth", "limitsofgrowth", "growthlimit", "growthmeetsalimit", "saturation"],
    "growth-and-underinvestment": ["growthunderinvestment", "underinvestment", "growthwithunderinvestment", "capacityunderinvestment"],
    "shifting-the-burden": ["shiftedburden", "shiftingburden", "burdenshifting", "addiction", "shiftingtheburdentotheintervener",
                            "symptomaticsolution", "dependenceontheintervener"],
    "fixes-that-fail": ["fixthatfails", "fixesthatbackfire", "fixthatbackfires", "fixesfail", "backfiringfix", "quickfixthatfails",
                        "fixesthatfails"],
    "escalation": ["armsrace", "escalatingcompetition", "escalatingconflict", "titfortat", "pricewar"],
    "accidental-adversaries": ["accidentaladversary", "partnersturnedadversaries", "unintendedadversaries"],
    "success-to-the-successful": ["successtosuccessful", "richgetricher", "mattheweffect", "winnertakeall", "winnertakesall",
                                  "cumulativeadvantage", "successbreedssuccess"],
    "tragedy-of-the-commons": ["commons", "tragedyofcommons", "commonsdilemma", "overuseofacommons", "sharedresourcedepletion"],
    "eroding-goals": ["driftinggoals", "erodinggoal", "erodingstandards", "goalerosion", "loweringthebar", "driftingstandards",
                      "goaldrift", "boiledfrog"],
}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def cword(v):
    """canonical archetype for a reply, or None. Exact canonical/alias first; then the longest alias
    or canonical contained in the reply (so 'the tragedy of the commons, clearly' still reads)."""
    if v is None: return None
    n = norm(v)
    if not n: return None
    for c in CANON:
        if n == norm(c) or n in ALIASES[c]: return c
    best = None
    for c in CANON:
        for s in [norm(c)] + ALIASES[c]:
            if len(s) >= 6 and s in n and (best is None or len(s) > best[1]):
                best = (c, len(s))
    return best[0] if best else None


def score(oracle_item, resp):
    raw = resp.get("archetype") if isinstance(resp, dict) else None
    got = cword(raw)
    exp, conf = oracle_item["archetype"], oracle_item.get("confusable")
    if got == exp:
        s, why = 1.0, "reference archetype"
    elif conf and got == conf:
        s, why = TRAP_CAP, f"the named confusable ({conf}): {oracle_item.get('confusable_text', '')}"
    elif got and FAMILY.get(got) == FAMILY.get(exp):
        s, why = FAMILY_CREDIT, f"same family ({FAMILY[exp]}), wrong archetype"
    elif got:
        s, why = 0.0, "a different archetype"
    else:
        s, why = 0.0, "label not recognized"
    return {
        "arc_subscore": s,
        "label": got, "raw": raw, "expected": exp, "recognized": got is not None,
        "trap_fired": bool(conf and got == conf),
        "family_match": bool(got and FAMILY.get(got) == FAMILY.get(exp)),
        "why": why,
        "jury_trap_and_escape": "UNCALIBRATED — not scored",
    }


# ---------- response builders ----------

def perfect_resp(it):
    return {"archetype": it["archetype"], "trap": "", "escape": ""}


def synonym_resp(it):
    a = ALIASES[it["archetype"]]
    return {"archetype": "It is the " + it["archetype"].replace("-", " ").title() + " archetype", "trap": "", "escape": ""} if not a else \
           {"archetype": a[0], "trap": "", "escape": ""}


def trap_resp(it):
    return {"archetype": it["confusable"], "trap": "", "escape": ""} if it.get("confusable") else None


def family_other(it):
    exp, conf = it["archetype"], it.get("confusable")
    for c in CANON:
        if c != exp and c != conf and FAMILY[c] == FAMILY[exp]: return c
    return None


def degraded_resp(it):
    other = family_other(it)
    if other is None:
        other = next(c for c in CANON if FAMILY[c] != FAMILY[it["archetype"]])
    return {"archetype": other, "trap": "", "escape": ""}


def unrelated_resp(it):
    return {"archetype": next(c for c in CANON if FAMILY[c] != FAMILY[it["archetype"]] and c != it.get("confusable")), "trap": "", "escape": ""}


# ---------- calibrate ----------

def _seed_blocks(seed_path):
    t = open(seed_path, encoding="utf-8").read()
    out = {}
    for b in re.split(r"\n(?=## ARC-)", t):
        m = re.match(r"## (ARC-[A-Z0-9-]+) \(([^)]*)\)", b)
        if not m: continue
        lvl = re.search(r"\bL[1-4]\b", m.group(2))
        ref = re.search(r"\*\*Reference:\*\*\s*`([a-z-]+)`", b)
        con = re.search(r"\*\*Confusable[^:]*:\*\*\s*`([a-z-]+)`", b)
        out[m.group(1)] = {"level": lvl.group(0) if lvl else None, "ref": ref.group(1) if ref else None, "conf": con.group(1) if con else None}
    return out


def cmd_calibrate(path):
    oracle = json.load(open(path))
    seed_path = os.path.join(os.path.dirname(os.path.abspath(path)), "seed_ARC_archetypes.md")
    seed = _seed_blocks(seed_path) if os.path.exists(seed_path) else {}
    checks = []
    cover = {}
    for iid, it in oracle["items"].items():
        sb = seed.get(iid)
        checks.append((f"{iid}: exists in the seed file at level {it.get('level')}", bool(sb) and sb["level"] == it.get("level")))
        checks.append((f"{iid}: reference label '{it['archetype']}' is canonical", it["archetype"] in FAMILY))
        checks.append((f"{iid}: confusable '{it.get('confusable')}' is canonical and differs from the reference",
                       it.get("confusable") in FAMILY and it.get("confusable") != it["archetype"]))
        checks.append((f"{iid}: the seed's Reference line says '{it['archetype']}'", bool(sb) and sb["ref"] == it["archetype"]))
        checks.append((f"{iid}: the seed's Confusable line says '{it.get('confusable')}'", bool(sb) and sb["conf"] == it.get("confusable")))
        cover.setdefault(it["archetype"], set()).add(it.get("level"))
        rp = score(it, perfect_resp(it))
        checks.append((f"{iid}: reference round-trips to 1.0 (got {rp['arc_subscore']})", rp["arc_subscore"] == 1.0 and not rp["trap_fired"]))
        sp = score(it, synonym_resp(it))
        checks.append((f"{iid}: an alias reply scores 1.0 (got {sp['arc_subscore']}, '{synonym_resp(it)['archetype']}')", sp["arc_subscore"] == 1.0))
        sent = score(it, {"archetype": "This reads as the " + it["archetype"].replace("-", " ") + " archetype, clearly."})
        checks.append((f"{iid}: the label inside a sentence scores 1.0 (got {sent['arc_subscore']})", sent["arc_subscore"] == 1.0))
        tp = score(it, trap_resp(it))
        checks.append((f"{iid}: the confusable fires and caps at {TRAP_CAP} (got {tp['arc_subscore']}, trap={tp['trap_fired']})",
                       tp["trap_fired"] and tp["arc_subscore"] == TRAP_CAP))
        fo = family_other(it)
        if fo:
            fp = score(it, {"archetype": fo})
            checks.append((f"{iid}: a same-family other label ({fo}) scores {FAMILY_CREDIT} (got {fp['arc_subscore']})", fp["arc_subscore"] == FAMILY_CREDIT))
        up = score(it, unrelated_resp(it))
        checks.append((f"{iid}: an unrelated label scores 0 (got {up['arc_subscore']})", up["arc_subscore"] == 0.0))
        gp = score(it, {"archetype": "the loop of doom"})
        checks.append((f"{iid}: an unrecognized label scores 0 and is flagged (recognized={gp['recognized']})", gp["arc_subscore"] == 0.0 and not gp["recognized"]))
    for c in CANON:
        for lvl in ("L1", "L2", "L3"):
            checks.append((f"coverage: {c} has an item at {lvl}", lvl in cover.get(c, set())))
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
    print(f"# ARC score — {item_id}")
    print(json.dumps(res, indent=2))
    return 0


def main():
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "calibrate": return cmd_calibrate(a[1])
    if len(a) == 4 and a[0] == "score": return cmd_score(a[1], a[2], a[3])
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main())
