"""Tier 4 scenes. One class per storyboard `scene`; one say(segment_id) block per segment.

Narration text comes from storyboard.yaml (never repeat it here, on screen or in code). The picture
carries the idea and the voice explains it; text only names what is drawn, in at most 4 words, and pops in
(Appear) when the voice reaches it. Tag the play that shows each event in the segment's storyboard `sync`
(sync="id"): it starts when the phrase is spoken; self.at(t, k[, "word"]) holds for finer cues. Place
objects on the 6x4 grid (A1 top left) so overlaps are caught; release() objects you remove so hold times
are checked. Draw on the dark token colours.
"""
from explainlib.anchors import ExplainScene   # first: quiets sox/phonemizer warnings
from explainlib import theme
from explainlib.motion import Appear, Retext
from manim import *

T = theme.load("tokens.json")
C = theme.manim_colors(T)
FONT = T["font"]["manim"]


class Scene1(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        thing = self.place(Circle(radius=1.2).set_stroke(C["fg"], width=4), "C2", "thing", span="2x2")
        name = Text("its name", font=FONT, font_size=28, color=C["fg"]).next_to(thing, DOWN, buff=0.25)
        with self.say("s1") as t:
            self.play(Create(thing), run_time=self.left(t, 0, cap=1.5), sync="thing")   # starts on its phrase
            if len(t.spans) > 1:
                self.at(t, 1)                                           # the label lands on the next sentence
            self.play(Appear(name), run_time=0.5)
