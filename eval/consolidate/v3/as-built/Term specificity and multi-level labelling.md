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
- **wordnet.bg1** WordNet is an online lexical database for English, designed for use under program control.
  kind: background · ref: millerWordNetLexicalDatabase1995 · check: DOI 10.1145/219717.219748 resolves on Crossref (Communications of the ACM 38(11), 39-41); stated in the title and the first sentence of the abstract

### df-idf: collection document frequency (df / idf) as a specificity signal
needs: none
- **df-idf.1** Collection df / idf is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more; specificity is inversely related to df (lower df = more specific).
  conf: not stated · class: not stated · holds: term weighting over a document collection for retrieval; not a definition of semantic specificity (df-idf.2) · src: sparckjonesStatisticalInterpretationTerm1972 · trail: TSL §Verdict, §1. Specificity signals · from: TSL:A-002, TSL:B-0009, TSL:B-0010, TSL:B-0011 · rating: "Confidence: high (3-0)"
- **df-idf.2** df is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity.
  conf: not stated · class: not stated · holds: a caveat the note gives in its entry for the collection-df signal; the opposite framing ("specificity = term use not meaning") was refuted 0-3 in verification · src: sparckjonesStatisticalInterpretationTerm1972 · trail: TSL §1. Specificity signals, §Refuted · from: TSL:B-0011, TSL:C-001

### information-content: information content, IC(c) = −log P(c)
needs: wordnet
- **information-content.1** Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999): general concepts have high P and low IC (root P = 1, IC = 0); specific concepts have low P and high IC.
  conf: not stated · class: not stated · holds: is-a taxonomies with corpus probabilities · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §1. Specificity signals · from: TSL:A-002, TSL:B-0012, TSL:B-0015 · rating: "Confidence: high (3-0)"
- **information-content.2** P(c) is monotonically nondecreasing up the taxonomy, by construction (a parent cumulatively subsumes its children's counts), so corpus probability is monotonic up the hierarchy and altitude maps directly onto generality.
  conf: not stated · class: deriv (note: "by construction") · holds: an is-a taxonomy in which a parent's count includes its children's · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §1. Specificity signals · from: TSL:A-002, TSL:B-0013
- **information-content.3** IC needs a unified root; WordNet has none naturally.
  conf: not stated · class: not stated · holds: a caveat the note gives in its entry for IC [S2]; WordNet · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §1. Specificity signals · from: TSL:B-0015

### c-tf-idf: class-based df (c-TF-IDF, BERTopic)
needs: df-idf, information-content
- **c-tf-idf.1** c-TF-IDF (BERTopic, Grootendorst 2022) treats each cluster as one document, L1-normalises tf for cluster size, and down-weights via log(1 + A/f_t).
  conf: not stated · class: not stated · holds: BERTopic's class-based TF-IDF procedure, as described in the paper and its documentation · src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation · trail: TSL §1. Specificity signals · from: TSL:B-0016, TSL:B-0019 · rating: "Confidence: high (3-0)"
- **c-tf-idf.2** In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term.
  conf: not stated · class: not stated · holds: the c-TF-IDF weighting as defined; the documentation's "spread across many classes" gloss is its own simplification (dns.6) · src: grootendorstBERTopicNeuralTopic2022, anonCTFIDFDocumentation · trail: TSL §1. Specificity signals · from: TSL:B-0017
- **c-tf-idf.3** Class/group-based df (c-TF-IDF) operationalises the same inverse-frequency principle at the cluster level, but it is an engineering instantiation, not an independently validated (benchmarked) specificity measure.
  conf: not stated · class: not stated · holds: cluster-level weighting in BERTopic · src: grootendorstBERTopicNeuralTopic2022 · trail: TSL §Verdict, §1. Specificity signals · from: TSL:A-008, TSL:B-0018
- **c-tf-idf.4** Group df has no head-to-head support against collection df or IC.
  conf: not stated · class: search (note: "no head-to-head support") · holds: the sources the review found · src: none (a statement about what the review found) · trail: TSL §Verdict · from: TSL:A-009

### altitude-ordering: ordering terms general→specific (altitude)
needs: df-idf, information-content, c-tf-idf, wordnet
- **altitude-ordering.1** Collection df / idf and information content are two foundational, mutually consistent specificity signals, established by the strongest, most direct primary evidence the review found.
  conf: not stated · class: not stated · holds: collection df in retrieval; IC in an is-a taxonomy · src: sparckjonesStatisticalInterpretationTerm1972, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict · from: TSL:A-002
- **altitude-ordering.2** IC (corpus probability) is the cleaner, principled altitude axis of the two, because of its monotonicity up the hierarchy.
  conf: not stated · class: not stated · holds: is-a taxonomies, where P(c) is monotonic up the hierarchy · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §1. Specificity signals, §2. How multi-level · from: TSL:A-003, TSL:B-0014, TSL:B-0021
- **altitude-ordering.3** Collection df reliably orders terms by specificity only at the specific end: ~74% accuracy overall on WordNet parent-child pairs, ~74–83% at the bottom two WordNet levels, degrading to ~55–68%, near-random, for general terms.
  conf: single (note: "the only direct empirical test") · class: not stated · holds: WordNet parent-child pairs; the bottom two levels vs general terms; not shown for cluster labels (altitude-ordering.8) · src: johoDocumentFrequencyTerm2007 · trail: TSL §Verdict, §2. How multi-level · from: TSL:A-004, TSL:B-0022, TSL:B-0023 · rating: "Confidence: high (3-0)"
- **altitude-ordering.4** The same pattern is independently corroborated by Caraballo & Charniak (1999): ~86% at lower levels, 45.5% at upper levels.
  conf: repl (note: "Independently corroborated") · class: not stated · holds: specificity of nouns, lower vs upper levels; each figure belongs to its own study · src: caraballoDeterminingSpecificityNouns1999, johoDocumentFrequencyTerm2007 · trail: TSL §Verdict · from: TSL:A-004, TSL:A-005
- **altitude-ordering.5** df is a good specificity signal but a weak altitude discriminator across the full range.
  conf: not stated · class: not stated · holds: the review's conclusion from the WordNet figures (altitude-ordering.3, .4) · src: none (the reviewer's conclusion from altitude-ordering.3 and .4) · trail: TSL §Verdict · from: TSL:A-006
- **altitude-ordering.6** One taxonomy-induction framework (Yang & Callan 2009) abandons a single fixed altitude signal and learns a separate information function per abstraction level: different feature sets win at different levels (co-occurrence alone for abstract L2–L3; contextual + co-occurrence + pattern + syntactic for concrete L4–L6), so no single fixed signal serves all altitudes.
  conf: not stated · class: not stated · holds: is-a taxonomy induction, not cluster-label ordering · src: yangMetricbasedFrameworkAutomatic2009 (Indirect) · trail: TSL §Verdict, §2. How multi-level · from: TSL:A-007, TSL:B-0024, TSL:B-0025, TSL:B-0026 · rating: "Confidence: high (3-0)"
- **altitude-ordering.7** No controlled head-to-head exists comparing collection df vs class df vs IC for ordering descriptive cluster labels general→specific; the closest tests (Joho & Sanderson; Yang & Callan) are over WordNet / taxonomy induction, indirect for the label-ordering task.
  conf: not stated · class: search (note: "no controlled head-to-head exists") · holds: the sources the review found; the closest tests are WordNet and taxonomy induction · src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009 · trail: TSL §Verdict, §Open Questions · from: TSL:A-014, TSL:A-015, TSL:B-0038, TSL:B-0039
- **altitude-ordering.8** The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet / taxonomies: sound for those, indirect for descriptive cluster-label ordering; the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.
  conf: not stated · class: not stated · holds: WordNet and taxonomies; not descriptive cluster labels · src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Standing caveats · from: TSL:B-0045, TSL:B-0046

### other-signals: BM25 saturation, PMI and burstiness
needs: altitude-ordering
- **other-signals.1** BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering: known weighting signals, not validated specificity-altitude axes here.
  conf: not stated · class: search (note: "produced no surviving verified claim") · holds: the review's source set · src: none (the note cites no source for them) · trail: TSL §1. Specificity signals · from: TSL:B-0020

### term-frequency-distribution: heavy-tailed term-frequency distributions
needs: none
- **term-frequency-distribution.1** Term-frequency distributions are heavy-tailed but not reliably Zipfian: Petersen et al. (2016) found power-law best for only 5/24 corpora, 19/24 better fit by discrete Yule, and continuous GEV best overall, especially in the sparse rare-term tail where Yule and power-law fail.
  conf: not stated · class: not stated · holds: 24 corpora; the rare-term tail is the region of rare, specific terms · src: petersenPowerLawDistributions2016 · trail: TSL §3. Frequency bucketing · from: TSL:B-0027, TSL:B-0028 · rating: "Confidence: high (3-0)"
- **term-frequency-distribution.2** Low-frequency words are the majority of unique types.
  conf: not stated · class: not stated · holds: stated in the note's entry for [S7] · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §3. Frequency bucketing · from: TSL:B-0030

### frequency-bucketing: discrete frequency banding and continuous scoring
needs: term-frequency-distribution, df-idf, information-content, c-tf-idf, altitude-ordering
- **frequency-bucketing.1** Threshold bucketing is corpus-structure-dependent and unstable under heavy tails: the same 1% relative cutoff produced a 9.3% vocabulary reduction (few long documents) vs 74.1% (many short documents), and cutoffs above 4% can empty a short-text vocabulary.
  conf: single (note: "Primary evidence is one simulated-LDA study") · class: model (note: "simulated-LDA study") · holds: LDA on simulated corpora; not shown on real corpora or non-LDA pipelines (gap.2) · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §Verdict, §3. Frequency bucketing, §Open Questions · from: TSL:A-011, TSL:B-0029, TSL:B-0031, TSL:B-0040, TSL:B-0041 · rating: "Confidence: high (3-0)"
- **frequency-bucketing.2** The evidence favours continuous scoring: idf, IC and c-TF-IDF weights are all continuous.
  conf: not stated · class: not stated · holds: the specificity signals reviewed · src: none (the reviewer's synthesis) · trail: TSL §Verdict · from: TSL:A-010
- **frequency-bucketing.3** No reviewed source benchmarks discrete bands for ordering labels.
  conf: not stated · class: search (note: "No reviewed source benchmarks discrete bands") · holds: the sources the review found · src: none (a statement about what the review found) · trail: TSL §Verdict · from: TSL:A-012
- **frequency-bucketing.4** Partial logarithmic binning (Milojević 2010) is the proposed mitigation for recovering tail structure, but it is a proposal for distribution analysis, debated against MLE (Clauset/Shalizi/Newman), and not validated for label ordering or label banding.
  conf: not stated · class: not stated · holds: distribution analysis; not label ordering · src: milojevicPowerlawDistributionsInformation2010 · trail: TSL §Verdict, §3. Frequency bucketing · from: TSL:A-012, TSL:B-0032

### minimum-support: minimum-support thresholds (vocabulary pruning)
needs: df-idf, term-frequency-distribution
- **minimum-support.1** Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003); discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018); strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018).
  conf: not stated · class: not stated · holds: topic-model preprocessing conventions, cited within [S7] · src: bleiLatentDirichletAllocation2003, dennyTextPreprocessingUnsupervised2018, grimmerTextData2013, maierApplyingLDASocial2018 · trail: TSL §Verdict, §4. Minimum-support · from: TSL:A-013, TSL:B-0033, TSL:B-0034 · rating: "Confidence: high (3-0)"
- **minimum-support.2** These thresholds are documented as conventions, not benchmarked optima: the primary survey notes "no systematic study" existed, and tests only simulated LDA corpora.
  conf: not stated · class: not stated · holds: the conventions in minimum-support.1 · src: bleiLatentDirichletAllocation2003, dennyTextPreprocessingUnsupervised2018, grimmerTextData2013, maierApplyingLDASocial2018, schofieldPullingOutStops2017 · trail: TSL §Verdict, §4. Minimum-support · from: TSL:A-013, TSL:B-0034
- **minimum-support.3** About 30% of the vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF).
  conf: single (note: "single simulated-corpus LDA study") · class: model (note: "simulated-LDA Monte Carlo study") · holds: LDA on simulated corpora (Bystrov et al.); not shown on real corpora or non-LDA pipelines (gap.2) · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §4. Minimum-support, §Open Questions, §Standing caveats · from: TSL:B-0033, TSL:B-0034, TSL:B-0040, TSL:B-0041, TSL:B-0044
- **minimum-support.4** Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.
  conf: not stated · class: not stated · holds: topic models · src: schofieldPullingOutStops2017 · trail: TSL §4. Minimum-support · from: TSL:B-0035

### phrase-and-multilingual-tail: phrase selection and stopword / multilingual handling at the rare-term tail
needs: df-idf
- **phrase-and-multilingual-tail.1** The review has no surviving claims on single-word vs multi-word phrase selection, or on stopword / multilingual handling at the rare-term tail (brief item 5); these are unanswered by this corpus.
  conf: not stated · class: search (note: "no surviving claims") · holds: the review's source set · src: none (no evidence collected) · trail: TSL §5. Not covered · from: TSL:B-0036, TSL:B-0037

## Do not say

- **dns.1** "Specificity = term use (frequency), not meaning."
  why: killed in verification, vote 0-3; df is a proxy, not a definition of semantic specificity · instead: df-idf.2 · trail: TSL §Refuted · from: TSL:C-001
- **dns.2** "df-as-specificity was largely untested before Joho & Sanderson 2007."
  why: killed in verification, vote 1-2 · instead: none · trail: TSL §Refuted · from: TSL:C-002
- **dns.3** "Extensive relative pruning (frequent + infrequent) doesn't compromise topic quality."
  why: killed in verification, vote 0-3; one of two claims that aggressive pruning is uniformly safe · instead: minimum-support.3 · trail: TSL §Refuted, §4. Minimum-support · from: TSL:C-003, TSL:B-0034
- **dns.4** "Vocabulary pruning + document sampling boosts performance without quality loss."
  why: killed in verification, vote 0-3; one of two claims that aggressive pruning is uniformly safe · instead: none · trail: TSL §Refuted, §4. Minimum-support · from: TSL:C-004, TSL:B-0034
- **dns.5** The missing head-to-head of collection df, class df and IC counted as a point for any of them.
  why: the note says to report it as "no controlled evidence found," not as a point for any option · instead: altitude-ordering.7 · trail: TSL §Verdict · from: TSL:A-016
- **dns.6** "c-TF-IDF down-weights terms spread across many classes."
  why: f_t is a frequency sum across classes, not a count of classes containing the term; the note calls the "spread across many classes" gloss the docs' own simplification · instead: c-tf-idf.2 · trail: TSL §1. Specificity signals · from: TSL:B-0017

## Gaps

- **gap.1** Has any benchmark compared collection df vs class df (c-TF-IDF) vs IC for ordering cluster labels general→specific? Apparently not done; the closest tests are WordNet / taxonomy induction (indirect).
  blocks: altitude-ordering · origin: the note's open question 1 (the core gap) and its most important negative result · src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009 · from: TSL:A-014, TSL:B-0038, TSL:B-0039
- **gap.2** Do the bucketing instabilities (9.3% vs 74.1%) and the ~30%-removable finding hold on real corpora and non-LDA pipelines (e.g. BERTopic c-TF-IDF)? The primary evidence is one simulated-LDA study.
  blocks: frequency-bucketing.1, minimum-support.3 · origin: the note's open question 2 and its standing caveat · src: bystrovAnalysingImpactRemoving2023 · from: TSL:B-0040, TSL:B-0041, TSL:B-0044
- **gap.3** The effect of single- vs multi-word selection and of stopword / multilingual handling on rare-term specificity.
  blocks: phrase-and-multilingual-tail · origin: the note's open question 3; §5 not covered (no evidence collected) · from: TSL:B-0036, TSL:B-0037, TSL:B-0042
- **gap.4** Does log binning or a rank transform actually improve label ordering in practice, or only distribution visualisation / fitting?
  blocks: frequency-bucketing.4 · origin: the note's open question 4 · src: milojevicPowerlawDistributionsInformation2010 · from: TSL:B-0043
- **gap.5** Whether BM25 saturation, PMI or burstiness order terms by altitude: they produced no surviving verified claim.
  blocks: other-signals · origin: not found in the review's source set · from: TSL:B-0020

## Out of scope

- TSL:A-001: the review's choice among the brief's options (routing, not a finding)
- TSL:A-017: ties the negative result to the brief's routing (routing, not a finding)

## Sources

```bibtex
@article{sparckjonesStatisticalInterpretationTerm1972,
  author = {Sp{\"a}rck Jones, K.},
  title = {A Statistical Interpretation of Term Specificity and Its Application in Retrieval},
  journal = {Journal of Documentation},
  year = {1972},
  volume = {28},
  number = {1},
  pages = {11--21},
  doi = {10.1108/eb026526},
  url = {https://www.emerald.com/insight/content/doi/10.1108/eb026526/full/html},
  note = {access: not stated; cited as: TSL [S1]}
}

@inproceedings{resnikUsingInformationContent1995,
  author = {Resnik, P.},
  title = {Using Information Content to Evaluate Semantic Similarity in a Taxonomy},
  booktitle = {Proceedings of IJCAI-95},
  year = {1995},
  volume = {1},
  pages = {448--453},
  eprint = {cmp-lg/9511007},
  url = {https://arxiv.org/pdf/cmp-lg/9709008},
  note = {access: not stated; cited as: TSL [S2] (first of two works); the note gives arXiv:cmp-lg/9511007 but links https://arxiv.org/pdf/cmp-lg/9709008; incomplete: doi}
}

@article{resnikSemanticSimilarityTaxonomy1999,
  author = {Resnik, P.},
  title = {Semantic Similarity in a Taxonomy: An Information-Based Measure and its Application to Problems of Ambiguity in Natural Language},
  journal = {Journal of Artificial Intelligence Research},
  year = {1999},
  volume = {11},
  pages = {95--130},
  eprint = {1105.5444},
  url = {https://arxiv.org/pdf/1105.5444},
  note = {access: not stated; cited as: TSL [S2] (second of two works); incomplete: doi}
}

@misc{grootendorstBERTopicNeuralTopic2022,
  author = {Grootendorst, M.},
  title = {BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
  year = {2022},
  eprint = {2203.05794},
  url = {https://arxiv.org/abs/2203.05794},
  note = {access: not stated; cited as: TSL [S3] (first of two works)}
}

@online{anonCTFIDFDocumentation,
  title = {c-TF-IDF documentation},
  url = {https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html},
  note = {access: not stated; cited as: TSL [S3] (second of two works); incomplete: author, year}
}

@inproceedings{johoDocumentFrequencyTerm2007,
  author = {Joho, H. and Sanderson, M.},
  title = {Document frequency and term specificity},
  booktitle = {RIAO 2007 (Large-Scale Semantic Access to Content)},
  year = {2007},
  doi = {10.5555/1931390.1931425},
  url = {https://www.dcs.gla.ac.uk/~hideo/pub/riao07/riao07.pdf},
  note = {access: not stated; cited as: TSL [S4]; incomplete: pages}
}

@inproceedings{yangMetricbasedFrameworkAutomatic2009,
  author = {Yang, H. and Callan, J.},
  title = {A Metric-based Framework for Automatic Taxonomy Induction},
  booktitle = {Proceedings of ACL-IJCNLP 2009},
  year = {2009},
  pages = {271--279},
  url = {https://www.cs.cmu.edu/~callan/Papers/acl09-huiyang.pdf},
  note = {access: not stated; cited as: TSL [S5]; incomplete: doi}
}

@article{petersenPowerLawDistributions2016,
  author = {Petersen, C. and Simonsen, J. G. and Lioma, C.},
  title = {Power Law Distributions in Information Retrieval},
  journal = {ACM Transactions on Information Systems},
  year = {2016},
  volume = {34},
  number = {2},
  pages = {Article 8},
  doi = {10.1145/2816815},
  url = {https://doi.org/10.1145/2816815},
  note = {access: not stated; cited as: TSL [S6]}
}

@article{bystrovAnalysingImpactRemoving2023,
  author = {Bystrov, V. and Naboka-Krell, V. and Staszewska-Bystrova, A. and Winker, P.},
  title = {Analysing the Impact of Removing Infrequent Words on Topic Quality in LDA Models},
  journal = {Central European Journal of Economic Modelling and Econometrics},
  year = {2023},
  eprint = {2311.14505},
  url = {https://arxiv.org/pdf/2311.14505},
  note = {access: not stated; cited as: TSL [S7]; the note dates the arXiv version 2023 and the journal publication 2025; incomplete: volume, pages, doi}
}

@article{milojevicPowerlawDistributionsInformation2010,
  author = {Milojevi{\'c}, S.},
  title = {Power-law Distributions in Information Science: Making the Case for Logarithmic Binning},
  journal = {JASIST},
  year = {2010},
  volume = {61},
  number = {12},
  pages = {2417--2425},
  doi = {10.1002/asi.21426},
  eprint = {1011.1533},
  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21426},
  note = {access: not stated; cited as: TSL [S7b]}
}

@article{bleiLatentDirichletAllocation2003,
  author = {Blei, D. M. and Ng, A. Y. and Jordan, M. I.},
  title = {Latent Dirichlet Allocation},
  journal = {JMLR},
  year = {2003},
  volume = {3},
  pages = {993--1022},
  note = {access: secondary (the note: "Supporting conventions cited within [S7]"); cited as: TSL [S8]; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: doi}
}

@article{dennyTextPreprocessingUnsupervised2018,
  author = {Denny, M. J. and Spirling, A.},
  title = {Text Preprocessing for Unsupervised Learning: Why It Matters, When It Misleads, and What to Do about It},
  journal = {Political Analysis},
  year = {2018},
  volume = {26},
  number = {2},
  pages = {168--189},
  note = {access: secondary (the note: "Supporting conventions cited within [S7]"); cited as: TSL [S8]; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: doi}
}

@article{grimmerTextData2013,
  author = {Grimmer, J. and Stewart, B. M.},
  title = {Text as Data},
  journal = {Political Analysis},
  year = {2013},
  volume = {21},
  number = {3},
  pages = {267--297},
  note = {access: secondary (the note: "Supporting conventions cited within [S7]"); cited as: TSL [S8]; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: doi}
}

@article{maierApplyingLDASocial2018,
  author = {Maier, D. and others},
  title = {Applying LDA to Social Science Research},
  journal = {Communication Methods and Measures},
  year = {2018},
  volume = {12},
  number = {2--3},
  pages = {93--118},
  note = {access: secondary (the note: "Supporting conventions cited within [S7]"); cited as: TSL [S8]; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: full author list, doi}
}

@inproceedings{schofieldPullingOutStops2017,
  author = {Schofield, A. and Magnusson, M. and Mimno, D.},
  title = {Pulling Out the Stops: Rethinking Stopword Removal for Topic Models},
  booktitle = {EACL 2017},
  year = {2017},
  pages = {432--436},
  note = {access: secondary (the note: "Supporting conventions cited within [S7]"); cited as: TSL [S8]; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: doi}
}

@inproceedings{caraballoDeterminingSpecificityNouns1999,
  author = {Caraballo, S. A. and Charniak, E.},
  title = {Determining the Specificity of Nouns from Text},
  booktitle = {EMNLP/VLC-99},
  year = {1999},
  pages = {63--70},
  note = {access: not stated; cited as: TSL, "Corroborating (not primary)"; metadata partly from secondary listings, the note says to verify before formal citation; incomplete: doi}
}

@article{millerWordNetLexicalDatabase1995,
  author = {Miller, George A.},
  title = {WordNet: A Lexical Database for English},
  journal = {Communications of the ACM},
  year = {1995},
  volume = {38},
  number = {11},
  pages = {39--41},
  doi = {10.1145/219717.219748},
  note = {background; checked on Crossref}
}
```
