"""Startup text per role, from biblion2 transcripts.

Per session file: role (from whoami's 'run as ... (role)' line, else from cwd),
first prompt bytes and its '# Project scope' share, SessionStart hook output
(stdout bytes, what the model saw = 'rendered' bytes, persisted or not),
Skill loads (name and injected bytes), Reads of spec.md / why.md / SKILL.md /
persisted hook output (with offset/limit), first-turn context from API usage.
Also a bytes-per-token calibration from Skill loads (usage delta / bytes).
Usage: python3 e_startup.py [--since YYYY-MM-DD]
"""
import json, glob, os, re, sys, statistics as st, collections
SINCE = sys.argv[sys.argv.index('--since') + 1] if '--since' in sys.argv else ''
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
LEADS = {'dev_tests', 'dev_dag', 'dev_tax', 'dev_readings', 'dev_migrate'}

def role_from_cwd(cwd):
    if '/intermediary' in cwd or 'intermediary' in cwd.split('/')[-1]: return 'intermediary'
    if 'documenter' in cwd: return 'documenter'
    if 'reporter' in cwd: return 'reporter'
    if '/designs' in cwd or 'design' in cwd.split('/')[-1]: return 'design'
    base = cwd.rstrip('/').split('/')[-1]
    if base == 'biblion2': return 'root'
    node = base.replace('biblion2-', '')
    if node == 'dev': return 'lead'
    if node in LEADS: return 'lead'
    return 'member'

def text_of(c):
    if isinstance(c, str): return c
    if isinstance(c, list):
        return ''.join(x.get('text', '') if isinstance(x, dict) and x.get('type') == 'text' else '' for x in c)
    return ''

def ctx_tokens(u):
    return (u.get('input_tokens') or 0) + (u.get('cache_creation_input_tokens') or 0) + (u.get('cache_read_input_tokens') or 0)

rows = []; calib = []
reads = collections.Counter(); read_detail = collections.defaultdict(list)
for f in files:
    R = dict(file=f, role=None, cwd='', date='', first_prompt=0, scope_in_prompt=0, ss=[], skills=[],
             first_ctx=None, whoami_bash=[], spec_reads=[], why_reads=[], hookfile_reads=0, skillmd_reads=0)
    pending_skill = None; tool_names = {}; last_ctx = None; skill_wait = None
    try:
        lines = open(f, errors='replace').read().splitlines()
    except Exception:
        continue
    for l in lines:
        try: o = json.loads(l)
        except Exception: continue
        t = o.get('type')
        if not R['cwd'] and o.get('cwd'): R['cwd'] = o['cwd']
        if not R['date'] and o.get('timestamp'): R['date'] = o['timestamp'][:10]
        if t == 'attachment':
            a = o['attachment']
            if a.get('type') == 'hook_success' and a.get('hookEvent') == 'SessionStart':
                so = a.get('stdout') or ''
                rend = sum(len(x.get('content', '').encode()) for x in (o.get('rendered') or []))
                R['ss'].append((a.get('hookName'), len(so.encode()), rend, (a.get('content') or '').startswith('<persisted-output>')))
                m = re.search(r'^run as .*\((\w+)\)\s*$', so, re.M)
                if m and not R['role']: R['role'] = m.group(1)
        elif t == 'assistant':
            m = o.get('message') or {}
            u = m.get('usage') or {}
            if u:
                c = ctx_tokens(u)
                if R['first_ctx'] is None: R['first_ctx'] = c
                if skill_wait and last_ctx is not None:
                    calib.append((skill_wait, c - last_ctx - last_out)); skill_wait = None
                last_ctx = c; last_out = u.get('output_tokens') or 0
            for x in (m.get('content') or []):
                if isinstance(x, dict) and x.get('type') == 'tool_use':
                    tool_names[x['id']] = (x['name'], x.get('input') or {})
                    inp = x.get('input') or {}
                    if x['name'] == 'Skill':
                        pending_skill = inp.get('skill')
                    if x['name'] == 'Read':
                        p = inp.get('file_path', '')
                        key = ('spec.md' if p.endswith('ref/spec.md') else 'why.md' if p.endswith('ref/why.md') else
                               'hook-stdout' if 'tool-results/hook-' in p else
                               'SKILL.md' if p.endswith('SKILL.md') and 'harness' in p else None)
                        if key:
                            reads[key] += 1
                            read_detail[key].append((inp.get('offset'), inp.get('limit')))
                            if key == 'spec.md': R['spec_reads'].append((inp.get('offset'), inp.get('limit')))
                            if key == 'why.md': R['why_reads'].append((inp.get('offset'), inp.get('limit')))
                            if key == 'hook-stdout': R['hookfile_reads'] += 1
                            if key == 'SKILL.md': R['skillmd_reads'] += 1
                    js = json.dumps(inp)
                    for doc in ('spec.md', 'why.md'):
                        if doc in js and x['name'] != 'Read':
                            R.setdefault('other_'+doc, []).append(x['name'] + ':' + (inp.get('command') or inp.get('pattern') or '')[:160])
                    if x['name'] == 'Bash' and re.search(r'harness\S*\s+whoami', inp.get('command', '')):
                        R['whoami_bash'].append(x['id'])
        elif t == 'user':
            m = o.get('message') or {}
            c = m.get('content')
            if o.get('isMeta') and pending_skill:
                b = len(text_of(c).encode())
                R['skills'].append((pending_skill, b)); skill_wait = b; pending_skill = None
                continue
            if isinstance(c, list) and any(isinstance(x, dict) and x.get('type') == 'tool_result' for x in c):
                for x in c:
                    if isinstance(x, dict) and x.get('tool_use_id') in R['whoami_bash']:
                        cc = x.get('content')
                        tx = cc if isinstance(cc, str) else ''.join(y.get('text', '') for y in (cc or []) if isinstance(y, dict))
                        R.setdefault('whoami_out', []).append(len(tx.encode()))
                continue
            txt = text_of(c)
            if txt and not R['first_prompt'] and not o.get('isMeta'):
                R['first_prompt'] = len(txt.encode())
                if txt.lstrip().startswith('# Project scope'):
                    i = txt.find('\n# Your start')
                    R['scope_in_prompt'] = len(txt[:i if i > 0 else len(txt)].encode())
    if not R['role']:
        R['role'] = role_from_cwd(R['cwd'])
    if SINCE and R['date'] < SINCE: continue
    rows.append(R)

def med(xs): return int(st.median(xs)) if xs else 0
def p90(xs): return int(sorted(xs)[int(0.9 * (len(xs) - 1))]) if xs else 0
print(f'{len(rows)} sessions')
by = collections.defaultdict(list)
for R in rows: by[R['role']].append(R)
print('\nrole | sessions | first prompt B (med) | scope in prompt B (med, n>0) | SessionStart stdout B (med) | seen by model B (med) | persisted % | skills loaded/session | skill text B (med/session) | first-turn ctx tok (med)')
for role, rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
    ss = [s for R in rs for s in R['ss']]
    sk = [sum(b for _, b in R['skills']) for R in rs]
    fp = [R['first_prompt'] for R in rs if R['first_prompt']]
    sc = [R['scope_in_prompt'] for R in rs if R['scope_in_prompt']]
    print(f"{role} | {len(rs)} | {med(fp)} | {med(sc)} (n={len(sc)}) | {med([s[1] for s in ss])} | {med([s[2] for s in ss])} | "
          f"{100*sum(s[3] for s in ss)//max(1,len(ss))}% of {len(ss)} | {sum(len(R['skills']) for R in rs)/len(rs):.2f} | {med(sk)} | {med([R['first_ctx'] for R in rs if R['first_ctx']])}")
print('\nrole | sessions running whoami by Bash | whoami Bash result B per session (med of sum) | harness-attributable startup B (med): prompt + SessionStart seen + skills + whoami Bash')
for role, rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
    w = [sum(R.get('whoami_out', [])) for R in rs]
    tot = [R['first_prompt'] + sum(s[2] for s in R['ss'][:1]) + sum(b for _, b in R['skills']) + sum(R.get('whoami_out', [])) for R in rs]
    print(f"{role} | {sum(1 for x in w if x)} | {med([x for x in w if x])} | {med(tot)} B ~{med(tot)//4} tok")
print('\nSkill loads by role:')
for role, rs in by.items():
    c = collections.Counter(n for R in rs for n, _ in R['skills'])
    print(' ', role, dict(c.most_common()))
print('\nSkill injected bytes (median by skill):')
sb = collections.defaultdict(list)
for R in rows:
    for n, b in R['skills']: sb[n].append(b)
for n, bs in sorted(sb.items(), key=lambda kv: -len(kv[1])):
    print(f'  {n}: n={len(bs)} med={med(bs)} B')
print('\nSessionStart by hookName (stdout med / seen med / persisted):')
hb = collections.defaultdict(list)
for R in rows:
    for s in R['ss']: hb[s[0]].append(s)
for k, v in hb.items():
    print(f'  {k}: n={len(v)} stdout med={med([s[1] for s in v])} p90={p90([s[1] for s in v])} seen med={med([s[2] for s in v])} persisted={sum(s[3] for s in v)}')
print('\nReads:', dict(reads))
for k in ('spec.md', 'why.md'):
    d = read_detail[k]
    print(f'  {k}: {len(d)} reads, whole-file (no offset/limit) {sum(1 for o, l in d if o is None and l is None)}, '
          f'sessions reading it {sum(1 for R in rows if R[k.split(".")[0] + "_reads"])} of {len(rows)}')
    print('    offsets:', collections.Counter(o for o, l in d).most_common(12))
    print('    limits :', collections.Counter(l for o, l in d).most_common(8))
    rr = collections.Counter(R['role'] for R in rows if R[k.split(".")[0] + "_reads"])
    print('    by role:', dict(rr))
for doc in ('spec.md', 'why.md'):
    oth = [c for R in rows for c in R.get('other_'+doc, [])]
    print(f'  {doc} touched by non-Read tools: {len(oth)} calls in {sum(1 for R in rows if R.get("other_"+doc))} sessions')
    for c in oth[:12]: print('     ', c.replace(chr(10), ' ')[:160])
print('  sessions reading persisted hook output:', sum(1 for R in rows if R['hookfile_reads']), 'reads', sum(R['hookfile_reads'] for R in rows))
print('  sessions re-reading harness SKILL.md by Read:', sum(1 for R in rows if R['skillmd_reads']))
print('  sessions running `harness whoami` by Bash:', sum(1 for R in rows if R['whoami_bash']), 'calls', sum(len(R['whoami_bash']) for R in rows))
cal = [d / b * 1 for b, d in calib if b > 2000 and 0 < d < b]
if cal:
    print(f'\nCalibration from {len(cal)} skill loads: tokens/byte med={st.median(cal):.3f} -> bytes/token ~{1/st.median(cal):.2f} (context delta minus the previous reply output tokens; still includes the tool call and result)')
