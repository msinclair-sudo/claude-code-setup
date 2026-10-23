# Stage C: state

v4 is frozen as built through stage C (plan.md revision 7): skill content as at b59851f, checker as at 7b5a0b3.
Each session reads this file first, and appends what finished and what is next.

## C0: done (2026-10-24)

- **Revision 7 and the v5 rulings** (4 to 9) are recorded in `../plan.md`.
- **`heldout/criteria.md`** was committed before the frame (a6a752b). Its seeds: draw 20261040, topics 20261041,
  letters 20261042.
- **Frame** (`heldout/frame.tsv`, from `tools/frame.py`, metadata only): 75 notes, 29 excluded.
  - 15 from v3's frame (development or read);
  - 8 v3 held-out;
  - 6 writing set-aside.

  That leaves 46 eligible notes.
- **The draw** (`heldout/draw.md`, `tools/draw.py`): one unit from each of the seven categories. Category 5 is
  dropped, with no members.

| ID | Cat. | Input (vault-relative) | Words |
|---|---|---|---|
| C-DENIT | 1 | `PhD/Proposal/Research/Results/Denitrification and N2O-reduction genes against organism phylogeny and habitat congruence, habitat association and within-genus variation (literature review).md` | 14,080 |
| C-ANALOG | 2 | `PhD/Proposal/Research/Results/Do changed conditions at a location fall within the range present elsewhere Evidence on present-day analogues for changed climate and changed soil conditions.md` | 12,664 |
| C-RANKNET | 3 | `PhD/Proposal/Research/Results/Rank-based association networks what exists, what has been benchmarked against known truth, and where the comparison has not been made.md` | 15,193 |
| C-PREDICT | 4 | `PhD/Proposal/Research/Results/Held-out prediction of taxonomic versus gene or trait community profiles from environment a literature review.md` | 12,203 |
| C-STEPDEN | 6 | `PhD/Proposal/Research/Results/Stepwise Denitrification with N2O Output in Constraint-Based Metabolic Models.md` | 3,200 |
| C-GHOSTFUS | 7 | `PhD/biblion/research/results/Featureless Ghost Nodes in Anchored Graph-Diffusion Fusion_ A Ve.md` | 3,929 |
| C-COVDIST | 8 | `PhD/Proposal/Research/Results/Quantifying Distance from Training Data to Test Points in Continuous Covariate Space.md` | 3,420 |

**Sessions, re-sized from the drawn notes.** Notes 1 to 4 are large deep runs of 12,000 to 15,000 words, about
three packets each by B6 and B7's sizes. Four in one session would be about 3M tokens, against the per-session
sizing of 1M. So the build becomes:
- **C1a:** C-DENIT and C-ANALOG, one builder;
- **C1b:** C-RANKNET and C-PREDICT, one builder;
- **C2:** C-STEPDEN, C-GHOSTFUS and C-COVDIST, one builder.

C3 to C6 are as planned. There are 15 minutes between sessions.

**Next: C1a**, after a 15-minute wait.

## C1a: started (2026-10-24, 03:03)

One builder for C-DENIT then C-ANALOG, with the B4 prompt. The notes are new, so the builder picks titles and reports the paths.

## C1a: done (2026-10-24, 04:06)

| ID | Knowledge note | Entries | First pass | `stronger` + `numbers` | Claims with a setting | Near-copies | Re-checks |
|---|---|---|---|---|---|---|---|
| C-DENIT | `PhD/Proposal/Research/Knowledge/Denitrification genes against organism phylogeny, habitat and within-genus variation.md` | 191 | 39 (20.4%, Wilson 15.3 to 26.7) | 4 | 141 of 171 (82%) | 60 (35%) | 4 of 39 still faulted, then 2 of 4, then 0 of 2 |
| C-ANALOG | `PhD/Proposal/Research/Knowledge/Present-day analogues for changed climate and changed soil conditions.md` | 128 | 12 (9.4%) | 0 | 100 of 110 (91%) | 30 (27%) | 2 of 12, then 2 of 2, then 0 of 2 |

- **Comparison:** C-DENIT's first pass is about twice stage B's pooled 9.7%; C-ANALOG's matches it. C-DENIT's faults are mostly `holds` (22) and `absent` (11).
- **Re-check, round 1:** 6 of 51 fixed entries still faulted (12%).
- **Later rounds:** in rounds 2 and 3, each fresh checker raised new points on the same few entries, not the ones already fixed.

**Builder** (one, about 520k tokens):
- **Before submitting:** its every-detail pass again *deleted* details first, then restored them with addresses, many from reference titles. It removed details of its own: a species attribution from its own knowledge, an inference about primers, and a `src` key inferred from a neighbouring sentence.
- **In the fixes:** almost all added addresses. It removed 5 details that no input sentence gives.
- **Constraint breach:** it ran `ls` on the Knowledge folder once, filtered to its own filenames. It read nothing else.

**Raised by the builder (for the owner; the skill stays frozen):**
- **A heading that carries a standing.** The critique's section heading "Single-source claims (11)" gives the standing for C-081, but headings have no address, so the checker never sees it. This is another case for v5 item 5.
- **Bracket labels without an access token** (`[Pold2024; derived; single study]`) are not detected as labels.
- **Standing words in a separate sentence** ("SINGLE SOURCE.") at the end of a paragraph.
- **The critic correcting the version read** (a preprint against the published version).
- **The critic's positive verification** of figures has no field.
- **A `src` label cannot hold brackets** (lint's key check breaks on them).
- **`class: search` needs a basis** (as in stage B).

**Next: C1b** (C-RANKNET and C-PREDICT, one builder), after a 15-minute wait.

## C1b: started (2026-10-24, 04:22)

One builder for C-RANKNET then C-PREDICT, with the same prompt as C1a.

## C1b: done (2026-10-24, 05:17)

| ID | Knowledge note | Entries | First pass | `stronger` + `numbers` | Claims with a setting | Near-copies | Re-checks |
|---|---|---|---|---|---|---|---|
| C-RANKNET | `PhD/Proposal/Research/Knowledge/Rank-based association networks against known truth.md` | 143 | 26 (18.2%, Wilson 12.7 to 25.3) | 1 | 109 of 126 (87%) | 55 (44%) | 1 of 26 still faulted, then 0 of 1 |
| C-PREDICT | `PhD/Proposal/Research/Knowledge/Held-out prediction of taxonomic versus gene or trait profiles from environment.md` | 130 | 18 (13.8%, Wilson 8.9 to 20.8) | 2 | 104 of 114 (91%) | 51 (45%) | 2 of 18, then 1 of 2, 1 of 1, 1 of 1, then 0 of 1 |

- **Re-check, round 1:** 3 of 44 fixed entries still faulted (7%).
- **averill.9 took four rounds**, and the rounds conflicted:
  - round 1 faulted an unsupported "(supplement)" label, and the builder had earlier removed "site scale" as unsupported;
  - round 2 faulted the figures for losing their definition, "site-scale out-of-sample R2";
  - round 3 faulted the dropped word "medians";
  - round 4 passed it once B-0013 and B-0034's wording were in.

  Successive single re-checkers read the same sentences differently. This is the checker noise B2 measured.

**Builder** (one, about 530k tokens):
- **Before submitting:** it again deleted settings from reference titles first, then restored them with R- addresses.
- **In the fixes:** almost all added addresses. Its removals were:
  - "Arabidopsis" for Liesecke 2018, in expression-benchmarks.8;
  - "site scale" in averill.9, restored in round 3.
- **A known unflagged error:** "Arabidopsis" also sits in `holds` of C-RANKNET expression-benchmarks.5 and .10. Neither entry was faulted, so under the procedure they were left as built.

**Raised by the builder (for the owner):**
- **A detection misfire, the mirror of H1-05:** in C-RANKNET the critic's "Verdict assessment" and "Verdict the body actually supports" sections were inventoried as answers (A-022 to A-048), duplicating C-002 to C-009. The writer's view may present the critic's assessment as the research's answers. This belongs with v5 item 8.
- **Labels on a line of their own**, as in C-PREDICT's `*Evidence class: …; Setting: …; Standing: …*` blocks, are applied to the study's claims.
- **Settings found only in reference titles** need R- addresses. The skill says reference addresses are only "for a finding that lives only there".
- **No search value for "searched, routes not named".**
- **`limit: access` where it was the critic, not the note, that lacked access.**
- **C-PREDICT was detected as author-year** although it also uses numbered markers.

**Next: C2** (C-STEPDEN, C-GHOSTFUS and C-COVDIST, one builder), after a 15-minute wait.
