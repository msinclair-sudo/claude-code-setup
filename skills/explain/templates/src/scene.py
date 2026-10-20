"""Tier 4 scenes. One class per storyboard `scene`; one say(segment_id) block per segment.

Narration text comes from storyboard.yaml (never repeat it here). Place objects
on the 6x4 grid (A1 top left) so overlaps are caught; release() objects you
remove so hold times are checked. Draw on the dark token colours.
"""
from explainlib.anchors import ExplainScene   # first: quiets sox/phonemizer warnings
from explainlib import theme
from manim import *

T = theme.load("tokens.json")
C = theme.manim_colors(T)
FONT = T["font"]["manim"]


class Scene1(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        title = self.place(Text("Title that states the point", font=FONT, color=C["fg"]), "A1", "title", span="6x1")
        with self.say("s1") as t:
            self.play(FadeIn(title), run_time=t.duration)
