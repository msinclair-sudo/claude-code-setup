"""Text motion for tier 4: text appears, and changes, in about 0.3 s, whatever the play's run_time.

    from explainlib.motion import Appear, Retext
    self.play(Appear(label), GrowFromEdge(bar, DOWN), run_time=2)   # the label is in by 0.3 s; the bar grows for 2 s
    self.play(Retext(title, Text("new title")), run_time=0.5)       # crossfade in place; `title` stays the object

Why: the owner's review of the fifth exemplar: the slow left-to-right Write of every label was "so
distracting", and the frames read out the narration like slides. Text on screen names things; it pops in
when the voice reaches it and then holds still, so the eye goes back to the picture. Write is for nothing
(`x check` warns on it); a formula built up term by term is a picture, so draw it with Create or
TransformMatchingTex instead.
"""
from manim import Animation, FadeIn, FadeOut

QUICK = 0.3


class _Quick:
    """Squeeze the animation into its first `quick` seconds, however long the play runs."""
    quick = QUICK

    def interpolate(self, alpha: float) -> None:
        super().interpolate(min(1.0, alpha * max(self.run_time, 1e-6) / self.quick))


class Appear(_Quick, FadeIn):
    """A label or number comes in: a 0.3 s fade, at the start of the play it is in."""


class Vanish(_Quick, FadeOut):
    """A label leaves: a 0.3 s fade."""


class Retext(Animation):
    """Change a label's text in place: a 0.3 s crossfade. The old object stays in the scene and becomes
    the new text, so code that refers to it later still works (Transform would morph letter shapes)."""

    def __init__(self, old, new, quick: float = QUICK, **kwargs):
        self.new, self.quick = new, quick
        super().__init__(old, **kwargs)

    def begin(self) -> None:
        self.old = self.mobject.copy()
        super().begin()

    def interpolate_mobject(self, alpha: float) -> None:
        k = min(1.0, alpha * max(self.run_time, 1e-6) / self.quick)
        src, w = (self.old, 1 - 2 * k) if k < 0.5 else (self.new, 2 * k - 1)
        self.mobject.become(src.copy().set_opacity(max(w, 0.0)))
