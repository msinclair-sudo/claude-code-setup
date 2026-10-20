"""Rarefaction in a metabarcoding experiment, tier 4: four chapters.

Narration comes from storyboard.yaml (say("sN")); every count from ../pipeline.py (simulated, seed 7).
Drawings of soil, cells, genomes, PCR and the sequencer are schematic; the charts are the simulation's
numbers. Colours mean taxa only (the six commonest; the rest grey); the two samples are white and told
apart by label and line style.
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
D = P.data()
N = P.N_TAXA
HUES = [C["accent"], C["accent2"], "#7BC47F", "#B79CE8", "#E8CF6A", "#E88FA8"]
COL = [HUES[i] if i < len(HUES) else C["muted"] for i in range(N)]
SAMPLE = C["fg"]              # samples are never a taxon colour
SOIL = "#7A5C3E"


def label(s, size=28, color=None, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color or C["fg"], weight=weight)


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


def cell(i, rng):
    """A schematic bacterium: rods for odd taxa, cocci for even ones."""
    if i % 2:
        m = RoundedRectangle(width=0.34, height=0.13, corner_radius=0.065).rotate(rng.uniform(0, PI))
    else:
        m = Circle(radius=0.075)
    return m.set_stroke(width=0).set_fill(COL[i], opacity=0.95)


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
        cap = self.place(VGroup(label("a droplet of soil", 28), label(f"{P.CELLS:,} cells, {N} taxa", 24, C["muted"]))
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
        self.wait(0.6)


class Barcode(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        # s3: a cell opens to its circular genome; the 16S gene lights up
        body = RoundedRectangle(width=4.2, height=2.0, corner_radius=1.0).set_stroke(COL[0], width=4).set_fill(COL[0], opacity=0.15)
        genome = Circle(radius=0.6).set_stroke(C["fg"], width=4)
        cellg = self.place(VGroup(body, genome), "B1", "cell", span="4x3")
        big = Circle(radius=2.0).set_stroke(C["fg"], width=5).move_to(cellg.get_center())
        gene = Arc(radius=2.0, start_angle=PI / 3, angle=0.32, stroke_width=16, color=C["fg"]).shift(cellg.get_center())
        glab = label("16S rRNA gene", 30).next_to(gene, UP + RIGHT, buff=0.15)
        gnl = label("circular genome", 26, C["muted"]).next_to(big, DOWN, buff=0.25)
        with self.say("s3") as t:
            self.play(FadeIn(cellg), self.tag("schematic"), run_time=1)
            self.play(FadeOut(body), Transform(genome, big), FadeIn(gnl), run_time=1.6)
            self.play(Create(gene), FadeIn(glab), run_time=1.2)
            self.wait(max(t.duration - 3.8, 0.5))

        # s4: copy number differs: taxon 1 has 8 copies, taxon 3 has 1
        def ring(n, colour, centre):
            c = Circle(radius=1.35).set_stroke(C["fg"], width=4).move_to(centre)
            arcs = VGroup(*[Arc(radius=1.35, start_angle=k * TAU / n + 0.2, angle=0.26, stroke_width=14, color=colour)
                            .shift(centre) for k in range(n)])
            return VGroup(c, arcs)
        left, right = cellg.get_center() + LEFT * 2.7 + UP * 0.3, cellg.get_center() + RIGHT * 2.7 + UP * 0.3
        g1, g3 = ring(int(D["copies"][0]), COL[0], left), ring(int(D["copies"][2]), COL[2], right)
        l1 = label(f"taxon 1: {D['copies'][0]} copies", 28, COL[0]).next_to(g1, DOWN, buff=0.3)
        l3 = label(f"taxon 3: {D['copies'][2]} copy", 28, COL[2]).next_to(g3, DOWN, buff=0.3)
        rng_note = label("bacterial genomes carry 1 to about 15 copies", 24, C["muted"]).next_to(VGroup(l1, l3), DOWN, buff=0.35)
        with self.say("s4") as t:
            self.play(FadeOut(glab), FadeOut(gene), FadeOut(gnl), Transform(genome, g1[0]), run_time=1.2)
            self.release("cell")   # its genome has become taxon 1's
            self.play(Create(g1[1]), FadeIn(l1), run_time=1.4)
            self.track(VGroup(g1, l1), "g1")
            self.play(FadeIn(g3), FadeIn(l3), run_time=1.2)
            self.track(VGroup(g3, l3), "g3")
            self.play(FadeIn(rng_note), run_time=0.8)
            self.wait(max(t.duration - 4.6, 0.5))
        self.play(FadeOut(VGroup(genome, g1, g3, l1, l3, rng_note)), run_time=0.6)
        self.release("g1", "g3")

        # s5: the barcode, a short stretch of the 16S gene, doubled by PCR each cycle
        gene_bar = Rectangle(width=7.0, height=0.28, stroke_width=0, fill_color=C["fg"], fill_opacity=0.3)
        bc = Rectangle(width=1.4, height=0.28, stroke_width=0, fill_color=C["fg"], fill_opacity=1).move_to(gene_bar).shift(RIGHT * 0.9)
        top = self.place(VGroup(gene_bar, bc), "A1", "gene", span="6x1")
        gl = label("16S rRNA gene", 22, C["muted"]).next_to(gene_bar, UP, buff=0.12).align_to(gene_bar, LEFT)
        bl = label("barcode", 24).next_to(bc, UP, buff=0.12)
        area = self.place(Rectangle(width=5, height=3.2, stroke_opacity=0), "B2", "pcr", span="4x2")

        def strands(n):
            g = VGroup(*[Line(LEFT * 0.45, RIGHT * 0.45, stroke_width=8, color=C["fg"]) for _ in range(n)])
            return g.arrange_in_grid(rows=max(1, n // 4), cols=min(n, 4), buff=(0.35, 0.3)).move_to(area)
        counter = self.place(label("PCR cycle 0: 1 copy", 30), "B4", "counter", span="4x1")
        with self.say("s5") as t:
            self.play(FadeIn(top), FadeIn(gl), FadeIn(bl), FadeIn(counter), run_time=0.9)
            now = strands(1)
            self.play(TransformFromCopy(bc, now[0]), run_time=0.8)
            step = max((t.duration - 3.9) / 4, 0.6)
            for k in range(1, 5):
                nxt = strands(2 ** k)
                self.play(TransformFromCopy(now, nxt[len(now):]), Transform(now, nxt[:len(now)]),
                          Transform(counter, label(f"PCR cycle {k}: {2 ** k} copies", 30).move_to(counter)), run_time=step)
                self.remove(now); now = nxt; self.add(now)
            self.play(Transform(counter, label(f"PCR cycle {P.CYCLES}: millions of copies", 30).move_to(counter)),
                      now.animate.set_opacity(0.5), run_time=1.6)
        self.play(FadeOut(VGroup(now, counter, top, gl, bl)), run_time=0.6)
        self.release("pcr", "gene", "counter")

        # s6: the chart, from share of cells to share of barcodes (same taxon order)
        ch = self.place(chart(D["true"], "share of cells per taxon", w=8.6, h=3.6, xlab="taxa, in the order of the cell counts"),
                        "A1", "chart", span="5x3")
        b = ch[2]
        new = bars(D["pool"], w=8.6, h=3.6).match_width(b).move_to(b, aligned_edge=DL)
        t1 = label(f"taxon 1: {D['true'][0]:.0%} → {D['pool'][0]:.1%}", 28, COL[0])
        t3 = label(f"taxon 3: {D['true'][2]:.1%} → {D['pool'][2]:.1%}", 28, COL[2])
        notes = self.place(VGroup(t1, t3).arrange(DOWN, aligned_edge=LEFT, buff=0.25), "A4", "notes", span="4x1")
        new_title = label("share of barcodes per taxon, after PCR", 24).move_to(ch[3])
        with self.say("s6") as t:
            self.play(FadeIn(ch), self.tag("simulated"), run_time=1)
            self.play(Transform(b, new), Transform(ch[3], new_title), run_time=max(t.duration * 0.5, 2))
            self.play(FadeIn(t1), Indicate(b[0], color=C["fg"]), run_time=1.2)
            self.play(FadeIn(t3), Indicate(b[2], color=C["fg"]), run_time=max(t.duration * 0.5 - 2.4, 1))
        self.wait(0.6)


class Depth(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        rng = np.random.default_rng(9)
        # s7: the pool, read at random; each read matched to a taxon
        pool_box = RoundedRectangle(width=4.6, height=3.2, corner_radius=0.3).set_stroke(C["muted"], width=2)
        pick = rng.choice(N, size=130, p=D["pool"])
        strs = VGroup(*[Line(LEFT * 0.16, RIGHT * 0.16, stroke_width=5, color=COL[i]).rotate(rng.uniform(0, PI))
                        .move_to(pool_box.get_center() + np.array([rng.uniform(-2.0, 2.0), rng.uniform(-1.3, 1.3), 0]))
                        for i in pick])
        pool = self.place(VGroup(pool_box, strs), "A1", "pool", span="2x3")
        plab = label("barcodes after PCR", 24, C["muted"]).next_to(pool, DOWN, buff=0.15)
        seq = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.2).set_stroke(C["fg"], width=3)
        seqg = self.place(VGroup(seq, label("sequencer", 26).move_to(seq)), "C2", "seq", span="2x1")
        arrow = Arrow(pool.get_right(), seqg.get_left(), buff=0.2, color=C["muted"], stroke_width=4)
        chosen = [int(k) for k in rng.choice(len(strs), 12, replace=False)]
        reads = VGroup(*[VGroup(Line(LEFT * 0.4, RIGHT * 0.4, stroke_width=6, color=COL[pick[k]]),
                                label(f"taxon {pick[k] + 1}", 18, COL[pick[k]]))
                         .arrange(RIGHT, buff=0.15) for k in chosen]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        rcol = self.place(reads, "E1", "reads", span="2x3")
        rlab = label("a random draw of reads,\neach matched to a taxon", 22, C["muted"]).next_to(rcol, DOWN, buff=0.15)
        term = self.place(label("sequencing depth = reads per sample", 30), "A4", "term", span="6x1")
        with self.say("s7") as t:
            self.play(FadeIn(pool), FadeIn(plab), FadeIn(seqg), GrowArrow(arrow), self.tag("schematic"), run_time=1.2)
            self.play(LaggedStart(*[AnimationGroup(strs[k].animate.move_to(seq.get_center()).set_opacity(0), FadeIn(reads[j]))
                                    for j, k in enumerate(chosen)], lag_ratio=0.25), run_time=max(t.duration - 2.6, 2))
            self.play(FadeIn(rlab), FadeIn(term), run_time=1.0)
        self.play(FadeOut(VGroup(pool, plab, seqg, arrow, reads, rlab, term)), run_time=0.6)
        self.release("pool", "seq", "reads", "term")

        # s8: which taxa turn up at three depths (rows aligned: labels right-aligned, strips left-aligned)
        texts = VGroup(*[label(f"{dep:,} reads: {int((D['runs'][dep] > 0).sum())} of {N} taxa", 28) for dep in P.DEPTHS])
        strips = VGroup(*[strip(D["runs"][dep] > 0) for dep in P.DEPTHS])
        for k in range(3):
            texts[k].move_to([0, -k * 1.2, 0], aligned_edge=RIGHT)
            strips[k].move_to([0.5, -k * 1.2, 0], aligned_edge=LEFT)
        grid = self.place(VGroup(texts, strips), "A1", "rows", span="6x3")
        key = self.place(label("filled: found    dim outline: never drawn", 24, C["muted"]), "A4", "key", span="6x1")
        with self.say("s8") as t:
            self.play(FadeIn(key), self.tag("simulated"), run_time=0.6)
            for k in (2, 1, 0):   # the narration goes from deep to shallow
                self.play(FadeIn(texts[k]), FadeIn(strips[k]), run_time=max((t.duration - 0.6) / 3 - 0.2, 1))
        self.play(FadeOut(VGroup(grid, key)), run_time=0.6)
        self.release("rows", "key")

        # s9: 30 repeat sequencings per depth: a share's spread narrows with depth, centred on the pool's share
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
            return VGroup(ax, ref, xs, ys, ttl), dots
        rare = 40
        p1, d1 = panel(0, 0.6, "taxon 1, common (scale to 60%)", COL[0], lambda v: f"{v:.0%}")
        ymax2 = float(np.ceil(max(x.max() for x in draws[rare]) * 1.1 * 1000) / 1000)   # covers every draw
        p2, d2 = panel(rare, ymax2, f"taxon {rare + 1}, rare (scale to {ymax2:.2%})", C["muted"], lambda v: f"{v:.2%}")
        self.place(VGroup(p1, d1), "A1", "p1", span="3x3")
        self.place(VGroup(p2, d2), "D1", "p2", span="3x3")
        key2 = self.place(VGroup(label("more reads: a tighter spread, the same centre", 26),
                                 label(f"each dot: one of {REP} repeat sequencings;  dashed: share of the barcode pool", 22, C["muted"]))
                          .arrange(DOWN, buff=0.12),
                          "A4", "key2", span="6x1")
        with self.say("s9") as t:
            self.play(FadeIn(p1), FadeIn(p2), FadeIn(key2), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(x) for x in d1], lag_ratio=0.01), run_time=max(t.duration * 0.35, 1.5))
            self.play(LaggedStart(*[FadeIn(x) for x in d2], lag_ratio=0.01), run_time=max(t.duration * 0.65 - 1.2, 1.5))
        self.wait(0.6)


class Rarefy(ExplainScene):
    def construct(self):
        self.camera.background_color = C["bg"]
        # s10: two samples from the same soil (white: a sample is not a taxon)
        def card(name, counts):
            head = label(f"{name} sample: {int(counts.sum()):,} reads", 28)
            n = label(f"{int((counts > 0).sum())} taxa found", 34, weight=BOLD)
            return VGroup(head, strip(counts > 0, colour=SAMPLE), n).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        title = self.place(VGroup(label("same soil, two samples, each its own draw", 30, C["muted"]),
                                  label("richness = number of taxa found;  filled: found, dim outline: missed", 22, C["muted"]))
                           .arrange(DOWN, buff=0.12), "A1", "title", span="6x1")
        deep = self.place(card("deep", D["deep"]), "A2", "deep", span="3x2")
        shal = self.place(card("shallow", D["shallow"]), "D2", "shallow", span="3x2")
        with self.say("s10") as t:
            self.play(FadeIn(title), self.tag("simulated"), run_time=0.8)
            self.play(FadeIn(deep), run_time=1.0)
            self.play(FadeIn(shal), run_time=1.0)
            self.wait(max(t.duration - 2.8, 0.5))

        # s11: subsample the deep sample to 2,000 reads, 200 times
        lo, hi = int(D["rare_draws"].min()), int(D["rare_draws"].max())
        ax = Axes(x_range=[lo - 1, hi + 1, 2], y_range=[0, 40, 20], x_length=9.0, y_length=2.6, tips=False,
                  axis_config=dict(color=C["muted"], include_ticks=False))
        vals, cnts = np.unique(D["rare_draws"], return_counts=True)
        hist = VGroup(*[Rectangle(width=ax.x_length / (hi - lo + 2) * 0.85, height=ax.y_length * c / 40, stroke_width=0,
                                  fill_color=SAMPLE, fill_opacity=0.75).move_to(ax.c2p(v, 0), aligned_edge=DOWN)
                        for v, c in zip(vals, cnts)])
        x0, x1 = ax.c2p(D["rare_lo"] - 0.5, 0)[0], ax.c2p(D["rare_hi"] + 0.5, 0)[0]
        band = Rectangle(width=x1 - x0, height=ax.y_length, stroke_width=0, fill_color=C["fg"], fill_opacity=0.08) \
            .move_to([(x0 + x1) / 2, ax.c2p(0, 20)[1], 0])
        blab = label(f"middle 95%: {D['rare_lo']} to {D['rare_hi']}", 20, C["muted"]).next_to(band, UP, buff=0.08).align_to(band, LEFT)
        mark = DashedLine(ax.c2p(D["obs_shallow"], 0), ax.c2p(D["obs_shallow"], 40), color=SAMPLE, dash_length=0.08, stroke_width=4)
        mlab = label(f"shallow sample: {D['obs_shallow']}", 22).next_to(mark, UP, buff=0.45)
        mean = Triangle(fill_color=SAMPLE, fill_opacity=1, stroke_width=0).scale(0.1).rotate(PI).next_to(ax.c2p(D["rare_mean"], 0), DOWN, buff=0.02)
        mean_l = label(f"average {round(D['rare_mean'])}", 20).next_to(mean, LEFT, buff=0.1)
        xt = VGroup(*[label(str(v), 20, C["muted"]).next_to(ax.c2p(v, 0), DOWN, buff=0.22) for v in range(lo - lo % 2 + 2, hi + 1, 4) if abs(v - D["rare_mean"]) > 1.5])
        xtitle = label("taxa found in each subsample", 22, C["muted"]).next_to(xt, DOWN, buff=0.12)
        hgroup = self.place(VGroup(band, blab, ax, hist, mark, mlab, mean, mean_l, xt, xtitle), "A2", "hist", span="6x3")
        htxt = self.place(label(f"deep sample, rarefied to {P.SHALLOW:,} reads, {P.DRAWS} times: "
                                f"{round(D['rare_mean'])} taxa on average", 28), "A1", "htxt", span="6x1")
        with self.say("s11") as t:
            self.play(FadeOut(VGroup(deep, shal, title)), run_time=0.6)
            self.release("deep", "shallow", "title")
            self.play(FadeIn(htxt), FadeIn(ax), FadeIn(xt), FadeIn(xtitle), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in hist], lag_ratio=0.08), FadeIn(mean), FadeIn(mean_l), run_time=max(t.duration * 0.5, 2))
            self.play(FadeIn(band), FadeIn(blab), Create(mark), FadeIn(mlab), run_time=max(t.duration * 0.5 - 1.4, 1.2))

        # s12: what rarefying does, what it does not fix, and what it costs
        does = label(f"rarefying makes richness comparable at a common depth", 30, weight=BOLD)
        head = label("it does not fix:", 28, C["muted"])
        lines = VGroup(
            label("PCR and copy-number bias: still in every read", 28),
            label("rare taxa the shallow sample missed: still missed", 28),
            label(f"and it sets aside {P.DEEP - P.SHALLOW:,} of the deep sample's reads", 28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        with self.say("s12") as t:
            self.play(FadeOut(VGroup(hgroup, htxt)), run_time=0.8)
            self.release("hist", "htxt")
            self.place(VGroup(does, head, lines).arrange(DOWN, aligned_edge=LEFT, buff=0.4), "A1", "limits", span="6x3")
            self.play(FadeIn(does), self.tag("summary"), run_time=0.8)
            self.play(FadeIn(head), LaggedStart(*[FadeIn(x, shift=RIGHT * 0.2) for x in lines], lag_ratio=0.6),
                      run_time=max(t.duration - 1.6, 2))
        self.wait(0.8)
