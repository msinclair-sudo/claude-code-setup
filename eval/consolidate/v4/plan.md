# consolidate v4: improvement plan (plan only, nothing built)

Written 2026-10-22 from the v3 measurements, for the owner's review before any build.

**The owner's read of v3:** the view pieces read better in all three topics, winning on calibration (scope, how
far a claim holds, what was not researched). The raw pieces won on attribution, a loss caused by stripping
source keys from the view ("author and year are content, not provenance"). All six pieces state absences
ambiguously. Where a view piece got a fact wrong, that is a consolidation problem to fix.

**What the measurements say, in one paragraph.** The faults are not spread out: `holds` and `absent` are 77 of
84 held-out faults and 111 of 122 development faults, and 131 of the 133 `holds` faults on record (first pass
and re-checks) *add* words the cited text does not contain. That is mechanically checkable. Consolidation is not
losing findings: in the raw-only diagnostic, nothing a raw writer used was missing from the knowledge note (D = 0
in all three topics). The view is losing them instead: every fact lost to the view writers sat in a field the
view drops (`holds`, `class`, `src`), and in TSL 7 of the view piece's 14 faults trace to the same fields, 4 of
them absences stated as fact. Separately, the omission check passed falsely on 4 of the 8 held-out notes.

Sources: `../heldout/results.md`, `../v3/README.md`, `../usability/results.md`, `diagnostics/`.

## Changes

Priorities: **1** large expected effect on faults or writer usefulness; **2** correctness of the checks and the
measurements; **3** small or local.

### 1. Provenance by lint, not by the checker (priority 1)

**Change.** Make the provenance of what an entry adds checkable by `kn.py lint`:
- **`holds` is made of the cited text.** Either one or more quoted spans, each found in the entry's `from` items
  (`holds: "simulated corpora" · "LDA"`), or `derived: <words>` where every content word is found in the `from`
  items (stopwords and connectives excepted). Lint errors on any span or content word not found.
- **Statement tokens.** Every number, year, `[n]` reference marker, capitalised name and quoted phrase in a
  statement (and in a do-not-say `why`) must occur in the `from` items. A name or year is also accepted when it
  matches the author and year of a source in the entry's `src` (the reference list maps `[28]` to a source, so
  naming the source is not an addition). Lint errors on the rest.
- **The fix is always to cite the sentence**, the antecedent of "It" or what "[48]" is, or to cut the words.
  Lint names the token and the entry.

**Motivation.** 131 of 133 `holds` faults are additions ("Eurasian steppe", "coastal", "16S lineages mapped to
genomes"). About 37 of the 63 first-pass `absent` faults quote a name, number, year or reference marker (a rough
count by pattern). The
re-checkers found that many first-pass `absent` faults were one sentence short of their support.

**How we'll know.** Before rebuilding, run the new lint in report-only mode over the 14 v3 notes as built
(`as-built/`) and score it against the checker's v3 verdicts. Target: it flags at least 90% of the recorded
`holds` faults and at least half of the `absent` faults, and flags no more than 5% of entries the checker passed.
After the rebuild: first-pass `holds` faults near zero, `absent` faults halved.

**Baselines.** No addresses change. v3 notes fail the new lint until migrated (`holds` becomes spans), so they
stay valid as v3 baselines but are not v4 notes. The report-only run is the bridge between the two.

### 2. Writer's view: attribution, setting, class, and the missed verdicts (priority 1)

**Change.** Each claim in the view shows:
- its statement;
- **who found it**, as author and year from the Sources block for each `src` key, plus "the reviewer's
  synthesis" for `src: none`;
- **the setting it holds for**, from `holds`;
- **its class in words** (measured, modelled, derived, the reviewer's reading, a search result), beside the
  standing.

The view ends with a reference list of the sources it cites, from the BibTeX block. Answers also come from
headings the view now misses: "Reformulated verdict" (H1-06), "Provisional verdicts" (TAXRES) and "Assessment"
sections (H1-RES). This goes through the same detection as change 4, so the view and the omission check agree.
Process wording is phrased for a writer: "not checked by a second reader" rather than "no critic checked it",
and no "the review". Where an answer refers to the brief's options ("option (a)"), the view quotes the option.

**Motivation.** Raw-only diagnostic: all 3 findings lost by the view (and 3 more attributions in TSL) sat in
`holds`, `class` or `src`. NFERT's view piece called a derived figure "the firmest" and made a one-system result
general. TSL view piece: 3 faults from dropped setting, 5 from raised standing (most because `class` was
missing). Blind readers in all three topics preferred raw for attribution. The view writers asked for "who found
it" and "which system" in their notes.

**How we'll know.** In the usability re-test (below): view pieces carry attributions and a reference list; facts
lost by the view (class B) fall to zero; setting and standing faults in view pieces fall. Blind readers stop
naming attribution as the reason to prefer raw. Before that, a cheap isolated test: generate the v4 view from
the three v3 knowledge notes, re-run one view writer per topic, and fact-check. That separates the view's effect
from the rebuild's.

**Baselines.** Nothing changes in the knowledge note; the view is generated, so it runs on v3 notes as they are.

### 3. Search status on every absence and gap (priority 1)

**Change.** New field `search:` on every claim with `class: search` and on every gap:
- `searched, not found`;
- `not searched`;
- `not stated`.

Each value has a basis, as `conf` does: `(note: "…")` for the note's "not found", "no study found" and
"unsearched" results and its named routes; `(critic: C-nnn)` for the critic's coverage gaps; `(run: …)` for the
run record's findings. A second field, `contrary:`, on claims and answers that state a conclusion:
- `searched` (a `bounding_or_contrary` finding in the run record, or the note naming contrary evidence it looked
  for);
- `one-sided (critic: C-nnn)` (the critic's one-sided-handling findings);
- `not stated`.

Never inferred: no basis means `not stated`. Lint requires `search:` on those entries and checks the quoted basis
like `conf`. The view prints them in words ("searched, not found"; "not searched"; "the research does not say
whether this was searched").

**Motivation.** The owner's grading: all six pieces state absences ambiguously, a misinformation risk. TSL: 4 of
the view piece's 14 faults and 2 of the raw piece's 6 were absences stated as fact. The research-brief protocol
already asks researchers to name their routes, and the critic already reports coverage gaps and one-sided
handling, so the information often exists. Many older notes give none, and the field will honestly say
`not stated`.

**How we'll know.** Every `class: search` claim and every gap carries the field (lint). In the re-test: zero view
pieces state an absence without qualification (fact-check category "absence stated as fact", added for v4), and
rubric item 4 is reported for information.

**Baselines.** No addresses change. v3 notes lack a required field, so they fail v4 lint until it is added.

### 4. Omission check: detection misses fail loudly (priority 2)

**Change.**
- **Titles.** Section patterns never match the note's level-1 title, and `REF_TITLE` matches only headings that
  are a references heading ("References", "Sources", "Sources (n)"), not "Sources of …". (H2-04 got no body
  addresses.)
- **Answers.** The patterns add "provisional verdicts", "assessment", "reformulated verdict" and
  "quantitative synthesis". When a note has no detected answers, no labels and no critique, lint fails rather
  than printing "not run"; the builder either declares the answer sections in the Inputs table (`answers:
  §Assessment …`, checked to exist) or writes `answers: none (reason)`. A miss becomes a decision someone makes.
  (TAXRES, H1-RES.)
- **Refuted.** A section of refuted or killed claims makes `critique: refutations only`. Its items stay `C-nnn`
  and become do-not-say as now, but the note still gets the "never checked by a second reader" gap. (GHOST, TSL.)
- **Unaddressed text.** Reference-list annotations and the "Sources not obtained" callout get addresses with a new
  prefix (`R-nnn`), so no existing address moves.
- **The count of what it couldn't address.** Detect and lint report, per input: the note's sentences, how many
  have an address, how many are required and accounted for, and every excluded region by title with its sentence
  count. Lint fails if a region outside a short allow-list (provenance, search record, run conventions, the
  reference entries themselves) is excluded, or if the body yields no addresses. H2-04's "239/239" would have
  read "239/239 required; 0 of about 300 body sentences addressed: FAIL".

**Motivation.** 4 of 8 held-out notes: H2-04's title matched the references pattern (0 body addresses, about 16
findings uncitable, check passed); TAXRES and H1-RES had answers under headings detection did not know (check
"not run"); GHOST's Refuted section counted as a critique (no second-reader gap). Development: TSL the same as
GHOST, and the "Sources not obtained" callout held a finding no entry could cite (16S).

**How we'll know.** Fixtures in `tests/test_kn.py` for each of the five cases, each failing on v3 code and
passing on v4. Run detect on all 14 development notes: every note either runs the omission check or has a
declared reason; no note has 0 body addresses; the excluded-region report lists only allow-listed regions.

**Baselines.** Renumbers addresses in the notes it touches: H2-04 gains B addresses (it had none, so nothing
cited breaks), and TAXRES's and H1-RES's answer sentences move from B to A, shifting the B numbers after them.
`R-nnn` is new and moves nothing. Needs `kn.py migrate` (change 7).

### 5. Checker wording on `holds`: one reading (priority 2)

**Change.** `checker.md`: an entry may leave out what its text says (narrower by omission is ok) but may not add
anything the text does not say, including a setting that narrows the claim. A setting the text does not state is
a `holds` fault. With change 1 most of these become lint errors before the checker sees them.

**Motivation.** The two sentences in v3 ("differs from the text" against "narrower is ok") split the checkers:
CB3's passed added settings (about 6 faults, 7%, under the other reading); the second batch of re-checks faulted
them, including text two earlier checkers had passed.

**How we'll know.** Re-score a seeded sample of 100 v3 entries the checkers passed under the new wording (two
fresh checkers each). It gives a corrected v3 rate to compare v4 against and the checker agreement rate. Target
agreement of 90% or better.

**Baselines.** No addresses change. v3's reported rates stand as reported; the re-scored rate is reported beside
them.

### 6. Ratings kept, with the critic's ruling beside them (priority 3)

**Change.** `rating` keeps the note's own grade; a critic who disputes it is shown beside it: `rating: "Moderate
as a methodological point" (critic: H1-05:C-050: rests on a summary of the preprint)`. The critic item must be in
`from`. The view shows the grade and the dispute.

**Motivation.** H1-05 averaging.1: the builder removed the note's rating to follow the critic, against the format.

**How we'll know.** Lint accepts the form and rejects a critic ruling whose item is not cited; the H1-05 case is
a test fixture.

**Baselines.** No addresses change.

### 7. Sentence splitting, key years, and migration (priority 3)

**Change.**
- `ABBR` gains single initials ("J.", "M. E."), "Supp", "Suppl", "Supp. Fig", "Tab", "Ref".
- The key-year mismatch moves from warning to an information line: it asks for a check the skill forbids, and
  every note with reused Refs.bib keys carries it permanently.
- **`kn.py migrate OLD NEW`** maps a note's `from` references from old addresses to new ones by matching
  sentence text, reports any it cannot map, and rewrites them. This keeps v3 notes usable after detection
  changes.

**Motivation.** Builders' reports: one sentence split into two addresses at initials and "Supp. Fig.", so an
entry citing one half lost the rest; the year warning stands permanently in 4 of the 8 held-out notes and most development notes.

**How we'll know.** Fixtures for initials and "Supp. Fig."; the 14 development notes migrate with every reference
mapped (any unmapped one listed and fixed by hand).

**Baselines.** Changing the splitter renumbers I, A, B and C addresses after any affected sentence in the notes
that have one. That invalidates their `from` references until `migrate` runs. The v3 notes in `../v3/` and
`../heldout/` stay as they are, as baselines.

### Carried over, not in this round

From the v3 README's candidates, with no measurement yet showing them large:
- labels that introduce a list;
- mid-bullet labels;
- the literal standing-word table;
- a verification-status field;
- two inputs' grades for one claim;
- where a label correction ends and a claim correction begins.

Also from the diagnostics: a claim mixing a measured figure with the reviewer's conversion carried one standing
(NFERT manufacturing-co2.6 `repl`). Change 2's class display exposes it; splitting such claims is a format rule
for later.

Not consolidation's job:
- The view writers' selection (class A, 10 facts) is the writing stage's.
- The background the research never gives (definitions, context figures) is a research-brief item
  (`Apps/Improvement Notes/1 Research.md`).

## Build order

1. Change 5, then the report-only lint of change 1 over the v3 notes, scored against the v3 verdicts. If it
   misses its targets, revise before anything else is built.
2. Changes 4 and 7, with `migrate` and the fixtures.
3. Changes 1 (enforced), 3 and 6 in the format, lint and checker.
4. Change 2, with the isolated test on the three v3 notes.
5. The evaluation below.

## Evaluation design for v4

**Development set** (14 notes, all have informed this plan): the six development notes (MB-01 + MB-02, H2-01,
TSL, CB1, CB2, NFERT) and the eight former held-out notes (H2-04, H1-05, H1-02, H1-06, GHOST, CB3, TAXRES,
H1-RES). Rebuilt from scratch under v4 by fresh builders who have not seen the v3 notes. Then first-pass check
and the step 8 loop as before. Reported per note and overall against v3 (122/893 and 84/804), and against the
re-scored v3 rate (change 5), with lint errors at first lint counted separately (what lint caught before any
checker).

**New held-out set.** Same procedure as v3:
- `heldout-v4/criteria.md` is written and committed before the draw.
- The frame is rebuilt from the vault's current result folders by a metadata-only script.
- It excludes every note read so far: the 14 above, EX-01, NP-01 and FD-01, and the five read in part.
- Notes are assigned to the same eight categories by script and drawn at random within each with a recorded
  seed.

Category 5 (critiqued harness note) had one note, GHOST, now used. Unless the vault has gained one since, it is
recorded as empty rather than filled from another category. Built once, checked once, reported without changing
the skill.

**Usability re-test.**
- **Topics:** three new ones, drawn from the new held-out notes once built, so the material is unseen. One
  critiqued run, one standard or harness run, one uncritiqued, preferring soil or microbiology, as before.
- **Pieces:** two writer samples per version per topic, raw notes against the v4 view, so 12 pieces. Same plain
  prompt (audience, length, standalone; no style guidance).
- **Fact-checks:** each piece fact-checked against the full knowledge note, with "absence stated as fact" added
  as a fault category.
- **Blind comparisons:** one per pair (raw 1 with view 1, raw 2 with view 2): 6 in all, each by a fresh reader.
- **Reporting:** the writers' gap notes as before, with v3's numbers from `../usability/results.md` alongside for
  reference (different topics, so not a paired comparison).

**Blinding.**
- Every artefact is named by topic and letter only (`T1-A.md`, `T1-A.writer-notes.md`, `T1-A.factcheck.md`),
  with letters assigned by seed.
- The key is in `ab-key.sealed.md`, committed but not opened until the owner's verdicts are in.
- The owner's copies go to the vault's `temp/` under the letter names.
- The blind readers get the two pieces of a pair as A and B only.
- Results are reported by letter until the owner has graded.

**Writing rubric.** `../writing-rubric.md`: recorded, not applied in v4.

**Cost, roughly.** Development rebuild: about 7 builders (two notes each), 14 first-pass checkers and about 6
re-checkers. Held-out: about 4 builders, 8 checkers and about 4 re-checkers. Re-scoring: 2 checkers. Usability:
12 writers, 12 fact-checkers, 6 blind readers. About 75 agent runs.

## What changes for the baselines, in one place

| Change | Renumbers addresses | v3 notes after the change |
|---|---|---|
| 1 provenance lint | no | fail lint (`holds` form) until migrated; scored in report-only mode first |
| 2 view | no | the view runs on them as they are |
| 3 search status | no | fail lint (new required field) until added |
| 4 omission | yes, in H2-04, TAXRES, H1-RES | `from` references there need `migrate` |
| 5 checker wording | no | v3 rates stand; a re-scored rate is added beside them |
| 6 rating | no | unaffected unless a rating was removed (H1-05 averaging.1) |
| 7 splitter | yes, in notes with initials or "Supp. Fig." | need `migrate` |

The v3 baselines in `../v3/` and `../heldout/` (as built, as fixed, verdicts) are kept unchanged.
