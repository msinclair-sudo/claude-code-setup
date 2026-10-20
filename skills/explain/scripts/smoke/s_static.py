"""Smoke: matplotlib + graphviz + tex2svg figures in a static page; static_check; Playwright still."""
import os, subprocess, sys
from pathlib import Path
import matplotlib; matplotlib.use("svg")
import matplotlib.pyplot as plt, numpy as np, graphviz
from explainlib import theme, static_check

skill = Path(os.environ["EXPLAIN_SKILL"]); out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
t = theme.load(skill / "templates/theme/tokens.json"); c = t["color"]

plt.rcParams.update({"font.family": "Lato", "svg.fonttype": "path", "axes.edgecolor": c["muted"],
                     "axes.labelcolor": c["fg"], "xtick.color": c["muted"], "ytick.color": c["muted"],
                     "axes.spines.top": False, "axes.spines.right": False})
d = np.linspace(100, 10000, 80)
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.plot(d, 400 * (1 - np.exp(-d / 2500)), color=c["accent"], lw=2.5)
ax.set_xlabel("reads per sample"); ax.set_ylabel("taxa observed")
ax.set_title("Observed richness keeps rising with depth", loc="left", color=c["fg"])
fig.tight_layout(); fig.savefig(out / "fig1.svg", transparent=True); plt.close(fig)

g = graphviz.Digraph(format="svg", graph_attr=dict(rankdir="BT", bgcolor="transparent"),
                     node_attr=dict(shape="box", style="rounded", fontname="Lato", color=c["muted"], fontcolor=c["fg"]),
                     edge_attr=dict(color=c["muted"]))
g.edge("soil", "terrestrial biome"); g.edge("sediment", "aquatic biome")
g.edge("terrestrial biome", "biome"); g.edge("aquatic biome", "biome")
g.node("biome", color=c["accent"], fontcolor=c["accent"])
(out / "fig2.svg").write_bytes(g.pipe())

subprocess.run([str(skill / "scripts/tex2svg.sh"), r"d(a,b) = \min_{p \in P(a,b)} |p|", str(out / "eq1.svg"), c["fg"][1:]], check=True)

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>static smoke</title>
<style>{theme.css(t)} main{{max-width:{t['size']['measure_ch']}ch;margin:2em auto;padding:0 1em}} figure{{margin:2em 0}} img{{max-width:100%}}</style></head>
<body><main><h1>Static smoke</h1><p>Three figure sources in one publishable page.</p>
<figure><img src="fig1.svg" alt="Curve rising steeply then flattening near 400 taxa by 10,000 reads"><figcaption class="x-muted">matplotlib</figcaption></figure>
<figure><img src="fig2.svg" alt="Soil and sediment each walk up to biome"><figcaption class="x-muted">graphviz</figcaption></figure>
<figure><img src="eq1.svg" alt="d of a b equals the minimum path length"><figcaption class="x-muted">tex2svg</figcaption></figure>
</main></body></html>"""
(out / "index.html").write_text(html)
print("static_check:", static_check.check_bundle(out) or "publishable")
(out / "bad").mkdir(exist_ok=True)
(out / "bad/index.html").write_text('<html><head><link rel=stylesheet href="https://x"><style>@import "y";</style></head><body><script>1</script><img src="nope.png"><audio src="a.m4a"></audio></body></html>')
print("bad page faults:", len(static_check.check_bundle(out / "bad")))

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=os.environ["REPORT_CHROME"])
    pg = b.new_page(viewport={"width": 1280, "height": 900}); pg.goto((out / "index.html").as_uri()); pg.wait_for_timeout(400)
    pg.screenshot(path=str(out / "still.png"), full_page=True); b.close()
