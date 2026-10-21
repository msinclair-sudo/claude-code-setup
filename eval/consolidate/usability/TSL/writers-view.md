# Term specificity and multi-level labelling: writer's view

> [!abstract] About this view
> What the research found, for writing from. It is generated from the knowledge note `Term specificity and multi-level labelling.md`, which stays the audit version: every claim here is checked there against the research, with its setting, sources and trail. Standing is given in brackets where the research stated one (`repl` replicated, `single` one source, `cont` contested, `unclear`, `mixed` the inputs differ); a claim with no bracket has no standing stated. "Limited by access" means the research says a source was not read in full, not that the evidence is weak.

## What the research found, by question

### TSL

**D1. Across methods that assign descriptive terms to groups of documents (TF-IDF and its class or group based variants, topic model labelling, graph based keyphrase extraction, hierarchical or taxonomic labelling, and faceted or multi granular tagging), what signals quantify how general or specific a candidate term is, and how do multi level labelling methods produce a sequence of terms running from general to specific? Specifically: which document frequency or information theoretic signals (collection document frequency and inverse document frequency, group or class based document frequency, pointwise mutual information, information content as negative log probability, BM25 style saturation, burstiness or concentration measures) are standard; how do heavy tailed (Zipfian) document frequency distributions affect threshold or quantile based bucketing of terms by frequency; what minimum document frequency or support thresholds are conventional and what is their measured effect; and how do hierarchical labelling systems decide a term's altitude (collection frequency, depth in an induced hierarchy, or information content)?**

*Answer to D1, as the review gave it; the critic did not reformulate it.*

**(a) Collection document frequency / information content — with a sharp qualification, and a (c)-flavoured nuance for cluster labelling.** The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality. IC is the cleaner *altitude* axis of the two because of that monotonicity. The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms**. Independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels. So df is a good *specificity* signal but a weak *altitude discriminator* across the full range. One taxonomy-induction framework abandons a single fixed altitude signal entirely, learning a separate information function per abstraction level. Class/group-based df (**c-TF-IDF**, BERTopic) operationalises the same inverse-frequency principle at the cluster level, but it is an **engineering instantiation, not an independently validated specificity measure**. So the answer is **not (b) group-df alone** — group df has no head-to-head support against collection df or IC. **Continuous vs discrete:** the evidence favours **continuous scoring** (idf, IC, c-TF-IDF weights are all continuous). **Discrete frequency banding is shown to be unstable under heavy tails** — the same relative cutoff produced 9.3% vs 74.1% vocabulary reduction across corpora, and cutoffs >4% can empty a short-text vocabulary. No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis, not validated for label banding. **Minimum-support thresholds:** **yes, standard practice** — drop frequency-1 terms; discard terms in <0.5–1% of documents; strip terms in >99% as corpus stopwords — but documented as **conventions, not benchmarked optima** (the primary survey notes "no systematic study" existed and tests only simulated LDA corpora). **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific. The closest tests are over WordNet / taxonomy induction — indirect for the label-ordering task. Report this as "no controlled evidence found," not as a point for any option. This is exactly the band-collapse question the brief's routing flagged as likely under-benchmarked.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### WordNet

- WordNet is an online lexical database for English, designed for use under program control. *(background, not from the research)*

### collection document frequency (df / idf) as a specificity signal

- Collection df / idf is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more; specificity is inversely related to df (lower df = more specific).
- df is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity.

### information content, IC(c) = −log P(c)

Builds on: WordNet.

- Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999): general concepts have high P and low IC (root P = 1, IC = 0); specific concepts have low P and high IC.
- P(c) is monotonically nondecreasing up the taxonomy, by construction (a parent cumulatively subsumes its children's counts), so corpus probability is monotonic up the hierarchy and altitude maps directly onto generality.
- IC needs a unified root; WordNet has none naturally.

### class-based df (c-TF-IDF, BERTopic)

Builds on: collection document frequency (df / idf) as a specificity signal, information content, IC(c) = −log P(c).

- c-TF-IDF (BERTopic, Grootendorst 2022) treats each cluster as one document, L1-normalises tf for cluster size, and down-weights via log(1 + A/f_t).
- In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term.
- Class/group-based df (c-TF-IDF) operationalises the same inverse-frequency principle at the cluster level, but it is an engineering instantiation, not an independently validated (benchmarked) specificity measure.
- Group df has no head-to-head support against collection df or IC.

### ordering terms general→specific (altitude)

Builds on: collection document frequency (df / idf) as a specificity signal, information content, IC(c) = −log P(c), class-based df (c-TF-IDF, BERTopic), WordNet.

- Collection df / idf and information content are two foundational, mutually consistent specificity signals, established by the strongest, most direct primary evidence the review found.
- IC (corpus probability) is the cleaner, principled altitude axis of the two, because of its monotonicity up the hierarchy.
- Collection df reliably orders terms by specificity only at the specific end: ~74% accuracy overall on WordNet parent-child pairs, ~74–83% at the bottom two WordNet levels, degrading to ~55–68%, near-random, for general terms. *(single)*
- The same pattern is independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels. *(repl)*
- df is a good specificity signal but a weak altitude discriminator across the full range.
- One taxonomy-induction framework (Yang & Callan 2009) abandons a single fixed altitude signal and learns a separate information function per abstraction level: different feature sets win at different levels (co-occurrence alone for abstract L2–L3; contextual + co-occurrence + pattern + syntactic for concrete L4–L6), so no single fixed signal serves all altitudes.
- No controlled head-to-head exists comparing collection df vs class df vs IC for ordering descriptive cluster labels general→specific; the closest tests (Joho & Sanderson; Yang & Callan) are over WordNet / taxonomy induction, indirect for the label-ordering task.
- The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet / taxonomies: sound for those, indirect for descriptive cluster-label ordering; the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.

### BM25 saturation, PMI and burstiness

Builds on: ordering terms general→specific (altitude).

- BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering: known weighting signals, not validated specificity-altitude axes here.

### heavy-tailed term-frequency distributions

- Term-frequency distributions are heavy-tailed but not reliably Zipfian: Petersen et al. (2016) found power-law best for only 5/24 corpora, 19/24 better fit by discrete Yule, and continuous GEV best overall, especially in the sparse rare-term tail where Yule and power-law fail.
- Low-frequency words are the majority of unique types.

### discrete frequency banding and continuous scoring

Builds on: heavy-tailed term-frequency distributions, collection document frequency (df / idf) as a specificity signal, information content, IC(c) = −log P(c), class-based df (c-TF-IDF, BERTopic), ordering terms general→specific (altitude).

- Threshold bucketing is corpus-structure-dependent and unstable under heavy tails: the same 1% relative cutoff produced a 9.3% vocabulary reduction (few long documents) vs 74.1% (many short documents), and cutoffs above 4% can empty a short-text vocabulary. *(single)*
- The evidence favours continuous scoring: idf, IC and c-TF-IDF weights are all continuous.
- No reviewed source benchmarks discrete bands for ordering labels.
- Partial logarithmic binning (Milojević 2010) is the proposed mitigation for recovering tail structure, but it is a proposal for distribution analysis, debated against MLE (Clauset/Shalizi/Newman), and not validated for label ordering or label banding.

### minimum-support thresholds (vocabulary pruning)

Builds on: collection document frequency (df / idf) as a specificity signal, heavy-tailed term-frequency distributions.

- Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003); discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018); strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018).
- These thresholds are documented as conventions, not benchmarked optima: the primary survey notes "no systematic study" existed, and tests only simulated LDA corpora.
- About 30% of the vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF). *(single)*
- Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.

### phrase selection and stopword / multilingual handling at the rare-term tail

Builds on: collection document frequency (df / idf) as a specificity signal.

- The review has no surviving claims on single-word vs multi-word phrase selection, or on stopword / multilingual handling at the rare-term tail (brief item 5); these are unanswered by this corpus.

## Do not say

Wordings the research itself says are wrong or overstated.

- "Specificity = term use (frequency), not meaning."
  Why: killed in verification, vote 0-3; df is a proxy, not a definition of semantic specificity
  Say instead: df is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity.
- "df-as-specificity was largely untested before Joho & Sanderson 2007."
  Why: killed in verification, vote 1-2
- "Extensive relative pruning (frequent + infrequent) doesn't compromise topic quality."
  Why: killed in verification, vote 0-3; one of two claims that aggressive pruning is uniformly safe
  Say instead: About 30% of the vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF).
- "Vocabulary pruning + document sampling boosts performance without quality loss."
  Why: killed in verification, vote 0-3; one of two claims that aggressive pruning is uniformly safe
- The missing head-to-head of collection df, class df and IC counted as a point for any of them.
  Why: the note says to report it as "no controlled evidence found," not as a point for any option
  Say instead: No controlled head-to-head exists comparing collection df vs class df vs IC for ordering descriptive cluster labels general→specific; the closest tests (Joho & Sanderson; Yang & Callan) are over WordNet / taxonomy induction, indirect for the label-ordering task.
- "c-TF-IDF down-weights terms spread across many classes."
  Why: f_t is a frequency sum across classes, not a count of classes containing the term; the note calls the "spread across many classes" gloss the docs' own simplification
  Say instead: In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term.

## Gaps

What the research did not establish.

- Has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for ordering cluster labels general→specific? Apparently not done; the closest tests are WordNet / taxonomy induction (indirect).
- Do the bucketing instabilities (9.3% vs 74.1%) and the ~30%-removable finding hold on real corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)? The primary evidence is one simulated-LDA study.
- The effect of single- vs multi-word selection and of stopword / multilingual handling on rare-term specificity.
- Does log binning or a rank transform actually improve label ordering in practice, or only distribution visualisation / fitting?
- Whether BM25 saturation, PMI or burstiness order terms by altitude: they produced no surviving verified claim.
