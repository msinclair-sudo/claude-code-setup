# Diagnostic: facts only in the TSL raw piece

Method and classes as in `raw-only-16S.md`. This reader counted a statement as raw-only when the view piece has
the finding but drops a source the raw sentence names; both counts are given.

| Class | Count, attribution counted | Count, findings only |
|---|---|---|
| No fact | 4 | 4 |
| In both | 62 | 67 |
| A. Unused | 2 | 0 |
| B. Lost by the view | 4 | 1 |
| C. Correctly excluded | 0 | 0 |
| D. Lost by consolidation | 0 | 0 |
| E. Writer's own | 2 | 2 |
| **Total** | **74** | **74** |

| # | Raw-only fact | Class | Evidence | Fact-check |
|---|---|---|---|---|
| 22 | the most direct test is by Joho and Sanderson (2007) | B (attribution) | altitude-ordering.3, `src` johoDocumentFrequencyTerm2007; the view shows the figures with no author. View writer: "I could not confirm it and left the test unattributed." | supported |
| 35 | labelling clusters means finding terms that set one group apart | E | background framing | illustration |
| 42 | a term frequent in one cluster is penalised like one spread thinly | E | the writer's own consequence of c-tf-idf.2 | illustration |
| 51 | the rare tail is where the specific terms live | B (finding) | term-frequency-distribution.1, `holds`: "the rare-term tail is the region of rare, specific terms"; the view statement stops before it | supported |
| 53 | Bystrov and colleagues (2023) applied the same cutoff to different corpora | B (attribution) | frequency-bucketing.1, `src`; "Bystrov" appears 0 times in the view. View writer: "The study behind 9.3% vs 74.1%. Not named." | number |
| 56 | log binning credited to Milojević (2010) | A (attribution) | frequency-bucketing.4 statement | supported |
| 62 | pruning conventions cited to Blei 2003, Denny & Spirling 2018, Grimmer & Stewart 2013, Maier 2018 | A (attribution) | minimum-support.1 statement | supported |
| 63 | Bystrov and colleagues found about 30% of a vocabulary removable | B (attribution) | minimum-support.3, `src`; the view piece says "the survey that examined them" | supported |

**Reading.** Nothing was lost by consolidation and nothing was excluded. All four B rows come from fields the
view drops: three attributions held only in `src`, and one finding held only in `holds` (row 51, which is a claim
in its own right and should have been a statement). Where an author-year is part of a statement, the view keeps
it and the view writer still sometimes left it out (A). The view writer noticed both missing attributions.
