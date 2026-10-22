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
