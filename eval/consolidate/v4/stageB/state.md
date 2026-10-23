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
