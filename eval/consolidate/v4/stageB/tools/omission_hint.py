"""The omission hint as tested in B1b (plan.md, revision 4, stage B step 2b). It was built in the skill (560d0cf) and
not adopted (planted2/results.md), so the skill's checker stays at B1's setup and the code lives here, unchanged, as
the record of what was tested. It uses kn.py's hint normalisation (`_hnorm`, `_hstem`, `_HWORD`).

Hedge, negation, contrast and scope words of the cited text that the entry does not carry. A word counts as carried
only with the next content word after it, so "by this corpus" is listed even when the entry uses "by" elsewhere.
Claims only. Fixed list, not tuned on results.
"""
import re

import kn as kn4

_hnorm, _hstem, _HWORD = kn4._hnorm, kn4._hstem, kn4._HWORD

OMIT_WORDS = set("""may might could suggest likely unlikely possibly perhaps probably appear seem apparently tentative
putative preliminary uncertain unclear predict
not no never none neither nor without cannot lack fail
but however although though whereas yet except unless despite rather contrary argue dispute contradict
only nearest closest by one single some few several most mostly often sometimes partly partial within among per under
when if""".split())
_OMIT_STEMS = {_hstem(w) for w in OMIT_WORDS}
_OMIT_STOP = set("""the a an this that these those its their it of to as at in on for and or is are was were be been
being has have had with from than""".split())
_OMIT_SKIP = {"from", "src", "trail", "conf", "class", "search", "contrary"}   # controlled values, not the entry's words
OMIT_LINE = "In the cited text, not in the entry (where to look, not what is wrong)"


def _is_omit(w):
    s = _hstem(w)
    return w in OMIT_WORDS or s in _OMIT_STEMS or s + "e" in OMIT_WORDS or (w.endswith("n't") and w != "n't")


def omission_hints(e, cited_texts, cap=8):
    """Hedge, negation, contrast and scope words in an entry's cited text that the entry leaves out, each with up to
    four following words, for the checker. Claims only; a list of short strings, empty when none."""
    if e["type"] != "claim":
        return []
    f = e["fields"]
    own = [e["statement"]] + [v for k, v in f.items() if k not in _OMIT_SKIP]
    toks = [[_hstem(w.strip(".'-")) for w in _HWORD.findall(_hnorm(t).lower())] for t in own]

    def carried(w, nxt):
        # the word, followed within four words by the next content word after it, in the entry's own wording
        w, nxt = _hstem(w), (_hstem(nxt) if nxt else None)
        for ts in toks:
            for j, t in enumerate(ts):
                if t == w and (nxt is None or nxt in ts[j + 1:j + 5]):
                    return True
        return False

    out = []
    for t in cited_texts:
        for clause in re.split(r"[.;:!?()\[\],\"]+|\s[-–—]\s", _hnorm(t)):
            ws = [w.strip(".'-") for w in _HWORD.findall(clause.lower())]
            ws = [w for w in ws if w]
            start = end = -1                     # the current window; overlapping windows merge into one phrase
            for i, w in enumerate(ws):
                if not _is_omit(w):
                    continue
                nxt = next((x for x in ws[i + 1:] if x not in _OMIT_STOP), None)
                if carried(w, nxt):
                    continue
                if i < end:
                    end = i + 5
                    out[-1] = " ".join(ws[start:end])
                else:
                    start, end = i, i + 5
                    out.append(" ".join(ws[start:end]))
    return list(dict.fromkeys(out))[:cap]
