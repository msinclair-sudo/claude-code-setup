"""Every `log N` citation in the CLI, by line, with the entry's heading from OBSERVATIONS.md."""
import re, sys, pathlib, collections
cli = pathlib.Path("setup/harness/bin/harness").read_text().splitlines()
obs = (pathlib.Path.home() / ".claude/harness/OBSERVATIONS.md").read_text().splitlines()
heads = {}
for l in obs:
    m = re.match(r"#+\s*(?:Entry\s*)?(\d+)[.:)\s—-]+(.*)", l)
    if m and int(m.group(1)) not in heads:
        heads[int(m.group(1))] = m.group(2).strip()[:110]
cites = collections.defaultdict(list)
for i, l in enumerate(cli):
    for n in re.findall(r"[Ll]og (\d+)", l):
        cites[int(n)].append(i + 1)
out = ["# entry heading | cli lines citing it"]
for n in sorted(cites):
    out.append(f"{n} {heads.get(n, '?')} | {' '.join(map(str, cites[n]))}")
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n")
print(len(cites), "entries,", len(heads), "headings found")
