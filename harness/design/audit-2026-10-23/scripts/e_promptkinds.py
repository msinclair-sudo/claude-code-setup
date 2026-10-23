"""What entry carries the prompt that fires UserPromptSubmit? For each orient
hook entry, classify the nearest preceding non-attachment entry."""
import json, glob, os, collections
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2-dev-2/*.jsonl'))[:60]
c = collections.Counter(); ex = {}
for f in files:
    prev = []
    for l in open(f, errors='replace'):
        try: o = json.loads(l)
        except Exception: continue
        t = o.get('type')
        if t == 'attachment' and o['attachment'].get('hookEvent') == 'UserPromptSubmit':
            for p in reversed(prev[-6:]):
                k = (p.get('type'), p.get('isMeta'), (p.get('attachment') or {}).get('type'), type((p.get('message') or {}).get('content')).__name__)
                if p.get('type') in ('user', 'attachment', 'queue-operation'):
                    c[k] += 1; ex.setdefault(k, json.dumps(p)[:400]); break
        prev.append(o)
for k, v in c.most_common(): print(v, k); print('   ', ex[k][:400])
