---
type: knowledge
title: Term specificity and multi-level labelling
inputs:
  - TSL: PhD/biblion/research/results/term-specificity-labelling-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---

# Term specificity and multi-level labelling

> [!abstract] Note Role
> **Contains**: what the research in the inputs found, one claim per finding, organised by concept, with the
> standing, conditions and sources the notes give, and links back to where each was verified.
> **Cannot contain**: anything not in the inputs (except background entries, marked), verification (it stays
> in the result notes), or guidance on writing, story or order of telling.
> **Order**: the concepts are listed in one valid ordering of the `needs` graph. It has no narrative meaning;
> other valid orderings are equally correct.

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
| TSL | [[term-specificity-labelling-result]] | yes | bracket keys | no | no | fallback |

## Concepts

### wordnet: WordNet
needs: none
- **wordnet.bg1** WordNet is an online lexical database of English that groups nouns, verbs, adjectives and adverbs into synonym sets, each representing a lexicalised concept, and links the sets by semantic relations.
  kind: background · ref: millerWordNetLexicalDatabase1995 · check: DOI 10.1145/219717.219748 resolves on Crossref (Communications of the ACM 38(11), 39–41); stated in the abstract

### term-specificity: Term specificity
needs: none
- **term-specificity.1** Document frequency is a frequency proxy for specificity, not a definition of semantic specificity; low df arising from typos, OCR errors or identifiers does not imply true specificity.
  conf: not stated · class: not stated · holds: the caveat the note attaches to collection df / idf (Spärck Jones 1972); the opposite framing was refuted 0-3 in verification · src: sparckjonesStatisticalInterpretationTerm1972 · trail: TSL §Specificity signals, §Refuted · from: TSL:B-0011, TSL:C-001

### level-ordering: Ordering terms general to specific across levels
needs: term-specificity
- **level-ordering.1** One taxonomy-induction framework (Yang & Callan 2009) abandons a single fixed altitude signal and learns a separate information function per abstraction level; the note reads this as no single fixed signal serving all altitudes.
  conf: not stated · class: not stated · holds: is-a taxonomy induction, not cluster-label ordering · src: yangMetricbasedFrameworkAutomatic2009 (Indirect) · trail: TSL §Verdict, §How multi-level · from: TSL:A-007, TSL:B-0024
- **level-ordering.2** Yang & Callan (2009) found different feature sets win at different abstraction levels: co-occurrence alone for the abstract levels L2–L3; contextual, co-occurrence, pattern and syntactic features together for the concrete levels L4–L6.
  conf: not stated · class: not stated · holds: is-a taxonomy induction, levels L2–L6; indirect for cluster-label ordering · src: yangMetricbasedFrameworkAutomatic2009 (Indirect) · trail: TSL §How multi-level · from: TSL:B-0024, TSL:B-0025

### collection-df: Collection document frequency (idf)
needs: term-specificity, level-ordering, wordnet
- **collection-df.1** Collection document frequency / idf is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more; specificity is inversely related to df (lower df = more specific).
  conf: not stated · class: not stated · holds: retrieval term weighting; a frequency proxy for specificity (term-specificity.1) · src: sparckjonesStatisticalInterpretationTerm1972 · trail: TSL §Verdict, §Specificity signals · from: TSL:A-002, TSL:B-0009, TSL:B-0010, TSL:B-0011 · rating: "Confidence: high (3-0)"
- **collection-df.2** Collection df reliably orders terms by specificity only at the specific end: about 74% accuracy overall on WordNet parent-child pairs, about 74–83% at the bottom two WordNet levels, degrading to about 55–68%, near-random, for general terms.
  conf: single (note: "the only direct empirical test") · class: meas (note: "the only direct empirical test") · holds: WordNet parent-child pairs (Joho & Sanderson 2007); indirect for ordering descriptive cluster labels · src: johoDocumentFrequencyTerm2007 · trail: TSL §Verdict, §How multi-level · from: TSL:A-004, TSL:B-0022, TSL:B-0023 · rating: "Confidence: high (3-0)"
- **collection-df.3** The specific-end pattern is independently corroborated by Caraballo & Charniak (1999): about 86% at lower levels and 45.5% at upper levels.
  conf: repl (note: "Independently corroborated") · class: not stated · holds: lower against upper levels; the note does not say of which hierarchy or what the percentage measures; listed as corroborating, not primary · src: caraballoDeterminingSpecificityNouns1999 (Corroborating (not primary)), johoDocumentFrequencyTerm2007 · trail: TSL §Verdict · from: TSL:A-005
- **collection-df.4** Collection df is a good specificity signal but a weak altitude discriminator across the full range of levels.
  conf: not stated · class: reading (note: "So df is a good") · holds: the reviewer's inference from Joho & Sanderson (2007) and Caraballo & Charniak (1999) over WordNet / noun hierarchies · src: johoDocumentFrequencyTerm2007, caraballoDeterminingSpecificityNouns1999 · trail: TSL §Verdict · from: TSL:A-006

### information-content: Information content IC(c) = −log P(c)
needs: level-ordering, wordnet
- **information-content.1** Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999): general concepts have high P and low IC (the root has P = 1, IC = 0); specific concepts have low P and high IC.
  conf: not stated · class: not stated · holds: is-a taxonomies with corpus probabilities · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §Specificity signals · from: TSL:A-002, TSL:B-0012, TSL:B-0015 · rating: "Confidence: high (3-0)"
- **information-content.2** P(c) is monotonically nondecreasing up the taxonomy by construction, because a parent cumulatively subsumes its children's counts, so altitude maps directly onto generality.
  conf: not stated · class: deriv (note: "by construction") · holds: is-a taxonomies; follows from the definition of P(c) · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §Specificity signals · from: TSL:A-002, TSL:B-0013
- **information-content.3** IC is the cleaner altitude axis of the two signals (IC and collection df), because of that monotonicity; the note calls it the principled altitude axis.
  conf: not stated · class: reading (note: "rests on principled monotonicity") · holds: the reviewer's judgement; evidence over WordNet / taxonomies, indirect for cluster-label ordering · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §Specificity signals, §How multi-level · from: TSL:A-003, TSL:B-0014, TSL:B-0021, TSL:B-0043
- **information-content.4** IC needs a unified root; WordNet has none naturally.
  conf: not stated · class: not stated · holds: WordNet · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Specificity signals · from: TSL:B-0015

### class-df: Class-based df (c-TF-IDF)
needs: collection-df
- **class-df.1** c-TF-IDF (BERTopic, Grootendorst 2022) treats each cluster as one document, L1-normalises term frequency for cluster size, and down-weights terms via log(1 + A/f_t).
  conf: not stated · class: not stated · holds: BERTopic's class-based TF-IDF procedure · src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation · trail: TSL §Specificity signals · from: TSL:B-0016
- **class-df.2** In c-TF-IDF, f_t is a frequency sum across classes, not a count of the classes containing the term.
  conf: not stated · class: not stated · holds: the c-TF-IDF formula; the documentation's "spread across many classes" gloss is its own simplification · src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation · trail: TSL §Specificity signals · from: TSL:B-0017
- **class-df.3** Class/group-based df (c-TF-IDF) operationalises the same inverse-frequency principle as collection df at the cluster level, but is an engineering instantiation, not an independently validated or benchmarked specificity measure.
  conf: not stated · class: not stated · holds: BERTopic c-TF-IDF · src: grootendorstBERTopicNeuralTopic2022 · trail: TSL §Verdict, §Specificity signals · from: TSL:A-008, TSL:B-0018, TSL:B-0019 · rating: "Confidence: high (3-0)"
- **class-df.4** Group df has no head-to-head support against collection df or IC, so group df alone is not the answer the evidence supports.
  conf: not stated · class: not stated · holds: the reviewed source set · src: grootendorstBERTopicNeuralTopic2022 · trail: TSL §Verdict · from: TSL:A-009

### other-signals: BM25 saturation, PMI and burstiness
needs: term-specificity
- **other-signals.1** BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering; the note treats them as known weighting signals, not validated specificity-altitude axes.
  conf: not stated · class: search (note: "produced no surviving verified claim") · holds: this review's source set and verification · src: none (no source named for these signals) · trail: TSL §Specificity signals · from: TSL:B-0020

### signal-comparison: Comparing specificity signals for ordering cluster labels
needs: collection-df, information-content, class-df
- **signal-comparison.1** No controlled head-to-head comparison exists of collection df, class df (c-TF-IDF) and IC for ordering descriptive cluster labels general to specific.
  conf: not stated · class: search (note: "no controlled head-to-head exists") · holds: the review's search; the note: "Appears not done" · src: none (a search result) · trail: TSL §Verdict, §Open Questions · from: TSL:A-014, TSL:B-0035, TSL:B-0036
- **signal-comparison.2** The closest tests (Joho & Sanderson 2007; Yang & Callan 2009) are over WordNet and taxonomy induction, indirect for the label-ordering task; the altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is sound for WordNet and taxonomies.
  conf: not stated · class: not stated · holds: WordNet / is-a taxonomies, not descriptive cluster labels · src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009 (Indirect), resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §Standing caveats · from: TSL:A-015, TSL:B-0042
- **signal-comparison.3** The verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support, with the direct label-ordering head-to-head absent.
  conf: not stated · class: reading (note: "rests on principled monotonicity") · holds: the reviewer's own account of the verdict's basis · src: none (the reviewer's synthesis) · trail: TSL §Standing caveats · from: TSL:B-0043

### heavy-tails: Heavy-tailed term frequency distributions
needs: none
- **heavy-tails.1** Term frequency distributions are heavy-tailed but not reliably Zipfian: Petersen et al. (2016) found a power law the best fit for only 5 of 24 corpora, with 19 of 24 better fit by a discrete Yule distribution.
  conf: not stated · class: not stated · holds: 24 corpora (Petersen et al. 2016) · src: petersenPowerLawDistributions2016 · trail: TSL §Frequency bucketing · from: TSL:B-0026
- **heavy-tails.2** A continuous generalised extreme value (GEV) distribution was the best fit overall, especially in the sparse rare-term tail where Yule and power-law fits fail, which is the region of rare, specific terms.
  conf: not stated · class: not stated · holds: 24 corpora (Petersen et al. 2016) · src: petersenPowerLawDistributions2016 · trail: TSL §Frequency bucketing · from: TSL:B-0026
- **heavy-tails.3** Low-frequency words are the majority of unique types.
  conf: not stated · class: not stated · holds: stated with the Bystrov et al. bucketing finding · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Frequency bucketing · from: TSL:B-0028

### frequency-bucketing: Threshold bucketing and discrete frequency bands
needs: heavy-tails, collection-df
- **frequency-bucketing.1** Discrete frequency banding is unstable under heavy tails and depends on corpus structure: the same 1% relative cutoff produced a 9.3% vocabulary reduction in a corpus of few long documents and 74.1% in one of many short documents.
  conf: single (note: "Primary evidence is one simulated-LDA study") · class: model (note: "simulated-LDA Monte Carlo study") · holds: simulated LDA corpora (Bystrov et al.); not shown on real corpora or non-LDA pipelines · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Verdict, §Frequency bucketing, §Open Questions · from: TSL:A-011, TSL:B-0027, TSL:B-0038, TSL:B-0041
- **frequency-bucketing.2** Cutoffs above 4% can empty a short-text vocabulary.
  conf: single (note: "Primary evidence is one simulated-LDA study") · class: model (note: "simulated-LDA Monte Carlo study") · holds: short-text corpora in simulated LDA corpora (Bystrov et al.) · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Verdict, §Frequency bucketing · from: TSL:A-011, TSL:B-0027, TSL:B-0038, TSL:B-0041
- **frequency-bucketing.3** No reviewed source benchmarks discrete frequency bands for ordering labels.
  conf: not stated · class: search (note: "No reviewed source benchmarks discrete bands") · holds: the reviewed source set · src: none (a search result) · trail: TSL §Verdict · from: TSL:A-012

### continuous-scoring: Continuous against discrete scoring
needs: collection-df, information-content, class-df, frequency-bucketing
- **continuous-scoring.1** The evidence favours continuous scoring: idf, IC and c-TF-IDF weights are all continuous.
  conf: not stated · class: not stated · holds: the reviewer's verdict over the reviewed signals · src: none (the reviewer's synthesis) · trail: TSL §Verdict · from: TSL:A-010

### log-binning: Logarithmic binning
needs: heavy-tails, frequency-bucketing
- **log-binning.1** Partial logarithmic binning is a proposed mitigation for recovering tail structure in distribution analysis (Milojević 2010), not validated for label ordering or label banding.
  conf: not stated · class: not stated · holds: distribution analysis in information science · src: milojevicPowerlawDistributionsInformation2010 · trail: TSL §Verdict, §Frequency bucketing · from: TSL:A-012, TSL:B-0029
- **log-binning.2** Logarithmic binning is debated against maximum-likelihood estimation (Clauset, Shalizi and Newman).
  conf: not stated · class: not stated · holds: power-law fitting · src: milojevicPowerlawDistributionsInformation2010 · trail: TSL §Frequency bucketing · from: TSL:B-0029

### minimum-support: Minimum-support thresholds (vocabulary pruning)
needs: collection-df, frequency-bucketing
- **minimum-support.1** Dropping frequency-1 terms is a standard minimum-support convention (Blei et al. 2003).
  conf: not stated · class: not stated · holds: topic-model preprocessing; conventions cited within Bystrov et al. · src: bleiLatentDirichletAllocation2003 (cited within [S7]) · trail: TSL §Verdict, §Minimum-support · from: TSL:A-013, TSL:B-0030, TSL:B-0031 · rating: "Confidence: high (3-0)"
- **minimum-support.2** Discarding terms that occur in fewer than 0.5–1% of documents is a standard convention (Denny & Spirling 2018).
  conf: not stated · class: not stated · holds: topic-model preprocessing; conventions cited within Bystrov et al. · src: dennyTextPreprocessingUnsupervised2018 (cited within [S7]) · trail: TSL §Verdict, §Minimum-support · from: TSL:A-013, TSL:B-0030, TSL:B-0031 · rating: "Confidence: high (3-0)"
- **minimum-support.3** Stripping terms that occur in more than 99% of documents as corpus stopwords is a standard convention (Grimmer & Stewart 2013; Maier et al. 2018).
  conf: not stated · class: not stated · holds: topic-model preprocessing; conventions cited within Bystrov et al. · src: grimmerTextData2013 (cited within [S7]), maierApplyingLDASocial2018 (cited within [S7]) · trail: TSL §Verdict, §Minimum-support · from: TSL:A-013, TSL:B-0030, TSL:B-0031 · rating: "Confidence: high (3-0)"
- **minimum-support.4** These thresholds are documented as conventions, not benchmarked optima: the primary survey notes that no systematic study existed, and it tests only simulated LDA corpora.
  conf: single (note: "single simulated-corpus LDA study") · class: search (note: "no systematic study") · holds: simulated LDA corpora (Bystrov et al.) · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Verdict, §Minimum-support · from: TSL:A-013, TSL:B-0031
- **minimum-support.5** About 30% of the vocabulary can be removed without qualitative topic loss, whichever criterion is used (df, tf or TF-IDF).
  conf: single (note: "single simulated-corpus LDA study") · class: model (note: "simulated-LDA Monte Carlo study") · holds: simulated LDA corpora (Bystrov et al.); not shown on real corpora or non-LDA pipelines · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Minimum-support, §Standing caveats · from: TSL:B-0030, TSL:B-0031, TSL:B-0041 · rating: "Confidence: high (3-0)"
- **minimum-support.6** Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, which the note says partly undermines the belief that such terms are too specific to matter.
  conf: not stated · class: not stated · holds: topic models (Schofield et al. 2017) · src: schofieldPullingOutStops2017 (cited within [S7]) · trail: TSL §Minimum-support · from: TSL:B-0032

### phrase-multilingual: Phrase selection and multilingual handling at the rare-term tail
needs: term-specificity
- **phrase-multilingual.1** The research collected no evidence on single- against multi-word phrase selection, or on stopword and multilingual handling at the rare-term tail (brief item 5): no claims survived.
  conf: not stated · class: search (note: "no surviving claims") · holds: this review's source set · src: none (no evidence collected) · trail: TSL §Not covered · from: TSL:B-0033, TSL:B-0034

## Do not say

- **dns.1** "Specificity = term use (frequency), not meaning."
  why: refuted in verification, vote 0-3; df is a proxy, not a definition of semantic specificity · instead: term-specificity.1 · trail: TSL §Refuted · from: TSL:C-001, TSL:B-0011
- **dns.2** "Low document frequency implies that a term is specific."
  why: the note: low df from typos/OCR/identifiers does not imply true specificity · instead: term-specificity.1 · trail: TSL §Specificity signals · from: TSL:B-0011
- **dns.3** "df-as-specificity was largely untested before Joho & Sanderson 2007."
  why: refuted in verification, vote 1-2 · instead: none · trail: TSL §Refuted · from: TSL:C-002
- **dns.4** "Extensive relative pruning (frequent + infrequent) doesn't compromise topic quality."
  why: refuted in verification, vote 0-3; one of the two claims that aggressive pruning is uniformly safe · instead: minimum-support.4, minimum-support.5 · trail: TSL §Refuted, §Minimum-support · from: TSL:C-003, TSL:B-0031
- **dns.5** "Vocabulary pruning + document sampling boosts performance without quality loss."
  why: refuted in verification, vote 0-3 · instead: minimum-support.5 · trail: TSL §Refuted · from: TSL:C-004
- **dns.6** The absence of a head-to-head comparison counted as a point for collection df, class df or IC.
  why: the note: report it as "no controlled evidence found," not as a point for any option · instead: signal-comparison.1 · trail: TSL §Verdict · from: TSL:A-016
- **dns.7** "c-TF-IDF down-weights terms spread across many classes."
  why: the note: f_t is a frequency sum across classes, not a count of classes containing the term; the "spread across many classes" gloss is the documentation's own simplification · instead: class-df.2 · trail: TSL §Specificity signals · from: TSL:B-0017

## Gaps

- **gap.1** Has any benchmark compared collection df, class df (c-TF-IDF) and IC for ordering cluster labels general to specific? Appears not done; the closest tests are WordNet / taxonomy induction (indirect).
  blocks: signal-comparison, signal-comparison.1 · origin: the note's open question 1 ("the core gap") · from: TSL:B-0035, TSL:B-0036
- **gap.2** Whether the bucketing instabilities (9.3% against 74.1%) and the ~30%-removable finding hold on real corpora and non-LDA pipelines (for example BERTopic c-TF-IDF).
  blocks: frequency-bucketing.1, frequency-bucketing.2, minimum-support.5 · origin: the note's open question 2; the primary evidence is one simulated-LDA study · from: TSL:B-0037, TSL:B-0038, TSL:B-0041 · src: bystrovAnalysingImpactRemoving2023
- **gap.3** The effect of single- against multi-word selection and of stopword / multilingual handling on rare-term specificity.
  blocks: phrase-multilingual · origin: the note's open question 3 and "Not covered" section; no evidence collected · from: TSL:B-0033, TSL:B-0039
- **gap.4** Whether log binning or a rank transform improves label ordering in practice, or only distribution visualisation and fitting.
  blocks: log-binning · origin: the note's open question 4 · from: TSL:B-0040
- **gap.5** Some references resolved partial author and page metadata from secondary listings (the S8 supporting set; Caraballo & Charniak); the note says to verify them against the DOI or venue record before formal citation.
  blocks: minimum-support, collection-df.3 · origin: the note's closing remark under References · trail: TSL §References · src: bleiLatentDirichletAllocation2003, dennyTextPreprocessingUnsupervised2018, grimmerTextData2013, maierApplyingLDASocial2018, schofieldPullingOutStops2017, caraballoDeterminingSpecificityNouns1999

## Out of scope

- TSL:A-001: the review's choice among the brief's options (routing, not a finding)
- TSL:A-017: links the result to the brief's routing (routing, not a finding)

## Sources

```bibtex
@article{sparckjonesStatisticalInterpretationTerm1972,
  author = {Sp{\"a}rck Jones, K.},
  title = {A Statistical Interpretation of Term Specificity and Its Application in Retrieval},
  journal = {Journal of Documentation},
  volume = {28},
  number = {1},
  pages = {11--21},
  year = {1972},
  doi = {10.1108/eb026526},
  url = {https://www.emerald.com/insight/content/doi/10.1108/eb026526/full/html},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S1]}
}
@inproceedings{resnikUsingInformationContent1995,
  author = {Resnik, P.},
  title = {Using Information Content to Evaluate Semantic Similarity in a Taxonomy},
  booktitle = {Proceedings of IJCAI-95},
  volume = {1},
  pages = {448--453},
  year = {1995},
  eprint = {cmp-lg/9511007},
  url = {https://arxiv.org/pdf/cmp-lg/9709008},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S2], first of two works; the note gives arXiv cmp-lg/9511007 but links cmp-lg/9709008}
}
@article{resnikSemanticSimilarityTaxonomy1999,
  author = {Resnik, P.},
  title = {Semantic Similarity in a Taxonomy: An Information-Based Measure and its Application to Problems of Ambiguity in Natural Language},
  journal = {Journal of Artificial Intelligence Research},
  volume = {11},
  pages = {95--130},
  year = {1999},
  eprint = {1105.5444},
  url = {https://arxiv.org/pdf/1105.5444},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S2], second of two works}
}
@misc{grootendorstBERTopicNeuralTopic2022,
  author = {Grootendorst, M.},
  title = {BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
  year = {2022},
  eprint = {2203.05794},
  url = {https://arxiv.org/abs/2203.05794},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S3], first of two works}
}
@misc{anonCTFIDFDocumentation,
  title = {c-TF-IDF documentation},
  url = {https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html},
  note = {access: not stated; cited as: TSL [S3], second of two works (BERTopic documentation); incomplete: author, year}
}
@inproceedings{johoDocumentFrequencyTerm2007,
  author = {Joho, H. and Sanderson, M.},
  title = {Document frequency and term specificity},
  booktitle = {RIAO 2007 (Large-Scale Semantic Access to Content)},
  year = {2007},
  doi = {10.5555/1931390.1931425},
  url = {https://www.dcs.gla.ac.uk/~hideo/pub/riao07/riao07.pdf},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S4]; incomplete: pages}
}
@inproceedings{yangMetricbasedFrameworkAutomatic2009,
  author = {Yang, H. and Callan, J.},
  title = {A Metric-based Framework for Automatic Taxonomy Induction},
  booktitle = {Proceedings of ACL-IJCNLP 2009},
  pages = {271--279},
  year = {2009},
  url = {https://www.cs.cmu.edu/~callan/Papers/acl09-huiyang.pdf},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S5]}
}
@article{petersenPowerLawDistributions2016,
  author = {Petersen, C. and Simonsen, J. G. and Lioma, C.},
  title = {Power Law Distributions in Information Retrieval},
  journal = {ACM Transactions on Information Systems},
  volume = {34},
  number = {2},
  pages = {Article 8},
  year = {2016},
  doi = {10.1145/2816815},
  url = {https://doi.org/10.1145/2816815},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S6]}
}
@article{bystrovAnalysingImpactRemoving2023,
  author = {Bystrov, V. and Naboka-Krell, V. and Staszewska-Bystrova, A. and Winker, P.},
  title = {Analysing the Impact of Removing Infrequent Words on Topic Quality in LDA Models},
  journal = {Central European Journal of Economic Modelling and Econometrics},
  year = {2023},
  eprint = {2311.14505},
  url = {https://arxiv.org/pdf/2311.14505},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S7]; arXiv 2023, published in the journal 2025; incomplete: volume, pages}
}
@article{milojevicPowerlawDistributionsInformation2010,
  author = {Milojevi{\'c}, S.},
  title = {Power-law Distributions in Information Science: Making the Case for Logarithmic Binning},
  journal = {JASIST},
  volume = {61},
  number = {12},
  pages = {2417--2425},
  year = {2010},
  doi = {10.1002/asi.21426},
  eprint = {1011.1533},
  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21426},
  note = {access: not stated (the note: "Source verification used full-text fetch where possible"); cited as: TSL [S7b]}
}
@article{bleiLatentDirichletAllocation2003,
  author = {Blei, D. M. and Ng, A. Y. and Jordan, M. I.},
  title = {Latent Dirichlet Allocation},
  journal = {JMLR},
  volume = {3},
  pages = {993--1022},
  year = {2003},
  note = {access: secondary (supporting convention cited within [S7]; the note: partial metadata resolved from secondary listings); cited as: TSL [S8]}
}
@article{dennyTextPreprocessingUnsupervised2018,
  author = {Denny, M. J. and Spirling, A.},
  title = {Text Preprocessing for Unsupervised Learning: Why It Matters, When It Misleads, and What to Do about It},
  journal = {Political Analysis},
  volume = {26},
  number = {2},
  pages = {168--189},
  year = {2018},
  note = {access: secondary (supporting convention cited within [S7]; the note: partial metadata resolved from secondary listings); cited as: TSL [S8]}
}
@article{grimmerTextData2013,
  author = {Grimmer, J. and Stewart, B. M.},
  title = {Text as Data},
  journal = {Political Analysis},
  volume = {21},
  number = {3},
  pages = {267--297},
  year = {2013},
  note = {access: secondary (supporting convention cited within [S7]; the note: partial metadata resolved from secondary listings); cited as: TSL [S8]}
}
@article{maierApplyingLDASocial2018,
  author = {Maier, D. and others},
  title = {Applying LDA to Social Science Research},
  journal = {Communication Methods and Measures},
  volume = {12},
  number = {2--3},
  pages = {93--118},
  year = {2018},
  note = {access: secondary (supporting convention cited within [S7]; the note: partial metadata resolved from secondary listings); cited as: TSL [S8]; incomplete: author (et al.)}
}
@inproceedings{schofieldPullingOutStops2017,
  author = {Schofield, A. and Magnusson, M. and Mimno, D.},
  title = {Pulling Out the Stops: Rethinking Stopword Removal for Topic Models},
  booktitle = {EACL 2017},
  pages = {432--436},
  year = {2017},
  note = {access: secondary (supporting convention cited within [S7]; the note: partial metadata resolved from secondary listings); cited as: TSL [S8]}
}
@inproceedings{caraballoDeterminingSpecificityNouns1999,
  author = {Caraballo, S. A. and Charniak, E.},
  title = {Determining the Specificity of Nouns from Text},
  booktitle = {EMNLP/VLC-99},
  pages = {63--70},
  year = {1999},
  note = {access: not stated (listed as "Corroborating (not primary)"; the note: partial metadata resolved from secondary listings); cited as: TSL References, Corroborating}
}
@article{millerWordNetLexicalDatabase1995,
  author = {Miller, George A.},
  title = {WordNet: A Lexical Database for English},
  journal = {Communications of the ACM},
  volume = {38},
  number = {11},
  pages = {39--41},
  year = {1995},
  doi = {10.1145/219717.219748},
  note = {background; checked on Crossref 2026-10-21}
}
```
