"""Survey hook-related jsonl entries across biblion2 transcripts.
Counts (attachment.type, hookEvent) and bytes of 'content'/'stdout'/'rendered'."""
import json, glob, os, collections, sys
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
c = collections.Counter(); b = collections.Counter(); keys = collections.defaultdict(set)
for f in files:
    for l in open(f, errors='replace'):
        if '"attachment"' not in l and 'stop_hook_summary' not in l: continue
        try: o = json.loads(l)
        except Exception: continue
        if o.get('type') == 'attachment':
            a = o['attachment']; t = a.get('type', '')
            if 'hook' not in t: continue
            k = (t, a.get('hookEvent') or a.get('hookName'))
            c[k] += 1
            b[k] += len(json.dumps(a.get('content') or a.get('blockingError') or a.get('stdout') or a.get('additionalContext') or ''))
            keys[k] |= set(a.keys())
        elif o.get('subtype') == 'stop_hook_summary':
            c[('stop_hook_summary', '')] += 1
print(len(files), 'files')
for k, v in c.most_common():
    print(v, b[k], k, sorted(keys[k]))
