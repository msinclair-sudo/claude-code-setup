"""Section sizes (bytes) of each harness SKILL.md, split at ## / ### headings,
with counts of 'log N' / 'obs N' / dated owner rulings (rationale markers) and
of `harness <sub>` command mentions per section."""
import re, sys, glob
for f in sys.argv[1:] or sorted(glob.glob('setup/skills/harness*/SKILL.md')):
    t = open(f).read(); secs = []; cur = '(top)'; buf = []
    for line in t.splitlines(keepends=True):
        if re.match(r'^#{2,3} ', line):
            secs.append((cur, ''.join(buf))); cur, buf = line.strip(), []
        buf.append(line)
    secs.append((cur, ''.join(buf)))
    print(f'== {f} {len(t.encode())} B')
    for h, b in secs:
        why = len(re.findall(r'\b(?:log|obs|logs)\s+\d+|\b20\d\d-\d\d-\d\d|\bbecause\b|\bWhy\b', b))
        cmds = len(re.findall(r'harness [a-z]+', b))
        print(f'   {len(b.encode()):6d} B  why-markers {why:3d}  cmds {cmds:3d}  {h[:80]}')
