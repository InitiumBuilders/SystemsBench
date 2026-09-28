#!/usr/bin/env python3
"""bench-run.py — run any model through every executable item: template → adapter → parse → score → files.

The harness (engine/harness.py) does one item at a time. This runner does the bank: for every format the
harness knows (CLD, DYN, SF, ARC) and every item in that format's oracle, it renders the prompt, asks the
adapter, parses the reply fail-closed, scores it with the format's own scorer, and writes the results as
files under results/. It never re-implements scoring: template, parse and score are imported from the
harness and the scorers. Level and domain come from the register (items/INDEX.md).

Adapters
  reference   built in, zero spend: replays each scorer's own reference builder (perfect_resp) through the
              REAL parse path, wrapped the way a model would wrap it. The instrument's ceiling: every item
              must score 1.0 with zero parse errors, or the instrument is broken.
  trap        built in, zero spend: replays each item's named trap (trap_resp). The instrument's floor for
              the naive answer: capped scores wherever a trap builder exists.
  sycophant   built in, zero spend, TRAP only: answers the reference alone and the trap when the probe's note suggests it,
              in silence. Every TRAP item must land `unfaithful`. (Other lanes: the reference.)
  candid      built in, zero spend, TRAP only: flips like the sycophant and says the note is why. Lands `faithful`.
  cmd         any model behind a shell command: the prompt goes to stdin, the reply is read from stdout.
              Requires --live (it may spend money), and is capped at --max-items unless --all is given.
              Example: --adapter cmd --cmd "claude -p" --live --all

The faithfulness probe (Structure §4.5): TRAP items run as a PAIR, the item as asked and the item with one fixed hint toward its
trap; the pair is scored for flipped / acknowledged and a label in {faithful, mixed, unfaithful}, reported in its own table and never
averaged into any score.

Accounting is fail-closed: a reply that does not parse is PARSE_ERROR, an adapter that fails is
ADAPTER_ERROR; both are counted beside the scores and never turned into a zero. Jury dimensions are not
run here and remain `UNCALIBRATED — not scored`. Nothing this runner writes is a benchmark score until the
item statistics clear Structure §3.3 and the jury dimensions are calibrated; a dry run measures the
instrument, not any AI.

Usage
  bench-run.py selftest                                    reference must be 1.0 and trap must be capped on two items per lane
  bench-run.py run --adapter reference|trap [--lanes SF,CLD] [--items REGEX] [--limit N] [--out DIR] [--date YYYY-MM-DD]
  bench-run.py run --adapter cmd --cmd "<command>" --live [--all | --max-items N] [--name NAME] [--timeout SEC] ...

Outputs (in --out, default results/dry-runs/<date>_<adapter> or results/live/<date>_<name>)
  run.json      adapter, lanes, counts, the instrument's self-test lines captured at run start, spec version
  scores.csv    one row per item: id, format, level, domain, status, subscore, trap_fired, and for TRAP the probe columns
                (hinted_subscore, flipped, acknowledged, faithfulness), seconds
  replies/      the raw reply per item (the audit trail; prompts are reproducible from the harness)
  summary.md    by lane, by level, by domain; errors counted beside scores

No live-model spend unless --adapter cmd --live. Added in SenseRun #15.
"""
import argparse, csv, datetime, hashlib, io, json, os, re, statistics, subprocess, sys, time, importlib.util

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.dirname(ENGINE_DIR)


def _load_harness():
    spec = importlib.util.spec_from_file_location("_harness", os.path.join(ENGINE_DIR, "harness.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


H = _load_harness()


def register():
    """items/INDEX.md rows -> {ID: {format, level, domain, status}}"""
    out, hdr = {}, None
    for line in io.open(os.path.join(BENCH, "items", "INDEX.md"), encoding="utf-8"):
        t = line.strip()
        if not t.startswith("|"): continue
        cells = [c.strip() for c in t.strip("|").split("|")]
        if cells and cells[0] == "ID": hdr = cells; continue
        if hdr is None or set("".join(cells)) <= set("-: "): continue
        if re.match(r"^[A-Z]+-[A-Z0-9-]+$", cells[0]) and len(cells) >= 4:
            row = dict(zip(hdr, cells))
            out[cells[0]] = {"format": row.get("Format", ""), "level": row.get("Diff", ""), "domain": row.get("Domain", ""), "status": row.get("Status", "")}
    return out


def wrap_like_a_model(resp):
    return "Here is my answer.\n\n```json\n" + json.dumps(resp, indent=1) + "\n```\n"


class Adapter:
    def __init__(self, kind, cmd=None, timeout=300):
        self.kind, self.cmd, self.timeout = kind, cmd, timeout

    def reply(self, prompt, fmt, item_id, oracle_item, scorer, variant=None):
        if self.kind == "reference":
            return wrap_like_a_model(scorer.perfect_resp(oracle_item)), True
        if self.kind in ("sycophant", "candid"):
            if fmt == "TRAP" and variant == "probe":
                pair = scorer.sycophant_pair(oracle_item) if self.kind == "sycophant" else scorer.candid_pair(oracle_item)
                return wrap_like_a_model(pair[1]), True
            return wrap_like_a_model(scorer.perfect_resp(oracle_item)), True
        if self.kind == "trap":
            tr = scorer.trap_resp(oracle_item) if hasattr(scorer, "trap_resp") else None
            if tr is None:
                return wrap_like_a_model(scorer.perfect_resp(oracle_item)), False   # no trap builder: replay the reference, flag it
            return wrap_like_a_model(tr), True
        if self.kind == "cmd":
            p = subprocess.run(self.cmd, shell=True, input=prompt, capture_output=True, text=True, timeout=self.timeout)
            if p.returncode != 0:
                raise RuntimeError(f"adapter rc={p.returncode}: {p.stderr.strip()[-300:]}")
            return p.stdout, True
        raise ValueError(self.kind)


def gates():
    """the instrument's self-test lines, captured so every results folder says what state the scorers were in"""
    lines = {}
    for fmt in H.FORMATS:
        rc, out = _sh(f"python3 {os.path.join(ENGINE_DIR, H.SCORER_FILE[fmt])} calibrate {H.ORACLE_PATH[fmt]}")
        lines[f"{fmt} calibrate"] = (out.strip().splitlines() or [""])[-1] + ("" if rc == 0 else f"  (rc={rc})")
    rc, out = _sh(f"python3 {os.path.join(ENGINE_DIR, 'harness.py')} selftest")
    lines["harness selftest"] = (out.strip().splitlines() or [""])[-1] + ("" if rc == 0 else f"  (rc={rc})")
    return lines


def _sh(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def select_items(lanes, item_re, limit):
    reg = register()
    picked = []
    prompts = json.load(open(H.PROMPTS_PATH))
    for fmt in lanes:
        oracle = H.load_oracle(fmt)["items"]
        wired = set(prompts.get(fmt, {}).get("items", {}))
        for iid, it in oracle.items():
            if iid not in wired: continue                       # not executable: no template
            if item_re and not re.search(item_re, iid): continue
            r = reg.get(iid, {})
            picked.append((fmt, iid, it, r.get("level", ""), r.get("domain", it.get("domain", ""))))
            if limit and len([p for p in picked if p[0] == fmt]) >= limit: break
    return picked


def run(args):
    lanes = [l.strip().upper() for l in args.lanes.split(",")] if args.lanes else list(H.FORMATS)
    for l in lanes:
        if l not in H.FORMATS: sys.exit(f"unknown lane {l} (have: {', '.join(H.FORMATS)})")
    date = args.date or datetime.date.today().isoformat()
    if args.adapter == "cmd":
        if not args.cmd: sys.exit("--adapter cmd needs --cmd")
        if not args.live: sys.exit("a model command may spend money: add --live to confirm (and --all to lift the --max-items cap)")
    items = select_items(lanes, args.items, args.limit)
    if args.adapter == "cmd" and not args.all and len(items) > args.max_items:
        print(f"capped at --max-items {args.max_items} of {len(items)} (pass --all to run every item)")
        items = items[:args.max_items]
    name = args.name or args.adapter
    out = args.out or os.path.join(BENCH, "results", "live" if args.adapter == "cmd" else "dry-runs", f"{date}_{name}")
    os.makedirs(os.path.join(out, "replies"), exist_ok=True)
    state = json.load(open(os.path.join(BENCH, ".state", "engine_state.json")))
    print(f"{'LIVE' if args.adapter == 'cmd' else 'DRY'} run · adapter={args.adapter} · lanes={','.join(lanes)} · items={len(items)} · out={os.path.relpath(out, BENCH)}")
    g = gates()
    for k, v in g.items(): print(f"  gate  {k}: {v}")
    adapter = Adapter(args.adapter, args.cmd, args.timeout)
    scorers = {fmt: H.load_scorer(fmt) for fmt in lanes}
    rows = []
    for n, (fmt, iid, it, level, domain) in enumerate(items, 1):
        prompt = H.render_template(fmt, iid)
        t0 = time.perf_counter(); status, sub, tf, note = "scored", "", "", ""
        probe = {"hinted_subscore": "", "flipped": "", "acknowledged": "", "faithfulness": ""}; parsed_n = None
        try:
            raw, real = adapter.reply(prompt, fmt, iid, it, scorers[fmt])
            io.open(os.path.join(out, "replies", iid + ".txt"), "w", encoding="utf-8").write(raw)
            if args.adapter == "trap" and not real: note = "no trap builder; reference replayed"
            try:
                parsed = H.parse_response(fmt, raw); parsed_n = parsed
                res = scorers[fmt].score(it, parsed)
                sub = res[H.SUBSCORE_KEY[fmt]]
                tf = res.get("trap_fired")
                if tf is None: tf = next((v for k, v in res.items() if "trap" in k and isinstance(v, bool)), "")
            except H.ParseError as e:
                status, note = "PARSE_ERROR", str(e)[:200]
            # the faithfulness probe: TRAP items run a second time with the hint; the pair is scored, never averaged in
            if fmt == "TRAP" and parsed_n is not None:
                try:
                    praw, _ = adapter.reply(H.render_template(fmt, iid, "probe"), fmt, iid, it, scorers[fmt], variant="probe")
                    io.open(os.path.join(out, "replies", iid + ".probe.txt"), "w", encoding="utf-8").write(praw)
                    try:
                        pr = scorers[fmt].score_pair(it, parsed_n, H.parse_response(fmt, praw))
                        probe = {"hinted_subscore": pr["hinted_subscore"], "flipped": pr["flipped"], "acknowledged": pr["acknowledged"], "faithfulness": pr["faithfulness"]}
                    except H.ParseError as e:
                        probe["faithfulness"] = "PROBE_PARSE_ERROR"; note = (note + "; " if note else "") + "probe: " + str(e)[:120]
                except Exception as e:
                    probe["faithfulness"] = "PROBE_ADAPTER_ERROR"; note = (note + "; " if note else "") + "probe: " + str(e)[:120]
        except Exception as e:
            status, note = "ADAPTER_ERROR", str(e)[:200]
        rows.append({"id": iid, "format": fmt, "level": level, "domain": domain, "status": status, "subscore": sub,
                     "trap_fired": tf, **probe, "seconds": round(time.perf_counter() - t0, 3), "note": note})
        if args.adapter == "cmd" or n % 25 == 0 or n == len(items):
            print(f"  {n:4d}/{len(items)}  {iid:22s} {status:13s} {sub if sub != '' else '-'}")
    with io.open(os.path.join(out, "scores.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["id"]); w.writeheader(); w.writerows(rows)
    meta = {"adapter": args.adapter, "kind": "LIVE" if args.adapter == "cmd" else "DRY", "name": name, "date": date, "lanes": lanes,
            "items": len(items), "scored": sum(r["status"] == "scored" for r in rows),
            "parse_errors": sum(r["status"] == "PARSE_ERROR" for r in rows), "adapter_errors": sum(r["status"] == "ADAPTER_ERROR" for r in rows),
            "command": (args.cmd.split()[0] + " …  sha256:" + hashlib.sha256(args.cmd.encode()).hexdigest()[:16]) if args.cmd else None,
            "spec_version": state.get("spec_version"), "last_senserun": state.get("last_senserun"), "gates": g,
            "probe": {k: sum(1 for r in rows if r["faithfulness"] == k) for k in ["faithful", "mixed", "unfaithful", "PROBE_PARSE_ERROR", "PROBE_ADAPTER_ERROR"]} if any(r["faithfulness"] for r in rows) else None,
            "jury": "UNCALIBRATED — not scored (no jury dimension is run by this runner)"}
    json.dump(meta, io.open(os.path.join(out, "run.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    io.open(os.path.join(out, "summary.md"), "w", encoding="utf-8").write(summary(meta, rows))
    print(open(os.path.join(out, "summary.md"), encoding="utf-8").read())
    return 0 if meta["adapter_errors"] == 0 else 2


def _stats(rs):
    s = [float(r["subscore"]) for r in rs if r["status"] == "scored"]
    pe = sum(r["status"] == "PARSE_ERROR" for r in rs); ae = sum(r["status"] == "ADAPTER_ERROR" for r in rs)
    tf = sum(1 for r in rs if r["trap_fired"] is True)
    if not s: return f"| {len(rs)} | 0 | {pe} | {ae} | – | – | – | {tf} |"
    return f"| {len(rs)} | {len(s)} | {pe} | {ae} | {statistics.mean(s):.3f} | {statistics.median(s):.3f} | {min(s):.2f} | {tf} |"


def summary(meta, rows):
    hdr = "| items | scored | PARSE_ERROR | ADAPTER_ERROR | mean | median | min | trap fired |"
    sep = "|---|---|---|---|---|---|---|---|"
    L = []
    if meta["kind"] == "DRY":
        L.append(f"# DRY RUN — adapter `{meta['adapter']}` — {meta['date']}\n\n**This measures the instrument, not any AI.** The `{meta['adapter']}` adapter replays the scorers' own builders through the real template → parse → score path. "
                 + ("Every item must score 1.0 with zero parse errors; anything less is a defect in the harness or a scorer.\n" if meta["adapter"] == "reference"
                    else "Each item's named naive answer is replayed; the scores show the caps the traps enforce. Items without a trap builder replay the reference and are noted.\n"))
    else:
        L.append(f"# LIVE RUN — `{meta['name']}` — {meta['date']}\n\nModel command: `{meta['command']}`. **Not a benchmark score:** no item statistic has cleared Structure §3.3 and every jury dimension is `UNCALIBRATED — not scored`. These are deterministic sub-scores on the executable lanes only.\n")
    L.append(f"Instrument at run time: " + " · ".join(f"{k} {v}" for k, v in meta["gates"].items()) + f" · spec {meta['spec_version']} · after SenseRun #{meta['last_senserun']}.\n")
    L.append("## By lane\n\n| lane " + hdr + "\n|---" + sep)
    for fmt in meta["lanes"]:
        L.append(f"| `{fmt}` " + _stats([r for r in rows if r["format"] == fmt]))
    L.append("| **all** " + _stats(rows) + "\n")
    L.append("## By level\n\n| level " + hdr + "\n|---" + sep)
    for lv in sorted({r["level"] for r in rows}):
        L.append(f"| {lv or '?'} " + _stats([r for r in rows if r["level"] == lv]))
    L.append("\n## By domain\n\n| domain " + hdr + "\n|---" + sep)
    for d in sorted({r["domain"] for r in rows}):
        L.append(f"| {d or '?'} " + _stats([r for r in rows if r["domain"] == d]))
    pr = [r for r in rows if r["faithfulness"]]
    if pr:
        L.append("\n## Faithfulness probe (Structure §4.5) — reported separately, never averaged in\n")
        L.append("Each TRAP item was asked twice: as written, and with one fixed note from a colleague pointing at the trap. `flipped` = right alone, different with company; `unfaithful` = flipped toward the note and never mentioned it.\n")
        L.append("| level | items | faithful | mixed | unfaithful | probe errors | flipped toward the note |\n|---|---|---|---|---|---|---|")
        def _p(rs): return "| %d | %d | %d | %d | %d | %d |" % (len(rs), sum(r["faithfulness"] == "faithful" for r in rs), sum(r["faithfulness"] == "mixed" for r in rs), sum(r["faithfulness"] == "unfaithful" for r in rs), sum(str(r["faithfulness"]).endswith("ERROR") for r in rs), sum(r["flipped"] is True and r["faithfulness"] in ("unfaithful", "faithful") and r["hinted_subscore"] != r["subscore"] for r in rs))
        for lv in sorted({r["level"] for r in pr}): L.append(f"| {lv or '?'} " + _p([r for r in pr if r["level"] == lv]))
        L.append("| **all** " + _p(pr))
    errs = [r for r in rows if r["status"] != "scored"]
    if errs:
        L.append("\n## Errors (counted above, never zeroed)\n")
        for r in errs[:50]: L.append(f"- `{r['id']}` {r['status']}: {r['note']}")
    notes = [r for r in rows if r["note"] and r["status"] == "scored"]
    if notes:
        L.append(f"\n## Notes\n\n{len(notes)} item(s): " + "; ".join(f"`{r['id']}` {r['note']}" for r in notes[:30]))
    L.append("\nJury dimensions: `UNCALIBRATED — not scored`. Files: `scores.csv` (per item), `replies/` (raw replies), `run.json`.\n")
    return "\n".join(L)


def selftest(args):
    checks = []
    for fmt in H.FORMATS:
        sc = H.load_scorer(fmt); oracle = H.load_oracle(fmt)["items"]
        prompts = json.load(open(H.PROMPTS_PATH))[fmt]["items"]
        ids = [i for i in oracle if i in prompts][:2]
        for iid in ids:
            it = oracle[iid]
            raw, _ = Adapter("reference").reply("", fmt, iid, it, sc)
            s = sc.score(it, H.parse_response(fmt, raw))[H.SUBSCORE_KEY[fmt]]
            checks.append((f"{fmt}/{iid}: reference through template→parse→score = 1.0 (got {s})", abs(s - 1.0) < 1e-9))
            raw, real = Adapter("trap").reply("", fmt, iid, it, sc)
            s = sc.score(it, H.parse_response(fmt, raw))[H.SUBSCORE_KEY[fmt]]
            checks.append((f"{fmt}/{iid}: trap through the same path is capped < 1.0 (got {s}, builder={'yes' if real else 'no'})", (s < 1.0) if real else True))
            t = H.render_template(fmt, iid)
            checks.append((f"{fmt}/{iid}: template renders", len(t) > 200))
    try:
        Adapter("cmd", "exit 3").reply("hello", "SF", "x", {}, None); checks.append(("cmd adapter: a failing command raises", False))
    except Exception:
        checks.append(("cmd adapter: a failing command raises (becomes ADAPTER_ERROR)", True))
    raw, _ = Adapter("cmd", "cat").reply("echo this back", "SF", "x", {}, None)
    checks.append(("cmd adapter: stdin prompt is what the command receives", raw.strip() == "echo this back"))
    if "TRAP" in H.FORMATS:
        sc = H.load_scorer("TRAP"); oracle = H.load_oracle("TRAP")["items"]; prompts = json.load(open(H.PROMPTS_PATH))["TRAP"]["items"]
        for iid in [i for i in oracle if i in prompts][:2]:
            it = oracle[iid]
            for kind, want in [("reference", "faithful"), ("sycophant", "unfaithful"), ("candid", "faithful")]:
                a = Adapter(kind); rn, _ = a.reply("", "TRAP", iid, it, sc); rp, _ = a.reply("", "TRAP", iid, it, sc, variant="probe")
                r = sc.score_pair(it, H.parse_response("TRAP", rn), H.parse_response("TRAP", rp))
                checks.append((f"TRAP/{iid}: {kind} adapter through the pair -> {want} (got {r['faithfulness']})", r["faithfulness"] == want))
            t = H.render_template("TRAP", iid, "probe"); checks.append((f"TRAP/{iid}: probe template carries the hint", "fairly sure" in t))
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        if not ok: print("FAIL  " + n)
    print(f"selftest: {len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd_name")
    sp.add_parser("selftest")
    r = sp.add_parser("run")
    r.add_argument("--adapter", choices=["reference", "trap", "sycophant", "candid", "cmd"], required=True)
    r.add_argument("--cmd"); r.add_argument("--live", action="store_true"); r.add_argument("--all", action="store_true")
    r.add_argument("--max-items", type=int, default=20); r.add_argument("--timeout", type=int, default=300)
    r.add_argument("--lanes"); r.add_argument("--items"); r.add_argument("--limit", type=int, default=0)
    r.add_argument("--out"); r.add_argument("--name"); r.add_argument("--date")
    args = ap.parse_args()
    if args.cmd_name == "selftest": return selftest(args)
    if args.cmd_name == "run": return run(args)
    ap.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
