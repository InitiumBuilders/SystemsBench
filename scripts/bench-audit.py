#!/usr/bin/env python3
"""bench-audit.py — count SystemsBench correctly. (Second pass; the first was wrong.)

INDEX.md holds TWO tables: a coverage MATRIX (Format x L1-L4 counts) and an item
REGISTER (ID, Format, Diff, Domain, Constructs, Date, File). The first version of
this script latched onto the matrix header and then read every following row as
data under it — so the per-format and per-level counts it produced were nonsense,
and it reported "no maturity column" when maturity is in fact carried inside the
File column as `gold: PROVISIONAL`.

Recorded because the correction matters more than the mistake: a script that
parses a document by position will believe whatever the document's shape suggests.
This one finds each table by its OWN header and refuses to guess.

Published to the public repo in SenseRun #11 (2026-09-27). It resolves the repo
root from its own location (or takes it as the first argument) and reports
agreement as well as drift, so a README that matches the register is recorded
as matching instead of being assumed stale.

SenseRun #12 (2026-09-27) added the maturity guard: every item's rung is
recomputed from evidence (oracle JSONs, the harness prompt file, gold files) and
compared with the register's Status column. A claim above the evidence fails
the run (exit 3). Understated claims are reported, not failed.

Usage:  python3 scripts/bench-audit.py            (from anywhere in the repo)
        python3 scripts/bench-audit.py /path/to/repo
"""
import io, os, re, sys, collections

_here = os.path.dirname(os.path.abspath(__file__))
R = (sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(_here)).rstrip('/') + '/'
raw = io.open(R + 'items/INDEX.md', encoding='utf-8').read()

def tables(md):
    """Every markdown table, each as (header_cells, [row_cells...])."""
    out, hdr, rows = [], None, []
    for line in md.split('\n'):
        t = line.strip()
        if t.startswith('|'):
            cells = [c.strip() for c in t.strip('|').split('|')]
            if set(''.join(cells)) <= set('-: ') and hdr:
                continue                       # separator
            if hdr is None:
                hdr, rows = cells, []
            else:
                rows.append(cells)
        else:
            if hdr:
                out.append((hdr, rows))
            hdr, rows = None, []
    if hdr:
        out.append((hdr, rows))
    return out

tabs = tables(raw)
matrix = next((t for t in tabs if t[0][0].lower() == 'format'), None)
register = next((t for t in tabs if t[0][0].lower() == 'id'), None)
print('  tables found: %d' % len(tabs))
print('  coverage matrix: %s' % ('yes, %d rows' % len(matrix[1]) if matrix else 'NO'))
print('  item register:   %s' % ('yes, %d rows' % len(register[1]) if register else 'NO'))

claimed_total, per_fmt_claim = 0, {}
if matrix:
    for row in matrix[1]:
        fmt = row[0].strip()
        nums = [int(re.sub(r'\D', '', c) or 0) for c in row[1:]]
        per_fmt_claim[fmt] = sum(nums)
        claimed_total += sum(nums)

items = register[1] if register else []
H = [h.lower() for h in (register[0] if register else [])]
def idx(frag):
    return next((i for i, h in enumerate(H) if frag in h), None)
i_fmt, i_diff, i_dom, i_file, i_status = idx('format'), idx('diff'), idx('domain'), idx('file'), idx('status')

fmts = collections.Counter()
diffs = collections.Counter()
doms = collections.Counter()
gold = collections.Counter()
for row in items:
    if i_fmt is not None and i_fmt < len(row): fmts[row[i_fmt]] += 1
    if i_diff is not None and i_diff < len(row): diffs[row[i_diff]] += 1
    if i_dom is not None and i_dom < len(row): doms[row[i_dom]] += 1
    cell = row[i_file] if (i_file is not None and i_file < len(row)) else ''
    m = re.search(r'gold:\s*([A-Za-z-]+)', cell)
    gold[m.group(1).upper() if m else 'NO GOLD REFERENCE'] += 1

# ── maturity: the earned rung per item, from evidence; the claimed rung from the column ──
import json, glob
RUNGS = ['AUTHORED', 'REVIEWED', 'ORACLE-READY', 'EXECUTABLE', 'HUMAN-CALIBRATED', 'CERTIFIED']
def _load(p):
    try: return json.load(io.open(R + p, encoding='utf-8'))
    except Exception: return {}
_oracle = set(_load('items/cld_oracle.json').get('items', {})) | set(_load('items/dyn_oracle.json').get('items', {}))
_hp = _load('items/harness_prompts.json')
_harness = set().union(*[set(_hp[k].get('items', {})) for k in _hp if k != '_meta' and isinstance(_hp[k], dict)]) if _hp else set()
_gold = {}
for _f in glob.glob(R + 'calibration/gold/*.gold.md'):
    _gold[os.path.basename(_f).replace('.gold.md', '')] = io.open(_f, encoding='utf-8').read()
_human = {k for k, v in _gold.items() if re.search(r'HUMAN-CALIBRATED|raters:\s*human', v, re.I)}
def earned(item_id, file_cell):
    if item_id in _human: return 'HUMAN-CALIBRATED'
    if item_id in _oracle and item_id in _harness: return 'EXECUTABLE'
    if item_id in _oracle or item_id in _gold: return 'ORACLE-READY'
    if re.search(r'reviewed:', file_cell or ''): return 'REVIEWED'
    return 'AUTHORED'
maturity = collections.Counter(); violations = []; understated = []
for row in items:
    _id = row[0]; _file = row[i_file] if (i_file is not None and i_file < len(row)) else ''
    e = earned(_id, _file); maturity[e] += 1
    if i_status is not None and i_status < len(row):
        c = row[i_status].strip()
        if c in RUNGS and RUNGS.index(c) > RUNGS.index(e): violations.append((_id, c, e))
        elif c in RUNGS and RUNGS.index(c) < RUNGS.index(e): understated.append((_id, c, e))
        elif c not in RUNGS: violations.append((_id, c, e))
has_status = i_status is not None

cl = io.open(R + 'CHANGELOG.md', encoding='utf-8').read()
rd = io.open(R + 'README.md', encoding='utf-8').read()
chg_v = (re.search(r'^##\s*(v[\d.]+)', cl, re.M) or [None, '?'])[1]
rd_v = (re.search(r'\*\*(v[\d.]+)\*\*', rd) or [None, '?'])[1]
rd_items = (re.search(r'\*\*(\d+)\s+items?\*\*', rd) or [None, '?'])[1]
agree = (chg_v == rd_v) and str(rd_items).isdigit() and int(rd_items) == len(items)

L = []; A = L.append
A('# SystemsBench — Status, Counted')
A('')
A('*Generated by `scripts/bench-audit.py`. Every number is derived from the files.')
A('If a README disagrees with this, the README is wrong — that is the point.*')
A('')
A('## What the bank actually holds')
A('')
A('**%d items in the register.** The coverage matrix claims **%d**.' % (len(items), claimed_total))
A('')
if len(items) != claimed_total:
    A('> Those two numbers come from two tables in the same file and **they disagree')
    A('> by %d**. The matrix is hand-maintained; the register is the roll. Trust the' % abs(len(items) - claimed_total))
    A('> register.')
    A('')
if fmts:
    A('| Format | In register | Matrix claims |')
    A('|---|---|---|')
    for k, v in fmts.most_common():
        A('| `%s` | %d | %s |' % (k, v, per_fmt_claim.get(k, '—')))
    for k, v in per_fmt_claim.items():
        if k not in fmts and v == 0:
            A('| `%s` | 0 | 0 · **not seeded** |' % k)
    A('')
if diffs:
    A('### By difficulty')
    A('')
    A('| Level | Items |')
    A('|---|---|')
    for k, v in sorted(diffs.items()):
        A('| %s | %d |' % (k, v))
    A('')

A('## Maturity — counted from evidence')
A('')
A('Each item\'s rung is computed from the files (oracle JSONs, the harness prompt')
A('file, the gold files), and compared with the `Status` column in the register.')
A('')
A('| Rung | Items | Earned when |')
A('|---|---|---|')
_when = {'AUTHORED': 'in the register with a prompt and a seed-file reference',
         'REVIEWED': 'a named second reader signed it (`reviewed:`)',
         'ORACLE-READY': 'machine-readable reference (oracle JSON) or a gold file',
         'EXECUTABLE': 'oracle + harness: elicit, parse, score with no hand in the loop',
         'HUMAN-CALIBRATED': 'a gold file with human labels clearing the §3.1 gate',
         'CERTIFIED': 'human-calibrated + a live-run item statistic on file'}
for k in RUNGS:
    A('| `%s` | %d | %s |' % (k, maturity.get(k, 0), _when[k]))
A('')
if not has_status:
    A('**The register carries no `Status` column.** Add it; this script will guard it.')
elif violations:
    A('**GUARD FAILED — %d item(s) claim a rung above the evidence:**' % len(violations))
    for _id, c, e in violations[:20]:
        A('- `%s` claims `%s`, earned `%s`' % (_id, c, e))
else:
    A('**Guard: every claimed rung is earned.** %d item(s) claim below what they earned (understated, not a failure).' % len(understated))
A('')
A('| Gold reference | Items |')
A('|---|---|')
for k, v in gold.most_common():
    A('| %s | %d |' % (k, v))
A('')
A('No item is `HUMAN-CALIBRATED` or `CERTIFIED`. The mechanism to become either')
A('now exists (a rung with a definition, and a guard); the labels do not, because no')
A('human has graded an item and no live run has happened. The SF format has reference')
A('answers and an exact-match rule but no scorer script and no harness template, so its')
A('%d items stay `AUTHORED` until `engine/sf-score.py` exists (BACKLOG #15).' % fmts.get('SF', 0))
A('')
A('## Version and count, checked')
A('')
A('| Source | Says |')
A('|---|---|')
A('| `CHANGELOG.md` | **%s** |' % chg_v)
A('| `README.md` | **%s**, "%s items" |' % (rd_v, rd_items))
A('| this register | **%d items** |' % len(items))
A('')
if agree:
    A('README, CHANGELOG and the register agree.')
else:
    A('The CHANGELOG is current; the README is stale by several versions and its')
    A('item count is off by roughly %dx. Nobody lied — the versions moved and the' % max(1, round(len(items) / max(1, int(rd_items) if str(rd_items).isdigit() else 1))))
    A('prose did not.')
A('')
A('## What may be said in public')
A('')
A('- ✅ "%d authored items across %d seeded formats"' % (len(items), len([k for k, v in fmts.items() if v])))
if agree:
    A('- ✅ the README states the counted number (%d) and the CHANGELOG version (%s)' % (len(items), chg_v))
else:
    A('- ❌ "%s items" (README) — stale' % rd_items)
A('- ❌ any claim of calibration, certification, or IRT stability')
A('')
A('*Re-run `python3 scripts/bench-audit.py` after any change to the register.*')

io.open(R + 'STATUS.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('\n  ok  STATUS.md rewritten')
print('  register: %d items | matrix claims: %d' % (len(items), claimed_total))
print('  formats: %s' % dict(fmts))
print('  gold:    %s' % dict(gold))
print('  readme/changelog/register: %s' % ('AGREE' if agree else 'DRIFT'))
print('  maturity: %s' % dict(maturity))
if has_status and violations:
    print('  GUARD FAILED: %d claim(s) above evidence' % len(violations)); sys.exit(3)
print('  guard: %s' % ('every claimed rung is earned' if has_status else 'no Status column to guard'))
