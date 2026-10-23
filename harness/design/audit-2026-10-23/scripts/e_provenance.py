"""Provenance in the skills a session loads: parentheticals and clauses citing
log/obs entries or dated owner rulings, e.g. '(log 172)', '(owner, 2026-10-15)',
'(obs 81)', '; --wait before 2026-10-16'. Bytes per skill and the load-weighted
cost using the measured load counts (e_startup.py)."""
import re, glob
LOADS = {'harness': 847, 'harness-upward': 415, 'harness-downward': 157, 'harness-reviewer': 82, 'harness-root': 7}
pat = re.compile(r'\s?\((?:[^()]*?\b(?:log|logs|obs)\s+\d+[^()]*|owner,? \d{4}-\d\d-\d\d[^()]*|[^()]*\b20\d\d-\d\d-\d\d[^()]*)\)|,?\s\b(?:log|obs)\s\d{2,3}\b')
tot = 0
for f in sorted(glob.glob('setup/skills/harness*/SKILL.md')):
    name = f.split('/')[2]; t = open(f).read()
    ms = pat.findall(t); b = sum(len(m.encode()) for m in ms)
    w = b * LOADS.get(name, 0)
    tot += w
    print(f'{name:22s} {len(ms):3d} citations {b:5d} B  loads {LOADS.get(name, 0):4d}  load-weighted {w:8d} B')
print(f'load-weighted total over the 18 days measured: {tot} B ~{tot//4} tok')
