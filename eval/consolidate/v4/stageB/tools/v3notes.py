"""The 14 v3 as-built notes, their v3 inventories (v3 detection, kn_v3.py = skills/consolidate/scripts/kn.py at
66d17ef) and first-pass verdicts, with v4 checker hints. Shared by stage B's baseline re-score, hint-effect and
planted-fault tools.

    python3 v3notes.py --parity     the v4 hints reproduce stage A's R1 and R2-setting flags on every entry
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path[:0] = [str(HERE), str(ROOT / "eval" / "consolidate" / "v4" / "stageA"), str(ROOT / "skills" / "consolidate" / "scripts")]
import kn_v3  # noqa: E402
import kn as kn4  # noqa: E402
import score_lint  # noqa: E402

score_lint.kn = kn_v3            # stage A's loader, on v3 detection: the addresses the v3 checkers saw


def load():
    """[{note, id, type, verdict, entry, cited, refs, bib}], one per checked entry of the v3 as-built notes."""
    rows, _ = score_lint.load()
    bibs = {}
    for nid, path, _ in score_lint.NOTES:
        bibs[nid] = score_lint.parse_note(path)[1]
    for r in rows:
        r["bib"] = bibs[r["note"]]
        r["hints"] = kn4.hints(r["entry"], r["cited"], r["bib"])
    return rows


def block(r, with_hints):
    """An entry as the v4 checker sees it: statement, fields, cited text, and the hints line if asked for."""
    e, f = r["entry"], r["entry"]["fields"]
    out = [f"{e['statement']}\n\n", "".join(f"- {k}: {v}\n" for k, v in f.items() if k != "from"), "\nFrom the note:\n\n"]
    out += [f"> {t}\n>\n" for t in r["cited"]]
    if with_hints and r["hints"]:
        out.append(f"\n{kn4.HINT_LINE}: {'; '.join(r['hints'])}\n")
    return "".join(out)


if __name__ == "__main__" and "--parity" in sys.argv:
    rows = load()
    bad = []
    for r in rows:
        stage_a = bool(r["r1"]) or bool(r["r2"] and r["r2"]["setting"])
        if stage_a != bool(r["hints"]):
            bad.append((r["note"], r["id"], r["r1"], (r["r2"] or {}).get("setting"), r["hints"]))
    print(f"{len(rows)} entries; hinted {sum(1 for r in rows if r['hints'])}; "
          f"stage A flagged (R1 or R2-setting) {sum(1 for r in rows if r['r1'] or (r['r2'] and r['r2']['setting']))}; "
          f"mismatches {len(bad)}")
    for b in bad[:15]:
        print("  ", b)
