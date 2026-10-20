"""Stills of what a reader sees, for the fresh-reader review and the static fallback.

  tier 0/1   the page at 1280 and 390 px wide
  tier 2     every step of the deck (slide or fragment), transitions off
  tier 3     the default view, then each slider position of each plot
  tier 4     the last frame of every storyboard segment
Writes checks/stills/*.png and checks/contact-<n>.png (12 stills a sheet).
"""
import json
import shutil
from pathlib import Path

from . import frames, geometry


def stills(r) -> list:
    d = r.p("checks/stills")
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    shots = [_page, _page, _deck, _interactive, _video][r.tier](r, d)
    sheets = []
    for k in range(0, len(shots), 12):
        sheets.append(frames.contact(shots[k:k + 12], r.p(f"checks/contact-{k // 12 + 1}.png"), cols=3, width=420))
    return sheets


def _page(r, d):
    out = []
    with geometry.browser() as b:
        for w, h in ((1280, 800), (390, 844)):
            pg = geometry.open_page(b, r.p("build/index.html"), (w, h))
            p = d / f"page-{w}.png"; pg.screenshot(path=str(p), full_page=True); out.append(p)
    return out


def deck_steps(pg) -> list:
    """Step through a reveal deck from the start; yields after each step. Returns step keys."""
    pg.evaluate("Reveal.configure({transition: 'none', backgroundTransition: 'none'}); Reveal.slide(0, 0, -1)")
    keys = []
    for _ in range(400):
        i = pg.evaluate("Reveal.getIndices()")
        key = f"{i['h']}.{i.get('v') or 0}.{i['f'] if i.get('f') is not None else -1}"
        if key in keys:
            break
        keys.append(key)
        yield key
        if pg.evaluate("Reveal.isLastSlide() && !Reveal.availableFragments().next"):
            break
        pg.evaluate("Reveal.next()"); pg.wait_for_timeout(120)


def _deck(r, d):
    out, index = [], {}
    with geometry.browser() as b:
        pg = geometry.open_page(b, r.p("build/deck.html"), (1280, 720))
        if pg.query_selector("#x-start"):
            pg.evaluate("document.getElementById('x-start').remove()")
        for n, key in enumerate(deck_steps(pg)):
            p = d / f"step-{n + 1:02d}.png"
            pg.screenshot(path=str(p)); out.append(p); index[p.name] = key
    (d / "index.json").write_text(json.dumps(index))
    return out


SLIDERS = """() => [...document.querySelectorAll('.js-plotly-plot')].map(g => ({id: g.id,
  steps: ((g.layout.sliders || [])[0] || {steps: []}).steps.map(s => s.args[0][0])}))"""


def _interactive(r, d):
    out = []
    with geometry.browser() as b:
        pg = geometry.open_page(b, r.p("build/page.html"), (1280, 900))
        pg.wait_for_timeout(800)
        p = d / "page-default.png"; pg.screenshot(path=str(p), full_page=True); out.append(p)
        for plot in pg.evaluate(SLIDERS):
            el = pg.query_selector(f"#{plot['id']}")
            for name in plot["steps"]:
                pg.evaluate("([id, n]) => Plotly.animate(id, [n], {frame: {duration: 0}, transition: {duration: 0}, mode: 'immediate'})",
                            [plot["id"], name])
                pg.wait_for_timeout(150)
                p = d / f"{plot['id']}-{name}.png"; el.screenshot(path=str(p)); out.append(p)
    return out


def _video(r, d):
    out, at = [], 0.0
    v = r.p("build/video.mp4")
    for sc in dict.fromkeys(g["scene"] for g in r.segments if g.get("scene")):
        log = r.p(f"checks/scene-{sc}.json")
        segs = json.loads(log.read_text())["segments"] if log.exists() else []
        for s in segs:
            p = d / f"{s['id']}.png"
            frames.grab(v, at + s["end"] - 0.15, p); out.append(p)
        found = list(r.p("checks/media/videos/scene").glob(f"*/{sc}.mp4"))   # draft and final renders sit side by side
        media = max(found, key=lambda f: f.stat().st_mtime) if found else None
        at += frames.durations(media)["video"] if media else 0
    return out
