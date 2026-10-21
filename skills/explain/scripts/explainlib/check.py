"""Every automated check for the report's tier -> checks/round-<n>.json.

Faults block delivery; warnings are for the fresh reader to weigh. External
checks (DOM geometry, renderer logs, axe, overlap asserts) are trusted over a
model looking at its own output.
"""
import ast
import json
import re

from . import frames, geometry, numbers, static_check
from .lint import lint


# Integer/DecimalNumber are left out: their literal is a counter's start value, not what the viewer reads.
DRAWN = {"Text", "MathTex", "Tex", "MarkupText", "Paragraph", "Title", "BulletedList"}


def _scene_strings(path) -> str:
    """What the video draws: literal arguments of Text, MathTex, Tex, ... in scene.py."""
    try:
        tree = ast.parse(path.read_text())
    except (OSError, SyntaxError):
        return ""
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, "id", getattr(n.func, "attr", None)) in DRAWN:
            out += [str(a.value) for a in n.args if isinstance(a, ast.Constant) and isinstance(a.value, (str, int, float))]
    return " ".join(out)


def run(r, rnd: int) -> dict:
    faults, warns = [], []
    for level, msg in lint(r):
        (faults if level == "error" else warns).append(f"lint: {msg}")
    t, b = r.tier, r.p("build")
    spoken = " ".join(g.get("narration") or "" for g in r.segments)
    shown = " ".join(g.get("onscreen") or "" for g in r.segments)

    if t in (0, 1):
        page = b / "index.html"
        faults += [f"static: {f}" for f in static_check.check_bundle(b)]
        src = {"page": numbers.html_text(page.read_text())}
        with geometry.browser() as br:
            for size in ((1280, 800), (390, 844)):
                pg = geometry.open_page(br, page, size)
                faults += [f"{size[0]}px: {f}" for f in geometry.page_faults(pg) + geometry.shrink_faults(pg)]
                if size[0] == 1280:
                    faults += geometry.load_faults(pg) + geometry.axe_faults(pg)
        for svg in b.glob("*.svg"):
            src[svg.name] = numbers.html_text(svg.read_text())
        warns += [f"numbers: {f}" for f in numbers.orphans(r, {k: v for k, v in src.items() if k != "page"})]
        faults += [f"numbers: {f}" for f in numbers.orphans(r, {"page": src["page"]})]

    elif t == 2:
        deck = b / "deck.html"
        from .stills import deck_steps
        with geometry.browser() as br:
            pg = geometry.open_page(br, deck, (1280, 720))
            if pg.query_selector("#x-start"):
                pg.evaluate("document.getElementById('x-start').remove()")
            n, planned, seen = 0, {g.get("step") for g in r.segments if g.get("narration")}, []
            for key in deck_steps(pg):
                n += 1; seen.append(key)
                zoom = pg.evaluate("Reveal.getScale()")
                faults += [f"step {key}: {f}" for f in
                           geometry.page_faults(pg, scope=".reveal .slides > section.present", min_px=20, zoom=zoom)]
                faults += [f"step {key}: {f}" for f in geometry.caption_faults(pg, ".reveal .slides > section.present")]
                if r.story.get("voice") and key not in planned:
                    faults.append(f"step {key} is not in the storyboard: it plays in silence "
                                  "(fragments meant to appear together need the same data-fragment-index)")
            faults += geometry.load_faults(pg) + geometry.axe_faults(pg)
            slides_text = numbers.html_text(r.p("src/slides.html").read_text())
        faults += [f"numbers: {f}" for f in numbers.orphans(r, {"slides": slides_text, "narration": spoken})]
        steps = {g.get("step") for g in r.segments}
        if r.story.get("voice"):
            for g in r.segments:
                if g.get("narration") and not (b / "audio" / f"{g['id']}.m4a").exists():
                    faults.append(f"audio: no clip for {g['id']}")
        if not (b / "captions.vtt").exists():
            faults.append("captions.vtt missing")
        if n < len(steps):
            warns.append(f"deck has {n} steps but the storyboard plans {len(steps)}")

    elif t == 3:
        page = b / "page.html"
        with geometry.browser() as br:
            pg = geometry.open_page(br, page, (1280, 900))
            before = pg.evaluate("[...document.querySelectorAll('.js-plotly-plot')].map(g => JSON.stringify(g.data.map(d => d.x)))")
            pg.wait_for_timeout(1500)
            after = pg.evaluate("[...document.querySelectorAll('.js-plotly-plot')].map(g => JSON.stringify(g.data.map(d => d.x)))")
            if before != after:
                faults.append("a plot changes by itself after load (auto_play left on?): the default view must hold still")
            controls = pg.evaluate("[...document.querySelectorAll('.js-plotly-plot')].reduce((n, g) => n + (g.layout.sliders || []).length + (g.layout.updatemenus || []).length, 0)")
            if controls > 2:
                faults.append(f"{controls} controls on the page; at most 2")
            faults += geometry.page_faults(pg) + geometry.load_faults(pg) + geometry.axe_faults(pg)
            pg2 = geometry.open_page(br, page, (390, 844))
            warns += [f"390px: {f}" for f in geometry.page_faults(pg2)]
            text = numbers.html_text(re.sub(r"<script.*?</script>", "", page.read_text(), flags=re.S))
        faults += [f"numbers: {f}" for f in numbers.orphans(r, {"page": text})]

    elif t == 4:
        v = b / "video.mp4"
        dur = frames.durations(v)
        if abs(dur.get("video", 0) - dur.get("audio", 0)) > 1.5:
            warns.append(f"video {dur.get('video', 0):.1f}s against audio {dur.get('audio', 0):.1f}s")
        cap = float(r.story.get("max_minutes") or 10)
        if dur.get("video", 0) > cap * 60 + 5:
            faults.append(f"video is {dur['video'] / 60:.1f} min; at most {cap:g} (chapters, or split it)")
        elif dur.get("video", 0) > 10 * 60 + 5:
            warns.append(f"video is {dur['video'] / 60:.1f} min, over 10: {r.story.get('length_reason')}")
        warns += motion_warnings(r.p("src/scene.py")) + text_warnings(r.p("src/scene.py"))
        for log in r.p("checks").glob("scene-*.json"):
            j = json.loads(log.read_text())
            faults += [f"{j['scene']}: {f}" for f in j["failures"]]
            warns += [f"{j['scene']}: {w}" for w in j["warnings"]]
        if not (b / "captions.vtt").exists() or (b / "captions.vtt").stat().st_size < 20:
            faults.append("captions.vtt missing or empty")
        faults += [f"numbers: {f}" for f in numbers.orphans(
            r, {"narration": spoken, "on screen": shown, "scene text": _scene_strings(r.p("src/scene.py"))})]

    res = {"round": rnd, "tier": t, "pass": not faults, "faults": faults, "warnings": warns}
    r.p("checks").mkdir(exist_ok=True)
    r.p(f"checks/round-{rnd}.json").write_text(json.dumps(res, indent=1))
    return res

FADES = ("FadeIn", "FadeOut")
MOVES = ("Create", "Uncreate", "Write", "Unwrite", "DrawBorderThenFill", "Transform", "ReplacementTransform",
         "TransformMatchingShapes", "TransformMatchingTex", "TransformFromCopy", "FadeTransform", "MoveToTarget",
         "GrowFromCenter", "GrowFromEdge", "GrowFromPoint", "GrowArrow", "SpinInFromNothing", "Indicate",
         "Circumscribe", "Flash", "FocusOn", "Wiggle", "ShowPassingFlash", "MoveAlongPath", "Rotate", "Restore",
         "Appear", "Retext")


def motion_warnings(scene_py) -> list:
    """Warn when fades are most of a scene file's animations (references/t4-animation.md, Motion)."""
    try:
        src = scene_py.read_text()
    except OSError:
        return []
    fades = sum(len(re.findall(rf"\b{n}\(", src)) for n in FADES)
    moves = sum(len(re.findall(rf"\b{n}\(", src)) for n in MOVES) + src.count(".animate.")
    total = fades + moves
    if total and fades / total > 0.4:
        return [f"motion: {fades} of {total} animations are fades; carry objects through with Transform, "
                f"draw with Create, bring text in with Appear, point with Indicate (references/t4-animation.md)"]
    return []


LABEL_WORDS = 4


def text_warnings(scene_py) -> list:
    """Text on screen names things; it does not write itself in or read out the narration (owner review of the
    fifth exemplar: the slow Write of every label "so distracting", and frames that read like slides)."""
    try:
        src = scene_py.read_text()
    except OSError:
        return []
    out = []
    n = len(re.findall(r"\bWrite\(", src))
    if n:
        out.append(f"text: {n} Write( calls draw text letter by letter; use Appear (explainlib.motion), Retext to change it")
    for m in re.finditer(r"""\b(?:label|Text)\(f?(["'])(.*?)\1""", src):
        text = re.sub(r"\{[^}]*\}", "0", m.group(2))
        nw = sum(1 for w in text.split() if re.search(r"[A-Za-z]", w))
        if nw > LABEL_WORDS:
            out.append(f"text: '{m.group(2)}' is {nw} words on screen; a label names a thing, the voice says the rest")
    return out
