# consolidate v4: improvement plan, revision 2 (plan only, nothing built or run)

Revised 2026-10-22 after the owner's review of revision 1 (in git history, 0e4495d). For review before anything is
built or run, stage A included.

**What the diagnostics settled.** Consolidation is not losing information: nothing the raw writers used was
lost in consolidation (D = 0 in all three topics). Every loss happened when the writer's view dropped a field:
setting, derivation or attribution. TSL's accuracy gap traces to the same cause: 7 of the view piece's 14 faults
come from removed fields, and most of its standing faults from removing `class` (`diagnostics/`). One limit: the
diagnostic only traced facts a raw writer used. A consolidation loss neither writer touched would not show there;
that is the omission check's job (change 4).

**The principle for the view.** Fields that carry epistemic weight are content the writer needs. Only
navigation is stripped.

## Changes

Priorities: **1** large expected effect on faults or writer usefulness; **2** correctness of the checks and the
measurements; **3** small or local.

### 1. Provenance by lint (priority 1; how it is built is decided at gate A)

Two rule families, scored separately against the v3 verdicts before anything is built (stage A):

- **R1, numbers and names.** Every number, year, `[n]` reference marker, capitalised name and quoted phrase in a
  statement (and in a do-not-say `why`) occurs in the entry's `from` items. A name or year is also accepted when it
  matches the author and year of a source in the entry's `src`, because the reference list maps `[28]` to a
  source, so naming it adds nothing. The fix is to cite the sentence that carries it, or cut the token.
- **R2, the `holds` word rule**, in three variants scored side by side:
  - **R2-full:** every word of `holds` occurs in the `from` items, except a fixed list of connectives.
  - **R2-content:** every content word does (stopwords and function words removed).
  - **R2-setting:** every setting-type term does: capitalised words, numbers, tokens with digits or hyphens, and
    terms from a fixed setting lexicon (habitat, organism group, system, method and scale words).

If R2 is adopted, `holds` takes one of two forms: quoted spans from the cited text, or `derived: <words>`, checked
by the adopted variant. If it is not, `holds` stays free text and stays the checker's job under change 5.

**Motivation.**
- 131 of the 133 `holds` faults on record (first pass and re-checks, development and held-out) add words the cited
  text does not contain.
- About 37 of the 63 first-pass `absent` faults quote a name, number, year or reference marker (a rough count by
  pattern).
- The risk: a word rule fails legitimate paraphrase, and builders learn to copy near-verbatim to satisfy it. Then
  the lint becomes the target instead of a measure of faithfulness.

**Thresholds** (fixed now, before any scoring; see stage A for definitions):

| Rule | Adopted if it catches | and flags no more than | Why these numbers |
|---|---|---|---|
| R1 | at least 40% of first-pass `absent` and `numbers` faults | 3% of the entries the checker passed | About half of `absent` faults add a consequence or gloss in ordinary words, which no token rule can see, so 60% is near R1's ceiling; 40% means it catches most of what it is built for. Its tokens are hard facts, so a correct entry failing on one is a real cost; 3% is about three spurious flags in a 110-entry note. |
| R2 (each variant) | at least 60% of first-pass `holds` faults | 5% of the entries the checker passed | 131 of 133 `holds` faults are additions, so a word rule that catches less than 60% is not doing its job. Paraphrase pressure is the binding cost: 5% is about five to seven flags per note, the most a builder will fix by citing the sentence rather than copying text. |

**Decision rule at gate A:**
- R1 is adopted if it passes.
- Of the R2 variants that pass both thresholds, the one with the highest catch rate is adopted (a tie goes to the
  one that flags fewer entries).
- If none passes, the fallbacks in order are: R2-content, R2-setting, then drop R2. If R2 is dropped, only R1 is
  kept and `holds` is left to the checker with change 5's wording.
- The owner decides at the gate. The thresholds only say what the numbers recommend.

**How we'll know (after stage B).** First-pass `holds` and `absent` faults fall by the amounts in gate B. Lint
errors at first lint are counted, as what lint caught before any checker.

**Baselines.** No addresses change. v3 notes fail the adopted rules until rebuilt; they stay as v3 baselines.

### 2. Writer's view: everything with epistemic weight (priority 1)

**The view keeps, for each claim:**
- the statement;
- author and year, from the Sources block for each `src` key ("the reviewer's synthesis" for `src: none`);
- the setting (`holds`);
- class in words: measured, derived, modelled, asserted, the reviewer's reading, a search result;
- standing (`conf`), with the note's own rating and, where the critic ruled on it, the critic's ruling beside it
  (change 6);
- search status on every absence, and whether contrary evidence was searched for (change 3).

**And for the note as a whole:**
- the question answers at the top, as now, plus the verdict and assessment sections it now misses ("Reformulated
  verdict", "Provisional verdicts", "Assessment"; through the same detection as change 4, so the view and the
  omission check agree);
- the do-not-say entries with their reasons;
- the gaps, each with its search status;
- a reference list at the end: every source the view cites, from the BibTeX block.

**The view drops:** trails and trail links, sentence addresses, and `src` keys as raw identifiers (replaced by
author and year in the text and the reference list).

**Also:**
- Process wording is phrased for a writer ("not checked by a second reader", never "no critic checked it" or "the
  review").
- Where an answer refers to the brief's options ("option (a)"), the view quotes the option.

**Motivation.** Raw-only diagnostic: every fact lost to the view writers sat in `holds`, `class` or `src` (3
findings, plus 3 attributions in TSL). TSL view piece: 3 faults from dropped setting, 5 from raised standing,
mostly because `class` was missing. NFERT's view piece called a derived figure "the firmest" and made a
one-system result general. Blind readers preferred raw in all three topics for attribution.

**How we'll know.** In stage C:
- view pieces carry attributions and a reference list;
- facts lost by the view (class B) fall to zero;
- setting and standing faults in view pieces fall;
- blind readers stop naming attribution as a reason to prefer raw.

**Baselines.** The knowledge note does not change; the view is generated and runs on any note.

### 3. Search status on every absence and gap (priority 1)

**Change.** A new field, `search:`, on every claim with `class: search` and on every gap:
- `searched, not found`;
- `not searched`;
- `not stated`.

Each value has a basis, as `conf` does:
- `(note: "…")` for the note's "not found", "no study found" and "unsearched" results and its named routes;
- `(critic: C-nnn)` for the critic's coverage gaps;
- `(run: …)` for the run record.

A second field, `contrary:`, goes on claims and answers that state a conclusion:
- `searched`: a `bounding_or_contrary` finding in the run record, or the note naming contrary evidence it looked
  for;
- `one-sided (critic: C-nnn)`: from the critic's one-sided-handling findings;
- `not stated`.

Both fields are never inferred: no basis means `not stated`. Lint requires `search:` on those entries and checks
the quoted basis as it does for `conf`. The view prints both in words.

**Motivation.**
- The owner's grading: all six pieces state absences ambiguously, a misinformation risk.
- TSL: absences stated as fact were 4 of the view piece's 14 faults and 2 of the raw piece's 6.

**How we'll know.**
- Lint: every `class: search` claim and every gap carries the field.
- Stage C: no view piece states an absence without qualification. The fact-checks gain the category "absence
  stated as fact".

**Baselines.** No addresses change.

### 4. Omission check: detection misses fail loudly (priority 2)

**Change.**
- **Titles.** Section patterns never match the note's level-1 title. `REF_TITLE` matches only a references
  heading ("References", "Sources", "Sources (n)"), not "Sources of …" (H2-04).
- **Answers.** Detection adds "provisional verdicts", "assessment", "reformulated verdict" and "quantitative
  synthesis". When a note has no detected answers, labels or critique, lint fails instead of printing "not run".
  The builder declares the answer sections in the Inputs table (`answers: §Assessment …`, checked to exist) or
  writes `answers: none (reason)`. A miss becomes a decision someone makes (TAXRES, H1-RES).
- **Refuted.** A refuted or killed section makes the critique `refutations only`. Its items become do-not-say
  entries as now, but the note still gets the "never checked by a second reader" gap (GHOST, TSL).
- **Unaddressed text.** Reference-list annotations and the "Sources not obtained" callout get addresses with a new
  prefix, `R-nnn`.
- **The count of what it couldn't address.** Detect and lint report, per input:
  - the note's sentences;
  - how many have an address;
  - how many are required, and how many of those are accounted for;
  - every excluded region, by title, with its sentence count.

  Lint fails if a region outside a short allow-list (provenance, search record, run conventions, the reference
  entries themselves) is excluded, or if the body yields no addresses.

**Motivation.** The check passed falsely on 4 of the 8 held-out notes: H2-04 (0 body addresses, about 16 findings
uncitable), TAXRES and H1-RES (answers under unknown headings), GHOST (Refuted section counted as a critique). The
same Refuted problem appeared in TSL during development, and a 16S finding sat in an unaddressed callout.

**How we'll know.**
- Test fixtures for the five cases, each failing on v3 code and passing on v4.
- In stage B, every development note runs the omission check or has a declared reason, and none has 0 body
  addresses.

**Baselines.** Renumbers addresses in H2-04 (gains B addresses), TAXRES and H1-RES (answer sentences move from B
to A). The v4 evaluation rebuilds every note from scratch, so this matters only for the v3 copies, which stay as
they are.

### 5. Checker wording on what an entry may leave out and add (priority 2)

**Change.** In `checker.md`, the sentence "An entry that is narrower or weaker than its text is ok" is replaced
with:

> An entry may leave out detail its text gives: a second example, another member of a list, a figure it does not
> use. That is ok. Leaving out a qualifier is not leaving out detail. Dropping a scope ("in one soil", "in this
> model", "on mocks"), a hedge ("may", "suggests"), a condition or a denominator makes the claim stronger, and is
> `stronger`. An entry may not add anything its text does not say, including a setting that narrows the claim:
> an added setting is `holds`, anything else added is `absent`. A claim restricted to fewer of the cases its text
> covers (the text says soils and sediments, the entry says soils) is ok.

**Motivation.** The two v3 sentences ("differs from the text" and "narrower is ok") split the checkers. CB3's
checker passed added settings (about 6 faults, 7%, under the other reading). The second batch of re-checks faulted
them, including text two earlier checkers had passed. The new wording must not weaken `stronger`.

**How we'll know.** At the start of stage B, two fresh checkers re-score a seeded sample of 100 v3 entries that
the first-pass checkers passed, under the new wording. This gives a corrected v3 rate to compare v4 with, and the
checkers' agreement. Target: 90% agreement or better.

**Baselines.** No addresses change. v3's reported rates stand, with the re-scored rate beside them.

### 6. Ratings kept, with the critic's ruling beside them (priority 3)

**Change.** `rating` keeps the note's own grade, and a critic who disputes it is shown beside it: `rating:
"Moderate as a methodological point" (critic: H1-05:C-050: rests on a summary of the preprint)`. The critic item
must be in `from`. The view shows both.

**Motivation.** For H1-05 averaging.1, the builder removed the note's rating to follow the critic.

**How we'll know.** Lint accepts the form and rejects a ruling whose item is not cited. The H1-05 case is a test
fixture.

**Baselines.** No addresses change.

### 7. Sentence splitting and key years (priority 3)

**Change.**
- `ABBR` gains single initials ("J.", "M. E."), "Supp", "Suppl", "Supp. Fig", "Tab" and "Ref".
- The key-year mismatch moves from warning to an information line: it asks for a check the skill forbids.

**Motivation.**
- Builders' reports: sentences split at initials and "Supp. Fig.", so an entry citing one half lost the rest.
- The year warning stands permanently in 4 of the 8 held-out notes and in most development notes.

**How we'll know.** Fixtures for initials and "Supp. Fig.".

**Baselines.** Renumbers addresses after any affected sentence. As with change 4, every note is rebuilt, and the
v3 copies stay as they are.

**`kn.py migrate`: dropped.** The address-dependency check (2026-10-22) searched `setup` (the main checkout and
both worktrees), `~/.claude/skills` and the whole vault. Nothing outside consolidation reads or resolves a sentence
address, and nothing but kn.py and its tests reads `*.index.json`.
- **The explain skill and its exemplars** cite whole result notes and sections ("MB-01 §2"), never addresses or
  knowledge-note claim IDs.
- **The usability fact-checks** cite claim IDs only.
- **No vault note** outside the knowledge folders cites an address or a claim ID.

Addresses do appear in five frozen records outside the notes and verdicts. All of them belong to v3 inventories,
which stay as they are:
- `eval/research-run/access-2026-10-21/*.tsv`: about 1,170 rows keyed by address;
- `v3/spot-check-16S.md`: a snapshot that quotes its sentences, so it reads on its own;
- four critic addresses in `v3/acceptance.md`;
- one example in this plan;
- synthetic fixtures in `test_kn.py`.

Renumbering under v4 would make these unmatchable against *v4* inventories, but they are records of v3. Commit
66d17ef's kn.py regenerates the v3 inventories they refer to, if they ever need tracing. Claim IDs, which
downstream ledgers would cite, do not change.

### Carried over, not in this round

Unchanged from revision 1:
- labels that introduce a list;
- mid-bullet labels;
- the literal standing-word table;
- a verification-status field;
- two inputs' grades for one claim;
- where a label correction ends and a claim correction begins;
- claims mixing a measured figure with the reviewer's conversion (NFERT manufacturing-co2.6).

Not consolidation's job: the view writers' selection, and background the research never gives.

## The evaluation, in gated stages

Each stage reports, then stops for the owner's go-ahead.

### Stage A: lint scoring (read-only; the skill does not change)

**Inputs.**
- The 14 notes as built under v3, before any fix: `../v3/as-built/` (6) and `../heldout/as-built/` (8).
- Their inventories (detect re-run on the unchanged result notes).
- The first-pass checker verdicts: `../v3/verdicts/` and `../heldout/verdicts/`, first pass only, 1,697 entries.

**Method.**
- A scoring script in `stageA/` (eval code, not the skill) implements R1 and the three R2 variants.
- Committed with it before it is run: the normalisation (case, punctuation, dashes, thousands separators, plural
  and simple suffix stripping), the stopword and connective lists, and the setting lexicon.
- For each rule, per note and overall:
  - **true positives:** flagged entries the checker faulted as `absent` or `numbers` (R1), or as `holds` (R2);
  - **false negatives:** those faults not flagged;
  - **false positives:** flagged entries the checker passed, as a share of all checker-passed entries (1,491);
  - flags on entries faulted for another reason, reported apart.
- CB3 is reported but left out of R2's false-positive rate, because its checker passed added settings that the
  others faulted. This is decided now.
- For information only, not for the gate: one fresh checker per rule family looks at a seeded sample of up to 30
  of each rule's false positives and says whether each is a real fault the checker missed or a lint error.

**Outputs.** `stageA/results.md`: the table of catches, misses and false positives per rule, which rules meet
their thresholds, and the decision rule's recommendation.

**Agent runs:** 2 (the information-only look at false positives). **Sessions:** one, no waits.

**Gate A:** the owner decides which rules change 1 is built with. Stop.

### Stage B: build v4, rebuild the development set

**Inputs.** Gate A's decision; the 14 development notes' result notes; the v3 numbers.

**Work.**
- Build changes 1 (as decided), 2 to 7, with tests and docs.
- Re-score 100 v3 entries under change 5's wording (two checkers).
- Rebuild all 14 notes from scratch with fresh builders who have not seen the v3 notes. Each note is first-pass
  checked by a fresh checker, fixed by its builder, and re-checked by a different fresh checker until clean, as in
  v3.

**Outputs.**
- `stageB/`: as-built notes, verdicts, re-checks, the omission report per note, lint errors at first lint, and
  `stageB/results.md`.
- The rebuilt notes in the vault.

**Agent runs:** 7 builders, 16 first-pass checkers (16S needs two), about 10 re-checkers and 2 re-scorers: about
35, plus the builders' fix rounds.

**Gate B: pass criteria** (fixed now). Measured on the 14 notes, against v3 on the same notes (206 faults on
1,697 entries, 12.1%):
1. The first-pass fault rate is at most 8%, about a third below v3. It is also below the re-scored v3 rate from
   change 5's sample.
2. `holds` and `absent` faults fall by at least half per 100 entries (v3: 188 on 1,697, 11.1 per 100; v4 at most
   5.5).
3. `stronger` and `numbers` together do not rise (v3: 3; allowed up to 5, given the counts), and `conf` does not
   rise (v3: 9).
4. The omission report: every note runs the omission check or has a declared reason; no note has 0 body addresses;
   no excluded region outside the allow-list.
5. Re-check: at most 15% of fixed entries still faulted in round 1 (v3: 11% development, 14% held-out).

The development notes informed this plan, so passing here is necessary, not sufficient: stage C is the real
test. Report, then stop.

### Stage C: held-out evaluation and usability re-test (only if stage B passes)

**Inputs.**
- The vault's current result notes.
- The v4 skill.
- The writing rubric (recorded, not applied).

**Work.**
- **Held-out set.**
  - `heldout-v4/criteria.md` is written and committed before the draw.
  - The frame is rebuilt by a metadata-only script.
  - It excludes every note read so far: the 14 development notes, EX-01, NP-01 and FD-01, and the five read in
    part.
  - Notes are assigned to categories by script, with one seeded draw per category.
  - **Category 5 (critiqued harness note) is dropped:** GHOST was its only note, and a note for it will come from
    future runs.
  - So seven notes, each built once, checked, fixed and re-checked, and reported without changing the skill.
- **Usability re-test.**
  - **Topics:** three, chosen from the seven drawn notes by the v3 rule: one critiqued run, one standard or
    harness run, one uncritiqued, preferring soil or microbiology. They are seeded where more than one qualifies.
  - **Pieces:** two writer samples per version per topic, raw notes against the v4 view: 12 pieces, same plain
    prompt.
  - **Fact-checks:** each piece against the full knowledge note, with "absence stated as fact" as a fault category.
  - **Blind comparisons:** one per pair (raw 1 with view 1, raw 2 with view 2), 6 in all.
  - **Reporting:** v3's numbers alongside for reference (different topics).
- **Blinding.**
  - Pieces, writer notes and fact-checks are named by topic and letter only (`T1-A.md`, `T1-A.notes.md`,
    `T1-A.factcheck.md`), with letters assigned by seed.
  - The key is in `ab-key.sealed.md`, unopened until the owner has graded.
  - The owner's copies go to the vault's `temp/` under letter names.
  - Results are reported by letter until then.

**Outputs.** `heldout-v4/` (criteria, frame, draw, as-built, verdicts, results) and `usability-v4/` (pieces,
notes, fact-checks, comparisons, sealed key, results by letter).

**Agent runs:** 4 builders, 8 checkers, about 4 re-checkers, 12 writers, 12 fact-checkers and 6 blind readers:
about 46, plus fix rounds.

**Gate C:** report, then stop. The owner grades the pieces before the key is opened.

## Running the stages: sequential sessions

The only thing borrowed from the research workflow is its scheduling. Batches run one at a time, in a fixed order,
with a wait between them, so a long run does not hit the 5-hour usage limit partway through. Nothing else carries
over: no briefs, preflight readers, critics, review loops or stage-2 checks. The evaluation's own checkers and
re-checks stay as designed.

**The wait is 15 minutes**, the research default; there is no reason to change it. If a usage-limit warning
appears, the current session finishes its open batch, writes its state record and stops. The next session starts
after the limit resets, as happened in v3.

**Sizing.** Estimates from this round's subagent token counts:

| Run | Observed |
|---|---|
| a builder, one or two notes, fixes included | 250k to 280k tokens |
| a first-pass checker, 100 to 120 entries | 70k to 110k |
| a re-checker | 40k to 75k |
| a reader (diagnostics) | 75k to 130k |

Writers and fact-checkers are estimated at 80k to 130k each. In v3 the usage warning came after roughly 2 to
2.5 million subagent tokens in one window. **Each session is sized to about 1 million**, well within that.

**Self-contained sessions.**
- A session works one group of notes from start to finish: build, first-pass check, fixes by the same builder,
  re-checks until clean. A builder's fix rounds therefore never need resuming across sessions.
- Before it ends, a session writes all its outputs and appends to `state.md` in the stage folder: what finished,
  what is next, and any open item.
- A later session starts by reading `state.md`, resumes from the last completed batch, and never redoes or
  half-does one.

**Stage A**: one session, no agents except the two information-only readers (about 0.2 million).

**Stage B:**

| Session | Batch | Agent runs | Estimate |
|---|---|---|---|
| B0 | build changes 1 to 7, tests, docs; re-score 100 v3 entries | 2 re-scorers | 0.2M |
| B1 | 16S (MB-01 + MB-02): one builder, two checkers, re-checks | about 5 | 0.9M |
| B2 | H2-01 + TSL; CB1 + CB2: two builders, four checkers, re-checks | about 8 | 1.0M |
| B3 | NFERT + CB3; GHOST + TAXRES + H1-RES: two builders, five checkers, re-checks | about 9 | 1.0M |
| B4 | H2-04 + H1-05: one builder, two checkers, re-checks | about 4 | 0.6M |
| B5 | H1-02 + H1-06: one builder, two checkers, re-checks | about 4 | 0.6M |
| B6 | compile `stageB/results.md` against v3 and the gate criteria | none | small |

15 minutes between sessions B1 to B5.

**Stage C:**

| Session | Batch | Agent runs | Estimate |
|---|---|---|---|
| C0 | rebuild the frame, write and commit the criteria, draw | none | small |
| C1 | held-out notes 1 to 4: two builders, four checkers, re-checks | about 8 | 1.0M |
| C2 | held-out notes 5 to 7: two builders, three checkers, re-checks | about 7 | 0.9M |
| C3 | pick the three topics; views; topic 1: 4 writers, 4 fact-checkers, 2 blind readers | 10 | 1.0M |
| C4 | topic 2: the same | 10 | 1.0M |
| C5 | topic 3: the same | 10 | 1.0M |
| C6 | compile results by letter; copy the letter-named pieces to the vault's `temp/` | none | small |

15 minutes between sessions.

**In all:** about 2 runs in stage A, 35 in stage B and 46 in stage C, plus builders' fix rounds, over 14 sessions.

## Unseen-note budget

Unseen notes are counted in units (a set in parts counts once), excluding everything read. The vault's result
folders hold the same 75 notes the v3 frame listed: none new since 2026-10-21.

| # | Category | v3 frame | Drawn in v3 | Unseen now | Stage C draws | Unseen after stage C |
|---|---|---|---|---|---|---|
| 1 | Critiqued, labelled, with standing | 3 | 1 | 2 | 1 | 1 |
| 2 | Critiqued, labelled, without standing | 2 | 1 | 1 | 1 | **0** |
| 3 | Critiqued, numbered (research workflow) | 26 | 1 | 25 | 1 | 24 |
| 4 | Critiqued, author-year (research workflow) | 4 | 1 | 3 | 1 | 2 |
| 5 | Critiqued harness note | 1 | 1 | **0** | dropped | 0 |
| 6 | Uncritiqued, with answers | 5 | 1 | 4 | 1 | 3 |
| 7 | Uncritiqued harness note | 7 | 1 | 6 | 1 | 5 |
| 8 | Uncritiqued, no answers | 11 | 1 | 10 | 1 | 9 |
| | **All** | **59** | **8** | **51** | **7** | **44** |

The usability topics are taken from stage C's seven drawn notes, so they use up nothing extra. If they were drawn
separately, three more would go, from categories 3, 7 and 8 at the v3 rule.

**What the backlog supports.** Category 2 runs out at stage C, and category 1 has one note left after it. So one
more full evaluation after v4 is possible only with category 2 dropped, and none after that, unless new research
runs add notes. Labelled-citation notes (categories 1 and 2) come only from runs under the current research
workflow, and category 5 needs a critiqued harness run. Categories 3, 7 and 8 have plenty.

## What changes for the baselines

| Change | Renumbers addresses | v3 notes |
|---|---|---|
| 1 provenance lint | no | fail the adopted rules; scored read-only in stage A |
| 2 view | no | the view runs on them as they are |
| 3 search status | no | lack the new field |
| 4 omission | yes, in H2-04, TAXRES and H1-RES | kept as they are; v4 rebuilds |
| 5 checker wording | no | v3 rates stand; a re-scored rate goes beside them |
| 6 rating | no | unaffected |
| 7 splitter | yes, after affected sentences | kept as they are; v4 rebuilds |

The v3 baselines in `../v3/` and `../heldout/` stay unchanged. The writing rubric (`../writing-rubric.md`) stays
recorded and unapplied.
