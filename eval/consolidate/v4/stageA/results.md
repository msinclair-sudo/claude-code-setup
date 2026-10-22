# Stage A: lint scoring, gate A report (2026-10-22)

Change 1's rules were scored read-only against the v3 first-pass checker verdicts. Rules, lists and thresholds
were committed before any scoring (65c759a). The skill did not change.
- Definitions: `rules.md`.
- Per-note numbers: `scores.md`.
- Every entry's flags: `flags.tsv`.
- The false-positive sample: `fp/`.

**Gate A: no rule meets its thresholds.** Under the decision rule fixed in advance, change 1 is not built as a
lint gate: R1 is not adopted, R2 is dropped after its fallbacks, and `holds` stays with the checker under change
5's wording. This is a missed gate, so it stops here for the owner's decision. Options are at the end.

## Sanity checks (before scoring)

- **Entries and verdicts match in every note:** 1,697 entries against 1,697 verdicts (893 development, 804
  held-out), no unmatched or duplicate IDs. Every `from` reference resolves in the rebuilt inventories, and no
  entry is without cited text.
- **Known cases:**
  - R2 flags H1-05's "Eurasian steppe" (covariation.11), "Oregon coastal" (other-habitats.4, functional-unit.5)
    and "coastal" (annotation.2), and H2-04's "three search angles" (covariation-sources.1), as expected.
  - CB1 lime-resource.7's "2020" is **not** flagged by R1. The rule as written accepts a year that matches a
    source in `src`, and that source's BibTeX year is 2020. The expectation in the plan was wrong, not the code.
    The src allowance is why: it accepted 66 tokens in 34 entries.

## Results against the thresholds

| Rule | Caught | Missed | Catch rate | Flags on checker-passed entries | FP rate | Threshold (catch / FP) | Meets |
|---|---|---|---|---|---|---|---|
| R1 (numbers and names) | 18 | 46 | 28.1% | 138 of 1,491 | 9.3% | 40% / 3% | no: both |
| R2-full | 124 | 1 | 99.2% | 846 of 1,406 | 60.2% | 60% / 5% | no: FP |
| R2-content | 123 | 2 | 98.4% | 808 of 1,406 | 57.5% | 60% / 5% | no: FP |
| R2-setting | 101 | 24 | 80.8% | 444 of 1,406 | 31.6% | 60% / 5% | no: FP |

R1 is scored against 64 `absent` and `numbers` faults, and R2 against 125 `holds` faults. R2's false-positive
rate leaves out CB3, as fixed in advance. CB3 alone: R2-full flags 52 of its 85 passed entries (61%), and
R2-setting 42 (49%).

**The decision rule, applied:** R1 fails both thresholds, so it is not adopted. No R2 variant passes. The
fallbacks (R2-content, then R2-setting) also fail, so R2 is dropped.

**What the numbers say.**
- **R2 is the owner's worry, measured.** It catches nearly every `holds` fault, but it flags a third to three
  fifths of the entries the checker passed. Built as a gate, it would push builders to copy text verbatim.
- **R1 catches little.** In v3, `absent` faults are mostly glosses and consequences in ordinary words, not
  miscopied tokens. That is because v3 already makes quotes and bases sit in the cited text.

### Breakdown (information only; not used for adoption)

| Part of R1 | Catch rate | FP rate |
|---|---|---|
| numbers, years and `[n]` markers only | 12.5% (8/64) | 1.1% (16/1,491) |
| capitalised names only | 17.2% (11/64) | 4.4% (65) |
| quoted phrases only | 14.1% (9/64) | 4.8% (72) |

R2's false positives whose only unmatched words are process or access words ("critic", "review", "abstract",
"source", "single-pass"): 114 of 846 (R2-full) and 48 of 444 (R2-setting).

## The false-positive sample (information only; recorded separately; does not affect adoption)

`random.Random(20261023)` drew 30 of R1's 138 false positives and 30 of R2-full's 846. Each sample went to one
fresh judge using change 5's wording. Verdicts are in `fp/R1-judged.md` and `fp/R2-judged.md`.

| Sample | Lint error | Checker miss | Unclear |
|---|---|---|---|
| R1 (30) | 15 | 14 | 1 |
| R2-full (30) | 17 | 11 | 2 |
| of which R2-content also flags (28) | 15 | 11 | 2 |
| of which R2-setting also flags (19) | 8 | 9 | 2 |

- **R1's checker misses** are the antecedent problem the re-checkers met. The entry names what the cited text
  only refers to: "These two" becomes Westoby and Fahimipour, "Both" becomes the ZnO and alpine studies, "The
  authors" becomes Changbai. Others are a source supplied for "the one primary source" (USGS) and a denominator
  added ("of the MAGs").
- **R1's lint errors** are do-not-say quotes paraphrasing their wording, spelling variants (Verdú and Verdu,
  -ise and -ize), and an acronym spelled out (GOS).
- **R2's checker misses** are added settings the checker passed.
- **R2's lint errors** are what the owner predicted: paraphrase ("natural marine" for "one surface-ocean data
  set"), word forms, and process wording ("checked by the critic", "labelled INDIRECT", "the reviewer's
  statement").

**Rough reading, from one judge and 30 entries each:** applying the sample's lint-error shares to the
false-positive rates, the lint would flag about 4.7% of faithful entries for R1, about 34% for R2-full and about
13% for R2-setting. All are still above their thresholds, so the sample does not change the gate. It does say
two things for later.

1. **The v3 checkers missed real faults.** About half of R1's and a third of R2's flags on passed entries are
   faults under change 5's wording. Scaled up, very roughly, that is tens of `absent` faults and a few hundred
   added settings in `holds`. This fits CB3's checker passing added settings, and it means v3's 12.1% understates
   the rate under the new wording. Stage B's re-score of 100 v3 entries (change 5) is now the important baseline.
   Without it, v4 would be compared against a lenient checker.
2. **The lint finds what the checker misses**, just not cleanly enough to be a gate.

## Mechanical fixes after the first run

| Fix | Before | After |
|---|---|---|
| Tokens with sub- or superscript digits (CaCO₃, NH₄-N, R²) were cut differently in the entry and the cited text, so a string present in both failed to match. The word pattern now uses Python's `\w` letters and digits on both sides. | R1: 18 caught, 177 FP (11.9%), 8 flags on other faults | R1: 18 caught, 138 FP (9.3%), 4 flags on other faults; R2 unchanged |

Nothing else was changed after the first run.

**Known limits of the rules as written,** recorded, not tuned:
- the stemming rule leaves "studies" and "study" unmatched;
- the setting lexicon contains "in" (from "in vitro"), so R2-setting can flag "in";
- citekey-shaped words in statements ("Piton2023") count as names;
- the `src` allowance accepts a year that comes only from a key (lime-resource.7).

## Options for the owner at gate A

The thresholds say not to build change 1 as a lint gate. Three options, not decided here:
1. **No lint** (the decision rule's result). Change 5's wording does the work, and the checker stays the only
   control on `holds` and `absent`.
2. **R1's number, year and marker part as a lint error.** It is 1.1% FP but only 12.5% catch: cheap and nearly
   harmless, but small. It is below the 40% catch threshold as a sub-rule, so adopting it is an owner's
   exception, not the rule's result.
3. **The lint as a pointer for the checker, not a gate (recommended).** `kn.py packets` prints, under each entry,
   the words and tokens not found in its cited text ("not found in the cited text: Oregon, coastal"), and the
   checker decides. Nothing blocks, so builders have no reason to copy verbatim. The checker's attention goes
   where the sample shows it misses faults: about half of R1's flags and a third of R2's.

   It would be judged in stage B by the same measures as everything else, without a threshold of its own, since
   it gates nothing. This is a new proposal, outside revision 2's change 1, so it needs the owner's yes.

## Unseen notes: a set-aside for evaluating the writing stage

**Proposed:** six notes, drawn now, before stage C draws, by a seeded draw within each category (seed recorded),
and excluded from stage C's frame. This gives two rounds of three topics (development and held-out, or two
held-out rounds) in the slots the usability test uses: a critiqued run, a harness run, and an uncritiqued run.
- **Category 3 (critiqued, numbered), 2 notes:** the largest pool (25), and critiqued.
- **Category 7 (uncritiqued harness), 2 notes:** the harness slot. Category 5, the critiqued harness, is empty.
- **Category 8 (uncritiqued, no answers), 1 note:** the uncritiqued slot. The largest uncritiqued pool, with the
  free-form reviews a writer may meet.
- **Category 6 (uncritiqued, with answers), 1 note:** the uncritiqued slot, the research-workflow kind.
- **None from categories 1, 2 or 4:** too scarce, and stage C needs them.

Soil or microbiology is preferred within a category by title (metadata), as in v3. The draw is made only with the
owner's go-ahead.

| # | Category | Unseen now | Writing set-aside | Stage C | Left after both |
|---|---|---|---|---|---|
| 1 | Critiqued, labelled, with standing | 2 | 0 | 1 | 1 |
| 2 | Critiqued, labelled, without standing | 1 | 0 | 1 | 0 |
| 3 | Critiqued, numbered | 25 | 2 | 1 | 22 |
| 4 | Critiqued, author-year | 3 | 0 | 1 | 2 |
| 5 | Critiqued harness | 0 | 0 | dropped | 0 |
| 6 | Uncritiqued, with answers | 4 | 1 | 1 | 2 |
| 7 | Uncritiqued harness | 6 | 2 | 1 | 3 |
| 8 | Uncritiqued, no answers | 10 | 1 | 1 | 8 |
| | **All** | **51** | **6** | **7** | **38** |

## Research runs that would refill categories 1 and 2

- **Category 1 can be refilled.** Research-brief rule 3a labels every citation `[access; class; standing]` and
  "standing is never left out" (`researcher-protocol.md` §3a; `workflow.md`). So any standard or deep run under
  the current workflow, which has a critic, produces a category 1 note. A quick run has no critic and lands in
  categories 6 to 8.
- **Category 2 (labelled without standing) cannot be refilled by new runs**, for the same reason. Its one unseen
  note goes in stage C, and the category then closes.
- **Category 5 (critiqued harness)** needs a biblion harness run with a critique, outside research-brief.

Candidates are drawn only from notes already read: their Stage 2 callouts. Unseen notes were not opened.
Nothing below is written or run.

| Order | Follow-up | Stage 2 status and the gaps it names | Kind |
|---|---|---|---|
| 1 | **MB-01** (16S workflow) | Triggered: per-cycle amplification efficiency (qPCR kinetics not searched), community copy number from metagenomes, 16S index hopping on patterned flow cells, within-run read-count variation against load, long-read platform error | evidence, several vocabularies: deep |
| 2 | **MB-02** (16S copies per cell, rarity, soil) | Triggered: in situ growth (qSIP, genome-based growth-rate potential), ploidy of dormant and sporulated forms, taxon-specific per-cell evidence for soil | evidence: standard or deep |
| 3 | **H2-01** (dimensionality of functional profiles) | Triggered on both arms: formal rank estimation under compositional transforms (random-matrix thresholds, cross-validated NMF, robust Aitchison PCA), and habitat classes with held-out tests | evidence: deep |
| 4 | **H1-05** (functional against taxonomic turnover) | Triggered: soil chronosequence metagenomes, soil metatranscriptomes against taxonomic turnover, fungal, archaeal and protist functional turnover, aquatic comparisons | evidence: deep |
| 5 | **H1-02** (recovery artefacts in MAGs) | Triggered: freshwater lakes and hypersaline salterns, sediments (yield data only), natural soils for strain heterogeneity | evidence: standard |
| 6 | **H2-04** (sources of functional covariation) | Triggered: phylogenetic profiling and pangenome co-occurrence, evolutionary quantitative genetics (G-matrix, subspace comparison) | evidence: deep |
| 7 | NP-01 (narrative pacing) | Triggered: practitioner guidance (radio, documentary, animation, screenwriting), comics and visual narrative research | outside the PhD topic; refills category 1 all the same |
| 8 | EX-01, FD-01 (explanation, visual output) | Triggered: expert audiences, neural TTS evaluation, practitioner production accounts; non-slide visual instruction sets | outside the PhD topic |

H1-06's stage 2 was not triggered (no ROUTING condition). The uncritiqued development notes (CB1, CB2, CB3,
NFERT, H1-RES, TAXRES) have no stage-2 check.

**Caution:** a follow-up on a development topic is a new, unread note and so qualifies as held-out. But its
subject overlaps a note whose knowledge note the builders' process was tuned on. For stage C or the writing
set-aside, a fresh topic is the cleaner test. For refilling category 1 at all, the follow-ups are the only
candidates on record.

## Stop

Gate A is reached and missed. Nothing in stage B is built until the owner decides how change 1 is built: no lint,
R1's number part only, or the lint as a pointer for the checker. The owner also decides the writing set-aside
draw.
