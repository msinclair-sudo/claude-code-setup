"""Print one example of each hook attachment kind, with top-level keys and rendered text."""
import json, glob, os, sys
files = sorted(glob.glob(os.path.expanduser('~/.claude/projects/*biblion2-dev-2/*.jsonl')), key=os.path.getmtime)[-30:]
seen = set()
for f in files:
    for l in open(f, errors='replace'):
        if '"attachment"' not in l: continue
        o = json.loads(l)
        if o.get('type') != 'attachment': continue
        a = o['attachment']; k = (a.get('type'), a.get('hookEvent'), a.get('hookName'))
        if 'hook' not in (k[0] or '') or k in seen: continue
        seen.add(k)
        print('=====', k, 'toplevel:', sorted(o.keys()))
        for fld in ('content', 'stdout', 'blockingError'):
            if fld in a: print(f'--{fld}:', json.dumps(a[fld])[:700])
        if 'rendered' in o: print('--rendered:', json.dumps(o['rendered'])[:900])
