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
Silence is part of the narration: without it, sentences run together and chapters blur. The owner's second review (2026-10-20) still found 0.6 s between segments "way too fast" and the move into a new chapter "very abrupt". The evidence (design-rules, NP rows): 2 s breaks between narrated segments helped in one research group's studies; breaks at event boundaries helped recall; silent pause length *inside* narration has never been tested, so inside a clip keep the voice's natural rhythm. Storyboard `pacing:` sets the pauses, in seconds:
- `sentence` (0.7) and `clause` (0.2): inside a clip. Kokoro (v1.0 model) reports no timings, so its own sentence pause was never applied (measured gaps 0.3-0.5 s); `tts` speaks one sentence at a time and inserts the pause itself, recording each sentence's start and end for the scene's sync anchors and `at()` cues (a word inside a sentence is placed by phonemes between the clause pauses heard in the audio, to about 0.25 s: `timing.py`);
- `segment` (2.0): after each segment, while the picture holds;
- `distil` (3.0): after a `distil` segment, the idea just restated stays on screen with nothing new;
- `chapter` (3.5): after a chapter's last segment, with a visible boundary (clear the stage, the next chapter's title). Use it where a written text would start a new section.

A segment can set `pause_after` (for example after a number the viewer should take in), and `pace` sets one sentence's following pause or speed (storyboard.md). Pauses are part of the clip cache key, so changing them resynthesises. The pauses lengthen the video: a chaptered video for an enrolled audience may run to about 10 minutes (design-rules: MOOC viewers dropped off near 6 min; enrolled students watched 12-13 min sessions).

## Writing for the ear
- **Short sentences**, one idea each; about 20 words at most. Long, complex narration did worse than written text.
- **Talk to the viewer**: "you", "we", "here". Conversational style helped (d ≈ 0.3-0.5).
- **One new term per segment**, said, shown, and used again in the next segment.
- **Come back to the subject** in every segment: name the soil, the sample, the gene, not "it" or "the data".
- **On screen, names, not sentences**: a label on the thing it names (at most 4 words), a number, a term; never the narration, reworded or not.

## Lexicon (write the narration in the right-hand form)
| on screen | narrate as |
|---|---|
| (filled in from the owner's listening test) | |
