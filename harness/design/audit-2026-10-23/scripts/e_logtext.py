"""Internal log/obs citations in text the CLI shows sessions.
1) Source: non-comment lines in the CLI with 'log N'/'obs N' inside a string literal,
   on lines that are part of print/die/ring_inbox/stop_block/text= calls (approximate:
   the line contains a quote before the citation and is not a '#' comment).
2) Transcripts: occurrences of 'log N' / 'obs N' in harness Bash results and in hook
   text the model saw, with the most frequent citations."""
import re, json, glob, os, collections
src = open('setup/harness/bin/harness').read().splitlines()
hits = []
for i, l in enumerate(src, 1):
    s = l.strip()
    if s.startswith('#') or '"""' in s: continue
    m = re.search(r'''(["'])[^"'#]*?\b(?:log|logs|obs)\s+\d+''', l)
    if m and not re.match(r'\s*(def |class )', l):
        hits.append((i, s[:140]))
print(f'{len(hits)} CLI source lines with a log/obs citation inside a string literal (sample):')
for i, s in hits[:15]: print(f'  {i}: {s}')
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
pat = re.compile(r'\b(?:log|obs) (\d{2,3})\b')
cnt = collections.Counter(); where = collections.Counter(); seen = set()
for f in files:
    for l in open(f, errors='replace'):
        if 'log ' not in l and 'obs ' not in l: continue
        try: o = json.loads(l)
        except Exception: continue
        if o.get('uuid') in seen: continue
        seen.add(o.get('uuid'))
        texts = []
        if o.get('type') == 'attachment' and 'hook' in (o['attachment'].get('type') or ''):
            texts = [('hook', x.get('content', '')) for x in (o.get('rendered') or []) if isinstance(x, dict)]
        elif o.get('type') == 'user':
            c = (o.get('message') or {}).get('content')
            if isinstance(c, list):
                for x in c:
                    if isinstance(x, dict) and x.get('type') == 'tool_result':
                        cc = x.get('content')
                        tx = cc if isinstance(cc, str) else ''.join(y.get('text', '') for y in (cc or []) if isinstance(y, dict))
                        if 'harness' in tx[:4000] or True: texts.append(('tool', tx))
        for k, t in texts:
            for m in pat.finditer(t):
                cnt[m.group(0)] += 1; where[k] += 1
print('\ncitations seen in hook text / tool results:', dict(where))
print('most frequent:', cnt.most_common(15))
