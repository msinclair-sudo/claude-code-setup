# Tier 4: narrated animation (Manim CE 0.22 + Kokoro)

## Cheat sheet (verified on manim 0.22.0, manim-voiceover 0.4.0, 2026-10-20)

Run everything through `scripts/x run …` so `REPORT_*`, the env's PATH and `explainlib` are set.

```python
from explainlib.kokoro_service import KokoroService   # import FIRST: quiets sox/phonemizer warnings
from manim import *
from manim_voiceover import VoiceoverScene

class Scene1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService())       # voice/speed from REPORT_VOICE, REPORT_TTS_SPEED
        with self.voiceover(text="One storyboard segment's narration.") as t:
            self.play(Create(obj), run_time=t.duration)  # animation length = narration length
```

- **One `with self.voiceover(...)` block per storyboard segment.** Its `t.duration` is the clip length; animations inside take `run_time=t.duration` (or split it: `run_time=t.duration * .6`, then the rest).
- **Captions come free:** manim-voiceover writes `<Scene>.srt` beside the mp4, one cue per voiceover block, timed to the audio. Convert to VTT with `x captions`.
- **No `<bookmark mark="..."/>`:** it needs whisper (torch). Split the segment instead.
- **Render:** `x run manim -ql --media_dir build/media src/scene.py Scene1` for drafts (480p15); `-qh` for delivery (1080p60, about 2× real time on this machine: a 6 s scene took 12.6 s including TTS). `--disable_caching` when a re-render must pick up changed code.
- **Output:** `build/media/videos/<file>/<quality>/<Scene>.mp4`, plus `.srt` and a `.wav` of the whole track. Audio is AAC in the mp4; video h264.
- **Maths:** `MathTex(r"d(a,b) = \min_p |p|")` uses the system TeX Live; works.
- **Text:** `Text("label", font="Lato", font_size=32)`. Pango and browsers share Lato, Noto Sans, Open Sans (check `x run fc-list : family`).
- **Colours:** draw on the token file's `dark` set (`theme.manim_colors(t)`); video is watched full screen.
- **Voiceover cache** lives in `<media_dir>/voiceovers/`; same text, voice and speed reuse the clip.
- **Stills for review:** `ffmpeg -i video.mp4 -vf "fps=1,scale=320:-1,tile=4x2" -frames:v 1 contact.png` (one frame a second, 8 to a sheet).
- **A/V check:** `ffprobe -show_entries stream=codec_type,duration -of compact video.mp4`; the video runs longer than the audio by any trailing `self.wait()`.
