"""Smoke: 3-slide narrated reveal deck, opened offline, stepped and photographed."""
import json, os, sys
from pathlib import Path
from explainlib import theme, tts

skill = Path(os.environ["EXPLAIN_SKILL"]); out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
vendor = Path(os.environ["REPORT_HOME"]) / "vendor/reveal.js-6.0.2/dist"
t = theme.load(skill / "templates/theme/tokens.json")

steps = {  # "h.v.f": narration
    "0.0.-1": "Two samples start far apart in the ontology.",
    "1.0.-1": "Each one is walked up, one parent at a time.",
    "1.0.0": "The first shared parent is where the paths meet.",
    "2.0.-1": "The steps taken become the distance between them.",
}
amap = {}
for k, text in steps.items():
    p, s = tts.clip(text, out / "audio", name="s" + k.replace(".", "_").replace("-", "m"))
    amap[k] = {"src": f"audio/{p.name}", "text": text}

slides = """
<section><h2>Two samples, one ontology</h2><p class="x-muted">Where do they meet?</p></section>
<section><h2>Walk up</h2><p>sample A: soil, then terrestrial biome</p>
  <p class="fragment">shared parent: <span class="x-accent">biome</span></p></section>
<section><h2>Distance = steps</h2><p>d(A, B) = 3</p></section>
"""
overlay = '<div id="x-start"><div><button>Start narrated deck</button><p>Captions are always on. P pauses.</p></div></div>'
html = (skill / "templates/deck.html").read_text()
for a, b in {"{{TITLE}}": "Smoke deck", "{{REVEAL_CSS}}": (vendor / "reveal.css").read_text(),
             "{{THEME_CSS}}": theme.css(t), "{{START_OVERLAY}}": overlay, "{{SLIDES}}": slides,
             "{{REVEAL_JS}}": (vendor / "reveal.js").read_text(), "{{AUDIO_MAP}}": json.dumps(amap),
             "{{NARRATE_JS}}": (skill / "templates/narrate.js").read_text()}.items():
    html = html.replace(a, b)
(out / "deck.html").write_text(html)
print("deck", len(html) // 1024, "KiB;", len(amap), "clips")

from playwright.sync_api import sync_playwright
bad, errors = [], []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=os.environ["REPORT_CHROME"],
                           args=["--autoplay-policy=no-user-gesture-required"])
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.on("request", lambda r: bad.append(r.url) if not r.url.startswith(("file:", "data:")) else None)
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto((out / "deck.html").as_uri()); pg.wait_for_timeout(500)
    pg.screenshot(path=str(out / "still-0-overlay.png"))
    pg.click("#x-start button")
    pg.evaluate("Reveal.configure({transition: 'none'})")  # stills mid-fade show ghosts
    pg.wait_for_timeout(400)
    n = 0
    for i in range(5):
        idx = pg.evaluate("JSON.stringify(Reveal.getIndices())")
        cap = pg.inner_text("#x-caption")
        src = pg.evaluate("document.querySelector('audio') ? 1 : 0")
        pg.screenshot(path=str(out / f"still-{i+1}.png")); n += 1
        print(f"step {i}: {idx}  caption={cap!r}")
        pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(400)
    pg.goto((out / "deck.html").as_uri() + "?print-pdf"); pg.wait_for_timeout(800)
    pg.pdf(path=str(out / "handout.pdf"), width="1280px", height="720px", print_background=True)
    b.close()
print("non-file requests:", bad or "none"); print("console errors:", errors or "none")
