from explainlib.kokoro_service import KokoroService  # first: quiets sox/phonemizer warnings
from manim import *
from manim_voiceover import VoiceoverScene


class Smoke(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService())
        c = Circle(color=BLUE)
        with self.voiceover(text="A circle appears, drawn in one stroke.") as t:
            self.play(Create(c), run_time=t.duration)
        eq = MathTex(r"d(a,b) = \min_{p} \, |p|").next_to(c, DOWN)
        lab = Text("shared parent", font_size=32).next_to(c, UP)
        with self.voiceover(text="It becomes a square, and the distance formula settles underneath.") as t:
            self.play(Transform(c, Square(color=YELLOW)), Write(eq), FadeIn(lab), run_time=t.duration)
        self.wait(0.5)
