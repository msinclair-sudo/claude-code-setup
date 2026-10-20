# Narration (Kokoro, local)

## Cheat sheet (measured 2026-10-20, CPU, kokoro-onnx 0.6.1, model v1.0)

- **Voice:** the owner chose **bm_george** (British male, about 155 wpm at speed 1.0). Voice, speed and provider live in `~/.config/explain/config.env`; edit them there.
- **Speed:** about 0.26× real time on CPU (a 10 s clip takes about 2.7 s). No GPU needed.
- **Rate at speed 1.0** on a 28-word method sentence:

  | voice | wpm | voice | wpm |
  |---|---|---|---|
  | af_heart | 165 | bf_emma | 177 |
  | af_bella | 161 | bf_isabella | 178 |
  | am_michael | 153 | bm_george | 155 |
  | | | bm_lewis | 160 |

  The British female voices run fast; `REPORT_TTS_SPEED=0.9` brings them near 160. The 150–170 wpm target is the YouTube norm, a heuristic with no comprehension evidence behind it.
- **Language follows the voice prefix:** `b*` voices speak `en-gb`, `a*` voices `en-us` (`tts.lang_for`). There is no Australian voice.
- **Voices available:** 28 English (af_alloy … af_sky, am_adam … am_santa, bf_alice, bf_emma, bf_isabella, bf_lily, bm_daniel, bm_fable, bm_george, bm_lewis).
- **Clips:** `tts.clip(text, dir, name)` → `.m4a` normalised to −16 LUFS, cached on (text, voice, speed, model).
- **Pronunciation:** espeak phonemises numbers and symbols; check anything technical by ear and rewrite it in the narration as it should be spoken. The lexicon below grows from those checks.

## Pacing
Silence is part of the narration: without it, sentences run together and chapters blur (owner review, 2026-10-20). Storyboard `pacing:` sets four pauses, in seconds:
- `sentence` (0.5) and `clause` (0.15): inside a clip, passed to Kokoro (its own 0.25 and 0.1 run sentences together);
- `segment` (0.6): after each segment, before the next visual;
- `chapter` (1.6): after a chapter's last segment in an animation, before a new slide in a deck. Use it where a written text would start a new paragraph.

A segment can set `pause_after` (for example after a number the viewer should take in). Pauses are part of the clip cache key, so changing them resynthesises.

## Lexicon (write the narration in the right-hand form)
| on screen | narrate as |
|---|---|
| (filled in from the owner's listening test) | |
