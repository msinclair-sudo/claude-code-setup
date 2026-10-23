# consolidate v4: improvement plan, revision 5

**Revision 5 (2026-10-23), after B2.** Two owner decisions.
- **Measurement.** Every first pass, on the v3 baseline and on v4, is two fresh checkers per entry, and a fault from
  either counts. Both sides use packets of 60 entries. Packet size is part of the frozen checking procedure. The
  baseline is re-checked to match: a second checker on each of its five packets.
- **One builder instruction**, before the rebuild. Every setting, name or detail in an entry comes from a sentence
  listed in its `from`; if it comes from elsewhere in the note, that sentence's address is added to `from`. It is a
  hard rule in SKILL.md and widens format.md's existing rule for `holds`. It is builder-side only, and the checker
  stays frozen.

**Revision 4 (2026-10-23), at the B1 checkpoint.** The owner chose option 2: add the omission hint and confirm it on
a fresh planted set before B2 (stage B, step 2b below). The checker is then frozen through stage C. B2's sample
excludes both planted pools. Nothing else changes.

**Revision 3 (2026-10-22), after gate A and the owner's spot-check.** Change 1 and stage B were revised on the
owner's decisions at gate A. After the spot-check, stage B gained a planted-fault test and change 2 a do-not-say
sentence rule. All of this is for review before B0 runs. The rest is revision 2, as approved (176eeeb), except that stage C now excludes the
writing set-aside.
- Stage A is done: `stageA/results.md`.
- The writing set-aside is drawn: `../writing-setaside/`.
- Revision 1 is in git history (0e4495d).

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

### 1. Provenance hints for the checker (priority 1; decided at gate A)

**Decision (owner, gate A).** No lint rule met its threshold, so none becomes a lint gate. Instead the lint's
findings become **hints for the checker**: under each entry in a checker packet, the words and tokens not found in
its cited text. R1's number, year and marker check is folded into the hints; there is no exception to the
thresholds.

**What the hints contain.** For each claim and do-not-say entry, as scored in stage A (`stageA/rules.md`, with the
tokeniser fix):
- **R1 tokens not found:** numbers, years, `[n]` markers, capitalised names and quoted phrases, with the `src`
  author and year allowance;
- **R2-setting words not found** in `holds`.

Of the three R2 variants, the setting variant gives the checker the most to work with per flag. In stage A's
sample, 9 of the 19 setting flags on checker-passed entries were real faults, against 11 of 28 for the content
variant. It also flags about half as many entries (32% against 58%), so the hints do not drown the packet. This is
a choice for the owner's review; the hint-effect measurement in stage B tests it.

**Rules for the hints.**
- **Hints go to the checker only, never to builders.** Only `kn.py packets --hints` produces them; `lint` never
  prints them. The checker packets are made by whoever runs the check, and the builder receives only the verdict
  lines. SKILL.md's step 8 says so. In the evaluation, the orchestrating session makes all packets.
- **The checker's instructions (`checker.md`) gain:**

  > Under some entries, "Not found in the cited text" lists words or numbers a script could not find in the quoted
  > text. They show where to look, not what is wrong. A paraphrase, another word form, an abbreviation spelled out,
  > or a word that adds nothing is fine. Judge, as always, whether the entry says anything its cited text does not
  > support. An entry with no hint gets the same care as one with hints.
- **The hint code lives in kn.py**, so v3 and v4 packets get identical hints. It reuses the stage A rules, moved
  from the eval script into the skill without change.

**Motivation (stage A).**
- As gates, R1 caught 28% of `absent` and `numbers` faults with 9.3% false flags, and R2 caught 81% to 99% of
  `holds` faults with 32% to 60%. A gate would push builders to copy text.
- In the false-positive sample, about half of R1's flags and a third of R2's on checker-passed entries were faults
  the checker had missed. The hints aim the checker at those, and nothing blocks the builder.

**How we'll know.** Stage B measures it directly: the same 100 entries are checked with and without hints, and
the verdict changes are reported (stage B, the hint-effect measurement).

**Baselines.** No addresses change. The v3 notes are re-scored with the same hint-equipped checker (stage B), so
v3 and v4 are compared on equal terms.

#### Stage A record (the rules scored as gates)

Two rule families, scored separately against the v3 verdicts before anything was built:

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

**Result (stage A):** no rule met its thresholds (`stageA/results.md`).

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
- **Do-not-say entries are full sentences a writer can use** (owner, after the spot-check). The `dns` statement
  is the wording not to use, written as a complete sentence a writer might write; `why` is a complete sentence;
  the view prints "Say instead" with the full statements of the `instead` entries. The format gains this rule, and
  the builder writes it; the view adds no words of its own.
  - **Spot-check entry 20 (dns.27), as built:** `"About 2.2" as the community copy number of water.` · why: `the
    EMP value pools free-living (soil, water, sediment) and plant-associated samples`. It is faithful, but a
    writer cannot use it.
  - **The same entry, as a writer could use it:** "Water communities carry about 2.2 16S copies per genome." ·
    why: "The EMP's value of about 2.2 pools free-living samples (soil, water and sediment) with plant-associated
    ones, so it is not a value for water." · say instead: community-copy-number.1.
  - **The checker** still judges faithfulness. Making a sentence whole may rephrase the cited wording but must not
    add to it.
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

**How we'll know.** Stage B re-scores about 300 v3 entries with this wording and the hints (change 1). The
result is the corrected v3 baseline that v4 is compared with. The hint-effect measurement, two checkers per
condition, also gives the checkers' agreement under the new wording.

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

### For v5 (owner, 2026-10-23, after B1b; recorded, not in this round)

The checker is frozen through stage C, so none of these change v4.
1. **Detail versus scope, in the checker wording.** Add worked examples showing that limits on method, site, sample
   count or relatedness ("measured by qSIP", "in one forest soil", "(12 symbionts)", "related recovered genomes")
   are scope, not detail. The test cases are the five B1b plants all four judges missed
   (`stageB/planted2/results.md`):
   - H1-06/perturbation-response.9;
   - H2-01/other-field-transfer.1;
   - H1-02/sample-dependence.7;
   - H1-RES/pangenome.11;
   - 16S/ploidy.11.

   Any new wording is confirmed on a freshly planted set, as in B1b.
2. **Two independent checkers per entry, a fault from either counted.** Test the catch rate against the cost on a
   planted set. B1 and B1b give a first reading: the "either" rate against each judge alone (B1b omissions: 26 and
   25 either, against 24 to 26 per judge), at twice the checker tokens.
3. **Decision rules compare conditions.** A rule about an intervention compares the conditions on the same claims,
   never an absolute level for the checker. B1b's rule tripped on "either W judge faults more than 5% of controls",
   though the judges without the hint faulted as many.

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

**Done (6046eb2).** No rule met its thresholds. The owner chose hints for the checker (change 1, revision 3), and
approved the writing set-aside, drawn on 2026-10-22 (d7c1a9f).

### Stage B: build v4, re-score v3, rebuild the development set

**The owner's spot-check** (20 entries, `../v3/spot-check-16S.md`), against the sealed first-pass checker
verdicts. The owner's labels are mapped to fault kinds as the owner gave them. The owner had seen comments on
entry 5 beforehand.

| Entry | Owner | Checker | Which way |
|---|---|---|---|
| 1 to 3, 7 to 9, 11 to 17, 19 | ok | ok | agree (11 and 16: language, a readability point, not a fault) |
| 4 primers.5 | ok | `absent` ("abstract only" not in the text) | checker stricter: an addition |
| 5 copy-number-correction.8 | `stronger` (drops "but not DNA mocks or most mock tests in one preprint") | ok | checker missed an omission (a dropped counter-clause) |
| 6 copy-number-correction.15 | `conf`/`critic` (`src` shows `repl`, `conf` is `single`) | ok | checker missed a contradiction between fields |
| 10 bias-consistency.1 | ok | `holds` (a setting not in the text) | checker stricter: an addition |
| 18 compositional-analysis.3 | `holds` (omits McLaren 2022) | `holds` ("model" not in the text) | both fault it, for opposite reasons: the owner an omission, the checker an addition |
| 20 dns.27 | ok for faithfulness, unreadable as do-not-say | ok | agree on faithfulness; readability goes to change 2 |

They agree on 16 of 20 (ok or fault). Each found 3 faults, but only one entry is shared, and it is faulted for
opposite reasons. **The checker catches additions and misses omissions** (dropped hedges and counter-evidence,
fields that contradict each other), which is the riskier kind. Hence the planted-fault test, before the baseline
is fixed. B0 records this table as `stageB/spotcheck.md`. No agents.

**Inputs.**
- The owner's decisions at gate A.
- The 14 development notes' result notes.
- The 14 v3 as-built notes and their first-pass verdicts.
- The v3 code (66d17ef) for v3 inventories.

**Work, in order.**
1. **Build** changes 1 (hints) and 2 to 7, including the do-not-say sentence rule, with tests and docs.
2. **Planted-fault test** (owner, after the spot-check). This tests whether the hint-equipped checker catches
   known faults, by kind, especially omissions.
   - **The pool:** a seeded draw of about 130 claims that the v3 first-pass checker passed, spread across the 14
     notes. That is enough for about 64 plants and 40 controls after screening. These claims are kept out of the
     baseline sample (step 3).
   - **Screening:** a fresh screener, using change 5's wording without hints, confirms each claim is clean.
     Claims it faults are set aside (and listed), because a planted fault on top of a real one would be caught
     for the wrong reason.
   - **Planting:** of the clean claims, about 64 get one known edit each, weighted towards omissions (owner):
     about 20 with a hedge removed, about 20 with a counter-clause dropped, and about 8 each for the other three
     types. Types are assigned by seed among the claims where each applies; about 40 stay unedited as controls. A
     fresh planter makes one minimal edit per claim and records the before, the after and the intended fault
     kind.
   - **The plants must be realistic** (owner). Omissions drop words that actually appear in the cited sentences:
     spot-check entry 5 is the model, a "but not DNA mocks or most mock tests in one preprint" present in the
     cited text and left out of the entry. Additions are ones a builder might plausibly make. The report notes
     that planted faults may still be easier to catch than natural ones.

     | Edit type | Plants | What changes | Fault it should be | From |
     |---|---|---|---|---|
     | Hedge or scope removed | about 20 | a hedge or scope present in the cited sentences ("may", "suggests", "in one soil", "on mocks", "in this model", a condition or a denominator) is left out of the entry | `stronger` | change 5's examples |
     | Counter-clause dropped | about 20 | a "but not …" or contrary finding present in the cited sentences is left out | `stronger` | spot-check entry 5 |
     | True setting added | about 8 | a setting from another sentence of the same result note, one the entry does not cite (true in the source, unsupported by the cited text) | `holds` | the checker's known strength, as a control on the method |
     | Number changed slightly | about 8 | 0.77 becomes 0.71, 36.6 becomes 33.6 | `numbers` | |
     | Standing raised | about 8 | in the statement ("one study found" becomes "studies find") or in a field (`conf` single becomes repl, or a `src` label made to disagree with `conf`) | `stronger` or `conf` | spot-check entry 6 |

     The first-version table, kept for its "From" notes:

     | Edit type | What changes | Fault it should be | From |
     |---|---|---|---|
     | Hedge or scope removed | drop "may", "suggests", "in one soil", "on mocks", "in this model", a condition or a denominator | `stronger` | change 5's examples |
     | Counter-clause dropped | drop the "but not …" or contrary finding the cited text gives | `stronger` | spot-check entry 5 |
     | True setting added | add a setting from another sentence of the same result note that the entry does not cite: true in the source, unsupported by the cited text | `holds` | the checker's known strength, as a control on the method |
     | Number changed slightly | 0.77 becomes 0.71, 36.6 becomes 33.6 | `numbers` | |
     | Standing raised | in the statement ("one study found" becomes "studies find") or in a field (`conf` single becomes repl, or a `src` label made to disagree with `conf`) | `stronger` or `conf` | spot-check entry 6 |
   - **Validation:** a fresh validator confirms that each planted claim differs from its clean version only by the
     intended edit, and that the edit is a fault under change 5's wording. Failures are dropped and counted.
   - **The judges:** two fresh hint-equipped checkers each judge all the claims (planted and controls), mixed in
     seeded random order. They are told it is an ordinary check. Hints are recomputed for the edited claims by the
     v4 code, as a real check would show them.
   - **The report**, per edit type:
     - claims planted;
     - caught by each checker and by either;
     - caught with the intended kind;
     - whether a hint was present.

     Omission edits carry no hints by construction, so their catch rate is the checker's unaided rate. The report
     also gives the controls' false-fault rate, and Wilson intervals throughout (about 20 or 8 per type, so the
     intervals are wide and are reported as such). It notes that planted faults may be easier to catch than
     natural ones.
   - **Checkpoint: stop and report after this step.** If a type's catch rate is poor, the checker's setup can
     change before the baseline is scored with it; changing it afterwards would mean re-scoring the baseline.
     - **The first fix to test, if omissions are caught poorly** (owner): an **omission hint** for the checker. It
       lists the hedge, negation and contrast words in the cited sentences that are missing from the entry ("may",
       "suggests", "not", "but", "only", "however", "one study", "in this model"). Checker only, like the other
       hints.
     - **Any change is confirmed on a freshly planted set**, not the same one (owner): a new seeded draw of clean
       claims, newly planted and validated, judged by two fresh checkers with the new setup.
   - **Done (7b5a0b3):** `stageB/planted/results.md`. The owner chose the omission hint (revision 4).

2b. **B1b: the omission hint, confirmed on a fresh planted set** (owner, at the checkpoint). The four double misses in
   B1 were scope qualifiers that do not look like hedges ("by this corpus", "only as a nearest precedent", "reported
   as a distribution", a second source's contrary argument).
   - **The hint** (`kn.omission_hints`, checker packets only, like the other hints). It covers hedge, negation,
     contrast and scope words in the cited text (the fixed list `OMIT_WORDS`). A word counts as carried only when the
     entry's own wording has it followed, within four words, by the next content word after it in the cited text.
     The entry's own wording is the statement and the free-text fields: not `from`, `src`, `trail`, `conf`,
     `class`, `search` or `contrary`. Each word not carried is listed with up to four following words, stopping at
     punctuation. Overlapping windows merge, and at most 8 are listed. The list and rule were fixed before the
     fresh set was drawn and are not tuned on it.
   - **The fresh set** (`stageB/tools/planted2.py`, `stageB/planted2/`): 200 v3-passed claims outside B1's pool, by
     seed (pool 20261028, assignment 20261029, judging order 20261030, controls 20261031), screened, planted and
     validated as in B1. Plants are weighted to scope-type omissions:
     - scope qualifier 24;
     - counter or contrary 12;
     - hedge 8;
     - setting, number and standing 4 each.

     Up to 45 controls. The planter never sees the word list.
   - **Judges:** four fresh checkers, all claims, same order, packets identical apart from the omission line. W1
     and W2 get the omission hint and the new checker.md paragraph. N1 and N2 get B1's setup (checker.md at
     7b5a0b3). One fresh adjudicator, without hints and blind to condition, reads every control any judge faulted
     (information only).
   - **Decision rule, fixed before drawing:**
     - **Noticeably more false alarms:** W's control faults (summed over its two judges) exceed N's by 3 or more,
       or either W judge faults more than 5% of controls. Then report, do not adopt, and stop.
     - **Adopt** if W's two judges together catch more omission plants (scope, counter, hedge) than N's, without
       noticeably more false alarms.
     - **Otherwise** do not adopt; the checker stays at B1's setup.
     - Raw counts decide. The adjudicator's reading is reported beside them.
   - **Then the checker is frozen through stage C.** That means `checker.md`, `hints()`, `omission_hints()` and
     `packets --hints`, at the commit recorded in `stageB/state.md`. If the hint is not adopted, its code is
     reverted.
   - **Done: not adopted** (`stageB/planted2/results.md`). It gave no gain: omission catches were 50 against 50
     over two judges. It raised no false alarms: control faults were 5 against 6, all four faulted controls were real
     faults, and the rule tripped only on its absolute 5% clause. **The checker is frozen at B1's setup**, with
     content identical to 7b5a0b3. The tested code is kept in `stageB/tools/omission_hint.py`.
3. **Re-score v3 (the new baseline).**
   - **The sample:** about 300 entries from the 14 v3 as-built notes, excluding the B1 and B1b planted pools, by
     seeded stratified draw. At least 10 per note; the rest are allocated in proportion to each note's entries, by largest remainder.
   - **The packets:** made with the v3 inventories (the v3 code, so the `from` addresses resolve as the v3
     checkers saw them) and the v4 hint code.
   - **The checkers:** fresh, with the v4 `checker.md` (change 5's wording and the hint paragraph), about 60
     entries each.
   - **The estimate:** the v3 rate is weighted back to each note's size.
4. **Measure the hint effect.** A seeded subset of 100 of the 300, stratified 60 with at least one hint and 40
   with none.
   - **The runs:** besides its with-hints verdicts from step 2 (W1), it is checked by one more fresh checker with
     hints (W2) and two fresh checkers without hints (N1, N2). Packets are identical apart from the hint lines.
   - **The report:**
     - agreement within each condition (W1 and W2, N1 and N2): the noise floor;
     - agreement across conditions;
     - fault rates and kinds with and without hints, overall and on hinted and unhinted entries;
     - every entry whose verdict differs across conditions.
   - **The adjudicator:** one fresh adjudicator, without hints and blind to which verdict came from which
     condition, judges each discordant entry. That shows whether the hints found real faults, induced false ones,
     or both.
5. **Rebuild** all 14 notes from scratch with fresh builders who have not seen the v3 notes. Each note is
   first-pass checked by a fresh hint-equipped checker, fixed by its builder, and re-checked by a different fresh
   hint-equipped checker until clean, as in v3.
   - **Revision 5:** the first pass is two fresh checkers per 60-entry packet (`kn.py packets --hints`, its
     default size). The builder fixes every fault from either, getting only verdict lines. Re-checks stay at one fresh
     checker per round, as in v3, whose re-check rates (11% and 14%) criterion 5 is compared with.
6. **Do-not-say readability.** Every rebuilt note's writer's view is generated. One fresh reader, given only the
   Do not say sections, marks each entry as usable by a writer as it stands, or a fragment, with a reason. This is
   reported with a target of at least 90% usable. It is not a gate criterion unless the owner makes it one.

**Outputs.**
- `stageB/spotcheck.md`: the owner's spot-check against the checker.
- `stageB/planted/`: the pool, screening, edits (sealed key), validation, both checkers' verdicts, catch rates by
  type.
- `stageB/baseline/`: sample, packets, verdicts, the re-scored v3 rates.
- `stageB/hints/`: the four runs, agreement tables, adjudication.
- `stageB/` rebuild: as-built notes, verdicts, re-checks, the omission report per note, do-not-say readability.
- `stageB/results.md`.
- The rebuilt notes in the vault.

**Agent runs:**
- Planted faults: 1 screener, 1 planter, 1 validator and 2 checkers. If the setup changes, a fresh set needs a
  screener, planter, validator and 2 checkers again.
- Re-score: 5 checkers.
- Hint effect: 3 checkers and 1 adjudicator.
- Rebuild: 7 builders, 16 first-pass checkers (16S needs two) and about 10 re-checkers.
- Do-not-say readability: 1 reader.

About 48, plus the builders' fix rounds.

**Gate B: criteria** (fixed now). v4's first pass on the 14 rebuilt notes, against the re-scored v3, with the
same checker setup:
1. **First-pass fault rate:** v4 at most two thirds of re-scored v3 (a third lower).
2. **`holds` plus `absent` faults** per 100 entries: v4 at most half of re-scored v3.
3. **`stronger` plus `numbers`** per 100 entries does not rise above re-scored v3, and `conf` does not either.
   Every `stronger` and `numbers` fault, in v4 and in the re-scored v3, is listed individually (note, entry,
   checker's reason).
4. **Omission:** every note runs the omission check or has a declared reason; no note has 0 body addresses; no
   excluded region outside the allow-list.
5. **Re-check:** at most 15% of fixed entries still faulted in round 1 (v3: 11% development, 14% held-out).

The absolute 8% target is dropped.

**Confidence intervals** (95%), reported for every rate and ratio in criteria 1 to 3:
- **For each rate:** Wilson intervals.
- **For each v4/v3 ratio:** a bootstrap with 10,000 resamples and a fixed seed, resampling v3's entries within
  each note (its stratified sample) and v4's notes as clusters. Entries from one note share a builder, so they
  are not independent.

The criteria are judged on the point estimates. Where a ratio's interval reaches 1 (no difference), the report
says so plainly. v3's reported 12.1% is shown beside the re-scored rate, to show how far it understated.

**A missed criterion means stop and report the numbers.** It is not an automatic fail: the owner decides. The
development notes informed this plan, so passing here is necessary, not sufficient; stage C is the real test.
Report, then stop.

### Stage C: held-out evaluation and usability re-test (only if stage B passes)

**Inputs.**
- The vault's current result notes.
- The v4 skill.
- The writing rubric (recorded, not applied).

**Work.**
- **Held-out set.**
  - `heldout-v4/criteria.md` is written and committed before the draw.
  - The frame is rebuilt by a metadata-only script.
  - It excludes every note read so far (the 14 development notes, EX-01, NP-01 and FD-01, and the five read in
    part) and the six writing set-aside units (`../writing-setaside/setaside.md`).
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
| B0 | record the spot-check; build changes 1 to 7 (with the do-not-say sentence rule), tests, docs | none | small |
| B1 | planted-fault test: screener, planter, validator, two checkers; report and **stop (checkpoint)** | 5 | 0.4M |
| B2 | re-score about 300 v3 entries (5 checkers); hint effect on 100 (W2, N1, N2, then 1 adjudicator) | 9 | 0.8M |
| B3 | 16S (MB-01 + MB-02): one builder, two checkers, re-checks | about 5 | 0.9M |
| B4 | H2-01 + TSL; CB1 + CB2: two builders, four checkers, re-checks | about 8 | 1.0M |
| B5 | NFERT + CB3; GHOST + TAXRES + H1-RES: two builders, five checkers, re-checks | about 9 | 1.0M |
| B6 | H2-04 + H1-05: one builder, two checkers, re-checks | about 4 | 0.6M |
| B7 | H1-02 + H1-06: one builder, two checkers, re-checks | about 4 | 0.6M |
| B8 | do-not-say readability (1 reader); compile `stageB/results.md`: rates, ratios and intervals against re-scored v3; every `stronger` and `numbers` fault listed | 1 | small |

15 minutes between sessions B2 to B8. B1 stops at its checkpoint for the owner. B2 reports its baseline and hint
numbers in `state.md` and does not stop: the gate is at the end of B8.

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

**In all:** 2 runs in stage A (done), about 48 in stage B and 46 in stage C, plus builders' fix rounds, over 17
sessions.

## Unseen-note budget

Unseen notes are counted in units (a set in parts counts once), excluding everything read. The vault's result
folders hold the same 75 notes the v3 frame listed: none new since 2026-10-21.

| # | Category | v3 frame | Drawn in v3 | Unseen before the set-aside | Writing set-aside (drawn) | Stage C draws | Unseen after stage C |
|---|---|---|---|---|---|---|---|
| 1 | Critiqued, labelled, with standing | 3 | 1 | 2 | 0 | 1 | 1 |
| 2 | Critiqued, labelled, without standing | 2 | 1 | 1 | 0 | 1 | **0** |
| 3 | Critiqued, numbered (research workflow) | 26 | 1 | 25 | 2 | 1 | 22 |
| 4 | Critiqued, author-year (research workflow) | 4 | 1 | 3 | 0 | 1 | 2 |
| 5 | Critiqued harness note | 1 | 1 | **0** | 0 | dropped | 0 |
| 6 | Uncritiqued, with answers | 5 | 1 | 4 | 1 | 1 | 2 |
| 7 | Uncritiqued harness note | 7 | 1 | 6 | 2 | 1 | 3 |
| 8 | Uncritiqued, no answers | 11 | 1 | 10 | 1 | 1 | 8 |
| | **All** | **59** | **8** | **51** | **6** | **7** | **38** |

The usability topics are taken from stage C's seven drawn notes, so they use up nothing extra. If they were drawn
separately, three more would go, from categories 3, 7 and 8 at the v3 rule.

**What the backlog supports.**
- Category 2 runs out at stage C, and category 1 has one note left after it. So one more full evaluation after v4
  is possible only with category 2 dropped, and none after that, unless new research runs add notes.
- Category 1 is refilled only by standard or deep runs under the current research workflow. Category 2 cannot be
  refilled, because rule 3a never leaves standing out. Category 5 needs a critiqued harness run.
- Categories 3 and 8 have plenty.
- The owner will choose fresh topics for evaluation later. The triggered follow-ups (MB-01 first) are to be run
  for their content.

## What changes for the baselines

| Change | Renumbers addresses | v3 notes |
|---|---|---|
| 1 provenance hints | no | re-scored with the hint-equipped checker in stage B |
| 2 view | no | the view runs on them as they are |
| 3 search status | no | lack the new field |
| 4 omission | yes, in H2-04, TAXRES and H1-RES | kept as they are; v4 rebuilds |
| 5 checker wording | no | v3 rates stand; a re-scored rate goes beside them |
| 6 rating | no | unaffected |
| 7 splitter | yes, after affected sentences | kept as they are; v4 rebuilds |

The v3 baselines in `../v3/` and `../heldout/` stay unchanged. The writing rubric (`../writing-rubric.md`) stays
recorded and unapplied.
