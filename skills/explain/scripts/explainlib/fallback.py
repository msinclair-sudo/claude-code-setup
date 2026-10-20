"""static/: the publishable version of any tier (no script, no media, <= 30 images).

  tier 0/1   build/ as it is
  tier 2     one still per step with its narration as text beneath
  tier 3     the page prose with each plot's SVG fallback in its place
  tier 4     the last frame of each segment with its narration beneath
"""
import html
import json
import re
import shutil

from . import static_check
from .build import page

MAX = 30


def _steps_page(r, stills, texts, intro):
    rows = []
    for p, text in zip(stills, texts):
        rows.append(f'<figure><img src="{p.name}" alt="{html.escape(text or p.stem)}">'
                    f'<figcaption>{html.escape(text)}</figcaption></figure>')
    body = (f'<h1>{html.escape(r.story.get("title", ""))}</h1>\n'
            f'<p class="x-message">{html.escape(r.story.get("message", ""))}</p>\n'
            f'<p class="x-muted">{intro}</p>\n' + "\n".join(rows))
    return page(r, body, wide=True)


def fallback(r) -> list:
    out = r.p("static")
    if out.exists():
        shutil.rmtree(out)
    t = r.tier
    if t in (0, 1):
        shutil.copytree(r.p("build"), out)
        for extra in ("note.md",):
            (out / extra).unlink(missing_ok=True)
    else:
        out.mkdir()
        stills = sorted(r.p("checks/stills").glob("*.png"))
        if t == 3:
            src = r.p("build/page.html").read_text()
            for svg in r.p("build/fallback").glob("*.svg"):
                shutil.copy(svg, out / svg.name)
            src = re.sub(r'<div class="x-plot" data-plot="([\w-]+)">.*?</script>\s*</div>\s*</div>',
                         lambda m: f'<figure><img src="{m.group(1)}.svg" alt="{m.group(1)}: default view"></figure>',
                         src, flags=re.S)
            src = re.sub(r"<script.*?</script>", "", src, flags=re.S)
            (out / "index.html").write_text(src)
        else:
            if t == 2:
                by_step = {g.get("step"): g.get("narration") or g.get("onscreen") or "" for g in r.segments}
                index = json.loads(r.p("checks/stills/index.json").read_text())
                texts = [by_step.get(index.get(p.name), "") for p in stills]
                intro = "Still version of a stepped deck: one image per step, the narration beneath."
            else:
                seg = {g["id"]: g for g in r.segments}
                texts = [seg.get(p.stem, {}).get("narration", "") for p in stills]
                intro = "Still version of a narrated animation: the end of each segment, the narration beneath."
            stills = stills[:MAX]
            for p in stills:
                shutil.copy(p, out / p.name)
            (out / "index.html").write_text(_steps_page(r, stills, texts[:MAX], intro))
    return static_check.check_bundle(out)
