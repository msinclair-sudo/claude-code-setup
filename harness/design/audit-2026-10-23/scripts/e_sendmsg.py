"""Cross-session messages (SendMessage) between biblion2 sessions, besides the ringer.
Counts received messages ('Another Claude session sent a message:' meta prompts) whose
body is not a harness ringer wake, their size, and how many say 'presented'
(a duplicate of the doorbell ring cmd_mark already sends). Also counts SendMessage
tool calls made right after a `harness mark ... --done`."""
import json, glob, os, re, collections, statistics as st
files = glob.glob(os.path.expanduser('~/.claude/projects/*biblion2*/*.jsonl'))
seen = set(); recv = []; pres = 0; after_done = 0; done_calls = 0
for f in files:
    last_done = False
    for l in open(f, errors='replace'):
        try: o = json.loads(l)
        except Exception: continue
        if o.get('uuid') in seen: continue
        seen.add(o.get('uuid'))
        if o.get('type') == 'user' and o.get('isMeta'):
            c = (o.get('message') or {}).get('content')
            if isinstance(c, str) and c.startswith('Another Claude session sent a message') and 'harness ringer' not in c[:300]:
                recv.append(len(c.encode()))
                if re.search(r'presented at [0-9a-f]{7,}|is presented', c): pres += 1
        if o.get('type') == 'assistant':
            for x in (o.get('message') or {}).get('content') or []:
                if not isinstance(x, dict) or x.get('type') != 'tool_use': continue
                if x.get('name') == 'Bash' and re.search(r'harness\s+mark\s+\S+.*--done', x['input'].get('command', '')):
                    last_done = True; done_calls += 1
                elif x.get('name') == 'SendMessage':
                    if last_done and 'presented' in json.dumps(x.get('input')): after_done += 1
                    last_done = False
print(f'cross-session messages received (not ringer): {len(recv)}, median {int(st.median(recv))} B, total {sum(recv)} B ~{sum(recv)//4} tok')
print(f'  of which announce a presentation: {pres}')
print(f'mark --done calls: {done_calls}; SendMessage "presented" sent right after one: {after_done}')
