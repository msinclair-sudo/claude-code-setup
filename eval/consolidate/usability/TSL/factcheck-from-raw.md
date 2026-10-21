# Fact-check: piece A against "Term specificity and multi-level labelling"

Authority: `PhD/biblion/research/knowledge/Term specificity and multi-level labelling.md` (Concepts, Do not say, Gaps). Nothing else was read.

| # | statement | verdict | entries | note |
|---|---|---|---|---|
| 1 | "Say you have sorted ten thousand abstracts into groups, and the groups nest: a broad group about soil microbes contains a narrower one about nitrogen cycling, which contains a narrower one still." | unsupported (illustration) | none | The writer's own scenario. |
| 2 | "Each group needs a label, and the labels should sit at the right height. "Microbiology" belongs near the top, "ammonia oxidation" further down." | unsupported (illustration) | none | Example. |
| 3 | "Getting this right takes two things: a number that says how specific a term is, and some evidence that sorting terms by that number puts them in the right order." | unsupported (illustration) | none | Framing. |
| 4 | "The literature on the first is old and solid." | supported | altitude-ordering.1, df-idf.1 | |
| 5 | "The literature on the second is thinner than you might expect." | supported | altitude-ordering.3, altitude-ordering.7, altitude-ordering.8 | |
| 6 | "Spärck Jones (1972) proposed weighting search terms by their document frequency, the number of documents in a collection that contain the term." | supported | df-idf.1 | The note doesn't define df. The gloss is the writer's, and it's accurate. |
| 7 | "A term that turns up in few documents is treated as more specific, so a match on it counts for more than a match on a term that turns up everywhere." | supported | df-idf.1 | |
| 8 | "This inverse relationship is the "idf" (inverse document frequency) in the familiar TF-IDF weighting." | unsupported (illustration) | none | Background. The note doesn't mention TF-IDF in general. |
| 9 | "Document frequency is a proxy, and it fails in predictable ways." | supported | df-idf.2 | |
| 10 | "A typo, an optical-character-recognition error or a sample identifier can be extremely rare without meaning anything specific." | supported | df-idf.2 | |
| 11 | "Rarity is evidence of specificity, not a definition of it." | supported | df-idf.2 | Avoids dns.1 correctly. |
| 12 | "Resnik (1995, 1999) worked from a different starting point: a taxonomy, a hierarchy in which every concept is a kind of its parent." | supported | information-content.1 | |
| 13 | "He estimated the probability P(c) of meeting a concept c in a corpus by counting occurrences of the concept and of everything beneath it." | supported | information-content.1, information-content.2 | |
| 14 | "The information content of the concept is then IC(c) = −log P(c)." | supported | information-content.1 | |
| 15 | "The root of the hierarchy covers everything, so its probability is 1 and its information content is 0." | supported | information-content.1 | |
| 16 | "Specific concepts near the leaves have low probability and high information content." | supported | information-content.1 | |
| 17 | "What makes this attractive for ordering is that a parent's count includes all its children's counts." | supported | information-content.2, altitude-ordering.2 | |
| 18 | "Probability therefore can never fall as you move up the hierarchy, and information content can never rise." | supported | information-content.2 | |
| 19 | "The ordering from general to specific is guaranteed by construction." | supported | information-content.2 | The note says "by construction" too. |
| 20 | "The cost is that you need the hierarchy first, with a single root at the top" | supported | information-content.3 | |
| 21 | "WordNet, the hierarchy of English words most of this work uses, does not have one naturally, so one has to be added." | supported | information-content.3, wordnet.bg1, altitude-ordering.8 | "So one has to be added" follows directly from information-content.3. |
| 22 | "The most direct test is by Joho and Sanderson (2007)." | supported | altitude-ordering.3 | The note calls it "the only direct empirical test" (conf: single). |
| 23 | "They took pairs of words from WordNet where one is the parent of the other and asked whether the more general word has the higher document frequency." | supported | altitude-ordering.3 | The method detail is the writer's paraphrase of "WordNet parent-child pairs". |
| 24 | "Overall it did about 74% of the time." | supported | altitude-ordering.3 | |
| 25 | "That average hides a split." | supported | altitude-ordering.3 | |
| 26 | "Among the most specific terms, in the bottom two levels of the hierarchy, accuracy was roughly 74–83%." | supported | altitude-ordering.3 | |
| 27 | "Among general terms it fell to 55–68%." | supported | altitude-ordering.3 | |
| 28 | "For a choice between two words, guessing gets half right, so at the general end document frequency is not much better than a coin." | supported | altitude-ordering.3 | The note says "near-random". The 50% baseline is the writer's reasoning. |
| 29 | "An earlier study by Caraballo and Charniak (1999) found the same pattern more sharply: about 86% correct at the lower levels and 45.5% at the upper ones." | number | altitude-ordering.4, altitude-ordering.3 | The note says "each figure belongs to its own study" (altitude-ordering.4 holds) and keeps these figures apart from Joho & Sanderson's. The piece credits both 86% and 45.5% to Caraballo & Charniak as one result. "More sharply" then ranks them against altitude-ordering.3's 74–83% / 55–68%, which is a cross-study comparison the note doesn't make. "Same pattern" (corroboration) is supported. |
| 30 | "So document frequency tells specific terms apart well and general terms apart badly." | supported | altitude-ordering.3, altitude-ordering.5 | Read in context it means WordNet pairs. The scope is restated in row 68. |
| 31 | "Yang and Callan (2009), building taxonomies automatically, reached a compatible conclusion from another direction." | supported | altitude-ordering.6 | |
| 32 | "The evidence that worked best differed by level." | supported | altitude-ordering.6 | |
| 33 | "Word co-occurrence alone served for the abstract upper levels; the concrete lower levels needed co-occurrence combined with surrounding context, lexical patterns and syntax." | supported | altitude-ordering.6 | The piece leaves out the L2–L3 / L4–L6 level labels. |
| 34 | "Their framework learns a separate scoring function for each level of abstraction rather than trusting one signal across the whole range." | supported | altitude-ordering.6 | |
| 35 | "Labelling clusters adds a step: you want the terms that characterise one group against the others." | unsupported (illustration) | none | Background. |
| 36 | "The widely used BERTopic method" | unsupported (illustration) | none | No entry says how widely BERTopic is used. |
| 37 | "BERTopic (Grootendorst, 2022) does this with a class-based TF-IDF." | supported | c-tf-idf.1 | |
| 38 | "Each cluster is treated as a single document." | supported | c-tf-idf.1 | |
| 39 | "A term's frequency within the cluster is normalised so that large clusters do not dominate, then multiplied by a factor of the form log(1 + A/f), where f is the term's total frequency summed across all clusters." | supported | c-tf-idf.1, c-tf-idf.2 | A is left undefined, as it is in the note. |
| 40 | "Terms that are frequent across the collection get pushed down." | supported | c-tf-idf.1, c-tf-idf.2 | Not the dns.6 gloss. |
| 41 | "First, f is a total count, not the number of clusters the term appears in" | supported | c-tf-idf.2 | |
| 42 | "so a term that is very frequent inside one cluster is penalised much like one spread thinly across many." | unsupported (illustration) | none | The writer's worked consequence of c-tf-idf.2. No entry says it. |
| 43 | "Second, class-based TF-IDF is an engineering application of the inverse-frequency idea." | supported | c-tf-idf.3 | |
| 44 | "Nobody has tested it as a measure of specificity in its own right." | overstated | c-tf-idf.3, c-tf-idf.4, gap.1 | The note says it is "not an independently validated (benchmarked) specificity measure". c-tf-idf.4 is class: search, holding only for "the sources the review found", and gap.1 says "apparently not done". The piece turns an absence in the reviewed sources into a universal negative ("nobody"). |
| 45 | "It is tempting to sort terms into bands such as common, middling and rare, and to assign labels by band." | unsupported (illustration) | none | Framing. |
| 46 | "The shape of word-frequency distributions makes this fragile." | supported | frequency-bucketing.1, term-frequency-distribution.1 | frequency-bucketing.1 is one simulated-LDA study. See row 52. |
| 47 | "Frequencies are heavy-tailed, with a few very common words and a long tail of rare ones, but the tail is not reliably the textbook power law." | supported | term-frequency-distribution.1 | |
| 48 | "Petersen and colleagues (2016) found a power law fit best in only 5 of 24 corpora." | supported | term-frequency-distribution.1 | |
| 49 | "The discrete Yule distribution fitted 19 of them better" | supported | term-frequency-distribution.1 | |
| 50 | "and a continuous generalised extreme value distribution fitted best overall, especially in the sparse rare-term tail where power-law and Yule fits break down." | supported | term-frequency-distribution.1 | |
| 51 | "That tail is exactly where the specific terms live." | supported | term-frequency-distribution.1 | From the holds: "the rare-term tail is the region of rare, specific terms". |
| 52 | "Fixed cutoffs behave differently from corpus to corpus." | overstated | frequency-bucketing.1, gap.2 | frequency-bucketing.1 is conf: single, class: model, and holds only for "LDA on simulated corpora; not shown on real corpora or non-LDA pipelines". The piece states it as general corpus behaviour, and the simulated-LDA scope never appears in this section. This also states gap.2 as known. |
| 53 | "Bystrov and colleagues (2023) applied the same relative document-frequency cutoff to different corpora." | number | frequency-bucketing.1 | The note gives the cutoff as "the same 1% relative cutoff". The piece drops the 1%, which defines the cutoff behind the 9.3% / 74.1% figures. It also calls it a "document-frequency" cutoff, which the note doesn't. The "corpora" were simulated. |
| 54 | "It removed 9.3% of the vocabulary from a corpus of a few long documents and 74.1% from one of many short documents" | supported | frequency-bucketing.1 | |
| 55 | "and cutoffs above 4% could empty a short-text vocabulary altogether." | supported | frequency-bucketing.1 | |
| 56 | "Logarithmic binning has been proposed as a better way to study heavy-tailed distributions (Milojević, 2010)" | supported | frequency-bucketing.4 | |
| 57 | "but it is contested even for that purpose" | supported | frequency-bucketing.4 | "Debated against MLE". |
| 58 | "and has never been tested for ordering labels." | overstated | frequency-bucketing.4, frequency-bucketing.3, gap.4 | The note says "not validated for label ordering or label banding", and frequency-bucketing.3 is class: search ("no reviewed source"). "Never been tested" is a universal claim about the literature that the note doesn't make. |
| 59 | "All the measures above give continuous scores" | supported | frequency-bucketing.2 | |
| 60 | "and the evidence favours keeping them continuous." | supported | frequency-bucketing.2 | |
| 61 | "Before scoring, most pipelines discard terms with too little support." | supported | minimum-support.1 | "Standard practice". |
| 62 | "The usual rules are to drop terms that occur only once (Blei and colleagues, 2003), to drop terms found in fewer than 0.5–1% of documents (Denny and Spirling, 2018), and to treat terms found in more than 99% of documents as corpus-specific stopwords (Grimmer and Stewart, 2013; Maier and colleagues, 2018)." | supported | minimum-support.1 | |
| 63 | "Bystrov and colleagues found that about 30% of a vocabulary could be removed without a visible loss of topic quality, whichever frequency measure was used to choose what went." | supported | minimum-support.3 | Hedged in row 65 (one study, simulated, LDA). |
| 64 | "These are conventions, not tested optima." | supported | minimum-support.2 | |
| 65 | "The pruning evidence comes mainly from one study of simulated corpora under a single topic model, latent Dirichlet allocation" | supported | minimum-support.2, minimum-support.3, gap.2 | |
| 66 | "and the stronger claim that heavy pruning is always harmless did not survive checking." | supported | dns.3, dns.4 | Reports the refutation correctly. It doesn't assert the refuted claim. |
| 67 | "No one appears to have compared collection document frequency, cluster-based frequency and information content head-to-head on the task that matters here: ordering descriptive cluster labels from general to specific." | supported | altitude-ordering.7, gap.1 | Hedged ("appears"). Doesn't count the gap as a point for any option (dns.5). |
| 68 | "Every ordering result above comes from word hierarchies such as WordNet, which is sound for those hierarchies and indirect for cluster labels." | supported | altitude-ordering.8 | |
| 69 | "Whether single words or multi-word phrases make better labels, and how stopwords and multilingual text affect the rare tail, went unaddressed in the work reviewed." | supported | phrase-and-multilingual-tail.1, gap.3 | |
| 70 | "Information content gives a guaranteed general-to-specific order when a hierarchy exists." | supported | information-content.2, altitude-ordering.2 | Holds for an is-a taxonomy with cumulative counts and a single root (information-content.3). The root condition was stated earlier, in row 20. |
| 71 | "Document frequency is a good guide among specific terms and a poor one among general terms." | supported | altitude-ordering.3, altitude-ordering.5 | WordNet scope restated in row 68. |
| 72 | "Class-based TF-IDF is reasonable engineering with no validation as a specificity measure." | supported | c-tf-idf.3 | "Reasonable" is the writer's own judgement. |
| 73 | "Continuous scores hold up better than fixed bands" | overstated | frequency-bucketing.2, frequency-bucketing.3 | The note says only that "the evidence favours continuous scoring", and that is the reviewer's synthesis (src: none). frequency-bucketing.3 says no reviewed source benchmarks discrete bands. "Hold up better" reads as a comparison that was tested. |
| 74 | "and the standard pruning thresholds are habits that have not been benchmarked." | supported | minimum-support.2 | |

Not classified, as not factual: "What can be said is modest." Section headings are also excluded.

## Do not say

No statement says what a Do not say entry warns against. Rows 11 (dns.1), 40–41 (dns.6), 66 (dns.3, dns.4) and 67 (dns.5) handle the warned-against points correctly.

## Gaps stated as known

- **gap.2**: row 52. "Fixed cutoffs behave differently from corpus to corpus" is stated generally, with no simulated-LDA scope. gap.2 asks whether the bucketing instabilities hold on real corpora and non-LDA pipelines. (For the ~30%-removable finding, row 65 does give the scope.)
- Borderline, not counted: row 58 ("never been tested for ordering labels") and row 44 ("Nobody has tested it") don't claim an answer to gap.4 or gap.1. They overstate how complete the absence is (see the overstated rows).

## Totals

| verdict | count |
|---|---|
| supported | 60 |
| overstated | 4 |
| number | 2 |
| unsupported (claim) | 0 |
| unsupported (illustration) | 8 |
| dns | 0 |
| **total** | **74** |
