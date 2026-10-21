# Held-out evaluation of consolidate v3: results (2026-10-22)

Run once, on v3 as committed (66d17ef), on eight notes drawn by seed 20261022 from a frame that excluded every
note already read (`criteria.md`, written before the draw; `draw.md`). The skill was not changed during the run.
Each note was built by a builder that had not seen the development notes, checked by a fresh checker that saw
only the packets, fixed by its builder, and re-checked by a different fresh checker until clean (step 8).

- `as-built/`: each note as its builder first finished it, before any check.
- `verdicts/`: first-pass verdicts (`<ID>.md`) and every re-check (`<ID>.recheck-N.md`).
- The fixed notes are in the vault, beside their inputs (`…/Knowledge/`, `…/knowledge/`).

| # | Category | ID | Note |
|---|---|---|---|
| 1 | Critiqued, labelled, with standing | H2-04 | Sources of functional covariation and cross-level functional axes |
| 2 | Critiqued, labelled, without standing | H1-05 | Functional and taxonomic turnover in soil microbial communities |
| 3 | Critiqued, numbered (research workflow) | H1-02 | Recovery artefacts in the gene content of metagenome-assembled genomes |
| 4 | Critiqued, author-year (research workflow) | H1-06 | Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring |
| 5 | Critiqued harness note | GHOST | Positioning graph nodes that lack features |
| 6 | Uncritiqued, with answers | CB3 | Agriculture's share of global greenhouse gas emissions |
| 7 | Uncritiqued harness note | TAXRES | Reference taxonomies and taxon-name resolution |
| 8 | Uncritiqued, no answers | H1-RES | Decoupling of microbial function from taxonomy |

## First-pass faults against the v3 development run

| ID | Entries | Faulted | stronger | conf | numbers | absent | critic | merged | holds |
|---|---|---|---|---|---|---|---|---|---|
| H2-04 | 127 | 18 (14%) | 0 | 1 | 0 | 2 | 0 | 0 | 15 |
| H1-05 | 142 | 35 (25%) | 0 | 1 | 0 | 6 | 1 | 0 | 27 |
| H1-02 | 126 | 17 (13%) | 1 | 1 | 0 | 7 | 0 | 0 | 8 |
| H1-06 | 138 | 8 (6%) | 0 | 0 | 0 | 5 | 1 | 0 | 2 |
| GHOST | 37 | 3 (8%) | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| CB3 | 85 | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| TAXRES | 27 | 1 (4%) | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| H1-RES | 122 | 2 (2%) | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| **Held-out** | **804** | **84 (10%)** | **2** | **3** | **0** | **22** | **2** | **0** | **55** |
| v3 development | 893 | 122 (14%) | 0 | 6 | 1 | 41 | 4 | 0 | 70 |

**The held-out rate (10%) is at or below the development rate (14%); v3 was not tuned to its development set in
a way that shows here.** The fault mix is the same: `holds` and `absent` make up 77 of 84 (dev: 111 of 122), a
setting, name or gloss carried into an entry from a sentence it does not cite. Overstatement stays rare
(`stronger` 2, `conf` 3); no number was miscopied.

By path:
- **Critiqued notes** (categories 1 to 5): 81 of 570 (14%), the development rate exactly.
- **Uncritiqued notes** (6 to 8): 3 of 234 (1%). Fewer things can go wrong without a critique (no critic-wins rule, no
  do-not-say from a critic, fewer cross-references), but the gap is too wide for that alone, and two of these three
  are the notes whose omission check did not run (below).
- **H1-05 (25%) is the outlier.** 27 of its 35 are `holds`: settings ("Eurasian steppe", "Oregon coastal",
  "mesocosm-scale", sample counts) taken from the body's description of a study into entries citing a sentence
  that does not give them. It is also the note with the most studies described once and referred to by number
  afterwards.

**The checkers did not read `holds` the same way, and that limits these comparisons.** `checker.md` says both
"`holds`: the setting in `holds` is missing or differs from the text" and "an entry that is narrower or weaker
than its text is ok". A setting the cited text does not state narrows the claim and also differs from the text.
Most checkers faulted it. CB3's checker passed it as narrower and said so (it estimated "roughly half a dozen" CB3
faults under the other reading). From the second batch of re-checks on, I told the checker to fault it, and that checker then
faulted a `holds` the H1-RES first pass had passed (capacity-expression.11, unchanged by the fix). So the `holds`
column depends on which reading a checker takes, and CB3's 0% should be read as about 7% under the reading the
others used. This is a v4 fix to `checker.md`, not a reason to re-run.

## Omission check

| ID | Version run | Items | Accounted |
|---|---|---|---|
| H2-04 | exact (labelled sentences, answers, critique) | 239 | 239 |
| H1-05 | exact | 244 | 244 |
| H1-02 | fallback (answers and critique) | 148 | 148 |
| H1-06 | fallback | 91 | 91 |
| GHOST | fallback | 12 | 12 |
| CB3 | fallback | 17 | 17 |
| TAXRES | not run (nothing detected) | 0 | 0 |
| H1-RES | not run (nothing detected) | 0 | 0 |

Every check that ran is complete. Two of those passes, and both "not run" results, are detection failures, not
coverage:
- **H2-04: the body had no addresses.** Its title begins "Sources of…", which matched the references-section
  pattern (`REF_TITLE`), so the whole review body was treated as a reference list and given no inventory
  addresses. The 239 items are the labelled answer and critique sentences only. The builder found about 16 body
  findings it could not cite and lint gave no error, only six "source cited by no entry" warnings that point at
  the symptom. 239/239 reads as complete and is not.
- **TAXRES: answers not detected.** Its answers are under "Provisional verdicts (single-pass)", which the answers
  pattern does not recognise, so nothing was inventoried and the check did not run.
- **H1-RES: answers not detected.** It has no answers heading by design (category 8), but each sub-claim ends in
  an "Assessment" section and the note closes with a "Quantitative synthesis": answer-like text the check could
  have used. 116 claims went in with no completeness check of any kind.

## Re-checks

Every fixed entry was re-checked by a fresh agent that made none of the fixes; the loop ran until a round found
nothing.

| ID | Fixed | Round 1 still faulted | Round 2 | Round 3 |
|---|---|---|---|---|
| H2-04 | 18 | 1 of 18 | 0 of 1 | |
| H1-05 | 35 | 6 of 35 | 1 of 6 | 0 of 1 |
| H1-02 | 17 | 1 of 17 | 1 of 2 (entry split in two) | 0 of 1 |
| H1-06 | 8 (9 entries after a split) | 1 of 9 | 0 of 1 | |
| GHOST | 3 | 1 of 3 | 0 of 1 | |
| CB3 | 0 | | | |
| TAXRES | 1 | 0 of 1 | | |
| H1-RES | 2 | 2 of 2 | 0 of 2 | |
| **All** | **84** | **12 of 85 (14%)** | **2 of 13** | **0 of 2** |

Development, for comparison: 13 of 121 (11%) still faulted in round 1, and three rounds to clean. Every fault
the held-out run found is now fixed and confirmed by a fresh checker, and all eight notes lint with 0 errors.
The fixed notes are copied into `notes/`.

Round 1 here saw the most `absent` faults that were really one sentence short: the fix adds the antecedent to
`from` (H1-05 needed this for four of its six). The second and third batches of re-checks (H2-04, H1-05 and H1-02 rounds 2 and 3; H1-RES
rounds 1 and 2) ran under the stricter `holds` reading (above). Two of the second batch's four faults were in text that had been there since the build and that two earlier checkers had
passed: H1-RES capacity-expression.11's `holds` (untouched by its fix) and H1-05 annotation.2's `src` label
("FT via agents"). The other two were new words a fix had added (H1-RES redundancy.15's rewritten `holds`, H1-02
sample-dependence.12's `holds` after the split). A re-check sees the whole entry, not only the fixed part, so it
also catches faults the first pass missed.

## Builders' shortfalls (what the skill did not handle)

Reported by the builders, with no change made:

**Detection**
- **H2-04: the references pattern matched the title** (above): 0 body addresses, about 16 findings uncitable, the
  omission check passing over the gap. Lint should error when a note's body yields no addresses.
- **TAXRES, H1-RES: answers not found** ("Provisional verdicts", "Assessment"), so the omission check did not run.
- **GHOST: the Refuted section counted as a critique.** "Refuted (killed in verification)" made detect report
  `critique yes`, so the note got no "never checked by a second reader" gap, although nothing in it corrects the
  body. (The development run met the same rule conflict on TSL.)
- **H1-05: body §3.4 filed as critique**, and access-only labels were not counted as labelled.
- **H2-04: "single environment" read as a standing word** (`STAND_TOK`), and the critique's category headings
  were dropped from the inventory.
- **Sentence splitting at initials and at "Supp. Fig."**: one sentence becomes two addresses, and an entry citing
  one half loses the rest.

**Places the format has no address for**
- Reference-list annotations and the "Sources not obtained" callout get no inventory address, so findings that live
  only there cannot be cited.

**Rule conflicts**
- **Lint's year-mismatch warning** asks the builder to check a key's year against the note, which the skill forbids
  (transcribe, never look up). Every note with reused Refs.bib keys carries these warnings permanently.
- **H1-05 averaging.1:** following the critic's ruling, the builder removed the note's own `rating` ("Moderate as
  a methodological point"), against the format's rule to copy the note's grades. The grade is kept in dns.6.
- **`holds`: narrower or different** (above).

**The writer's view**
- **H1-06: "Reformulated verdict" missed.** The view looks for the critic's "Reformulated answers"; H1-06's critic
  wrote "Reformulated verdict", so the view gives the original answers without the critic's version.

**How the fixes went**
- Most `absent` faults were fixed by adding the sentence that carries the words (an antecedent of "It", what [48]
  is) to `from`. The re-checkers themselves pointed out that several first-pass `absent` faults were packet
  artefacts of this kind: the words were in the note, one sentence away.
- One fix split an entry (H1-02 sample-dependence.12 into .12 and .14), which the format allows.
- One fix went beyond the fault (H1-RES redundancy.15 also rewrote `holds`, adding words the text did not have) and
  was faulted for it on re-check.
