"""Byte/token breakdown of the system-prompt files the harness writes for the
documenter, intermediary and design sessions, split at top-level '# ' headings,
and of the skill files. tokens ~= bytes/4."""
import os, re, glob, sys
S = os.path.expanduser('~/.claude/harness/-mnt-a-OneDrive---Charles-Sturt-University-PhD-apps-biblion2')
def split(path):
    txt = open(path, errors='replace').read()
    parts, cur, buf = [], '(preamble)', []
    for line in txt.splitlines(keepends=True):
        if re.match(r'^# \S', line):
            parts.append((cur, sum(len(x.encode()) for x in buf))); cur, buf = line.strip()[:70], []
        buf.append(line)
    parts.append((cur, sum(len(x.encode()) for x in buf)))
    return len(txt.encode()), parts
for p in ['documenter/prompt.md', 'intermediary/prompt.md', 'designs/enviroment-dag.prompt.md']:
    tot, parts = split(os.path.join(S, p))
    print(f'== {p}: {tot} B ~{tot//4} tok')
    for h, b in parts:
        if b > 300: print(f'   {b:7d} B ~{b//4:6d} tok  {h}')
