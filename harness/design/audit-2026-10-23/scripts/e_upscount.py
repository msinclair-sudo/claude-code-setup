"""Are UserPromptSubmit hook entries written when the hook prints nothing?
Counts UPS entries by stdout empty/non-empty, and prompt-like entries."""
import json, glob, os, collections
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
c = collections.Counter(); seen = set()
for f in files:
    for l in open(f, errors='replace'):
        if 'UserPromptSubmit' not in l and '"user"' not in l and 'queued_command' not in l: continue
        try: o = json.loads(l)
        except Exception: continue
        if o.get('uuid') in seen: continue
        seen.add(o.get('uuid'))
        t = o.get('type')
        if t == 'attachment':
            a = o['attachment']
            if a.get('hookEvent') == 'UserPromptSubmit':
                c[(a.get('type'), 'empty' if not (a.get('stdout') or '').strip() else 'text', 'rendered' if o.get('rendered') else 'no-render')] += 1
            elif a.get('type') == 'queued_command':
                c['queued_command'] += 1
        elif t == 'user':
            cc = (o.get('message') or {}).get('content')
            if isinstance(cc, str):
                c['user str ' + ('meta-ringer' if 'harness ringer' in cc[:200] else 'meta' if o.get('isMeta') else 'prompt')] += 1
            elif isinstance(cc, list) and cc and isinstance(cc[0], dict) and cc[0].get('type') == 'text':
                c['user list-text ' + ('meta' if o.get('isMeta') else 'prompt')] += 1
for k, v in c.most_common(): print(v, k)
