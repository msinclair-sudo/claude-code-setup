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
    return VGroup(drop, grains).scale(0.3).to_corner(UL, buff=0.3)


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
                      Write(cap), *self.tags("schematic drawing"), run_time=1.6)
            self.play(glass.animate(path_arc=-PI / 3).shift(world.get_center() - ring.get_center()), run_time=1.6)
            self.track(glass, "glass")
            self.play(self.camera.frame.animate.scale(0.42).move_to(world.get_center()),
                      LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.03),
                      run_time=max(t.duration - 3.4, 2))

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
                      *self.tags("schematic drawing; simulated counts"), run_time=1.8)
            self.track(icon, "icon")
            self.play(Write(info), run_time=max(t.duration - 3.4, 1.2))

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
            k_ = t.duration / 7.5                              # five moves, finished inside the narration
            self.play(ReplacementTransform(info, ch[3]), Create(ch[0]), Create(ch[1]), Write(ch[4]), run_time=1.0 * k_)
            self.play(LaggedStart(*[c.animate.scale(0.6).move_to(b[pick[k]].get_bottom() + UP * 0.05)
                                    for k, c in enumerate(cells)], lag_ratio=0.02), run_time=1.5 * k_)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.02), FadeOut(cells), run_time=1.5 * k_)
            self.play(Create(top), Write(tl), run_time=1.2 * k_)
            self.play(Create(tail), Write(ll), run_time=1.2 * k_)

        # s3b: real soils have the same shape (data, one global survey)
        card = self.place(VGroup(label("real soils, sequenced: one global survey (data)", 22, C["muted"]),
                                 label("2% of bacterial taxa: about 41% of an average sample's reads", 28))
                          .arrange(DOWN, buff=0.12), "A4", "card", span="4x1")
        with self.say("s3b") as t:
            self.play(Write(card[0]), run_time=0.8)
            self.play(Write(card[1]), Indicate(VGroup(*b[:6]), color=C["fg"], scale_factor=1.05), run_time=max(t.duration - 1.0, 2))

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
        key = self.place(VGroup(label("DNA extraction: beads break the cells open", 30),
                                label("grey dots: beads", 22, C["muted"])).arrange(DOWN, buff=0.12),
                         "A4", "key", span="6x1")
        strands = VGroup(*[dna(COL[i]).move_to(cells[k]) for k, i in enumerate(who)])
        opened = [k for k in range(len(who)) if k not in tough]
        with self.say("s5") as t:
            self.play(Create(tube), LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.05),
                      Write(key[0]), *self.tags("schematic"), run_time=1.6)
            self.play(LaggedStart(*[GrowFromCenter(b_) for b_ in beads], lag_ratio=0.03), Write(key[1]), run_time=1.0)
            for _ in range(3):
                self.play(*[b_.animate.shift(np.array([rng.uniform(-0.5, 0.5), rng.uniform(-0.4, 0.4), 0])) for b_ in beads],
                          Wiggle(tube, scale_value=1.02, rotation_angle=0.02 * TAU), run_time=0.5)
            self.play(*[ReplacementTransform(cells[k], strands[k]) for k in opened], run_time=max(t.duration - 4.5, 1.2))

        # s6: the tough cells stay shut, circled one by one
        key2 = VGroup(label("tougher cells (thick outline) give up less DNA", 30),
                      label("one study: harder shaking gave up to 400% more Gram-positive DNA", 22, C["muted"])
                      ).arrange(DOWN, buff=0.12).move_to(key)
        with self.say("s6") as t:
            self.play(Succession(*[Circumscribe(cells[k], color=C["fg"], run_time=1.0) for k in tough]),
                      run_time=3.0)
            self.play(ReplacementTransform(key, key2), run_time=max(t.duration - 3.0, 1.2))

        # s7: one strand straightens into a ring, its genome; the 16S gene is drawn on
        lead = strands[0]
        centre = stage.get_center()
        big = Circle(radius=2.0).set_stroke(C["fg"], width=5).move_to(centre)
        gene = Arc(radius=2.0, start_angle=PI / 3, angle=0.32, stroke_width=16, color=COL[0]).shift(centre)
        glab = label("16S rRNA gene", 30).next_to(gene, UP + RIGHT, buff=0.04)
        gnl = label("one genome, a ring of DNA", 26, C["muted"]).next_to(big, DOWN, buff=0.25)
        rest = VGroup(tube, beads, *[strands[k] for k in opened if k != 0], *[cells[k] for k in tough], key2)
        with self.say("s7") as t:
            self.play(FadeOut(rest), run_time=0.8)
            self.release("tube", "key")
            self.play(Transform(lead, big), run_time=1.4)
            self.play(Write(gnl), run_time=0.8)
            self.play(Create(gene), Write(glab), run_time=max(t.duration * 0.3, 1.2))

        # s8: the ring moves left and gains its copies; taxon 3's ring has one
        c1, c3 = int(D["copies"][0]), int(D["copies"][2])
        left, right = centre + LEFT * 2.9 + UP * 0.3, centre + RIGHT * 2.9 + UP * 0.3
        g1, g3 = genome_ring(c1, COL[0], left), genome_ring(c3, COL[2], right)
        l1 = label(f"taxon 1: {c1} cop{'y' if c1 == 1 else 'ies'}", 28, COL[0]).next_to(g1, DOWN, buff=0.3)
        l3 = label(f"taxon 3: {c3} cop{'y' if c3 == 1 else 'ies'}", 28, COL[2]).next_to(g3, DOWN, buff=0.3)
        span = label("a genome carries 1 to about 15 copies, rarely more", 24, C["muted"]).next_to(VGroup(l1, l3), DOWN, buff=0.35)
        with self.say("s8") as t:
            self.play(FadeOut(glab), FadeOut(gnl), Transform(lead, g1[0]), Transform(gene, g1[1][0]), run_time=1.2)
            self.play(Write(span), run_time=1.0)
            self.play(LaggedStart(*[Create(a) for a in g1[1][1:]], lag_ratio=0.3), Write(l1), run_time=2.0)
            self.track(VGroup(lead, gene, g1[1], l1), "g1")
            self.play(Create(g3[0]), run_time=0.8)
            self.play(Create(g3[1]), Write(l3), run_time=1.0)
            self.track(VGroup(g3, l3), "g3")
        self.add(g1[1])

        # s9: a growing cell holds two genomes: the first ring is copied beside itself
        twin = VGroup(lead, gene, g1[1]).copy()
        with self.say("s9") as t:
            self.play(FadeOut(VGroup(g3, l3, span)), run_time=0.8)
            self.release("g3")
            self.play(VGroup(lead, gene, g1[1], l1).animate.shift(RIGHT * 1.0), run_time=0.8)
            twin.move_to(VGroup(lead).get_center() + RIGHT * 3.2)
            outline = RoundedRectangle(width=7.4, height=3.6, corner_radius=1.6).set_stroke(COL[0], width=3) \
                .move_to(VGroup(lead, twin).get_center())
            note = label("a cell can hold several genome copies (here two); in soil, barely measured", 26).next_to(outline, DOWN, buff=0.3)
            self.play(TransformFromCopy(VGroup(lead, gene, g1[1]), twin), run_time=1.6)
            self.play(Create(outline), FadeOut(l1), Write(note), run_time=max(t.duration - 3.2, 1.2))
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
            self.play(FadeOut(VGroup(lead, gene, g1[1], twin, outline, note)), run_time=0.6)
            self.release("g1", "twin")
            self.play(draw_chart(ch, 1.6), Write(before), *self.tags("simulated"), run_time=1.6)
            for k in (1, 2):
                new = bars(D[keys[k]], **CHART).match_width(b).move_to(b, aligned_edge=DL)
                self.play(Transform(b, new), Transform(ch[3], label(titles[k], 24).move_to(ch[3])), run_time=1.6)
            self.play(Write(notes[1]), Write(after), Indicate(b[0], color=C["fg"]), run_time=1.2)


class Amplify(Chaptered):
    NUMBER, TITLE = 3, "PCR"

    def construct(self):
        self.camera.background_color = C["bg"]
        self.chapter()
        # s11: primers land on the conserved stretches either side of the barcode
        gene_bar = Rectangle(width=8.0, height=0.3, stroke_width=0, fill_color=C["fg"], fill_opacity=0.3)
        bc = Rectangle(width=1.8, height=0.3, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(gene_bar).shift(RIGHT * 0.8)
        fwd = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=C["fg"], stroke_width=6, max_tip_length_to_length_ratio=0.35) \
            .next_to(bc, UP, buff=0.12).align_to(bc, RIGHT).shift(LEFT * 1.85)
        rev = Arrow(RIGHT * 0.5, LEFT * 0.5, buff=0, color=C["fg"], stroke_width=6, max_tip_length_to_length_ratio=0.35) \
            .next_to(bc, DOWN, buff=0.12).align_to(bc, LEFT).shift(RIGHT * 1.85)
        names = VGroup(label("primer", 22, C["muted"]).next_to(fwd, LEFT, buff=0.12),
                       label("primer", 22, C["muted"]).next_to(rev, RIGHT, buff=0.12))
        regions = VGroup(label("conserved", 20, C["muted"]).next_to(gene_bar, DOWN, buff=0.55).align_to(gene_bar, LEFT),
                         label("variable stretch: the barcode", 22).next_to(bc, UP, buff=0.12).align_to(bc, LEFT),
                         label("conserved", 20, C["muted"]).next_to(gene_bar, DOWN, buff=0.55).align_to(gene_bar, RIGHT))
        top = self.place(VGroup(gene_bar, bc, fwd, rev, names, regions), "A1", "gene", span="6x1")
        fwd.shift(LEFT * 4 + UP * 1.2); rev.shift(RIGHT * 4 + DOWN * 1.2)       # they fly in from off the gene
        names.set_opacity(0)
        with self.say("s11") as t:
            self.play(Create(gene_bar), *self.tags("schematic"), run_time=1.0)
            self.play(fwd.animate.shift(RIGHT * 4 + DOWN * 1.2), rev.animate.shift(LEFT * 4 + UP * 1.2),
                      names.animate.set_opacity(1), run_time=1.6)
            self.play(DrawBorderThenFill(bc), Write(regions), run_time=max(t.duration - 2.6, 1.2))

        # s12: the barcode is copied, each new strand out of an old one
        area = self.place(Rectangle(width=5, height=3.0, stroke_opacity=0), "B2", "pcr", span="4x2")

        def strands(n):
            g = VGroup(*[Line(LEFT * 0.45, RIGHT * 0.45, stroke_width=8, color=C["fg"]) for _ in range(n)])
            return g.arrange_in_grid(rows=max(1, n // 4), cols=min(n, 4), buff=(0.35, 0.3)).move_to(area)
        counter = self.place(label("PCR cycle 0: 1 copy", 30), "B4", "counter", span="4x1")
        with self.say("s12") as t:
            self.play(Write(counter), run_time=0.6)
            now = strands(1)
            self.play(TransformFromCopy(bc, now[0]), run_time=0.8)
            step = max((t.duration - 3.0) / 4, 0.6)
            for k in range(1, 5):
                nxt = strands(2 ** k)
                self.play(TransformFromCopy(now, nxt[len(now):]), Transform(now, nxt[:len(now)]),
                          Transform(counter, label(f"PCR cycle {k}: {2 ** k} copies", 30).move_to(counter)), run_time=step)
                self.remove(now); now = nxt; self.add(now)
            self.play(Transform(counter, label(f"PCR cycle {P.CYCLES}: many copies", 30).move_to(counter)),
                      now.animate.set_opacity(0.5), run_time=1.4)
        self.play(FadeOut(VGroup(now, counter, top)), run_time=0.6)
        self.release("pcr", "gene", "counter")

        # s13: fold bias per taxon after 35 cycles, on a log scale; the dots drop onto the axis
        lb = np.log2(D["bias"])
        W = 10.0
        x = lambda v: v / 5 * W / 2                                # log2 -5..5 -> -W/2..W/2
        axis = Line([-W / 2, 0, 0], [W / 2, 0, 0], color=C["muted"], stroke_width=2)
        ticks = VGroup(*[VGroup(Line([x(v), -0.08, 0], [x(v), 0.08, 0], color=C["muted"], stroke_width=2),
                                label(s, 22, C["muted"]).next_to([x(v), 0, 0], DOWN, buff=0.18))
                         for v, s in ((-4, "1/16"), (-2, "1/4"), (0, "1"), (2, "4"), (4, "16"))])
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
        ttl = label(f"fold bias per taxon after {P.CYCLES} PCR cycles (log scale)", 24).next_to(axis, UP, buff=2.2)
        xl = label("1 = no bias;  dashed: fourfold either way;  ringed: beyond fourfold", 20, C["muted"]).next_to(ticks, DOWN, buff=0.15)
        plot = self.place(VGroup(axis, ticks, dots, rings, lines, ttl, xl), "A1", "bias", span="6x3")
        head = self.place(VGroup(label(f"one study, {P.CYCLES} cycles: 1 taxon in 5 more than fourfold off", 26),
                                 label(f"simulated: {int(far.sum())} of {N} taxa", 24, C["muted"]))
                          .arrange(DOWN, buff=0.12), "A4", "head", span="6x1")
        with self.say("s13") as t:
            self.play(Create(axis), Write(ticks), Write(ttl), Write(xl), *self.tags("simulated"), run_time=1.2)
            self.play(LaggedStart(*[d_.animate(rate_func=rush_into).shift(DOWN * 2.4) for d_ in dots.shift(UP * 2.4)],
                                  lag_ratio=0.02), run_time=max(t.duration * 0.35, 2))
            self.play(Create(lines), Write(head[0]), run_time=1.4)
            self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.1), Write(head[1]), run_time=1.6)
        self.play(FadeOut(VGroup(plot, head)), run_time=0.6)
        self.release("bias", "head")

        # s14 (distil): the chart, from gene copies to barcodes
        ch = self.place(chart(D["templates"], "share of 16S gene copies", xlab="taxa, in the order of the cell counts", **CHART),
                        "A1", "chart", span="6x3")
        b = ch[2]
        notes = self.place(VGroup(label(f"taxon 1: {pct(D['pool'][0])} of barcodes", 28, COL[0]),
                                  label(f"taxon 3: {pct(D['true'][2])} of cells → {pct(D['pool'][2])} of barcodes", 28, COL[2]))
                           .arrange(RIGHT, buff=0.9), "A4", "notes", span="6x1")
        with self.say("s14") as t:
            self.play(draw_chart(ch, 1.4), run_time=1.4)
            new = bars(D["pool"], **CHART).match_width(b).move_to(b, aligned_edge=DL)
            self.play(Transform(b, new), Transform(ch[3], label("share of barcodes after PCR: shifted again", 24).move_to(ch[3])), run_time=1.8)
            self.play(Write(notes[0]), Indicate(b[0], color=C["fg"]), run_time=1.2)
            self.play(Write(notes[1]), Indicate(b[2], color=C["fg"], scale_factor=2), run_time=1.4)


class Sequence(Chaptered):
    NUMBER, TITLE = 4, "Sequencing"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(13)
        self.chapter()
        # s15: three samples; each barcode gets its sample's index tag
        tubes, kids = VGroup(), []
        for k, s in enumerate("ABC"):
            box = RoundedRectangle(width=2.4, height=1.9, corner_radius=0.25).set_stroke(SAMPLE, width=3)
            name = label(f"sample {s}", 24).next_to(box, UP, buff=0.12)
            amps = VGroup(*[Line(LEFT * 0.27, RIGHT * 0.27, stroke_width=7, color=COL[int(i)])
                            for i in rng.choice(6, 6)]).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.2)).move_to(box)
            tubes.add(VGroup(box, name, amps)); kids.append(amps)
        tubes.arrange(RIGHT, buff=0.9)
        self.place(tubes, "A1", "tubes", span="6x2")
        key = self.place(VGroup(label("an index tag names each sample", 30),
                                label("white squares: the index tag, one pattern per sample", 22, C["muted"]))
                         .arrange(DOWN, buff=0.1), "A4", "key", span="6x1")
        tagged_amps, tags_ = [], []
        for k, amps in enumerate(kids):
            for a in amps:
                tg = index_tag(k).next_to(a, LEFT, buff=0.05)
                tagged_amps.append(VGroup(tg, a)); tags_.append(tg)
        with self.say("s15") as t:
            self.play(LaggedStart(*[AnimationGroup(Create(tb[0]), Write(tb[1])) for tb in tubes], lag_ratio=0.3),
                      *self.tags("schematic"), run_time=1.6)
            self.play(LaggedStart(*[GrowFromCenter(a) for amps in kids for a in amps], lag_ratio=0.04), run_time=1.2)
            self.play(LaggedStart(*[GrowFromEdge(tg, RIGHT) for tg in tags_], lag_ratio=0.05), Write(key),
                      run_time=max(t.duration - 2.8, 1.5))

        # s16: the samples pour into one pool; reads travel from the pool into the sequencer
        pool_box = RoundedRectangle(width=4.2, height=1.5, corner_radius=0.25).set_stroke(C["muted"], width=2)
        pool = self.place(VGroup(pool_box, label("one pooled run", 22, C["muted"]).next_to(pool_box, DOWN, buff=0.1)),
                          "B3", "pool", span="4x1")
        order = rng.permutation(len(tagged_amps))
        spots = [None] * len(tagged_amps)
        for slot, j in enumerate(order):                      # 6 x 3 grid, samples mixed
            c, r = slot % 6, slot // 6
            spots[j] = pool_box.get_center() + np.array([(c - 2.5) * pool_box.width / 6.6, (1 - r) * pool_box.height / 3.8, 0])
        seq = RoundedRectangle(width=2.6, height=1.2, corner_radius=0.2).set_stroke(C["fg"], width=3)
        seqg = self.place(VGroup(seq, label("sequencer", 26).move_to(seq)), "A1", "seq", span="2x1")
        with self.say("s16") as t:
            self.play(Create(pool_box), Write(pool[1]), run_time=0.8)
            self.play(*[g.animate(path_arc=-PI / 3).scale(0.8).move_to(p) for g, p in zip(tagged_amps, spots)],
                      *[Uncreate(tb[0]) for tb in tubes], *[FadeOut(tb[1]) for tb in tubes], FadeOut(key), run_time=1.8)
            self.release("tubes", "key")
            self.play(Create(seqg[0]), Write(seqg[1]), run_time=0.8)
            picks = rng.choice(len(tagged_amps), 8, replace=False)
            flying = [tagged_amps[j].copy() for j in picks]
            self.add(*flying)
            self.play(LaggedStart(*[MoveAlongPath(f, ArcBetweenPoints(f.get_center(), seq.get_center(), angle=-PI / 3))
                                    for f in flying], lag_ratio=0.3), run_time=max(t.duration - 3.2, 1.6))
            self.play(*[FadeOut(f, scale=0.3) for f in flying], run_time=0.4)
            self.remove(*flying)

        # s17: each sample's reads fill its meter; they come out uneven
        meters = VGroup()
        for k, s in enumerate("ABC"):
            frame = Rectangle(width=4.5, height=0.36).set_stroke(C["rule"], width=2)
            fill = Rectangle(width=4.5 * SKETCH_DEPTH[k], height=0.36, stroke_width=0, fill_color=SAMPLE, fill_opacity=0.85) \
                .align_to(frame, LEFT)
            meters.add(VGroup(label(f"sample {s}", 24), index_tag(k), VGroup(frame, fill)).arrange(RIGHT, buff=0.25))
        meters.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        edge = max(m[1].get_right()[0] for m in meters) + 0.25
        for m in meters:                                      # bars share one left edge
            m[2].shift(RIGHT * (edge - m[2].get_left()[0]))
        mg = self.place(meters, "D1", "meters", span="3x2")
        term = self.place(label("sequencing depth: reads per sample", 30), "A4", "term", span="6x1")
        with self.say("s17") as t:
            self.play(LaggedStart(*[AnimationGroup(Write(m[0]), GrowFromCenter(m[1]), Create(m[2][0])) for m in meters],
                                  lag_ratio=0.2), run_time=1.2)
            self.play(*[GrowFromEdge(m[2][1], LEFT) for m in meters], run_time=max(t.duration * 0.45, 2))
            self.play(Write(term), run_time=1.0)
        self.play(FadeOut(VGroup(pool, *tagged_amps, mg, term)), run_time=0.6)
        self.release("pool", "meters", "term")

        # s18: reads sorted into bins by tag; one lands in the wrong bin
        bins_ = VGroup()
        for k, s in enumerate("ABC"):
            box = Rectangle(width=2.6, height=1.8).set_stroke(SAMPLE, width=3)
            head = VGroup(label(f"sample {s}", 24), index_tag(k)).arrange(RIGHT, buff=0.2).next_to(box, UP, buff=0.12)
            bins_.add(VGroup(box, head))
        bins_.arrange(RIGHT, buff=0.8)
        self.place(bins_, "A2", "bins", span="6x2")
        key3 = self.place(label("demultiplexing: reads sorted by tag", 30), "A4", "key3", span="6x1")
        plan = [(k, k) for k in (0, 1, 2, 0, 1, 2, 0, 1, 2)] + [(0, 1)]   # last read: sample A's, sorted into B
        reads, slots, fill_n = VGroup(), [], [0, 0, 0]
        for k, dest in plan:
            reads.add(tagged(COL[int(rng.integers(0, 6))], k).scale(0.8).move_to(seq.get_center()))
            slots.append(bins_[dest][0].get_top() + DOWN * (0.35 + 0.42 * fill_n[dest]))
            fill_n[dest] += 1
        wrong = reads[-1]
        flag = label("misassigned (exaggerated here)", 22, C["muted"])
        with self.say("s18") as t:
            self.play(LaggedStart(*[AnimationGroup(Create(b_[0]), Write(b_[1])) for b_ in bins_], lag_ratio=0.2),
                      Write(key3), run_time=1.0)
            self.play(LaggedStart(*[MoveAlongPath(r, ArcBetweenPoints(r.get_center(), s, angle=PI / 4))
                                    for r, s in zip(reads[:-1], slots[:-1])], lag_ratio=0.25), run_time=max(t.duration * 0.45, 2))
            self.play(MoveAlongPath(wrong, ArcBetweenPoints(wrong.get_center(), slots[-1], angle=PI / 4)), run_time=1.0)
            flag.next_to(bins_[1][0], DOWN, buff=0.15)
            self.play(Circumscribe(wrong, color=C["fg"]), Write(flag), run_time=1.2)

        # s19 (distil): the three piles hold; their sizes are marked
        piles = VGroup(*[Rectangle(width=0.4, height=max(1.6 * SKETCH_DEPTH[k], 0.03), stroke_width=0,
                                   fill_color=SAMPLE, fill_opacity=0.85).next_to(bins_[k][0], RIGHT, buff=0.12)
                         .align_to(bins_[k][0], DOWN) for k in range(3)])
        key4 = label("each sample: its own pile of reads, each a different size", 30).move_to(key3)
        with self.say("s19") as t:
            self.play(FadeOut(flag), FadeOut(seqg), run_time=0.6)
            self.release("seq")
            self.play(*[GrowFromEdge(p_, DOWN) for p_ in piles], Transform(key3, key4), run_time=1.6)


class Reads(Chaptered):
    NUMBER, TITLE = 5, "From reads to a table"

    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(17)
        self.chapter()
        # s20: merge each read pair; drop short or low-quality reads (every bar labelled)
        frag = Rectangle(width=6.0, height=0.26, stroke_width=0, fill_color=C["fg"], fill_opacity=0.35)
        fl = label("one DNA fragment", 20, C["muted"]).next_to(frag, LEFT, buff=0.2)
        r1 = Arrow(LEFT * 2.0, RIGHT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, UP, buff=0.15).align_to(frag, LEFT)
        r2 = Arrow(RIGHT * 2.0, LEFT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, DOWN, buff=0.15).align_to(frag, RIGHT)
        rl = VGroup(label("read 1", 20, C["muted"]).next_to(r1, RIGHT, buff=0.15),
                    label("read 2", 20, C["muted"]).next_to(r2, LEFT, buff=0.15))
        self.place(VGroup(fl, frag, r1, r2, rl), "A1", "pair", span="6x1")
        merged = Rectangle(width=frag.width, height=frag.height, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(frag)
        ml = label("merged read", 20).next_to(merged, RIGHT, buff=0.2)
        good = [Rectangle(width=2.4, height=0.2, stroke_width=0, fill_color=C["fg"], fill_opacity=1) for _ in range(3)]
        short = Rectangle(width=0.9, height=0.2, stroke_width=0, fill_color=C["fg"], fill_opacity=1)
        poor = VGroup(*[Rectangle(width=0.3, height=0.2, stroke_width=0, fill_color=C["fg"],
                                  fill_opacity=float(o)) for o in rng.uniform(0.1, 0.6, 8)]).arrange(RIGHT, buff=0)
        rows = VGroup(good[0], short, good[1], poor, good[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        notes = VGroup(*[label(s, 22, C["muted"]) for s in
                         ("kept", "too short: dropped", "kept", "poor quality (faint): dropped", "kept")])
        for n, r in zip(notes, rows):
            n.next_to(r, RIGHT, buff=0.3).align_to(rows, RIGHT).shift(RIGHT * 0.3 + RIGHT * n.width)
        head = label("merged reads, filtered", 22, C["muted"]).next_to(rows, UP, buff=0.25).align_to(rows, LEFT)
        self.place(VGroup(head, rows, notes), "B2", "filter", span="4x2")
        key = self.place(label("merge read pairs; drop short or poor reads", 30), "A4", "key", span="6x1")
        with self.say("s20") as t:
            self.play(Create(frag), Write(fl), Write(key), *self.tags("schematic"), run_time=1.0)
            self.play(GrowArrow(r1), GrowArrow(r2), Write(rl), run_time=1.2)
            self.play(ReplacementTransform(VGroup(r1, r2), merged), FadeOut(rl), Write(ml), run_time=1.2)
            self.play(Write(head), LaggedStart(*[GrowFromEdge(r, LEFT) for r in rows], lag_ratio=0.15), Write(notes),
                      run_time=max(t.duration * 0.25, 1.2))
            self.play(FadeOut(VGroup(short, notes[1]), shift=DOWN * 0.4), FadeOut(VGroup(poor, notes[3]), shift=DOWN * 0.4),
                      run_time=1.2)
        self.play(FadeOut(VGroup(fl, frag, merged, ml, head, *good, notes[0], notes[2], notes[4], key)), run_time=0.6)
        self.release("pair", "filter", "key")

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
        asv_l = label("ASV", 30, weight=BOLD)
        legend = label("white, underlined: sequencing errors", 26, C["muted"])
        legend2 = label("one exact sequence: the ASV", 26, C["muted"])
        side = VGroup(legend,
                      VGroup(label("one soil dataset:", 26, C["muted"]),
                             label("8,270 to 16,609 ASVs, by pipeline", 26, C["muted"])).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.place(side, "D1", "side", span="3x3")
        legend2.move_to(legend, aligned_edge=LEFT)
        key2 = self.place(label("denoising: near-copies fold into ASVs", 30), "A4", "key2", span="6x1")
        with self.say("s21") as t:
            self.play(Write(ctitle), LaggedStart(*[Write(v) for v in cloud], lag_ratio=0.15), Write(legend), Write(key2), run_time=1.8)
            asv.move_to(cloud)
            self.play(ReplacementTransform(cloud, asv), FadeOut(ctitle), TransformMatchingShapes(legend, legend2),
                      run_time=max(t.duration * 0.3, 1.5))
            asv_l.next_to(asv, UP, buff=0.25)
            self.play(Write(asv_l), run_time=0.8)
            self.play(Write(side[1]), run_time=1.2)
        self.play(FadeOut(VGroup(asv, asv_l, legend2, side[1], key2)), run_time=0.6)
        self.release("cloud", "side", "key2")

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
        key3 = self.place(label("chimera: half one template, half another", 30), "A4", "key3", span="6x1")
        with self.say("s22") as t:
            self.play(GrowFromEdge(ta, LEFT), GrowFromEdge(tb, LEFT), Write(tl), Write(key3), run_time=1.0)
            self.play(GrowFromEdge(h1, LEFT), run_time=1.2)
            self.play(h1.animate(path_arc=PI / 4).next_to(h2, LEFT, buff=0), GrowFromEdge(h2, LEFT), run_time=1.2)
            self.play(ReplacementTransform(VGroup(h1, h2), chim), Write(cl), run_time=1.0)
            self.play(Write(dl), LaggedStart(*[TransformFromCopy(chim, m) for m in many], lag_ratio=0.15),
                      run_time=max(t.duration * 0.2, 1.0))
            self.play(*[Create(Cross(Square(side_length=0.45).move_to(many[j]), stroke_color=C["fg"], stroke_width=4))
                        for j in caught], Write(dk), run_time=1.4)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not getattr(self, "_tag", None)], run_time=0.6)
        self.release("temps", "chimera", "detector", "key3")

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
        key4 = self.place(label("named by a reference database, then counted", 28), "A4", "key4", span="6x1")
        with self.say("s23") as t:
            self.play(Write(VGroup(q, ql)), Write(shl), LaggedStart(*[GrowFromEdge(r, LEFT) for r in shelf], lag_ratio=0.08),
                      Write(key4), run_time=1.2)
            arr = Arrow(q.get_right(), shelf.get_left(), buff=0.1, color=C["muted"], stroke_width=3)
            cls = label("classifier: best match", 20, C["muted"]).next_to(q, DOWN, buff=0.15)
            self.play(GrowArrow(arr), Write(cls), run_time=0.8)
            self.track(VGroup(arr, cls), "classifier")
            self.play(Indicate(shelf[2], color=C["fg"], scale_factor=1.1), Write(named), run_time=1.0)
            self.track(named, "named")
            self.play(Write(tt), Write(cols_), LaggedStart(*[GrowFromCenter(r) for r in rows_], lag_ratio=0.1), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(c, LEFT) for c in cells_], lag_ratio=0.05), Write(more),
                      run_time=max(t.duration * 0.3, 1.5))

        # s24 (distil): the table holds; its title says what it counts
        tt2 = label("count table: reads per taxon, not cells", 24).move_to(tt)
        key5 = VGroup(label("the table counts reads, not cells", 30),
                      label("our simulation leaves out the false taxa these steps can add", 22, C["muted"])
                      ).arrange(DOWN, buff=0.1).move_to(key4)
        with self.say("s24") as t:
            self.play(Transform(tt, tt2), Transform(key4, key5[0]), Indicate(cells_, color=C["fg"], scale_factor=1.03), run_time=1.4)
            self.play(Write(key5[1]), run_time=1.6)
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
            self.play(DrawBorderThenFill(icon), Write(key), *self.tags("simulated"), run_time=0.8)
            self.track(icon, "icon")
            for k in range(3):
                self.play(Write(texts[k]), LaggedStart(*[Create(sq) for sq in strips[k]], lag_ratio=0.01),
                          run_time=max((t.duration - 0.8) / 3 - 0.2, 1))

        # s26: the empty slots at 500 reads are the low-abundance taxa
        shallow = strips[2]
        missed = [i for i in range(N) if D["runs"][min(P.DEPTHS)][i] == 0]
        note = label("missed at 500 reads: low-abundance taxa, too few barcodes to be picked", 24).move_to(key)
        with self.say("s26") as t:
            self.play(Transform(key, note), run_time=1.0)
            self.play(LaggedStart(*[Indicate(shallow[i], color=C["fg"], scale_factor=1.8) for i in missed[:24]],
                                  lag_ratio=0.05), run_time=max(t.duration - 1.2, 2))
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
            self.play(Create(p1[0]), Create(p2[0]), Create(p1[1]), Create(p2[1]), Write(VGroup(*p1[2:], *p2[2:])),
                      Write(key2), run_time=1.4)
            self.play(LaggedStart(*[GrowFromCenter(x) for x in d1], lag_ratio=0.01), run_time=max(t.duration * 0.35, 1.5))
            self.play(LaggedStart(*[GrowFromCenter(x) for x in d2], lag_ratio=0.01), run_time=max(t.duration * 0.65 - 1.4, 1.5))

        # s28 (distil): the three counts, deepest to shallowest
        summary = VGroup(*[label(f"{dep:,} reads → {int((D['runs'][dep] > 0).sum())} taxa", 34) for dep in deps]
                         ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        head = label("fewer reads, fewer taxa found", 30, weight=BOLD)
        with self.say("s28") as t:
            self.play(FadeOut(VGroup(p1, d1, p2, d2, key2)), run_time=0.6)
            self.release("p1", "p2", "key2")
            self.place(VGroup(head, summary).arrange(DOWN, aligned_edge=LEFT, buff=0.5), "B1", "summary", span="4x3")
            self.play(Write(head), LaggedStart(*[Write(s) for s in summary], lag_ratio=0.3), run_time=max(t.duration - 0.6, 1.5))


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
            self.play(Write(title), DrawBorderThenFill(icon), *self.tags("simulated"), run_time=0.8)
            self.track(icon, "icon")
            for c in (deep_c, shal_c):
                self.play(Write(c[0]), LaggedStart(*[Create(sq) for sq in c[1]], lag_ratio=0.01), Write(c[2]), run_time=1.4)

        # s30: rarefying: the deep sample drawn down to 2,000 reads at random; the rest set aside
        one = P.rarefy(D["deep"], P.SHALLOW, rng) > 0
        lost = [i for i in range(N) if D["deep"][i] > 0 and not one[i]]
        head2 = label(f"deep, rarefied: {P.SHALLOW:,} reads", 28).move_to(deep_c[0], aligned_edge=LEFT)
        aside = label(f"{P.DEEP - P.SHALLOW:,} reads set aside", 24, C["muted"]).move_to(deep_c[2], aligned_edge=LEFT)
        with self.say("s30") as t:
            self.play(Transform(deep_c[0], head2), run_time=1.2)
            self.play(*[deep_c[1][i].animate.set_fill(opacity=0).set_stroke(C["rule"]) for i in lost],
                      FadeOut(deep_c[2], shift=DOWN * 0.2), Write(aside), run_time=max(t.duration * 0.5, 2))
            self.track(aside, "aside")

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
            self.play(FadeOut(VGroup(deep, shal, title, aside)), run_time=0.6)
            self.release("deep", "shallow", "title", "aside")
            self.play(Write(htxt), Create(ax), Write(xt), Write(xtitle), Write(ylab), run_time=1.0)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in hist], lag_ratio=0.08), GrowFromCenter(mean), Write(mean_l),
                      run_time=max(t.duration * 0.5, 2))
            self.play(GrowFromEdge(band, DOWN), Write(blab), Create(mark), Write(mlab), run_time=max(t.duration * 0.5 - 1.6, 1.2))

        # s32: what rarefying does not fix
        does = label("rarefying evens out depth, nothing else", 30, weight=BOLD)
        lines = VGroup(label("extraction, copy-number and PCR bias: still in every read", 26),
                       label("taxa the shallow sample missed: still missed", 26)).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        with self.say("s32") as t:
            self.play(FadeOut(VGroup(hgroup, htxt)), run_time=0.8)
            self.release("hist", "htxt")
            lim = self.place(VGroup(does, lines).arrange(DOWN, aligned_edge=LEFT, buff=0.35), "A1", "limits", span="6x2")
            self.play(Write(does), *self.tags("summary"), run_time=1.0)
            self.play(LaggedStart(*[Write(x) for x in lines], lag_ratio=0.8), run_time=max(t.duration - 1.8, 2))

        # s33: the open questions
        more = VGroup(label("that bias can differ between samples", 26),
                      label("whether to rarefy at all: still debated", 26),
                      label("total cells: shares cannot show them; spike-ins or cell counts can", 26)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        with self.say("s33") as t:
            self.place(more, "A3", "more", span="6x2").align_to(lim, LEFT)
            self.play(LaggedStart(*[Write(x) for x in more], lag_ratio=0.8), run_time=max(t.duration - 0.5, 2))

        # s34 (distil): one line stays
        final = VGroup(label("rarefying makes richness comparable", 34, weight=BOLD),
                       label("it does not undo what came before the sequencer", 30)).arrange(DOWN, buff=0.3)
        with self.say("s34") as t:
            self.play(FadeOut(VGroup(lim, more)), run_time=0.8)
            self.release("limits", "more")
            self.place(final, "A2", "final", span="6x2")
            self.play(Write(final[0]), run_time=1.2)
            self.play(Write(final[1]), run_time=1.2)
        self.wait(0.8)
