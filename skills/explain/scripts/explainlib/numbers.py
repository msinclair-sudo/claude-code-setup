"""Orphan numbers: every number shown or spoken must come from claims.yaml.

A number counts if it appears in a claim's `text` or `value`. Incidental
numbers (figure numbers, years in a citation, axis ticks drawn by a library)
go in storyboard `numbers_ok: [...]`. Numbers glued to letters ("16S", "D1",
"h2") are names, not quantities, and are skipped.
"""
import re
from html.parser import HTMLParser

NUM = re.compile(r"(?<![\w.])[-−]?\d[\d,]*(?:\.\d+)?(?![\w])")


def norm(tok: str) -> str:
    t = tok.replace(",", "").replace("−", "-")
    try:
        f = float(t)
    except ValueError:
        return t
    return str(int(f)) if f == int(f) else repr(f)


def found(text: str) -> set:
    return {norm(m.group()) for m in NUM.finditer(text or "")}


def ledger(r) -> set:
    ok = set()
    for c in r.claims:
        ok |= found(str(c.get("text", "")))
        v = c.get("value")
        if isinstance(v, (int, float)):
            ok.add(norm(str(v)))
        elif v is not None:
            ok |= found(str(v))
    ok |= {norm(str(x)) for x in r.story.get("numbers_ok") or []}
    return ok


class _Text(HTMLParser):
    """Visible text of a page, SVG <text> included; skips style and script."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    HIDDEN = ("style", "script", "metadata", "head")  # plus namespaced tags (rdf:, dc:, cc:)

    def _hidden(self, tag):
        return tag in self.HIDDEN or ":" in tag

    VOID = {"br", "img", "hr", "meta", "input", "link", "wbr", "source", "track", "col", "area", "base", "embed"}

    def handle_starttag(self, tag, attrs):
        if self.skip and tag not in self.VOID:  # inside a hidden block: count nesting so its end is found
            self.skip += 1
            return
        if self._hidden(tag) or "x-sources" in (dict(attrs).get("class") or ""):  # bibliography is not a claim
            self.skip += 1
            return
        for k, v in attrs:
            if k in ("alt", "aria-label") and v:
                self.parts.append(v)

    def handle_endtag(self, tag):
        if self.skip and tag not in self.VOID:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.parts.append(d)


def html_text(html: str) -> str:
    p = _Text(); p.feed(html or ""); return " ".join(p.parts)


def orphans(r, sources: dict) -> list:
    """sources: {where: text}. Returns ['where: 12.5 not in claims.yaml', ...]."""
    ok = ledger(r)
    out = []
    for where, text in sources.items():
        for n in sorted(found(text) - ok):
            out.append(f"{where}: {n} is not in claims.yaml (add the claim, or list it in numbers_ok)")
    return out
