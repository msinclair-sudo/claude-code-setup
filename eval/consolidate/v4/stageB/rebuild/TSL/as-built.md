---
type: knowledge
title: Term specificity and multi-level labelling
inputs:
  - TSL: PhD/biblion/research/results/term-specificity-labelling-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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
| TSL | [[term-specificity-labelling-result]] | refutations only | bracket keys | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### collection-df: collection document frequency (idf) as a specificity signal
needs: none
- **collection-df.1** Collection document frequency (df, idf) is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more, and specificity is inversely related to df (lower df = more specific).
  conf: not stated · class: not stated · holds: collection-level document frequency of terms; the confidence label is the harness's · src: sparckjonesStatisticalInterpretationTerm1972 · rating: "Confidence: high (3-0)" · trail: TSL §1. Specificity, §Verdict · from: TSL:B-0009..0011, TSL:B-0004, TSL:A-002
- **collection-df.2** Document frequency is a frequency proxy, not a definition of semantic specificity: low df from typos, OCR or identifiers does not imply true specificity.
  conf: not stated · class: not stated · holds: df as a specificity signal · src: sparckjonesStatisticalInterpretationTerm1972 · trail: TSL §1. Specificity · from: TSL:B-0009, TSL:B-0011

### information-content: information content in an is-a taxonomy
needs: none
- **information-content.bg1** WordNet is an online lexical database in which English nouns, verbs, adjectives and adverbs are organised into sets of synonyms, each representing a lexicalised concept, and semantic relations link the synonym sets.
  kind: background · ref: millerWordNetLexicalDatabase1995 · check: DOI 10.1145/219717.219748 resolves on Crossref; stated in the abstract
- **information-content.1** Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999) gives general concepts high P and low IC (root P = 1, IC = 0) and specific concepts low P and high IC; P(c) is monotonically nondecreasing up the taxonomy by construction (a parent cumulatively subsumes its children's counts), so altitude maps directly onto generality.
  conf: not stated · class: deriv (note: "by construction") · holds: an is-a taxonomy with corpus probabilities; the confidence label is the harness's · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · rating: "Confidence: high (3-0)" · trail: TSL §1. Specificity, §Verdict · from: TSL:B-0012, TSL:B-0013, TSL:B-0015, TSL:B-0004, TSL:A-002
- **information-content.2** Of collection df and IC, IC is the cleaner altitude axis because of its monotonicity: corpus probability is the principled altitude axis.
  conf: not stated · class: not stated · holds: is-a taxonomies · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Verdict, §1. Specificity, §2. How · from: TSL:A-002, TSL:A-003, TSL:B-0014, TSL:B-0021
- **information-content.3** Information content needs a unified root, and WordNet has none naturally.
  conf: not stated · class: not stated · holds: is-a taxonomies, WordNet · src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §1. Specificity · from: TSL:B-0012, TSL:B-0015

### class-df: class-based document frequency (c-TF-IDF)
needs: collection-df
- **class-df.1** Class-based TF-IDF (c-TF-IDF, BERTopic; Grootendorst 2022) treats each cluster as one document, L1-normalises term frequency for cluster size and down-weights via log(1 + A/f_t), operationalising the inverse-frequency principle at the cluster level.
  conf: not stated · class: not stated · holds: clusters treated as documents (topic modelling); the confidence label is the harness's · src: grootendorstBERTopicNeuralTopic2022, bertopicCTFIDFDocumentation · rating: "Confidence: high (3-0)" · trail: TSL §1. Specificity, §Verdict · from: TSL:R-0008, TSL:B-0016, TSL:B-0019, TSL:B-0004, TSL:A-008
- **class-df.2** In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term.
  conf: not stated · class: not stated · holds: the c-TF-IDF weighting · src: grootendorstBERTopicNeuralTopic2022, bertopicCTFIDFDocumentation · trail: TSL §1. Specificity · from: TSL:B-0016, TSL:B-0017
- **class-df.3** c-TF-IDF is an engineering instantiation of inverse frequency, not an independently benchmarked or validated specificity measure; group df has no head-to-head support against collection df or IC.
  conf: not stated · class: not stated · holds: class or group df at the cluster level · src: grootendorstBERTopicNeuralTopic2022 · trail: TSL §1. Specificity, §Verdict · from: TSL:B-0018, TSL:A-008, TSL:A-009

### weighting-signals: other term-weighting signals
needs: none
- **weighting-signals.1** BM25 saturation, PMI and burstiness appeared in the source set but produced no surviving verified claim tying them to altitude ordering; they are known weighting signals, not validated specificity-altitude axes here.
  conf: not stated · class: not stated · holds: the review's source set and verification · src: none (the note names no source for this) · trail: TSL §1. Specificity · from: TSL:B-0020

### altitude-ordering: ordering terms from general to specific
needs: collection-df, information-content
- **altitude-ordering.1** On WordNet parent-child pairs, collection df ordered terms by specificity with ~74% accuracy overall but reliably only at the specific end (~74–83% accuracy at the bottom two WordNet levels), degrading to ~55–68%, near-random, for general terms.
  conf: single (note: "the only direct empirical test") · class: not stated · holds: WordNet parent-child pairs (an is-a taxonomy), indirect for ordering descriptive cluster labels; the confidence label is the harness's · src: johoDocumentFrequencyTerm2007 · rating: "Confidence: high (3-0)" · trail: TSL §Verdict, §2. How · from: TSL:A-014, TSL:A-004, TSL:B-0022, TSL:B-0023, TSL:B-0004, TSL:A-015
- **altitude-ordering.2** Caraballo and Charniak (1999) found ~86% accuracy at lower levels and 45.5% at upper levels.
  conf: not stated · class: not stated · holds: specificity of nouns ordered by level; a corroborating source, not primary · src: caraballoDeterminingSpecificityNouns1999 (corroborating, not primary) · trail: TSL §Verdict, §References · from: TSL:A-005, TSL:R-0029, TSL:R-0030
- **altitude-ordering.3** Collection df is a good specificity signal but a weak altitude discriminator across the full range of generality: it orders specific terms well and general terms near-randomly.
  conf: repl (note: "Independently corroborated by Caraballo & Charniak (1999)") · class: not stated · holds: WordNet levels, and lower and upper levels of noun specificity in the corroborating study · src: johoDocumentFrequencyTerm2007, caraballoDeterminingSpecificityNouns1999 · trail: TSL §Verdict · from: TSL:R-0030, TSL:A-004..006
- **altitude-ordering.4** In taxonomy induction, different feature sets won at different abstraction levels (co-occurrence alone for abstract levels L2–L3; contextual, co-occurrence, pattern and syntactic features for concrete levels L4–L6), so no single fixed signal serves all altitudes; the framework abandons a single fixed altitude signal and learns a separate information function per abstraction level.
  conf: not stated · class: not stated · holds: is-a taxonomy induction, not cluster-label ordering (indirect); the confidence label is the harness's · src: yangMetricbasedFrameworkAutomatic2009 · rating: "Confidence: high (3-0)" · trail: TSL §2. How, §Verdict · from: TSL:B-0024..0026, TSL:B-0004, TSL:A-007
- **altitude-ordering.5** The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet and taxonomies, sound for those and indirect for ordering descriptive cluster labels, so the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.
  conf: not stated · class: not stated · holds: WordNet and is-a taxonomies · src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999 · trail: TSL §Standing caveats, §Verdict · from: TSL:B-0045, TSL:B-0046, TSL:A-015

### label-ordering: ordering descriptive cluster labels from general to specific
needs: altitude-ordering, class-df
- **label-ordering.1** No controlled head-to-head comparison exists of collection df, class df (c-TF-IDF) and IC for ordering descriptive cluster labels from general to specific; the closest tests are over WordNet and taxonomy induction, indirect for the label-ordering task.
  conf: not stated · class: search (note: "no controlled evidence found") · holds: the review's five search angles and 20 fetched sources · src: none (a search result) · search: searched, not found (note: "no controlled evidence found") · trail: TSL §Verdict, §Open Questions, §Term Specificity · from: TSL:A-014..016, TSL:B-0038, TSL:B-0039, TSL:B-0001
- **label-ordering.2** No reviewed source benchmarks discrete frequency bands for ordering labels.
  conf: not stated · class: search (note: "No reviewed source benchmarks discrete bands") · holds: the sources the review read · src: none (a statement about the reviewed sources) · search: not stated · trail: TSL §Verdict · from: TSL:A-012
- **label-ordering.3** The evidence favours continuous scoring for specificity: idf, IC and c-TF-IDF weights are all continuous.
  conf: not stated · class: not stated · holds: specificity signals for labelling · src: sparckjonesStatisticalInterpretationTerm1972, resnikUsingInformationContent1995, grootendorstBERTopicNeuralTopic2022 · trail: TSL §Verdict · from: TSL:A-010

### term-frequency-distributions: heavy-tailed term frequency distributions
needs: none
- **term-frequency-distributions.1** Term frequency distributions are heavy-tailed but not reliably Zipfian: a power law fitted best for only 5 of 24 corpora, 19 of 24 were better fit by a discrete Yule distribution, and a continuous GEV fitted best overall, especially in the sparse rare-term tail where Yule and power law fail, the region of rare, specific terms.
  conf: not stated · class: not stated · holds: 24 corpora (information retrieval); the confidence label is the harness's · src: petersenPowerLawDistributions2016 · rating: "Confidence: high (3-0)" · trail: TSL §3. Frequency · from: TSL:R-0015, TSL:B-0027, TSL:B-0028, TSL:B-0004
- **term-frequency-distributions.2** Low-frequency words are the majority of unique types.
  conf: not stated · class: not stated · holds: the corpora of the simulated-LDA pruning study · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §3. Frequency · from: TSL:B-0044, TSL:B-0029, TSL:B-0030

### frequency-banding: discrete frequency bands and cutoffs under heavy tails
needs: term-frequency-distributions
- **frequency-banding.1** Threshold bucketing is corpus-structure-dependent and unstable: the same 1% relative cutoff produced 9.3% vocabulary reduction in a corpus of few long documents against 74.1% in one of many short documents, and cutoffs above 4% can empty a short-text vocabulary.
  conf: single (note: "single simulated-corpus LDA study") · class: model (note: "one simulated-LDA Monte Carlo study") · holds: simulated LDA corpora; the bucketing/pruning evidence leans heavily on one study; the confidence label is the harness's · src: bystrovAnalysingImpactRemoving2023 · rating: "Confidence: high (3-0)" · trail: TSL §3. Frequency, §Verdict, §4. Minimum, §Standing caveats · from: TSL:B-0029, TSL:B-0031, TSL:B-0004, TSL:A-011, TSL:B-0034, TSL:B-0044
- **frequency-banding.2** Partial logarithmic binning is the proposed mitigation for recovering tail structure (Milojević 2010), but it is a proposal for distribution analysis, debated against MLE (Clauset, Shalizi, Newman), and not validated for label ordering or label banding.
  conf: not stated · class: not stated · holds: analysis of heavy-tailed distributions · src: milojevicPowerlawDistributionsInformation2010, clauset · trail: TSL §3. Frequency, §Verdict · from: TSL:B-0032, TSL:A-012

### minimum-support: minimum-support thresholds for vocabulary
needs: term-frequency-distributions
- **minimum-support.1** Minimum-support thresholds are standard practice: drop frequency-1 terms (Blei et al. 2003), discard terms in fewer than 0.5–1% of documents (Denny & Spirling 2018), and strip terms in more than 99% of documents as corpus stopwords (Grimmer & Stewart 2013; Maier et al. 2018); these are documented as conventions, not benchmarked optima, and the primary survey notes that "no systematic study" existed and tests only simulated LDA corpora.
  conf: not stated · class: not stated · holds: topic-model vocabulary preprocessing; the conventions are cited within [S7], the simulated-LDA pruning study; the confidence label is the harness's · src: bleiLatentDirichletAllocation2003 (cited within [S7]), dennyTextPreprocessingUnsupervised2018 (cited within [S7]), grimmerTextData2013 (cited within [S7]), maierApplyingLDASocial2018 (cited within [S7]) · rating: "Confidence: high (3-0)" · trail: TSL §Verdict, §4. Minimum, §References · from: TSL:B-0044, TSL:A-013, TSL:B-0033, TSL:B-0034, TSL:B-0004, TSL:R-0023
- **minimum-support.2** About 30% of vocabulary is removable without qualitative topic loss, independent of the pruning criterion (df, tf or TF-IDF).
  conf: single (note: "single simulated-corpus LDA study") · class: model (note: "single simulated-corpus LDA study") · holds: simulated LDA corpora; not shown on real corpora or non-LDA pipelines · src: bystrovAnalysingImpactRemoving2023 · trail: TSL §4. Minimum, §Standing caveats, §Open Questions · from: TSL:B-0033, TSL:B-0034, TSL:B-0044, TSL:B-0040, TSL:B-0041
- **minimum-support.3** Schofield et al. (2017) found that removing very-low-frequency terms has negligible impact, partly undermining the "too specific to matter" belief.
  conf: not stated · class: not stated · holds: stopword and very-low-frequency term removal in topic models · src: schofieldPullingOutStops2017 (cited within [S7]) · trail: TSL §4. Minimum, §References · from: TSL:R-0028, TSL:B-0035, TSL:R-0023

### not-covered: phrases and multilingual handling at the rare-term tail
needs: none
- **not-covered.1** Single-word against multi-word phrase selection, and stopword and multilingual handling at the rare-term tail, produced no surviving claims: their effect on rare-term specificity is unanswered by this corpus.
  conf: not stated · class: search (note: "no surviving claims") · holds: the review's source set · src: none (no evidence collected) · search: not stated · trail: TSL §5. Not covered, §Open Questions · from: TSL:B-0036, TSL:B-0037, TSL:B-0042

## Do not say

- **dns.1** "Specificity is a matter of term use (frequency), not meaning."
  why: The claim was killed in verification (vote 0-3): df is a proxy, not a definition of semantic specificity. · instead: collection-df.2 · trail: TSL §Refuted · from: TSL:C-001, TSL:B-0011
- **dns.2** "Document frequency as a measure of specificity was largely untested before Joho and Sanderson (2007)."
  why: The claim was killed in verification (vote 1-2). · instead: none · trail: TSL §Refuted · from: TSL:C-002
- **dns.3** "Extensive relative pruning of both frequent and infrequent terms does not compromise topic quality."
  why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted. · instead: minimum-support.1, minimum-support.2 · trail: TSL §Refuted, §4. Minimum · from: TSL:C-003, TSL:B-0034
- **dns.4** "Vocabulary pruning combined with document sampling boosts performance without loss of quality."
  why: The claim was killed in verification (vote 0-3), one of two claims that aggressive pruning is uniformly safe that were refuted. · instead: none · trail: TSL §Refuted, §4. Minimum · from: TSL:C-004, TSL:B-0034
- **dns.5** "The evidence favours collection df over class df or IC for ordering cluster labels from general to specific."
  why: No controlled head-to-head exists comparing collection df, class df and IC for ordering descriptive cluster labels, and the note says to report this as "no controlled evidence found," not as a point for any option. · instead: label-ordering.1 · trail: TSL §Verdict · from: TSL:A-014, TSL:A-016
- **dns.6** "c-TF-IDF down-weights terms that are spread across many classes."
  why: In c-TF-IDF, f_t is a frequency sum across classes, not a count of classes containing the term; the note calls the "spread across many classes" gloss the documentation's own simplification. · instead: class-df.2 · trail: TSL §1. Specificity · from: TSL:B-0017

## Gaps

- **gap.1** The review's answers were never checked by a second reader: its adversarial verification killed four claims, but no critic reviewed the answers, which rest on these figures: ~74–83% accuracy at the bottom two WordNet levels against ~55–68% for general terms, ~86% against 45.5% at lower and upper levels, 9.3% against 74.1% vocabulary reduction from the same relative cutoff, cutoffs above 4% emptying a short-text vocabulary, and the <0.5–1% and >99% document-frequency conventions.
  blocks: altitude-ordering, frequency-banding, minimum-support · origin: no critic: the critique is refutations only (3-vote adversarial verification of 25 of 91 extracted claims, 21 confirmed, 4 killed) · search: not stated · from: TSL:A-004, TSL:A-005, TSL:A-011, TSL:A-013, TSL:B-0001
- **gap.2** A controlled head-to-head of collection df, class df (c-TF-IDF) and IC for ordering cluster labels from general to specific.
  blocks: label-ordering · origin: the note's core open question; it appears not done · search: searched, not found (note: "no controlled evidence found") · from: TSL:B-0038, TSL:B-0039, TSL:A-014, TSL:A-016
- **gap.3** Whether the bucketing instabilities (9.3% against 74.1%) and the ~30%-removable finding hold on real corpora and non-LDA pipelines (for example BERTopic c-TF-IDF); the primary evidence is one simulated-LDA study.
  blocks: frequency-banding, minimum-support · origin: the note's open questions · search: not stated · src: bystrovAnalysingImpactRemoving2023 · from: TSL:B-0040, TSL:B-0041
- **gap.4** The effect of single- against multi-word phrase selection, and of stopword and multilingual handling, on rare-term specificity (brief item 5).
  blocks: not-covered · origin: the note's not-covered section and open questions · search: not stated · from: TSL:B-0036, TSL:B-0037, TSL:B-0042
- **gap.5** Whether log binning or a rank transform actually improves label ordering in practice, or only distribution visualisation and fitting.
  blocks: frequency-banding · origin: the note's open questions · search: not stated · src: milojevicPowerlawDistributionsInformation2010 · from: TSL:B-0043, TSL:A-012
- **gap.6** The supporting conventions set (Blei, Denny & Spirling, Grimmer & Stewart, Maier, Schofield) and Caraballo & Charniak have author and page metadata resolved partly from secondary listings, to be verified against their DOI or venue records.
  blocks: minimum-support, altitude-ordering · origin: the note's reference caveat · search: not stated · from: TSL:R-0031

## Out of scope

- TSL:A-001: the review's choice among the brief's options (routing, not a finding; its qualification is in the claims)
- TSL:A-017: the brief's routing flag (routing, not a finding)

## Sources

```bibtex
@article{sparckjonesStatisticalInterpretationTerm1972,
  author = {Spärck Jones, K.},
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
  note = {access: not stated; cited as: TSL [S2] (with Resnik 1999); the note gives arXiv:cmp-lg/9511007 but links cmp-lg/9709008}
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
  note = {access: not stated; cited as: TSL [S2] (with Resnik 1995)}
}

@misc{grootendorstBERTopicNeuralTopic2022,
  author = {Grootendorst, M.},
  title = {BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
  year = {2022},
  eprint = {2203.05794},
  url = {https://arxiv.org/abs/2203.05794},
  note = {access: not stated; type: preprint (arXiv); cited as: TSL [S3] (with the c-TF-IDF documentation)}
}

@misc{bertopicCTFIDFDocumentation,
  author = {{BERTopic}},
  title = {c-TF-IDF documentation},
  url = {https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html},
  note = {access: not stated; type: software documentation; incomplete: author, year; cited as: TSL [S3] (with Grootendorst 2022)}
}

@inproceedings{johoDocumentFrequencyTerm2007,
  author = {Joho, H. and Sanderson, M.},
  title = {Document frequency and term specificity},
  booktitle = {RIAO 2007 (Large-Scale Semantic Access to Content)},
  year = {2007},
  doi = {10.5555/1931390.1931425},
  url = {https://www.dcs.gla.ac.uk/~hideo/pub/riao07/riao07.pdf},
  note = {access: not stated; incomplete: pages; cited as: TSL [S4]}
}

@inproceedings{yangMetricbasedFrameworkAutomatic2009,
  author = {Yang, H. and Callan, J.},
  title = {A Metric-based Framework for Automatic Taxonomy Induction},
  booktitle = {Proceedings of ACL-IJCNLP 2009},
  year = {2009},
  pages = {271--279},
  url = {https://www.cs.cmu.edu/~callan/Papers/acl09-huiyang.pdf},
  note = {access: not stated; cited as: TSL [S5]}
}

@article{petersenPowerLawDistributions2016,
  author = {Petersen, C. and Simonsen, J. G. and Lioma, C.},
  title = {Power Law Distributions in Information Retrieval},
  journal = {ACM Transactions on Information Systems},
  year = {2016},
  volume = {34},
  number = {2},
  pages = {8},
  doi = {10.1145/2816815},
  note = {access: not stated; cited as: TSL [S6]}
}

@misc{bystrovAnalysingImpactRemoving2023,
  author = {Bystrov, V. and Naboka-Krell, V. and Staszewska-Bystrova, A. and Winker, P.},
  title = {Analysing the Impact of Removing Infrequent Words on Topic Quality in LDA Models},
  year = {2023},
  eprint = {2311.14505},
  url = {https://arxiv.org/pdf/2311.14505},
  note = {access: not stated; type: preprint (arXiv), published in Central European Journal of Economic Modelling and Econometrics (2025); incomplete: volume, pages of the published version; cited as: TSL [S7]}
}

@article{milojevicPowerlawDistributionsInformation2010,
  author = {Milojević, S.},
  title = {Power-law Distributions in Information Science — Making the Case for Logarithmic Binning},
  journal = {JASIST},
  year = {2010},
  volume = {61},
  number = {12},
  pages = {2417--2425},
  doi = {10.1002/asi.21426},
  eprint = {1011.1533},
  note = {access: not stated; cited as: TSL [S7b]}
}

@article{bleiLatentDirichletAllocation2003,
  author = {Blei, D. M. and Ng, A. Y. and Jordan, M. I.},
  title = {Latent Dirichlet Allocation},
  journal = {JMLR},
  year = {2003},
  volume = {3},
  pages = {993--1022},
  note = {access: secondary (supporting conventions cited within [S7]; metadata partly from secondary listings, to verify); cited as: TSL [S8]}
}

@article{dennyTextPreprocessingUnsupervised2018,
  author = {Denny, M. J. and Spirling, A.},
  title = {Text Preprocessing for Unsupervised Learning: Why It Matters, When It Misleads, and What to Do about It},
  journal = {Political Analysis},
  year = {2018},
  volume = {26},
  number = {2},
  pages = {168--189},
  note = {access: secondary (supporting conventions cited within [S7]; metadata partly from secondary listings, to verify); cited as: TSL [S8]}
}

@article{grimmerTextData2013,
  author = {Grimmer, J. and Stewart, B. M.},
  title = {Text as Data},
  journal = {Political Analysis},
  year = {2013},
  volume = {21},
  number = {3},
  pages = {267--297},
  note = {access: secondary (supporting conventions cited within [S7]; metadata partly from secondary listings, to verify); cited as: TSL [S8]}
}

@article{maierApplyingLDASocial2018,
  author = {Maier, D. and others},
  title = {Applying LDA to Social Science Research},
  journal = {Communication Methods and Measures},
  year = {2018},
  volume = {12},
  number = {2--3},
  pages = {93--118},
  note = {access: secondary (supporting conventions cited within [S7]; metadata partly from secondary listings, to verify); incomplete: author; cited as: TSL [S8]}
}

@inproceedings{schofieldPullingOutStops2017,
  author = {Schofield, A. and Magnusson, M. and Mimno, D.},
  title = {Pulling Out the Stops: Rethinking Stopword Removal for Topic Models},
  booktitle = {EACL 2017},
  year = {2017},
  pages = {432--436},
  note = {access: secondary (supporting conventions cited within [S7]; metadata partly from secondary listings, to verify); cited as: TSL [S8]}
}

@inproceedings{caraballoDeterminingSpecificityNouns1999,
  author = {Caraballo, S. A. and Charniak, E.},
  title = {Determining the Specificity of Nouns from Text},
  booktitle = {EMNLP/VLC-99},
  year = {1999},
  pages = {63--70},
  note = {access: not stated; type: corroborating (not primary); metadata partly from secondary listings, to verify; cited as: TSL References, corroborating}
}

@misc{clauset,
  author = {Clauset and Shalizi and Newman},
  note = {access: not stated; incomplete: title, year, venue, author given names; named in the body only (log binning debated against MLE), not in the reference list; cited as: TSL §3}
}

@article{millerWordNetLexicalDatabase1995,
  author = {Miller, George A.},
  title = {WordNet: a lexical database for English},
  journal = {Communications of the ACM},
  year = {1995},
  volume = {38},
  number = {11},
  pages = {39--41},
  doi = {10.1145/219717.219748},
  note = {background}
}
```
