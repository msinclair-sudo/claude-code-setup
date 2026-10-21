# Research-run updates: proposed, not applied

Issues found downstream of the research workflow (in consolidation and writing) that a later version of the
workflow should address. Each has its evidence. Nothing here changes `workflow.md` until the owner approves it.

## 1. One note bundles things that could be processed separately

**Raised 2026-10-21**, from the 16S knowledge note (MB-01 + MB-02): 488 claims, 53 do-not-say entries, 41 gaps.
Large files are fine. Bundling separable things into one file is not, because they cannot then be processed,
checked or re-run independently.

**Where the 16S note's size comes from** (v2 note, `eval/consolidate/v2/` in the setup repo; counts by the
inventory items each entry cites):

| Source of size | Evidence | Separable? |
|---|---|---|
| Two result notes merged into one knowledge note | MB-01 gives 378 entries (326 claims, 31 do-not-say, 21 gaps), MB-02 gives 180 (138, 22, 20). Only 24 claims draw on both. | Yes. This is consolidation's choice ("one note per research set"), not the run's. |
| Several directions in one brief and one note | MB-01 has five directions (D1 and D2 share one body section): body words D1 and D2 4,294, D3 868, D4 802, D5 2,060. Of the 415 claims that cite the body, 373 (90%) cite one direction only; 43 span two or more. MB-02: D1 54 claims, D2 30, D3 29. | Mostly. |
| The critique | 14% of MB-01 (3,797 words in two callouts, 149 items), 21% of MB-02 (3,387; 145), 21% of H2-01 (2,901; 136). Every do-not-say entry and 33 of the 41 gaps rest on it, and 149 of the 488 claims cite it. | Yes: it is already two blocks of its own. |
| The answers, twice | MB-01's "Answers as delivered" callout (the workflow's per-direction answer objects) is 4,620 words, 18% of the note, beside the body's own "Answers in brief" (241 words); 313 answer sentences are inventoried and must each be accounted for. MB-02: 3,798 words, 27% of the note. | Yes: the same answers in two forms. |
| References | 30% of MB-01 (5,768 words of references, 2,028 of sources not obtained), 17% of MB-02, 30% of H2-01, 17 to 23% of the uncritiqued notes. | Yes, as a `.bib` file, at the cost of the note no longer standing alone. |
| Run record | Provenance, search record, stage-2 check: 3 to 7%. | Already optional as `run.json`. |

**Sizes of the seven development inputs** (words, and the share in body / answers / critique / references):
MB-01 26,054 (33 / 18 / 14 / 30), MB-02 15,887 (26 / 27 / 21 / 17), H2-01 13,812 (28 / 15 / 21 / 30), CB1 5,895
(66 / 11 / 0 / 17), CB2 4,197 (67 / 7 / 0 / 18), NFERT 2,333 (66 / 10 / 0 / 23), TSL 1,702 (45 / 23 / 3 / 22).

**What could be split in future runs** (for the owner to decide; not applied):
1. **The critique as its own file**, `<title>.critique.md` beside the result note and linked from it, with a
   short verdict callout left in the note. Consolidation's critic pass, the stage-2 check and a later fact-check
   all read the critique alone.
2. **One answers block, not two.** Either the per-direction answer objects or the body's answers section, not
   both in the note; the other can live in `run.json`.
3. **One result note per direction** when the directions draw on different literatures, which the triage rule
   already says should be separate briefs ("Directions that need different literatures go in separate briefs").
   MB-01's five directions shared one brief.
4. **References as a `.bib` file beside the note.** Rule 3b already makes them BibTeX, so collection works either
   way; a separate file would make collection trivial, but the note would no longer stand alone, which the
   current design requires. Listed for completeness; the trade-off is the owner's.
5. **In consolidation, not research:** one knowledge note per result note, cross-linked by concept, instead of
   one per research set. Only 5% of the 16S claims needed both inputs.

## 2. Review flags mix up access with evidence

**Raised 2026-10-21.** A negative verdict often happens because a source could not be accessed, not because its
evidence is weak. "Not confirmable, source not accessed" is a different finding from "not supported", and a
reader of a downgraded claim cannot tell which it was unless the note says.

**How it was counted.** Two fresh agents read the seven result notes of the six development sets, one the
critiques (434 items, in MB-01, MB-02, H2-01 and TSL; the other three notes had no critic), the other every
sentence outside them. Each item was classed by the reason it states (access, evidence, both, or none given),
from its own words only. Files, one row per item with the quoted words: `eval/research-run/access-2026-10-21/`
in the setup repo (`<ID>.critic.tsv`, `<ID>.flags.tsv`).

**Critic negatives** (items saying a claim, label or figure is unsupported, overstated, wrong or should be
weaker):

| Note | Negatives | Access only | Access and evidence | Evidence | No reason |
|---|---|---|---|---|---|
| MB-01 | 93 | 9 | 5 | 75 | 4 |
| MB-02 | 82 | 15 | 9 | 53 | 5 |
| H2-01 | 73 | 11 | 3 | 55 | 4 |
| TSL | 4 | 0 | 0 | 1 | 3 |
| **All** | **252** | **35 (14%)** | **17 (7%)** | **184 (73%)** | **16 (6%)** |

Coverage gaps (66) mostly give no reason at all (49); 9 give access, 6 evidence, 2 both.

**The 52 access negatives are four different things** (sorted by hand from the quoted words; judgement calls):

| Kind | MB-01 | MB-02 | H2-01 | All | Example |
|---|---|---|---|---|---|
| The claim rests on limited access (abstract only, secondary, supplement unread) | 8 | 17 | 3 | 28 | "rests on one abstract-only study" |
| The access label overstates the reading (full text claimed, not confirmable or a machine summary) | 4 | 0 | 9 | 13 | "A machine summary is not a full-text reading" |
| The access label understates it (an open copy existed, labelled abstract only) | 1 | 5 | 0 | 6 | "is open in PMC (PMC1762399 ...) but labelled AB" |
| The critic's own access failed | 1 | 2 | 2 | 5 | "PMC returned a captcha" |

Only the first kind is a claim that is limited because of access. The second and third are labelling errors,
and the fourth is a failure of the check, not of the claim; all four currently arrive in the same critique
lists, worded as negatives.

**Standing flags outside the critique** (sentences in which the review itself marks a claim weaker, unverified
or limited): 735 in all, of which 670 give an evidence reason, 28 access, 20 both, 17 none. Of the 28 access
flags, 12 are process caveats ("No claim-level verification was performed", "single-pass extraction"), not a
source left unread. What the notes do not flag matters more: about 125 citations in MB-01, MB-02 and H2-01
carry a bare abstract-only label on an unqualified claim, and 61 single-source flags sit on abstract-only
citations without saying whether the standing reflects the evidence or the access. Five of the seven notes
state an access policy (a legend or per-answer access line); TSL and NFERT state only that full text was used
"where possible".

**Answer:** access is the stated reason for about a fifth of critic negatives (52 of 252), and for about half of
those (28) the claim itself is limited by access; the rest are label errors or the critic's own failed
retrieval. Outside the critique, access is rarely the stated reason (48 of 735 flags), but it is often the
silent one.

**In consolidation now** (v3, applied): where a note or its critic says a claim is limited because of access,
the knowledge note keeps the reason in an optional `limit: access` (or `access and evidence`) field with its
basis, and in a do-not-say entry's `why`. Label errors become critic-corrected labels in `src`. Where the note
gives no reason, nothing is added. In the six v3 knowledge notes, 22 claims carry `limit` (16S 12, H2-01 5, CB1 5; none in TSL, CB2 or NFERT).

**For future runs** (proposed, not applied):
1. **Every negative names its reason.** The critique schema's items each carry `reason: access | evidence |
   both`, so "not confirmable, source not accessed" and "not supported" never share a wording.
2. **Split the critique's access list** into: claims limited by access; label errors (over- and understated);
   and the critic's own failed retrievals (route, error, date), which are not findings about the claim.
3. **A standing set only by access says so.** In rule 3a, a source read only as an abstract keeps its evidence
   standing and adds a flag (for example `unconfirmed: abstract only`), rather than leaving `single` or `unclear`
   to carry both meanings.
4. **Try the open copy before labelling abstract only** (PMC, Europe PMC, the publisher's open version), and
   record the route tried: six of the 52 were open copies the review never opened.
5. **Coverage gaps say which kind they are:** not searched, searched and not found, or found and not obtained.

## 3. The research comes back shaped like its questions

**Raised 2026-10-21** by the owner. Briefs ask specific questions, and the results come back fitted to them.
When the claims are reused in writing, they carry that shape: what was not asked is not there, even when the
literature holds it a step away. The questions should stay targeted; the run should leave room around them.

**Proposed** (not applied):
1. **A fixed share of search effort for nearby material:** the same quantity in a different setting, a related
   quantity in the same setting, and the mechanism behind it. Fixed, so that it is neither crowded out by the
   directions nor allowed to take the run over. For a deep run this could be one angle's worth; for standard
   and quick runs, a stated share of the searches.
2. **One open direction per brief:** "what does this literature treat as important that the directions above
   do not ask about?" It obeys every AGENT BRIEF constraint (no project framing, no expected answer) and goes
   through the same lint and blind preflight.
3. **A fallback order when the exact answer is not there:** the exact answer; the same measure in a different
   setting; a related measure in the same setting; the mechanism or theory; expert opinion. Each answer reports
   the closest level actually reached, instead of "not found".
4. **Distance labels on every finding.** Nearby material is only usable if it says how far it is from what was
   asked, and along which dimension: setting, organism, method, scale or measure ("measured in faeces, not
   soil"). Extend the two existing `FINDINGS_SCHEMA` fields rather than adding new ones: `nearest_precedent` and
   `bounding_or_contrary` are now true/false flags; each becomes the flag plus `distance` (the fallback level
   from item 3) and `dimension` (what differs, in words). In-text, a short flag after the rule 3a label.
5. **The critic checks for narrowness:** did the way the directions were worded exclude relevant evidence?
   Reported beside the existing `expectation_echo` check, as `narrow_framing` with the evidence it names. (The
   preflight already looks for this before the run, as `nearest_precedent_risk`; this is the same question asked
   after it, against what the search actually found.)

**What consolidation would need:** a place for the distance label (a claim field, or in `holds`), and the open
direction's findings read as ordinary claims. Nothing in the knowledge-note format changes until the research
side does.
