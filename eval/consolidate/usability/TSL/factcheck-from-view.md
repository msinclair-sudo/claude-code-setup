# Fact-check: piece B against "Term specificity and multi-level labelling"

Authority: `PhD/biblion/research/knowledge/Term specificity and multi-level labelling.md`. Entry IDs abbreviated: AO = altitude-ordering, IC = information-content, TFD = term-frequency-distribution, FB = frequency-bucketing, MS = minimum-support, PMT = phrase-and-multilingual-tail.

| # | Statement | Verdict | Entries | Note |
|---|---|---|---|---|
| 1 | "Suppose you have clustered a few thousand documents and want to name each cluster." | unsupported (illustration) | none | Scenario set up by the writer. |
| 2 | "One word is rarely enough." | unsupported (illustration) | none | Writer's framing of the labelling task. |
| 3 | "A useful label runs from broad to narrow, so a reader sees first what field a cluster belongs to and then what it is actually about, the way "disease" might head a label that ends in "influenza"." | unsupported (illustration) | none | Writer's example. |
| 4 | "To build one, a method has to decide two things about every candidate term: how specific it is, and where it sits relative to the other terms." | unsupported (illustration) | none | Writer's framing. |
| 5 | "The first question has several well-tested answers." | overstated | AO.1, AO.3, c-tf-idf.3 | Only df/idf and IC are called foundational, and df's ordering ability rests on "the only direct empirical test" (AO.3, conf single); c-TF-IDF is "not an independently validated" measure. "Several well-tested" raises the standing. |
| 6 | "The second has far fewer." | supported | AO.7, AO.8 | Altitude evidence is indirect; no controlled head-to-head. |
| 7 | "The oldest and most widely used signal is document frequency: the number of documents in the whole collection that contain a term." | overstated | df-idf.1 | Note calls it "the seminal specificity signal"; "most widely used" is a claim about usage the note does not make. |
| 8 | "Spärck Jones proposed in 1972 that matches on rarer terms should count for more, because rarer terms tend to be more specific." | supported | df-idf.1 | |
| 9 | "Her inverse document frequency (idf) weight puts that into practice," | supported | df-idf.1 | |
| 10 | "and it still underlies most term-weighting schemes." | unsupported (claim) | none | No entry on idf's present-day prevalence. |
| 11 | "The rule is simple: the fewer documents a term appears in, the more specific it is taken to be." | supported | df-idf.1 | "Specificity is inversely related to df." |
| 12 | "This is a proxy with an obvious failure. A word can be rare because it is a typo, an optical-character-recognition error or an identifier code, none of which makes it specific." | supported | df-idf.2 | |
| 13 | "Frequency describes how a term is used; it does not define specificity." | supported | df-idf.2 | Matches the proxy caveat; does not say dns.1 (it says the reverse). |
| 14 | "A second signal comes from work on lexical taxonomies, chiefly WordNet, a machine-readable database of English words organised into "is-a" hierarchies (a parent concept subsumes its children)." | supported | wordnet.bg1, IC.1, IC.2, IC.3 | |
| 15 | "Resnik defined the information content of a concept as IC(c) = −log P(c), where P(c) is the probability of encountering that concept in a corpus." | supported | IC.1 | |
| 16 | "Because a parent's count includes all its children's counts, P(c) can only stay level or rise as you climb the hierarchy." | supported | IC.2 | Monotonically nondecreasing, by construction. |
| 17 | "The root has a probability of 1 and an information content of 0. General concepts have high probability and low information content; specific ones the reverse." | supported | IC.1 | |
| 18 | "That built-in monotonicity is what makes information content attractive for ordering." | supported | AO.2 | |
| 19 | "Height in the taxonomy and generality line up by construction, giving a principled scale of altitude that raw document frequency lacks." | supported | IC.2, AO.2 | |
| 20 | "The catch is that the measure needs a single root to sum into, and WordNet does not naturally have one." | supported | IC.3 | |
| 21 | "Of all the specificity signals, these two, document frequency and information content, have the strongest direct evidence behind them, and they agree with each other." | overstated | AO.1 | AO.1 says "the strongest, most direct primary evidence the review found"; the piece drops the scope of the review and states it of all signals. "Agree with each other" = "mutually consistent", fine. |
| 22 | "Methods that label clusters often move the frequency idea from documents to groups." | overstated | c-tf-idf.3 | The note has one instance (c-TF-IDF in BERTopic); "often" turns it into a pattern. |
| 23 | "The best-known current example is class-based TF-IDF (c-TF-IDF)," | unsupported (claim) | none | No entry ranks c-TF-IDF's prominence. |
| 24 | "used in the BERTopic topic-modelling tool (Grootendorst, 2022)." | supported | c-tf-idf.1 | |
| 25 | "It treats each cluster as if it were one large document, normalises term frequencies so that big clusters do not dominate, and down-weights each term with a logarithmic factor based on its frequency summed across all clusters." | supported | c-tf-idf.1, c-tf-idf.2 | |
| 26 | "That frequency is a total count of occurrences, not a count of how many clusters contain the term, a distinction the tool's own documentation blurs." | supported | c-tf-idf.2 (and dns.6 why) | Correctly avoids dns.6. |
| 27 | "c-TF-IDF is a sensible engineering application of the inverse-frequency principle." | supported | c-tf-idf.3 | |
| 28 | "Nobody has benchmarked it as a measure of specificity, though," | supported | c-tf-idf.3 | Note says "not an independently validated (benchmarked)"; "nobody" drops "independently", a minor tightening. |
| 29 | "and no study has compared it head to head with collection frequency or information content." | overstated | c-tf-idf.4 | c-tf-idf.4 is a search result (holds: the sources the review found); the piece states it as a fact about the literature, unhedged. |
| 30 | "The direct test of whether document frequency orders terms correctly used parent-child pairs from WordNet, where the right answer is known." | supported | AO.3 | "The only direct empirical test." |
| 31 | "Overall, frequency put about 74% of pairs in the right order." | supported | AO.3 | |
| 32 | "The success was not spread evenly. Near the bottom of the hierarchy, in its two most specific levels, accuracy was roughly 74–83%." | supported | AO.3 | |
| 33 | "Higher up, among general terms, it fell to about 55–68%;" | supported | AO.3 | |
| 34 | "for a choice between two terms, the lower end of that range is not far above a coin toss." | supported | AO.3 | Note: "near-random"; the piece's gloss is narrower, not wider. |
| 35 | "Caraballo and Charniak (1999) found the same shape independently: about 86% correct at lower levels and 45.5% at upper ones." | supported | AO.4 | Figures kept to their own study. |
| 36 | "Frequency, then, separates a narrow term from a slightly broader one reasonably well, and struggles to tell one broad term from another," | supported | AO.3, AO.5 | |
| 37 | "which is exactly where the top of a multi-level label gets built." | overstated | AO.3 (holds), AO.8 | AO.3 holds for WordNet parent-child pairs, "not shown for cluster labels"; the piece carries the result to label construction without a hedge (the indirectness is only acknowledged later, at #64). |
| 38 | "One response is to stop looking for a single signal. Yang and Callan (2009), building taxonomies automatically, learned a separate scoring function for each level of abstraction." | supported | AO.6 | Setting (taxonomy induction) kept. |
| 39 | "Different evidence won at different heights: co-occurrence statistics alone worked best at the abstract levels, while the concrete levels needed contextual, co-occurrence, pattern-based and syntactic features combined." | supported | AO.6 | Level numbers (L2–L3, L4–L6) omitted, not altered. |
| 40 | "Their result suggests that no one fixed measure serves every altitude." | supported | AO.6 | Hedged with "suggests". |
| 41 | "A tempting shortcut is to sort terms into frequency bands, such as common, middling and rare, and assign each band a level in the label." | unsupported (illustration) | none | Writer's set-up for the banding question. |
| 42 | "The trouble is the shape of the data. Term frequencies are heavily skewed, with a long tail of rare words that make up most of the distinct vocabulary." | supported | TFD.1, TFD.2 | |
| 43 | "They are often described as following Zipf's power law," | unsupported (illustration) | none | Background of the writer's own; the note says only "not reliably Zipfian". |
| 44 | "but Petersen and colleagues (2016) found a power law fitted best in only 5 of 24 corpora." | supported | TFD.1 | |
| 45 | "A discrete Yule distribution fitted 19 of them better, and a continuous generalised extreme value distribution did best overall, particularly in the rare-word tail." | supported | TFD.1 | |
| 46 | "Under skew like this, cutoffs behave unpredictably." | overstated | FB.1 | FB.1 is conf single, class model (one simulated-LDA study); the sentence states it as a general law before the next sentence names "one study". |
| 47 | "In one study the same relative cutoff, 1%, shrank the vocabulary by 9.3% in a collection of a few long documents and by 74.1% in one of many short documents." | supported | FB.1 | Simulated-LDA setting not given here but given at #57 and #61. |
| 48 | "Cutoffs above 4% could remove a short-text vocabulary entirely." | supported | FB.1 | |
| 49 | "Nobody appears to have tested frequency bands as a way of ordering labels." | supported | FB.3 | Hedged. |
| 50 | "Logarithmic binning has been proposed for recovering the structure of the tail, but that proposal concerns analysing distributions, remains disputed against maximum-likelihood fitting," | supported | FB.4 | |
| 51 | "and has not been tried for labels." | overstated | FB.4, gap.4 | Note says "not validated for label ordering or label banding" and leaves its value for labels open (gap.4); "not been tried" asserts an absence of attempts the note does not record. |
| 52 | "The signals with the best support, namely idf, information content and c-TF-IDF weights, are all continuous scores." | overstated | FB.2, c-tf-idf.3, AO.1 | FB.2 supports "all continuous", but putting c-TF-IDF among "the signals with the best support" raises its standing: it is "not an independently validated" measure (c-tf-idf.3) and AO.1 gives the strongest evidence to df and IC only. |
| 53 | "The evidence points towards ranking terms on a continuous scale rather than binning them." | supported | FB.2 | |
| 54 | "Almost every pipeline discards some terms before scoring:" | overstated | MS.1 | Note: "standard practice" (conventions cited at [S8]); "almost every pipeline" is a firmer, universal claim. |
| 55 | "words that occur only once, terms found in fewer than about 0.5–1% of documents, and terms found in more than 99%, which are treated as collection-specific stopwords." | supported | MS.1 | |
| 56 | "These are conventions, not tested optima." | supported | MS.2 | |
| 57 | "The survey that examined them noted that no systematic study had existed, and its own tests used only simulated corpora for one kind of topic model (latent Dirichlet allocation)." | supported | MS.2, MS.3 | |
| 58 | "In those tests about 30% of a vocabulary could go without visible loss of topic quality, whichever criterion chose what went." | supported | MS.3 | Setting kept ("in those tests"). |
| 59 | "Claims that heavier pruning is safe across the board did not survive checking." | supported | dns.3, dns.4 | Reports the refutation; does not repeat the refuted claims. |
| 60 | "Other familiar weighting signals, including BM25's saturating term-frequency curve, pointwise mutual information and measures of how "bursty" a term's occurrences are, turn up in this literature without any verified link to altitude." | supported | other-signals.1, gap.5 | |
| 61 | "Whether the pruning and banding results carry over from simulated topic models to real corpora and to tools like BERTopic is untested." | overstated | gap.2, FB.1, MS.3 | gap.2 is an open question (the primary evidence is one simulated-LDA study); "is untested" asserts that no one has tested it. Mild. |
| 62 | "So is how choosing multi-word phrases over single words, or handling stopwords and several languages, changes the specificity of rare terms." | overstated | PMT.1, gap.3 | The note says the review collected no evidence ("unanswered by this corpus"); the piece turns absence of evidence in the review into "untested". |
| 63 | "The gap that matters most for labelling is plainer still. Nobody appears to have run a controlled comparison of collection frequency, cluster-level frequency and information content as ways of ordering cluster labels from general to specific." | supported | AO.7, gap.1 | Hedged; gap.1 is "the core gap". |
| 64 | "The nearest evidence comes from WordNet and taxonomy construction, related tasks but not the same one." | supported | AO.7, AO.8 | |
| 65 | "That absence counts for none of the three signals and against none." | supported | AO.7 (dns.5 respected) | |
| 66 | "What a method has in the meantime is a principled altitude scale in information content, wherever a taxonomy exists, and a frequency signal that can be trusted at the specific end and much less at the general one." | supported | AO.2, AO.3, AO.5, AO.8 | Follows the indirectness caveat in #64. "Wherever a taxonomy exists" glosses over the unified-root caveat (IC.3), which the piece stated at #20. |

## Gaps stated as known

None is stated as answered. Three are given firmer than the note gives them, as settled absences rather than open questions (counted above as overstated): gap.2 ("is untested", #61), gap.3 ("So is", #62) and gap.4 ("has not been tried for labels", #51). gap.1 (#63) and gap.5 (#60) are reported correctly.

## Do not say

No dns entry is said. The piece explicitly avoids dns.1 (#13), dns.5 (#65) and dns.6 (#26), and reports dns.3/dns.4 as refuted (#59).

## Totals

| verdict | count |
|---|---|
| supported | 46 |
| overstated | 12 |
| number | 0 |
| unsupported (claim) | 2 |
| unsupported (illustration) | 6 |
| dns | 0 |
| **total statements** | **66** |
