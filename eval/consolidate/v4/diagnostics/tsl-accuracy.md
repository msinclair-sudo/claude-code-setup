# Diagnostic: TSL accuracy, view piece against raw piece

From the v3 usability fact-checks (`../../usability/TSL/factcheck-from-{view,raw}.md`). Analysis only.

A fault is a statement checked as overstated, number, unsupported claim or do-not-say. Claims are the
statements checked, minus illustrations (the writer's own examples and framing, which carry no claim).

| Piece | Statements | Illustrations | Claims | Faults | Faults per claim |
|---|---|---|---|---|---|
| View | 66 | 6 | 60 | 14 (12 overstated, 2 unsupported claim) | 23% |
| Raw | 74 | 8 | 66 | 6 (4 overstated, 2 number) | 9% |

## The view piece's 14 faults

| # | Statement (short) | Verdict | Cause |
|---|---|---|---|
| 5 | "The first question has several well-tested answers." | overstated | standing raised (AO.3 is conf single; c-TF-IDF not validated) |
| 7 | df is "the oldest and most widely used signal" | overstated | standing raised ("most widely used" not in the note) |
| 10 | idf "still underlies most term-weighting schemes" | unsupported claim | writer's own claim about prevalence |
| 21 | df and IC "have the strongest direct evidence" of all signals | overstated | scope dropped: AO.1 holds for what the review found |
| 22 | label methods "often" move frequency to groups | overstated | one instance (c-TF-IDF) made a pattern |
| 23 | c-TF-IDF is "the best-known current example" | unsupported claim | writer's own claim about prominence |
| 29 | "no study has compared it head to head" | overstated | absence: c-tf-idf.4 is `class: search`, stated as fact |
| 37 | "exactly where the top of a multi-level label gets built" | overstated | setting dropped: AO.3 holds for WordNet pairs, not cluster labels |
| 46 | "cutoffs behave unpredictably" under skew | overstated | setting dropped: one simulated-LDA study (FB.1 single, model) |
| 51 | "has not been tried for labels" | overstated | absence: "not validated" became "not tried" |
| 52 | idf, IC and c-TF-IDF are "the signals with the best support" | overstated | standing raised for c-TF-IDF |
| 54 | "Almost every pipeline discards some terms" | overstated | standing raised ("standard practice" made universal) |
| 61 | transfer to real corpora and BERTopic "is untested" | overstated | absence: an open gap stated as untested |
| 62 | "So is" the effect of phrases, stopwords, languages | overstated | absence: "unanswered by this corpus" stated as untested |

By cause:

| Cause | View | Raw | What the view lacked |
|---|---|---|---|
| Absence stated as fact ("untested", "not tried", "nobody") | 4 | 2 | `class: search` and the search status of each gap |
| Setting or scope dropped | 3 | 1 | `holds` |
| Standing raised or one case generalised | 5 | 1 | conf was shown; the view did not show `class` (model, single study) or the note's own scope words |
| Number (merged studies, dropped cutoff) | 0 | 2 | (raw only: figures from two studies attributed to one) |
| Writer's own claim | 2 | 0 | (not a view field) |
| **Total** | **14** | **6** | |

Seven of the view's 14 faults trace to fields the view removed: search status (4) and setting (3). Most of
the standing faults (5) trace to `class` being dropped as well: a model or single-study result read as
general. Absences went wrong in both pieces: the raw note says "no reviewed source", and the raw writer still wrote
"nobody has tested it" and "never been tested". Carrying the search status is necessary, and the writing
stage must also be held to it (rubric item 4).
