"""Stage C, C6: results by letter (the key stays sealed).

    python3 compile.py      usability/{factchecks,blind}/ -> usability/results.md; heldout/ -> heldout/results.md
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = HERE.parent
U = S / "usability"
sys.path.insert(0, str(HERE))
import c  # noqa: E402

CLASSES = ["supported", "overstated", "number", "unsupported", "do-not-say", "absence as fact", "access overreach",
           "illustration"]
FAULTS = ["overstated", "number", "unsupported", "do-not-say"]
PIECES = [f"T{k}-{n}{L}" for k in (1, 2, 3) for n in (1, 2) for L in "AB"]
IDS = ["C-DENIT", "C-ANALOG", "C-RANKNET", "C-PREDICT", "C-STEPDEN", "C-GHOSTFUS", "C-COVDIST"]


def fc_counts(p):
    text = (U / "factchecks" / f"{p}.factcheck.md").read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if re.search(r"supported\W*\d", ln, re.I)]
    line = lines[-1] if lines else ""
    out = {}
    for c_ in CLASSES:
        m = re.search(rf"\b{re.escape(c_)}\b\W*(\d+)", line, re.I)
        out[c_] = int(m.group(1)) if m else 0
    out["total"] = sum(out[c_] for c_ in CLASSES)
    return out


def blind_scores(p):
    text = (U / "blind" / f"{p}.blind.md").read_text(encoding="utf-8")
    sc = {}
    for ln in text.splitlines():
        m = re.match(r"\W*(A(?:10|[1-9]))\b[^0-9]*?(\d)\s*/\s*3", ln)
        if m and m.group(1) not in sc:
            sc[m.group(1)] = int(m.group(2))
    tot = re.search(r"Total\W*[^0-9]*(\d+)\s*/\s*30", text)
    sc["total"] = int(tot.group(1)) if tot else sum(v for k, v in sc.items() if k.startswith("A"))
    return sc


def pair(k, n):
    text = (U / "blind" / f"T{k}-pair{n}.blind.md").read_text(encoding="utf-8")
    pref = re.search(r"Preferred:\s*\**\s*([^\n*]+)", text)
    conf = re.search(r"Confidence:\s*\**\s*([^\n*]+)", text)
    why = re.search(r"Why[^:]*:\s*\**\s*(.+)", text, re.S)
    return (pref.group(1).strip() if pref else "?", conf.group(1).strip() if conf else "?",
            " ".join(why.group(1).split())[:400] if why else "")


def usability():
    L = ["# Stage C usability re-test: results by letter\n",
         "The key (`ab-key.sealed.md`) is sealed until the owner has graded all 12 pieces. Nothing here says which input "
         "a piece came from. Protocol: `protocol.md`; marking scheme: `marking-scheme.md`.\n",
         "## Fact-checks against the knowledge note\n",
         "| Piece | Words | Statements | " + " | ".join(c_.capitalize() for c_ in CLASSES) + " | Faults |",
         "|---|---|---|" + "---|" * len(CLASSES) + "---|"]
    for p in PIECES:
        f = fc_counts(p)
        w = len((U / "pieces" / f"{p}.md").read_text(encoding="utf-8").split())
        L.append(f"| {p} | {w} | {f['total']} | " + " | ".join(str(f[c_]) for c_ in CLASSES) +
                 f" | {sum(f[c_] for c_ in FAULTS)} |")
    L += ["", "Faults are overstated, number, unsupported and do-not-say, as in v3. Absences stated as fact and access "
          "overreach are counted separately (marking-scheme criteria A4 and A3).", "",
          "## Blind readers: Part A scores (0 to 3)\n",
          "| Piece | " + " | ".join(f"A{i}" for i in range(1, 11)) + " | Total /30 |", "|---|" + "---|" * 11]
    for p in PIECES:
        b = blind_scores(p)
        L.append(f"| {p} | " + " | ".join(str(b.get(f"A{i}", "?")) for i in range(1, 11)) + f" | {b['total']} |")
    L += ["", "## Blind readers: pair preferences\n", "| Pair | Preferred | Confidence | Why |", "|---|---|---|---|"]
    for k in (1, 2, 3):
        for n in (1, 2):
            pr, cf, why = pair(k, n)
            L.append(f"| T{k} pair {n} | {pr} | {cf} | {why.replace('|', '/')} |")
    L += ["", "## Writers' notes\n", "Each piece's `pieces/<piece>.notes.md` lists what its writer needed and could "
          "not find, and what was hard to use.", "",
          "## v3, for reference (different topics)\n",
          "v3's usability test (`../../../usability/results.md`): fact-check faults 27 for view pieces and 27 for raw "
          "pieces over three topics; all three blind readers preferred the raw piece."]
    (U / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"usability/results.md: {len(PIECES)} pieces")


def heldout():
    L = ["# Stage C held-out evaluation: results\n",
         "Seven notes drawn by seed (`draw.md`), built once by v4 frozen, first-pass checked by two fresh checkers per "
         "60-entry packet (a fault from either counted), fixed, and re-checked until clean. Per-note detail is in "
         "`../state.md` and each note's `first-pass.md`.\n",
         "| Note | Entries | First pass | Kinds |", "|---|---|---|---|"]
    tot = tf = 0
    for i in IDS:
        fp = (S / "heldout" / i / "first-pass.md").read_text(encoding="utf-8")
        m = re.search(r"First-pass fault rate: (\d+)/(\d+) = ([\d.]+%)", fp)
        k = re.search(r"Kinds \(entries\): (.+)\.", fp)
        tf, tot = tf + int(m.group(1)), tot + int(m.group(2))
        L.append(f"| {i} | {m.group(2)} | {m.group(1)} ({m.group(3)}) | {k.group(1) if k else ''} |")
    L.append(f"| **All** | **{tot}** | **{tf} ({tf / tot:.1%})** | |")
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        c.measures(IDS)
    L += ["", "## Near-copying and settings kept (claims; `../../stageB/tools/notestats.py` definitions)\n",
          buf.getvalue().rstrip(), "",
          "Stage B's v4 notes for comparison: claims with a real setting 78% to 98% by note; near-copies 19% to 63%."]
    (S / "heldout" / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"heldout/results.md: {tf}/{tot}")


if __name__ == "__main__":
    heldout()
    usability()
