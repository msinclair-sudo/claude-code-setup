"""Repeated passages between the harness skills, the spec, why.md and CLI help.
Text is split into words (lowercased, punctuation dropped); a passage is shared
when a run of >= N consecutive words (default 10) appears in both documents.
For each skill: bytes covered by passages also in the spec / another skill /
`harness <sub> --help` (help is run in-process-free: `python3 -I harness <sub> --help`,
which argparse answers before doing any work). Then the longest shared runs.
Usage: python3 e_overlap.py [N]"""
import re, sys, subprocess, itertools, collections, os
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
SK = 'setup/skills'
docs = {}
for s in ['harness', 'harness-upward', 'harness-downward', 'harness-root', 'harness-reviewer',
          'harness-documenter', 'harness-intermediary', 'harness-reporter']:
    docs[s] = open(f'{SK}/{s}/SKILL.md').read()
docs['spec'] = open(f'{SK}/harness/ref/spec.md').read()
docs['why'] = open(f'{SK}/harness/ref/why.md').read()
helps = ''
for sub in ['ask', 'check', 'note', 'test', 'brief', 'mark', 'ring', 'pairs', 'whoami', 'doorbell', 'review',
            'integrate', 'queue', 'fact', 'finding', 'blocked', 'recycle', 'spawn', 'waiting', 'hold', 'slot', 'docs',
            'catchup', 'claim', 'release', 'status', 'focus', 'charter', 'sweep', 'report', 'documenter', 'intermediary']:
    try:
        helps += subprocess.run([sys.executable, '-I', 'setup/harness/bin/harness', sub, '--help'],
                                capture_output=True, text=True, timeout=30, stdin=subprocess.DEVNULL).stdout + '\n'
    except Exception:
        pass
docs['cli-help'] = helps
def words(t):
    out = []
    for m in re.finditer(r"[A-Za-z0-9_'\-]+", t):
        out.append((m.group(0).lower(), m.start(), m.end()))
    return out
W = {k: words(v) for k, v in docs.items()}
SH = {k: {tuple(x[0] for x in w[i:i + N]) for i in range(len(w) - N + 1)} for k, w in W.items()}
def covered(a, b):
    """bytes of a covered by N-word runs that also occur in b, and the runs."""
    w = W[a]; hit = [False] * len(w)
    for i in range(len(w) - N + 1):
        if tuple(x[0] for x in w[i:i + N]) in SH[b]:
            for j in range(i, i + N): hit[j] = True
    runs, i = [], 0
    while i < len(w):
        if hit[i]:
            j = i
            while j < len(w) and hit[j]: j += 1
            runs.append((w[i][1], w[j - 1][2])); i = j
        else: i += 1
    return sum(e - s for s, e in runs), runs
skills = [k for k in docs if k.startswith('harness')]
print(f'N={N} words. bytes of each skill also found in: (size in bytes)')
hdr = ['spec', 'why', 'cli-help'] + skills
print('skill'.ljust(22), 'size'.rjust(6), ' '.join(h[-10:].rjust(10) for h in hdr))
allruns = []
for a in skills:
    row = []
    for b in hdr:
        if a == b: row.append('-'.rjust(10)); continue
        c, runs = covered(a, b)
        row.append(str(c).rjust(10))
        for s, e in runs: allruns.append((e - s, a, b, docs[a][s:e]))
    print(a.ljust(22), str(len(docs[a])).rjust(6), ' '.join(row))
c, _ = covered('why', 'spec'); print(f'\nwhy.md bytes also in spec: {c} of {len(docs["why"])}')
print('\nlongest shared passages (skill -> other):')
seen = set()
for n, a, b, t in sorted(allruns, reverse=True):
    key = t[:60]
    if key in seen or n < 250: continue
    seen.add(key)
    print(f'  {n:5d} B  {a} ~ {b}: {" ".join(t.split())[:230]!r}')
    if len(seen) >= 25: break
