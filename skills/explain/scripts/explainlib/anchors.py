"""ExplainScene: Manim scene with an anchor grid, storyboard narration and verify checks.

    from explainlib.anchors import ExplainScene      # import before manim (quiets warnings)
    from manim import *

    class Walk(ExplainScene):
        def construct(self):
            with self.say("s1") as t:                     # narration comes from storyboard.yaml
                self.play(Create(self.place(tree, "B1", "tree", span="4x3")), run_time=t.duration)

Grid: 6 columns A-F by 4 rows 1-4 over the frame, A1 top left; `span="CxR"`
covers C columns and R rows from the given cell. place() scales an object down
to fit its cells (logged as a warning) and records when it appeared.

At the end of every say(...) block the segment's `verify` list is checked:
  inside_frame: all            every visible object inside the frame
  no_overlap: [a, b] | all     named objects' bounding boxes do not intersect
  order: [a, b]                a was placed before b
  hold_min_s: 2                every object released in this segment stayed >= 2 s
Results go to <report>/checks/scene-<Class>.json; `x check` reads them.

Inside a segment, attach each move to the words that name it. The storyboard declares the events
(`sync: {pool: "The samples are pooled"}`, a phrase that occurs once in the narration) and the scene
tags the play that shows each one:
    with self.say("s16") as t:
        self.play(pour, run_time=self.left(t, 0, cap=1.5), sync="pool")   # starts when "The samples..." does
        self.at(t, 1, "a random draw")                       # a cue the code chooses: hold until a word
        self.play(draw, run_time=self.left(t, 1))
A tagged play waits for its phrase, so it never starts early; if the picture is still busy when the
phrase is spoken, the start is late. Every anchor and cue becomes a row in the scene log ("sync"),
and `x check` writes them to checks/sync.json. Faults: late by more than the tolerance (storyboard
`sync_tolerance`, default 0.5 s), a declared event never played, events played out of the order they
are spoken. A phrase at a sentence's start is exact; inside a sentence it is estimated (timing.py,
about 0.25 s). say() warns when a segment of two or more sentences has no anchor or cue.
Set EXPLAIN_STRICT=1 to raise on the first failure instead.
"""
import json
import os
from contextlib import contextmanager
from pathlib import Path

from .kokoro_service import KokoroService, spans as clip_spans  # noqa: F401  (quiets sox/phonemizer on import)
from . import report as _report
from . import timing

from manim import DOWN, LEFT, RIGHT, UP, config  # noqa: E402
from manim_voiceover import VoiceoverScene  # noqa: E402

COLS, ROWS, MARGIN = "ABCDEF", 4, 0.35
# seconds of silence: after each segment, after a chapter's last segment, between sentences in a clip
from .tts import PACING, pause_for, sentences  # noqa: E402  (one pacing table for decks and animations)


class VerifyError(AssertionError):
    pass


class Until(float):
    """A run_time from left(): the seconds from the call to a point in the narration, which remembers
    that point, so a play that first waits for its sync phrase can shorten it by the wait."""
    @classmethod
    def make(cls, d, end, floor, cap):
        d = max(d, floor)
        o = super().__new__(cls, min(d, cap) if cap else d)
        o.end, o.floor, o.cap = end, floor, cap
        return o

    def after(self, now):
        return Until.make(self.end - now, self.end, self.floor, self.cap)


def cell_box(cell: str, span: str = "1x1"):
    """(x0, y0, x1, y1) in scene units for a cell and span; A1 is top left."""
    w, h = config.frame_width - 2 * MARGIN, config.frame_height - 2 * MARGIN
    cw, rh = w / len(COLS), h / ROWS
    c, r = COLS.index(cell[0].upper()), int(cell[1:]) - 1
    sc, sr = (int(x) for x in span.lower().split("x"))
    if c + sc > len(COLS) or r + sr > ROWS:
        raise ValueError(f"{cell} span {span} runs off the grid")
    x0 = -config.frame_width / 2 + MARGIN + c * cw
    y1 = config.frame_height / 2 - MARGIN - r * rh
    return x0, y1 - sr * rh, x0 + sc * cw, y1


def bbox(m):
    ul, dr = m.get_corner(UP + LEFT), m.get_corner(DOWN + RIGHT)
    return ul[0], dr[1], dr[0], ul[1]


def intersects(a, b, tol=0.02):
    return a[0] < b[2] - tol and b[0] < a[2] - tol and a[1] < b[3] - tol and b[1] < a[3] - tol


class ExplainScene(VoiceoverScene):
    def setup(self):
        super().setup()
        self.report = _report.load(os.environ.get("EXPLAIN_REPORT", "."))
        self.pacing = {**PACING, **(self.report.story.get("pacing") or {})}
        self.set_speech_service(KokoroService(pacing=self.pacing,
                                              cache_dir=Path(config.media_dir) / "voiceovers" / type(self).__name__))
        self._seg = {g["id"]: g for g in self.report.segments}
        mine = [g["id"] for g in self.report.segments if g.get("scene") == type(self).__name__]
        self._last = mine[-1] if mine else None   # its pause is the chapter break
        self._placed = {}   # name -> {"m": mobject, "t": time placed, "cell": ...}
        self._released = []  # (name, placed_t, released_t, segment)
        self._current = None
        self._tol = float(self.report.story.get("sync_tolerance") or 0.5)
        self._t = None   # the current segment's voiceover tracker
        self._log = {"scene": type(self).__name__, "segments": [], "sync": [], "warnings": [], "failures": []}

    # placement ------------------------------------------------------------
    def place(self, m, cell: str, name: str | None = None, span: str = "1x1", pad: float = 0.12):
        x0, y0, x1, y1 = cell_box(cell, span)
        bw, bh = x1 - x0 - 2 * pad, y1 - y0 - 2 * pad
        if m.width > bw or m.height > bh:
            k = min(bw / max(m.width, 1e-6), bh / max(m.height, 1e-6))
            m.scale(k)
            self._log["warnings"].append(f"{name or type(m).__name__} scaled by {k:.2f} to fit {cell} {span}")
        m.move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0])
        if name:
            self._placed[name] = {"m": m, "t": self.renderer.time, "cell": f"{cell}/{span}"}
        return m

    def tag(self, text: str, font: str = "Lato", color: str = "#9AA4AE", size: int = 22):
        """A corner label (bottom right) saying what the frame is: 'schematic', 'simulated', 'data'.
        Call again to change it; returns the animation to play (or None if unchanged)."""
        from manim import FadeIn, Text, Transform
        new = Text(text, font=font, font_size=size, color=color)
        x0, y0, x1, y1 = cell_box("F4")
        new.move_to([x1 - new.width / 2 - 0.15, y0 + new.height / 2 + 0.15, 0])
        old = getattr(self, "_tag", None)
        if old is not None and old.text == text:
            return None
        if old is None:
            self._tag = new
            return FadeIn(new)
        anim = Transform(old, new)
        old.text = text
        return anim

    def track(self, m, name: str):
        """Record an object placed some other way (axes coordinates, next_to) for the verify checks."""
        self._placed[name] = {"m": m, "t": self.renderer.time, "cell": "tracked"}
        return m

    def release(self, *names):
        for n in names:
            rec = self._placed.pop(n, None)
            if rec:
                self._released.append((n, rec["t"], self.renderer.time, self._current))

    # narration ------------------------------------------------------------
    @contextmanager
    def say(self, sid: str):
        g = self._seg.get(sid)
        if g is None:
            raise KeyError(f"segment {sid} is not in storyboard.yaml")
        self._current, start = sid, self.renderer.time
        with self.voiceover(text=g["narration"], **({"pace": g["pace"]} if g.get("pace") else {})) as t:
            audio = Path(t.cache_dir) / t.data["final_audio"]
            t.spans = clip_spans(audio)
            t.sentences = sentences(g["narration"])
            t.audio, t.knots = audio, {}
            self._t, self._cues, self._played, self._motion = t, 0, {}, 0.0
            yield t
        declared = g.get("sync") or {}
        if len(t.spans) > 1 and not self._cues and not declared and g.get("role") != "distil":
            self._log["warnings"].append(f"{sid}: {len(t.spans)} sentences and no sync anchor or at() cue; "
                                         "the picture may run ahead of or behind the voice")
        for name in declared:
            if name not in self._played:
                self._fail(f"{sid}: sync '{name}' (\"{declared[name]}\") is never played; tag its play with sync='{name}'")
        shown = sorted(self._played, key=lambda n: self._played[n][1])        # by when they started
        spoken = sorted(self._played, key=lambda n: self._played[n][0])       # by when they are said
        if shown != spoken:
            self._fail(f"{sid}: sync events play in the order {', '.join(shown)} but are spoken {', '.join(spoken)}")
        self._verify(g, start)
        seg = self._log["segments"][-1]
        seg["sentences"] = [[round(start + a, 3), round(start + b, 3)] for a, b in t.spans]
        seg["speech"] = round(sum(b - a for a, b in t.spans), 2)   # seconds of voice
        seg["motion"] = round(self._motion, 2)                     # seconds something moves (not waits)
        self._t = None
        # a beat after each segment, a longer one at the end of a chapter (a paragraph break)
        pause = pause_for(g, self.pacing, chapter_end=sid == self._last)
        if pause:
            self.wait(float(pause))
        if self._log["segments"] and self._log["segments"][-1]["id"] == sid:
            self._log["segments"][-1]["settled"] = round(self.renderer.time, 3)   # end of the pause: stills

    def _knots(self, t, k: int):
        if k not in t.knots:
            a, b = t.spans[k]
            y, rate = (None, 24000)
            try:
                import soundfile as sf
                y, rate = sf.read(str(t.audio))
                y = y.mean(axis=1) if y.ndim > 1 else y
            except Exception:
                pass
            lang = "en-gb" if os.environ.get("REPORT_VOICE", "b")[:1] == "b" else "en-us"
            t.knots[k] = timing.knots(t.sentences[k], a, b, y, rate, lang, float(self.pacing.get("clause", 0.2)))
        return t.knots[k]

    def mark(self, t, k: int, word: str | None = None) -> float:
        """Scene time when sentence k (0 = first) starts, or, with `word`, when that word in it is
        reached (phoneme share between the clause pauses heard in the audio: timing.py)."""
        if not word:
            return t.start_t + t.spans[k][0]
        text = t.sentences[k] if k < len(t.sentences) else ""
        i = text.lower().find(word.lower())
        if i < 0:
            raise ValueError(f"{self._current}: {word!r} is not in sentence {k + 1}: {text!r}")
        return t.start_t + timing.onset(text, i, self._knots(t, k))

    def _row(self, kind, name, phrase, k, exact, due, start):
        late = start - due
        status = "late" if late > self._tol else "slow" if late > self._tol / 2 else "pass"
        row = {"segment": self._current, "id": name, "kind": kind, "phrase": phrase, "sentence": k + 1,
               "exact": exact, "voice_at": round(due - self._t.start_t, 2), "due": round(due, 3),
               "start": round(start, 3), "delta": round(late, 2), "status": status}
        self._log["sync"].append(row)
        msg = (f"{self._current}: {kind} '{name}' (\"{phrase}\") is spoken at {row['voice_at']:.1f}s "
               f"but its picture starts {late:.1f}s later; the move before it runs too long")
        if status == "late":
            self._fail(msg)
        elif status == "slow":
            self._log["warnings"].append(msg)
        return row

    def at(self, t, k: int, word: str | None = None):
        """Hold until sentence k (or `word` in it) is spoken: a cue the code chooses (declare the events
        that matter in the storyboard's `sync` instead). Late past the tolerance is a fault."""
        self._cues += 1
        due, now = self.mark(t, k, word), self.renderer.time
        self._row("cue", f"{k + 1}:{word or ''}", word or t.sentences[k][:30], k, not word or
                  t.sentences[k].lower().startswith(word.lower()), due, max(now, due))
        if due > now:
            self.wait(due - now)

    def play(self, *args, sync: str | None = None, **kwargs):
        """Scene.play; with `sync`, first hold until the storyboard's phrase for that event is spoken."""
        from manim import Wait
        if sync is not None:
            t = self._t
            declared = (self._seg[self._current].get("sync") or {}) if t else {}
            if sync not in declared:
                raise ValueError(f"{self._current}: sync '{sync}' is not declared in the segment's storyboard `sync`")
            if sync in self._played:
                raise ValueError(f"{self._current}: sync '{sync}' is played twice")
            phrase = declared[sync]
            k, i = timing.find(t.sentences, phrase)
            due = self.mark(t, k, t.sentences[k][i:i + len(phrase)]) if i else self.mark(t, k)
            now = self.renderer.time
            if due > now:
                self.wait(due - now)
                if isinstance(kwargs.get("run_time"), Until):     # left() measured from before the wait
                    kwargs["run_time"] = kwargs["run_time"].after(self.renderer.time)
            self._played[sync] = (due, max(now, due))
            row = self._row("anchor", sync, phrase, k, i == 0, due, max(now, due))
        t0 = self.renderer.time
        super().play(*args, **kwargs)
        if sync is not None:
            row["end"] = round(self.renderer.time, 3)
        if self._t is not None and not all(isinstance(a, Wait) for a in args):
            self._motion += self.renderer.time - t0

    def left(self, t, k: int | None = None, word: str | None = None, floor: float = 0.3,
             cap: float | None = None) -> float:
        """Seconds from now to the end of sentence k (default: the last), or to `word` in it: a run_time.
        `cap` keeps a move short (it then holds still until the next cue); leave it off for a process
        that should run the whole sentence (reads flowing, bars growing one by one)."""
        k = len(t.spans) - 1 if k is None else k
        end = self.mark(t, k, word) if word else t.start_t + t.spans[k][1]
        return Until.make(end - self.renderer.time, end, floor, cap)

    # checks ---------------------------------------------------------------
    def _fail(self, msg):
        self._log["failures"].append(msg)
        if os.environ.get("EXPLAIN_STRICT") == "1":
            raise VerifyError(msg)

    def _verify(self, g, start):
        sid, v = g["id"], g.get("verify") or {}
        if isinstance(v, list):  # allow [{inside_frame: all}, {...}]
            v = {k: x for d in v for k, x in d.items()}
        fw, fh = config.frame_width / 2, config.frame_height / 2
        if v.get("inside_frame", "all"):
            for m in self.mobjects:
                if m.width == 0 and m.height == 0:
                    continue
                x0, y0, x1, y1 = bbox(m)
                if x0 < -fw - 1e-3 or x1 > fw + 1e-3 or y0 < -fh - 1e-3 or y1 > fh + 1e-3:
                    name = next((n for n, r in self._placed.items() if r["m"] is m), type(m).__name__)
                    self._fail(f"{sid}: {name} leaves the frame")
        no = v.get("no_overlap")
        if no:
            names = list(self._placed) if no == "all" else [n for n in no if n in self._placed]
            for i, a in enumerate(names):
                for b in names[i + 1:]:
                    if intersects(bbox(self._placed[a]["m"]), bbox(self._placed[b]["m"])):
                        self._fail(f"{sid}: {a} overlaps {b}")
        order = v.get("order") or []
        times = {n: r["t"] for n, r in self._placed.items()}
        times.update({n: t0 for n, t0, _, _ in self._released})
        for a, b in zip(order, order[1:]):
            if a in times and b in times and times[a] > times[b]:
                self._fail(f"{sid}: {a} should appear before {b}")
        hold = float(v.get("hold_min_s", 0) or 0)
        for n, t0, t1, seg in self._released:
            if seg == sid and hold and t1 - t0 < hold:
                self._fail(f"{sid}: {n} shown {t1 - t0:.1f}s; at least {hold}s")
        self._log["segments"].append({"id": sid, "start": round(start, 3),
                                      "end": round(self.renderer.time, 3)})

    def tear_down(self):
        super().tear_down()
        out = self.report.p("checks")
        out.mkdir(parents=True, exist_ok=True)
        (out / f"scene-{type(self).__name__}.json").write_text(json.dumps(self._log, indent=1))
