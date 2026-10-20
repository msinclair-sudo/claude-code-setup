# Tier 4: narrated animation (Manim CE 0.22 + Kokoro)

## Rules
- **Only for a change** the viewer must understand (a process, a transformation, a walk through a structure), watched narrated and system-paced. A result that is a static shape is a tier 1 figure.
- **At most 6 minutes, in chapters:** one Manim scene per chapter, a few segments per scene.
- **Narration drives time:** each segment is one `with self.say("sN") as t:` block, animations take `run_time=t.duration` (or split it). The voice names what moves while it moves.
- **Place everything on the grid** (`self.place(obj, "B2", "name", span="2x1")`) so overlaps and frame exits are caught; `release()` what you remove so hold times are checked. Each new element holds at least 2 s.
- **One new thing at a time.** Dim (not delete) what the viewer still needs; remove what they don't.
- **Draw on the dark tokens.** A colour keeps one meaning for the whole video: if colours mark taxa, samples get labels and line styles, not colours.
- **Every frame says what it is:** `self.tag("schematic")` on drawings, `self.tag("simulated")` or `"data"` on charts; it sits bottom right and changes with the frame.
- **Show the spread, not one draw,** when the narration is about variability: repeat the draw and plot every repeat faintly.
- **After a render error, check the API below before retrying**; do not guess at Manim names.

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
