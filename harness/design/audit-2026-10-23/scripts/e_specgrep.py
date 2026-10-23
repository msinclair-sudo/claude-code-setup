"""How sessions reach ref/spec.md and ref/why.md: Read calls (offset/limit) and
Bash/Grep calls naming the file, with the result bytes they brought back."""
import json, glob, os, re, collections
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
seen = set(); calls = []; pend = {}
for f in files:
    for l in open(f, errors='replace'):
        if 'spec.md' not in l and 'why.md' not in l and 'tool_result' not in l: continue
        try: o = json.loads(l)
        except Exception: continue
        if o.get('uuid') in seen: continue
        seen.add(o.get('uuid'))
        for x in (o.get('message') or {}).get('content') or []:
            if not isinstance(x, dict): continue
            if x.get('type') == 'tool_use':
                inp = json.dumps(x.get('input'))
                for doc in ('ref/spec.md', 'ref/why.md'):
                    if doc in inp and x['name'] in ('Read', 'Bash', 'Grep'):
                        if x['name'] == 'Bash' and not re.search(r'(grep|sed|cat|head|tail|awk|less)[^|;]*' + re.escape(doc), x['input'].get('command', '')): continue
                        pend[x['id']] = (doc, x['name'], (x.get('input') or {}).get('offset'), (x.get('input') or {}).get('limit'), os.path.basename(os.path.dirname(f))[-25:])
            elif x.get('type') == 'tool_result' and x.get('tool_use_id') in pend:
                cc = x.get('content'); t = cc if isinstance(cc, str) else ''.join(y.get('text', '') for y in cc or [] if isinstance(y, dict))
                calls.append(pend.pop(x['tool_use_id']) + (len(t.encode()),))
c = collections.Counter((d, n) for d, n, *_ in calls)
print('calls by doc and tool:', dict(c))
for d in ('ref/spec.md', 'ref/why.md'):
    xs = [r for r in calls if r[0] == d]
    print(f'{d}: {len(xs)} calls, {sum(r[-1] for r in xs)} B returned; sessions dirs: {collections.Counter(r[4] for r in xs).most_common(6)}')
    print('   Read offsets/limits:', [(r[2], r[3]) for r in xs if r[1] == 'Read'][:20])
