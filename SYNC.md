# SystemsBench has two homes. Keep them one thing.

| Home | What it is |
|---|---|
| [`InitiumBuilders/SystemsBench`](https://github.com/InitiumBuilders/SystemsBench) | the public canon |
| `DAVARA-DV2-BASELINE/systemsbench` | the copy Davara is built from |

**Every baseline release checks them, and any change to either must reach the
other before the release ships.** `scripts/sync-systemsbench.py` is the gate.

```bash
python3 scripts/sync-systemsbench.py          # report drift, both directions
python3 scripts/sync-systemsbench.py --gate   # non-zero exit if drifted (CI form)
python3 scripts/sync-systemsbench.py --pull   # canon -> baseline, only where canon is newer
python3 scripts/sync-systemsbench.py --stage  # baseline -> a push-ready clone, scrubbed
```

## The trap, recorded because it nearly cost the bank

The rule is *"always the latest"*, and the trap is **assuming you know which side
that is.**

On 2026-08-02 the public canon was at **v0.8.1 with 16 items**. The baseline copy
was at **v0.12.0 with 300** — four versions and 284 items *ahead*, because the
SF/CLD/DYN/LEV banks were each filled to 25/25/25 in July and never pushed up.

A naive "pull the latest from GitHub" would have **deleted 284 items.** The
newest commit date is not the newest content; a repo can be freshly touched and
badly stale at the same time.

So the tool never assumes a direction. It reports drift **per file, with a
direction**, and moves only what is provably older. Direction is a finding, not
a setting.

## The public repo is public

Anything staged to travel *up* is scrubbed first — API keys, private hostnames,
the relay name. A hit **aborts the run**; it does not warn and continue. The
scrub list lives in the script, not in someone's memory.

## What the baseline SERVES is a separate question

The repo mirrors the canon in full — including `results/`, `logs/` and the pitch
site. `MANIFEST.baseline` decides which handful of those files ride in Davara's
context. Mirror completely; serve deliberately.
