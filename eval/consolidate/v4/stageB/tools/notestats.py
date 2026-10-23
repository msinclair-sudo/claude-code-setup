"""Per-note measures for stage B (owner, 2026-10-23): information for the B8 report, not gate criteria, and the
early-stop checks run after each rebuilt note's first pass.

    python3 notestats.py <NOTE> [<NOTE> ...]    v3 against v4 (both first-pass, as built) for each note

Definitions (fixed 2026-10-23, before any B4 note was built):
- **Real setting in `holds`:** a claim's `holds` is not empty or "not stated", and has at least one setting-type
  token by the rule the v4 checker hints use for `holds` (kn.hints, from stage A's R2-setting): a capitalised word,
  a number or a token with a digit, a hyphenated token, or a word of the setting lexicon (kn.HINT_SETTING).
- **Near-copy:** at least 80% of a claim statement's words lie in runs of three or more words copied, in order,
  from one of its cited sentences.
Both are over claims (not do-not-say entries). v3 is the as-built note in v3/as-built or heldout/as-built, with v3
inventories; v4 is stageB/rebuild/<NOTE>/as-built.md, with v4 inventories.
"""
import difflib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v3notes  # noqa: E402

kn4, kn3, sl = v3notes.kn4, v3notes.kn_v3, v3notes.score_lint
REBUILD = HERE.parent / "rebuild"
NOT_SET = {"", "not stated", "none", "not given", "unstated"}


def load(path, mod):
    """[{id, type, statement, fields, cited}] for one note, with inventories from `mod` (kn_v3 or kn)."""
    sl.kn = mod
    try:
        entries, _, inputs = sl.parse_note(Path(path))
        text = Path(path).read_text(encoding="utf-8")
        decls = mod.declared_answers(mod.frontmatter(text)) if hasattr(mod, "declared_answers") else {}
        items = {}
        for nid, p in inputs.items():
            inv = mod.detect(p, nid, decls.get(nid))[1] if decls is not None and mod is kn4 else mod.detect(p, nid)[1]
            for x in inv:
                items[f"{nid}:{x['id']}"] = x
        default = next(iter(inputs)) if len(inputs) == 1 else "?"
        for e in entries:
            e["cited"] = [items[g]["text"] for ref in mod.entry_refs(e["fields"], default)
                          for g in (mod.expand(ref) or [ref]) if g in items]
        return entries
    finally:
        sl.kn = kn3


def real_setting(holds):
    h = kn4._hnorm(holds or "").strip()
    if h.lower().strip(" .") in NOT_SET:
        return False
    caps = {m.group(0).lower().rstrip("'-") for m in kn4._HCAP.finditer(h) if len(m.group(0)) >= 2}
    lex = {kn4._hstem(x) for x in kn4.HINT_SETTING}
    for w in kn4._HWORD.findall(h.lower()):
        w = w.strip(".'-")
        if w and (w in caps or re.search(r"\d", w) or "-" in w or w in kn4.HINT_SETTING or kn4._hstem(w) in lex):
            return True
    return False


def words(t):
    return [w.strip(".'-") for w in kn4._HWORD.findall(kn4._hnorm(t).lower()) if w.strip(".'-")]


def near_copy(statement, cited):
    s = words(statement)
    if not s:
        return False
    best = 0
    for c in cited:
        m = difflib.SequenceMatcher(None, s, words(c), autojunk=False)
        best = max(best, sum(b.size for b in m.get_matching_blocks() if b.size >= 3))
    return best / len(s) >= 0.8


def v3_path(note):
    return next(p for nid, p, _ in sl.NOTES if nid == note)


def stats(entries):
    cl = [e for e in entries if e["type"] == "claim"]
    return {"claims": len(cl), "setting": sum(real_setting(e["fields"].get("holds")) for e in cl),
            "near": sum(near_copy(e["statement"], e["cited"]) for e in cl)}


def main(notes):
    out = ["| Note | v3 claims | v3 with a setting | v4 claims | v4 with a setting | v4/v3 share | v3 near-copies | "
           "v4 near-copies |", "|---|---|---|---|---|---|---|---|"]
    for n in notes:
        a = stats(load(v3_path(n), kn3))
        b = stats(load(REBUILD / n / "as-built.md", kn4))
        sa, sb = a["setting"] / a["claims"], b["setting"] / b["claims"]
        out.append(f"| {n} | {a['claims']} | {a['setting']} ({sa:.0%}) | {b['claims']} | {b['setting']} ({sb:.0%}) | "
                   f"{sb / sa:.2f} | {a['near']} ({a['near'] / a['claims']:.0%}) | "
                   f"{b['near']} ({b['near'] / b['claims']:.0%}) |")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1:])
