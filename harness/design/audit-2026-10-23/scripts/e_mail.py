"""biblion2 doorbell mail: every delivered message (doorbell/<node>/delivered.jsonl).
Per node per day: count and bytes; by sender; by delivery path ('how');
most repeated texts after normalising numbers, hashes, quoted text and names.
Usage: python3 e_mail.py [--since YYYY-MM-DD]"""
import json, glob, os, re, sys, collections, statistics as st
SINCE = sys.argv[sys.argv.index('--since') + 1] if '--since' in sys.argv else ''
S = os.path.expanduser('~/.claude/harness/-mnt-a-OneDrive---Charles-Sturt-University-PhD-apps-biblion2/doorbell')
def norm(s):
    s = s.split('\n')[0]
    s = re.sub(r'\b[0-9a-f]{7,40}\b', 'H', s)
    s = re.sub(r"'[^']{1,80}'", "'X'", s)
    s = re.sub(r'"[^"]{1,200}"', '"X"', s)
    s = re.sub(r'\([^()]{1,160}\)', '(…)', s)
    s = re.sub(r'\bdev(_[a-z]+)?(_\d)?\b|\bmain\b', 'NODE', s)
    s = re.sub(r'\b[a-z0-9]+(?:[-_.][a-z0-9]+){1,}\b', 'NAME', s)
    s = re.sub(r'\d+', '#', s)
    return s[:150]
msgs = []
for f in glob.glob(f'{S}/*/delivered.jsonl'):
    node = f.split('/')[-2]
    for l in open(f, errors='replace'):
        try: m = json.loads(l)
        except Exception: continue
        day = (m.get('at') or m.get('delivered') or '')[:10]
        if SINCE and day < SINCE: continue
        m['_node'], m['_day'] = node, day; msgs.append(m)
print(f'{len(msgs)} delivered messages, {len({m["_node"] for m in msgs})} nodes, days {min(m["_day"] for m in msgs)}..{max(m["_day"] for m in msgs)}')
b = [len((m.get('text') or '').encode()) for m in msgs]
print(f'bytes: total {sum(b)} ~{sum(b)//4} tok, median {int(st.median(b))}, p90 {sorted(b)[int(.9*len(b))]}, max {max(b)}')
nd = collections.Counter((m['_node'], m['_day']) for m in msgs)
ndb = collections.Counter()
for m in msgs: ndb[(m['_node'], m['_day'])] += len((m.get('text') or '').encode())
v = list(nd.values())
print(f'per node-day ({len(v)} node-days): messages median {int(st.median(v))}, p90 {sorted(v)[int(.9*len(v))]}, max {max(v)}; bytes median {int(st.median(ndb.values()))}, max {max(ndb.values())}')
pn = collections.defaultdict(list)
for (n, d), c in nd.items(): pn[n].append(c)
print('per node: days active, msgs/day median, total msgs')
for n, cs in sorted(pn.items(), key=lambda kv: -sum(kv[1])):
    print(f'   {n:16s} {len(cs):3d} {int(st.median(cs)):4d} {sum(cs):5d}')
def sender(m):
    f = m.get('from') or '?'
    return 'intermediary' if f.startswith('intermediary') else f if f in ('harness', 'test queue', 'owner', 'researchd') else 'node' if re.match(r'^(main|dev)', f) else f
print('by sender:', collections.Counter(sender(m) for m in msgs).most_common(12))
print('by how:', collections.Counter(m.get('how') for m in msgs).most_common())
print('by priority:', collections.Counter(m.get('priority') for m in msgs).most_common())
c = collections.Counter(); cb = collections.Counter(); ex = {}
for m in msgs:
    k = f"[{sender(m)}] " + norm(m.get('text') or '')
    c[k] += 1; cb[k] += len((m.get('text') or '').encode()); ex.setdefault(k, (m.get('text') or '')[:220])
print('\nmost repeated (normalised first line): count, total bytes')
for k, n in sorted(c.items(), key=lambda kv: -cb[kv[0]])[:30]:
    if n < 5: continue
    print(f'  {n:5d} {cb[k]:8d} B | {k[:140]}')
    print(f'        e.g. {ex[k][:200]!r}')
