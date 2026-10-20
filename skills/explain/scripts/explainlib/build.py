"""Build a report folder into build/, by tier.

  0 note         src/note.md                      -> build/index.html (+ note.md)
  1 figures      src/figures.py, src/page.md      -> build/index.html + figure files
  2 slides       src/slides.html (+ narration)    -> build/deck.html, audio/, captions.vtt, transcript.md
  3 interactive  src/figures.py, src/page.md      -> build/page.html, fallback/<id>.svg
  4 animation    src/scene.py                     -> build/video.mp4, captions.vtt, transcript.md, player.html

src/figures.py is run with the report folder as cwd. For tier 1 it defines
make(out: Path, t: dict) and writes figure files into `out`; for tier 3 it
defines figures(t: dict) -> {id: plotly Figure} and page.md places them with
{{plot:id}} on a line of its own.
"""
import html
import json
import os
import re
import runpy
import shutil
import subprocess
from pathlib import Path

from . import captions, frames, theme
from .report import TEMPLATES


def fill(tpl: str, **kv) -> str:
    for k, v in kv.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    return tpl


def md_to_html(md: str) -> str:
    p = subprocess.run(["pandoc", "-f", "markdown-smart", "-t", "html", "--mathml", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return p.stdout


def page(r, body: str, wide=False) -> str:
    return fill((TEMPLATES / "page.html").read_text(), TITLE=html.escape(r.story.get("title", "")),
                THEME_CSS=theme.css(r.tokens), BODY=body, MAIN_CLASS=' class="x-wide"' if wide else "")


def fresh(d: Path) -> Path:
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    return d


def build(r, draft=False) -> Path:
    out = fresh(r.p("build"))
    return [t0, t1, t2, t3, t4][r.tier](r, out, draft)


def t0(r, out, draft):
    md = r.p("src/note.md").read_text()
    shutil.copy(r.p("src/note.md"), out / "note.md")
    (out / "index.html").write_text(page(r, md_to_html(md)))
    return out


def t1(r, out, draft):
    fig = r.p("src/figures.py")
    if fig.exists():
        ns = runpy.run_path(str(fig))
        ns["make"](out, r.tokens)
    (out / "index.html").write_text(page(r, md_to_html(r.p("src/page.md").read_text())))
    return out


def t2(r, out, draft):
    vendor = Path(os.environ["REPORT_HOME"]) / "vendor/reveal.js-6.0.2/dist"
    amap, cues, at = {}, [], 0.0
    voice = bool(r.story.get("voice"))
    from . import tts
    for g in r.segments:
        text = (g.get("narration") or "").strip()
        if not text:
            continue
        if voice:
            p, sec = tts.clip(text, out / "audio", name=g["id"])
            amap[g["step"]] = {"src": f"audio/{p.name}", "text": text}
        else:
            sec = len(text.split()) / 155 * 60
            amap[g["step"]] = {"src": "", "text": text}
        cues.append((at, at + sec, text)); at += sec + 0.7
    overlay = ('<div id="x-start"><div><button>Start</button>'
               '<p>Narrated. Captions stay on. P pauses; arrow keys step.</p></div></div>') if voice else ""
    for g in amap.values():  # unnarrated decks keep captions but play nothing
        if not g["src"]:
            g.pop("src")
    deck = fill((TEMPLATES / "deck.html").read_text(), TITLE=html.escape(r.story.get("title", "")),
                REVEAL_CSS=(vendor / "reveal.css").read_text(), THEME_CSS=theme.css(r.tokens),
                START_OVERLAY=overlay, SLIDES=r.p("src/slides.html").read_text(),
                REVEAL_JS=(vendor / "reveal.js").read_text(), AUDIO_MAP=json.dumps(amap),
                NARRATE_JS=(TEMPLATES / "narrate.js").read_text())
    (out / "deck.html").write_text(deck)
    src_assets = r.p("src/assets")
    if src_assets.exists():
        shutil.copytree(src_assets, out / "assets")
    (out / "captions.vtt").write_text(captions.vtt(cues))
    (out / "transcript.md").write_text(captions.transcript(r))
    return out


PLOT = re.compile(r"^\{\{plot:([\w-]+)\}\}\s*$", re.M)


def t3(r, out, draft):
    import plotly.graph_objects as go
    import plotly.io as pio
    figs = runpy.run_path(str(r.p("src/figures.py")))["figures"](r.tokens)
    md = r.p("src/page.md").read_text()
    first = [True]
    fb = out / "fallback"; fb.mkdir()
    os.environ.setdefault("BROWSER_PATH", os.environ.get("REPORT_CHROME", ""))

    def emb(m):
        fid = m.group(1)
        f = figs[fid]
        base = go.Layout(theme.plotly_layout(r.tokens))  # theme fills gaps; the author's layout wins
        base.update(f.layout.to_plotly_json())
        f.layout = base
        div = pio.to_html(f, include_plotlyjs=first[0], full_html=False, div_id=fid, auto_play=False,
                          config={"displaylogo": False, "responsive": True})
        first[0] = False
        pio.write_image(f, fb / f"{fid}.svg", format="svg", width=960, height=540)  # static/ needs it
        return f'\n<div class="x-plot" data-plot="{fid}">{div}</div>\n'

    md = PLOT.sub(lambda m: f"\n\n<!--PLOT:{m.group(1)}-->\n\n", md)
    body = md_to_html(md)
    body = re.sub(r"<!--PLOT:([\w-]+)-->", lambda m: emb(m), body)
    (out / "page.html").write_text(page(r, body, wide=True))
    return out


def scenes(r) -> list:
    seen = []
    for g in r.segments:
        if g.get("scene") and g["scene"] not in seen:
            seen.append(g["scene"])
    return seen


def t4(r, out, draft):
    q, sub = ("-ql", "480p15") if draft else ("-qh", "1080p60")
    media = r.p("checks/media")
    env = dict(os.environ, EXPLAIN_REPORT=str(r.dir))
    for f in r.p("checks").glob("scene-*.json"):
        f.unlink()
    parts, cues, at = [], [], 0.0
    for sc in scenes(r):
        subprocess.run(["manim", q, "--disable_caching", "--media_dir", str(media),
                        str(r.p("src/scene.py")), sc], check=True, env=env, cwd=r.dir)
        mp4 = media / "videos" / "scene" / sub / f"{sc}.mp4"
        parts.append(mp4)
        srt = mp4.with_suffix(".srt")
        if srt.exists():
            cues += captions.shift(captions.srt_cues(srt), at)
        at += frames.durations(mp4).get("video", 0.0)
    lst = out / "parts.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    frames.run("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", out / "video.mp4")
    lst.unlink()
    (out / "captions.vtt").write_text(captions.vtt(cues))
    (out / "transcript.md").write_text(captions.transcript(r))
    chapters = "".join(f"<li>{html.escape(s)}</li>" for s in scenes(r))
    body = (f'<h1>{html.escape(r.story.get("title", ""))}</h1>\n<p class="x-message">{html.escape(r.story.get("message", ""))}</p>\n'
            '<video controls preload="metadata" style="width:100%" src="video.mp4">'
            '<track kind="captions" src="captions.vtt" srclang="en" label="English" default></video>\n'
            f'<h2>Chapters</h2><ol>{chapters}</ol>\n<p><a href="transcript.md">Transcript</a></p>')
    (out / "player.html").write_text(page(r, body, wide=True))
    return out
