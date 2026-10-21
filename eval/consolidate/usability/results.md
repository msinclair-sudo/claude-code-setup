# Usability test: results (2026-10-22)

Protocol: `protocol.md`. Six pieces, one per topic and input; every statement fact-checked against the full
knowledge note; one blind comparison per topic. Labels were drawn by seed (`ab-key.txt`): 16S A = raw, B = view;
TSL A = raw, B = view; NFERT A = view, B = raw. Each topic's folder holds both pieces, both writers' notes, both
fact-checks, the blind comparison and the writer's view the view writer was given.

## Accuracy (fact-check against the knowledge note)

| Topic | Input | Statements | Supported | Overstated | Number | Unsupported claim | Do-not-say | Gap as known | Illustration |
|---|---|---|---|---|---|---|---|---|---|
| 16S | view | 80 | 63 (79%) | 4 | 3 | 2 | 0 | 0 | 8 |
| 16S | raw | 70 | 49 (70%) | 9 | 4 | 1 | 1 | 1 | 6 |
| TSL | view | 66 | 46 (70%) | 12 | 0 | 2 | 0 | 0 | 6 |
| TSL | raw | 74 | 60 (81%) | 4 | 2 | 0 | 0 | 1 | 8 |
| NFERT | view | 68 | 60 (88%) | 3 | 0 | 1 | 0 | 0 | 4 |
| NFERT | raw | 72 | 59 (82%) | 3 | 2 | 1 | 0 | 0 | 7 |
| **All** | **view** | **214** | **169 (79%)** | **19** | **3** | **5** | **0** | **0** | 18 |
| **All** | **raw** | **216** | **168 (78%)** | **16** | **8** | **2** | **1** | **2** | 21 |

Faults (overstated, number, unsupported claim, do-not-say): view 27, raw 27. **Overall there is no difference; by
topic there is, and it goes both ways:** the view was more accurate on 16S (9 faults against 15) and NFERT (4
against 6), and less accurate on TSL (14 against 6). One checker per piece; at these counts a difference of a
few faults is within what a second checker would move.

Where each input went wrong:
- **Raw:** errors the critique corrects but the body still carries, which the writer has to find (16S: a
  do-not-say wording on pipeline agreement, two studies merged into one replicate experiment, a lost denominator
  in the controls survey); and the writer's own arithmetic (NFERT: a derived 12 t CO2e per tonne of N, compared
  with figures from another system boundary).
- **View:** scope. The view gives each claim's statement and standing, not its setting (`holds`) or that a
  "not found" was a search result (`class: search`). TSL's view writer turned "no reviewed source" into
  "untested" or "never tried" four times, and one simulated-LDA study into a general rule; NFERT's turned "one
  system reviewed by Ladha" into "a heavily fertilised legume does little fixing". Both settings are in the
  knowledge note and were dropped by the view.

## The blind readers

All three preferred the piece written from the raw notes: 16S modestly, TSL moderately, NFERT modestly. Their
reasons, consistent across topics:
- **Attribution.** Raw pieces name the study behind each result and can carry references; view pieces cannot,
  because the view removes source keys and names survive only where a claim's wording happens to include them
  (TSL: the central ordering test unattributed; NFERT: citations in one cluster, no reference list).
- **Shape.** The 16S raw piece was organised around one idea (presence errors behave differently from abundance
  errors; fixed bias spares ratios), the view piece walked the twelve steps as a list with tool names. The view
  hands the writer its concept order, and the writer followed it.
- **Process language leaking in.** The NFERT view piece talks about "the review", a question "not researched" and
  "not checked by a second reader": the view's own labels ("no critic checked it") and gap wording, carried into
  a standalone piece. (Both TSL pieces said a claim "did not survive checking": the raw note has the same.)

The readers found real errors in the raw pieces too (16S raw's confusing replicate figures, NFERT raw's derived
figure that does not reconcile), and preferred them anyway.

## What the view writers lacked (their notes)

Across the three topics, in the view writers' own words:
- **The setting of each claim** (implicit: they asked which crop, which system, which corpus; the fact-checks
  show what happened without it).
- **Who found it**: source names for attribution and a reference list (TSL, NFERT, 16S).
- **Definitions and background** the research never gives: what the 16S gene is and why it is used, what a mock
  community is, what WordNet is, metric definitions (Bray-Curtis, UniFrac), field N2O, world fertiliser tonnage.
  The raw writers asked for the same things: this is a research gap, not a view gap (and the place for the
  research-run update in section 3 of `research-run-updates.md`).
- **Brief-internal labels in the answers**: TSL's answer picks option "(a)" over "(b)" with a "(c)-flavoured
  nuance"; the options are in the brief, which the view does not include.
- **Which findings carry the weight**: the 16S view (22,000 words, 410 claims) gave no sense of which claims are
  load-bearing for a general reader; the writer had to sort them, and spent most effort cross-checking against
  the Do not say list.
- **Repetition**: the same finding as an answer, a claim and a "say instead" line, slightly differently worded.
- **Sparse standing**: most claims show no bracket because the research gave none; writers could not tell how
  firm they were.
- **Off-topic bulk**: half the 16S view (MB-02's rarity and soil sections) was outside the piece's brief.
- "Limited by access" is explained in the header and never used in TSL, which made the writer wonder what was
  missing.

The raw writers' main cost was the one the knowledge note exists to remove: 16S's raw writer cross-checked every
figure against the critique ("several figures I wanted were wrong or overstated in the body and answers, and
the fix was only in the critique"), and still let one do-not-say wording through.

## Reading of the results (not applied)

The view as specified (statement and standing only) removes too much. What it removes that writers need is not
provenance in the audit sense but two fields: the setting a claim holds for, and whose finding it is. With those
two, the view's accuracy advantage on critiqued material (16S) would likely hold and its scope losses (TSL,
NFERT) would likely close; that is a hypothesis for the next round, not a result. Process wording ("no critic
checked it", "the review") should be phrased for the writer, not copied from the audit note. No change has been
made; the six pieces are for the owner to read.
