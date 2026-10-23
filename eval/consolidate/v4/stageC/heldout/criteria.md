# Stage C: held-out evaluation of consolidate v4 and the usability re-test (written before the frame and draw)

Written on 2026-10-24, after gate B and before the frame is rebuilt or any note is drawn. This round runs once, on
v4 frozen as built: skill content as at b59851f, checker as at 7b5a0b3. Its results are reported without changing
the skill or the knowledge notes. The owner's rulings are in plan.md, revision 7.

## The frame

The frame is every note in the vault's four result folders (`Apps/Research/Results`,
`PhD/Proposal/Research/Results`, `PhD/biblion/research/results`, `Topics/Biology/Research/Results`).
- `frame.tsv` lists each note with the features that `kn.py detect` reports (v4, frozen) and its word count.
- `tools/frame.py` makes it and prints metadata only, so no note's content is read to build it.
- The vault held 75 result notes on 2026-10-24, the same count as the v3 frame.

**Excluded, by script, from existing records:**
- **Development or read:** every note excluded in the v3 frame (`../../../heldout/frame.tsv`). These are:
  - the seven development inputs;
  - EX-01, NP-01 and FD-01;
  - the five notes read in part: BRIEF-07, BRIEF-09, CM-3, INTRO-07 and H2_research.
- **The eight v3 held-out notes** (`../../../heldout/draw.md`, marked DRAWN). All 14 notes of stage B are among
  these and the development inputs.
- **The six writing set-aside units** (`../../../writing-setaside/setaside.md`), which no consolidation evaluation
  may use.

A note whose title marks it as one part of a set is one unit with its other parts. It is drawn whole, and the
knowledge note is built from the whole set.

## Categories

These are v3's categories (`../../../heldout/criteria.md`), assigned by the same rule from the frame's detected
features, first match wins:
1. Critiqued, labelled citations with standing.
2. Critiqued, labelled citations without standing.
3. Critiqued, numbered citations (research workflow).
4. Critiqued, author-year citations (research workflow).
5. Critiqued harness note. **Dropped:** it has no unseen member.
6. Uncritiqued, with an answers section.
7. Uncritiqued harness note.
8. Uncritiqued, no answers section.

This gives seven notes, one per category. The features come from the frozen v4 detect, so a note may fall in a
different category from v3's frame; the frame records what v4 detects. A category with no unseen member is reported
and skipped.

## The draw

- **Seed 20261040.** `random.Random(20261040).choice` over each category's eligible units, sorted by path, with
  categories in ascending order and one generator for the whole draw.
- `tools/draw.py` writes `draw.md`, which lists every category's members and marks the drawn one.

## What is run, once (the frozen procedure, as in stage B, B4 to B7)

For each drawn note:
1. A fresh builder does procedure steps 1 to 7, with the B4 prompt ("add the address, never delete the detail").
2. The first-pass faithfulness check uses 60-entry packets from `kn.py packets --hints`. **Two fresh checkers per
   packet, and a fault from either counts.**
3. The builder fixes, given verdict lines only.
4. One fresh re-checker per round re-checks the fixed entries until nothing is still faulted.

The knowledge note is a new vault note in the Knowledge folder beside its input's Results folder.

**Reported per note and overall:**
- first-pass fault rate (Wilson 95%) and kinds;
- `holds` plus `absent`, `stronger` plus `numbers`, and `conf`, per 100 entries;
- re-check rounds;
- omission and lint results;
- **near-copying and settings kept:** the share of claims that near-copy a cited sentence, and the share whose
  `holds` gives a real setting (`../../stageB/tools/notestats.py` definitions, v4 only);
- do-not-say entries about the review's own process, counted for information;
- every place a builder says the skill fell short.

**References:**
- stage B's v4 rates (same procedure);
- the v3 held-out rate (10%, one checker per entry, so not the same procedure).

## The usability re-test

**Topics.** Three distinct notes from the seven drawn, one per slot, in slot order:
1. **Critiqued:** categories 1 to 4.
2. **Harness:** category 7. If no note is drawn there, a drawn note whose size hint is standard.
3. **Uncritiqued:** categories 6 or 8.

Within a slot, the choice is among the drawn notes whose file name matches
`soil|microb|bacteri|archae|fung|16s|metagenom|genom|gene|nitrogen|denitrif|taxonom|communit` (case-insensitive,
the set-aside rule), if any match; otherwise among all the slot's drawn notes. **Seed 20261041:**
`random.Random(20261041).choice` per slot, members sorted by path. Topics are numbered T1 to T3 in slot order.

**Pieces.** For each topic, four fresh writers, each with one folder holding only its input:
- **raw 1 and raw 2:** the result note or set;
- **view 1 and view 2:** `kn.py view` of the frozen-v4 knowledge note.

All four get v3's prompt word for word (`../../../usability/protocol.md`). The topic line is written neutrally from
the note's own research questions and recorded in `../usability/protocol.md` before any writer runs. That makes 12
pieces.

**Pairs and letters.**
- Pair n of a topic is raw n with view n.
- Within each pair the two pieces are A and B, by **seed 20261042**: one `random.Random(20261042).random() < 0.5`
  draw per pair, in the order T1 pair 1, T1 pair 2, T2 pair 1 and so on. Under 0.5, raw is A.
- Pieces are named `T<k>-<n><L>`, for example `T1-2B`. Writer notes, fact-checks and blind sheets carry the same
  name.
- The key is `../usability/ab-key.sealed.md`. It is written once by script and not opened until the owner has
  graded all 12 pieces.

**Fact-checks.** One fresh agent per piece checks it against the full knowledge note, the audit version, and
nothing else. It is not told which input the piece came from. Each statement is one of:
- supported;
- overstated (firmer, wider or more general than the entry);
- number wrong;
- unsupported (in no entry);
- do-not-say violation;
- **absence stated as fact** (an untested or unknown point given without whether it was searched for);
- **access overreach** (a finding the knowledge note marks as read only in abstract or second-hand, interpreted
  beyond what its authors state). This is information for the marking scheme's A3.

**Blind readers.** One fresh agent per pair, six in all. Each gets:
- the pair's two pieces;
- the topic's research questions, as the scope;
- Part A of the marking scheme (`../usability/marking-scheme.md`) with its anchors.

It follows the scheme's rules:
- grade each piece on its own first;
- choose the lower score when between two anchors;
- quote every error;
- judge accuracy with its own knowledge, and open no other file.

It fills a per-piece sheet (Part A only) for each piece, then the per-pair sheet: preferred, confidence and why. It
is not told how the pieces were made.

**The owner.**
- The owner grades all 12 pieces with the full scheme, on blank sheets in the vault's `temp/stage-C/`.
- The key, the fact-checks and the blind sheets stay in the repo until grading is done. Results are reported by
  letter until then.
- After grading: scores by condition, consistency across topics and pairs, and the owner's scores against the blind
  readers', criterion by criterion.
