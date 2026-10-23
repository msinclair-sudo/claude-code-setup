"""Per-turn hook text in biblion2 sessions.

What the model sees from a hook is the entry's 'rendered' field (a
<system-reminder> block); entries are de-duplicated by uuid. Kinds:
  orient = hook_success UserPromptSubmit (hook-orient: delta + doorbell mail)
  stop   = hook_blocking_error Stop (hook-stop blocks; exit-0 stdout never reaches the model)
  post   = hook_additional_context PostToolUse (harness-mail doorbell)
  start  = SessionStart (whoami), reported apart, not per turn
A turn starts at each real prompt (user text that is not a tool result or meta),
which includes ringer wake prompts (isMeta user text 'Another Claude session sent a
message: harness ringer: ...'); those wake prompts are measured too.
Outputs: distribution per turn, per session-day and node-day totals, and the
most repeated lines after normalising numbers, hashes, times, names and quoted text.
Usage: python3 e_turns.py [--since YYYY-MM-DD]
"""
import json, glob, os, re, sys, collections, statistics as st
SINCE = sys.argv[sys.argv.index('--since') + 1] if '--since' in sys.argv else ''
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
seen = set()
turns = []                       # dicts: kind->bytes
sessday = collections.Counter(); nodeday = collections.Counter(); sessday_turns = collections.Counter()
lines = collections.Counter(); line_ex = {}
wake_prompts = []; kinds_total = collections.Counter(); kinds_n = collections.Counter()
PREFIX = re.compile(r'^(UserPromptSubmit hook success: |Stop hook blocking error from command: "[^"]*": |PostToolUse:\w+ hook additional context: |SessionStart:\w+ hook success: )')
def norm(s):
    s = re.sub(r'\b[0-9a-f]{7,40}\b', 'H', s)
    s = re.sub(r"'[^']{1,80}'", "'X'", s)
    s = re.sub(r'`[^`]{1,120}`', '`X`', s)
    s = re.sub(r'\bdev(_[a-z]+)?(_\d)?\b|\bmain\b', 'NODE', s)
    s = re.sub(r'\b[a-z0-9]+(?:[-_][a-z0-9]+){1,}\b', 'NAME', s)
    s = re.sub(r'\d+', '#', s)
    return s.strip()
def kind_of(o):
    a = o['attachment']; t = a.get('type'); e = a.get('hookEvent')
    if e == 'SessionStart': return 'start'
    if t == 'hook_success' and e == 'UserPromptSubmit': return 'orient'
    if t == 'hook_blocking_error' and e == 'Stop': return 'stop'
    if t == 'hook_additional_context' and e == 'PostToolUse': return 'post'
    return f'{t}:{e}'
for f in files:
    cur = None; cwd = ''
    for l in open(f, errors='replace'):
        try: o = json.loads(l)
        except Exception: continue
        u = o.get('uuid')
        if u in seen: continue
        seen.add(u)
        cwd = cwd or o.get('cwd', '')
        day = (o.get('timestamp') or '')[:10]
        if SINCE and day and day < SINCE: continue
        t = o.get('type')
        if t == 'user':
            c = (o.get('message') or {}).get('content')
            if o.get('isMeta') and not (isinstance(c, str) and 'harness ringer' in c[:200]):
                continue
            if isinstance(c, list) and any(isinstance(x, dict) and x.get('type') == 'tool_result' for x in c):
                continue
            txt = c if isinstance(c, str) else ''.join(x.get('text', '') for x in (c or []) if isinstance(x, dict))
            if not txt: continue
            cur = collections.Counter(); turns.append(cur)
            sessday_turns[(f, day)] += 1
            if 'harness ringer' in txt[:200]:
                wake_prompts.append(len(txt.encode()))
                for ln in txt.splitlines():
                    if ln.strip(): lines['[wake] ' + norm(ln)] += 1; line_ex.setdefault('[wake] ' + norm(ln), ln[:200])
            continue
        if t == 'attachment' and 'hook' in (o['attachment'].get('type') or '') and o.get('rendered'):
            k = kind_of(o)
            txt = ''.join(x.get('content', '') for x in o['rendered'] if isinstance(x, dict))
            txt = txt.replace('<system-reminder>\n', '').replace('\n</system-reminder>', '')
            b = len(txt.encode())
            kinds_total[k] += b; kinds_n[k] += 1
            if k == 'start': continue
            if cur is not None: cur[k] += b
            sessday[(f, day)] += b
            nodeday[(cwd.rstrip('/').split('/')[-1], day)] += b
            for ln in PREFIX.sub('', txt).splitlines():
                if ln.strip():
                    key = f'[{k}] ' + norm(ln)
                    lines[key] += 1; line_ex.setdefault(key, ln[:200])
def q(xs, p): return sorted(xs)[int(p * (len(xs) - 1))] if xs else 0
print(f'{len(files)} files, {len(turns)} turns')
print('\nhook text seen by the model, totals by kind:')
for k, v in kinds_total.most_common():
    print(f'  {k}: {kinds_n[k]} entries, {v} B ~{v//4} tok, mean {v//kinds_n[k]} B')
tot = [sum(c.values()) for c in turns]
nz = [x for x in tot if x]
print(f'\nper turn (all {len(tot)} turns): median {int(st.median(tot))} B, p90 {q(tot,.9)} B, max {max(tot)} B, mean {sum(tot)//len(tot)} B')
print(f'per turn with any hook text ({len(nz)} = {100*len(nz)//len(tot)}%): median {int(st.median(nz))} B, p90 {q(nz,.9)} B, max {max(nz)} B')
for k in ('orient', 'stop', 'post'):
    xs = [c[k] for c in turns if c[k]]
    print(f'  {k}: in {len(xs)} turns ({100*len(xs)//len(tot)}%), median {int(st.median(xs))} B, p90 {q(xs,.9)} B, max {max(xs)} B')
sd = list(sessday.values())
print(f'\nper session-day ({len(sd)} with hook text): median {int(st.median(sd))} B ~{int(st.median(sd))//4} tok, p90 {q(sd,.9)} B, max {max(sd)} B')
nd = list(nodeday.values())
print(f'per node-day ({len(nd)}): median {int(st.median(nd))} B ~{int(st.median(nd))//4} tok, p90 {q(nd,.9)} B, max {max(nd)} B')
top = sorted(nodeday.items(), key=lambda kv: -kv[1])[:8]
print('  largest node-days:', [(k, v) for k, v in top])
print(f'\nwake prompts ("harness ringer: ..."): {len(wake_prompts)}, median {int(st.median(wake_prompts))} B, p90 {q(wake_prompts,.9)} B, total {sum(wake_prompts)} B')
print('\nmost repeated lines (count, total bytes of that line across turns):')
rows = sorted(lines.items(), key=lambda kv: -kv[1] * len(line_ex[kv[0]]))[:40]
for k, n in rows:
    print(f'  {n:6d} x ~{len(line_ex[k]):4d} B = {n*len(line_ex[k]):8d} B | {k[:150]}')
