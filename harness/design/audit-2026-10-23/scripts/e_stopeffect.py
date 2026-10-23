"""What a session does right after a Stop-hook block, by block type.
Type = first words of the block. 'acted' = within the next 3 assistant entries the
session runs a harness command named in the block (e.g. 'mark X --done');
'stopped' = it ends with text only. For present-it blocks, the first other tool run. Also the context size the extra turn re-reads."""
import json, glob, os, re, collections, statistics as st
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
res = collections.defaultdict(collections.Counter); ctxs = []; seen = set(); first_tool = collections.Counter()
def kind(t):
    for k, p in [('present-it', 'You are about to stop with work on'), ('doorbell', 'Doorbell'),
                 ('owed-below', 'Owed to the rank below'), ('handoff-unasked', 'You ended saying this waits on the owner'),
                 ('reset-pending', 'A reset of this node is pending'), ('halted', 'The owner halted'),
                 ('deferral-back', 'Back from deferral'), ('rank0-yours', 'You are about to stop with these still yours'),
                 ('doorbell-unarmed', 'Your doorbell is not armed')]:
        if p in t[:200]: return k
    return 'other:' + t[:40]
for f in files:
    ents = []
    for l in open(f, errors='replace'):
        try: o = json.loads(l)
        except Exception: continue
        if o.get('uuid') in seen: continue
        seen.add(o.get('uuid')); ents.append(o)
    for i, o in enumerate(ents):
        if o.get('type') == 'attachment' and o['attachment'].get('type') == 'hook_blocking_error' and o['attachment'].get('hookEvent') == 'Stop':
            be = o['attachment'].get('blockingError') or {}
            t = be.get('blockingError', '') if isinstance(be, dict) else str(be)
            k = kind(t)
            cmds = set(re.findall(r'harness ([a-z]+ \S+(?: --[a-z-]+)?)', t))
            acted = None; n = 0
            for p in ents[i + 1:]:
                if p.get('type') != 'assistant': continue
                n += 1
                u = (p.get('message') or {}).get('usage') or {}
                if n == 1 and u: ctxs.append((u.get('cache_read_input_tokens') or 0) + (u.get('cache_creation_input_tokens') or 0))
                for x in (p.get('message') or {}).get('content') or []:
                    if isinstance(x, dict) and x.get('type') == 'tool_use':
                        c = json.dumps(x.get('input'))
                        if any(cm.split()[0] in c and (cm.split()[1] in c) for cm in cmds): acted = 'acted'
                        elif acted is None:
                            acted = 'other tool'
                            if k == 'present-it':
                                cmd = (x.get('input') or {}).get('command', '') if x.get('name') == 'Bash' else ''
                                hm = re.search(r'(?:harness|\$H)\s+([a-z]+(?: --[a-z-]+)?)', cmd)
                                first_tool[x.get('name') + (':harness ' + hm.group(1) if hm else (':git' if 'git ' in cmd else ''))] += 1
                if acted or n >= 3: break
            res[k][acted or 'text only, stopped'] += 1
for k, c in sorted(res.items(), key=lambda kv: -sum(kv[1].values())):
    print(f'{k:22s} n={sum(c.values()):5d}  ' + ', '.join(f'{a}: {v}' for a, v in c.most_common()))
print('present-it, first other tool:', first_tool.most_common(15))
print(f'context re-read by the forced extra turn: median {int(st.median(ctxs))} tok, total {sum(ctxs)} tok over {len(ctxs)} blocks')
