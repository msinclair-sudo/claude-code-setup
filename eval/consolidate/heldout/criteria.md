# Held-out evaluation of consolidate v3: categories and selection (written before the draw)

Written 2026-10-21, before any note was drawn. The evaluation runs once, on v3 as committed (66d17ef), and its
results are reported without changing the skill.

## The frame

Every note in the vault's four result folders (`Apps/Research/Results`, `PhD/Proposal/Research/Results`,
`PhD/biblion/research/results`, `Topics/Biology/Research/Results`): 75 notes. `frame.tsv` lists each with the
features `kn.py detect` reports and its word count; it was made by a script that prints metadata only, so no
note's content was read to build it.

**Excluded: every note already read** (15):
- the seven development inputs: MB-01, MB-02, H2-01, TSL, CB1-LIMING, CB2-RRNA, NFERT;
- read in full during design: EX-01, NP-01, FD-01;
- read in part (headers or opening sections): Aggregating Per-Genome (BRIEF-07), What Coverage-Based (BRIEF-09),
  Guild in microbial ecology (CM-3), Public genome collections (INTRO-07), H2_research.

The style survey during design ran automated counts over all notes; that is not counted as reading.

**Research sets.** A note whose title marks it as one part of a set (`Slice1_part1`, `Slice1_part2`) is drawn as
one unit with its other parts; the knowledge note is built from the whole set.

## What matters, and why

The categories follow the paths consolidation takes, since those are what can fail differently:

| Feature | Why it matters | Source |
|---|---|---|
| Critique present or absent | the critic-wins rule, do-not-say from the critic, the "never checked by a second reader" gap | detect: `critique` |
| Labelled citations, with or without standing words | exact omission check over labelled sentences; standing and class read from markers | detect: `citations`, `standing labels` |
| Citation style (numbered, author-year, bracket keys) | how sources are matched to references and keys | detect: `citations` |
| Answers section present or absent | the fallback omission check runs over answers; without answers and critique it does not run at all | detect: `answers section` |
| Run type: research-brief workflow (deep, standard, quick), the biblion deep-research harness, or earlier free-form reviews | different layouts, verification records and question statements | folder (`PhD/biblion` is the harness), size hints in Provenance |
| Topic area | soil and microbial ecology, modelling and statistics, software and tooling, metadata standards, agricultural emissions | title |
| Size | from about 900 to 22,000 words | word count |

Topic and size are recorded for each drawn note but are not strata: crossing them with the paths would leave
most cells empty.

## Categories

Assigned by script from the frame's detected features, in this order (first match wins):

| # | Category | Rule |
|---|---|---|
| 1 | Critiqued, labelled citations with standing | critique yes; citations labelled; standing labels yes |
| 2 | Critiqued, labelled citations without standing | critique yes; citations labelled; standing labels no |
| 3 | Critiqued, numbered citations (research workflow) | critique yes; numbered; not the harness |
| 4 | Critiqued, author-year citations (research workflow) | critique yes; author-year (narrative, parenthetical or compact); not the harness |
| 5 | Critiqued harness note | critique yes; `PhD/biblion` |
| 6 | Uncritiqued, with an answers section (research workflow or other) | critique no; answers yes; not the harness |
| 7 | Uncritiqued harness note | critique no; `PhD/biblion` |
| 8 | Uncritiqued, no answers section (free-form reviews; omission check cannot run) | critique no; answers no; not the harness |

**Not available from existing notes:** citations in the research-brief rule 3a form (`[FT; meas; repl]`), the
standard-label path. MB-01 was the only one, and it is development data. This category waits for MB-01's
stage-2 follow-up, run under the current workflow, as agreed; its brief is not drafted yet.

## The draw

One note per category, drawn at random: `random.Random(20261022).choice` over the category's members sorted by
path, categories in the order above, one generator for the whole draw. A category with one member yields it.
The seed is fixed here, before the draw. Script: `draw.py`; its output, with every category's members, is
`draw.md`.

## What is run, once

For each drawn note, the skill as written: a fresh builder does steps 1 to 7; a fresh checker does the first
faithfulness pass (step 8); the builder fixes; a fresh checker re-checks the fixed entries until it finds
nothing. Reported per note and overall: the first-pass fault rate and kinds, omission results, lint, the
re-check rounds, and every place a builder says the skill fell short. No change to the skill or to the
knowledge notes after the run; findings go to the v4 list.
