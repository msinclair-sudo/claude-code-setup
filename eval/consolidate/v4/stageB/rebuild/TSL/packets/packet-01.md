## collection-df.1 (claim)

Collection document frequency (df, idf) is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more, and specificity is inversely related to df (lower df = more specific).

- conf: not stated
- class: not stated
- holds: collection-level document frequency of terms; the confidence label is the harness's
- src: sparckjonesStatisticalInterpretationTerm1972
- rating: "Confidence: high (3-0)"
- trail: TSL §1. Specificity, §Verdict

From the note:

> TSL:B-0009 [1. Specificity signals the field uses] - **Collection df / idf** [S1] — *the* seminal specificity signal (Spärck Jones 1972): weight terms by collection frequency so matches on rarer, more specific terms count for more.
>
> TSL:B-0010 [1. Specificity signals the field uses] Specificity inversely related to df.
>
> TSL:B-0011 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: df is a *frequency proxy*, not a definition of semantic specificity — the "specificity = term use not meaning" framing was **refuted** (0-3); low df from typos/OCR/identifiers does not imply true specificity.
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-002 [Verdict] The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>

Not found in the cited text (where to look, not what is wrong): holds: collection-level

## collection-df.2 (claim)

Document frequency is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity.

- conf: not stated
- class: not stated
- holds: df as a specificity signal
- src: sparckjonesStatisticalInterpretationTerm1972
- trail: TSL §1. Specificity

From the note:

> TSL:B-0009 [1. Specificity signals the field uses] - **Collection df / idf** [S1] — *the* seminal specificity signal (Spärck Jones 1972): weight terms by collection frequency so matches on rarer, more specific terms count for more.
>
> TSL:B-0011 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: df is a *frequency proxy*, not a definition of semantic specificity — the "specificity = term use not meaning" framing was **refuted** (0-3); low df from typos/OCR/identifiers does not imply true specificity.
>

## information-content.1 (claim)

Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999) gives general concepts high P and low IC (root P = 1, IC = 0) and specific concepts low P and high IC; P(c) is monotonically nondecreasing up the taxonomy by construction (a parent cumulatively subsumes its children's counts), so altitude maps directly onto generality.

- conf: not stated
- class: deriv (note: "by construction")
- holds: an is-a taxonomy with corpus probabilities; the confidence label is the harness's
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- rating: "Confidence: high (3-0)"
- trail: TSL §1. Specificity, §Verdict

From the note:

> TSL:B-0012 [1. Specificity signals the field uses] - **Information content IC(c) = −log P(c)** [S2] — Resnik (1995/1999): general concepts have high P, low IC (root P=1, IC=0); specific concepts low P, high IC.
>
> TSL:B-0013 [1. Specificity signals the field uses] P(c) monotonically nondecreasing up the taxonomy, by construction (a parent cumulatively subsumes its children's counts).
>
> TSL:B-0015 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: needs a unified root; WordNet has none naturally.
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-002 [Verdict] The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>

## information-content.2 (claim)

Of collection df and IC, IC is the cleaner altitude axis because of its monotonicity: corpus probability is the principled altitude axis.

- conf: not stated
- class: not stated
- holds: is-a taxonomies
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Verdict, §1. Specificity, §2. How

From the note:

> TSL:A-002 [Verdict] The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> TSL:A-003 [Verdict] IC is the cleaner *altitude* axis of the two because of that monotonicity.
>
> TSL:B-0014 [1. Specificity signals the field uses] The cleanest altitude axis.
>
> TSL:B-0021 [2. How multi-level systems order general→specific] - **Information content / corpus probability** is the principled altitude axis (above) [S2].
>

## information-content.3 (claim)

Information content needs a unified root, and WordNet has none naturally.

- conf: not stated
- class: not stated
- holds: is-a taxonomies, WordNet
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §1. Specificity

From the note:

> TSL:B-0012 [1. Specificity signals the field uses] - **Information content IC(c) = −log P(c)** [S2] — Resnik (1995/1999): general concepts have high P, low IC (root P=1, IC=0); specific concepts low P, high IC.
>
> TSL:B-0015 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: needs a unified root; WordNet has none naturally.
>

Not found in the cited text (where to look, not what is wrong): holds: is-a

## class-df.1 (claim)

Class-based TF-IDF (c-TF-IDF, BERTopic; Grootendorst 2022) treats each cluster as one document, L1-normalises term frequency for cluster size and down-weights via log(1 + A/f_t), operationalising the inverse-frequency principle at the cluster level.

- conf: not stated
- class: not stated
- holds: clusters treated as documents (topic modelling); the confidence label is the harness's
- src: grootendorstBERTopicNeuralTopic2022, bertopicCTFIDFDocumentation
- rating: "Confidence: high (3-0)"
- trail: TSL §1. Specificity, §Verdict

From the note:

> TSL:R-0008 [References] *BERTopic: Neural topic modeling with a class-based TF-IDF procedure.* arXiv:2203.05794. https://arxiv.org/abs/2203.05794 — and c-TF-IDF documentation, https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html
>
> TSL:B-0016 [1. Specificity signals the field uses] - **Class/group df — c-TF-IDF** [S3] — BERTopic (Grootendorst 2022): treat each cluster as one document, L1-normalise tf for cluster size, down-weight via log(1 + A/f_t).
>
> TSL:B-0019 [1. Specificity signals the field uses] *Confidence: high (3-0).*
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-008 [Verdict] Class/group-based df (**c-TF-IDF**, BERTopic) operationalises the same inverse-frequency principle at the cluster level, but it is an **engineering instantiation, not an independently validated specificity measure** [S3].
>

Not found in the cited text (where to look, not what is wrong): L1-normalises; holds: modelling

## class-df.2 (claim)

In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term.

- conf: not stated
- class: not stated
- holds: the c-TF-IDF weighting
- src: grootendorstBERTopicNeuralTopic2022, bertopicCTFIDFDocumentation
- trail: TSL §1. Specificity

From the note:

> TSL:B-0016 [1. Specificity signals the field uses] - **Class/group df — c-TF-IDF** [S3] — BERTopic (Grootendorst 2022): treat each cluster as one document, L1-normalise tf for cluster size, down-weight via log(1 + A/f_t).
>
> TSL:B-0017 [1. Specificity signals the field uses] *Technical nuance:* f_t is a frequency *sum* across classes, not a count of classes containing the term — so the "spread across many classes" gloss is the docs' own simplification.
>

## class-df.3 (claim)

c-TF-IDF is an engineering instantiation of inverse frequency, not an independently benchmarked or validated specificity measure; group df has no head-to-head support against collection df or IC.

- conf: not stated
- class: not stated
- holds: class or group df at the cluster level
- src: grootendorstBERTopicNeuralTopic2022
- trail: TSL §1. Specificity, §Verdict

From the note:

> TSL:B-0018 [1. Specificity signals the field uses] Engineering instantiation of inverse-frequency, **not** independently benchmarked.
>
> TSL:A-008 [Verdict] Class/group-based df (**c-TF-IDF**, BERTopic) operationalises the same inverse-frequency principle at the cluster level, but it is an **engineering instantiation, not an independently validated specificity measure** [S3].
>
> TSL:A-009 [Verdict] So the answer is **not (b) group-df alone** — group df has no head-to-head support against collection df or IC.
>

## weighting-signals.1 (claim)

BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering; they are known weighting signals, not validated specificity-altitude axes here.

- conf: not stated
- class: not stated
- holds: the review's source set and verification
- src: none (the note names no source for this)
- trail: TSL §1. Specificity

From the note:

> TSL:B-0020 [1. Specificity signals the field uses] - **BM25 saturation, PMI, burstiness** — appeared in the source set but produced no surviving verified claim tying them to *altitude ordering*; treat as known weighting signals, not validated specificity-altitude axes here.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## altitude-ordering.1 (claim)

On WordNet parent-child pairs, collection df ordered terms by specificity with ~74% accuracy overall but reliably only at the specific end (~74–83% accuracy at the bottom two WordNet levels), degrading to ~55–68%, near-random, for general terms.

- conf: single (note: "the only direct empirical test")
- class: not stated
- holds: WordNet parent-child pairs (an is-a taxonomy), indirect for ordering descriptive cluster labels; the confidence label is the harness's
- src: johoDocumentFrequencyTerm2007
- rating: "Confidence: high (3-0)"
- trail: TSL §Verdict, §2. How

From the note:

> TSL:A-014 [Verdict] **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific.
>
> TSL:A-004 [Verdict] The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms** [S4].
>
> TSL:B-0022 [2. How multi-level systems order general→specific] - **Collection df works only at the specific end** [S4]: ~74% overall on WordNet parent-child pairs, reliable only at the bottom two levels, ~55–68% for general terms.
>
> TSL:B-0023 [2. How multi-level systems order general→specific] *Confidence: high (3-0).* This is the key bounding fact tempering §1.
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-015 [Verdict] The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
>

Not found in the cited text (where to look, not what is wrong): holds: is-a

## altitude-ordering.2 (claim)

Caraballo and Charniak (1999) found ~86% accuracy at lower levels and 45.5% at upper levels.

- conf: not stated
- class: not stated
- holds: specificity of nouns ordered by level; a corroborating source, not primary
- src: caraballoDeterminingSpecificityNouns1999 (corroborating, not primary)
- trail: TSL §Verdict, §References

From the note:

> TSL:A-005 [Verdict] Independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels.
>
> TSL:R-0029 [References] **Corroborating (not primary):** Caraballo, S. A., & Charniak, E. (1999).
>
> TSL:R-0030 [References] *Determining the Specificity of Nouns from Text.* EMNLP/VLC-99, 63–70.
>

## altitude-ordering.3 (claim)

Collection df is a good specificity signal but a weak altitude discriminator across the full range of generality: it orders specific terms well and general terms near-randomly.

- conf: repl (note: "Independently corroborated by Caraballo & Charniak (1999)")
- class: not stated
- holds: WordNet levels, and lower and upper levels of noun specificity in the corroborating study
- src: johoDocumentFrequencyTerm2007, caraballoDeterminingSpecificityNouns1999
- trail: TSL §Verdict

From the note:

> TSL:R-0030 [References] *Determining the Specificity of Nouns from Text.* EMNLP/VLC-99, 63–70.
>
> TSL:A-004 [Verdict] The qualification is decisive and comes from the only direct empirical test: **collection df reliably orders terms by specificity only at the specific end** (~74–83% accuracy at the bottom two WordNet levels) and **degrades to ~55–68% — near-random — for general terms** [S4].
>
> TSL:A-005 [Verdict] Independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels.
>
> TSL:A-006 [Verdict] So df is a good *specificity* signal but a weak *altitude discriminator* across the full range.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## altitude-ordering.4 (claim)

In taxonomy induction, different feature sets won at different abstraction levels (co-occurrence alone for abstract levels L2–L3; contextual, co-occurrence, pattern and syntactic features for concrete levels L4–L6), so no single fixed signal serves all altitudes; the framework abandons a single fixed altitude signal and learns a separate information function per abstraction level.

- conf: not stated
- class: not stated
- holds: is-a taxonomy induction, not cluster-label ordering (indirect); the confidence label is the harness's
- src: yangMetricbasedFrameworkAutomatic2009
- rating: "Confidence: high (3-0)"
- trail: TSL §2. How, §Verdict

From the note:

> TSL:B-0024 [2. How multi-level systems order general→specific] - **Learned, per-level information functions** [S5]: Yang & Callan (2009) found different feature sets win at different abstraction levels (co-occurrence alone for abstract L2–L3; contextual+co-occurrence+pattern+syntactic for concrete L4–L6) — i.e. no single fixed signal serves all altitudes.
>
> TSL:B-0025 [2. How multi-level systems order general→specific] *Confidence: high (3-0).
>
> TSL:B-0026 [2. How multi-level systems order general→specific] Indirect:* this is is-a taxonomy induction, not cluster-label ordering.
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-007 [Verdict] One taxonomy-induction framework [S5] abandons a single fixed altitude signal entirely, learning a separate information function per abstraction level.
>

## altitude-ordering.5 (claim)

The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet and taxonomies, sound for those and indirect for ordering descriptive cluster labels, so the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.

- conf: not stated
- class: not stated
- holds: WordNet and is-a taxonomies
- src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Standing caveats, §Verdict

From the note:

> TSL:B-0045 [Standing caveats on the corpus] The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet/taxonomies — sound for those, *indirect* for descriptive cluster-label ordering.
>
> TSL:B-0046 [Standing caveats on the corpus] The verdict's altitude claim therefore rests on principled monotonicity (IC) plus indirect empirical support, with the direct label-ordering head-to-head genuinely absent.
>
> TSL:A-015 [Verdict] The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
>

Not found in the cited text (where to look, not what is wrong): holds: is-a

## label-ordering.1 (claim)

No controlled head-to-head comparison exists of collection df, class df (c-TF-IDF) and IC for ordering descriptive cluster labels from general to specific; the closest tests are over WordNet and taxonomy induction, indirect for the label-ordering task.

- conf: not stated
- class: search (note: "no controlled evidence found")
- holds: the review's five search angles and 20 fetched sources
- src: none (a search result)
- search: searched, not found (note: "no controlled evidence found")
- trail: TSL §Verdict, §Open Questions, §Term Specificity

From the note:

> TSL:A-014 [Verdict] **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific.
>
> TSL:A-015 [Verdict] The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
>
> TSL:A-016 [Verdict] Report this as "no controlled evidence found," not as a point for any option.
>
> TSL:B-0038 [Open Questions (unanswered by the literature)] **Head-to-head (the core gap):** has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for *ordering cluster labels* general→specific?
>
> TSL:B-0039 [Open Questions (unanswered by the literature)] Appears **not done**; closest tests are WordNet/taxonomy induction (indirect).
>
> TSL:B-0001 [Term Specificity & Multi-Altitude Labelling — Literature Review] Returned from the `deep-research` harness (5 search angles → 20 sources fetched → 91 claims extracted → 25 adversarially verified, 3-vote, need 2/3 refutes to kill → 21 confirmed, 4 killed).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## label-ordering.2 (claim)

No reviewed source benchmarks discrete frequency bands for ordering labels.

- conf: not stated
- class: search (note: "No reviewed source benchmarks discrete bands")
- holds: the sources the review read
- src: none (a statement about the reviewed sources)
- search: not stated
- trail: TSL §Verdict

From the note:

> TSL:A-012 [Verdict] No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis [S7b], not validated for label banding.
>

## label-ordering.3 (claim)

The evidence favours continuous scoring for specificity: idf, IC and c-TF-IDF weights are all continuous.

- conf: not stated
- class: not stated
- holds: specificity signals for labelling
- src: sparckjonesStatisticalInterpretationTerm1972, resnikUsingInformationContent1995, grootendorstBERTopicNeuralTopic2022
- trail: TSL §Verdict

From the note:

> TSL:A-010 [Verdict] **Continuous vs discrete:** the evidence favours **continuous scoring** (idf, IC, c-TF-IDF weights are all continuous).
>

## term-frequency-distributions.1 (claim)

Term frequency distributions are heavy-tailed but not reliably Zipfian: a power law fitted best for only 5 of 24 corpora, 19 of 24 were better fit by a discrete Yule distribution, and a continuous GEV fitted best overall, especially in the sparse rare-term tail where Yule and power law fail, the region of rare, specific terms.

- conf: not stated
- class: not stated
- holds: 24 corpora (information retrieval); the confidence label is the harness's
- src: petersenPowerLawDistributions2016
- rating: "Confidence: high (3-0)"
- trail: TSL §3. Frequency

From the note:

> TSL:R-0015 [References] *Power Law Distributions in Information Retrieval.* ACM Transactions on Information Systems, 34(2), Article 8.
>
> TSL:B-0027 [3. Frequency bucketing under heavy tails] - **Distributions are heavy-tailed but not reliably Zipfian** [S6]: Petersen et al. (2016) found power-law best for only 5/24 corpora; 19/24 better fit by discrete Yule; continuous GEV best overall, **especially in the sparse rare-term tail where Yule/power-law fail** — precisely the region of rare, specific terms.
>
> TSL:B-0028 [3. Frequency bucketing under heavy tails] *Confidence: high (3-0).*
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>

## term-frequency-distributions.2 (claim)

Low-frequency words are the majority of unique types.

- conf: not stated
- class: not stated
- holds: the corpora of the simulated-LDA pruning study
- src: bystrovAnalysingImpactRemoving2023
- trail: TSL §3. Frequency

From the note:

> TSL:B-0044 [Standing caveats on the corpus] The bucketing/pruning evidence leans heavily on one simulated-LDA Monte Carlo study (Bystrov et al.).
>
> TSL:B-0029 [3. Frequency bucketing under heavy tails] - **Threshold bucketing is corpus-structure-dependent and unstable** [S7]: same 1% cutoff → 9.3% reduction (few long docs) vs 74.1% (many short docs); >4% empties short-text vocabularies.
>
> TSL:B-0030 [3. Frequency bucketing under heavy tails] Low-frequency words are the majority of unique types.
>

## frequency-banding.1 (claim)

Threshold bucketing is corpus-structure-dependent and unstable: the same 1% relative cutoff produced 9.3% vocabulary reduction in a corpus of few long documents against 74.1% in one of many short documents, and cutoffs above 4% can empty a short-text vocabulary.

- conf: single (note: "single simulated-corpus LDA study")
- class: model (note: "one simulated-LDA Monte Carlo study")
- holds: simulated LDA corpora; the bucketing/pruning evidence leans heavily on one study; the confidence label is the harness's
- src: bystrovAnalysingImpactRemoving2023
- rating: "Confidence: high (3-0)"
- trail: TSL §3. Frequency, §Verdict, §4. Minimum, §Standing caveats

From the note:

> TSL:B-0029 [3. Frequency bucketing under heavy tails] - **Threshold bucketing is corpus-structure-dependent and unstable** [S7]: same 1% cutoff → 9.3% reduction (few long docs) vs 74.1% (many short docs); >4% empties short-text vocabularies.
>
> TSL:B-0031 [3. Frequency bucketing under heavy tails] *Confidence: high (3-0).*
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:A-011 [Verdict] **Discrete frequency banding is shown to be unstable under heavy tails** — the same relative cutoff produced 9.3% vs 74.1% vocabulary reduction across corpora, and cutoffs >4% can empty a short-text vocabulary [S7].
>
> TSL:B-0034 [4. Minimum-support thresholds] *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>
> TSL:B-0044 [Standing caveats on the corpus] The bucketing/pruning evidence leans heavily on one simulated-LDA Monte Carlo study (Bystrov et al.).
>

## frequency-banding.2 (claim)

Partial logarithmic binning is the proposed mitigation for recovering tail structure (Milojević 2010), but it is a proposal for distribution analysis, debated against MLE (Clauset, Shalizi, Newman), and not validated for label ordering or label banding.

- conf: not stated
- class: not stated
- holds: analysis of heavy-tailed distributions
- src: milojevicPowerlawDistributionsInformation2010, clauset
- trail: TSL §3. Frequency, §Verdict

From the note:

> TSL:B-0032 [3. Frequency bucketing under heavy tails] - **Partial logarithmic binning** is the proposed mitigation for recovering tail structure [S7b] — but it's a *proposal* for distribution analysis (Milojević 2010), debated vs MLE (Clauset/Shalizi/Newman), and **not validated for label ordering**.
>
> TSL:A-012 [Verdict] No reviewed source benchmarks discrete bands for *ordering* labels; log binning is only a *proposed* mitigation for distribution analysis [S7b], not validated for label banding.
>

Not found in the cited text (where to look, not what is wrong): holds: heavy-tailed

## minimum-support.1 (claim)

Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003), discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018), and strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018); these are documented as conventions, not benchmarked optima, and the primary survey notes that "no systematic study" existed and tests only simulated LDA corpora.

- conf: not stated
- class: not stated
- holds: topic-model vocabulary preprocessing; the conventions are cited within [S7], the simulated-LDA pruning study; the confidence label is the harness's
- src: bleiLatentDirichletAllocation2003 (cited within [S7]), dennyTextPreprocessingUnsupervised2018 (cited within [S7]), grimmerTextData2013 (cited within [S7]), maierApplyingLDASocial2018 (cited within [S7])
- rating: "Confidence: high (3-0)"
- trail: TSL §Verdict, §4. Minimum, §References

From the note:

> TSL:B-0044 [Standing caveats on the corpus] The bucketing/pruning evidence leans heavily on one simulated-LDA Monte Carlo study (Bystrov et al.).
>
> TSL:A-013 [Verdict] **Minimum-support thresholds:** **yes, standard practice** — drop frequency-1 terms; discard terms in <0.5–1% of documents; strip terms in >99% as corpus stopwords — but documented as **conventions, not benchmarked optima** (the primary survey notes "no systematic study" existed and tests only simulated LDA corpora) [S8].
>
> TSL:B-0033 [4. Minimum-support thresholds] - **Standard conventions** [S8]: drop frequency-1 (Blei et al. 2003); <0.5–1% of docs (Denny & Spirling 2018); >99% as stopwords (Grimmer & Stewart 2013; Maier et al. 2018). ~30% of vocabulary removable without qualitative topic loss, independent of criterion (df, tf, or TF-IDF).
>
> TSL:B-0034 [4. Minimum-support thresholds] *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>
> TSL:B-0004 [Term Specificity & Multi-Altitude Labelling — Literature Review] Confidence labels below are the harness's; indirect support is flagged inline.
>
> TSL:R-0023 [References] [S8] Supporting conventions cited within [S7]: Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003).
>

Not found in the cited text (where to look, not what is wrong): holds: topic-model

## minimum-support.2 (claim)

About 30% of vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF).

- conf: single (note: "single simulated-corpus LDA study")
- class: model (note: "single simulated-corpus LDA study")
- holds: simulated LDA corpora; not shown on real corpora or non-LDA pipelines
- src: bystrovAnalysingImpactRemoving2023
- trail: TSL §4. Minimum, §Standing caveats, §Open Questions

From the note:

> TSL:B-0033 [4. Minimum-support thresholds] - **Standard conventions** [S8]: drop frequency-1 (Blei et al. 2003); <0.5–1% of docs (Denny & Spirling 2018); >99% as stopwords (Grimmer & Stewart 2013; Maier et al. 2018). ~30% of vocabulary removable without qualitative topic loss, independent of criterion (df, tf, or TF-IDF).
>
> TSL:B-0034 [4. Minimum-support thresholds] *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>
> TSL:B-0044 [Standing caveats on the corpus] The bucketing/pruning evidence leans heavily on one simulated-LDA Monte Carlo study (Bystrov et al.).
>
> TSL:B-0040 [Open Questions (unanswered by the literature)] **Real-corpus replication:** do the bucketing instabilities (9.3% vs 74.1%) and ~30%-removable findings hold on *real* corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)?
>
> TSL:B-0041 [Open Questions (unanswered by the literature)] Primary evidence is one simulated-LDA study.
>

## minimum-support.3 (claim)

Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.

- conf: not stated
- class: not stated
- holds: stopword and very-low-frequency term removal in topic models
- src: schofieldPullingOutStops2017 (cited within [S7])
- trail: TSL §4. Minimum, §References

From the note:

> TSL:R-0028 [References] *Pulling Out the Stops: Rethinking Stopword Removal for Topic Models.* EACL 2017, 432–436.
>
> TSL:B-0035 [4. Minimum-support thresholds] Schofield et al. (2017) found removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.
>
> TSL:R-0023 [References] [S8] Supporting conventions cited within [S7]: Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003).
>

Not found in the cited text (where to look, not what is wrong): holds: in

## not-covered.1 (claim)

Single-word against multi-word phrase selection, and stopword and multilingual handling at the rare-term tail, produced no surviving claims: their effect on rare-term specificity is unanswered by this corpus.

- conf: not stated
- class: search (note: "no surviving claims")
- holds: the review's source set
- src: none (no evidence collected)
- search: not stated
- trail: TSL §5. Not covered, §Open Questions

From the note:

> TSL:B-0036 [5. Not covered (no evidence collected)] Single-word vs multi-word phrase selection, and stopword/multilingual handling at the rare-term tail (brief item 5) — **no surviving claims**.
>
> TSL:B-0037 [5. Not covered (no evidence collected)] Treat as unanswered by this corpus.
>
> TSL:B-0042 [Open Questions (unanswered by the literature)] **Phrases & multilingual tail:** effect of single- vs multi-word selection and stopword/multilingual handling on rare-term specificity — uncovered.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## dns.1 (do not say)

"Specificity is a matter of term use (frequency), not meaning."

- why: The claim was killed in verification (vote 0-3): df is a proxy, not a definition of semantic specificity.
- instead: collection-df.2
- trail: TSL §Refuted

From the note:

> TSL:C-001 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"Specificity = term use (frequency), not meaning."** Vote 0-3. df is a proxy, not a definition of semantic specificity [S1].
>
> TSL:B-0011 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: df is a *frequency proxy*, not a definition of semantic specificity — the "specificity = term use not meaning" framing was **refuted** (0-3); low df from typos/OCR/identifiers does not imply true specificity.
>

Not found in the cited text (where to look, not what is wrong): "Specificity is a matter of term use (frequency), not meaning."

## dns.2 (do not say)

"Document frequency as a measure of specificity was largely untested before Joho and Sanderson (2007)."

- why: The claim was killed in verification (vote 1-2).
- instead: none
- trail: TSL §Refuted

From the note:

> TSL:C-002 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"df-as-specificity was largely untested before Joho & Sanderson 2007."** Vote 1-2 [S4].
>

Not found in the cited text (where to look, not what is wrong): "Document frequency as a measure of specificity was largely untested before Joho and Sanderson (2007)."

## dns.3 (do not say)

"Extensive relative pruning of both frequent and infrequent terms does not compromise topic quality."

- why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted.
- instead: minimum-support.1, minimum-support.2
- trail: TSL §Refuted, §4. Minimum

From the note:

> TSL:C-003 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"Extensive relative pruning (frequent + infrequent) doesn't compromise topic quality."** Vote 0-3.
>
> TSL:B-0034 [4. Minimum-support thresholds] *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>

Not found in the cited text (where to look, not what is wrong): "Extensive relative pruning of both frequent and infrequent terms does not compromise topic quality."

## dns.4 (do not say)

"Vocabulary pruning combined with document sampling boosts performance without loss of quality."

- why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted.
- instead: none
- trail: TSL §Refuted, §4. Minimum

From the note:

> TSL:C-004 [Refuted (killed in verification — do NOT reintroduce)] - ✗ **"Vocabulary pruning + document sampling boosts performance without quality loss."** Vote 0-3.
>
> TSL:B-0034 [4. Minimum-support thresholds] *Confidence: high (3-0).* Caveats: conventions, not optima; evidence is a **single simulated-corpus LDA study**; two claims that aggressive pruning is uniformly safe were **refuted** (0-3).
>

Not found in the cited text (where to look, not what is wrong): "Vocabulary pruning combined with document sampling boosts performance without loss of quality."

## dns.5 (do not say)

"The evidence favours collection df over class df or IC for ordering cluster labels from general to specific."

- why: No controlled head-to-head exists comparing collection df, class df and IC for ordering descriptive cluster labels, and the note says to report this as "no controlled evidence found," not as a point for any option.
- instead: label-ordering.1
- trail: TSL §Verdict

From the note:

> TSL:A-014 [Verdict] **The most important negative result:** **no controlled head-to-head exists** comparing collection df vs class df vs IC for *ordering descriptive cluster labels* general→specific.
>
> TSL:A-016 [Verdict] Report this as "no controlled evidence found," not as a point for any option.
>

Not found in the cited text (where to look, not what is wrong): "The evidence favours collection df over class df or IC for ordering cluster labels from general to specific."

## dns.6 (do not say)

"c-TF-IDF down-weights terms that are spread across many classes."

- why: In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term; the note calls the "spread across many classes" gloss the documentation's own simplification.
- instead: class-df.2
- trail: TSL §1. Specificity

From the note:

> TSL:B-0017 [1. Specificity signals the field uses] *Technical nuance:* f_t is a frequency *sum* across classes, not a count of classes containing the term — so the "spread across many classes" gloss is the docs' own simplification.
>

Not found in the cited text (where to look, not what is wrong): "c-TF-IDF down-weights terms that are spread across many classes."

