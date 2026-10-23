"""Functions referenced nowhere but their own def; flags whose dest is never read."""
import re, sys, pathlib
root = pathlib.Path("setup/harness")
cli = (root / "bin/harness").read_text()
others = "".join(p.read_text() for p in [root / "bin/harness-gui", root / "bin/harness-mail"])
tests = (root / "tests/test_harness.py").read_text()
lines = cli.splitlines()
defs = [(i + 1, m.group(1)) for i, l in enumerate(lines) if (m := re.match(r"def (\w+)\(", l))]
out = []
out.append("# functions in harness with no reference besides their def\n# line name refs_in_cli refs_in_tests refs_in_gui_mail")
for ln, name in defs:
    w = re.compile(r"\b%s\b" % re.escape(name))
    c = len(w.findall(cli)) - 1
    t = len(w.findall(tests))
    o = len(w.findall(others))
    if c == 0:
        out.append(f"{ln} {name} cli={c} tests={t} gui/mail={o}")
out.append("\n# functions used only once in the cli (single caller; inline candidates if tiny)")
for ln, name in defs:
    c = len(re.findall(r"\b%s\b" % re.escape(name), cli)) - 1
    if c == 1:
        out.append(f"{ln} {name}")
out.append("\n# flags whose dest is never read as a.<dest> / args.<dest> / getattr(.., '<dest>')")
for i, l in enumerate(lines):
    for m in re.finditer(r'add_argument\(\s*"(--[\w-]+)"(?:\s*,\s*"(--[\w-]+)")?', l):
        dest_m = re.search(r'dest\s*=\s*"(\w+)"', l)
        dest = dest_m.group(1) if dest_m else m.group(1)[2:].replace("-", "_")
        if not re.search(r"\.(%s)\b|['\"]%s['\"]" % (dest, dest), cli.replace(l, "")):
            out.append(f"{i+1} {m.group(1)} dest={dest}")
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n")
print(len(defs), "defs")
