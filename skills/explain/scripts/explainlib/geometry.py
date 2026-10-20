"""Browser checks on a rendered page, measured in the DOM (VLMs judge overflow poorly).

    with browser() as b:
        pg = open_page(b, path, (1280, 800)); faults = page_faults(pg)
"""
import os
from contextlib import contextmanager
from pathlib import Path

from playwright.sync_api import sync_playwright

LOCAL = ("file:", "data:", "blob:", "about:")

_JS = r"""
(opts) => {
  const out = [], vw = innerWidth;
  const scope = opts.scope ? document.querySelector(opts.scope) : document.body;
  if (!scope) return ['scope ' + opts.scope + ' not found'];
  const box = opts.scope ? scope.getBoundingClientRect() : {left: 0, top: 0, right: vw, bottom: Infinity};
  const se = document.scrollingElement;
  if (!opts.scope && se.scrollWidth > se.clientWidth + 1) out.push('page scrolls sideways (' + se.scrollWidth + 'px wide in ' + se.clientWidth + ')');
  const vis = el => { const s = getComputedStyle(el); const r = el.getBoundingClientRect();
    return s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05 && r.width > 0 && r.height > 0; };
  // the box of an element's own text (not its block box: a full-width heading's box is mostly empty)
  const textBox = el => { let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity;
    for (const n of el.childNodes) { if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const g = document.createRange(); g.selectNodeContents(n);
      for (const q of g.getClientRects()) { l = Math.min(l, q.left); t = Math.min(t, q.top); r = Math.max(r, q.right); b = Math.max(b, q.bottom); } }
    return r > l ? {left: l, top: t, right: r, bottom: b, width: r - l, height: b - t} : el.getBoundingClientRect(); };
  const label = el => (el.id ? '#' + el.id : el.tagName.toLowerCase()) + ' "' + (el.textContent || '').trim().slice(0, 40) + '"';
  const texts = [];
  for (const el of scope.querySelectorAll('*')) {
    if (['STYLE','SCRIPT','svg','style','script','title','desc'].includes(el.tagName)) continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own || !vis(el)) continue;
    if (el.closest('#x-start, .controls, .progress, .slide-number, .modebar')) continue;
    const r = textBox(el);
    texts.push([el, r]);
    if (r.right > box.right + 1 || r.left < box.left - 1 || r.bottom > box.bottom + 1)
      out.push('outside ' + (opts.scope || 'viewport') + ': ' + label(el));
    if (!(el instanceof SVGElement)) {
      if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflowX !== 'visible')
        out.push('text clipped: ' + label(el));
      const px = parseFloat(getComputedStyle(el).fontSize) * (opts.zoom || 1);
      if (px < opts.minPx && !el.closest('figcaption, small, sup, sub, .x-small, #x-caption'))
        out.push('text under ' + opts.minPx + 'px (' + px.toFixed(1) + '): ' + label(el));
    }
  }
  for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
    const [a, ra] = texts[i], [b, rb] = texts[j];
    if (a.contains(b) || b.contains(a)) continue;
    const ix = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
    const iy = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (ix > 2 && iy > 2) out.push('text overlaps: ' + label(a) + ' / ' + label(b));
  }
  return out;
}
"""


@contextmanager
def browser():
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=os.environ["REPORT_CHROME"],
                               args=["--autoplay-policy=no-user-gesture-required"])
        try:
            yield b
        finally:
            b.close()


def open_page(b, path, size=(1280, 800), query=""):
    pg = b.new_page(viewport={"width": size[0], "height": size[1]})
    pg._x_bad, pg._x_err = [], []
    pg.on("request", lambda r: pg._x_bad.append(r.url) if not r.url.startswith(LOCAL) else None)
    pg.on("console", lambda m: pg._x_err.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: pg._x_err.append(str(e)))
    pg.goto(Path(path).resolve().as_uri() + query)
    pg.wait_for_timeout(600)
    return pg


def page_faults(pg, scope=None, min_px=14, zoom=1.0) -> list:
    out = pg.evaluate(_JS, {"scope": scope, "minPx": min_px, "zoom": zoom})
    return sorted(set(out))


_CAPTION_JS = r"""
(scope) => {
  const cap = document.getElementById('x-caption');
  if (!cap || !cap.textContent.trim()) return [];
  const c = cap.getBoundingClientRect(), out = [];
  const textBox = el => { let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity;
    for (const n of el.childNodes) { if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const g = document.createRange(); g.selectNodeContents(n);
      for (const q of g.getClientRects()) { l = Math.min(l, q.left); t = Math.min(t, q.top); r = Math.max(r, q.right); b = Math.max(b, q.bottom); } }
    return r > l ? {left: l, top: t, right: r, bottom: b, width: r - l} : el.getBoundingClientRect(); };
  for (const el of document.querySelector(scope).querySelectorAll('*')) {
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const s = getComputedStyle(el), r = textBox(el);
    if (!own || s.visibility === 'hidden' || +s.opacity < 0.05 || !r.width) continue;
    if (Math.min(r.right, c.right) - Math.max(r.left, c.left) > 2 && Math.min(r.bottom, c.bottom) - Math.max(r.top, c.top) > 2)
      out.push('caption covers "' + el.textContent.trim().slice(0, 40) + '"');
  }
  return out;
}
"""


def caption_faults(pg, scope) -> list:
    """Narration captions sit over the slide; nothing readable may be under them."""
    return pg.evaluate(_CAPTION_JS, scope)


def shrink_faults(pg, ratio=0.6) -> list:
    """Figures drawn below `ratio` of their natural width: their text shrinks with them."""
    return pg.evaluate("""(ratio) => [...document.images].filter(i => i.naturalWidth && i.clientWidth &&
        i.clientWidth < ratio * i.naturalWidth).map(i => 'figure ' + i.getAttribute('src') + ' drawn at ' +
        Math.round(100 * i.clientWidth / i.naturalWidth) + '% of its size: its text shrinks with it')""", ratio)


def load_faults(pg) -> list:
    return ([f"network request: {u}" for u in pg._x_bad] +
            [f"console error: {e[:160]}" for e in pg._x_err])


def axe_faults(pg) -> list:
    axe = Path(os.environ["REPORT_HOME"]) / "vendor/axe-core-4.14.0/axe.min.js"
    pg.add_script_tag(path=str(axe))
    res = pg.evaluate("async () => (await axe.run(document, {resultTypes: ['violations']})).violations"
                      ".map(v => ({id: v.id, impact: v.impact, n: v.nodes.length, help: v.help}))")
    return [f"axe {v['impact']}: {v['id']} ({v['n']}x) {v['help']}"
            for v in res if v["impact"] in ("serious", "critical")]
