"""Rarefaction in a metabarcoding experiment, tier 4: seven chapters, from soil to a rarefied count table.

Narration comes from storyboard.yaml (say("sN")); every count from ../pipeline.py (simulated, seed 7);
literature facts from claims.yaml (MB-01 review). Drawings of soil, cells, genomes, PCR, the sequencer and
the bioinformatics steps are schematic; the charts are the simulation's numbers. Colours mean taxa only
(the six commonest; the rest grey); samples are white and told apart by label and index pattern.
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


def chart(shares, title, w=5.6, h=3.0, ymax=0.5, xlab="taxa, commonest first"):
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


class Soil(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(5)
        drop = Circle(radius=1.9).set_stroke(SOIL, width=3).set_fill(SOIL, opacity=0.45)
        grains = VGroup(*[RegularPolygon(n=int(rng.integers(5, 8)), radius=rng.uniform(0.04, 0.11))
                          .set_stroke(width=0).set_fill("#A58A6C", opacity=0.7)
                          .move_to(drop.point_at_angle(rng.uniform(0, TAU)) * rng.uniform(0, 0.9)) for _ in range(60)])
        world = self.place(VGroup(drop, grains), "A1", "droplet", span="3x3")
        pick = rng.choice(N, size=70, p=D["true"])          # cells in proportion to the true shares
        lens_r = 1.25
        cells = VGroup(*[cell(i, rng).move_to(world.get_center() + lens_r * 0.85 * np.sqrt(rng.uniform()) *
                                              np.array([np.cos(a), np.sin(a), 0]))
                         for i, a in zip(pick, rng.uniform(0, TAU, 70))])
        ring = Circle(radius=lens_r).set_stroke(C["fg"], width=9).set_fill(C["fg"], opacity=0.06)
        handle = Line(ORIGIN, [1.4, -1.4, 0], stroke_width=16, color=C["fg"]).shift(ring.point_at_angle(-PI / 4))
        glass = VGroup(ring, handle).move_to(world.get_center() + np.array([3.5, 2.2, 0]))
        cap = self.place(VGroup(label("a droplet of soil, simulated", 28),
                                label(f"{P.CELLS:,} cells, {N} taxa", 24, C["muted"]))
                         .arrange(DOWN, aligned_edge=LEFT, buff=0.1), "A4", "label", span="3x1")
        with self.say("s1") as t:
            self.play(FadeIn(world), FadeIn(cap), self.tag("schematic drawing; simulated counts"), run_time=1.2)
            self.play(glass.animate.shift(world.get_center() - ring.get_center()), run_time=1.6)
            self.track(glass, "glass")
            self.play(LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.03), run_time=max(t.duration - 2.8, 1.5))

        ch = self.place(chart(D["true"], "true counts: share of cells per taxon"), "D1", "chart", span="3x3")
        b = ch[2]
        cap2 = self.place(label("a few common taxa, a long tail of rare ones", 26, C["muted"]), "D4", "label2", span="3x1")
        with self.say("s2") as t:
            self.play(FadeIn(VGroup(ch[0], ch[1], ch[3], ch[4])), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.02), run_time=max(t.duration - 2.3, 2))
            self.play(FadeIn(cap2), run_time=0.8)


class Genes(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(11)
        # s3: bead beating; most cells split and spill DNA, the tough ones stay shut
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
        tube = self.place(VGroup(cells, beads), "A1", "tube", span="6x3")
        key = self.place(VGroup(label("DNA extraction: some cells break open more easily", 30),
                                label("thick outline: a tougher cell wall;  grey dots: beads", 22, C["muted"]),
                                label("one study: harder beating gave up to 400% more Gram-positive DNA", 22, C["muted"]))
                         .arrange(DOWN, buff=0.12), "A4", "key", span="6x1")
        strands = VGroup(*[dna(COL[i]).move_to(cells[k]) for k, i in enumerate(who)])
        with self.say("s3") as t:
            self.play(FadeIn(tube), FadeIn(key[0]), self.tag("schematic"), run_time=1.0)
            for _ in range(3):
                self.play(*[b.animate.shift(np.array([rng.uniform(-0.5, 0.5), rng.uniform(-0.4, 0.4), 0])) for b in beads],
                          run_time=0.5)
            self.play(*[ReplacementTransform(cells[k], strands[k]) for k in range(len(who)) if k not in tough],
                      run_time=max(t.duration * 0.3, 1.5))
            self.play(FadeIn(key[1]), FadeIn(key[2]), *[Indicate(cells[k], color=C["fg"], scale_factor=1.15) for k in tough], run_time=1.4)
        self.play(FadeOut(VGroup(beads, key, *[strands[k] for k in range(len(who)) if k not in tough],
                                 *[cells[k] for k in tough])), run_time=0.6)
        self.release("tube", "key")

        # s4: a cell opens to its circular genome; the 16S gene lights up
        body = RoundedRectangle(width=4.2, height=2.0, corner_radius=1.0).set_stroke(COL[0], width=4).set_fill(COL[0], opacity=0.15)
        genome = Circle(radius=0.6).set_stroke(C["fg"], width=4)
        cellg = self.place(VGroup(body, genome), "B1", "cell", span="4x3")
        big = Circle(radius=2.0).set_stroke(C["fg"], width=5).move_to(cellg.get_center())
        gene = Arc(radius=2.0, start_angle=PI / 3, angle=0.32, stroke_width=16, color=C["fg"]).shift(cellg.get_center())
        glab = label("16S rRNA gene", 30).next_to(gene, UP + RIGHT, buff=0.04)
        gnl = label("circular genome", 26, C["muted"]).next_to(big, DOWN, buff=0.25)
        with self.say("s4") as t:
            self.play(FadeIn(cellg), run_time=1)
            self.play(FadeOut(body), Transform(genome, big), FadeIn(gnl), run_time=1.6)
            self.play(Create(gene), FadeIn(glab), run_time=1.2)

        # s5: copy number differs: taxon 1 has 7 copies, taxon 3 has 1
        def ring(n, colour, centre):
            c = Circle(radius=1.35).set_stroke(C["fg"], width=4).move_to(centre)
            arcs = VGroup(*[Arc(radius=1.35, start_angle=k * TAU / n + 0.2, angle=0.26, stroke_width=14, color=colour)
                            .shift(centre) for k in range(n)])
            return VGroup(c, arcs)
        c1, c3 = int(D["copies"][0]), int(D["copies"][2])
        left, right = cellg.get_center() + LEFT * 2.7 + UP * 0.3, cellg.get_center() + RIGHT * 2.7 + UP * 0.3
        g1, g3 = ring(c1, COL[0], left), ring(c3, COL[2], right)
        l1 = label(f"taxon 1: {c1} cop{'y' if c1 == 1 else 'ies'}", 28, COL[0]).next_to(g1, DOWN, buff=0.3)
        l3 = label(f"taxon 3: {c3} cop{'y' if c3 == 1 else 'ies'}", 28, COL[2]).next_to(g3, DOWN, buff=0.3)
        rng_note = label("bacterial genomes carry 1 to 15 copies", 24, C["muted"]).next_to(VGroup(l1, l3), DOWN, buff=0.35)
        with self.say("s5") as t:
            self.play(FadeOut(glab), FadeOut(gene), FadeOut(gnl), Transform(genome, g1[0]), run_time=1.2)
            self.release("cell")   # its genome has become taxon 1's
            self.play(FadeIn(rng_note), run_time=0.8)
            self.play(Create(g1[1]), FadeIn(l1), run_time=1.4)
            self.track(VGroup(g1, l1), "g1")
            self.play(FadeIn(g3), FadeIn(l3), run_time=1.2)
            self.track(VGroup(g3, l3), "g3")


class Amplify(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        # s6: primers on the conserved flanks of a variable region; PCR copies the barcode cycle by cycle
        gene_bar = Rectangle(width=8.0, height=0.3, stroke_width=0, fill_color=C["fg"], fill_opacity=0.3)
        bc = Rectangle(width=1.8, height=0.3, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(gene_bar).shift(RIGHT * 0.8)
        fwd = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=C["accent"], stroke_width=6, max_tip_length_to_length_ratio=0.35) \
            .next_to(bc, UP, buff=0.12).align_to(bc, RIGHT).shift(LEFT * 1.85)
        rev = Arrow(RIGHT * 0.5, LEFT * 0.5, buff=0, color=C["accent"], stroke_width=6, max_tip_length_to_length_ratio=0.35) \
            .next_to(bc, DOWN, buff=0.12).align_to(bc, LEFT).shift(RIGHT * 1.85)
        fwd.set_color(C["fg"]); rev.set_color(C["fg"])            # primers are not taxa: no taxon colour
        names = VGroup(label("primer", 22, C["muted"]).next_to(fwd, LEFT, buff=0.12),
                       label("primer", 22, C["muted"]).next_to(rev, RIGHT, buff=0.12))
        regions = VGroup(label("conserved", 20, C["muted"]).next_to(gene_bar, DOWN, buff=0.55).align_to(gene_bar, LEFT),
                         label("variable region: the barcode", 22).next_to(bc, UP, buff=0.12).align_to(bc, LEFT),
                         label("conserved", 20, C["muted"]).next_to(gene_bar, DOWN, buff=0.55).align_to(gene_bar, RIGHT))
        top = self.place(VGroup(gene_bar, bc, fwd, rev, names, regions), "A1", "gene", span="6x1")
        area = self.place(Rectangle(width=5, height=3.0, stroke_opacity=0), "B2", "pcr", span="4x2")

        def strands(n):
            g = VGroup(*[Line(LEFT * 0.45, RIGHT * 0.45, stroke_width=8, color=C["fg"]) for _ in range(n)])
            return g.arrange_in_grid(rows=max(1, n // 4), cols=min(n, 4), buff=(0.35, 0.3)).move_to(area)
        counter = self.place(label("PCR cycle 0: 1 copy", 30), "B4", "counter", span="4x1")
        with self.say("s6") as t:
            self.play(FadeIn(gene_bar), FadeIn(bc), FadeIn(regions), self.tag("schematic"), run_time=1.0)
            self.play(GrowArrow(fwd), GrowArrow(rev), FadeIn(names), run_time=1.2)
            self.play(FadeIn(counter), run_time=0.5)
            now = strands(1)
            self.play(TransformFromCopy(bc, now[0]), run_time=0.8)
            step = max((t.duration - 5.1) / 4, 0.6)
            for k in range(1, 5):
                nxt = strands(2 ** k)
                self.play(TransformFromCopy(now, nxt[len(now):]), Transform(now, nxt[:len(now)]),
                          Transform(counter, label(f"PCR cycle {k}: {2 ** k} copies", 30).move_to(counter)), run_time=step)
                self.remove(now); now = nxt; self.add(now)
            self.play(Transform(counter, label(f"PCR cycle {P.CYCLES}: many copies", 30).move_to(counter)),
                      now.animate.set_opacity(0.5), run_time=1.6)
        self.play(FadeOut(VGroup(now, counter, top)), run_time=0.6)
        self.release("pcr", "gene", "counter")

        # s7: fold bias per taxon after 35 cycles, on a log scale; beyond fourfold either way lit
        lb = np.log2(D["bias"])
        W = 10.0
        x = lambda v: v / 5 * W / 2                                # log2 -5..5 -> -W/2..W/2
        axis = Line([-W / 2, 0, 0], [W / 2, 0, 0], color=C["muted"], stroke_width=2)
        ticks = VGroup(*[VGroup(Line([x(v), -0.08, 0], [x(v), 0.08, 0], color=C["muted"], stroke_width=2),
                                label(s, 22, C["muted"]).next_to([x(v), 0, 0], DOWN, buff=0.18))
                         for v, s in ((-4, "1/16"), (-2, "1/4"), (0, "1"), (2, "4"), (4, "16"))])
        far = np.abs(lb) > 2
        bins = np.floor(lb / 0.25)
        dots = VGroup()
        for i in np.argsort(lb):
            d_ = Dot(radius=0.07, color=COL[i], fill_opacity=1 if far[i] else 0.35)
            if far[i]:
                d_.set_stroke(C["fg"], width=2.5, opacity=1)
            dots.add(d_)
        stack = {}
        for d_, i in zip(dots, np.argsort(lb)):
            b_ = bins[i]; k = stack.get(b_, 0); stack[b_] = k + 1
            d_.move_to([x(np.clip((b_ + 0.5) * 0.25, -5, 5)), 0.16 + k * 0.17, 0])
        lines = VGroup(*[DashedLine([x(v), -0.05, 0], [x(v), 1.9, 0], color=C["fg"], dash_length=0.08, stroke_width=2)
                         for v in (-2, 2)])
        ttl = label(f"fold bias per taxon after {P.CYCLES} PCR cycles (log scale)", 24).next_to(axis, UP, buff=2.2)
        xl = label("1 = no bias;  dashed: fourfold either way;  ringed: beyond fourfold", 20, C["muted"]).next_to(ticks, DOWN, buff=0.15)
        plot = self.place(VGroup(axis, ticks, dots, lines, ttl, xl), "A1", "bias", span="6x3")
        head = self.place(VGroup(label(f"one study, gut communities, {P.CYCLES} cycles: 1 taxon in 5 more than fourfold off", 26),
                                 label(f"simulated: {int(far.sum())} of {N} taxa", 24, C["muted"]))
                          .arrange(DOWN, buff=0.12), "A4", "head", span="6x1")
        with self.say("s7") as t:
            self.play(FadeIn(VGroup(axis, ticks, ttl, xl)), self.tag("simulated"), run_time=1.0)
            self.play(LaggedStart(*[FadeIn(d_, scale=0.5) for d_ in dots], lag_ratio=0.02), run_time=max(t.duration * 0.4, 2))
            self.play(Create(lines), FadeIn(head[0]), run_time=1.2)
            self.play(FadeIn(head[1]), *[Indicate(dots[j], scale_factor=1.6, color=dots[j].get_color())
                                         for j, i in enumerate(np.argsort(lb)) if far[i]], run_time=1.6)
        self.play(FadeOut(VGroup(plot, head)), run_time=0.6)
        self.release("bias", "head")

        # s8: the chart through the steps: cells -> DNA -> 16S copies -> barcodes (same taxon order)
        names = ["cells", "DNA", "16S copies", "barcodes"]
        keys = ["true", "dna", "templates", "pool"]
        titles = ["share of cells per taxon", "share of extracted DNA", "share of 16S gene copies",
                  "share of barcodes: no longer the cells' shares"]
        row = VGroup()
        for k, n in enumerate(names):
            row.add(label(n, 28, C["muted"]))
            if k < 3:
                row.add(label("→", 28, C["muted"]))
        row.arrange(RIGHT, buff=0.3)
        steps = [row[2 * k] for k in range(4)]
        self.place(row, "A1", "steps", span="6x1")
        ch = self.place(chart(D["true"], titles[0], w=8.6, h=3.0, ymax=0.55, xlab="taxa, in the order of the cell counts"),
                        "A2", "chart", span="6x2")
        b = ch[2]
        t1, t3 = D["true"][0], D["true"][2]
        p1, p3 = D["pool"][0], D["pool"][2]
        notes = self.place(VGroup(label(f"taxon 1: {pct(t1)} → {pct(p1)}", 28, COL[0]),
                                  label(f"taxon 3: {pct(t3)} → {pct(p3)}", 28, COL[2])).arrange(RIGHT, buff=1.2),
                           "A4", "notes", span="6x1")
        with self.say("s8") as t:
            self.play(FadeIn(ch), FadeIn(row), steps[0].animate.set_color(C["fg"]), run_time=1.0)
            step = max(t.duration * 0.55 / 3, 1.2)
            for k in range(1, 4):
                new = bars(D[keys[k]], w=8.6, h=3.0, ymax=0.55).match_width(b).move_to(b, aligned_edge=DL)
                self.play(Transform(b, new), Transform(ch[3], label(titles[k], 24).move_to(ch[3])),
                          steps[k - 1].animate.set_color(C["muted"]), steps[k].animate.set_color(C["fg"]), run_time=step)
            self.play(FadeIn(notes[0]), Indicate(b[0], color=C["fg"]), run_time=1.2)
            self.play(FadeIn(notes[1]), Indicate(b[2], color=C["fg"]), run_time=1.2)


class Sequence(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(13)
        # s9: three samples; each one's barcodes get its own index pattern; all pooled
        tubes, kids = VGroup(), []
        for k, s in enumerate("ABC"):
            box = RoundedRectangle(width=2.4, height=1.9, corner_radius=0.25).set_stroke(SAMPLE, width=3)
            name = label(f"sample {s}", 24).next_to(box, UP, buff=0.12)
            amps = VGroup(*[Line(LEFT * 0.27, RIGHT * 0.27, stroke_width=7, color=COL[int(i)])
                            for i in rng.choice(6, 6)]).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.2)).move_to(box)
            tubes.add(VGroup(box, name, amps)); kids.append(amps)
        tubes.arrange(RIGHT, buff=0.9)
        self.place(tubes, "A1", "tubes", span="6x2")
        pool_box = RoundedRectangle(width=4.2, height=1.5, corner_radius=0.25).set_stroke(C["muted"], width=2)
        pool = self.place(VGroup(pool_box, label("one pooled run", 22, C["muted"]).next_to(pool_box, DOWN, buff=0.1)),
                          "B3", "pool", span="4x1")
        key = self.place(VGroup(label("index tags name the sample; samples pooled", 30),
                                label("white squares: the index tag, one pattern per sample", 22, C["muted"]))
                         .arrange(DOWN, buff=0.1), "A4", "key", span="6x1")
        tagged_amps = []
        for k, amps in enumerate(kids):
            for a in amps:
                tg = index_tag(k).next_to(a, LEFT, buff=0.05)
                tagged_amps.append(VGroup(tg, a))
        order = rng.permutation(len(tagged_amps))
        spots = [None] * len(tagged_amps)
        for slot, j in enumerate(order):                      # 6 x 3 grid, samples mixed
            c, r = slot % 6, slot // 6
            spots[j] = pool_box.get_center() + np.array([(c - 2.5) * pool_box.width / 6.6, (1 - r) * pool_box.height / 3.8, 0])
        with self.say("s9") as t:
            self.play(FadeIn(tubes), self.tag("schematic"), run_time=1.0)
            self.play(*[FadeIn(g[0], shift=RIGHT * 0.1) for g in tagged_amps], run_time=max(t.duration * 0.35, 1.5))
            self.play(FadeIn(pool), FadeIn(key), run_time=0.6)
            self.play(*[g.animate.scale(0.8).move_to(p) for g, p in zip(tagged_amps, spots)],
                      *[FadeOut(tb[0]) for tb in tubes], *[FadeOut(tb[1]) for tb in tubes], run_time=max(t.duration * 0.35, 1.5))
        self.release("tubes")
        pooled = VGroup(*tagged_amps)

        # s10: the sequencer reads a random sample of the pool; depths come out uneven
        seq = RoundedRectangle(width=2.6, height=1.2, corner_radius=0.2).set_stroke(C["fg"], width=3)
        seqg = self.place(VGroup(seq, label("sequencer", 26).move_to(seq)), "A1", "seq", span="2x1")
        depth = SKETCH_DEPTH
        meters = VGroup()
        for k, s in enumerate("ABC"):
            frame = Rectangle(width=4.5, height=0.36).set_stroke(C["rule"], width=2)
            fill = Rectangle(width=4.5 * depth[k], height=0.36, stroke_width=0, fill_color=SAMPLE, fill_opacity=0.85) \
                .align_to(frame, LEFT)
            meters.add(VGroup(label(f"sample {s}", 24), index_tag(k), VGroup(frame, fill)).arrange(RIGHT, buff=0.25))
        meters.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        edge = max(m[1].get_right()[0] for m in meters) + 0.25
        for m in meters:                                      # bars share one left edge
            m[2].shift(RIGHT * (edge - m[2].get_left()[0]))
        mg = self.place(meters, "D1", "meters", span="3x2")
        fills = [m[2][1] for m in meters]
        for f in fills:
            f.save_state(); f.stretch(0.001, 0, about_edge=LEFT)
        term = self.place(label("sequencing depth = reads per sample", 30), "A4", "key2", span="6x1")
        with self.say("s10") as t:
            self.play(FadeOut(key), pool[0].animate.set_stroke(opacity=0.5), pool[1].animate.set_opacity(0.6),
                      pooled.animate.set_opacity(0.6), FadeIn(seqg), run_time=0.8)
            self.release("key")
            self.play(FadeIn(meters), run_time=0.6)
            arrow = Arrow(pool_box.get_top(), seq.get_bottom(), buff=0.15, color=C["muted"], stroke_width=4)
            alab = label("a random draw", 22, C["muted"]).next_to(arrow.get_center(), DOWN + LEFT, buff=0.25)
            self.play(GrowArrow(arrow), FadeIn(alab), run_time=0.6)
            picks = rng.choice(len(tagged_amps), 10, replace=False)
            flying = [tagged_amps[j].copy().set_opacity(1) for j in picks]
            self.add(*flying)
            self.play(LaggedStart(*[f.animate.move_to(seq.get_center()).scale(0.5).set_opacity(0) for f in flying], lag_ratio=0.25),
                      *[Restore(f) for f in fills], run_time=max(t.duration * 0.5, 2))
            self.remove(*flying)
            self.play(FadeIn(term), run_time=0.8)
        self.play(FadeOut(VGroup(pool, pooled, mg, term, arrow, alab)), run_time=0.6)
        self.release("pool", "meters", "key2")

        # s11: demultiplexing: reads sorted into bins by index; one lands in the wrong bin
        bins_ = VGroup()
        for k, s in enumerate("ABC"):
            box = Rectangle(width=2.6, height=1.8).set_stroke(SAMPLE, width=3)
            head = VGroup(label(f"sample {s}", 24), index_tag(k)).arrange(RIGHT, buff=0.2).next_to(box, UP, buff=0.12)
            bins_.add(VGroup(box, head))
        bins_.arrange(RIGHT, buff=0.8)
        self.place(bins_, "A2", "bins", span="6x2")
        key3 = self.place(label("demultiplexing: reads sorted by index", 30), "A4", "key3", span="6x1")
        plan = [(k, k) for k in (0, 1, 2, 0, 1, 2, 0, 1, 2)] + [(0, 1)]   # last read: sample A's, sorted into B
        reads, slots = VGroup(), []
        fill_n = [0, 0, 0]
        for k, dest in plan:
            r = tagged(COL[int(rng.integers(0, 6))], k).scale(0.8).move_to(seqg.get_center())
            reads.add(r)
            box = bins_[dest][0]
            slots.append(box.get_top() + DOWN * (0.35 + 0.42 * fill_n[dest]))
            fill_n[dest] += 1
        wrong = reads[-1]
        flag = label("misassigned (exaggerated here)", 22, C["muted"])
        with self.say("s11") as t:
            self.play(FadeIn(bins_), FadeIn(key3), run_time=0.8)
            self.play(LaggedStart(*[r.animate.move_to(s) for r, s in zip(reads[:-1], slots[:-1])], lag_ratio=0.25),
                      run_time=max(t.duration * 0.45, 2))
            self.play(wrong.animate.move_to(slots[-1]), run_time=1.0)
            flag.next_to(bins_[1][0], DOWN, buff=0.15)
            self.play(Circumscribe(wrong, color=C["fg"]), FadeIn(flag), run_time=1.2)


class Reads(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(17)
        # s12: merge each read pair; drop short or low-quality reads (every bar labelled)
        frag = Rectangle(width=6.0, height=0.26, stroke_width=0, fill_color=C["fg"], fill_opacity=0.35)
        fl = label("one DNA fragment", 20, C["muted"]).next_to(frag, LEFT, buff=0.2)
        r1 = Arrow(LEFT * 2.0, RIGHT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, UP, buff=0.15).align_to(frag, LEFT)
        r2 = Arrow(RIGHT * 2.0, LEFT * 2.0, buff=0, color=C["fg"], stroke_width=6).next_to(frag, DOWN, buff=0.15).align_to(frag, RIGHT)
        rl = VGroup(label("read 1", 20, C["muted"]).next_to(r1, RIGHT, buff=0.15),
                    label("read 2", 20, C["muted"]).next_to(r2, LEFT, buff=0.15))
        pair = self.place(VGroup(fl, frag, r1, r2, rl), "A1", "pair", span="6x1")
        merged = Rectangle(width=frag.width, height=frag.height, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(frag)
        ml = label("merged read", 20).next_to(merged, RIGHT, buff=0.2)
        good = [Rectangle(width=2.4, height=0.2, stroke_width=0, fill_color=C["fg"], fill_opacity=1) for _ in range(3)]
        short = Rectangle(width=0.9, height=0.2, stroke_width=0, fill_color=C["fg"], fill_opacity=1)
        poor = VGroup(*[Rectangle(width=0.3, height=0.2, stroke_width=0, fill_color=C["fg"],
                                  fill_opacity=float(o)) for o in rng.uniform(0.1, 0.6, 8)]).arrange(RIGHT, buff=0)
        rows = VGroup(good[0], short, good[1], poor, good[2]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        notes = VGroup(*[label(s, 22, C["muted"]) for s in
                         ("kept", "too short: dropped", "kept", "low quality (faint): dropped", "kept")])
        for n, r in zip(notes, rows):
            n.next_to(r, RIGHT, buff=0.3).align_to(rows, RIGHT).shift(RIGHT * 0.3 + RIGHT * n.width)
        head = label("merged reads, filtered", 22, C["muted"]).next_to(rows, UP, buff=0.25).align_to(rows, LEFT)
        filt = self.place(VGroup(head, rows, notes), "B2", "filter", span="4x2")
        key = self.place(label("merge read pairs; drop short or low-quality reads", 30), "A4", "key", span="6x1")
        with self.say("s12") as t:
            self.play(FadeIn(frag), FadeIn(fl), FadeIn(key), self.tag("schematic"), run_time=0.8)
            self.play(GrowArrow(r1), GrowArrow(r2), FadeIn(rl), run_time=1.2)
            self.play(ReplacementTransform(VGroup(r1, r2), merged), FadeOut(rl), FadeIn(ml), run_time=1.2)
            self.play(FadeIn(head), FadeIn(rows), FadeIn(notes), run_time=max(t.duration * 0.25, 1))
            self.play(FadeOut(VGroup(short, notes[1]), shift=DOWN * 0.3), FadeOut(VGroup(poor, notes[3]), shift=DOWN * 0.3),
                      run_time=1.2)
        self.play(FadeOut(VGroup(fl, frag, merged, ml, head, *good, notes[0], notes[2], notes[4], key)), run_time=0.6)
        self.release("pair", "filter", "key")

        # s13: near-copies with errors collapse onto one exact sequence, an ASV
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
                      label("OTUs: clustered at 97% instead", 26, C["muted"]),
                      VGroup(label("one soil dataset:", 26, C["muted"]),
                             label("8,270 to 16,609 ASVs, by pipeline", 26, C["muted"])).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.place(side, "D1", "side", span="3x3")
        legend2.move_to(legend, aligned_edge=LEFT)
        key2 = self.place(label("denoising: errors folded into ASVs", 30), "A4", "key2", span="6x1")
        with self.say("s13") as t:
            self.play(FadeIn(ctitle), FadeIn(cloud), FadeIn(legend), FadeIn(key2), run_time=1.2)
            asv.move_to(cloud)
            self.play(ReplacementTransform(cloud, asv), FadeOut(ctitle), Transform(legend, legend2),
                      run_time=max(t.duration * 0.3, 1.5))
            asv_l.next_to(asv, UP, buff=0.25)
            self.play(FadeIn(asv_l), FadeIn(side[1]), run_time=1.0)
            self.play(FadeIn(side[2]), run_time=1.0)
        self.play(FadeOut(VGroup(asv, asv_l, side, key2)), run_time=0.6)
        self.release("cloud", "side", "key2")

        # s14: a chimera: a copy starts on one template and finishes on another; a detector catches some
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
        filt = self.place(VGroup(dl, many, dk), "A3", "detector", span="6x1")
        key3 = self.place(label("chimera: half of one template, half of another", 30), "A4", "key3", span="6x1")
        with self.say("s14") as t:
            self.play(FadeIn(temps), FadeIn(tl), FadeIn(key3), run_time=1.0)
            self.play(GrowFromEdge(h1, LEFT), run_time=1.2)
            self.play(h1.animate.next_to(h2, LEFT, buff=0), FadeIn(h2), run_time=1.2)
            self.play(ReplacementTransform(VGroup(h1, h2), chim), FadeIn(cl), run_time=1.0)
            self.play(FadeIn(dl), FadeIn(many), run_time=max(t.duration * 0.2, 0.8))
            self.play(*[Create(Cross(Square(side_length=0.45).move_to(many[j]), stroke_color=C["fg"], stroke_width=4)) for j in caught],
                      FadeIn(dk), run_time=1.4)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not getattr(self, "_tag", None)], run_time=0.6)
        self.release("temps", "chimera", "detector", "key3")

        # s15: classify against a reference database, then count into a table of taxa by samples
        q = label("TACGGAGGGT…", 22, COL[0], font=MONO)
        ql = label("ASV", 22).next_to(q, UP, buff=0.1)
        shelf = VGroup(*[Rectangle(width=2.2, height=0.16, stroke_width=0, fill_color=C["muted"], fill_opacity=0.6)
                         for _ in range(7)]).arrange(DOWN, buff=0.08)
        shl = label("reference database", 22, C["muted"]).next_to(shelf, UP, buff=0.12)
        ref = VGroup(shelf, shl)
        named = label("→ taxon 1", 24, COL[0])
        left = self.place(VGroup(VGroup(q, ql), ref).arrange(RIGHT, buff=0.9), "A1", "classify", span="3x2")
        named.next_to(left, DOWN, buff=0.3)
        self.track(named, "named")
        # the table: rows are taxa (coloured squares), columns samples; each cell a bar for its count
        cols_ = VGroup(*[VGroup(label(s, 24), index_tag(k)).arrange(DOWN, buff=0.08) for k, s in enumerate("ABC")])
        rows_ = VGroup(*[Square(side_length=0.22, stroke_width=0, fill_color=COL[i], fill_opacity=1) for i in range(6)])
        cells_ = VGroup()
        for i in range(6):
            for k in range(3):
                v = float(D["pool"][i] / D["pool"][0]) * SKETCH_DEPTH[k] * rng.uniform(0.7, 1.0)
                cells_.add(Rectangle(width=max(1.1 * v, 0.04), height=0.18, stroke_width=0, fill_color=SAMPLE, fill_opacity=0.8))
        table = VGroup()
        for k, c in enumerate(cols_):
            c.move_to([0.9 + k * 1.5, 0.6, 0])
        for i, r in enumerate(rows_):
            r.move_to([0, -i * 0.42, 0])
            for k in range(3):
                cells_[i * 3 + k].move_to([0.35 + k * 1.5, -i * 0.42, 0], aligned_edge=LEFT)
        more = label("…", 28, C["muted"]).move_to([0, -6 * 0.42, 0])
        table.add(cols_, rows_, cells_, more)
        tt = label("count table: taxa by samples", 24, C["muted"]).next_to(table, UP, buff=0.25)
        self.place(VGroup(table, tt), "D1", "table", span="3x3")
        key4 = self.place(VGroup(label("classifier and reference database, then a count table", 28),
                                 label("our simulation leaves out the false taxa these steps add", 22, C["muted"]))
                          .arrange(DOWN, buff=0.1), "A4", "key4", span="6x1")
        with self.say("s15") as t:
            self.play(FadeIn(VGroup(q, ql)), FadeIn(ref), FadeIn(key4[0]), run_time=1.0)
            arr = Arrow(q.get_right(), shelf.get_left(), buff=0.1, color=C["muted"], stroke_width=3)
            cls = label("classifier: best match", 20, C["muted"]).next_to(q, DOWN, buff=0.15)
            self.play(GrowArrow(arr), FadeIn(cls), run_time=0.8)
            self.track(VGroup(arr, cls), "classifier")
            self.play(Indicate(shelf[2], color=C["fg"]), FadeIn(named), run_time=1.0)
            self.play(FadeIn(tt), FadeIn(cols_), FadeIn(rows_), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(c, LEFT) for c in cells_], lag_ratio=0.05), FadeIn(more),
                      run_time=max(t.duration * 0.3, 1.5))
            self.play(FadeIn(key4[1]), run_time=0.8)


class Depth(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(9)
        # s16: which taxa turn up at three depths (rows aligned: labels right-aligned, strips left-aligned)
        texts = VGroup(*[label(f"{dep:,} reads: {int((D['runs'][dep] > 0).sum())} of {N} taxa", 28) for dep in P.DEPTHS])
        strips = VGroup(*[strip(D["runs"][dep] > 0) for dep in P.DEPTHS])
        for k in range(3):
            texts[k].move_to([0, -(2 - k) * 1.2, 0], aligned_edge=RIGHT)
            strips[k].move_to([0.5, -(2 - k) * 1.2, 0], aligned_edge=LEFT)
        grid = self.place(VGroup(texts, strips), "A1", "rows", span="6x3")
        key = self.place(label("filled: found    dim outline: never drawn", 24, C["muted"]), "A4", "key", span="6x1")
        with self.say("s16") as t:
            self.play(FadeIn(key), self.tag("simulated"), run_time=0.6)
            for k in (2, 1, 0):   # the narration goes from deep to shallow
                self.play(FadeIn(texts[k]), FadeIn(strips[k]), run_time=max((t.duration - 0.6) / 3 - 0.2, 1))
        self.play(FadeOut(VGroup(grid, key)), run_time=0.6)
        self.release("rows", "key")

        # s17: 30 repeat sequencings per depth: a share's spread narrows with depth, centred on the pool's share
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
        rare = 40
        p1, d1 = panel(0, 0.6, "taxon 1, common", COL[0], lambda v: f"{v:.1%}")
        ymax2 = float(np.ceil(max(x.max() for x in draws[rare]) * 1.1 * 1000) / 1000)   # covers every draw
        p2, d2 = panel(rare, ymax2, f"taxon {rare + 1}, rare (note the smaller scale)", C["muted"], lambda v: f"{v:.1%}")
        self.place(VGroup(p1, d1), "A1", "p1", span="3x3")
        self.place(VGroup(p2, d2), "D1", "p2", span="3x3")
        key2 = self.place(VGroup(label("more reads: a tighter spread, the same centre", 26),
                                 label(f"each dot: one of {REP} repeat sequencings;  dashed: share of the barcode pool", 22, C["muted"]))
                          .arrange(DOWN, buff=0.12),
                          "A4", "key2", span="6x1")
        with self.say("s17") as t:
            self.play(FadeIn(p1), FadeIn(p2), FadeIn(key2), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(x) for x in d1], lag_ratio=0.01), run_time=max(t.duration * 0.35, 1.5))
            self.play(LaggedStart(*[FadeIn(x) for x in d2], lag_ratio=0.01), run_time=max(t.duration * 0.65 - 1.2, 1.5))


class Rarefy(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        # s18: two samples from the same soil (white: a sample is not a taxon)
        def card(name, counts):
            head = label(f"{name} sample: {int(counts.sum()):,} reads", 28)
            n = label(f"{int((counts > 0).sum())} taxa found", 34, weight=BOLD)
            return VGroup(head, strip(counts > 0, colour=SAMPLE), n).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        title = self.place(VGroup(label("same soil, two samples, each its own draw", 30, C["muted"]),
                                  label("richness = number of taxa found;  filled: found, dim outline: missed", 22, C["muted"]))
                           .arrange(DOWN, buff=0.12), "A1", "title", span="6x1")
        deep = self.place(card("deep", D["deep"]), "A2", "deep", span="3x2")
        shal = self.place(card("shallow", D["shallow"]), "D2", "shallow", span="3x2")
        with self.say("s18") as t:
            self.play(FadeIn(title), self.tag("simulated"), run_time=0.8)
            self.play(FadeIn(deep), run_time=1.0)
            self.play(FadeIn(shal), run_time=1.0)

        # s19: subsample the deep sample to 2,000 reads, 200 times
        lo, hi = int(D["rare_draws"].min()), int(D["rare_draws"].max())
        ymax = int(np.ceil(np.unique(D["rare_draws"], return_counts=True)[1].max() / 10) * 10)
        ax = Axes(x_range=[lo - 1, hi + 1, 2], y_range=[0, ymax, ymax / 2], x_length=9.0, y_length=2.6, tips=False,
                  axis_config=dict(color=C["muted"], include_ticks=False))
        vals, cnts = np.unique(D["rare_draws"], return_counts=True)
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
        htxt = self.place(label(f"deep sample rarefied to {P.SHALLOW:,} reads, {P.DRAWS} times: "
                                f"{round(D['rare_mean'])} taxa on average", 28), "A1", "htxt", span="6x1")
        with self.say("s19") as t:
            self.play(FadeOut(VGroup(deep, shal, title)), run_time=0.6)
            self.release("deep", "shallow", "title")
            self.play(FadeIn(htxt), FadeIn(ax), FadeIn(xt), FadeIn(xtitle), FadeIn(ylab), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in hist], lag_ratio=0.08), FadeIn(mean), FadeIn(mean_l), run_time=max(t.duration * 0.5, 2))
            self.play(FadeIn(band), FadeIn(blab), Create(mark), FadeIn(mlab), run_time=max(t.duration * 0.5 - 1.4, 1.2))

        # s20: what rarefying does not fix, and what it costs
        does = label("rarefying evens out depth, nothing else", 30, weight=BOLD)
        lines = VGroup(
            label("extraction, copy-number and PCR bias: still in every read", 26),
            label("and that bias can differ between samples", 26, C["muted"]),
            label("taxa the shallow sample missed: still missed", 26),
            label(f"{P.DEEP - P.SHALLOW:,} of the deep sample's reads set aside", 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        with self.say("s20") as t:
            self.play(FadeOut(VGroup(hgroup, htxt)), run_time=0.8)
            self.release("hist", "htxt")
            lim = self.place(VGroup(does, lines).arrange(DOWN, aligned_edge=LEFT, buff=0.35), "A1", "limits", span="6x2")
            self.play(FadeIn(does), self.tag("summary"), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.2) for x in lines], lag_ratio=0.7),
                      run_time=max(t.duration - 1.6, 2))

        # s21: the open debate, and what shares cannot show
        more = VGroup(
            label("whether to rarefy: still debated, and it differs by measure", 26),
            label("richness, differences between samples, tests of single taxa", 22, C["muted"]),
            label("total load: shares cannot show it; spike-ins or cell counts can", 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        with self.say("s21") as t:
            self.place(more, "A3", "more", span="6x2").align_to(lim, LEFT)
            self.play(FadeIn(more[0], shift=RIGHT * 0.2), run_time=1.0)
            self.play(FadeIn(more[1]), run_time=max(t.duration * 0.4, 1.5))
            self.play(FadeIn(more[2], shift=RIGHT * 0.2), run_time=1.0)
        self.wait(0.8)
