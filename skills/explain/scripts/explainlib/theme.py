"""Theme tokens -> CSS variables (pages, decks), Plotly layout, Manim colours.

One tokens.json per report (copied from templates/theme/tokens.json by `x new`
and edited in the storyboard's token pass). Everything visual reads from it.
"""
import json
from pathlib import Path


def load(path) -> dict:
    return json.loads(Path(path).read_text())


def scale(t: dict, step: int) -> str:
    s = t["size"]
    return f'{s["base_px"] * s["ratio"] ** step:.1f}px'


def _vars(c: dict) -> str:
    return "".join(f"--x-{k}:{v};" for k, v in c.items())


def css(t: dict) -> str:
    """Variables plus a small base used by page.html and deck.html."""
    f, s = t["font"], t["size"]
    return (
        f":root{{{_vars(t['color'])}--x-font:{f['body']};--x-mono:{f['mono']};--x-measure:{s['measure_ch']}ch;"
        f"--x-caption-bg:rgba(0,0,0,.72);--x-caption-fg:#fff;--x-caption-font:600 22px/1.35 {f['body']};}}"
        f"@media (prefers-color-scheme: dark){{:root{{{_vars(t['dark'])}}}}}"
        f"html,body{{background:var(--x-bg);color:var(--x-fg);font-family:var(--x-font);}}"
        f"body{{font-size:{s['base_px']}px;line-height:1.55;}}"
        f"h1{{font-size:{scale(t, 3)};line-height:1.15;}} h2{{font-size:{scale(t, 2)};}} h3{{font-size:{scale(t, 1)};}}"
        f".x-muted{{color:var(--x-muted);}} .x-accent{{color:var(--x-accent);}}"
        # deck: reveal's base css + these, never a bundled reveal theme (they @import web fonts)
        f".reveal{{font-family:var(--x-font);color:var(--x-fg);font-size:32px;}}"
        f".reveal-viewport{{background:var(--x-bg);}}"
        f".reveal h1,.reveal h2,.reveal h3{{font-family:var(--x-font);color:var(--x-fg);margin:0 0 .5em;font-weight:700;}}"
        f".reveal h2{{font-size:1.6em;}} .reveal .slides section{{text-align:left;}}"
        f".reveal .controls,.reveal .progress{{color:var(--x-accent);}}"
        f".reveal img,.reveal svg{{max-width:100%;max-height:520px;}}"
    )


def plotly_layout(t: dict) -> dict:
    c = t["color"]
    return dict(
        font=dict(family=t["font"]["body"], color=c["fg"], size=t["size"]["base_px"] - 2),
        paper_bgcolor=c["bg"], plot_bgcolor=c["bg"],
        colorway=[c["accent"], c["accent2"], c["muted"]],
        xaxis=dict(gridcolor=c["rule"], zeroline=False), yaxis=dict(gridcolor=c["rule"], zeroline=False),
        margin=dict(l=60, r=24, t=64, b=56),
    )


def manim_colors(t: dict) -> dict:
    """Manim draws on the dark set: video is watched full screen."""
    return dict(t["dark"])
