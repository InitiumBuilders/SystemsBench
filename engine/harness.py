#!/usr/bin/env python3
"""harness.py — per-format elicitation + response-parsing bridge for the CLD and DYN formats.

The connective tissue between a *live model reply* and the deterministic scorers
(`engine/cld-score.py`, `engine/dyn-score.py`). Those scorers grade a STRUCTURED `resp.json`; nothing
else in the repo turns a raw, prose-wrapped model reply into that file, and no prompt elicits the
canonical schema. This module is that bridge — implementing the already-governed §4.6 protocol
(step 2 "fix the harness", step 4 "auto-grade deterministic formats") and the §3.1 structured schemas.
It is **construct-neutral**: it changes how a response *reaches* the instrument, not what is measured.

REUSE, not reinvention (Research build-vs-reuse, SenseRun #10): the parser does NOT re-implement
semantic normalization — it hands raw values to the scorer, whose existing `norm`/synonym/`cbool`
logic does case/space/punct + synonym + boolean coercion. The parser's value-add is (a) extraction of
the structured object from messy text (```json fences, prose, nesting), (b) shape validation, and
(c) **fail-closed** behavior: an unparseable/malformed reply yields `PARSE_ERROR — not scored`, never a
fabricated or silent-empty resp that would score a deceptive 0 (ANTIPATTERNS #1/#2).

NOT built (held-open fork → August + Ember): semantic variable *aliasing* (a model's words → the
oracle's canonical names). A hand alias map would leak the oracle and inflate scores — a
measurement-validity question, not a worker-applicable infra step. The honest robustness lever is
strong *elicitation* (the `template` schema wrapper) + the scorers' existing synonym tolerance.

Subcommands:
  template <CLD|DYN> <ITEM_ID>     print the item scenario + the canonical-schema instruction wrapper.
  parse    <CLD|DYN> <FILE|->      extract+validate the structured resp from a raw reply; print resp.json
                                   to stdout (rc 0), or `PARSE_ERROR — not scored: …` to stderr (rc 3).
  selftest                         fail-closed round-trip: every oracle reference, serialized in several
                                   wire-wrappings, parses back and scores 1.0 through the EXISTING scorer;
                                   plus negative tests (no-JSON / missing-key → PARSE_ERROR). rc=0 iff all pass.

No live-model spend; pure local computation (§4.6 / host rail).
"""
import json, re, sys, os, importlib.util

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.dirname(ENGINE_DIR)
PROMPTS_PATH = os.environ.get("HARNESS_PROMPTS", os.path.join(BENCH, "items", "harness_prompts.json"))
ORACLE_PATH = {"CLD": os.path.join(BENCH, "items", "cld_oracle.json"),
               "DYN": os.path.join(BENCH, "items", "dyn_oracle.json")}
SCORER_FILE = {"CLD": "cld-score.py", "DYN": "dyn-score.py"}
SUBSCORE_KEY = {"CLD": "structural_subscore", "DYN": "trajectory_subscore"}

# schema contract the parser enforces (fail-closed shape check; the scorer does the semantics).
REQUIRED = {"CLD": ["variables", "edges", "loops", "dominant_loop"],
            "DYN": ["behavior_mode", "eventual_direction"]}
LISTKEYS = {"CLD": ["variables", "edges", "loops"], "DYN": []}
FORMATS = ("CLD", "DYN")


class ParseError(Exception):
    """Raised on any failure to recover a well-shaped response — the fail-closed signal."""


# ---------- scorer loader (filenames have hyphens → import by path; reuse, don't duplicate) ----------

def load_scorer(fmt):
    path = os.path.join(ENGINE_DIR, SCORER_FILE[fmt])
    spec = importlib.util.spec_from_file_location(f"_scorer_{fmt.lower()}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_oracle(fmt):
    return json.load(open(ORACLE_PATH[fmt]))


# ---------- extraction ----------

def _first_json_object(s):
    """Return the first top-level balanced {...} that json-parses, respecting strings/escapes/nesting.
    Tolerates leading/trailing prose. Returns the parsed object or None."""
    i, n = 0, len(s)
    while i < n:
        if s[i] != "{":
            i += 1
            continue
        depth, in_str, esc = 0, False, False
        for j in range(i, n):
            ch = s[j]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(s[i:j + 1])
                    except json.JSONDecodeError:
                        break  # not valid JSON — advance to the next '{'
        i += 1
    return None


def extract_json(raw):
    """Pull the structured object out of a raw model reply: fenced ```json blocks first, then a
    whole-string balanced-brace scan. Raises ParseError if nothing parseable is found."""
    candidates = [m.group(1) for m in re.finditer(r"```(?:json|JSON)?\s*(.*?)```", raw, re.DOTALL)]
    candidates.append(raw)  # fallback: scan the entire reply
    for c in candidates:
        obj = _first_json_object(c)
        if obj is not None:
            return obj
    raise ParseError("no parseable JSON object found in the response")


def validate(fmt, obj):
    """Shape-check (NOT semantics): object with the required keys present and list-typed where required.
    Returns the object unchanged on success; raises ParseError otherwise (fail-closed)."""
    if not isinstance(obj, dict):
        raise ParseError("parsed JSON is not an object")
    missing = [k for k in REQUIRED[fmt] if k not in obj or obj[k] in (None, "", [])]
    if missing:
        raise ParseError(f"missing required {fmt} key(s): {', '.join(missing)}")
    for k in LISTKEYS[fmt]:
        if not isinstance(obj[k], list):
            raise ParseError(f"{fmt} key '{k}' must be a list, got {type(obj[k]).__name__}")
    return obj


def parse_response(fmt, raw):
    """raw reply text -> validated resp dict (the scorer's input). Raises ParseError, fail-closed."""
    if fmt not in FORMATS:
        raise ParseError(f"unknown format {fmt!r} (have: {', '.join(FORMATS)})")
    return validate(fmt, extract_json(raw))


# ---------- templates ----------

def render_template(fmt, item_id):
    prompts = json.load(open(PROMPTS_PATH))
    if fmt not in prompts:
        raise KeyError(f"no prompts for format {fmt}")
    items = prompts[fmt]["items"]
    if item_id not in items:
        raise KeyError(f"unknown {fmt} item {item_id} (have: {', '.join(items)})")
    scenario = items[item_id]["prompt"]
    schema = prompts[fmt]["schema_instructions"]
    return f"{scenario}\n\n{schema}"


# ---------- subcommands ----------

def cmd_template(fmt, item_id):
    try:
        sys.stdout.write(render_template(fmt, item_id) + "\n")
        return 0
    except (KeyError, FileNotFoundError) as e:
        print(f"template: {e}", file=sys.stderr)
        return 2


def cmd_parse(fmt, src):
    raw = sys.stdin.read() if src == "-" else open(src).read()
    try:
        resp = parse_response(fmt, raw)
    except ParseError as e:
        print(f"PARSE_ERROR — not scored: {e}", file=sys.stderr)
        return 3
    print(json.dumps(resp, indent=2))
    return 0


# ---------- self-test (fail-closed round-trip) ----------

def _wire_wrappings(resp):
    """The messy shapes a live reply might arrive in — each must parse back to `resp`."""
    blob = json.dumps(resp, indent=2)
    compact = json.dumps(resp)
    return {
        "bare": compact,
        "fenced-json": f"```json\n{blob}\n```",
        "prose-sandwich": f"Here is my analysis of the system.\n\n```json\n{blob}\n```\n\nThat is my prediction.",
        "fenced-nolang": f"```\n{blob}\n```\nNote: see reasoning above.",
        "brace-in-prose": f"My answer: {compact} — done.",
    }


def _stringy_dyn(resp):
    """A DYN reply with yes/no string booleans + a mode/direction synonym — the scorer must still see 1.0
    (proves the parser passes raw values through to the scorer's normalization, not re-implementing it)."""
    SYN_MODE = {"overshoot-and-collapse": "boom and bust", "oscillation": "oscillating",
                "s-shaped": "logistic", "better-before-worse": "fixes that fail",
                "delayed-rise-to-plateau": "delayed rise"}
    SYN_DIR = {"collapse": "crash", "same": "unchanged", "higher": "rises", "lower": "falls"}
    r = dict(resp)
    r["behavior_mode"] = SYN_MODE.get(resp["behavior_mode"], resp["behavior_mode"])
    r["eventual_direction"] = SYN_DIR.get(resp["eventual_direction"], resp["eventual_direction"])
    for k in ("overshoot", "oscillation", "delay_dominant"):
        if k in r:
            r[k] = "yes" if r[k] else "no"
    return r


def cmd_selftest():
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))

    for fmt in FORMATS:
        scorer = load_scorer(fmt)
        oracle = load_oracle(fmt)
        skey = SUBSCORE_KEY[fmt]
        for iid, it in oracle["items"].items():
            canonical = scorer.perfect_resp(it)
            for wire, payload in _wire_wrappings(canonical).items():
                try:
                    parsed = parse_response(fmt, payload)
                    sc = scorer.score(it, parsed)[skey]
                    ok = abs(sc - 1.0) <= 1e-6
                except ParseError as e:
                    ok, sc = False, f"PARSE_ERROR({e})"
                check(f"{fmt}/{iid} [{wire}]: round-trips to 1.0 (got {sc})", ok)

            # DYN: synonym + stringy-boolean reply still scores 1.0 via the SCORER's normalization.
            if fmt == "DYN":
                payload = f"```json\n{json.dumps(_stringy_dyn(canonical))}\n```"
                try:
                    parsed = parse_response(fmt, payload)
                    sc = scorer.score(it, parsed)[skey]
                    ok = abs(sc - 1.0) <= 1e-6
                except ParseError as e:
                    ok, sc = False, f"PARSE_ERROR({e})"
                check(f"{fmt}/{iid} [synonym+stringy-bool]: scorer normalizes -> 1.0 (got {sc})", ok)

        # negative: no JSON at all -> fail closed.
        try:
            parse_response(fmt, "I think the system will just settle down smoothly. No diagram.")
            check(f"{fmt}: prose-only reply -> PARSE_ERROR", False)
        except ParseError:
            check(f"{fmt}: prose-only reply -> PARSE_ERROR", True)

        # negative: well-formed JSON missing a required key -> fail closed.
        sample = next(iter(oracle["items"].values()))
        bad = scorer.perfect_resp(sample)
        bad.pop(REQUIRED[fmt][0])
        try:
            parse_response(fmt, json.dumps(bad))
            check(f"{fmt}: missing required key '{REQUIRED[fmt][0]}' -> PARSE_ERROR", False)
        except ParseError:
            check(f"{fmt}: missing required key '{REQUIRED[fmt][0]}' -> PARSE_ERROR", True)

        # template renders (prompts file present + carries the schema wrapper).
        try:
            first_id = next(iter(oracle["items"]))
            t = render_template(fmt, first_id)
            check(f"{fmt}: template renders for {first_id} (scenario + schema)", "JSON" in t.upper() and len(t) > 200)
        except Exception as e:
            check(f"{fmt}: template renders ({e})", False)

    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(("PASS  " if ok else "FAIL  ") + n)
    print(f"selftest: {len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


def main():
    a = sys.argv[1:]
    if len(a) == 1 and a[0] == "selftest":
        return cmd_selftest()
    if len(a) == 3 and a[0] == "template":
        return cmd_template(a[1], a[2])
    if len(a) == 3 and a[0] == "parse":
        return cmd_parse(a[1], a[2])
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
