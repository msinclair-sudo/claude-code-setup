"""Each check catches its fault. Run: x run python -m unittest discover -s scripts/tests -v

Needs the report env (browser, ffmpeg, manim). Fixtures are built in a temp dir.
"""
import inspect
import json
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

from explainlib import check, lint, numbers, report, static_check

SKILL = Path(__file__).resolve().parents[2]
X = SKILL / "scripts/x"


def scaffold(tmp, tier, **story):
    d = Path(tmp) / f"t{tier}"
    subprocess.run([str(X), "new", str(d), "--tier", str(tier), "--title", "fixture"], check=True, capture_output=True)
    sb = d / "storyboard.yaml"
    import yaml
    s = yaml.safe_load(sb.read_text())
    s.update({"tier_reason": "fixture", "message": "fixture message"}, **story)
    sb.write_text(yaml.safe_dump(s, sort_keys=False))
    (d / "claims.yaml").write_text(yaml.safe_dump({"claims": [
        {"id": "c1", "text": "the ledger holds 400 taxa", "source": "fixture", "kind": "illustrative", "value": 400}]}))
    return d


class Lint(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def errors(self, d):
        return [m for l, m in lint.lint(report.load(d)) if l == "error"]

    def test_long_narration_and_onscreen(self):
        d = scaffold(self.tmp, 2, segments=[{"id": "s1", "step": "0.0.-1", "visual": "v", "claims": ["c1"],
                                             "onscreen": " ".join(["w"] * 17), "narration": " ".join(["w"] * 36)}])
        e = " ".join(self.errors(d))
        self.assertIn("on-screen text is 17 words", e)
        self.assertIn("narration is 36 words", e)

    def warnings(self, d):
        return [m for l, m in lint.lint(report.load(d)) if l == "warn"]

    def test_pacing_language_and_distil(self):
        long = "This sentence keeps going on and on with clause after clause until it is far longer than any listener can hold in mind."
        segs = [{"id": f"s{i}", "role": "setting" if i == 1 else "mechanism", "scene": "Ch", "visual": "v",
                 "onscreen": "the true counts per taxon", "narration": long if i == 1 else "These are the true counts per taxon here.",
                 "verify": {"inside_frame": "all"}} for i in (1, 2, 3)]
        d = scaffold(self.tmp, 4, delivery="presented", segments=segs)
        w = " ".join(self.warnings(d))
        self.assertIn("-word sentence", w)
        self.assertIn("word for word", w)
        self.assertIn("no distil line", w)
        segs[2]["role"] = "distil"
        d2 = scaffold(self.tmp + "/b", 4, delivery="presented", segments=segs)
        self.assertNotIn("no distil line", " ".join(self.warnings(d2)))

    def test_pause_rule(self):
        from explainlib.tts import PACING, pause_for
        self.assertEqual(pause_for({"pause_after": 1.0}, PACING, chapter_end=True), 1.0)
        self.assertEqual(pause_for({}, PACING, chapter_end=True), PACING["chapter"])
        self.assertEqual(pause_for({"role": "distil"}, PACING, chapter_end=False), PACING["distil"])
        self.assertEqual(pause_for({"role": "mechanism"}, PACING, chapter_end=False), PACING["segment"])

    def test_motion_mostly_fades(self):
        f = Path(self.tmp) / "scene.py"
        f.write_text("self.play(FadeIn(a), FadeIn(b), FadeOut(c))\nself.play(Create(d))\n")
        self.assertTrue(check.motion_warnings(f))
        f.write_text("self.play(Transform(a, b), Create(d), Write(t))\nself.play(FadeOut(c))\n")
        self.assertFalse(check.motion_warnings(f))

    def test_text_writes_and_sentences(self):
        f = Path(self.tmp) / "scene.py"
        f.write_text('self.play(Write(label("a cell can hold several genome copies")))\n')
        w = " ".join(check.text_warnings(f))
        self.assertIn("Write(", w)
        self.assertIn("7 words on screen", w)
        f.write_text('self.play(Appear(label("taxon 1: 46%")), Retext(t, label("cycle 35")))\n')
        self.assertFalse(check.text_warnings(f))

    def test_tier4_must_be_presented(self):
        d = scaffold(self.tmp, 4, delivery="read")
        self.assertTrue(any("system-paced" in m for m in self.errors(d)))

    def test_tier3_controls_and_default_view(self):
        d = scaffold(self.tmp, 3, controls=3)
        e = " ".join(self.errors(d))
        self.assertIn("at most 2", e)
        self.assertIn("default_view", e)

    def test_unknown_claim(self):
        d = scaffold(self.tmp, 2, segments=[{"id": "s1", "step": "0.0.-1", "visual": "v", "claims": ["c9"]}])
        self.assertTrue(any("c9" in m for m in self.errors(d)))


class Numbers(unittest.TestCase):
    def test_ledger(self):
        tmp = tempfile.mkdtemp()
        try:
            r = report.load(scaffold(tmp, 0))
            self.assertEqual(numbers.orphans(r, {"t": "we saw 400 taxa"}), [])
            self.assertEqual(len(numbers.orphans(r, {"t": "we saw 410 taxa and 2.5%"})), 2)
            self.assertEqual(numbers.orphans(r, {"t": "16S and D1 are names"}), [])
        finally:
            shutil.rmtree(tmp)


class Page(unittest.TestCase):
    """A tier 1 page with one of each layout fault."""
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        d = scaffold(cls.tmp, 1)
        (d / "src/page.md").write_text(textwrap.dedent("""\
            # Faults

            <p>We counted 999 things.</p>

            <p style="white-space:nowrap">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</p>

            <p style="font-size:9px">tiny text that nobody can read</p>

            <div style="position:relative;height:40px"><span style="position:absolute;left:0;top:0">first label</span><span style="position:absolute;left:10px;top:4px">second label</span></div>

            <figure><img src="fig1.svg" alt="figure"></figure>
            """))
        subprocess.run([str(X), "build", str(d)], check=True, capture_output=True)
        cls.res = check.run(report.load(d), 1)
        cls.faults = " | ".join(cls.res["faults"])

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_fails(self):
        self.assertFalse(self.res["pass"])

    def test_overflow(self):
        self.assertIn("scrolls sideways", self.faults)

    def test_small_text(self):
        self.assertIn("text under 14px", self.faults)

    def test_overlap(self):
        self.assertIn("text overlaps", self.faults)

    def test_orphan_number(self):
        self.assertIn("999 is not in claims.yaml", self.faults)


class Deck(unittest.TestCase):
    """A narrated deck whose text runs under the caption, with an unplanned fragment step."""
    def test_caption_and_silent_step(self):
        tmp = tempfile.mkdtemp()
        try:
            d = scaffold(tmp, 2, voice=False, segments=[
                {"id": "s1", "step": "0.0.-1", "visual": "v", "narration": "A caption on this step."}])
            (d / "src/slides.html").write_text(
                '<section><h2>Title</h2><p style="position:absolute;bottom:0;left:30%;margin:0">'
                'text under the caption bar</p><p class="fragment">an unplanned step</p></section>')
            import yaml
            sb = d / "storyboard.yaml"; s = yaml.safe_load(sb.read_text()); s["voice"] = True
            sb.write_text(yaml.safe_dump(s, sort_keys=False))
            subprocess.run([str(X), "build", str(d)], check=True, capture_output=True)
            f = " | ".join(check.run(report.load(d), 1)["faults"])
            self.assertIn("caption covers", f)
            self.assertIn("step 0.0.0 is not in the storyboard", f)
        finally:
            shutil.rmtree(tmp)


class Static(unittest.TestCase):
    def test_refuses_script_media_and_imports(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            (tmp / "index.html").write_text('<style>@import "x.css";</style><script>1</script><audio src="a.m4a"></audio>'
                                            '<img src="missing.png"><a href="javascript:1">x</a>')
            f = " ".join(static_check.check_bundle(tmp))
            for want in ("@import", "no script", "no audio", "missing.png", "script URLs"):
                self.assertIn(want, f)
        finally:
            shutil.rmtree(tmp)

    def test_matches_harness(self):
        """Drift: the vendored check is the harness's, word for word (only inside the setup repo)."""
        cli = SKILL.parents[1] / "harness/bin/harness"
        if not cli.exists():
            self.skipTest("harness CLI not beside the skill (installed copy)")
        src = cli.read_text()
        start = src.index("_REPORT_BAD_TAGS = {")
        end = src.index("    return faults\n", start) + len("    return faults\n")
        mine = Path(static_check.__file__).read_text()
        self.assertIn(src[start:end], mine, "report_html_check changed in the harness: re-vendor it")


class Animation(unittest.TestCase):
    """Overlap, frame and hold failures recorded by ExplainScene."""
    def test_verify_failures(self):
        tmp = tempfile.mkdtemp()
        try:
            d = scaffold(tmp, 4, delivery="presented", segments=[
                {"id": "s1", "scene": "Scene1", "visual": "two boxes", "narration": "Two boxes appear.",
                 "verify": {"no_overlap": "all", "hold_min_s": 5}},
                {"id": "s2", "scene": "Scene1", "visual": "one leaves", "narration": "One goes."}])
            (d / "src/scene.py").write_text(textwrap.dedent("""\
                from explainlib.anchors import ExplainScene
                from manim import *

                class Scene1(ExplainScene):
                    def construct(self):
                        a = self.place(Square(), "B2", "a")
                        b = self.place(Circle(), "C2", "b")
                        c = self.place(Square(), "B2", "c")           # same cell as a: overlap
                        with self.say("s1") as t:
                            self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=t.duration)
                            self.release("b")                         # shown < 5 s
                        far = Square().shift(RIGHT * 20)              # off frame
                        with self.say("s2") as t:
                            self.add(far); self.wait(t.duration)
                """))
            subprocess.run([str(X), "build", str(d), "--draft"], check=True, capture_output=True)
            log = json.loads((d / "checks/scene-Scene1.json").read_text())
            f = " ".join(log["failures"])
            self.assertIn("leaves the frame", f)
            self.assertIn("a overlaps c", f)
            self.assertIn("b shown", f)
        finally:
            shutil.rmtree(tmp)

    def test_sentence_cues(self):
        """Sentence spans are recorded with the set pause between them; a late cue is a fault; no cue, a warning."""
        tmp = tempfile.mkdtemp()
        try:
            d = scaffold(tmp, 4, delivery="presented", segments=[
                {"id": "s1", "scene": "Scene1", "visual": "a box", "narration": "A box appears. Then it turns."},
                {"id": "s2", "scene": "Scene1", "visual": "it stays", "narration": "It stays. It waits."}])
            (d / "src/scene.py").write_text(textwrap.dedent("""\
                from explainlib.anchors import ExplainScene
                from manim import *

                class Scene1(ExplainScene):
                    def construct(self):
                        a = Square()
                        with self.say("s1") as t:
                            self.play(FadeIn(a), run_time=t.spans[1][0] + 1.5)   # still busy when sentence 2 starts
                            self.at(t, 1)
                            self.play(Rotate(a), run_time=0.5)
                        with self.say("s2") as t:
                            self.wait(t.duration)
                """))
            subprocess.run([str(X), "build", str(d), "--draft"], check=True, capture_output=True)
            log = json.loads((d / "checks/scene-Scene1.json").read_text())
            self.assertIn("sentence 2 is spoken", " ".join(log["failures"]))
            self.assertIn("s2: 2 sentences and no at() cue", " ".join(log["warnings"]))
            (a0, a1), (b0, b1) = log["segments"][0]["sentences"]
            self.assertAlmostEqual(b0 - a1, 0.7, delta=0.05)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
