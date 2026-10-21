"""When is a word spoken? Kokoro (v1.0 ONNX) returns audio only, no timings, and word timings would need
whisper (and torch). Each sentence is synthesised alone, so its start and end are exact (tts.synth_spans).
A word inside it is placed by its share of the sentence's phonemes, between knots heard in the audio:
the sentence start, the pause at each comma, semicolon or colon (matched to the pause nearest its
estimate), and the sentence end.

Measured on the rarefaction exemplar, 104 clause onsets (the end of a comma's pause) as ground truth,
each estimated with its own pause left out: character share, median error 0.15 s, 90th percentile
0.44 s, worst 2.2 s (numerals: "251" is short to read, long to say); this module, 0.14 s, 0.26 s and
0.53 s. So a cue that must be exact goes at the start of a sentence; one inside a sentence is good to
about a quarter of a second.
"""
import re
from functools import lru_cache

import numpy as np

CLAUSE = re.compile(r"[,;:]\s+")


@lru_cache(maxsize=None)
def _tokenizer():
    try:
        from kokoro_onnx.tokenizer import Tokenizer
        from phonemizer.backend.espeak import api
        delete = api.EspeakAPI._delete

        def _delete(library, tempdir):    # its temp copy of espeak may already be gone at exit (shared /tmp)
            try:
                delete(library, tempdir)
            except FileNotFoundError:
                pass
        api.EspeakAPI._delete = staticmethod(_delete)
        return Tokenizer()
    except Exception:  # no phonemizer: fall back to characters
        return None


@lru_cache(maxsize=4096)
def phonemes(text: str, lang: str = "en-gb") -> int:
    if not text.strip():
        return 0
    tok = _tokenizer()
    if tok is None:
        return len(text.strip())
    return len(tok.phonemize(text, lang).replace(" ", ""))


def quiet_runs(y, rate: int, a: float, b: float, min_s: float = 0.08, rel: float = 0.02):
    """(start, end) seconds of each silence of at least `min_s` inside [a, b] (10 ms frames)."""
    hop = max(int(rate * 0.01), 1)
    rms = np.sqrt(np.convolve(np.asarray(y, float) ** 2, np.ones(hop) / hop, "same"))[::hop]
    q = rms < rel * (rms.max() or 1)
    out, run = [], 0
    i0, i1 = int(a * 100), min(int(b * 100), len(q))
    for i in range(i0, i1):
        if q[i]:
            run += 1
            continue
        if run >= min_s * 100:
            out.append(((i - run) / 100, i / 100))
        run = 0
    return out


def knots(sentence: str, a: float, b: float, y=None, rate: int = 24000, lang: str = "en-gb",
          clause_pause: float = 0.2):
    """[(char index, speech stops, speech resumes)]: the sentence start, each clause pause found in the
    audio, the sentence end. Without audio, only the start and end."""
    out = [(0, a, a)]
    marks = [m.end() for m in CLAUSE.finditer(sentence)]
    if y is not None and marks:
        runs = quiet_runs(y, rate, a, b)
        P = max(phonemes(sentence, lang), 1)
        speech = max((b - a) - clause_pause * len(marks), 0.1)
        used = set()
        for j, i in enumerate(marks):
            est = a + speech * phonemes(sentence[:i], lang) / P + clause_pause * (j + 1)
            near = [k for k, (_, e) in enumerate(runs) if k not in used and abs(e - est) < 0.6]
            if near:
                k = min(near, key=lambda k: abs(runs[k][1] - est))
                if runs[k][0] > out[-1][2]:
                    used.add(k)
                    out.append((i, runs[k][0], runs[k][1]))
    out.append((len(sentence), b, b))
    return out


def onset(sentence: str, i: int, kn, lang: str = "en-gb") -> float:
    """Seconds at which character i of the sentence is reached, interpolated by phonemes between knots."""
    lo = max((k for k in kn if k[0] <= i), key=lambda k: k[0])
    if lo[0] == i:
        return lo[2]
    hi = min((k for k in kn if k[0] > i), key=lambda k: k[0])
    span = max(phonemes(sentence[lo[0]:hi[0]], lang), 1)
    return lo[2] + (hi[1] - lo[2]) * phonemes(sentence[lo[0]:i], lang) / span


def find(sentences: list[str], phrase: str):
    """(sentence index, char index) of the phrase's one occurrence; ValueError if absent or repeated."""
    hits = [(k, m.start()) for k, s in enumerate(sentences)
            for m in re.finditer(re.escape(phrase.lower()), s.lower())]
    if len(hits) != 1:
        raise ValueError(f"{phrase!r} occurs {len(hits)} times in the narration; a cue phrase occurs once")
    return hits[0]
