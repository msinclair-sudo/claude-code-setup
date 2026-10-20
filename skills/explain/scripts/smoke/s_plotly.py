"""Smoke: Plotly slider + HOPs page, offline; kaleido SVG; Playwright check."""
import os, sys, time
from pathlib import Path
import numpy as np, plotly.graph_objects as go, plotly.io as pio
from explainlib import theme

skill = Path(os.environ["EXPLAIN_SKILL"]); out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
t = theme.load(skill / "templates/theme/tokens.json"); L = theme.plotly_layout(t)
rng = np.random.default_rng(1)

# 1. rarefaction-like curve with a depth slider (frames)
depth = np.linspace(100, 10000, 60); rich = 400 * (1 - np.exp(-depth / 2500))
f1 = go.Figure(go.Scatter(x=depth, y=rich, mode="lines", line=dict(width=3)))
marks = [1000, 3000, 6000, 9000]
f1.add_trace(go.Scatter(x=[marks[0]], y=[400 * (1 - np.exp(-marks[0] / 2500))], mode="markers", marker=dict(size=14)))
f1.frames = [go.Frame(data=[go.Scatter(x=[m], y=[400 * (1 - np.exp(-m / 2500))])], traces=[1], name=str(m)) for m in marks]
f1.update_layout(**L, title="Observed richness keeps rising with depth", showlegend=False,
                 xaxis_title="reads per sample", yaxis_title="taxa observed",
                 sliders=[dict(active=0, pad=dict(t=60), currentvalue=dict(prefix="depth: "), steps=[
                     dict(label=str(m), method="animate", args=[[str(m)], dict(mode="immediate", frame=dict(duration=0))]) for m in marks])])
# 2. HOPs: one draw per frame
draws = rng.normal(5, 1.2, size=(20, 3))
f2 = go.Figure(go.Bar(x=["A", "B", "C"], y=draws[0]))
f2.frames = [go.Frame(data=[go.Bar(y=d)], name=str(i)) for i, d in enumerate(draws)]
f2.update_layout(**L, title="Each frame is one plausible outcome", yaxis_range=[0, 10],
                 updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate",
                     args=[None, dict(frame=dict(duration=400, redraw=True), fromcurrent=True, mode="immediate")])])])

html = ("<!doctype html><html lang=en><head><meta charset=utf-8><title>plotly smoke</title>"
        f"<style>{theme.css(t)} main{{max-width:960px;margin:2em auto;}}</style></head><body><main>"
        "<h1>Plotly smoke</h1>"
        + pio.to_html(f1, include_plotlyjs=True, full_html=False, div_id="f1", auto_play=False)
        + pio.to_html(f2, include_plotlyjs=False, full_html=False, div_id="f2", auto_play=False)
        + "</main></body></html>")
(out / "page.html").write_text(html); print("page", len(html) // 1024, "KiB")

t0 = time.time()
os.environ.setdefault("BROWSER_PATH", os.environ["REPORT_CHROME"])
pio.write_image(f1, out / "f1.svg", format="svg", width=900, height=500)
print(f"kaleido svg {time.time()-t0:.1f}s", (out / "f1.svg").stat().st_size, "bytes")

from playwright.sync_api import sync_playwright
bad, err = [], []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=os.environ["REPORT_CHROME"])
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    pg.on("request", lambda r: bad.append(r.url) if not r.url.startswith(("file:", "data:", "blob:")) else None)
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.goto((out / "page.html").as_uri()); pg.wait_for_timeout(1200)
    pg.screenshot(path=str(out / "still.png"), full_page=True)
    print("plots rendered:", pg.evaluate("document.querySelectorAll('.js-plotly-plot').length"))
    b.close()
print("non-file requests:", bad or "none"); print("errors:", err or "none")
