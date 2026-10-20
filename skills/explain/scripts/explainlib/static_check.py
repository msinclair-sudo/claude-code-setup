"""Can this page be published by the harness as it stands? (Tiers 0-1 and every static/ fallback.)

`report_html_check` and its constants are copied VERBATIM from the harness CLI
(setup/harness/bin/harness, report_html_check, at commit b5c40b9); a drift test
compares the two. `check_bundle` adds the publish-time limits from report_publish.

    python -m explainlib.static_check <dir-with-index.html>
"""
import re
import sys
from pathlib import Path

REPORT_HTML_CAP = 2 * 2**20
REPORT_ASSETS_MAX, REPORT_ASSET_CAP, REPORT_ASSETS_TOTAL = 30, 10 * 2**20, 40 * 2**20
REPORT_ASSET_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,80}$")
REPORT_IMAGE = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")
_MAGIC = {".png": b"\x89PNG", ".gif": b"GIF8", ".webp": b"RIFF"}

# ---- verbatim from harness (b5c40b9) ----
_REPORT_BAD_TAGS = {"script", "iframe", "frame", "frameset", "object", "embed", "applet",
                    "form", "input", "button", "textarea", "select", "base", "link", "portal",
                    "audio", "video", "source", "track", "foreignobject", "noscript"}
_REPORT_URL_ATTRS = {"src", "href", "xlink:href", "srcset", "poster", "action", "formaction",
                     "background", "data", "cite", "longdesc", "usemap", "lowsrc", "dynsrc"}
_REPORT_IMG_ATTRS = {"src", "srcset", "poster", "xlink:href", "lowsrc", "dynsrc", "background"}
_REPORT_DATA_IMG = re.compile(r"^data:image/(png|jpeg|gif|webp|svg\+xml)[;,]")
_REPORT_CSS_BAD = re.compile(r"@import|expression\s*\(|behavior\s*:|-moz-binding", re.I)
_REPORT_CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I | re.S)


def _report_url(v):
    return re.sub(r"[\x00-\x20]", "", v or "").lower()


def report_html_check(text, assets):
    """The faults that keep `text` from being published: [str]. A report is a
    static page — nothing in it may run, load from elsewhere, or submit."""
    from html.parser import HTMLParser
    names = set(assets or ())
    faults = []

    def css(s, where):
        if _REPORT_CSS_BAD.search(s or ""):
            faults.append(f"{where}: @import, expression(), behavior or -moz-binding")
        for m in _REPORT_CSS_URL.finditer(s or ""):
            u = m.group(2).strip()
            if not (_REPORT_DATA_IMG.match(_report_url(u)) or u in names):
                faults.append(f"{where}: url({u[:60]}) is not a listed figure or a data image")

    class P(HTMLParser):
        style = False

        def handle_starttag(self, tag, attrs):
            self.check(tag, attrs)
            if tag == "style":
                self.style = True

        def handle_startendtag(self, tag, attrs):
            self.check(tag, attrs)

        def handle_endtag(self, tag):
            if tag == "style":
                self.style = False

        def handle_data(self, data):
            if self.style:
                css(data, "<style>")

        def check(self, tag, attrs):
            line = self.getpos()[0]
            at = f"line {line}, <{tag}>"
            if tag in _REPORT_BAD_TAGS:
                faults.append(f"{at}: no {tag} in a report (nothing may run, load or submit)")
            a = {k: (v or "") for k, v in attrs}
            if tag == "meta" and "http-equiv" in a:
                faults.append(f"{at}: no meta http-equiv")
            if tag in ("set", "animate", "animatemotion", "animatetransform") and \
                    a.get("attributename", "").lower() in ("href", "xlink:href"):
                faults.append(f"{at}: no animated link")
            for k, v in a.items():
                if k.startswith("on"):
                    faults.append(f"{at}: no {k}= handler")
                elif k == "style":
                    css(v, at)
                elif k in _REPORT_URL_ATTRS:
                    for u in ([x.strip().split(" ")[0] for x in v.split(",")] if k == "srcset"
                              else [v.strip()]):
                        lu = _report_url(u)
                        if lu.startswith(("javascript:", "vbscript:")):
                            faults.append(f"{at}: {k}={u[:60]}: no script URLs")
                        elif lu.startswith("data:") and not _REPORT_DATA_IMG.match(lu):
                            faults.append(f"{at}: {k}: data: only for images")
                        elif k in _REPORT_IMG_ATTRS or (tag in ("use", "image", "img")):
                            if not (_REPORT_DATA_IMG.match(lu) or u in names
                                    or (tag == "use" and u.startswith("#"))):
                                faults.append(f"{at}: {k}={u[:60]} is not a listed figure or "
                                              f"a data image")
                        elif k == "href" and tag == "a":
                            if not (u.startswith("#") or u in names
                                    or lu.startswith(("http://", "https://"))):
                                faults.append(f"{at}: href={u[:60]}: link to #a-section, a "
                                              f"listed figure, or an http(s) page")
                        elif lu and not lu.startswith("#"):
                            faults.append(f"{at}: {k}={u[:60]}: nothing is loaded from "
                                          f"elsewhere")

    try:
        P(convert_charrefs=True).feed(text or "")
    except Exception as e:
        faults.append(f"unreadable HTML: {e}")
    return faults

# ---- end verbatim ----


def check_bundle(d) -> list:
    """Faults that would stop `harness report --publish index.html --asset <every image>` in d."""
    d = Path(d)
    page = d / "index.html"
    if not page.is_file():
        return [f"{page}: missing"]
    raw = page.read_bytes()
    faults = []
    if len(raw) > REPORT_HTML_CAP:
        faults.append(f"index.html is {len(raw)} bytes; at most {REPORT_HTML_CAP}")
    imgs = sorted(p for p in d.iterdir() if p.is_file() and p.suffix.lower() in REPORT_IMAGE)
    if len(imgs) > REPORT_ASSETS_MAX:
        faults.append(f"{len(imgs)} figures; at most {REPORT_ASSETS_MAX}")
    total = 0
    for p in imgs:
        if not REPORT_ASSET_RE.match(p.name):
            faults.append(f"{p.name}: letters, digits, '.', '_' and '-' only")
        n = p.stat().st_size; total += n
        if n > REPORT_ASSET_CAP:
            faults.append(f"{p.name}: {n} bytes; at most {REPORT_ASSET_CAP}")
        body = p.read_bytes()
        if p.suffix.lower() == ".svg":
            faults += [f"{p.name}: {f}" for f in report_html_check(body.decode("utf-8", "replace"), [])]
        elif not body.startswith(_MAGIC.get(p.suffix.lower(), b"\xff\xd8")):
            faults.append(f"{p.name} is not the image its name says")
    if total > REPORT_ASSETS_TOTAL:
        faults.append(f"figures total {total} bytes; at most {REPORT_ASSETS_TOTAL}")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return faults + ["index.html is not UTF-8"]
    return faults + report_html_check(text, [p.name for p in imgs])


if __name__ == "__main__":
    bad = check_bundle(sys.argv[1])
    print("\n".join(bad) or "static_check: publishable")
    sys.exit(1 if bad else 0)
