# Term specificity and multi-level labelling: writer's view

> [!abstract] About this view
> What the research found, for writing from. Each claim gives who found it, the setting it holds for, the kind of evidence, its standing where the research stated one, and for an absence whether it was searched for. A claim with no standing given has none stated in the research; "limited by access" means a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. The view is generated from the knowledge note `Term specificity and multi-level labelling.md`, where every claim is checked against the research.

## What the research found, by question

### TSL

**D1. Across methods that assign descriptive terms to groups of documents (TF-IDF and its class or group based variants, topic model labelling, graph based keyphrase extraction, hierarchical or taxonomic labelling, and faceted or multi granular tagging), what signals quantify how general or specific a candidate term is, and how do multi level labelling methods produce a sequence of terms running from general to specific? Specifically: which document frequency or information theoretic signals (collection document frequency and inverse document frequency, group or class based document frequency, pointwise mutual information, information content as negative log probability, BM25 style saturation, burstiness or concentration measures) are standard; how do heavy tailed (Zipfian) document frequency distributions affect threshold or quantile based bucketing of terms by frequency; what minimum document frequency or support thresholds are conventional and what is their measured effect; and how do hierarchical labelling systems decide a term's altitude (collection frequency, depth in an induced hierarchy, or information content)?**

*Answer, as the research gave it; not checked by a second reader.* **Open Questions (unanswered by the literature)**

1. **Head-to-head (the core gap):** has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for *ordering cluster labels* general→specific? Appears **not done**; closest tests are WordNet/taxonomy induction (indirect). 2. **Real-corpus replication:** do the bucketing instabilities (9.3% vs 74.1%) and ~30%-removable findings hold on *real* corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)? Primary evidence is one simulated-LDA study. 3. **Phrases & multilingual tail:** effect of single- vs multi-word selection and stopword/multilingual handling on rare-term specificity — uncovered. 4. **Does log binning / rank transform actually improve label *ordering*** in practice, or only distribution visualisation/fitting?

*Answer, as the research gave it; not checked by a second reader.* **(a) Collection document frequency / information content — with a sharp qualification, and a (c)-flavoured nuance for cluster labelling**

The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality. IC is the cleaner *altitude* axis of the two because of that monotonicity. The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms**. Independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels. So df is a good *specificity* signal but a weak *altitude discriminator* across the full range. One taxonomy-induction framework abandons a single fixed altitude signal entirely, learning a separate information function per abstraction level. Class/group-based df (**c-TF-IDF**, BERTopic) operationalises the same inverse-frequency principle at the cluster level, but it is an **engineering instantiation, not an independently validated specificity measure**. So the answer is **not (b) group-df alone** — group df has no head-to-head support against collection df or IC. **Continuous vs discrete:** the evidence favours **continuous scoring** (idf, IC, c-TF-IDF weights are all continuous). **Discrete frequency banding is shown to be unstable under heavy tails** — the same relative cutoff produced 9.3% vs 74.1% vocabulary reduction across corpora, and cutoffs >4% can empty a short-text vocabulary. No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis, not validated for label banding. **Minimum-support thresholds:** **yes, standard practice** — drop frequency-1 terms; discard terms in <0.5–1% of documents; strip terms in >99% as corpus stopwords — but documented as **conventions, not benchmarked optima** (the primary survey notes "no systematic study" existed and tests only simulated LDA corpora). **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific. The closest tests are over WordNet / taxonomy induction — indirect for the label-ordering task. Report this as "no controlled evidence found," not as a point for any option. This is exactly the band-collapse question the brief's routing flagged as likely under-benchmarked.

## Concepts

In an order where each concept comes after the ones it builds on; the order means nothing more.

### collection document frequency (idf) as a specificity signal

- Collection document frequency (df, idf) is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more, and specificity is inversely related to df (lower df = more specific); but df is a frequency proxy, not a definition of semantic specificity, and low df from typos, OCR or identifiers does not imply true specificity. (Sparck Jones 1972)
  Holds for: collection-level document frequency of terms; the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
- Document frequency is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity. (Sparck Jones 1972)
  Holds for: df as a specificity signal.

### information content in an is-a taxonomy

- WordNet is an online lexical database in which English nouns, verbs, adjectives and adverbs are organised into sets of synonyms, each representing a lexicalised concept, and semantic relations link the synonym sets. (Miller 1995)
  Background, not from the research.
- Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999) gives general concepts high P and low IC (root P = 1, IC = 0) and specific concepts low P and high IC; P(c) is monotonically nondecreasing up the taxonomy by construction (a parent cumulatively subsumes its children's counts), so altitude maps directly onto generality; it needs a unified root, and WordNet has none naturally. (Resnik 1995; Resnik 1999)
  Holds for: an is-a taxonomy with corpus probabilities; the confidence label is the harness's.
  Evidence: derived; rated "Confidence: high (3-0)" by the research.
- Of collection df and IC, IC is the cleaner altitude axis because of its monotonicity: corpus probability is the principled altitude axis. (Resnik 1995; Resnik 1999)
  Holds for: is-a taxonomies.
- Information content needs a unified root, and WordNet has none naturally. (Resnik 1995; Resnik 1999)
  Holds for: is-a taxonomies, WordNet.

### class-based document frequency (c-TF-IDF)

Builds on: collection document frequency (idf) as a specificity signal.

- Class-based TF-IDF (c-TF-IDF, BERTopic; Grootendorst 2022) treats each cluster as one document, L1-normalises term frequency for cluster size and down-weights via log(1 + A/f_t), operationalising the inverse-frequency principle at the cluster level, but it is an engineering instantiation, not an independently validated specificity measure. (Grootendorst 2022; BERTopic n.d.)
  Holds for: clusters treated as documents (topic modelling); the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
- In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term. (Grootendorst 2022; BERTopic n.d.)
  Holds for: the c-TF-IDF weighting.
- c-TF-IDF is an engineering instantiation of inverse frequency, not an independently benchmarked or validated specificity measure; group df has no head-to-head support against collection df or IC. (Grootendorst 2022)
  Holds for: class or group df at the cluster level.

### other term-weighting signals

- BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering; they are known weighting signals, not validated specificity-altitude axes here. (the note names no source for this)
  Holds for: the review's source set and verification.

### ordering terms from general to specific

Builds on: collection document frequency (idf) as a specificity signal, information content in an is-a taxonomy.

- On WordNet parent-child pairs, collection df ordered terms by specificity with ~74% accuracy overall but reliably only at the specific end (~74–83% accuracy at the bottom two WordNet levels), degrading to ~55–68%, near-random, for general terms. (Joho and Sanderson 2007)
  Holds for: WordNet parent-child pairs (an is-a taxonomy), indirect for ordering descriptive cluster labels; the confidence label is the harness's.
  Evidence: a single source; rated "Confidence: high (3-0)" by the research.
- Caraballo and Charniak (1999) found ~86% accuracy at lower levels and 45.5% at upper levels. (Caraballo and Charniak 1999)
  Holds for: specificity of nouns ordered by level; a corroborating source, not primary.
- Collection df is a good specificity signal but a weak altitude discriminator across the full range of generality: it orders specific terms well and general terms near-randomly. (Joho and Sanderson 2007; Caraballo and Charniak 1999)
  Holds for: WordNet levels, and lower and upper levels of noun specificity in the corroborating study.
- In taxonomy induction, different feature sets won at different abstraction levels (co-occurrence alone for abstract levels L2–L3; contextual, co-occurrence, pattern and syntactic features for concrete levels L4–L6), so no single fixed signal serves all altitudes; the framework abandons a single fixed altitude signal and learns a separate information function per abstraction level. (Yang and Callan 2009)
  Holds for: is-a taxonomy induction, not cluster-label ordering (indirect); the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
- The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet and taxonomies, sound for those and indirect for ordering descriptive cluster labels, so the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support. (Resnik 1995; Resnik 1999; Joho and Sanderson 2007; Yang and Callan 2009)
  Holds for: WordNet and is-a taxonomies.

### ordering descriptive cluster labels from general to specific

Builds on: ordering terms from general to specific, class-based document frequency (c-TF-IDF).

- No controlled head-to-head comparison exists of collection df, class df (c-TF-IDF) and IC for ordering descriptive cluster labels from general to specific; the closest tests are over WordNet and taxonomy induction, indirect for the label-ordering task. (a search result)
  Holds for: the review's five search angles and 20 fetched sources.
  Evidence: a search result.
  Searched for and not found.
- No reviewed source benchmarks discrete frequency bands for ordering labels. (a statement about the reviewed sources)
  Holds for: the sources the review read.
  Evidence: a search result.
  The research does not say whether this was searched for.
- The evidence favours continuous scoring for specificity: idf, IC and c-TF-IDF weights are all continuous. (Sparck Jones 1972; Resnik 1995; Grootendorst 2022)
  Holds for: specificity signals for labelling.

### heavy-tailed term frequency distributions

- Term frequency distributions are heavy-tailed but not reliably Zipfian: a power law fitted best for only 5 of 24 corpora, 19 of 24 were better fit by a discrete Yule distribution, and a continuous GEV fitted best overall, especially in the sparse rare-term tail where Yule and power law fail, the region of rare, specific terms. (Petersen et al. 2016)
  Holds for: 24 corpora (information retrieval); the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
- Low-frequency words are the majority of unique types. (Bystrov et al. 2023)
  Holds for: the corpora of the simulated-LDA pruning study.

### discrete frequency bands and cutoffs under heavy tails

Builds on: heavy-tailed term frequency distributions.

- Threshold bucketing is corpus-structure-dependent and unstable: the same 1% relative cutoff produced 9.3% vocabulary reduction in a corpus of few long documents against 74.1% in one of many short documents, and cutoffs above 4% can empty a short-text vocabulary. (Bystrov et al. 2023)
  Holds for: simulated LDA corpora; the bucketing/pruning evidence leans heavily on one study; the confidence label is the harness's.
  Evidence: modelled; a single source; rated "Confidence: high (3-0)" by the research.
- Partial logarithmic binning is the proposed mitigation for recovering tail structure (Milojević 2010), but it is a proposal for distribution analysis, debated against MLE (Clauset, Shalizi, Newman), and not validated for label ordering or label banding. (Milojevic 2010; Clauset et al. n.d.)
  Holds for: analysis of heavy-tailed distributions.

### minimum-support thresholds for vocabulary

Builds on: heavy-tailed term frequency distributions.

- Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003), discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018), and strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018); these are documented as conventions, not benchmarked optima, and the primary survey notes that "no systematic study" existed and tests only simulated LDA corpora. (Blei et al. 2003; Denny and Spirling 2018; Grimmer and Stewart 2013; Maier and others 2018)
  Holds for: topic-model vocabulary preprocessing; the conventions are cited within [S7], the simulated-LDA pruning study; the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
- About 30% of vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF). (Bystrov et al. 2023)
  Holds for: simulated LDA corpora; not shown on real corpora or non-LDA pipelines.
  Evidence: modelled; a single source.
- Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief. (Schofield et al. 2017)
  Holds for: stopword and very-low-frequency term removal in topic models.

### phrases and multilingual handling at the rare-term tail

- Single-word against multi-word phrase selection, and stopword and multilingual handling at the rare-term tail, produced no surviving claims: their effect on rare-term specificity is unanswered by this corpus. (no evidence collected)
  Holds for: the review's source set.
  Evidence: a search result.
  The research does not say whether this was searched for.

## Do not say

Wordings the research itself says are wrong or overstated, each with the reason and what to say instead.

- Do not write: "Specificity is a matter of term use (frequency), not meaning."
  Why: The claim was killed in verification (vote 0-3): df is a proxy, not a definition of semantic specificity.
  Say instead: Document frequency is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity. (Sparck Jones 1972)
  Holds for: df as a specificity signal.
- Do not write: "Document frequency as a measure of specificity was largely untested before Joho and Sanderson (2007)."
  Why: The claim was killed in verification (vote 1-2).
- Do not write: "Extensive relative pruning of both frequent and infrequent terms does not compromise topic quality."
  Why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted.
  Say instead: Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003), discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018), and strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018); these are documented as conventions, not benchmarked optima, and the primary survey notes that "no systematic study" existed and tests only simulated LDA corpora. (Blei et al. 2003; Denny and Spirling 2018; Grimmer and Stewart 2013; Maier and others 2018)
  Holds for: topic-model vocabulary preprocessing; the conventions are cited within [S7], the simulated-LDA pruning study; the confidence label is the harness's.
  Evidence: rated "Confidence: high (3-0)" by the research.
  Say instead: About 30% of vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF). (Bystrov et al. 2023)
  Holds for: simulated LDA corpora; not shown on real corpora or non-LDA pipelines.
  Evidence: modelled; a single source.
- Do not write: "Vocabulary pruning combined with document sampling boosts performance without loss of quality."
  Why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted.
- Do not write: "The evidence favours collection df over class df or IC for ordering cluster labels from general to specific."
  Why: No controlled head-to-head exists comparing collection df, class df and IC for ordering descriptive cluster labels, and the note says to report this as "no controlled evidence found," not as a point for any option.
  Say instead: No controlled head-to-head comparison exists of collection df, class df (c-TF-IDF) and IC for ordering descriptive cluster labels from general to specific; the closest tests are over WordNet and taxonomy induction, indirect for the label-ordering task. (a search result)
  Holds for: the review's five search angles and 20 fetched sources.
  Evidence: a search result.
  Searched for and not found.
- Do not write: "c-TF-IDF down-weights terms that are spread across many classes."
  Why: In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term; the note calls the "spread across many classes" gloss the documentation's own simplification.
  Say instead: In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term. (Grootendorst 2022; BERTopic n.d.)
  Holds for: the c-TF-IDF weighting.

## Gaps

What the research did not establish.

- The review's answers were never checked by a second reader: its adversarial verification killed four claims, but no critic reviewed the answers, which rest on these figures: ~74–83% accuracy at the bottom two WordNet levels against ~55–68% for general terms, ~86% against 45.5% at lower and upper levels, 9.3% against 74.1% vocabulary reduction from the same relative cutoff, cutoffs above 4% emptying a short-text vocabulary, and the <0.5–1% and >99% document-frequency conventions.
  The research does not say whether this was searched for.
- A controlled head-to-head of collection df, class df (c-TF-IDF) and IC for ordering cluster labels from general to specific.
  Searched for and not found.
- Whether the bucketing instabilities (9.3% against 74.1%) and the ~30%-removable finding hold on real corpora and non-LDA pipelines (for example BERTopic c-TF-IDF); the primary evidence is one simulated-LDA study. (Bystrov et al. 2023)
  The research does not say whether this was searched for.
- The effect of single- against multi-word phrase selection, and of stopword and multilingual handling, on rare-term specificity (brief item 5).
  The research does not say whether this was searched for.
- Whether log binning or a rank transform actually improves label ordering in practice, or only distribution visualisation and fitting. (Milojevic 2010)
  The research does not say whether this was searched for.
- The supporting conventions set (Blei, Denny & Spirling, Grimmer & Stewart, Maier, Schofield) and Caraballo & Charniak have author and page metadata resolved partly from secondary listings, to be verified against their DOI or venue records.
  The research does not say whether this was searched for.

## References

- BERTopic (n.d.). c-TF-IDF documentation. https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html
- Blei, D. M.; Ng, A. Y.; Jordan, M. I. (2003). Latent Dirichlet Allocation. JMLR 3: 993--1022.
- Bystrov, V.; Naboka-Krell, V.; Staszewska-Bystrova, A.; Winker, P. (2023). Analysing the Impact of Removing Infrequent Words on Topic Quality in LDA Models. https://arxiv.org/pdf/2311.14505
- Caraballo, S. A.; Charniak, E. (1999). Determining the Specificity of Nouns from Text. EMNLP/VLC-99: 63--70.
- Clauset; Shalizi; Newman (n.d.).
- Denny, M. J.; Spirling, A. (2018). Text Preprocessing for Unsupervised Learning: Why It Matters, When It Misleads, and What to Do about It. Political Analysis 26(2): 168--189.
- Grimmer, J.; Stewart, B. M. (2013). Text as Data. Political Analysis 21(3): 267--297.
- Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. https://arxiv.org/abs/2203.05794
- Joho, H.; Sanderson, M. (2007). Document frequency and term specificity. RIAO 2007 (Large-Scale Semantic Access to Content). https://doi.org/10.5555/1931390.1931425
- Maier, D.; others (2018). Applying LDA to Social Science Research. Communication Methods and Measures 12(2--3): 93--118.
- Miller, George A. (1995). WordNet: a lexical database for English. Communications of the ACM 38(11): 39--41. https://doi.org/10.1145/219717.219748
- Milojevic, S. (2010). Power-law Distributions in Information Science Making the Case for Logarithmic Binning. JASIST 61(12): 2417--2425. https://doi.org/10.1002/asi.21426
- Petersen, C.; Simonsen, J. G.; Lioma, C. (2016). Power Law Distributions in Information Retrieval. ACM Transactions on Information Systems 34(2): 8. https://doi.org/10.1145/2816815
- Resnik, P. (1995). Using Information Content to Evaluate Semantic Similarity in a Taxonomy. Proceedings of IJCAI-95 1: 448--453. https://arxiv.org/pdf/cmp-lg/9709008
- Resnik, P. (1999). Semantic Similarity in a Taxonomy: An Information-Based Measure and its Application to Problems of Ambiguity in Natural Language. Journal of Artificial Intelligence Research 11: 95--130. https://arxiv.org/pdf/1105.5444
- Schofield, A.; Magnusson, M.; Mimno, D. (2017). Pulling Out the Stops: Rethinking Stopword Removal for Topic Models. EACL 2017: 432--436.
- Sparck Jones, K. (1972). A Statistical Interpretation of Term Specificity and Its Application in Retrieval. Journal of Documentation 28(1): 11--21. https://doi.org/10.1108/eb026526
- Yang, H.; Callan, J. (2009). A Metric-based Framework for Automatic Taxonomy Induction. Proceedings of ACL-IJCNLP 2009: 271--279. https://www.cs.cmu.edu/~callan/Papers/acl09-huiyang.pdf
