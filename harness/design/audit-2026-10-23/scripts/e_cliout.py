"""Size of what harness commands print back into sessions.
For each Bash tool call in biblion2 transcripts that runs harness subcommand(s)
(`harness sub`, `.../harness sub`, or `$H sub` after H=...harness), join the
tool_result and measure its bytes. Calls with exactly one harness subcommand are
attributed to it; others go to 'multi'. Also splits each subcommand by its
first flag, and reports whether the output was piped through head/sed/tail.
Usage: python3 e_cliout.py [sub ...]   (extra args: print the 5 largest results for those subs)
Results are de-duplicated by tool_use_id (a resumed session repeats its history).
"""
import json, glob, os, re, sys, collections, statistics as st
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
pat = re.compile(r'(?:^|[\s;&|(`])(?:\S*/harness|harness|\$H|\$\{H\})\s+([a-z][a-z-]+)((?:[ \t]+[^\s;&|]+)*)')
res = collections.defaultdict(list); byflag = collections.defaultdict(list); piped = collections.Counter()
big = collections.defaultdict(list); seen_ids = set()
for f in files:
    pend = {}
    for l in open(f, errors='replace'):
        if 'tool_use' not in l and 'tool_result' not in l: continue
        try: o = json.loads(l)
        except Exception: continue
        m = o.get('message') or {}
        c = m.get('content')
        if not isinstance(c, list): continue
        for x in c:
            if not isinstance(x, dict): continue
            if x.get('type') == 'tool_use' and x.get('name') == 'Bash':
                cmd = (x.get('input') or {}).get('command', '')
                if 'harness' not in cmd: continue
                hits = [(mm.group(1), mm.group(2) or '') for mm in pat.finditer(cmd)]
                hits = [h for h in hits if h[0] not in ('bin',)]
                if hits: pend[x['id']] = (hits, cmd)
            elif x.get('type') == 'tool_result' and x.get('tool_use_id') in pend and x.get('tool_use_id') not in seen_ids:
                seen_ids.add(x.get('tool_use_id'))
                hits, cmd = pend.pop(x['tool_use_id'])
                cc = x.get('content')
                txt = cc if isinstance(cc, str) else ''.join(y.get('text', '') for y in (cc or []) if isinstance(y, dict))
                b = len(txt.encode())
                key = hits[0][0] if len({h[0] for h in hits}) == 1 else 'multi'
                res[key].append(b)
                if key == 'multi':
                    for sub in {h[0] for h in hits}:
                        if sub in ('whoami', 'brief', 'note'): res['multi incl. ' + sub].append(b)
                if key != 'multi':
                    fl = re.findall(r'(--[a-z][\w-]*)', hits[0][1])
                    byflag[f'{key} {fl[0] if fl else "(none)"}'].append(b)
                    if re.search(r'\|\s*(head|tail|sed|grep)', cmd): piped[key] += 1
                    big[key].append((b, cmd[:200].replace('\n', ' '), f))
def q(xs, p): return sorted(xs)[int(p * (len(xs) - 1))]
tot = sum(sum(v) for v in res.values())
print(f'{len(files)} files; harness Bash results total {tot} B ~{tot//4} tok')
print('sub | calls | median B | p90 B | max B | total B | share | piped%')
for k, v in sorted(res.items(), key=lambda kv: -sum(kv[1]))[:30]:
    print(f'{k} | {len(v)} | {int(st.median(v))} | {q(v,.9)} | {max(v)} | {sum(v)} | {100*sum(v)/tot:.1f}% | {100*piped[k]//len(v)}%')
print('\nby first flag (top by total bytes):')
for k, v in sorted(byflag.items(), key=lambda kv: -sum(kv[1]))[:40]:
    print(f'  {k} | {len(v)} | med {int(st.median(v))} | p90 {q(v,.9)} | total {sum(v)}')
for s in sys.argv[1:]:
    print(f'\nlargest {s}:')
    for b, cmd, f in sorted(big[s], reverse=True)[:5]:
        print(f'  {b} {cmd}  [{os.path.basename(os.path.dirname(f))[-30:]}]')
