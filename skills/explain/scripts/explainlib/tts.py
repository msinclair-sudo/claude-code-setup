"""Narration clips: Kokoro -> wav -> loudness-normalised AAC (.m4a), cached.

    clip(text, out_dir) -> (path, seconds)

Cache key: sha256 of (text, voice, speed, model file name). A clip whose key
matches is reused, so re-rendering only resynthesises changed segments.
"""
import hashlib
import json
import logging
import os
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
# sentences together; a listener needs a beat to take in what was just said. Per report:
# storyboard `pacing: {sentence: 0.5, clause: 0.15}`; machine default: REPORT_TTS_SENTENCE_PAUSE.
SENTENCE_PAUSE = float(os.environ.get("REPORT_TTS_SENTENCE_PAUSE", "0.5"))
CLAUSE_PAUSE = float(os.environ.get("REPORT_TTS_CLAUSE_PAUSE", "0.15"))


def settings(voice=None, speed=None):
    return (voice or os.environ.get("REPORT_VOICE", "bf_emma"),
            float(speed or os.environ.get("REPORT_TTS_SPEED", "1.0")))


def pauses(pacing: dict | None = None):
    p = pacing or {}
    return float(p.get("sentence", SENTENCE_PAUSE)), float(p.get("clause", CLAUSE_PAUSE))


def key(text, voice, speed, pacing=None) -> str:
    model = Path(os.environ["REPORT_TTS_MODEL"]).name
    return hashlib.sha256(json.dumps([text, voice, speed, model, pauses(pacing)]).encode()).hexdigest()[:16]


def synth(text: str, voice=None, speed=None, pacing=None):
    voice, speed = settings(voice, speed)
    sp, cp = pauses(pacing)
    return kokoro().create(text, voice=voice, speed=speed, lang=lang_for(voice), sentence_pause=sp, clause_pause=cp)


def clip(text: str, out_dir, name: str | None = None, voice=None, speed=None, pacing=None):
    voice, speed = settings(voice, speed)
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    k = key(text, voice, speed, pacing)
    m4a = out_dir / f"{name or k}.m4a"
    meta = m4a.with_suffix(".json")
    if m4a.exists() and meta.exists() and json.loads(meta.read_text()).get("key") == k:
        return m4a, json.loads(meta.read_text())["seconds"]
    samples, rate = synth(text, voice, speed, pacing)
    wav = m4a.with_suffix(".wav")
    sf.write(wav, samples, rate)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav),
                    "-af", f"loudnorm=I={LUFS}:TP=-1.5:LRA=11", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "96k", str(m4a)], check=True)
    wav.unlink()
    seconds = len(samples) / rate
    meta.write_text(json.dumps({"key": k, "text": text, "voice": voice, "speed": speed, "seconds": seconds}))
    return m4a, seconds
