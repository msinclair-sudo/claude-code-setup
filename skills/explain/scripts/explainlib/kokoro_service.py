"""manim-voiceover SpeechService backed by local Kokoro (kokoro-onnx).

    from explainlib.kokoro_service import KokoroService
    self.set_speech_service(KokoroService())          # voice/speed from REPORT_* env
    with self.voiceover(text="...") as t:
        self.play(Create(curve), run_time=t.duration)

Written against manim-voiceover 0.4.0 (services/gtts.py is the pattern).
No <bookmark> support: that needs whisper transcription. Instead each clip is spoken one sentence at a
time, and the sentences' (start, end) seconds go to `<clip>.spans.json` beside it (read by `spans()`).
"""
import json
import os
from pathlib import Path

from . import tts  # first: quiets the sox/phonemizer loggers before manim-voiceover imports sox

import soundfile as sf
from manim_voiceover._typing import VoiceoverData
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import PathLike, SpeechService, initialize_speech_service, path_to_string


class KokoroService(SpeechService):
    def __init__(self, voice: str | None = None, speed: float | None = None, pacing: dict | None = None,
                 **kwargs: object) -> None:
        initialize_speech_service(self, kwargs)
        self.voice = voice or os.environ.get("REPORT_VOICE", "bf_emma")
        self.speed = float(speed or os.environ.get("REPORT_TTS_SPEED", "1.0"))
        self.pacing = pacing or {}

    def generate_from_text(self, text: str, cache_dir: PathLike | None = None,
                           path: PathLike | None = None, **kwargs: object) -> VoiceoverData:
        if cache_dir is None:
            cache_dir = self.cache_dir
        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "kokoro",
                      "voice": self.voice, "speed": self.speed, "pauses": list(tts.pauses(self.pacing)), "join": tts.JOIN,
                      "model": Path(os.environ["REPORT_TTS_MODEL"]).name}
        cached = self.get_cached_result(input_data, cache_dir)
        if cached is not None:
            return cached
        audio_path = path_to_string(path) if path else self.get_audio_basename(input_data) + ".wav"
        samples, rate, spans = tts.synth_spans(input_text, self.voice, self.speed, self.pacing)
        sf.write(str(Path(cache_dir) / audio_path), samples, rate)
        span_file(Path(cache_dir) / audio_path).write_text(json.dumps(spans))
        return {"input_text": text, "input_data": input_data, "original_audio": audio_path}


def span_file(audio: Path) -> Path:
    return audio.with_suffix(".spans.json")


def spans(audio: Path) -> list[tuple[float, float]]:
    """Each sentence's (start, end) in seconds within a clip; one span for the whole clip if unknown."""
    f = span_file(Path(audio))
    if f.exists():
        return [tuple(x) for x in json.loads(f.read_text())]
    return [(0.0, sf.info(str(audio)).duration)]
