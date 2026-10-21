"""Narration clips: Kokoro -> wav -> loudness-normalised AAC (.m4a), cached.

    clip(text, out_dir) -> (path, seconds)

Cache key: sha256 of (text, voice, speed, model file name). A clip whose key
matches is reused, so re-rendering only resynthesises changed segments.
"""
import hashlib
import json
import logging
import os
import re
import subprocess
from pathlib import Path

# benign noise: sox (pulled in by manim-voiceover) warns when the sox binary is
# absent; phonemizer warns on espeak word-count mismatches. `disabled` survives
# the setLevel these libraries do on import.
for _n in ("sox", "phonemizer"):
    logging.getLogger(_n).disabled = True

import soundfile as sf

LUFS = -16
_K = {}


def kokoro():
    """One loaded model per process."""
    if "k" not in _K:
        from kokoro_onnx import Kokoro
        _K["k"] = Kokoro(os.environ["REPORT_TTS_MODEL"], os.environ["REPORT_TTS_VOICES"])
    return _K["k"]


def lang_for(voice: str) -> str:
    return "en-gb" if voice[:1] == "b" else "en-us"


# Pauses inside a clip. Kokoro's own defaults (0.25 s after a sentence, 0.1 s after a clause) run
# sentences together; a listener needs a beat to take in what was just said. kokoro-onnx places its
# sentence pause only where the model reports timings (v1.0 reports none: measured gaps were 0.3-0.5 s),
# so synth() speaks one sentence at a time and inserts the sentence pause itself. Per report:
# storyboard `pacing: {sentence: 0.7, clause: 0.2}`; machine default: REPORT_TTS_SENTENCE_PAUSE.
SENTENCE_PAUSE = float(os.environ.get("REPORT_TTS_SENTENCE_PAUSE", "0.7"))
CLAUSE_PAUSE = float(os.environ.get("REPORT_TTS_CLAUSE_PAUSE", "0.2"))
# Seconds of silence (references/narration.md, Pacing): inside a clip (sentence, clause), after a segment,
# after a distil line, and at the end of a chapter (a scene in an animation, a slide in a deck).
PACING = {"sentence": SENTENCE_PAUSE, "clause": CLAUSE_PAUSE, "segment": 2.0, "distil": 3.0, "chapter": 3.5}
PACING_KEYS = tuple(PACING)


def pause_for(g: dict, pacing: dict, chapter_end: bool) -> float:
    """The silence after segment g: its own pause_after, else the chapter, distil or segment pause."""
    if g.get("pause_after") is not None:
        return float(g["pause_after"])
    if chapter_end:
        return float(pacing["chapter"])
    return float(pacing["distil"] if g.get("role") == "distil" else pacing["segment"])


def settings(voice=None, speed=None):
    return (voice or os.environ.get("REPORT_VOICE", "bf_emma"),
            float(speed or os.environ.get("REPORT_TTS_SPEED", "1.0")))


def pauses(pacing: dict | None = None):
    p = pacing or {}
    return float(p.get("sentence", SENTENCE_PAUSE)), float(p.get("clause", CLAUSE_PAUSE))


JOIN = "sentences-v1"   # how a clip is assembled; part of every cache key
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def sentences(text: str) -> list[str]:
    return [s for s in _SENTENCE_END.split(" ".join(text.split())) if s]


def sentence_pace(pace) -> dict:
    """A segment's optional per-sentence controls, `pace: {2: {pause: 1.2, speed: 0.9}}`, normalised to
    {"2": {"pause": 1.2, "speed": 0.9}}. Sentences are numbered from 1. `pause`: seconds of silence after
    that sentence (default: the sentence pause); `speed`: a multiplier on the voice's speed (default 1)."""
    return {str(k): {f: float(v) for f, v in sorted((d or {}).items())} for k, d in sorted((pace or {}).items(), key=lambda x: int(x[0]))}


def key(text, voice, speed, pacing=None, pace=None) -> str:
    model = Path(os.environ["REPORT_TTS_MODEL"]).name
    parts = [text, voice, speed, model, pauses(pacing), JOIN]
    if pace:                       # only when set, so clips without it keep their cache
        parts.append(sentence_pace(pace))
    return hashlib.sha256(json.dumps(parts).encode()).hexdigest()[:16]


def synth_spans(text: str, voice=None, speed=None, pacing=None, pace=None):
    """(samples, rate, spans): one sentence at a time, joined by the sentence pause; spans are each
    sentence's (start, end) in seconds, so a scene can move the picture when the voice names it.
    `pace` sets a sentence's own pause after it and speed (sentence_pace)."""
    import numpy as np
    voice, speed = settings(voice, speed)
    sp, cp = pauses(pacing)
    pace = sentence_pace(pace)
    parts, spans, n, rate = [], [], 0, 24000
    for i, s in enumerate(sentences(text)):
        own = pace.get(str(i + 1), {})
        a, rate = kokoro().create(s, voice=voice, speed=speed * own.get("speed", 1.0), lang=lang_for(voice),
                                  sentence_pause=sp, clause_pause=cp)
        if i:
            gap = np.zeros(int(round(pace.get(str(i), {}).get("pause", sp) * rate)), dtype=a.dtype)
            parts.append(gap); n += len(gap)
        spans.append((round(n / rate, 3), round((n + len(a)) / rate, 3)))
        parts.append(a); n += len(a)
    return np.concatenate(parts), rate, spans


def synth(text: str, voice=None, speed=None, pacing=None, pace=None):
    samples, rate, _ = synth_spans(text, voice, speed, pacing, pace)
    return samples, rate


def clip(text: str, out_dir, name: str | None = None, voice=None, speed=None, pacing=None, pace=None):
    voice, speed = settings(voice, speed)
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    k = key(text, voice, speed, pacing, pace)
    m4a = out_dir / f"{name or k}.m4a"
    meta = m4a.with_suffix(".json")
    if m4a.exists() and meta.exists() and json.loads(meta.read_text()).get("key") == k:
        return m4a, json.loads(meta.read_text())["seconds"]
    samples, rate = synth(text, voice, speed, pacing, pace)
    wav = m4a.with_suffix(".wav")
    sf.write(wav, samples, rate)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav),
                    "-af", f"loudnorm=I={LUFS}:TP=-1.5:LRA=11", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "96k", str(m4a)], check=True)
    wav.unlink()
    seconds = len(samples) / rate
    meta.write_text(json.dumps({"key": k, "text": text, "voice": voice, "speed": speed, "seconds": seconds}))
    return m4a, seconds
