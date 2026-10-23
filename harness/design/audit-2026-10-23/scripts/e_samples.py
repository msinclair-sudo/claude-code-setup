"""Print sample outputs (near the median size) of single harness subcommand calls
from the last days of biblion2 transcripts, to read what the output spends bytes on.
Usage: python3 e_samples.py 'brief' '(none)' [since]"""
import json, glob, os, re, sys, statistics as st
sub, flag = sys.argv[1], sys.argv[2]; since = sys.argv[3] if len(sys.argv) > 3 else '2026-10-20'
pat = re.compile(r'(?:^|[\s;&|(`])(?:\S*/harness|harness|\$H)\s+([a-z][a-z-]+)((?:[ \t]+[^\s;&|]+)*)')
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
out = []
for f in files:
    pend = {}
    for l in open(f, errors='replace'):
        if 'tool_' not in l: continue
        o = json.loads(l)
        if (o.get('timestamp') or '') < since: continue
        for x in (o.get('message') or {}).get('content') or []:
            if not isinstance(x, dict): continue
            if x.get('type') == 'tool_use' and x.get('name') == 'Bash':
                cmd = x['input'].get('command', '')
                h = [(m.group(1), m.group(2)) for m in pat.finditer(cmd)]
                if len(h) == 1 and h[0][0] == sub and '|' not in cmd:
                    fl = re.findall(r'(--[a-z][\w-]*)', h[0][1])
                    if (fl[0] if fl else '(none)') == flag: pend[x['id']] = cmd
            elif x.get('type') == 'tool_result' and x.get('tool_use_id') in pend:
                cc = x.get('content'); t = cc if isinstance(cc, str) else ''.join(y.get('text', '') for y in cc or [] if isinstance(y, dict))
                out.append((len(t), pend.pop(x['tool_use_id']), t))
out.sort(key=lambda r: r[0])
print(len(out), 'samples; median', out[len(out)//2][0] if out else 0)
for r in out[len(out)//2: len(out)//2 + 2]:
    print('=' * 20, r[0], r[1][:150]); print(r[2][:3500])
