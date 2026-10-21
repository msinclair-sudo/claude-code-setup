# consolidate v2: development baseline (2026-10-21)

The skill as committed in 84ff243, run on the six development notes. Kept so v3 and later versions are compared
against the same numbers. Nothing here is held out: every note below, and every note read during design (EX-01,
NP-01, FD-01, and the headers of Aggregating Per-Genome, What Coverage-Based, Guild, Public genome collections,
H2_research), counts as development data.

## Contents

- `notes/`: the six knowledge notes as v2 left them (after the builders' fixes). Their `.index.json` files are
  not kept; `kn.py lint` rewrites them from the note.
- `verdicts/`: the faithfulness checkers' verdicts on the notes as first built (step 8, before fixes). One fresh
  checker per file; MB's 541 entries were split across two.
- `acceptance.md`: test A (the 28 MB-01 critic corrections) and test B (the 29 literature claims in the MB-01
  video's `claims.yaml`), run by one fresh agent on the 16S note after fixes.
- `mb01-fact-sheet.md`: the MB-01 fact sheet test A was scored against (the critic's corrections, written by
  hand for the video).

## Faults found by the checkers (before fixes)

| Note | Inputs | Entries | Faulted | stronger | conf | numbers | absent | critic | merged | holds |
|---|---|---|---|---|---|---|---|---|---|---|
| 16S | MB-01 + MB-02 | 541 | 170 (31%) | 4 | 23 | 1 | 30 | 0 | 1 | 111 |
| Dimensionality | H2-01 | 167 | 8 (5%) | 0 | 2 | 0 | 3 | 2 | 0 | 1 |
| Term specificity | TSL | 42 | 13 (31%) | 0 | 3 | 0 | 10 | 0 | 0 | 0 |
| Liming | CB1 | 113 | 11 (10%) | 0 | 3 | 0 | 6 | 0 | 0 | 2 |
| rRNA recovery | CB2 | 73 | 9 (12%) | 0 | 4 | 0 | 4 | 0 | 0 | 1 |
| N-fertiliser | NFERT | 48 | 6 (13%) | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| **All** | | **984** | **217 (22%)** | 4 | 37 | 1 | 56 | 2 | 1 | 116 |

Most faults were one habit: a setting in `holds`, a quoted basis or a rating taken from a sentence the entry did
not cite in `from`, so the checker (which sees only the `from` text) could not find it.

## How the faults were fixed

The builder of each note fixed its own faults and re-ran lint. **No fresh checker confirmed the fixes**: the
builders graded their own corrections. 16S: 169 fixed (107 by citing the sentence, 12 narrowed, 50 dropped), and
one disputed ("one laboratory", which the format's word list counts as `single`; the owner ruled the list decides,
so it is not a fault). The other five notes: every fault fixed.

## Acceptance (16S note, after fixes)

- Test A: 26 of 28 corrections applied, 2 partly (access caveats missing from four Sources notes; two consortium
  author orders), 0 missing.
- Test B: 25 of 29 claims covered; the 4 absent are the ones the video sourced outside the research. 7 places
  where the video says more than the note allows.
