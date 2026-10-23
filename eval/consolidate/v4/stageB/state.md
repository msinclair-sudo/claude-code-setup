# Stage B state

Each session appends what finished, what is next, and any open item. A session starts by reading this and resumes
from the last completed batch (`../plan.md`, Running the stages).

## B0: done (2026-10-22)

**The spot-check is recorded:** `spotcheck.md`.

**v4 is built in the skill** (`skills/consolidate/`). 14 tests pass (`scripts/tests/test_kn.py`, 3 of them new).

| Change | What was built |
|---|---|
| 1 hints | `kn.hints()`, the stage A rules (R1 tokens and R2-setting words) moved into kn.py unchanged. `kn.py packets --hints` prints "Not found in the cited text (where to look, not what is wrong)" under an entry. Lint never prints hints. checker.md says how to read them; SKILL.md step 8 says the packets are made by whoever runs the check and the builder gets only verdict lines. **Parity:** on the 1,697 v3 entries the hints mark exactly the 743 that stage A's R1 or R2-setting flagged, with 0 mismatches (`tools/v3notes.py --parity`). |
| 2 view | Per claim: author and year (from the Sources block), "Holds for", the evidence in words (class, standing, the note's rating and a second reader's ruling, limited by access), search and contrary status. Answers: `[n]` markers become author and year (via the BibTeX "cited as"); a second reader's "Reformulated verdict" (unlabelled) is read; all answer, verdict and assessment sections; "(a)"-style labels; answers tied to no question are shown. Do not say as "Do not write / Why / Say instead" with full statements; gaps with their search status; a reference list. Entry IDs in builder text are replaced by the concept they belong to. Process wording is for a writer ("as corrected by a second reader", "not checked by a second reader"). |
| 2 do-not-say | format.md: the statement and `why` are full sentences (the dns.27 example). |
| 3 search status | `search:` is required on `class: search` claims and on every gap; `contrary:` is optional; the basis is a note quote, a critic item or the run record. Never inferred. |
| 4 omission | The note's title never decides a section; `REF_TITLE` is whole-heading only; answers under "Provisional verdicts", "Assessment" and "Quantitative synthesis" are found; frontmatter `answers:` declarations; `critique: refutations only`; `R-nnnn` addresses for the reference list and "Sources not obtained"; a coverage report. Lint fails on 0 body addresses, a reference list larger than the rest, a section with text but no address, an omission check that cannot run, and a missing second-reader gap. |
| 5 checker wording | checker.md: leaving out detail is ok; dropping a scope, hedge, condition, denominator or counter-clause is `stronger`; any addition is `holds` or `absent`; fields must agree. |
| 6 ratings | `rating: "…" (critic: C-nnn: ruling)`; the critic item is checked and shown to the checker. |
| 7 small | The splitter keeps initials and "Supp. Fig." together; a key-year mismatch is information, not a warning; lint warns on entry IDs in `holds`, `why`, `origin` or a src reason. |

**v4 detection on the development notes' result notes** (15 inputs):
- H2-04: 76 body addresses (v3: 0).
- H1-RES: answers found, fallback over 43 items (v3: not run).
- TAXRES: fallback over 4 (v3: not run).
- GHOST and TSL: `refutations only`.
- No input has an unaddressed section.

**Not applicable:** quoting the brief's options. TSL's "(a)" to "(c)" are the review's own; the brief has no lettered
options.

**Eval tools for B1 and B2:** `tools/kn_v3.py` (kn.py at 66d17ef, for v3 inventories) and `tools/v3notes.py` (the
v3 notes, their verdicts, the v4 hints, and packet blocks).

**Next: B1, the planted-fault test**, when the owner says go. Then stop at its checkpoint.

## B1: started (2026-10-22)

Seeds: pool 20261025, assignment 20261026, judge order 20261027. Pool: 130 claims the v3 first-pass checker
passed, 4 to 29 per note (`planted/pool.json`), committed (765fad0) before screening. The screener is running.

## B1: done, stopped at the checkpoint (2026-10-22)

`planted/results.md`.
- Screening set aside 28 of 130 v3-passed claims as faulted (24 `holds`).
- 59 plants were made; 48 passed validation (9 of 15 counter-clause plants failed).
- Two blind hint-equipped judges caught, by either: hedge 17/20 (85%), counter-clause 5/6, setting 7/7, number 7/7,
  standing 8/8. They faulted 1 of 43 controls.
- Double misses were all subtle scope qualifiers: "by this corpus", "nearest precedent", "reported as a
  distribution", and a second source's contrary argument.

Recommendation: proceed to B2 without the omission hint; the owner decides. **Next: B2** (re-score about 300 v3
entries, excluding the 130 planted-pool claims; hint effect on 100), on the owner's go.

## B1b: started (2026-10-23)

**The owner chose option 2:** add the omission hint, confirm it on a fresh planted set weighted to scope-type
omissions, with and without the hint, then freeze the checker through stage C. If the hint noticeably raises false
alarms on controls, report it, don't adopt it, and stop. Plan: `../plan.md`, stage B step 2b (revision 4).

**Built before drawing:**
- `kn.omission_hints`, `OMIT_WORDS` and `OMIT_LINE`;
- the checker.md paragraph;
- one new test (15 pass);
- `v3notes.block(..., omit=)`;
- `tools/planted2.py`.

The parity check still gives 743/743.

**Hint information, development data only** (`planted2/hint-info.md`):
- It fires on 824 of 1,516 v3 claims (54%), 2.6 items on average.
- It would have listed new items for 8 of B1's 20 hedge plants and all 6 counter plants.
- Three of B1's four double misses would be listed: "by this corpus", "nearest precedent only", and "argues the
  tail is not identifiable…". "Reported as a distribution" would not be.

`planted2/checker-N.md` is checker.md as at 7b5a0b3, for the N judges.

## B1b: done, not adopted, stopped (2026-10-23)

`planted2/results.md`.
- **The set.** 200 drawn, 176 screened clean, 56 planted, 41 validated. 86 claims judged by four fresh checkers: W1
  and W2 with the omission hint, N1 and N2 with B1's setup.
- **Omissions caught (either):** W 26 of 31 (84%), N 25 of 31 (81%). Summed over two judges, 50 against 50. The one
  W-only catch had no omission line.
- **Controls faulted (either):** W 3 of 45, N 4 of 45. A blind adjudicator read all four faulted controls as real
  faults the screener missed.
- **The pre-set rule says not adopted, stop.** It tripped on the absolute clause: W2 faulted 3 of 45, over 5%. N1
  and N2 faulted 3 each too, so the hint did not raise false alarms. It also gave no gain, so the other branch says
  not adopted as well.

**The checker is frozen through stage C at B1's setup.** That is `checker.md`, `hints()` and `packets --hints`, with
content identical to 7b5a0b3. The skill files were restored from 7b5a0b3 (14 tests pass), and the tested hint code is
in `tools/omission_hint.py` (v3notes and planted2 import it from there). Parity is still 743/743, and the moved code
regenerates the committed packets and hint information unchanged.

**Next: B2**, on the owner's go. Its sample excludes both planted pools (B1 130, B1b 200).

## B2: started (2026-10-23)

The owner agreed: not adopted, checker frozen through stage C; go ahead with B2. Three v5 items are recorded in
`../plan.md` ("For v5"). Tool: `tools/baseline.py`.

**The sample** (`baseline/sample.json`, committed before checking). 300 entries, between 12 and 56 per note. Seeds:
draw 20261032, order 20261033, hint subset 20261034 and 20261035, adjudication 20261036, bootstrap 20261037.
- Each note is split into its v3-passed claims and the rest. Each stratum is drawn from its entries outside the two
  planted pools, then weighted back to its full size.
- That gives 230 v3-passed claims and 70 from the rest, and 141 of the 300 carry a hint line.
- The work is five packets of 60, checked by five fresh checkers using the frozen checker.md.

## B2: done (2026-10-23), stopped for the owner

**Baseline** (`baseline/results.md`). One checker per entry. Checker 2 skipped two entries; it judged them on
request, both `ok`.
- **Re-scored v3 first-pass fault rate: 35.9%** (bootstrap 95% 30.8% to 41.2%), a whole-note estimate weighted by
  stratum. The unweighted sample rate is 108 of 300 (36.0%). v3 as reported was 12.1%.
- **Per 100 entries:**
  - `holds` plus `absent`: 33.6 (28.7 to 38.7);
  - `stronger` plus `numbers`: 1.4 (0.2 to 3.0; 4 `stronger`, 0 `numbers`, all listed);
  - `conf`: 0.4.
- **The faults are almost all additions:** `holds` 79, `absent` 23. 65 of 230 v3-passed claims are faulted now, and
  40 of the 44 v3-faulted entries are faulted again.
- **By note:** from 15% (GHOST, NFERT) to 58% (TAXRES). The intervals are wide, with 12 to 56 entries per note.

**Hint effect** (`hints/results.md`). 100 entries, 60 hinted and 40 not. W1 is the baseline checkers; W2 is fresh
with hints; N1 and N2 are fresh without.
- **Faults found:** W1 45, W2 23, N1 36, N2 25. On the 40 unhinted entries, every run faulted 2 to 6.
- **Agreement (ok against fault):** within condition, 78 (W) and 81 (N); across conditions, 78 to 89. The hints do
  not separate the conditions beyond checker-to-checker noise.
- **The 30 discordant entries**, read by a blind adjudicator, who found faults in 26:
  - real faults passed: W runs 22, N runs 25;
  - faults the adjudicator did not see: W runs 4, N runs 0. All 4 came from W1.

  So the hints trade about 3 more catches for up to 4 false faults.

**The open item, for the owner before B3.** On the same 100 entries, single checkers in the frozen setup faulted
between 23 and 45. Two checkers in the same condition disagree on about one entry in five. Gate B compares one
checker per entry on v4 against one checker per entry on v3. A difference of 10 points can therefore come from which
checkers ran rather than from v4.
- The baseline checkers (60-entry packets) were the strictest run.
- The v4 first-pass checkers are planned at about 100 to 120 entries each.

Options:
- match packet sizes;
- two checkers per entry on both sides (v5 item 2 as an evaluation design, not a checker change);
- accept the noise and read the gate's intervals.

**Next: B3**, on the owner's go.

## B2: completed under revision 5 (2026-10-23)

**The owner's decisions** (`../plan.md`, revision 5):
- two checkers per entry on both sides, a fault from either counted;
- 60-entry packets, now part of the frozen procedure;
- the baseline re-checked to match;
- one builder rule before the rebuild.

**What v4 had for `holds` and `absent` faults on the builder side: nothing new.**
- The only rule was format.md's sentence from v3 (4f28b9c): "The same goes for `holds`: the setting comes from the
  cited sentences, or the sentence it comes from is cited." It covers `holds` only, and the v3 notes were built
  under it.
- The provenance lint was dropped at stage A, and the hints reach only the checker.

**What was added:**
- A SKILL.md hard rule, "Every detail comes from `from`": every setting, name or detail in an entry, in its
  statement, `holds` or any other field, comes from a sentence listed in its `from`. If it comes from elsewhere in
  the note, that sentence's address is added.
- format.md's sentence widened to match.

checker.md and kn.py are unchanged since 7b5a0b3, and the 14 tests pass.

**Baseline, two checkers per 60-entry packet** (`baseline/results.md`). The second checker set is in
`baseline/second/`.
- **First-pass fault rate: 38.6%** (bootstrap 95% 33.4% to 43.9%); in the sample, 118 of 300. Each set alone: 35.9%
  and 35.6%.
- **The two checkers agree on 282 of 300 entries** (94%; 56 to 60 per packet). On the same packets, single-checker
  noise is much smaller than the hint runs suggested.
- **Per 100 entries:**
  - `holds` plus `absent`: 36.1 (31.1 to 41.3);
  - `stronger` plus `numbers`: 1.9 (0.5 to 3.6; 4 `stronger` and 2 `numbers` entries, all listed);
  - `conf`: 0.4;
  - `critic`: 1.0.

**Next: B3** (16S, MB-01 plus MB-02). The vault's 16S knowledge note equals `../v3/notes/` (the fixed v3 version),
so the rebuild may overwrite it.

## B3: done (2026-10-23), 16S

This followed the 15-minute wait after B2. Files are in `rebuild/16S/`:
- `as-built.md`, the first-pass state;
- `final.md`, the clean note, also in the vault;
- `packets/` and `verdicts-a/`, `verdicts-b/`;
- `first-pass.md`;
- `fixes-1..3.md` and `recheck-1..3/`.

The tool is `tools/rebuild.py`.

**The build.** One fresh builder (about 720k tokens) lint-clean at the first try, with MB-01 605/605 and MB-02
298/298 accounted for. The note has:
- 40 concepts, 505 claims and 55 do-not-say entries;
- 32 gaps;
- 256 sources.

On its own initiative, the builder checked that each word was in its `from` sentences, using a script of its own,
not the hints. It removed about 70 added settings before submitting. That is the new hard rule at work.

**First pass**, two checkers per 60-entry packet, 10 packets and 20 checkers (`rebuild/16S/first-pass.md`):
- **68 of 560 faulted (12.1%, Wilson 9.7% to 15.1%)**;
- per 100 entries: `holds` plus `absent` 9.5, `stronger` plus `numbers` 1.8 (10 `stronger`, all listed), `conf` 0.5;
- checker A 52, checker B 63, both 47; they agree on 539 of 560.

For comparison, only, since gate B is judged on all 14 notes in B8: the 16S stratum of the re-scored v3 baseline
was 35% with one checker.

**Fixes and re-checks.** The builder fixed all 68.
- **Round 1:** 2 of 68 still faulted (3%), both `absent`.
- **Round 2:** 1 of 2 (extraction.8, a dropped "for relative abundance").
- **Round 3:** clean.

**Open item for the owner (the checker is frozen, so it is recorded, not changed).** format.md and checker.md
conflict:
- format.md: "Where the critic corrects the claim and not the source's label, the label stays and conf carries the
  correction";
- checker.md: "a label in `src` that contradicts `conf` is `conf`".

The builder followed format.md, and chimeras.1 and copy-number.26 drew `conf` faults. It then changed `src` to the
critic-corrected form.

**Next: B4** (H2-01 plus TSL; CB1 plus CB2), after a 15-minute wait, on the owner's go.

## Owner's rulings after B3 (2026-10-23): plan revision 6

- **`src` against `conf`.** format.md now says `src` shows the critic's standing, marked, with the review's label
  as `was "..."` (the form lint already checks). The checker is unchanged. 16S was built before this and is not
  rebuilt.
- **Builder rule.** Add the sentence's address; never delete the detail. This is in SKILL.md and format.md.
- **B8 information:**
  - settings kept;
  - the 16S removals;
  - near-copies;
  - `stronger` and `numbers` per note.

  The tool is `tools/notestats.py`, with definitions in its docstring.
- **Early stops,** checked after each note's first pass:
  - a note above its v3 estimate;
  - pooled `stronger` plus `numbers` above 3.6 per 100;
  - a note's setting share below 0.75 of its v3 share.

**16S under the new measures (information):**
- **Claims with a real setting:** v3 341 of 410 (83%); v4 411 of 505 (81%); ratio 0.98.
- **Near-copies:** v3 148 (36%); v4 205 (41%).
- **The builder's list of its pre-submission removals** (`rebuild/16S/removed-settings.md`, from its edit scripts):
  76 removals in 72 entries, all dropped, none kept with an added address. That came before the clarification.
  - By the builder's own account, 42 of the removed details are stated elsewhere in the inputs, 6 partly, 8 not at
    all, and 20 unchecked.
  - Its 16 other fixes added an address.

**B4 inputs checked:** the vault's H2-01, TSL, CB1 and CB2 knowledge notes equal `../v3/notes/`, so they may be
overwritten.

## B4: started (2026-10-23)

This follows a 15-minute wait after B3 and the rulings. There are two builders: H2-01 plus TSL, and CB1 plus CB2.

## B4: done (2026-10-23)

First passes use two checkers per 60-entry packet (`rebuild/<NOTE>/first-pass.md`). Each "v3 estimate" is the
re-scored baseline for that note.

| Note | Entries | First pass | v3 estimate | `stronger` + `numbers` | Settings v4/v3 | Near-copies v3, v4 | Re-checks |
|---|---|---|---|---|---|---|---|
| H2-01 | 143 | 10 (7.0%) | 61% | 1 | 0.91 (90% to 82%) | 51%, 44% | 0 of 10 still faulted |
| TSL | 31 | 6 (19.4%) | 36% | 3 | 0.87 (97% to 84%) | 45%, 24% | 0 of 6 |
| CB1 | 145 | 4 (2.8%) | 18% | 1 | 1.00 (93% to 93%) | 59%, 59% | 0 of 4 |
| CB2 | 81 | 2 (2.5%) | 32% | 1 | 1.09 (84% to 92%) | 61%, 48% | 0 of 2 |

**Stop checks: none met.**
- Every note is below its v3 estimate.
- Pooled `stronger` plus `numbers`, over 16S and B4, is 16 in 960 entries: 1.7 per 100, against the 3.6 threshold.
- Every setting ratio is at least 0.87.

**Builders:**
- **H2-01 and TSL** (about 380k tokens): deleted details at first, then reread the rule and restored them with
  addresses (about 30).
- **CB1 and CB2** (about 380k tokens): CB1 kept details with addresses. In CB2 it removed eight details while
  rewording, before submitting ("tropical", "activated sludge", "METASEED" and others). All fixes added addresses
  and removed nothing.

The H2-01 builder reports that lint's match for "the only direct empirical test" is narrow (a warning left on TSL).
Both builders found the `class: search` basis duplicating `search`.

**Next: B5** (NFERT plus CB3; GHOST plus TAXRES plus H1-RES), after a 15-minute wait. All nine remaining vault
notes equal their saved v3 copies.

## B5: started (2026-10-23, 20:25)

Resumed after the owner's pause until 8:11 pm. There are two builders: NFERT plus CB3, and GHOST plus TAXRES plus H1-RES. Prompts are as in B4.

## B5: done (2026-10-23, 21:36)

First passes use two checkers per 60-entry packet (`rebuild/<NOTE>/first-pass.md`). Each "v3 estimate" is the
re-scored baseline for that note.

| Note | Entries | First pass | v3 estimate | `stronger` + `numbers` | Settings v4/v3 | Near-copies v3, v4 | Re-checks |
|---|---|---|---|---|---|---|---|
| NFERT | 54 | 1 (1.9%) | 20% | 0 | 1.00 (88% to 88%) | 63%, 58% | 0 of 1 still faulted |
| CB3 | 92 | 11 (12.0%) | 55% | 3 | 0.96 (97% to 94%) | 56%, 48% | 0 of 11 |
| GHOST | 46 | 2 (4.3%) | 23% | 0 | 0.98 (87% to 85%) | 39%, 39% | 0 of 2 |
| TAXRES | 30 | 6 (20.0%) | 66% | 1 | 1.10 (85% to 93%) | 50%, 61% | 0 of 6 |
| H1-RES | 177 | 7 (4.0%) | 18% | 1 | 0.94 (83% to 78%) | 53%, 63% | 0 of 7 |

**Stop checks: none met.**
- Every note is below its v3 estimate.
- Pooled `stronger` plus `numbers` over 16S, B4 and B5 is 21 in 1,359 entries: 1.5 per 100, against the 3.6 threshold.
- Every setting ratio is at least 0.94.

**The five `stronger` and `numbers` faults:**

| Note | Entry | Fault |
|---|---|---|
| CB3 | soil-n2o.4 | dropped IPCC's "medium confidence" |
| CB3 | dns.1, dns.2 | dropped "exactly" from "produces exactly five per cent" (the builder had flagged this wording as borderline) |
| TAXRES | fungal-repositories.1 | Index Fungorum's 114,301 names lost the "entering the backbone" context |
| H1-RES | n-cycle-vertical.4 | "suggested" became "found" |

**Builders:**
- **NFERT and CB3** (about 310k tokens).
  - **Before submitting:** it removed eight pieces of its own wording that no sentence in the entry's `from` gave. Examples: "AR6 WGIII Summary for Policymakers" from a `holds`, "Tubiello et al. 2022, Table 1", and "2013" from a `why`. Its other checks added addresses.
  - **In the fixes:** six added an address, and three restored a hedge or counter-clause. Four removed `limit: access` (below). One deleted an inferred `src` label, "(via Gerber et al. 2013's Annex)".
- **GHOST, TAXRES and H1-RES** (about 320k tokens).
  - **Before submitting:** it removed only wording it had added (for example a computed "340 genomes", restored to "88 newly sequenced and 252 public"), never a detail from the input.
  - **In the fixes:** about ten added an address, and one restored a hedge. Four removed a detail no addressable sentence gives. Two of those were "sub-claim 1" and "sub-claim 3", which only headings give. The other two were the label "neighbour feature propagation" for option (a), and "denitrifier".

**Open items for the owner** (the checker stays frozen; nothing changed):
- **`limit: access`: format.md and checker.md disagree.** format.md lists "a figure not confirmable from the text read" as an access reason, and checker.md does not. CB3's "I read these shares off the rendered figure, not the text" was faulted on four entries under checker.md's list, and the builder removed the limits.
- **Headings have no address.** A setting that only a heading gives ("the sub-claim 1 evidence") cannot be cited under "every detail comes from `from`", so it has to be dropped. The H1-RES builder counted a few more unflagged entries of this kind.
- **Both builders raised:**
  - access values with no match (for example a reference in neither access list);
  - citekeys for works with no title or year;
  - no field for the note's own search routes, or for who produced a finding;
  - H1-RES has citations with no reference list (`src: none (...)`).

**Next: B6** (H2-04 plus H1-05), after a 15-minute wait.

## B6: started (2026-10-23, 21:53)

This follows a 15-minute wait after B5. One builder builds H2-04 and then H1-05, with prompts as in B4.

## B6: done (2026-10-23, 22:47)

| Note | Entries | First pass | v3 estimate | `stronger` + `numbers` | Settings v4/v3 | Near-copies v3, v4 | Re-checks |
|---|---|---|---|---|---|---|---|
| H2-04 | 142 | 21 (14.8%) | 27% | 0 | 1.00 (88% to 88%) | 39%, 45% | 1 of 21 still faulted, then 0 of 1 |
| H1-05 | 119 | 17 (14.3%) | 52% | 3 | 0.99 (96% to 95%) | 20%, 19% | 2 of 17, then 0 of 2 |

**Stop checks: none met.**
- Both notes are below their v3 estimates.
- Pooled `stronger` plus `numbers` over 16S and B4 to B6 is 24 in 1,620 entries: 1.5 per 100.
- Both setting ratios are at least 0.99.

**H1-05's `stronger` and `numbers` faults:**
- other-habitats.11 dropped "mostly".
- unit-annotation-metric.16 turned "I found no study" into "no study".
- other-habitats.8 (`numbers`) was disputed by the builder. "About 31 of 148 reversed" and the critic's "13 deviating" are different counts, so the builder made the difference explicit in `holds`, and the re-check passed it.

**Builder** (one, about 470k tokens):
- **Before submitting:** its first every-detail pass *deleted* details that came from reference titles, against the rule. It then restored them all with addresses: 19 edits in H2-04 and 39 in H1-05.
- **In the fixes:** most added addresses, and two restored hedges.
- **Removals:** four details that no input sentence gives:
  - "a review", which became "a theoretical or review paper";
  - a critic clause that C-113 does not cover;
  - "plant", from "plant trait ecology";
  - "16S", from a GeoChip contrast.
- **Round 2:** H2-04 dns.16 had quoted "independent" where the text says "near-independent". The builder corrected the quote and added two addresses.

**Open items raised (for the owner; nothing changed):**
- **A detection misfire.** H1-05 §3.4's heading "Functional redundancy as an explanation: for, against, critiques" matches the critic-title pattern. The reviewer's own text was therefore inventoried as critique items C-112 to C-128. The builder did not use them as `critic:` bases. Lint can't tell, so a `critic: C-120` basis would pass as a second reader's finding.
- **Format gaps:**
  - `class: search` needs a basis, which lint enforces and format.md doesn't show (raised in B4 and B5 too);
  - a "*Conflicts:*" label heads only the first sentence of a block;
  - critic verdict headers ("Supported.") have no field;
  - positive second-reader verification ("figures checked against full text by the critic") has no field;
  - source dependence (shared data or authors) has no field.

**Next: B7** (H1-02 plus H1-06, one builder), after a 15-minute wait.

## B7: started (2026-10-23, 23:03)

This follows a 15-minute wait after B6. One builder builds H1-02 and then H1-06, with prompts as in B4.

## B7: done (2026-10-23, 23:49)

| Note | Entries | First pass | v3 estimate | `stronger` + `numbers` | Settings v4/v3 | Near-copies v3, v4 | Re-checks |
|---|---|---|---|---|---|---|---|
| H1-02 | 124 | 14 (11.3%) | 52% | 0 | 1.09 (90% to 98%) | 54%, 44% | 0 of 14 still faulted |
| H1-06 | 103 | 10 (9.7%) | 38% | 2 | 1.07 (89% to 95%) | 48%, 50% | 2 of 10, then 1 of 2, then 0 of 1 |

**Stop checks: none met.**
- Both notes are below their v3 estimates.
- Pooled `stronger` plus `numbers` over all 14 notes is 26 in 1,847 entries: 1.4 per 100.
- Both setting ratios are above 1.

**H1-06's `stronger` and `numbers` faults:**
- perturbation-response-depth.9 (`numbers`) pooled two studies' tau_D ranges and extended them to a litter study that gives none.
- env-preference-depth.2 (`stronger`, `absent`) dropped the critic's "or a preprint" clause.

**Builder** (one, about 435k tokens):
- **Before submitting:** it removed only wording it had added ("simulated data", "before MAG yield rose", "natural" and "in simulation"). In H1-06 it first deleted setting words, then restored them all with reference-title addresses.
- **In H1-02 it replaced author names in `holds` with descriptions** of the sources (for example "same-sample isolate pairs") instead of adding the reference addresses. It reasoned that the writer's view shows authors from `src`. Names are details under the rule, so this is a removal, recorded here.
- **In the fixes:** almost all added addresses. Two detail removals: "than real pairs" (its own comparison), and "ASVs against 97% OTUs only" (the note's wording, which the critic corrects; the statement keeps the corrected contrast).
- **Re-check rounds 2 and 3, H1-06:**
  - genome-incompleteness.6 restored a "modelled" scope.
  - rankwise-structuring.9 first narrowed "uncontrolled for group number and size" to the note's words. In round 3 it gained A-021's address, the sentence that names Bay among the uncontrolled studies.

**Raised by the builder (for the owner):**
- Class markers at the end of a paragraph ("(measured; natural)") were used as the basis for the study's earlier sentences.
- "inferred" has no class value, so `deriv` was used.
- The note calls mock-community subsampling "modelled", while format.md says mock communities are `meas`; the builder kept `model`.
- The critic contradicting the note on provenance has no rule.
- The critic's "Expectation echo" block and positive rulings have no field.

**Next: B8**, after a 15-minute wait.

## B8: started (2026-10-24, 00:05)

This follows a 15-minute wait after B7. Steps: do-not-say readability with one reader (`tools/dns.py`), then `tools/results.py`, which writes `results.md`.

## B8: done (2026-10-24). Gate B: all five criteria met; stopped for the owner

The full report is `results.md`, from `tools/results.py`. Its ratio bootstrap seed, 20261038, was fixed before scoring, in c69db8a.

| Criterion | v4 (14 notes, 1,847 entries) | Re-scored v3 | v4/v3 (95%) | Threshold | Met |
|---|---|---|---|---|---|
| 1. First-pass fault rate | 9.7% (Wilson 8.4 to 11.1) | 38.6% (33.4 to 43.9) | 0.25 (0.17 to 0.32) | at most 2/3 | yes |
| 2. `holds` + `absent` per 100 | 7.9 | 36.1 | 0.22 (0.14 to 0.29) | at most 1/2 | yes |
| 3. `stronger` + `numbers` per 100 | 1.4 | 1.9 | 0.75 (0.31 to 2.67) | not above v3 | yes |
| 3. `conf` per 100 | 0.3 | 0.4 | 0.82 (0.00 to unbounded) | not above v3 | yes |
| 4. Omission | all 15 inputs run it (5 exact, 10 fallback); every input has body addresses; no unaddressed section outside the allow-list | | | | yes |
| 5. Re-check, round 1 | 7 of 179 fixed entries still faulted, 3.9% | v3: 11%, 14% | | at most 15% | yes |

- **Criterion 3 is met on the point estimate only.** Both ratio intervals reach well above 1, so the data cannot distinguish v4 from v3 on `stronger` plus `numbers` or on `conf`.
- **Every note is below its v3 estimate.**
- **Settings:** every setting ratio is at least 0.87; the lowest are TSL 0.87 and H2-01 0.91.
- **Near-copies** fell in 8 notes, rose in 5 and were flat in 1. The largest rises are H1-RES (53% to 63%) and TAXRES (50% to 61%).
- **Do-not-say readability** (information, one reader): 184 of 199 usable (92.5%), against the 90% target.
  - The reader marked 14 more entries usable as borderline. A strict reading would make them fragments, giving 170 of 199 (85.4%).
  - The fragments are mostly a missing "Say instead" (4), or a "Do not write" about the review's own process (6).

**Open items for the owner**, collected from B4 to B7:
1. **`limit: access`: format.md and checker.md disagree** on "a figure not confirmable from the text read" (B5, CB3).
2. **Headings have no address**, so a setting only a heading gives cannot be cited (B5, H1-RES).
3. **A detection misfire:** a body heading containing "critiques" is inventoried as critique items, and a `critic:` basis on them would pass lint (B6, H1-05 C-112 to C-128).
4. **`class: search` needs a basis**, which lint enforces but format.md doesn't show (raised in B4 to B6). Lint's match for "the only direct empirical test" is narrow (B4).
5. **Fields the format lacks:**
   - a positive second-reader ruling or verification;
   - the critic's verdict headers;
   - source dependence;
   - who produced a finding;
   - search routes for a whole review;
   - the critic's "Expectation echo" block.
6. **Calls with no rule:**
   - a class marker at the end of a paragraph;
   - "inferred" with no class value;
   - mock communities called "modelled";
   - the critic contradicting the note on provenance;
   - access values with no match;
   - citekeys for works with no title or year.
7. **Builders sometimes deleted details on their first self-check** and then restored them with addresses (B4, B6, B7). In H1-02, author names in `holds` were replaced by descriptions, not given addresses.
8. **Do-not-say entries:** a missing "Say instead" and process-level "Do not write" sentences account for 10 of the 15 fragments.

The checker is frozen at 7b5a0b3, and `kn.py`, `checker.md` and the tests are unchanged since then. All 14 tests pass. **Stage C does not start without the owner's go.**
