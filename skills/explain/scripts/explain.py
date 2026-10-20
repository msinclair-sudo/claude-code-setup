"""explain: make a report at the lowest tier that carries the message.

    x new <dir> --tier N --title "..." [--voice]   scaffold brief, storyboard, claims, tokens, src/
    x lint <dir>                                   check the plan before building
    x build <dir> [--draft]                        render build/ (draft: 480p15 video; final 1080p at REPORT_FPS, default 30)
    x stills <dir>                                 screenshots / frames + contact sheets in checks/
    x check <dir> --round N                        every automated check -> checks/round-N.json
    x fallback <dir>                               static/ that the harness can publish today
    x all <dir> --round N [--draft]                lint, build, stills, check, fallback in one go
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

from explainlib import report

TEMPLATES = report.TEMPLATES
SRC = {0: ["note.md"], 1: ["page_t1.md", "figures_t1.py"], 2: ["slides.html"],
       3: ["page_t3.md", "figures_t3.py"], 4: ["scene.py"]}


def cmd_new(a):
    d = Path(a.dir)
    if d.exists() and any(d.iterdir()):
        sys.exit(f"{d} exists and is not empty")
    (d / "src").mkdir(parents=True, exist_ok=True)
    for f in ("brief.md", "claims.yaml"):
        shutil.copy(TEMPLATES / f, d / f)
    shutil.copy(TEMPLATES / "theme/tokens.json", d / "tokens.json")
    sb = (TEMPLATES / "storyboard.yaml").read_text()
    sb = sb.replace("{{TITLE}}", a.title).replace("{{TIER}}", str(a.tier)).replace("{{VOICE}}", "true" if a.voice else "false")
    (d / "storyboard.yaml").write_text(sb)
    for f in SRC[a.tier]:
        dest = d / "src" / {"figures": "figures.py", "page": "page.md"}.get(f.split("_t")[0], f)
        shutil.copy(TEMPLATES / "src" / f, dest)
    print(f"{d}: tier {a.tier} ({report.TIERS[a.tier]}). Next: fill brief.md, storyboard.yaml, claims.yaml, then `x lint {d}`.")


def cmd_lint(a):
    from explainlib.lint import lint
    r = report.load(a.dir)
    res = lint(r)
    for level, msg in res:
        print(f"{level.upper():5s} {msg}")
    errs = sum(1 for l, _ in res if l == "error")
    print(f"lint: {errs} error(s), {len(res) - errs} warning(s)")
    return 1 if errs else 0


def cmd_build(a):
    from explainlib.build import build
    r = report.load(a.dir)
    out = build(r, draft=a.draft, only=[s for s in (a.only or "").split(",") if s] or None)
    print(f"built {out}: " + ", ".join(sorted(p.name for p in out.iterdir())))


def cmd_stills(a):
    from explainlib.stills import stills
    sheets = stills(report.load(a.dir))
    print("contact sheets: " + ", ".join(str(s) for s in sheets))


def cmd_check(a):
    from explainlib.check import run
    res = run(report.load(a.dir), a.round)
    for f in res["faults"]:
        print("FAULT", f)
    for w in res["warnings"]:
        print("warn ", w)
    print(f"round {a.round}: {'PASS' if res['pass'] else 'FAIL'} ({len(res['faults'])} faults, {len(res['warnings'])} warnings)"
          f" -> checks/round-{a.round}.json")
    return 0 if res["pass"] else 1


def cmd_fallback(a):
    from explainlib.fallback import fallback
    bad = fallback(report.load(a.dir))
    print("\n".join(f"FAULT static: {b}" for b in bad) or f"static/: publishable ({Path(a.dir) / 'static'})")
    return 1 if bad else 0


def cmd_all(a):
    if cmd_lint(a):
        return 1
    cmd_build(a); cmd_stills(a)
    rc = cmd_check(a)
    return cmd_fallback(a) or rc


def main():
    ap = argparse.ArgumentParser(prog="x", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("new"); p.add_argument("dir"); p.add_argument("--tier", type=int, required=True, choices=range(5))
    p.add_argument("--title", required=True); p.add_argument("--voice", action="store_true"); p.set_defaults(f=cmd_new)
    for name, f in (("lint", cmd_lint), ("stills", cmd_stills), ("fallback", cmd_fallback)):
        p = sp.add_parser(name); p.add_argument("dir"); p.set_defaults(f=f)
    p = sp.add_parser("build"); p.add_argument("dir"); p.add_argument("--draft", action="store_true")
    p.add_argument("--only", help="tier 4: re-render these scenes (comma-separated), reuse the others"); p.set_defaults(f=cmd_build)
    p = sp.add_parser("check"); p.add_argument("dir"); p.add_argument("--round", type=int, default=1); p.set_defaults(f=cmd_check)
    p = sp.add_parser("all"); p.add_argument("dir"); p.add_argument("--round", type=int, default=1)
    p.add_argument("--draft", action="store_true"); p.set_defaults(f=cmd_all)
    a = ap.parse_args()
    sys.exit(a.f(a) or 0)


if __name__ == "__main__":
    main()
