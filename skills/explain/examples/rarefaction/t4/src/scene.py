"""Rarefaction in a metabarcoding experiment, tier 4: seven chapters, from soil to a rarefied count table.

Narration comes from storyboard.yaml (say("sN")); every count from ../pipeline.py (simulated, seed 7);
literature facts from claims.yaml (MB-01, MB-02 reviews). Drawings of soil, cells, genomes, PCR, the
sequencer and the bioinformatics steps are schematic; the charts are the simulation's numbers. Colours mean
taxa only (the six most abundant; the rest grey); samples are white and told apart by label and index pattern.

Motion (references/t4-animation.md): things that become other things are transformed, not swapped; pictures
are drawn up while the voice explains them; the camera moves in to look closer; fades are kept for exits.
Each chapter opens on its title and ends on a distil line over a still picture.
"""
from explainlib.anchors import ExplainScene   # first: quiets sox/phonemizer warnings
from explainlib import theme
from manim import *

import importlib.util
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location("pipeline", Path("..") / "pipeline.py")
P = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P)

T = theme.load("tokens.json")
C = theme.manim_colors(T)
FONT = T["font"]["manim"]
MONO = "DejaVu Sans Mono"
D = P.data()
N = P.N_TAXA
HUES = [C["accent"], C["accent2"], "#7BC47F", "#B79CE8", "#E8CF6A", "#E88FA8"]
COL = [HUES[i] if i < len(HUES) else C["muted"] for i in range(N)]
SAMPLE = C["fg"]              # samples are never a taxon colour
SOIL = "#7A5C3E"
SKETCH_DEPTH = [1.0, 0.62, 0.012]   # schematic reads per sample, A to C (narration: nearly 100-fold)
CHART = dict(w=8.6, h=3.0, ymax=0.55)


def label(s, size=28, color=None, weight=NORMAL, font=None):
    return Text(s, font=font or FONT, font_size=size, color=color or C["fg"], weight=weight)


def pct(x):
    """A share as spoken in the narration: whole percent from 10%, one decimal below."""
    return f"{x:.0%}" if x >= 0.095 else f"{x:.1%}"


def bars(shares, w=5.6, h=3.0, ymax=0.5):
    """80 bars on a baseline; height = share / ymax of h; bar i is always taxon i+1."""
    bw = w / N
    g = VGroup()
    for i, s in enumerate(shares):
        r = Rectangle(width=bw * 0.8, height=max(h * s / ymax, 0.001), stroke_width=0, fill_color=COL[i], fill_opacity=1)
        r.move_to([-w / 2 + bw * (i + 0.5), 0, 0], aligned_edge=DOWN)
        g.add(r)
    return g


def chart(shares, title, w=5.6, h=3.0, ymax=0.5, xlab="taxa, most abundant first"):
    """[grid, baseline, bars, title, x label]."""
    b = bars(shares, w, h, ymax)
    base = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=C["muted"], stroke_width=2)
    grid = VGroup()
    for v in (0.25, 0.5):
        y = h * v / ymax
        grid.add(DashedLine([-w / 2, y, 0], [w / 2, y, 0], color=C["rule"], stroke_width=1.5, dash_length=0.08),
                 label(f"{int(v * 100)}%", 20, C["muted"]).next_to([-w / 2, y, 0], LEFT, buff=0.12))
    ttl = label(title, 24).next_to([0, h + 0.15, 0], UP, buff=0.1)
    xl = label(xlab, 20, C["muted"]).next_to(base, DOWN, buff=0.15)
    return VGroup(grid, base, b, ttl, xl)


def draw_chart(ch, run_time=2.0):
    """Build a chart up: axes drawn, bars grown, words written."""
    return AnimationGroup(Create(ch[0]), Create(ch[1]), Write(ch[3]), Write(ch[4]),
                          LaggedStart(*[GrowFromEdge(r, DOWN) for r in ch[2]], lag_ratio=0.02), run_time=run_time)


def strip(found, cols=40, size=0.13, colour=None):
    """Detection strip: one square per taxon, filled if found, a dim outline if never drawn."""
    g = VGroup()
    for i, f in enumerate(found):
        c = COL[i] if colour is None else colour
        sq = Square(side_length=size, stroke_width=1.5, stroke_color=c if f else C["rule"], fill_color=c,
                    fill_opacity=1 if f else 0)
        sq.move_to([(i % cols) * size * 1.35, -(i // cols) * size * 1.35, 0])
        g.add(sq)
    return g


def cell(i, rng, scale=1.0):
    """A schematic bacterium: rods for odd taxa, cocci for even ones."""
    if i % 2:
        m = RoundedRectangle(width=0.34, height=0.13, corner_radius=0.065).rotate(rng.uniform(0, PI))
    else:
        m = Circle(radius=0.075)
    return m.scale(scale).set_stroke(width=0).set_fill(COL[i], opacity=0.95)


def dna(colour, length=0.7, waves=3, amp=0.07):
    """A short wavy strand of DNA."""
    return ParametricFunction(lambda t: np.array([t, amp * np.sin(t / length * waves * TAU), 0]),
                              t_range=[-length / 2, length / 2], color=colour, stroke_width=5)


def index_tag(k, unit=0.1):
    """Sample k's index: k+1 small white squares (a pattern, not a colour)."""
    return VGroup(*[Square(side_length=unit, stroke_width=0, fill_color=SAMPLE, fill_opacity=1)
                    for _ in range(k + 1)]).arrange(RIGHT, buff=unit * 0.4)


def tagged(colour, k, length=0.55):
    """An amplicon carrying sample k's index on its left end."""
    s = Line(LEFT * length / 2, RIGHT * length / 2, stroke_width=7, color=colour)
    t = index_tag(k).next_to(s, LEFT, buff=0.05)
    return VGroup(t, s)


def genome_ring(n, colour, centre, r=1.35):
    """A circular genome with n copies of the 16S gene drawn as arcs."""
    c = Circle(radius=r).set_stroke(C["fg"], width=4).move_to(centre)
    arcs = VGroup(*[Arc(radius=r, start_angle=k * TAU / n + 0.2, angle=0.26, stroke_width=14, color=colour)
                    .shift(centre) for k in range(n)])
    return VGroup(c, arcs)


def soil_icon():
    """The droplet from chapter 1, small, for the top-left corner when the story returns to the soil."""
    rng = np.random.default_rng(5)
    drop = Circle(radius=1.9).set_stroke(SOIL, width=3).set_fill(SOIL, opacity=0.45)
    grains = VGroup(*[RegularPolygon(n=int(rng.integers(5, 8)), radius=rng.uniform(0.04, 0.11))
                      .set_stroke(width=0).set_fill("#A58A6C", opacity=0.7)
                      .move_to(drop.point_at_angle(rng.uniform(0, TAU)) * rng.uniform(0, 0.9)) for _ in range(60)])
    return VGroup(drop, grains).scale(0.3).to_corner(UR, buff=0.3)


class Chaptered(ExplainScene):
    """An ExplainScene that opens on its chapter title (silent) and helps with corner tags."""
    NUMBER, TITLE = 0, ""

    def chapter(self):
        t = VGroup(label(f"{self.NUMBER}", 64, C["muted"]), label(self.TITLE, 48)).arrange(RIGHT, buff=0.5)
        self.play(Write(t), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(t, shift=UP * 0.3), run_time=0.6)

    def tags(self, text):
        a = self.tag(text)
        return [a] if a else []

    def heading(self, text):
        """The step's name, small, top left in the margin above the grid (signalling): written the first time,
        transformed after. Play it on its own, about half a second."""
        new = label(text, 24, C["muted"])
        new.move_to([-config.frame_width / 2 + 0.35 + new.width / 2, config.frame_height / 2 - 0.2, 0])
        old = getattr(self, "_heading", None)
        if old is None:
            self._heading = new
            return Write(new)
        return Transform(old, new)


class Soil(Chaptered, MovingCameraScene):
    NUMBER, TITLE = 1, "The soil"

    def construct(self):
        self.camera.background_color = C["bg"]
        self.camera.frame.save_state()
        rng = np.random.default_rng(5)
        self.chapter()
        # s1: a droplet; the glass comes over it; the camera pushes in until cells fill the view
        drop = Circle(radius=1.9).set_stroke(SOIL, width=3).set_fill(SOIL, opacity=0.45)
        grains = VGroup(*[RegularPolygon(n=int(rng.integers(5, 8)), radius=rng.uniform(0.04, 0.11))
                          .set_stroke(width=0).set_fill("#A58A6C", opacity=0.7)
                          .move_to(drop.point_at_angle(rng.uniform(0, TAU)) * rng.uniform(0, 0.9)) for _ in range(60)])
        world = self.place(VGroup(drop, grains), "B1", "droplet", span="3x3")
        lens_r = 1.25
        pick = rng.choice(N, size=70, p=D["true"])          # cells in proportion to the true shares
        cells = VGroup(*[cell(i, rng).move_to(world.get_center() + lens_r * 0.85 * np.sqrt(rng.uniform()) *
                                              np.array([np.cos(a), np.sin(a), 0]))
                         for i, a in zip(pick, rng.uniform(0, TAU, 70))])
        ring = Circle(radius=lens_r).set_stroke(C["fg"], width=9).set_fill(C["fg"], opacity=0.06)
        handle = Line(ORIGIN, [1.4, -1.4, 0], stroke_width=16, color=C["fg"]).shift(ring.point_at_angle(-PI / 4))
        glass = VGroup(ring, handle).move_to(world.get_center() + np.array([4.2, 1.6, 0]))
        cap = self.place(label("soil, up close", 30), "E3", "label", span="2x1")
        with self.say("s1") as t:
            self.play(DrawBorderThenFill(drop), LaggedStart(*[GrowFromCenter(g) for g in grains], lag_ratio=0.02),
                      Write(cap), *self.tags("schematic drawing"), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(glass.animate(path_arc=-PI / 3).shift(world.get_center() - ring.get_center()), run_time=self.left(t, 1, "bacteria"))
            self.track(glass, "glass")
            self.at(t, 1, "bacteria")
            self.play(self.camera.frame.animate.scale(0.42).move_to(world.get_center()),
                      LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.03), run_time=self.left(t, 1))

        # s2: pull back; the droplet shrinks to an icon; the cells gather into a sample of 80 taxa
        icon = VGroup(drop, grains)
        crowd = cells.copy().arrange_in_grid(rows=7, cols=10, buff=0.2).scale(1.4)
        self.place(crowd, "A2", "crowd", span="2x2")
        info = self.place(VGroup(label("simulated", 26, C["muted"]), label(f"{P.CELLS:,} cells", 32),
                                 label(f"{N} taxa", 32)).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
                          "D2", "info", span="3x2")
        with self.say("s2") as t:
            self.play(Restore(self.camera.frame), FadeOut(glass), FadeOut(cap), run_time=1.6)
            self.release("glass", "label", "droplet")
            self.play(icon.animate.scale(0.3).to_corner(UL, buff=0.3), Transform(cells, crowd),
                      *self.tags("schematic drawing; simulated counts"), run_time=self.left(t, 0))
            self.track(icon, "icon")
            self.at(t, 1)
            self.play(Write(info), run_time=self.left(t, 1))

        # s3: each cell flies to its taxon's bar; the bars grow; braces name the two groups
        ch = self.place(chart(D["true"], "cells per taxon", xlab="taxa, most abundant first", **CHART),
                        "B1", "chart", span="5x3")
        b = ch[2]
        top = Brace(VGroup(*b[:6]), UP, color=C["fg"], buff=0.35)
        tail = Brace(VGroup(*b[12:]), UP, color=C["muted"], buff=0.35)
        tl = label("a few abundant taxa", 24).next_to(top, UP, buff=0.1)
        ll = label("many low-abundance taxa", 24, C["muted"]).next_to(tail, UP, buff=0.1)
        with self.say("s3") as t:
            self.release("crowd", "info")
            self.play(ReplacementTransform(info, ch[3]), Create(ch[0]), Create(ch[1]), Write(ch[4]), run_time=0.8)
            self.play(LaggedStart(*[c.animate.scale(0.6).move_to(b[pick[k]].get_bottom() + UP * 0.05)
                                    for k, c in enumerate(cells)], lag_ratio=0.02), run_time=self.left(t, 0))
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.02), FadeOut(cells), run_time=1.2)
            self.at(t, 1, "abundant")
            self.play(Create(top), Write(tl), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Create(tail), Write(ll), run_time=self.left(t, 2))

        # s3b: real soils have the same shape (data, one global survey)
        card = self.place(VGroup(label("real soils, sequenced: one global survey (data)", 22, C["muted"]),
                                 label("2% of bacterial taxa: about 41% of an average sample's reads", 28))
                          .arrange(DOWN, buff=0.12), "A4", "card", span="4x1")
        with self.say("s3b") as t:
            self.play(Write(card[0]), Indicate(VGroup(*b[12:]), color=C["fg"], scale_factor=1.02), run_time=self.left(t, 0))
            self.at(t, 1, "just 2%")
            self.play(Write(card[1]), Indicate(VGroup(*b[:6]), color=C["fg"], scale_factor=1.05), run_time=self.left(t, 1))

        # s4 (distil): the chart holds; its title says what it is
        truth = label("the truth: cells per taxon", 24).move_to(ch[3])
        with self.say("s4") as t:
            self.play(Transform(ch[3], truth), run_time=1.0)
            self.play(Indicate(b, scale_factor=1.04, color=C["fg"]), run_time=1.2)


class Genes(Chaptered, MovingCameraScene):
    NUMBER, TITLE = 2, "From cells to genes"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(11)
        self.chapter()
        # s5: bead beating; most cells split and spill DNA
        who = [0, 1, 2, 3, 4, 5, 0, 3, 1, 4, 2, 0]
        tough = {2, 7, 10}                                    # schematic: three thick-walled cells
        cells = VGroup()
        for k, i in enumerate(who):
            c = cell(i, rng, scale=3.2)
            if k in tough:
                c.set_stroke(C["fg"], width=6)
            cells.add(c)
        cells.arrange_in_grid(rows=3, cols=4, buff=(0.9, 0.7))
        beads = VGroup(*[Circle(radius=0.11).set_stroke(width=0).set_fill(C["muted"], opacity=0.8)
                         .move_to(np.array([rng.uniform(-3.4, 3.4), rng.uniform(-1.6, 1.6), 0])) for _ in range(22)])
        tube = RoundedRectangle(width=8.2, height=4.2, corner_radius=0.5).set_stroke(C["muted"], width=2)
        stage = self.place(VGroup(tube, cells, beads), "A1", "tube", span="6x3")
        key = self.place(VGroup(label("grey dots: beads", 22, C["muted"])), "A4", "key", span="6x1")
        strands = VGroup(*[dna(COL[i]).move_to(cells[k]) for k, i in enumerate(who)])
        opened = [k for k in range(len(who)) if k not in tough]
        with self.say("s5") as t:
            self.play(self.heading("DNA extraction"), *self.tags("schematic"), run_time=0.5)
            self.play(Create(tube), LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.05), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(LaggedStart(*[GrowFromCenter(b_) for b_ in beads], lag_ratio=0.03), Write(key[0]), run_time=0.9)
            shake = self.left(t, 1, "which break") / 3
            for _ in range(3):
                self.play(*[b_.animate.shift(np.array([rng.uniform(-0.5, 0.5), rng.uniform(-0.4, 0.4), 0])) for b_ in beads],
                          Wiggle(tube, scale_value=1.02, rotation_angle=0.02 * TAU), run_time=shake)
            self.at(t, 1, "which break")
            self.play(*[ReplacementTransform(cells[k], strands[k]) for k in opened], run_time=self.left(t, 1))

        # s6: the tough cells stay shut, circled one by one
        key2 = VGroup(label("thick outline: a tougher cell, still shut", 22, C["muted"]),
                      label("one study: harder shaking gave up to 400% more Gram-positive DNA", 24)
                      ).arrange(DOWN, buff=0.12).move_to(key)
        with self.say("s6") as t:
            self.play(Succession(*[Circumscribe(cells[k], color=C["fg"], run_time=1.0) for k in tough]),
                      run_time=self.left(t, 0, "so they"))
            self.play(ReplacementTransform(key, key2[0]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Write(key2[1]), run_time=self.left(t, 1, "from Gram"))

        # s7: one strand straightens into a ring, its genome; the 16S gene is drawn on
        lead = strands[0]
        centre = stage.get_center()
        big = Circle(radius=2.0).set_stroke(C["fg"], width=5).move_to(centre)
        gene = Arc(radius=2.0, start_angle=PI / 3, angle=0.32, stroke_width=16, color=COL[0]).shift(centre)
        glab = label("16S rRNA gene", 30).next_to(gene, UP + RIGHT, buff=0.04)
        gnl = label("one genome, a ring of DNA", 26, C["muted"]).next_to(big, DOWN, buff=0.25)
        rest = VGroup(tube, beads, *[strands[k] for k in opened if k != 0], *[cells[k] for k in tough], key2)
        with self.say("s7") as t:
            self.play(self.heading("the 16S rRNA gene"), run_time=0.5)
            self.play(FadeOut(rest), run_time=0.8)
            self.release("tube", "key")
            self.play(Transform(lead, big), Write(gnl), run_time=self.left(t, 0, "one gene"))
            self.at(t, 0, "one gene")
            self.play(Create(gene), Write(glab), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Indicate(gene, color=C["fg"]), Indicate(glab, color=COL[0]), run_time=self.left(t, 1, "which kind"))

        # s8: the ring moves left and gains its copies; taxon 3's ring has one
        c1, c3 = int(D["copies"][0]), int(D["copies"][2])
        left, right = centre + LEFT * 2.9 + UP * 0.3, centre + RIGHT * 2.9 + UP * 0.3
        g1, g3 = genome_ring(c1, COL[0], left), genome_ring(c3, COL[2], right)
        l1 = label(f"taxon 1: {c1} cop{'y' if c1 == 1 else 'ies'}", 28, COL[0]).next_to(g1, DOWN, buff=0.3)
        l3 = label(f"taxon 3: {c3} cop{'y' if c3 == 1 else 'ies'}", 28, COL[2]).next_to(g3, DOWN, buff=0.3)
        span = label("a genome carries 1 to about 15 copies, rarely more", 24, C["muted"]).next_to(VGroup(l1, l3), DOWN, buff=0.35)
        with self.say("s8") as t:
            self.play(self.heading("copies per genome"), run_time=0.5)
            self.play(FadeOut(glab), FadeOut(gnl), Transform(lead, g1[0]), Transform(gene, g1[1][0]), run_time=self.left(t, 0, "from 1"))
            self.at(t, 0, "from 1")
            self.play(Write(span), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(LaggedStart(*[Create(a) for a in g1[1][1:]], lag_ratio=0.3), Write(l1), run_time=self.left(t, 1))
            self.track(VGroup(lead, gene, g1[1], l1), "g1")
            self.at(t, 2)
            self.play(Create(g3[0]), run_time=0.6)
            self.play(Create(g3[1]), Write(l3), run_time=self.left(t, 2))
            self.track(VGroup(g3, l3), "g3")
        self.add(g1[1])

        # s9: a growing cell holds two genomes: the first ring is copied beside itself
        twin = VGroup(lead, gene, g1[1]).copy()
        with self.say("s9") as t:
            self.play(self.heading("copies per cell"), run_time=0.5)
            self.play(FadeOut(VGroup(g3, l3, span)), run_time=0.8)
            self.release("g3")
            self.play(VGroup(lead, gene, g1[1], l1).animate.shift(RIGHT * 1.0), run_time=0.8)
            twin.move_to(VGroup(lead).get_center() + RIGHT * 3.2)
            outline = RoundedRectangle(width=7.4, height=3.6, corner_radius=1.6).set_stroke(COL[0], width=3) \
                .move_to(VGroup(lead, twin).get_center())
            note = label("a cell can hold several genome copies (here two); in soil, barely measured", 26).next_to(outline, DOWN, buff=0.3)
            self.play(TransformFromCopy(VGroup(lead, gene, g1[1]), twin), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Create(outline), FadeOut(l1), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Write(note), run_time=self.left(t, 2))
            self.track(VGroup(outline, note), "twin")

        # s10 (distil): the chart from chapter 1 returns and is reshaped twice
        names = ["cells", "DNA", "16S copies"]
        keys = ["true", "dna", "templates"]
        titles = ["share of cells per taxon", "share of extracted DNA", "share of 16S gene copies: already shifted"]
        ch = self.place(chart(D["true"], titles[0], xlab="taxa, in the order of the cell counts", **CHART),
                        "A1", "chart", span="6x3")
        b = ch[2]
        before = label(f"taxon 1: {pct(D['true'][0])} of cells", 28, COL[0])
        after = label(f"{D['templates'][0]:.1%} of gene copies", 28, COL[0])   # as spoken: 49.5%
        notes = self.place(VGroup(before, label("→", 28, COL[0]), after).arrange(RIGHT, buff=0.3, aligned_edge=DOWN), "A4", "notes", span="6x1")
        with self.say("s10") as t:
            self.play(self.heading("the shares so far"), run_time=0.5)
            self.play(FadeOut(VGroup(lead, gene, g1[1], twin, outline, note)), run_time=0.6)
            self.release("g1", "twin")
            self.play(draw_chart(ch, 1.2), *self.tags("simulated"), run_time=1.2)
            step = self.left(t, 0) / 2
            for k in (1, 2):
                new = bars(D[keys[k]], **CHART).match_width(b).move_to(b, aligned_edge=DL)
                self.play(Transform(b, new), Transform(ch[3], label(titles[k], 24).move_to(ch[3])), run_time=step)
            self.at(t, 1)
            self.play(Write(before), run_time=self.left(t, 1, "to 49.5"))
            self.at(t, 1, "to 49.5")
            self.play(Write(notes[1]), Write(after), Indicate(b[0], color=C["fg"]), run_time=self.left(t, 1))


class Amplify(Chaptered):
    NUMBER, TITLE = 3, "PCR"

    def construct(self):
        self.camera.background_color = C["bg"]
        self.chapter()
        # s11: three taxa's 16S genes: the conserved stretches alike, the variable region different in each
        CW, VW, H = 3.0, 1.8, 0.3
        genes, varis, lefts, rights = VGroup(), [], [], []
        for k in range(3):
            l_ = Rectangle(width=CW, height=H, stroke_width=0, fill_color=C["muted"], fill_opacity=0.55)
            v_ = Rectangle(width=VW, height=H, stroke_width=0, fill_color=COL[k], fill_opacity=1)
            r_ = Rectangle(width=CW, height=H, stroke_width=0, fill_color=C["muted"], fill_opacity=0.55)
            g = VGroup(l_, v_, r_).arrange(RIGHT, buff=0)
            name = label(f"taxon {k + 1}", 22, COL[k]).next_to(g, LEFT, buff=0.3)
            genes.add(VGroup(g, name)); varis.append(v_); lefts.append(l_); rights.append(r_)
        genes.arrange(DOWN, buff=0.75, aligned_edge=RIGHT)
        gtitle = label("16S rRNA gene", 26).next_to(genes, UP, buff=0.5).align_to(genes[0][0], LEFT)
        cons = VGroup(label("conserved", 22, C["muted"]).next_to(lefts[2], DOWN, buff=0.15),
                      label("conserved", 22, C["muted"]).next_to(rights[2], DOWN, buff=0.15))
        vlab = label("variable region", 22).next_to(varis[2], DOWN, buff=0.15)
        stage = self.place(VGroup(gtitle, genes, cons, vlab), "A1", "genes", span="6x3")
        legend = self.place(VGroup(label("conserved: much the same across bacteria", 24, C["muted"]),
                                   label("variable: differs from taxon to taxon", 24, C["muted"])).arrange(DOWN, buff=0.08),
                            "A4", "legend", span="6x1")
        with self.say("s11") as t:
            self.play(self.heading("the 16S rRNA gene"), *self.tags("schematic"), run_time=0.5)
            self.play(Write(gtitle), run_time=0.5)
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(g[0], LEFT), Write(g[1])) for g in genes], lag_ratio=0.3),
                      run_time=self.left(t, 0))
            self.at(t, 1, "conserved")
            self.play(Write(cons), Write(legend[0]), *[Indicate(VGroup(lefts[k], rights[k]), color=C["fg"], scale_factor=1.03)
                                                       for k in range(3)], run_time=self.left(t, 1))
            self.at(t, 2, "variable")
            self.play(Write(vlab), Write(legend[1]), *[Indicate(v_, color=C["fg"]) for v_ in varis], run_time=self.left(t, 2))

        # s11b: primers land on the conserved stretches of all three; the variable region between them is the barcode
        prim = VGroup()
        for k in range(3):
            f_ = Arrow(LEFT * 0.45, RIGHT * 0.45, buff=0, color=C["fg"], stroke_width=5, max_tip_length_to_length_ratio=0.35) \
                .next_to(lefts[k], UP, buff=0.06).align_to(lefts[k], RIGHT)
            r_ = Arrow(RIGHT * 0.45, LEFT * 0.45, buff=0, color=C["fg"], stroke_width=5, max_tip_length_to_length_ratio=0.35) \
                .next_to(rights[k], UP, buff=0.06).align_to(rights[k], LEFT)
            prim.add(f_, r_)
        plab = label("primers", 22, C["muted"]).next_to(prim[0], LEFT, buff=0.15)
        brace = Brace(varis[2], DOWN, color=C["fg"], buff=0.55)
        blab = VGroup(label("barcode", 26, weight=BOLD),
                      label("a variable region (V4) of the 16S rRNA gene", 22)).arrange(DOWN, buff=0.06).next_to(brace, DOWN, buff=0.1)
        stage.add(prim, plab, brace, blab)
        for a_ in prim:
            a_.shift(UP * 1.5)
        plab.set_opacity(0)
        with self.say("s11b") as t:
            self.play(self.heading("PCR primers"), run_time=0.5)
            self.play(*[a_.animate.shift(DOWN * 1.5) for a_ in prim], plab.animate.set_opacity(1), run_time=self.left(t, 0, "so one"))
            self.play(*[Indicate(VGroup(lefts[k], rights[k]), color=C["fg"], scale_factor=1.03) for k in range(3)],
                      run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(FadeOut(legend), Create(brace), *[Indicate(v_, color=C["fg"]) for v_ in varis], run_time=self.left(t, 1))
            self.release("legend")
            self.at(t, 2)
            self.play(Write(blab[1]), run_time=self.left(t, 2, "our barcode"))
            self.at(t, 2, "barcode")
            self.play(ReplacementTransform(vlab, blab[0]), run_time=self.left(t, 2))

        # s12: PCR copies taxon 1's barcode, each new strand out of an old one
        top_var = varis[0]
        keep = VGroup(genes[0], gtitle)
        out_ = VGroup(genes[1], genes[2], cons, brace, blab, *prim, plab)
        bc_lab = label("barcode (16S, V4)", 22).next_to(top_var, UP, buff=0.12)

        def strands(n, area_c):
            g = VGroup(*[Line(LEFT * 0.45, RIGHT * 0.45, stroke_width=8, color=COL[0]) for _ in range(n)])
            return g.arrange_in_grid(rows=max(1, n // 4), cols=min(n, 4), buff=(0.35, 0.3)).move_to(area_c)
        counter = label("PCR cycle 0: 1 copy", 30)
        with self.say("s12") as t:
            self.play(self.heading("PCR"), FadeOut(out_), run_time=0.6)
            self.release("genes")
            self.play(keep.animate.to_edge(UP, buff=0.9), run_time=0.8)
            bc_lab.next_to(top_var, UP, buff=0.12)
            area_c = keep.get_bottom() + DOWN * 2.0
            counter.move_to(area_c + DOWN * 1.8)
            self.play(Write(bc_lab), Write(counter), run_time=0.5)
            now = strands(1, area_c)
            self.play(TransformFromCopy(top_var, now[0]), run_time=self.left(t, 0))
            self.at(t, 1)
            step = self.left(t, 1) / 4
            for k in range(1, 5):
                nxt = strands(2 ** k, area_c)
                self.play(TransformFromCopy(now, nxt[len(now):]), Transform(now, nxt[:len(now)]),
                          Transform(counter, label(f"PCR cycle {k}: {2 ** k} copies", 30).move_to(counter)), run_time=step)
                self.remove(now); now = nxt; self.add(now)
            self.at(t, 2, "our simulation")
            self.play(Transform(counter, label(f"PCR cycle {P.CYCLES}: many copies", 30).move_to(counter)), run_time=self.left(t, 2))
            self.track(VGroup(keep, bc_lab, now, counter), "pcr")

        # s13: PCR bias: taxon 1's copies outrun taxon 3's (schematic), and one study's figure
        col1 = VGroup(*[Line(LEFT * 0.4, RIGHT * 0.4, stroke_width=8, color=COL[0]) for _ in range(16)]).arrange(DOWN, buff=0.12)
        col3 = VGroup(*[Line(LEFT * 0.4, RIGHT * 0.4, stroke_width=8, color=COL[2]) for _ in range(5)]).arrange(DOWN, buff=0.12)
        cols = VGroup(col1, col3).arrange(RIGHT, buff=1.2, aligned_edge=DOWN)
        clabs = VGroup(label("taxon 1", 22, COL[0]).next_to(col1, DOWN, buff=0.2), label("taxon 3", 22, COL[2]).next_to(col3, DOWN, buff=0.2))
        race = self.place(VGroup(cols, clabs), "A1", "race", span="3x3")
        card = self.place(VGroup(label("one study (data)", 22, C["muted"]),
                                 label("lab-grown gut communities", 26),
                                 label(f"after {P.CYCLES} cycles: about 1 taxon in 5", 26),
                                 label("more than fourfold off", 26)).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
                          "D1", "card", span="3x3")
        with self.say("s13") as t:
            self.play(self.heading("PCR bias"), FadeOut(VGroup(keep, bc_lab, counter)), run_time=0.6)
            self.release("pcr")
            self.play(ReplacementTransform(now, col1), Write(clabs[0]), run_time=1.0)
            self.play(LaggedStart(*[GrowFromEdge(x, LEFT) for x in col3], lag_ratio=0.5), Write(clabs[1]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Write(card[:2]), run_time=self.left(t, 1, "about 1"))
            self.at(t, 1, "about 1")
            self.play(Write(card[2:]), run_time=self.left(t, 1))

        # s13b: the simulation: the axis first, then one dot per taxon
        lb = np.log2(D["bias"])
        W = 10.0
        x = lambda v: v / 5 * W / 2                                # log2 -5..5 -> -W/2..W/2
        axis = Line([-W / 2, 0, 0], [W / 2, 0, 0], color=C["muted"], stroke_width=2)
        ticks = VGroup(*[VGroup(Line([x(v), -0.08, 0], [x(v), 0.08, 0], color=C["muted"], stroke_width=2),
                                label(s_, 22, C["muted"]).next_to([x(v), 0, 0], DOWN, buff=0.18))
                         for v, s_ in ((-4, "1/16"), (-2, "1/4"), (0, "1"), (2, "4"), (4, "16"))])
        ends = VGroup(label("← copied too few", 22, C["muted"]).next_to([x(-4.6), 0, 0], DOWN, buff=0.7).align_to([x(-5), 0, 0], LEFT),
                      label("copied too many →", 22, C["muted"]).next_to([x(4.6), 0, 0], DOWN, buff=0.7).align_to([x(5), 0, 0], RIGHT),
                      label("1 = fair", 22, C["muted"]).next_to([x(0), 0, 0], DOWN, buff=0.7))
        far = np.abs(lb) > 2
        bins_ = np.floor(lb / 0.25)
        order = np.argsort(lb)
        dots, rings, stack = VGroup(), VGroup(), {}
        for i in order:
            d_ = Dot(radius=0.07, color=COL[i], fill_opacity=1 if far[i] else 0.45)
            k = stack.get(bins_[i], 0); stack[bins_[i]] = k + 1
            d_.move_to([x(np.clip((bins_[i] + 0.5) * 0.25, -5, 5)), 0.16 + k * 0.17, 0])
            dots.add(d_)
            if far[i]:
                rings.add(Circle(radius=0.12).set_stroke(C["fg"], width=2.5).move_to(d_))
        lines = VGroup(*[DashedLine([x(v), -0.05, 0], [x(v), 1.9, 0], color=C["fg"], dash_length=0.08, stroke_width=2)
                         for v in (-2, 2)])
        for i_ in (0, 2):
            j_ = int(np.where(order == i_)[0][0])
            dots[j_].set_fill(opacity=1)
        d1_, d3_ = dots[int(np.where(order == 0)[0][0])], dots[int(np.where(order == 2)[0][0])]
        top_y = max(d_.get_top()[1] for d_ in dots) + 0.35
        n1t = label("taxon 1", 20, COL[0]).move_to([d1_.get_x() + 1.3, top_y, 0])
        n3t = label("taxon 3", 20, COL[2]).move_to([d3_.get_x() - 1.3, top_y, 0])
        n1 = VGroup(n1t, Arrow(n1t.get_bottom(), d1_.get_center(), buff=0.1, color=COL[0], stroke_width=3))
        n3 = VGroup(n3t, Arrow(n3t.get_bottom(), d3_.get_center(), buff=0.1, color=COL[2], stroke_width=3))
        ttl = label(f"each taxon's PCR bias after {P.CYCLES} cycles (simulated)", 24).next_to(axis, UP, buff=2.9)
        dlab = label("each dot: one taxon", 22, C["muted"]).next_to(ttl, DOWN, buff=0.15)
        count = label(f"ringed: beyond fourfold, {int(far.sum())} of {N} taxa", 24).next_to(ends, DOWN, buff=0.3)
        plot = self.place(VGroup(axis, ticks, ends, dots, rings, lines, ttl, dlab, count, n1, n3), "A1", "bias", span="6x4")
        with self.say("s13b") as t:
            self.play(FadeOut(VGroup(race, card)), run_time=0.5)
            self.release("race", "card")
            self.play(Write(ttl), *self.tags("simulated"), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Create(axis), Write(ticks), run_time=self.left(t, 1, "1 is fair"))
            self.at(t, 1, "1 is fair")
            self.play(Write(ends[2]), Indicate(ticks[2], color=C["fg"]), run_time=self.left(t, 1, "4 is"))
            self.at(t, 1, "4 is")
            self.play(Write(ends[1]), Indicate(ticks[3], color=C["fg"]), run_time=self.left(t, 1, "a quarter"))
            self.at(t, 1, "a quarter")
            self.play(Write(ends[0]), Indicate(ticks[1], color=C["fg"]), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Write(dlab), LaggedStart(*[d_.animate(rate_func=rush_into).shift(DOWN * 2.4) for d_ in dots.shift(UP * 2.4)],
                                               lag_ratio=0.02), run_time=self.left(t, 2, "ringed"))
            self.at(t, 2, "ringed")
            self.play(Create(lines), LaggedStart(*[Create(r) for r in rings], lag_ratio=0.1), Write(count), Write(n1), Write(n3),
                      run_time=self.left(t, 2))
        self.play(FadeOut(plot), run_time=0.6)
        self.release("bias")

        # s14: the chart, from gene copies to barcodes; taxon 1 and taxon 3 marked
        ch = self.place(chart(D["templates"], "share of 16S gene copies", xlab="taxa, in the order of the cell counts", **CHART),
                        "A1", "chart", span="6x3")
        b = ch[2]
        with self.say("s14") as t:
            self.play(self.heading("share of barcodes"), run_time=0.5)
            self.play(draw_chart(ch, 1.0), run_time=1.0)
            new = bars(D["pool"], **CHART).match_width(b).move_to(b, aligned_edge=DL)
            self.play(Transform(b, new), Transform(ch[3], label("share of barcodes after PCR", 24).move_to(ch[3])), run_time=self.left(t, 0))
            m1 = label(f"taxon 1: {pct(D['pool'][0])}", 24, COL[0]).next_to(b[0], RIGHT, buff=0.15).align_to(b[0], UP)
            a3 = Arrow(b[2].get_top() + UP * 0.9 + RIGHT * 0.5, b[2].get_top() + UP * 0.05, buff=0, color=COL[2], stroke_width=4)
            m3 = label(f"taxon 3: {pct(D['true'][2])} of cells → {pct(D['pool'][2])}", 24, COL[2]).next_to(a3.get_start(), UP + RIGHT, buff=0.05)
            self.at(t, 1)
            self.play(Write(m1), Indicate(b[0], color=C["fg"]), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(GrowArrow(a3), Write(m3), run_time=self.left(t, 2))
            self.track(VGroup(m1, a3, m3), "marks")

        # s14b (distil): taxon 1 and taxon 3 side by side; the ratio between them counts up with each step
        HB, YM = 3.0, 0.5
        stages = [("in cells", "true"), ("in 16S gene copies", "templates"), ("in barcodes", "pool")]
        def pair(key):
            v1, v3 = D[key][0], D[key][2]
            r1 = Rectangle(width=1.0, height=max(HB * v1 / YM, 0.02), stroke_width=0, fill_color=COL[0], fill_opacity=1)
            r3 = Rectangle(width=1.0, height=max(HB * v3 / YM, 0.02), stroke_width=0, fill_color=COL[2], fill_opacity=1)
            r1.move_to([-1.2, 0, 0], aligned_edge=DOWN); r3.move_to([1.2, 0, 0], aligned_edge=DOWN)
            v1l = label(pct(v1) if key != "templates" else f"{v1:.1%}", 24, COL[0]).next_to(r1, UP, buff=0.1)
            v3l = label(pct(v3), 24, COL[2]).next_to(r3, UP, buff=0.1)
            return VGroup(r1, r3, v1l, v3l)
        base = Line([-2.2, 0, 0], [2.2, 0, 0], color=C["muted"], stroke_width=2)
        names = VGroup(label("taxon 1", 22, COL[0]).move_to([-1.2, -0.3, 0]), label("taxon 3", 22, COL[2]).move_to([1.2, -0.3, 0]))
        p0 = pair("true")
        def ratio_text(key):
            return label(f"{D[key][0] / D[key][2]:.0f} to 1", 44, weight=BOLD)
        rgrp = ratio_text("true").move_to([4.6, 1.6, 0])
        hist_ = VGroup()
        stg = label(stages[0][0], 28, C["muted"]).move_to([0, 3.4, 0])
        comp = self.place(VGroup(base, names, p0, rgrp, stg), "B1", "compare", span="4x3")
        with self.say("s14b") as t:
            self.play(FadeOut(VGroup(ch[0], ch[1], ch[3], ch[4], *[b[i] for i in range(N) if i not in (0, 2)], *self.mobjects_of("marks"))),
                      run_time=0.6)
            self.release("chart", "marks")
            self.play(ReplacementTransform(b[0], p0[0]), ReplacementTransform(b[2], p0[1]), Create(base), Write(names), Write(stg),
                      self.heading("taxon 1 against taxon 3"), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Write(p0[2]), Write(p0[3]), run_time=self.left(t, 1, "about 3"))
            self.at(t, 1, "about 3")
            self.play(Write(rgrp), run_time=self.left(t, 1))
            log_ = VGroup(*[label(f"{nm}: {D[k_][0] / D[k_][2]:.0f} to 1", 22, C['muted']) for nm, k_ in stages]
                          ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(rgrp, DOWN, buff=0.5)
            for j, (name_, key) in enumerate(stages[1:], start=2):
                self.at(t, j)
                nxt = pair(key).move_to(p0, aligned_edge=DOWN)
                self.play(Transform(p0, nxt), Transform(stg, label(name_, 28, C["muted"]).move_to(stg)),
                          Transform(rgrp, ratio_text(key).move_to(rgrp)), Write(log_[j - 2]), run_time=max(self.left(t, j) - (0.6 if j == 3 else 0), 0.5))
            self.play(Write(log_[2]), run_time=0.6)

    def mobjects_of(self, name):
        rec = self._placed.get(name)
        return [rec["m"]] if rec else []


class Sequence(Chaptered):
    NUMBER, TITLE = 4, "Sequencing"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(13)
        self.chapter()
        # s15: the chain from the earlier chapters: soil, a cell, its DNA, barcode copies, into sample A's tube
        tubes, kids = VGroup(), []
        for k, s in enumerate("ABC"):
            box = RoundedRectangle(width=2.4, height=1.9, corner_radius=0.25).set_stroke(SAMPLE, width=3)
            name = label(f"sample {s}", 24).next_to(box, UP, buff=0.12)
            amps = VGroup(*[Line(LEFT * 0.27, RIGHT * 0.27, stroke_width=7, color=COL[int(i)])
                            for i in rng.choice(6, 6)]).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.2)).move_to(box)
            tubes.add(VGroup(box, name, amps)); kids.append(amps)
        tubes.arrange(RIGHT, buff=0.9)
        self.place(tubes, "A2", "tubes", span="6x2")
        legend = self.place(label("lines: barcode copies, coloured by taxon", 22, C["muted"]), "A4", "legend", span="6x1")
        icon = soil_icon().scale(1.6).move_to([-5.6, 2.7, 0])
        cell0 = Circle(radius=0.2).set_stroke(width=0).set_fill(COL[0], 0.95).move_to([-3.6, 2.7, 0])
        strand0 = dna(COL[0]).move_to([-1.6, 2.7, 0])
        copies0 = VGroup(*[Line(LEFT * 0.27, RIGHT * 0.27, stroke_width=7, color=COL[0]) for _ in range(3)]) \
            .arrange(DOWN, buff=0.12).move_to([0.4, 2.7, 0])
        arrows = VGroup(*[Arrow(a_ + RIGHT * 0.45, b_ + LEFT * 0.45, buff=0, color=C["muted"], stroke_width=3)
                          for a_, b_ in (([-5.6, 2.7, 0], [-3.6, 2.7, 0]), ([-3.6, 2.7, 0], [-1.6, 2.7, 0]), ([-1.6, 2.7, 0], [0.4, 2.7, 0]))])
        steps = VGroup(label("soil", 20, C["muted"]).next_to(icon, DOWN, buff=0.1),
                       label("cell", 20, C["muted"]).next_to(cell0, DOWN, buff=0.25),
                       label("DNA", 20, C["muted"]).next_to(strand0, DOWN, buff=0.25),
                       label("PCR: barcode copies", 20, C["muted"]).next_to(copies0, DOWN, buff=0.2))
        with self.say("s15") as t:
            self.play(self.heading("samples"), *self.tags("schematic"), run_time=0.5)
            self.play(DrawBorderThenFill(icon), Write(steps[0]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(GrowArrow(arrows[0]), TransformFromCopy(icon, cell0), Write(steps[1]), run_time=self.left(t, 1, "give up"))
            self.play(GrowArrow(arrows[1]), TransformFromCopy(cell0, strand0), Write(steps[2]), run_time=self.left(t, 1, "and PCR"))
            self.at(t, 1, "PCR copies")
            self.play(GrowArrow(arrows[2]), TransformFromCopy(strand0, copies0), Write(steps[3]), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Create(tubes[0][0]), Write(tubes[0][1]), run_time=0.5)
            self.play(*[c.animate(path_arc=-PI / 3).move_to(kids[0][j]) for j, c in enumerate(copies0)],
                      LaggedStart(*[GrowFromCenter(a) for a in kids[0][3:]], lag_ratio=0.2), run_time=1.0)
            self.remove(copies0); self.add(kids[0][:3])
            self.play(*[AnimationGroup(Create(tb[0]), Write(tb[1]), LaggedStart(*[GrowFromCenter(a) for a in tb[2]], lag_ratio=0.1))
                        for tb in tubes[1:]], Write(legend), run_time=self.left(t, 2))
        self.play(FadeOut(VGroup(icon, cell0, strand0, arrows, steps)), run_time=0.5)

        # s15b: each sample's barcodes get its index tag
        tags_, tagged_amps = [], []
        for k, amps in enumerate(kids):
            for a in amps:
                tg = index_tag(k).next_to(a, LEFT, buff=0.05)
                tagged_amps.append(VGroup(tg, a)); tags_.append((k, tg))
        legend2 = label("white squares: the index tag, one pattern per sample", 22, C["muted"]).move_to(legend)
        with self.say("s15b") as t:
            self.play(self.heading("indexing"), Transform(legend, legend2), run_time=0.5)
            step = self.left(t, 0) / 3
            for k in range(3):
                self.play(LaggedStart(*[GrowFromEdge(tg, RIGHT) for kk, tg in tags_ if kk == k], lag_ratio=0.1),
                          Indicate(tubes[k][1], color=C["fg"]), run_time=step)
            self.at(t, 1)
            self.play(*[Indicate(tb[0], color=C["fg"], scale_factor=1.03) for tb in tubes], run_time=self.left(t, 1))

        # s16: pooled; reads drawn at random into the sequencer, each sample's meter growing as its reads arrive
        pool_box = RoundedRectangle(width=4.2, height=1.5, corner_radius=0.25).set_stroke(C["muted"], width=2)
        pool = self.place(VGroup(pool_box, label("one pooled run", 22, C["muted"]).next_to(pool_box, DOWN, buff=0.1)),
                          "B3", "pool", span="4x1")
        order = rng.permutation(len(tagged_amps))
        spots = [None] * len(tagged_amps)
        for slot, j in enumerate(order):
            c, r = slot % 6, slot // 6
            spots[j] = pool_box.get_center() + np.array([(c - 2.5) * pool_box.width / 6.6, (1 - r) * pool_box.height / 3.8, 0])
        seq = RoundedRectangle(width=2.6, height=1.2, corner_radius=0.2).set_stroke(C["fg"], width=3)
        seqg = self.place(VGroup(seq, label("sequencer", 26).move_to(seq)), "A1", "seq", span="2x1")
        FULL = 3.6
        frames_, trk, fills = VGroup(), [ValueTracker(0) for _ in range(3)], []
        rows = VGroup()
        for k, s in enumerate("ABC"):
            fr = Rectangle(width=FULL, height=0.34).set_stroke(C["rule"], width=2)
            rows.add(VGroup(label(f"sample {s}", 22), index_tag(k), fr).arrange(RIGHT, buff=0.25))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        edge = max(r_[1].get_right()[0] for r_ in rows) + 0.25
        for r_ in rows:
            r_[2].shift(RIGHT * (edge - r_[2].get_left()[0]))
        mtitle = label("reads per sample", 24, C["muted"]).next_to(rows, UP, buff=0.2).align_to(rows, LEFT)
        meters = self.place(VGroup(mtitle, rows), "D1", "meters", span="3x2")
        for k in range(3):
            fr = rows[k][2]
            fills.append(always_redraw(lambda k=k, fr=fr: Rectangle(width=max(FULL * fr.width / FULL * trk[k].get_value(), 0.001),
                                                                    height=0.34, stroke_width=0, fill_color=SAMPLE,
                                                                    fill_opacity=0.85).align_to(fr, LEFT).align_to(fr, UP)))
        plan = [0] * 12 + [1] * 7 + [2]                       # schematic: one sample far behind
        rng.shuffle(plan)
        plan = [k for k in plan if k != 2] + [2]
        per = {0: 1.0 / 12, 1: SKETCH_DEPTH[1] / 7, 2: SKETCH_DEPTH[2]}
        rp_r1 = Arrow(LEFT * 0.7, RIGHT * 0.2, buff=0, color=C["fg"], stroke_width=4)
        rp_r2 = Arrow(RIGHT * 0.7, LEFT * 0.2, buff=0, color=C["fg"], stroke_width=4)
        rp_bar = Rectangle(width=1.4, height=0.14, stroke_width=0, fill_color=COL[0], fill_opacity=1)
        rp = VGroup(rp_r1.next_to(rp_bar, UP, buff=0.06).align_to(rp_bar, LEFT), rp_bar,
                    rp_r2.next_to(rp_bar, DOWN, buff=0.06).align_to(rp_bar, RIGHT))
        rpl = label("read pair: read 1 and read 2", 22, C["muted"])
        pair_g = self.place(VGroup(rp, rpl).arrange(DOWN, buff=0.15), "A2", "pair", span="2x1")
        with self.say("s16") as t:
            self.play(self.heading("sequencing"), Create(pool_box), Write(pool[1]), run_time=0.6)
            self.play(*[g.animate(path_arc=-PI / 3).scale(0.8).move_to(p) for g, p in zip(tagged_amps, spots)],
                      *[Uncreate(tb[0]) for tb in tubes], *[FadeOut(tb[1]) for tb in tubes], FadeOut(legend),
                      run_time=self.left(t, 0, "and the sequencer"))
            self.release("tubes", "legend")
            self.at(t, 0, "the sequencer")
            self.play(Create(seq), Write(seqg[1]), Write(mtitle), *[Create(r_[2]) for r_ in rows],
                      *[Write(r_[0]) for r_ in rows], *[GrowFromCenter(r_[1]) for r_ in rows], run_time=0.8)
            self.add(*fills)
            seen = []

            def draw(ks, total):
                for k in ks:                                  # each read reaches the sequencer as its sample's meter grows
                    cands = [i for i, g in enumerate(tagged_amps) if (i // 6) == k and i not in seen] or [k * 6]
                    j = cands[0]; seen.append(j)
                    f_ = tagged_amps[j].copy()
                    self.add(f_)
                    self.play(MoveAlongPath(f_, ArcBetweenPoints(f_.get_center(), seq.get_center(), angle=-PI / 3)),
                              trk[k].animate.increment_value(per[k]), run_time=max(total / len(ks), 0.15))
                    self.remove(f_)
            draw(plan[:8], self.left(t, 0))
            self.at(t, 1)
            self.play(Create(rp[1]), GrowArrow(rp[0]), GrowArrow(rp[2]), run_time=self.left(t, 1, "giving"))
            self.at(t, 1, "a read pair")
            self.play(Write(rpl), run_time=0.6)
            draw(plan[8:], self.left(t, 1) + 1.2)            # the last reads run on into the pause

        # s17: the meters hold; their name is the sequencing depth
        mt2 = label("sequencing depth: reads per sample", 24).move_to(mtitle, aligned_edge=LEFT)
        with self.say("s17") as t:
            self.play(self.heading("sequencing depth"), Transform(mtitle, mt2), run_time=self.left(t, 0))
            self.at(t, 1, "the deepest")
            self.play(Circumscribe(rows[0], color=C["fg"]), run_time=self.left(t, 1, "the shallowest"))
            self.at(t, 1, "the shallowest")
            self.play(Circumscribe(rows[2], color=C["fg"]), run_time=self.left(t, 1))
        self.play(FadeOut(VGroup(pool, *tagged_amps, meters, *fills, pair_g)), run_time=0.6)
        self.release("pool", "meters", "pair")

        # s18: reads sorted into bins by tag; one lands in the wrong bin
        bins_ = VGroup()
        for k, s in enumerate("ABC"):
            box = Rectangle(width=2.6, height=1.8).set_stroke(SAMPLE, width=3)
            head = VGroup(label(f"sample {s}", 24), index_tag(k)).arrange(RIGHT, buff=0.2).next_to(box, UP, buff=0.12)
            bins_.add(VGroup(box, head))
        bins_.arrange(RIGHT, buff=0.8)
        self.place(bins_, "A2", "bins", span="6x2")
        plan2 = [(k, k) for k in (0, 1, 2, 0, 1, 0, 0, 1)] + [(0, 1)]   # last read: sample A's, sorted into B
        reads, slots, fill_n = VGroup(), [], [0, 0, 0]
        for k, dest in plan2:
            reads.add(tagged(COL[int(rng.integers(0, 6))], k).scale(0.8).move_to(seq.get_center()))
            slots.append(bins_[dest][0].get_top() + DOWN * (0.3 + 0.36 * fill_n[dest]))
            fill_n[dest] += 1
        wrong = reads[-1]
        flag = label("misassigned (exaggerated here)", 22, C["muted"])
        with self.say("s18") as t:
            self.play(self.heading("demultiplexing"), LaggedStart(*[AnimationGroup(Create(b_[0]), Write(b_[1])) for b_ in bins_],
                                                                  lag_ratio=0.2), run_time=0.8)
            self.play(LaggedStart(*[MoveAlongPath(r, ArcBetweenPoints(r.get_center(), s, angle=PI / 4))
                                    for r, s in zip(reads[:-1], slots[:-1])], lag_ratio=0.25), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(MoveAlongPath(wrong, ArcBetweenPoints(wrong.get_center(), slots[-1], angle=PI / 4)),
                      run_time=self.left(t, 1, "about 2%"))
            flag.next_to(bins_[1][0], DOWN, buff=0.15)
            self.at(t, 1, "about 2%")
            self.play(Circumscribe(wrong, color=C["fg"]), Write(flag), run_time=self.left(t, 1))

        # s19 (distil): the three piles hold; a pile beside each bin shows its size
        piles = VGroup(*[Rectangle(width=0.4, height=max(1.6 * SKETCH_DEPTH[k], 0.03), stroke_width=0,
                                   fill_color=SAMPLE, fill_opacity=0.85).next_to(bins_[k][0], RIGHT, buff=0.12)
                         .align_to(bins_[k][0], DOWN) for k in range(3)])
        plabs = VGroup(*[label("reads", 18, C["muted"]).next_to(piles[k], DOWN, buff=0.08) for k in range(3)])
        with self.say("s19") as t:
            self.play(FadeOut(flag), FadeOut(seqg), run_time=0.5)
            self.release("seq")
            self.play(*[GrowFromEdge(p_, DOWN) for p_ in piles], Write(plabs), run_time=1.4)


class Reads(Chaptered):
    NUMBER, TITLE = 5, "From reads to a table"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(17)
        self.chapter()
        # s20: a read pair overlaps in the middle of the barcode; the two reads join into one merged read
        frag = Rectangle(width=6.0, height=0.26, stroke_width=0, fill_color=COL[0], fill_opacity=0.5)
        fl = label("barcode copy", 22, C["muted"]).next_to(frag, LEFT, buff=0.2)
        r1 = Arrow(LEFT * 2.0, RIGHT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, UP, buff=0.15).align_to(frag, LEFT)
        r2 = Arrow(RIGHT * 2.0, LEFT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, DOWN, buff=0.15).align_to(frag, RIGHT)
        rl = VGroup(label("read 1", 22, C["muted"]).next_to(r1, UP, buff=0.08),
                    label("read 2", 22, C["muted"]).next_to(r2, DOWN, buff=0.08))
        ov = Rectangle(width=2.0, height=1.1, stroke_width=0, fill_color=C["fg"], fill_opacity=0.1).move_to(frag)
        ovl = label("overlap", 20, C["muted"]).next_to(ov, UP, buff=0.05).shift(UP * 0.35)
        self.place(VGroup(fl, frag, r1, r2, rl, ov, ovl), "A1", "pair", span="6x2")
        merged = Rectangle(width=frag.width, height=frag.height, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(frag)
        ml = label("merged read", 24).next_to(merged, DOWN, buff=0.3)
        with self.say("s20") as t:
            self.play(self.heading("merging"), *self.tags("schematic"), run_time=0.5)
            self.play(Create(frag), Write(fl), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(GrowArrow(r1), GrowArrow(r2), Write(rl), run_time=self.left(t, 1, "overlap"))
            self.play(FadeIn(ov), Write(ovl), run_time=self.left(t, 1, "so they"))
            self.at(t, 1, "joined")
            self.play(ReplacementTransform(VGroup(r1, r2), merged), FadeOut(VGroup(rl, ov, ovl)), Write(ml),
                      run_time=self.left(t, 1))
        self.play(FadeOut(VGroup(fl, frag, merged, ml)), run_time=0.5)
        self.release("pair")

        # s20b: each barcode has an expected length; taxa differ by a few bases (the ends exaggerated)
        LENS, PER = (251, 253, 255), 0.3
        codes = VGroup(*[Rectangle(width=6.0 + (L - LENS[0]) * PER, height=0.26, stroke_width=0, fill_color=COL[k], fill_opacity=1)
                         for k, L in enumerate(LENS)]).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        ends = VGroup(*[label(f"{L} bases", 22, COL[k]).next_to(codes[k], RIGHT, buff=0.2) for k, L in enumerate(LENS)])
        x0, x1 = codes[0].get_right()[0] - 0.15, codes[2].get_right()[0] + 0.15
        band = Rectangle(width=x1 - x0, height=codes.height + 0.5, stroke_width=0, fill_color=C["fg"], fill_opacity=0.12) \
            .move_to([(x0 + x1) / 2, codes.get_center()[1], 0])
        bandl = label("expected length", 24).next_to(band, UP, buff=0.12)
        src = label("one V4 dataset (data): distinct sequences 251 to 255 bases", 22, C["muted"])
        note = label("ends exaggerated", 20, C["muted"])
        lens = self.place(VGroup(codes, ends, band, bandl), "A1", "lengths", span="6x3")
        self.place(VGroup(src, note).arrange(DOWN, buff=0.1), "A4", "lensrc", span="6x1")
        with self.say("s20b") as t:
            self.play(self.heading("filtering by length"), run_time=0.5)
            self.play(LaggedStart(*[GrowFromEdge(c, LEFT) for c in codes], lag_ratio=0.25), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(FadeIn(band), Write(bandl), run_time=self.left(t, 1, "and taxa"))
            self.play(*[Indicate(VGroup(c, ), color=C["fg"], scale_factor=1.02) for c in codes], Write(note),
                      run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(LaggedStart(*[Write(e) for e in ends], lag_ratio=0.3), Write(src), run_time=self.left(t, 2))
        self.play(FadeOut(VGroup(lens, src, note)), run_time=0.5)
        self.release("lengths", "lensrc")

        # s20c: quality fades toward a read's end, which is trimmed; off-target copies are much shorter or longer
        NSEG = 30
        qread = VGroup(*[Rectangle(width=7.2 / NSEG, height=0.3, stroke_width=0, fill_color=C["fg"],
                                   fill_opacity=1.0 if j < 18 else max(1.0 - (j - 17) * 0.075, 0.12))
                         for j in range(NSEG)]).arrange(RIGHT, buff=0)
        ql = label("one read, coloured by quality", 22, C["muted"]).next_to(qread, UP, buff=0.15).align_to(qread, LEFT)
        cut_at = qread[22].get_left()[0]
        snip = DashedLine([cut_at, qread.get_bottom()[1] - 0.25, 0], [cut_at, qread.get_top()[1] + 0.25, 0],
                          color=C["fg"], dash_length=0.08, stroke_width=3)
        tl_ = label("trimmed: low quality", 22).next_to(snip, RIGHT, buff=0.2).shift(DOWN * 0.55)
        top = self.place(VGroup(ql, qread, snip, tl_), "A1", "quality", span="6x2")
        ref = Rectangle(width=4.0, height=0.22, stroke_width=0, fill_color=COL[0], fill_opacity=1)
        refl = label("barcode", 22, C["muted"]).next_to(ref, LEFT, buff=0.2)
        other = Rectangle(width=9.0, height=0.22, stroke_width=0, fill_color=C["muted"], fill_opacity=0.5)
        otl = label("other DNA", 22, C["muted"]).next_to(other, LEFT, buff=0.2)
        offs = VGroup(Rectangle(width=1.6, height=0.22, stroke_width=0, fill_color=C["muted"], fill_opacity=1),
                      Rectangle(width=6.2, height=0.22, stroke_width=0, fill_color=C["muted"], fill_opacity=1))
        offs.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        lower = VGroup(VGroup(refl, ref), VGroup(otl, other), offs).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        lower[0].shift(UP * 0.5)                               # room for the primer above the other DNA
        prim = Arrow(UP * 0.5, DOWN * 0.05, buff=0, color=C["fg"], stroke_width=5).next_to(other, UP, buff=0.04) \
            .align_to(other, LEFT).shift(RIGHT * 1.5)
        offs.align_to(prim, LEFT)
        offl = label("off-target copies", 22).next_to(offs, RIGHT, buff=0.3)
        primel = label("primer", 20, C["muted"]).next_to(prim, RIGHT, buff=0.1)
        self.place(VGroup(lower, offl, prim, primel), "A3", "offtarget", span="6x2")
        with self.say("s20c") as t:
            self.play(Write(ql), LaggedStart(*[GrowFromEdge(q_, LEFT) for q_ in qread], lag_ratio=0.05),
                      run_time=self.left(t, 0, "quality tends"))
            self.play(Indicate(VGroup(*qread[18:]), color=C["muted"], scale_factor=1.0), run_time=self.left(t, 0, "which is"))
            self.play(Create(snip), run_time=0.5)
            self.play(VGroup(*qread[22:]).animate.shift(RIGHT * 0.6).set_opacity(0.05), Write(tl_), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(GrowFromEdge(ref, LEFT), Write(refl), GrowFromEdge(other, LEFT), Write(otl), run_time=1.0)
            self.play(GrowArrow(prim), Write(primel), run_time=self.left(t, 1, "can make"))
            self.play(LaggedStart(*[GrowFromEdge(o, LEFT) for o in offs], lag_ratio=0.4), Write(offl), run_time=self.left(t, 1))
        self.play(FadeOut(VGroup(top, lower, offl, prim, primel)), run_time=0.5)
        self.release("quality", "offtarget")

        # s20d: read lengths as a histogram (illustrative): the finding (peak, tail, bump), then the axes
        lengths = np.r_[rng.normal(253, 2.0, 1500), rng.uniform(150, 246, 500), rng.normal(300, 4, 120)]
        BW = 5
        edges = np.arange(140, 322, BW)
        cnt, _ = np.histogram(lengths, edges)
        YM = float(cnt.max()) * 1.1
        ax = Axes(x_range=[140, 320, 20], y_range=[0, YM, YM], x_length=9.6, y_length=3.0, tips=False,
                  axis_config=dict(color=C["muted"], include_ticks=False))
        hb = VGroup(*[Rectangle(width=ax.x_length * BW / 180 * 0.9, height=max(ax.y_length * c / YM, 0.002),
                                stroke_width=0, fill_color=SAMPLE, fill_opacity=0.8).move_to(ax.c2p(e + BW / 2, 0), aligned_edge=DOWN)
                      for e, c in zip(edges[:-1], cnt)])
        xt = VGroup(*[label(str(v), 20, C["muted"]).next_to(ax.c2p(v, 0), DOWN, buff=0.15) for v in (150, 200, 250, 300)])
        xtt = label("read length (bases)", 22, C["muted"]).next_to(xt, DOWN, buff=0.1)
        ytt = label("number of reads", 22, C["muted"]).rotate(PI / 2).next_to(ax, LEFT, buff=0.2)
        peak_l = label("expected length", 22).next_to(ax.c2p(250, YM * 0.92), LEFT, buff=0.25)
        tail_l = label("short tail", 22, C["muted"]).next_to(ax.c2p(195, YM * 0.12), UP, buff=0.15)
        bump_l = label("off-target", 22, C["muted"]).next_to(ax.c2p(300, YM * 0.2), UP, buff=0.15)
        hist = self.place(VGroup(ax, hb, xt, xtt, ytt, peak_l, tail_l, bump_l), "A1", "hist", span="6x3")
        is_peak = lambda e: 240 <= e < 270
        with self.say("s20d") as t:
            self.play(Create(ax.x_axis), *self.tags("illustrative"), run_time=0.6)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in hb], lag_ratio=0.03), run_time=self.left(t, 1, "most reads"))
            self.at(t, 1, "expected")
            self.play(Write(peak_l), Indicate(VGroup(*[r for r, e in zip(hb, edges[:-1]) if is_peak(e)]), color=C["fg"]),
                      run_time=self.left(t, 1, "with a tail"))
            self.at(t, 1, "tail")
            self.play(Write(tail_l), Write(bump_l), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Write(xt), Write(xtt), run_time=self.left(t, 2, "and the number"))
            self.play(Create(ax.y_axis), Write(ytt), run_time=self.left(t, 2))

        # s20e: two cut-offs, a judgement; the same for every sample; too strict or too loose
        def vline(x_, h_=YM):
            return DashedLine(ax.c2p(x_, 0), ax.c2p(x_, h_), color=C["fg"], dash_length=0.1, stroke_width=3)
        LO, HI = 240, 270
        lo, hi = vline(LO), vline(HI)
        cutl = label("cut-offs", 22).next_to(VGroup(lo, hi), UP, buff=0.1)
        outside = lambda e, a=LO, b=HI: e + BW <= a or e >= b
        dropl = label("dropped", 22, C["muted"]).next_to(ax.c2p(170, YM * 0.32), UP, buff=0)
        judge = label("set by eye, with judgement", 22, C["muted"]).next_to(cutl, RIGHT, buff=0.6)
        with self.say("s20e") as t:
            self.play(Create(lo), Create(hi), Write(cutl), run_time=1.0)
            self.play(*[r.animate.set_opacity(0.15) for r, e in zip(hb, edges[:-1]) if outside(e)],
                      FadeOut(VGroup(tail_l, bump_l)), Write(dropl), Write(judge), run_time=self.left(t, 0))
            # every sample gets the same two lines
            self.at(t, 1)
            big = VGroup(ax, hb, xt, xtt, ytt, peak_l, lo, hi, cutl, dropl, judge)
            minis = VGroup()
            for k, (ntail, npk) in enumerate(((500, 1500), (300, 1100), (700, 900))):
                Lk = np.r_[rng.normal(253, 2.0, npk), rng.uniform(150, 246, ntail), rng.normal(300, 4, 60)]
                ck, _ = np.histogram(Lk, edges)
                g = VGroup(*[Rectangle(width=3.4 * BW / 180 * 0.9, height=max(1.3 * c / YM, 0.002), stroke_width=0,
                                       fill_color=SAMPLE, fill_opacity=0.15 if outside(e) else 0.8)
                             .move_to([-1.7 + 3.4 * (e + BW / 2 - 140) / 180, 0, 0], aligned_edge=DOWN)
                             for e, c in zip(edges[:-1], ck)])
                base = Line([-1.7, 0, 0], [1.7, 0, 0], color=C["muted"], stroke_width=2)
                nm = VGroup(label(f"sample {'ABC'[k]}", 20), index_tag(k)).arrange(RIGHT, buff=0.12).next_to(base, DOWN, buff=0.15)
                minis.add(VGroup(base, g, nm))
            minis.arrange(RIGHT, buff=0.6, aligned_edge=DOWN)
            self.place(minis, "A4", "minis", span="6x1")
            self.play(big.animate.scale(0.72).to_edge(UP, buff=0.7), run_time=0.8)
            lines_ = VGroup()
            for m in minis:
                x_lo = m[0].get_left()[0] + (LO - 140) / 180 * m[0].width
                x_hi = m[0].get_left()[0] + (HI - 140) / 180 * m[0].width
                lines_.add(*[DashedLine([x_, m[0].get_y(), 0], [x_, m[0].get_y() + max(m[1].height, 0.5) * 1.05, 0],
                                        color=C["fg"], dash_length=0.06, stroke_width=2) for x_ in (x_lo, x_hi)])
            self.play(LaggedStart(*[Create(VGroup(m[0], m[2])) for m in minis], lag_ratio=0.2),
                      LaggedStart(*[GrowFromEdge(m[1], DOWN) for m in minis], lag_ratio=0.2), run_time=1.2)
            self.play(LaggedStart(*[TransformFromCopy(VGroup(lo, hi), VGroup(lines_[2 * k], lines_[2 * k + 1])) for k in range(3)],
                                  lag_ratio=0.25), run_time=self.left(t, 1))
            # too strict, then too loose, on the big histogram
            self.at(t, 2)
            strict = label("too strict: real reads lost", 22).move_to(judge, aligned_edge=LEFT)
            loose = label("too loose: faulty reads kept", 22).move_to(judge, aligned_edge=LEFT)
            hb_e = list(zip(hb, edges[:-1]))
            self.play(lo.animate.move_to(ax.c2p(252, YM / 2)), FadeTransform(judge, strict), FadeOut(dropl),
                      *[r.animate.set_opacity(0.15) for r, e in hb_e if 240 <= e < 252], run_time=self.left(t, 2, "too loose"))
            self.at(t, 2, "too loose")
            self.play(lo.animate.move_to(ax.c2p(160, YM / 2)), FadeTransform(strict, loose),
                      *[r.animate.set_opacity(0.8) for r, e in hb_e if 160 <= e < 252], run_time=self.left(t, 2))
        self.play(lo.animate.move_to(ax.c2p(LO, YM / 2)), FadeOut(loose),
                  *[r.animate.set_opacity(0.15) for r, e in hb_e if 160 <= e < LO], run_time=0.8)
        self.play(FadeOut(VGroup(*[m_ for m_ in big if m_ is not dropl], minis, lines_)), run_time=0.5)
        self.release("hist", "minis")

        # s21: near-copies with errors fold into one exact sequence, an ASV
        true_seq = "TACGGAGGGTGCAAGCGTTA"
        variants = []
        for _ in range(7):
            s = list(true_seq)
            for j in rng.choice(len(s), int(rng.integers(1, 3)), replace=False):
                s[j] = str(rng.choice([c for c in "ACGT" if c != s[j]]))
            variants.append(s)

        def seq_text(s, colour):
            g = VGroup(*[label(ch_, 24, colour if ch_ == true_seq[j] else C["fg"], font=MONO,
                               weight=NORMAL if ch_ == true_seq[j] else BOLD) for j, ch_ in enumerate(s)])
            g.arrange(RIGHT, buff=0.04)
            for j, ch_ in enumerate(s):
                if ch_ != true_seq[j]:
                    g[j].add(Underline(g[j], color=C["fg"], buff=0.02))
            return g
        cloud = VGroup(*[seq_text(v, COL[0]) for v in variants]).arrange(DOWN, buff=0.12)
        ctitle = label("reads of one real sequence", 22, C["muted"]).next_to(cloud, UP, buff=0.2)
        asv = seq_text(list(true_seq), COL[0])
        self.place(VGroup(ctitle, cloud), "A1", "cloud", span="3x3")
        asv_l = label("ASV: amplicon sequence variant", 28, weight=BOLD)
        legend = label("white, underlined: sequencing errors", 26, C["muted"])
        legend2 = label("one exact sequence: the ASV", 26, C["muted"])
        side = VGroup(legend,
                      VGroup(label("one soil dataset:", 26, C["muted"]),
                             label("8,270 to 16,609 ASVs, by pipeline", 26, C["muted"])).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.place(side, "D1", "side", span="3x3")
        legend2.move_to(legend, aligned_edge=LEFT)
        with self.say("s21") as t:
            self.play(self.heading("denoising"), *self.tags("schematic"), run_time=0.5)
            self.play(Write(ctitle), LaggedStart(*[Write(v) for v in cloud], lag_ratio=0.15), Write(legend), run_time=self.left(t, 0))
            self.at(t, 1)
            asv.move_to(cloud)
            self.play(ReplacementTransform(cloud, asv), FadeOut(ctitle), TransformMatchingShapes(legend, legend2),
                      run_time=self.left(t, 1, "called"))
            asv_l.next_to(asv, UP, buff=0.25)
            self.play(Write(asv_l), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Write(side[1]), run_time=self.left(t, 2))
        self.play(FadeOut(VGroup(asv, asv_l, legend2, side[1])), run_time=0.6)
        self.release("cloud", "side")

        # s22: a chimera: a copy starts on one template and finishes on another; a detector catches some
        ta = Rectangle(width=5.0, height=0.26, stroke_width=0, fill_color=COL[0], fill_opacity=1)
        tb = Rectangle(width=5.0, height=0.26, stroke_width=0, fill_color=COL[1], fill_opacity=1)
        temps = VGroup(ta, tb).arrange(DOWN, buff=0.9)
        tl = VGroup(label("template, taxon 1", 20, C["muted"]).next_to(ta, LEFT, buff=0.2),
                    label("template, taxon 2", 20, C["muted"]).next_to(tb, LEFT, buff=0.2))
        self.place(VGroup(temps, tl), "A1", "temps", span="4x2")
        h1 = Rectangle(width=2.5, height=0.2, stroke_width=0, fill_color=COL[0], fill_opacity=1) \
            .next_to(ta, DOWN, buff=0.12).align_to(ta, LEFT)
        h2 = Rectangle(width=2.5, height=0.2, stroke_width=0, fill_color=COL[1], fill_opacity=1) \
            .next_to(tb, UP, buff=0.12).align_to(tb, RIGHT)
        chim = VGroup(Rectangle(width=2.5, height=0.26, stroke_width=0, fill_color=COL[0], fill_opacity=1),
                      Rectangle(width=2.5, height=0.26, stroke_width=0, fill_color=COL[1], fill_opacity=1)).arrange(RIGHT, buff=0)
        cl = label("chimera", 26)
        self.place(VGroup(chim, cl).arrange(DOWN, buff=0.15), "E1", "chimera", span="2x2")
        many = VGroup(*[chim.copy().scale(0.35) for _ in range(5)]).arrange(RIGHT, buff=0.3)
        caught = [0, 1, 3]
        dl = label("detector:", 24, C["muted"]).next_to(many, LEFT, buff=0.3)
        dk = label("crossed: caught;  plain: missed", 22, C["muted"]).next_to(many, RIGHT, buff=0.4)
        self.place(VGroup(dl, many, dk), "A3", "detector", span="6x1")
        with self.say("s22") as t:
            self.play(self.heading("chimeras"), run_time=0.5)
            self.play(GrowFromEdge(ta, LEFT), GrowFromEdge(tb, LEFT), Write(tl), run_time=0.8)
            self.play(GrowFromEdge(h1, LEFT), run_time=self.left(t, 0, "into one"))
            self.play(h1.animate(path_arc=PI / 4).next_to(h2, LEFT, buff=0), GrowFromEdge(h2, LEFT), run_time=self.left(t, 0, "a chimera"))
            self.at(t, 0, "a chimera")
            self.play(ReplacementTransform(VGroup(h1, h2), chim), Write(cl), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Write(dl), LaggedStart(*[TransformFromCopy(chim, m) for m in many], lag_ratio=0.15), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(*[Create(Cross(Square(side_length=0.45).move_to(many[j]), stroke_color=C["fg"], stroke_width=4))
                        for j in caught], Write(dk), run_time=self.left(t, 2))
        self.play(*[FadeOut(m) for m in self.mobjects if m is not getattr(self, "_tag", None)], run_time=0.6)
        self.release("temps", "chimera", "detector")

        # s23: classify against a reference database, then count into a table of taxa by samples
        q = label("TACGGAGGGT…", 22, COL[0], font=MONO)
        ql = label("ASV", 22).next_to(q, UP, buff=0.1)
        shelf = VGroup(*[Rectangle(width=2.2, height=0.16, stroke_width=0, fill_color=C["muted"], fill_opacity=0.6)
                         for _ in range(7)]).arrange(DOWN, buff=0.08)
        shl = label("reference database", 22, C["muted"]).next_to(shelf, UP, buff=0.12)
        ref = VGroup(shelf, shl)
        named = label("→ taxon 1", 24, COL[0])
        left = self.place(VGroup(VGroup(q, ql), ref).arrange(RIGHT, buff=0.9), "A1", "classify", span="3x2")
        named.next_to(left, DOWN, buff=0.3)
        cols_ = VGroup(*[VGroup(label(s, 24), index_tag(k)).arrange(DOWN, buff=0.08) for k, s in enumerate("ABC")])
        rows_ = VGroup(*[Square(side_length=0.22, stroke_width=0, fill_color=COL[i], fill_opacity=1) for i in range(6)])
        cells_ = VGroup()
        for i in range(6):
            for k in range(3):
                v = float(D["pool"][i] / D["pool"][0]) * SKETCH_DEPTH[k] * rng.uniform(0.7, 1.0)
                cells_.add(Rectangle(width=max(1.1 * v, 0.04), height=0.18, stroke_width=0, fill_color=SAMPLE, fill_opacity=0.8))
        for k, c in enumerate(cols_):
            c.move_to([0.9 + k * 1.5, 0.6, 0])
        for i, r in enumerate(rows_):
            r.move_to([0, -i * 0.42, 0])
            for k in range(3):
                cells_[i * 3 + k].move_to([0.35 + k * 1.5, -i * 0.42, 0], aligned_edge=LEFT)
        more = label("…", 28, C["muted"]).move_to([0, -6 * 0.42, 0])
        table = VGroup(cols_, rows_, cells_, more)
        tt = label("count table: taxa by samples", 24, C["muted"]).next_to(table, UP, buff=0.25)
        self.place(VGroup(table, tt), "D1", "table", span="3x3")
        with self.say("s23") as t:
            self.play(self.heading("naming and counting"), run_time=0.5)
            self.play(Write(VGroup(q, ql)), Write(shl), LaggedStart(*[GrowFromEdge(r, LEFT) for r in shelf], lag_ratio=0.08),
                      run_time=self.left(t, 0, "matching"))
            arr = Arrow(q.get_right(), shelf.get_left(), buff=0.1, color=C["muted"], stroke_width=3)
            cls = label("classifier: best match", 20, C["muted"]).next_to(q, DOWN, buff=0.15)
            self.at(t, 0, "matching")
            self.play(GrowArrow(arr), Write(cls), run_time=0.8)
            self.track(VGroup(arr, cls), "classifier")
            self.play(Indicate(shelf[2], color=C["fg"], scale_factor=1.1), Write(named), run_time=self.left(t, 0))
            self.track(named, "named")
            self.at(t, 1)
            self.play(Write(tt), Write(cols_), LaggedStart(*[GrowFromCenter(r) for r in rows_], lag_ratio=0.1), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(c, LEFT) for c in cells_], lag_ratio=0.05), Write(more), run_time=self.left(t, 1))

        # s24 (distil): the table holds; its title says what it counts
        tt2 = label("count table: reads per taxon, not cells", 24).move_to(tt)
        key5 = VGroup(VMobject(), label("our simulation leaves out the false taxa these steps can add", 24, C["muted"]))
        self.place(key5, "A4", "key5", span="6x1")
        with self.say("s24") as t:
            self.play(self.heading("the count table"), run_time=0.5)
            self.play(Transform(tt, tt2), Indicate(cells_, color=C["fg"], scale_factor=1.03), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(Write(key5[1]), run_time=0.6)
            self.track(key5[1], "sim")


class Depth(Chaptered):
    NUMBER, TITLE = 6, "Depth"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(9)
        self.chapter()
        # s25: which taxa turn up at three depths, drawn from the deepest down
        deps = sorted(P.DEPTHS, reverse=True)
        icon = soil_icon()
        texts = VGroup(*[label(f"{dep:,} reads: {int((D['runs'][dep] > 0).sum())} of {N} taxa", 28) for dep in deps])
        strips = VGroup(*[strip(D["runs"][dep] > 0) for dep in deps])
        for k in range(3):
            texts[k].move_to([0, -k * 1.2, 0], aligned_edge=RIGHT)
            strips[k].move_to([0.5, -k * 1.2, 0], aligned_edge=LEFT)
        grid = self.place(VGroup(texts, strips), "A1", "rows", span="6x3")
        key = self.place(VGroup(label("filled: found    dim outline: missed", 24, C["muted"]),
                                label("taxa in the order of their cell counts", 20, C["muted"])).arrange(DOWN, buff=0.08),
                         "A4", "key", span="6x1")
        with self.say("s25") as t:
            self.play(self.heading("three depths"), run_time=0.5)
            self.play(DrawBorderThenFill(icon), Write(key), *self.tags("simulated"), run_time=self.left(t, 0))
            self.track(icon, "icon")
            for k in range(3):
                self.at(t, k + 1)
                self.play(Write(texts[k]), LaggedStart(*[Create(sq) for sq in strips[k]], lag_ratio=0.01), run_time=self.left(t, k + 1))

        # s26: the empty slots at 500 reads are the low-abundance taxa
        shallow = strips[2]
        missed = [i for i in range(N) if D["runs"][min(P.DEPTHS)][i] == 0]
        note = label("missed at 500 reads: low-abundance taxa, too few barcodes to be picked", 24).move_to(key)
        with self.say("s26") as t:
            self.play(self.heading("missed taxa"), run_time=0.5)
            self.play(Transform(key, note), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(LaggedStart(*[Indicate(shallow[i], color=C["fg"], scale_factor=1.8) for i in missed[:24]],
                                  lag_ratio=0.05), run_time=self.left(t, 1))
        self.play(FadeOut(VGroup(grid, key, icon)), run_time=0.6)
        self.release("rows", "key", "icon")

        # s27: 30 repeat sequencings per depth: a share's spread narrows with depth, centred on the pool's share
        REP = 30
        draws = {idx: [rng.binomial(dep, D["pool"][idx], REP) / dep for dep in P.DEPTHS] for idx in (0, 40)}

        def panel(idx, ymax, title, colour, fmt):
            ax = Axes(x_range=[0, 4, 1], y_range=[0, ymax, ymax / 2], x_length=4.6, y_length=3.0, tips=False,
                      axis_config=dict(color=C["muted"], include_ticks=False))
            ref = DashedLine(ax.c2p(0.3, D["pool"][idx]), ax.c2p(3.7, D["pool"][idx]), color=C["fg"], dash_length=0.1)
            dots = VGroup()
            for k, dep in enumerate(P.DEPTHS):
                for s in draws[idx][k]:
                    dots.add(Dot(ax.c2p(k + 1 + rng.uniform(-0.18, 0.18), s), radius=0.05, color=colour, fill_opacity=0.55))
            xs = VGroup(*[label(f"{dep:,}", 20, C["muted"]).next_to(ax.c2p(k + 1, 0), DOWN, buff=0.15) for k, dep in enumerate(P.DEPTHS)])
            ys = VGroup(*[label(fmt(v), 20, C["muted"]).next_to(ax.c2p(0, v), LEFT, buff=0.12) for v in (ymax / 2, ymax)])
            ttl = label(title, 24, colour).next_to(ax, UP, buff=0.25)
            xtl = label("reads per sample", 20, C["muted"]).next_to(xs, DOWN, buff=0.1)
            ytl = label("share of reads", 20, C["muted"]).rotate(PI / 2).next_to(ys, LEFT, buff=0.12)
            return VGroup(ax, ref, xs, ys, ttl, xtl, ytl), dots
        low = 40
        p1, d1 = panel(0, 0.6, "taxon 1, abundant", COL[0], lambda v: f"{v:.0%}")
        ymax2 = float(np.ceil(max(x.max() for x in draws[low]) * 1.1 * 1000) / 1000)   # covers every draw
        p2, d2 = panel(low, ymax2, f"taxon {low + 1}, low-abundance (note the smaller scale)", C["muted"], lambda v: f"{v:.1%}")
        self.place(VGroup(p1, d1), "A1", "p1", span="3x3")
        self.place(VGroup(p2, d2), "D1", "p2", span="3x3")
        key2 = self.place(VGroup(label("more reads: a tighter spread, the same centre", 26),
                                 label(f"each dot: one of {REP} repeat sequencings;  dashed: share of the barcode pool", 22, C["muted"]))
                          .arrange(DOWN, buff=0.12), "A4", "key2", span="6x1")
        with self.say("s27") as t:
            self.play(self.heading("repeat sequencing"), run_time=0.5)
            self.play(Create(p1[0]), Create(p2[0]), Create(p1[1]), Create(p2[1]), Write(VGroup(*p1[2:], *p2[2:])),
                      Write(key2[1]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(LaggedStart(*[GrowFromCenter(x) for x in d1], lag_ratio=0.01), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(LaggedStart(*[GrowFromCenter(x) for x in d2], lag_ratio=0.01), run_time=self.left(t, 2))
            self.at(t, 3)
            self.play(Write(key2[0]), run_time=self.left(t, 3))

        # s28 (distil): the three counts, deepest to shallowest
        summary = VGroup(*[label(f"{dep:,} reads → {int((D['runs'][dep] > 0).sum())} taxa", 34) for dep in deps]
                         ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        head = label("fewer reads, fewer taxa found", 30, weight=BOLD)
        with self.say("s28") as t:
            self.play(self.heading("fewer reads, fewer taxa"), run_time=0.5)
            self.play(FadeOut(VGroup(p1, d1, p2, d2, key2)), run_time=0.6)
            self.release("p1", "p2", "key2")
            self.place(VGroup(head, summary).arrange(DOWN, aligned_edge=LEFT, buff=0.5), "B1", "summary", span="4x3")
            self.play(Write(head), run_time=0.5)
            for x_ in summary:
                self.play(Write(x_), run_time=0.5)
                self.wait(max((t.duration - 2.6) / 3 - 0.5, 0.2))


class Rarefy(Chaptered):
    NUMBER, TITLE = 7, "Rarefaction"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(21)
        self.chapter()
        # s29: two samples from the same soil (white: a sample is not a taxon)
        def card(name, counts):
            head = label(f"{name} sample: {int(counts.sum()):,} reads", 28)
            n = label(f"{int((counts > 0).sum())} taxa found", 34, weight=BOLD)
            VGroup(head, n).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            st = strip(counts > 0, colour=SAMPLE).next_to(VGroup(head, n), RIGHT, buff=0.7)
            return VGroup(head, st, n)
        icon = soil_icon()
        title = self.place(VGroup(label("same soil, two samples, each its own draw", 30, C["muted"]),
                                  label("richness = number of taxa found;  filled: found, dim outline: missed", 22, C["muted"]))
                           .arrange(DOWN, buff=0.12), "A1", "title", span="6x1")
        deep_c, shal_c = card("deep", D["deep"]), card("shallow", D["shallow"])
        deep = self.place(deep_c, "A2", "deep", span="6x1")
        shal = self.place(shal_c, "A3", "shallow", span="6x1")
        shal_c[1].align_to(deep_c[1], LEFT)
        VGroup(shal_c[0], shal_c[2]).align_to(deep_c[0], LEFT)
        with self.say("s29") as t:
            self.play(self.heading("two samples"), run_time=0.5)
            self.play(Write(title), DrawBorderThenFill(icon), *self.tags("simulated"), run_time=self.left(t, 0))
            self.track(icon, "icon")
            for k, c in enumerate((deep_c, shal_c), start=1):
                self.at(t, k)
                self.play(Write(c[0]), LaggedStart(*[Create(sq) for sq in c[1]], lag_ratio=0.01), run_time=self.left(t, k, "and shows"))
                self.at(t, k, "and shows")
                self.play(Write(c[2]), run_time=self.left(t, k))

        # s30: rarefying: the deep sample drawn down to 2,000 reads at random; the rest set aside
        one = P.rarefy(D["deep"], P.SHALLOW, rng) > 0
        lost = [i for i in range(N) if D["deep"][i] > 0 and not one[i]]
        head2 = label(f"deep, rarefied: {P.SHALLOW:,} reads", 28).move_to(deep_c[0], aligned_edge=LEFT)
        aside = label(f"{P.DEEP - P.SHALLOW:,} reads set aside", 24, C["muted"]).move_to(deep_c[2], aligned_edge=LEFT)
        with self.say("s30") as t:
            self.play(self.heading("rarefying"), run_time=0.5)
            self.play(Transform(deep_c[0], head2), run_time=self.left(t, 0, "and sets"))
            self.at(t, 0, "and sets")
            self.play(*[deep_c[1][i].animate.set_fill(opacity=0).set_stroke(C["rule"]) for i in lost],
                      FadeOut(deep_c[2], shift=DOWN * 0.2), Write(aside), run_time=self.left(t, 0))
            self.track(aside, "aside")
            self.at(t, 1)
            self.play(Indicate(deep_c[0], color=C["fg"]), Indicate(shal_c[0], color=C["fg"]), run_time=self.left(t, 1))

        # s31: rarefaction: the draw repeats 200 times; each result drops into a histogram
        lo, hi = int(D["rare_draws"].min()), int(D["rare_draws"].max())
        vals, cnts = np.unique(D["rare_draws"], return_counts=True)
        ymax = int(np.ceil(cnts.max() / 10) * 10)
        ax = Axes(x_range=[lo - 1, hi + 1, 2], y_range=[0, ymax, ymax / 2], x_length=9.0, y_length=2.6, tips=False,
                  axis_config=dict(color=C["muted"], include_ticks=False))
        hist = VGroup(*[Rectangle(width=ax.x_length / (hi - lo + 2) * 0.85, height=ax.y_length * c / ymax, stroke_width=0,
                                  fill_color=SAMPLE, fill_opacity=0.75).move_to(ax.c2p(v, 0), aligned_edge=DOWN)
                        for v, c in zip(vals, cnts)])
        x0, x1 = ax.c2p(D["rare_lo"] - 0.5, 0)[0], ax.c2p(D["rare_hi"] + 0.5, 0)[0]
        band = Rectangle(width=x1 - x0, height=ax.y_length, stroke_width=0, fill_color=C["fg"], fill_opacity=0.08) \
            .move_to([(x0 + x1) / 2, ax.c2p(0, ymax / 2)[1], 0])
        blab = label(f"middle 95%: {D['rare_lo']} to {D['rare_hi']}", 20, C["muted"]).next_to(band, UP, buff=0.08).align_to(band, LEFT)
        mark = DashedLine(ax.c2p(D["obs_shallow"], 0), ax.c2p(D["obs_shallow"], ymax), color=SAMPLE, dash_length=0.08, stroke_width=4)
        mlab = label(f"shallow sample: {D['obs_shallow']}", 22).next_to(mark, UP, buff=0.45)
        xt = VGroup(*[label(str(v), 20, C["muted"]).next_to(ax.c2p(v, 0), DOWN, buff=0.18) for v in range(lo + lo % 2, hi + 1, 2)])
        mean = Triangle(fill_color=SAMPLE, fill_opacity=1, stroke_width=0).scale(0.1) \
            .move_to([ax.c2p(D["rare_mean"], 0)[0], xt.get_bottom()[1] - 0.3, 0])
        mean_l = label(f"average {round(D['rare_mean'])}", 20).next_to(mean, RIGHT, buff=0.1)
        xtitle = label("taxa found in each subsample", 22, C["muted"]).next_to(mean, DOWN, buff=0.15).set_x(ax.get_center()[0])
        ylab = label("subsamples", 20, C["muted"]).rotate(PI / 2).next_to(ax, LEFT, buff=0.2)
        hgroup = self.place(VGroup(band, blab, ax, hist, mark, mlab, mean, mean_l, xt, xtitle, ylab), "A2", "hist", span="6x3")
        htxt = self.place(label(f"rarefaction: the draw repeated {P.DRAWS} times, {round(D['rare_mean'])} taxa on average", 28),
                          "A1", "htxt", span="6x1")
        with self.say("s31") as t:
            self.play(self.heading("rarefaction"), run_time=0.5)
            self.play(FadeOut(VGroup(deep, shal, title, aside)), run_time=0.6)
            self.release("deep", "shallow", "title", "aside")
            self.play(Write(htxt), Create(ax), Write(xt), Write(xtitle), Write(ylab), run_time=1.0)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in hist], lag_ratio=0.08), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(GrowFromCenter(mean), Write(mean_l), run_time=self.left(t, 1, "and the middle"))
            self.at(t, 1, "the middle")
            self.play(GrowFromEdge(band, DOWN), Write(blab), run_time=self.left(t, 1))
            self.at(t, 2)
            self.play(Create(mark), Write(mlab), run_time=self.left(t, 2))

        # s32: what rarefying does not fix, shown on the pictures it is about
        bc = chart(D["pool"], "share of barcodes", xlab="taxa", **CHART)
        bias_g = self.place(bc, "A1", "biaschart", span="3x2")
        ab = Arrow(bc[2][0].get_top() + RIGHT * 1.6 + DOWN * 0.5, bc[2][0].get_top() + RIGHT * 0.1, buff=0, color=C["fg"], stroke_width=4)
        abl = label("bias: still in every read", 24).next_to(ab.get_start(), RIGHT, buff=0.1)
        sh_t = label("shallow sample", 24, C["muted"])
        sh_s = strip(D["shallow"] > 0, colour=SAMPLE)
        sh = self.place(VGroup(sh_t, sh_s).arrange(DOWN, aligned_edge=LEFT, buff=0.2), "D1", "shallowstrip", span="3x2")
        missed = [i for i in range(N) if D["shallow"][i] == 0]
        ml_ = label("missed taxa: still missed", 24).next_to(sh, DOWN, buff=0.3)
        with self.say("s32") as t:
            self.play(self.heading("what rarefying does not fix"), FadeOut(VGroup(hgroup, htxt)), *self.tags("summary"), run_time=0.6)
            self.release("hist", "htxt")
            self.play(draw_chart(bc, 1.2), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(GrowArrow(ab), Write(abl), run_time=self.left(t, 1, "are in every"))
            self.at(t, 1, "every read")
            self.play(Indicate(bc[2], color=C["fg"], scale_factor=1.03), run_time=self.left(t, 1))
            self.track(VGroup(ab, abl), "biasl")
            self.at(t, 2)
            self.play(Write(sh_t), LaggedStart(*[Create(sq) for sq in sh_s], lag_ratio=0.01), run_time=self.left(t, 2, "stay missed"))
            self.at(t, 2, "stay missed")
            self.play(LaggedStart(*[Indicate(sh_s[i], color=C["fg"], scale_factor=1.8) for i in missed], lag_ratio=0.05),
                      Write(ml_), run_time=self.left(t, 2))
            self.track(ml_, "missedl")

        # s33: shares cannot show total cells: a crowded soil and a sparse one give the same shares
        rng = np.random.default_rng(3)
        def soil_with(n):
            drop = Circle(radius=1.1).set_stroke(SOIL, width=3).set_fill(SOIL, opacity=0.45)
            pick = rng.choice(N, size=n, p=D["true"])
            cs = VGroup(*[cell(i, rng).move_to(drop.get_center() + 0.9 * np.sqrt(rng.uniform()) *
                                                np.array([np.cos(a), np.sin(a), 0])) for i, a in zip(pick, rng.uniform(0, TAU, n))])
            return VGroup(drop, cs)
        rich, poor = soil_with(90), soil_with(9)
        rl = label("soil 1: many cells", 22, C["muted"]).next_to(rich, DOWN, buff=0.1)
        pl = label("soil 2: few cells", 22, C["muted"]).next_to(poor, DOWN, buff=0.1)
        soils = VGroup(VGroup(rich, rl), VGroup(poor, pl)).arrange(DOWN, buff=0.4)
        c1 = chart(D["true"], "shares", xlab="", **CHART).scale(0.45)
        c2 = chart(D["true"], "shares", xlab="", **CHART).scale(0.45)
        charts_ = VGroup(c1, c2).arrange(DOWN, buff=0.5)
        row = VGroup(soils, charts_).arrange(RIGHT, buff=2.2)
        self.place(row, "A1", "twosoils", span="6x3")
        arrs = VGroup(*[Arrow(s_.get_right(), c_.get_left(), buff=0.3, color=C["muted"], stroke_width=3)
                        for s_, c_ in ((rich, c1), (poor, c2))])
        same = label("same shares", 26, weight=BOLD).next_to(charts_, RIGHT, buff=0.3)
        tot = self.place(label("total cells: measured by spike-ins or cell counts", 26), "A4", "total", span="6x1")
        with self.say("s33") as t:
            self.play(Indicate(VGroup(ab, abl), color=C["fg"]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(FadeOut(VGroup(bias_g, ab, abl, sh, ml_)), run_time=0.6)
            self.release("biaschart", "biasl", "shallowstrip", "missedl")
            self.at(t, 2)
            self.play(self.heading("total cells"), *self.tags("schematic"), DrawBorderThenFill(rich[0]), DrawBorderThenFill(poor[0]),
                      Write(rl), Write(pl), run_time=0.8)
            self.play(LaggedStart(*[GrowFromCenter(c) for c in rich[1]], lag_ratio=0.01),
                      LaggedStart(*[GrowFromCenter(c) for c in poor[1]], lag_ratio=0.1), run_time=1.0)
            self.play(GrowArrow(arrs[0]), GrowArrow(arrs[1]), draw_chart(c1, 1.0), draw_chart(c2, 1.0), Write(same),
                      run_time=self.left(t, 2, "that takes"))
            self.at(t, 2, "that takes")
            self.play(Write(tot), run_time=self.left(t, 2))
            self.track(VGroup(arrs, same), "same")

        # s34 (distil): the two results side by side: richness made comparable, counts still biased
        lo, hi = int(D["rare_draws"].min()), int(D["rare_draws"].max())
        vals, cnts = np.unique(D["rare_draws"], return_counts=True)
        hbars = VGroup(*[Rectangle(width=0.18, height=2.0 * c / cnts.max(), stroke_width=0, fill_color=SAMPLE, fill_opacity=0.8)
                         .move_to([0.22 * (v - lo), 0, 0], aligned_edge=DOWN) for v, c in zip(vals, cnts)])
        hbase = Line(hbars.get_corner(DL) + LEFT * 0.1, hbars.get_corner(DR) + RIGHT * 0.1, color=C["muted"], stroke_width=2)
        left = VGroup(hbars, hbase, label("richness: now comparable", 28).next_to(hbase, DOWN, buff=0.3))
        bc2 = chart(D["pool"], "", xlab="", **CHART).scale(0.5)
        right = VGroup(bc2, label("counts: still biased", 28).next_to(bc2, DOWN, buff=0.3))
        both = self.place(VGroup(left, right).arrange(RIGHT, buff=2.0, aligned_edge=DOWN), "A1", "both", span="6x3")
        with self.say("s34") as t:
            self.play(FadeOut(VGroup(row, arrs, same, tot)), self.heading("what rarefying does"), *self.tags("summary"), run_time=0.6)
            self.release("twosoils", "same", "total")
            self.play(Create(hbase), LaggedStart(*[GrowFromEdge(r, DOWN) for r in hbars], lag_ratio=0.05), run_time=1.0)
            self.play(Write(left[2]), run_time=self.left(t, 0))
            self.at(t, 1)
            self.play(draw_chart(bc2, 1.0), run_time=1.0)
            self.play(Write(right[1]), run_time=self.left(t, 1))
        self.wait(0.8)
