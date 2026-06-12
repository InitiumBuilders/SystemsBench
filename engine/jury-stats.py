#!/usr/bin/env python3
"""jury-stats.py — jury aggregation + agreement math for SystemsBench.

EVIDENCE ONLY: implements the recorded aggregation conventions (median per sub-criterion
-> mean per dimension; ordinal Krippendorff alpha; the section-3.1 bootstrap accept-rule)
and SIMULATES the three candidate hardening forks from SystemsBenchFuture.MD section 6.1.
It changes no governance: fork simulations are dry-runs producing evidence for the
August + Ember ratification, exactly per the review process specified there.

Subcommands:
  collect <outdir>                       extract R*.out -> R*.json; rc=0 iff all parse clean
  calibrate <baseline.json>              reproduce the recorded N=3 gold numbers (calculator self-test)
  report <baseline.json> <ceiling-dir> <mid-dir> <trap-dir>   full N=5 vs N=3 markdown report
"""
import json, math, sys, glob, os, statistics

SUBS = ["A1","A2","A3","A4","B1","B2","C1","C2","C3","C4","C5","D1","D2","D3","E1","E2","E3"]
DIMS = {"A": ["A1","A2","A3","A4"], "B": ["B1","B2"], "C": ["C1","C2","C3","C4","C5"],
        "D": ["D1","D2","D3"], "E": ["E1","E2","E3"]}
WEIGHTS = {"A": 0.22, "B": 0.18, "C": 0.30, "D": 0.18, "E": 0.12}
VALID = {0.0, 0.5, 1.0}

# ---------- extraction ----------

def extract_json(text):
    """First balanced {...} block that parses; tolerates prose/fences around it."""
    for i, ch in enumerate(text):
        if ch != "{":
            continue
        depth = 0
        for j in range(i, len(text)):
            if text[j] == "{": depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[i:j+1])
                    except json.JSONDecodeError:
                        break
    return None

def validate_rater(obj):
    errs = []
    scores = obj.get("scores", {})
    missing = [s for s in SUBS if s not in scores]
    if missing: errs.append(f"missing subs: {missing}")
    bad = {k: v for k, v in scores.items() if k in SUBS and float(v) not in VALID}
    if bad: errs.append(f"off-scale values: {bad}")
    return errs

def cmd_collect(outdir):
    raws = sorted(glob.glob(os.path.join(outdir, "R*.out")))
    if not raws:
        print(f"collect: no R*.out files in {outdir}", file=sys.stderr); return 2
    failures = 0
    for raw in raws:
        rid = os.path.basename(raw)[:-4]
        obj = extract_json(open(raw, encoding="utf-8", errors="replace").read())
        errs = validate_rater(obj) if obj else ["no parseable JSON object"]
        if errs:
            print(f"  {rid}: FAIL — {'; '.join(errs)}"); failures += 1; continue
        out = os.path.join(outdir, f"{rid}.json")
        json.dump(obj, open(out, "w"), indent=1)
        print(f"  {rid}: OK -> {out}")
    print(f"collect: {len(raws)-failures}/{len(raws)} raters clean")
    return 1 if failures else 0

# ---------- agreement math ----------

def ordinal_delta2(cats, counts):
    """delta^2[(c,k)] per Krippendorff ordinal metric, from marginal counts."""
    d2 = {}
    for a in range(len(cats)):
        for b in range(a + 1, len(cats)):
            s = sum(counts[g] for g in range(a, b + 1)) - (counts[a] + counts[b]) / 2.0
            d2[(cats[a], cats[b])] = s * s
    return d2

def kripp_alpha(units):
    """units: list of lists of values (one list per sub-criterion). Ordinal alpha.
    Returns (alpha|None, Do, De, pct_unanimous)."""
    vals = [v for u in units for v in u]
    n = len(vals)
    cats = sorted(set(vals))
    counts = {c: vals.count(c) for c in cats}
    clist = [counts[c] for c in cats]
    d2 = ordinal_delta2(cats, clist)
    def dd(a, b):
        if a == b: return 0.0
        lo, hi = min(a, b), max(a, b)
        return d2[(lo, hi)]
    Do = 0.0
    for u in units:
        m = len(u)
        if m < 2: continue
        s = sum(dd(u[i], u[j]) for i in range(m) for j in range(m) if i != j)
        Do += s / (m - 1)
    Do /= n
    De = 0.0
    for a in cats:
        for b in cats:
            if a == b: continue
            De += counts[a] * counts[b] * dd(a, b)
    De /= n * (n - 1)
    unanimous = sum(1 for u in units if len(set(u)) == 1)
    pct = unanimous / len(units) if units else 0.0
    if De == 0:
        return None, Do, De, pct  # perfect agreement: alpha undefined, never a fail
    return 1 - Do / De, Do, De, pct

# ---------- accept rules (base + the three candidate forks, simulated) ----------

def thresh(n): return math.ceil(2 * n / 3)

def accept_base(vals):
    """Recorded section-3.1: (a) unanimity; (b) >=ceil(2N/3) within one contiguous window
    of <=1 ordinal band (span <= 0.5)."""
    n = len(vals)
    if len(set(vals)) == 1: return "ACCEPT-UNANIMITY"
    windows = [{0.0}, {0.5}, {1.0}, {0.0, 0.5}, {0.5, 1.0}]
    best = max(sum(1 for v in vals if v in w) for w in windows)
    return "ACCEPT-WINDOW" if best >= thresh(n) else "AMBIGUOUS-ANCHOR"

def accept_fork1(vals):
    """Fork 1: unanimity OR >=ceil(2N/3) IDENTICAL labels (not merely adjacent)."""
    n = len(vals)
    if len(set(vals)) == 1: return "ACCEPT-UNANIMITY"
    mode_count = max(vals.count(v) for v in set(vals))
    return "ACCEPT-IDENTICAL" if mode_count >= thresh(n) else "AMBIGUOUS-ANCHOR"

def accept_fork3(vals):
    """Fork 3: base rule + max-spread guard (reject any full 0<->1.0 span)."""
    if min(vals) == 0.0 and max(vals) == 1.0: return "AMBIGUOUS-ANCHOR(spread)"
    return accept_base(vals)

FORKS = [("base §3.1", accept_base), ("fork1 identical", accept_fork1),
         ("fork3 max-spread", accept_fork3)]

# ---------- aggregation ----------

def median(vals):
    return statistics.median(vals)

def labels_from(data):
    """data: {sub: [values...]} -> gold label per recorded convention."""
    sub_med = {s: median(data[s]) for s in SUBS}
    dim = {d: sum(sub_med[s] for s in subs) / len(subs) for d, subs in DIMS.items()}
    comp = sum(WEIGHTS[d] * dim[d] for d in DIMS)
    return sub_med, dim, comp

def dim_units(data, d):
    return [data[s] for s in DIMS[d]]

# ---------- data loading ----------

def load_baseline(path):
    """baseline json: {tier: {sub: [v1,v2,v3]}}"""
    return {t: {s: [float(x) for x in subs[s]] for s in SUBS}
            for t, subs in json.load(open(path)).items() if not t.startswith("_")}

def load_rater_dir(d):
    """dir of R*.json -> {sub: [values in rater order]}"""
    out = {s: [] for s in SUBS}
    files = sorted(glob.glob(os.path.join(d, "R*.json")),
                   key=lambda p: int(os.path.basename(p)[1:-5]))
    if not files:
        raise SystemExit(f"no R*.json in {d} — run collect first")
    for f in files:
        sc = json.load(open(f))["scores"]
        for s in SUBS: out[s].append(float(sc[s]))
    return out, len(files)

# ---------- calibrate (calculator self-test vs recorded gold numbers) ----------

def approx(a, b, tol=0.005): return abs(a - b) <= tol

def cmd_calibrate(path):
    base = load_baseline(path)
    checks = []
    # composites (recorded: ceiling full-vector 0.925 / coverage A-D 0.9375; mid 0.4375; trap 0.0275)
    _, dim_c, comp_c = labels_from(base["ceiling"])
    cov = sum(WEIGHTS[d] * dim_c[d] for d in "ABCD") / sum(WEIGHTS[d] for d in "ABCD")
    _, dim_m, comp_m = labels_from(base["mid"])
    _, dim_t, comp_t = labels_from(base["trap"])
    checks += [("ceiling full-vector composite 0.925", approx(comp_c, 0.925)),
               ("ceiling coverage A-D 0.9375", approx(cov, 0.9375)),
               ("mid composite 0.4375", approx(comp_m, 0.4375)),
               ("trap composite 0.0275", approx(comp_t, 0.0275)),
               ("ceiling A 0.750", approx(dim_c["A"], 0.75)),
               ("mid A 0.375", approx(dim_m["A"], 0.375)),
               ("trap A 0.125", approx(dim_t["A"], 0.125))]
    # recorded ceiling alphas: A=0.686 D=0.000 E=0.111; B,C undefined (perfect)
    for d, want in [("A", 0.686), ("D", 0.000), ("E", 0.111)]:
        a, Do, De, _ = kripp_alpha(dim_units(base["ceiling"], d))
        checks.append((f"ceiling alpha {d} {want}", a is not None and approx(a, want)))
    for d in ["B", "C"]:
        a, _, De, _ = kripp_alpha(dim_units(base["ceiling"], d))
        checks.append((f"ceiling alpha {d} undefined(perfect)", a is None and De == 0))
    # recorded accept: 51/51 ACCEPT at N=3 under base rule
    total = ok = 0
    for t in base:
        for s in SUBS:
            total += 1
            if accept_base(base[t][s]).startswith("ACCEPT"): ok += 1
    checks.append((f"base rule N=3: 51/51 ACCEPT (got {ok}/{total})", ok == total == 51))
    # hand-computed N=5 sanity: 0,0,0.5,1,1 must FAIL base; 0,0.5,0.5,0.5,1 must PASS base but FAIL fork3
    checks.append(("N=5 split 0,0,.5,1,1 fails base", accept_base([0,0,.5,1,1]) == "AMBIGUOUS-ANCHOR"))
    checks.append(("N=5 0,.5,.5,.5,1 passes base", accept_base([0,.5,.5,.5,1]) == "ACCEPT-WINDOW"))
    checks.append(("N=5 0,.5,.5,.5,1 fails fork3", accept_fork3([0,.5,.5,.5,1]).startswith("AMBIGUOUS")))
    checks.append(("N=5 .5,.5,.5,1,1 fails fork1", accept_fork1([.5,.5,.5,1,1]) == "AMBIGUOUS-ANCHOR"))
    checks.append(("N=5 .5,.5,.5,.5,1 passes fork1", accept_fork1([.5,.5,.5,.5,1]) == "ACCEPT-IDENTICAL"))
    bad = [name for name, okk in checks if not okk]
    for name, okk in checks:
        print(("PASS  " if okk else "FAIL  ") + name)
    print(f"calibrate: {len(checks)-len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0

# ---------- report ----------

def fmt(x): return f"{x:.3f}".rstrip("0").rstrip(".") if isinstance(x, float) else str(x)

def cmd_report(bpath, cdir, mdir, tdir):
    base = load_baseline(bpath)
    new = {}
    nN = {}
    for tier, d in [("ceiling", cdir), ("mid", mdir), ("trap", tdir)]:
        new[tier], nN[tier] = load_rater_dir(d)
    N5 = nN["ceiling"]
    print(f"# Jury re-score report — LEV-ORG-001 quality-spread · N={N5} synthetic raters "
          f"vs recorded N=3 baseline")
    print()
    match_total = match_ok = 0
    amb = {f: {3: 0, 5: 0} for f, _ in FORKS}
    for tier in ["ceiling", "mid", "trap"]:
        b, n = base[tier], new[tier]
        smb, dmb, cb = labels_from(b)
        smn, dmn, cn = labels_from(n)
        print(f"## {tier.upper()}")
        print(f"| Sub | N=3 labels | N=3 med | N={N5} labels | N={N5} med | med match "
              f"| base@3 | base@{N5} | fork1@{N5} | fork3@{N5} |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for s in SUBS:
            m = smb[s] == smn[s]
            match_total += 1; match_ok += m
            r = {}
            for fname, fn in FORKS:
                a3, a5 = fn(b[s]), fn(n[s])
                r[fname] = (a3, a5)
                if not a3.startswith("ACCEPT"): amb[fname][3] += 1
                if not a5.startswith("ACCEPT"): amb[fname][5] += 1
            print(f"| {s} | {','.join(fmt(v) for v in b[s])} | {fmt(smb[s])} "
                  f"| {','.join(fmt(v) for v in n[s])} | {fmt(smn[s])} | {'=' if m else 'DIFF'} "
                  f"| {r['base §3.1'][0].split('-')[0]} | {r['base §3.1'][1]} "
                  f"| {r['fork1 identical'][1]} | {r['fork3 max-spread'][1]} |")
        print()
        print(f"Dimensions (N=3 -> N={N5}): " + " · ".join(
            f"{d} {fmt(dmb[d])}->{fmt(dmn[d])}" for d in DIMS))
        print(f"Composite (N=3 -> N={N5}): **{fmt(cb)} -> {fmt(cn)}**  (delta {cn-cb:+.3f})")
        alphas = []
        for d in DIMS:
            a, Do, De, pct = kripp_alpha(dim_units(n, d))
            alphas.append(f"{d}: " + (f"alpha={a:.3f}" if a is not None else "undef(perfect)")
                          + f" ({pct:.0%} unanimous)")
        print(f"Krippendorff alpha @N={N5} (ordinal): " + " · ".join(alphas))
        print()
    print("## Accept-rule falsifiability summary (51 sub-criteria across the spread)")
    print(f"| Rule | AMBIGUOUS @N=3 | AMBIGUOUS @N={N5} |")
    print("|---|---|---|")
    for fname, _ in FORKS:
        print(f"| {fname} | {amb[fname][3]}/51 | {amb[fname][5]}/51 |")
    print()
    print(f"Median-label agreement N={N5} vs N=3 gold: {match_ok}/{match_total} "
          f"({match_ok/match_total:.0%}) sub-criteria identical.")
    return 0

def main():
    if len(sys.argv) < 2: print(__doc__); return 1
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "collect" and len(args) == 1: return cmd_collect(args[0])
    if cmd == "calibrate" and len(args) == 1: return cmd_calibrate(args[0])
    if cmd == "report" and len(args) == 4: return cmd_report(*args)
    print(__doc__); return 1

if __name__ == "__main__":
    sys.exit(main())
