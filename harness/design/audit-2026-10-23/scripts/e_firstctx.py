"""What fills a session's context before its first reply: sizes of the startup
attachments (rendered bytes) and the system prompt (prompt_snapshot), by role.
Also: for reviewers, whether the injected ponytail text reached the model.
Roles from whoami's 'run as' line, else cwd (same rule as e_startup.py)."""
import json, glob, os, re, collections, statistics as st
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
LEADS = {'dev', 'dev_tests', 'dev_dag', 'dev_tax', 'dev_readings', 'dev_migrate'}
def role_from_cwd(cwd):
    b = cwd.rstrip('/').split('/')[-1]
    for r in ('intermediary', 'documenter', 'reporter'):
        if r in cwd: return r
    if 'design' in cwd: return 'design'
    if b == 'biblion2': return 'root'
    return 'lead' if b.replace('biblion2-', '') in LEADS else 'member'
agg = collections.defaultdict(lambda: collections.defaultdict(list))
pony = collections.Counter(); nonpersist = []
for f in files:
    role = None; cwd = ''; sizes = collections.Counter(); seen_first = False; sysp = 0
    for l in open(f, errors='replace'):
        try: o = json.loads(l)
        except Exception: continue
        cwd = cwd or o.get('cwd', '')
        t = o.get('type')
        if t == 'assistant': seen_first = True; break
        if t == 'attachment':
            a = o['attachment']; at = a.get('type')
            if at == 'prompt_snapshot':
                sp = a.get('systemPrompt'); sysp = len(json.dumps(sp, ensure_ascii=False).encode()) if sp else 0
                continue
            rb = sum(len(x.get('content', '').encode()) for x in (o.get('rendered') or []) if isinstance(x, dict))
            if at == 'hook_success' and a.get('hookEvent') == 'SessionStart':
                so = a.get('stdout') or ''
                m = re.search(r'^run as .*\((\w+)\)\s*$', so, re.M)
                if m: role = m.group(1)
                if 'PONYTAIL MODE ACTIVE' in so:
                    pony['stdout has ponytail'] += 1
                    if any('PONYTAIL MODE ACTIVE' in x.get('content', '') for x in (o.get('rendered') or [])):
                        pony['model saw ponytail'] += 1
                if not (a.get('content') or '').startswith('<persisted-output>'):
                    nonpersist.append(len(so.encode()))
                at = 'SessionStart hook'
            sizes[at] += rb
    role = role or role_from_cwd(cwd)
    for k, v in sizes.items(): agg[role][k].append(v)
    agg[role]['system prompt (snapshot json)'].append(sysp)
for role, d in agg.items():
    n = max(len(v) for v in d.values())
    print(f'== {role} ({n} sessions): median rendered bytes per startup attachment (sessions with it)')
    for k, v in sorted(d.items(), key=lambda kv: -st.median(kv[1])):
        print(f'   {k:32s} n={len(v):4d} med={int(st.median(v)):7d} B ~{int(st.median(v))//4} tok')
print('\nponytail injection:', dict(pony))
print('non-persisted SessionStart stdout bytes: max', max(nonpersist), 'median', int(st.median(nonpersist)), 'n', len(nonpersist))
