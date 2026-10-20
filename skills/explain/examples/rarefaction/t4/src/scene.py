"""Rarefaction, tier 4: two chapters. Narration comes from storyboard.yaml; data from ../sim.py."""
from explainlib.anchors import ExplainScene   # first: quiets sox/phonemizer warnings
from explainlib import theme
from manim import *

import importlib.util
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location("sim", Path("..") / "sim.py")
sim = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(sim)

T = theme.load("tokens.json")
C = theme.manim_colors(T)
FONT = T["font"]["manim"]
D = sim.data()
ORDER = np.argsort(-D["p"])                     # most abundant taxon first: top-left of the grid


def first_seen(counts, seed):
    """Index of the read that first reveals each taxon, for one random read order."""
    reads = np.random.default_rng(seed).permutation(np.repeat(np.arange(len(counts)), counts))
    seen = np.full(len(counts), np.inf)
    _, idx = np.unique(reads, return_index=True)
    seen[np.unique(reads)] = idx
    return seen


def label(s, size=30, color=None):
    return Text(s, font=FONT, font_size=size, color=color or C["fg"])


class Reads(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        sizes = 0.05 + 0.06 * (np.log(D["p"][ORDER]) - np.log(D["p"]).min()) / np.ptp(np.log(D["p"]))
        dots = VGroup(*[Dot(radius=r, color=C["rule"]) for r in sizes]).arrange_in_grid(rows=15, cols=20, buff=0.16)
        grid = self.place(dots, "A1", "grid", span="4x4")
        cap = self.place(label("300 simulated taxa,\nmost of them rare", 28, C["muted"]), "E1", "caption", span="2x1")
        tag = self.place(label("simulated", 22, C["muted"]), "F4", "tag")
        with self.say("s1") as t:
            self.play(FadeIn(grid, lag_ratio=0.002), FadeIn(cap), FadeIn(tag), run_time=t.duration)

        def reveal(counts, depth, colour, seed, seg, cap_text, extra=None):
            seen = first_seen(counts, seed)[ORDER]
            prog = ValueTracker(0)
            reads = lambda: int(depth * prog.get_value() ** 2.5)       # slow start: most taxa appear early
            for i, d in enumerate(grid):
                d.add_updater(lambda m, i=i: m.set_color(colour if seen[i] < reads() else C["rule"]))
            slot = self.place(Rectangle(width=3.6, height=1.6, stroke_opacity=0), "E2", "counter", span="2x1")
            corner = slot.get_corner(UL)
            # Lato digits, rebuilt each frame and pinned at the slot's top left, so growing numbers never
            # push into their labels (Integer() lays out once, in Manim's serif)
            counter = always_redraw(lambda: VGroup(
                VGroup(label(f"{int((seen < reads()).sum())}", 60, colour), label("taxa", 30)).arrange(RIGHT, aligned_edge=DOWN, buff=0.25),
                VGroup(label(f"{reads():,}", 28, C["muted"]), label("reads", 26, C["muted"])).arrange(RIGHT, aligned_edge=DOWN, buff=0.2),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(corner, aligned_edge=UL))
            new_cap = self.place(label(cap_text, 28, colour), "E1", "caption2", span="2x1")
            with self.say(seg) as t:
                self.play(FadeOut(self._placed["caption"]["m"]), FadeIn(new_cap), FadeIn(counter), run_time=0.6)
                self.play(prog.animate.set_value(1), run_time=max(t.duration - 1.6, 2), rate_func=linear)
                self.play(FadeIn(extra), run_time=1) if extra is not None else self.wait(1)
            for d in grid:
                d.clear_updaters()
            counter.clear_updaters()
            return counter, new_cap

        counter, cap2 = reveal(D["deep"], sim.DEEP, C["accent"], 11, "s2", "deep: 20,000 reads")
        self.release("caption")
        self.play(FadeOut(counter), *[d.animate.set_color(C["rule"]) for d in grid], run_time=0.8)
        self.release("counter")
        self._placed["caption"] = self._placed.pop("caption2")
        gap = self.place(label(f"{D['obs_deep'] - D['obs_shallow']} fewer than\nthe deep sample", 26, C["fg"]), "E3", "gap", span="2x1")
        reveal(D["shallow"], sim.SHALLOW, C["accent2"], 12, "s3", "shallow: 2,000 reads", extra=gap)
        self.wait(0.5)


class Curve(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(3)
        depths = np.unique(np.r_[np.linspace(100, 2000, 14), np.linspace(2000, sim.DEEP, 18)].astype(int))
        ys = sim.curve(D["deep"], depths, rng, reps=10)
        ax = Axes(x_range=[0, 20000, 5000], y_range=[0, 300, 100], x_length=10.5, y_length=4.6,
                  axis_config=dict(color=C["muted"]), tips=False)
        ticks = VGroup(*[label(f"{x:,}", 22, C["muted"]).next_to(ax.c2p(x, 0), DOWN, buff=0.2) for x in (5000, 10000, 15000, 20000)],
                       *[label(str(y), 22, C["muted"]).next_to(ax.c2p(0, y), LEFT, buff=0.2) for y in (100, 200, 300)])
        xl = label("reads used", 26, C["muted"]).next_to(ax.x_axis, DOWN, buff=0.75)
        yl = label("taxa", 26, C["muted"]).next_to(ax.c2p(0, 300), RIGHT, buff=0.25)
        plot = self.place(VGroup(ax, ticks, xl, yl), "A2", "axes", span="6x3")
        title = self.place(label("taxa found, as reads are used", 32), "A1", "title", span="4x1")
        tag = self.place(label("simulated", 22, C["muted"]), "F1", "tag")
        curve = ax.plot_line_graph(depths, ys, line_color=C["accent"], add_vertex_dots=False, stroke_width=5)
        dot = Dot(ax.c2p(sim.SHALLOW, D["obs_shallow"]), radius=0.11, color=C["accent2"])
        with self.say("s4") as t:
            self.play(FadeIn(plot), FadeIn(title), FadeIn(tag), run_time=1)
            self.track(curve, "curve")
            self.play(Create(curve), run_time=max(t.duration * 0.6, 2), rate_func=linear)
            cl = label("deep sample", 26, C["accent"]).next_to(ax.c2p(16000, ys[-3]), DOWN, buff=0.25)
            self.track(dot, "dot")
            dl = label("shallow sample", 26, C["accent2"]).next_to(dot, DOWN + RIGHT, buff=0.2)
            self.play(FadeIn(cl), FadeIn(dot, scale=1.5), FadeIn(dl), run_time=max(t.duration * 0.4 - 1, 0.8))
        cut = DashedLine(ax.c2p(sim.SHALLOW, 0), ax.c2p(sim.SHALLOW, 300), color=C["fg"], dash_length=0.12)
        cut_l = label("2,000 reads", 22, C["fg"]).next_to(ax.c2p(sim.SHALLOW, 0), DOWN, buff=0.2)
        deep_pt = Dot(ax.c2p(sim.SHALLOW, D["rare_mean"]), radius=0.09, color=C["accent"])
        dv = label(f"deep at 2,000, average: {round(D['rare_mean'])}", 30, C["accent"]).next_to(deep_pt, RIGHT, buff=0.35).shift(DOWN * 0.45)
        sv = label(f"shallow: {D['obs_shallow']}", 30, C["accent2"]).next_to(dv, DOWN, aligned_edge=LEFT, buff=0.2)
        with self.say("s5") as t:
            self.play(Create(cut), FadeOut(dl), FadeIn(cut_l), run_time=1)
            self.track(dv, "deep_val"); self.track(sv, "shallow_val")
            self.play(FadeIn(deep_pt), FadeIn(dv), FadeIn(sv), run_time=1.2)
            self.play(Indicate(VGroup(dv, sv), color=C["fg"]), run_time=max(t.duration - 2.2, 1))
        self.wait(0.6)
