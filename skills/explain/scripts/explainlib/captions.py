"""Captions and transcript: VTT from timed segments or from manim-voiceover's SRT."""
import re
from pathlib import Path


def ts(sec: float) -> str:
    h, rem = divmod(max(sec, 0.0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def vtt(cues) -> str:
    """cues: [(start, end, text)]"""
    return "WEBVTT\n\n" + "\n".join(f"{ts(a)} --> {ts(b)}\n{t}\n" for a, b, t in cues)


def srt_cues(path) -> list:
    out = []
    for block in re.split(r"\n\s*\n", Path(path).read_text().strip()):
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        a, b = [x.strip().replace(",", ".") for x in lines[1].split("-->")]
        sec = lambda x: sum(float(p) * m for p, m in zip(x.split(":"), (3600, 60, 1)))
        out.append((sec(a), sec(b), " ".join(lines[2:])))
    return out


def shift(cues, by: float) -> list:
    return [(a + by, b + by, t) for a, b, t in cues]


def transcript(r, title: str | None = None) -> str:
    lines = [f"# {title or r.story.get('title', 'Transcript')}", ""]
    for g in r.segments:
        if g.get("narration"):
            lines += [g["narration"].strip(), ""]
    return "\n".join(lines)
