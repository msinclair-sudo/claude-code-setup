---
type: knowledge
title: Positioning graph nodes that lack features
inputs:
  - GHOST: PhD/biblion/research/results/ghost-node-positioning-result.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---

# Positioning graph nodes that lack features

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
| GHOST | [[ghost-node-positioning-result]] | yes | bracket keys | no | no | fallback |

## Concepts

### gnn: graph neural networks and graph convolutional networks
needs: none
- **gnn.bg1** A graph convolutional network (GCN) is a convolutional neural network variant that operates directly on graph-structured data and learns node representations that encode both local graph structure and node features; it was introduced for semi-supervised node classification.
  kind: background · ref: kipfSemiSupervisedClassificationGraph2017 · check: arXiv:1609.02907 resolves (ICLR 2017 conference paper); stated in the abstract

### homophily: homophily in networks
needs: none
- **homophily.bg1** Homophily is the principle that similarity breeds connection: ties form more often between similar than between dissimilar members of a network.
  kind: background · ref: mcphersonBirdsFeatherHomophily2001 · check: DOI 10.1146/annurev.soc.27.1.415 resolves on Crossref; stated in the abstract ("Similarity breeds connection")

### missingness: the process that causes missing data
needs: none
- **missingness.bg1** Whether the process that causes missing data can be ignored in inference depends on conditions on that process, among them that the missing data are "missing at random" and the observed data "observed at random".
  kind: background · ref: rubinInferenceMissingData1976 · check: DOI 10.1093/biomet/63.3.581 resolves on Crossref; stated in the summary on the publisher's abstract page

### attribute-missing-graph: graphs whose nodes carry edges but lack feature vectors
needs: gnn
- **attribute-missing-graph.1** Existing graph learning methods, including the popular GNN, "cannot provide satisfied learning performance since they are not specified for attribute-missing graphs".
  conf: not stated · class: not stated · holds: attribute-missing graphs, as Chen et al. state it; the note gives no measurement or setting · src: chenLearningAttributeMissingGraphs2022 · trail: GHOST §5. Bounding · from: GHOST:B-0039
- **attribute-missing-graph.2** The review sorts the field's strategies for featureless nodes as "two families plus a model-internal approach", and lists four: neighbour feature propagation / diffusion imputation, model-internal imputation, structure-only / positional embedding, and dynamic / joint reconstruction.
  conf: not stated · class: not stated · holds: the review's reading of its 21 fetched sources · src: none (the reviewer's synthesis) · trail: GHOST §1. Strategies · from: GHOST:B-0008, GHOST:B-0009, GHOST:B-0013, GHOST:B-0015, GHOST:B-0017, GHOST:B-0001

### feature-propagation: neighbour feature propagation (diffusion imputation)
needs: attribute-missing-graph, homophily
- **feature-propagation.1** Feature Propagation (FP) minimises Dirichlet energy, giving a diffusion-type PDE on the graph whose discretisation reconstructs missing features from observed neighbours: a simple, fast, scalable algorithm.
  conf: not stated · class: not stated · holds: its motivating setting is the partially-attributed / cold-start case ("age and gender available only for a small subset of users") · src: rossiUnreasonableEffectivenessFeature2022 · rating: "Confidence: high (3-0)" · trail: GHOST §1. Strategies · from: GHOST:B-0009, GHOST:B-0011, GHOST:B-0012
- **feature-propagation.2** FP rests on a feature-homophily assumption and degrades on heterophilous graphs.
  conf: not stated · class: not stated · holds: given as a caveat of R1 · src: rossiUnreasonableEffectivenessFeature2022 (caveat) · trail: GHOST §2. Degradation · from: GHOST:B-0030
- **feature-propagation.3** FP outperformed prior missing-feature methods on its seven benchmarks.
  conf: not stated · class: not stated · holds: seven benchmarks, 2022; homophilous + sparse + MCAR, and mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022 · trail: GHOST §2. Degradation · from: GHOST:B-0020, GHOST:B-0029
- **feature-propagation.4** FP is now a baseline, superseded as state of the art by PCFI, DART and others; that it outperforms previous methods is a 2022 historical fact.
  conf: not stated · class: not stated · holds: the field as the review read it; PCFI and DART are named without references · src: none (the note cites nothing for it) · trail: GHOST §2. Degradation, §Standing caveats · from: GHOST:B-0021, GHOST:B-0052

### model-internal-imputation: imputation inside the model (GCNMF)
needs: gnn, attribute-missing-graph
- **model-internal-imputation.1** GCNMF folds Gaussian-mixture imputation inside a GCN.
  conf: not stated · class: not stated · holds: a method description; no setting given · src: chenLearningAttributeMissingGraphs2022 · trail: GHOST §1. Strategies · from: GHOST:B-0013

### joint-reconstruction: dynamic / joint reconstruction of attributes and structure
needs: attribute-missing-graph
- **joint-reconstruction.1** "Attribute-missing graph" methods jointly reconstruct attributes and update structure via alternating optimisation (EGS), rather than fixed mean/zero imputation on a static graph.
  conf: not stated · class: not stated · holds: a method description; no setting given · src: chenLearningAttributeMissingGraphs2022, songDynamicGraphStructure2025 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §1. Strategies · from: GHOST:B-0017, GHOST:B-0018

### missingness-degradation: degradation as the featureless fraction rises
needs: feature-propagation, model-internal-imputation, joint-reconstruction, homophily, missingness
- **missingness-degradation.1** On homophilous, sparse-feature graphs under MCAR missingness, diffusion / propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally, ~2–4% relative node-classification accuracy at 99% missing, while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark.
  conf: repl (note: "The single most replicated empirical result") · class: meas (note: "empirical result") · holds: only the homophilous-sparse-MCAR-scoped version survived verification (the critic, against R7); the ~2–4% range is the note's own, spanning R1 and R2 · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, chenLearningAttributeMissingGraphs2022 · trail: GHOST §Verdict, §critic · from: GHOST:A-002, GHOST:C-001
- **missingness-degradation.2** FP loses on average ~4% relative node-classification accuracy at 99% missing across seven benchmarks.
  conf: not stated · class: not stated · holds: seven benchmarks; homophilous + sparse + MCAR, and mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022 · trail: GHOST §2. Degradation · from: GHOST:B-0020, GHOST:B-0029
- **missingness-degradation.3** SGHFP (a hypergraph variant of feature propagation) loses on average 2.67% relative accuracy at 99% missing across four datasets: Cora 81.23→79.41 (−2.25%), Photo 91.73→87.73 (−4.36%, the worst case), PubMed 77.36→74.29 (−3.97%).
  conf: not stated · class: not stated · holds: four datasets, 99% missing; per-dataset figures verified from Table 2; homophilous + sparse + MCAR, and mostly author-reported · src: leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0)" · trail: GHOST §2. Degradation · from: GHOST:B-0022, GHOST:B-0023, GHOST:B-0029
- **missingness-degradation.4** At 99% missing on Cora, propagation reaches ~78–79% accuracy.
  conf: not stated · class: not stated · holds: Cora, 99% missing; homophilous + sparse + MCAR, and mostly author-reported · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §2. Degradation · from: GHOST:B-0024, GHOST:B-0026, GHOST:B-0029
- **missingness-degradation.5** At 99% missing on Cora, GCNMF reaches 34.54% accuracy; GCNMF is the strategy that fails badly under high missingness.
  conf: repl (note: "confirmed by two independent papers") · class: not stated · holds: Cora, 99% missing; homophilous + sparse + MCAR · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §2. Degradation, §1. Strategies · from: GHOST:B-0024, GHOST:B-0014, GHOST:B-0026, GHOST:B-0029
- **missingness-degradation.6** At 99% missing on Cora, PaGNN sits at ~58%: low, but not the catastrophic collapse of GCNMF.
  conf: not stated · class: not stated · holds: Cora, 99% missing; homophilous + sparse + MCAR, and mostly author-reported · src: chenLearningAttributeMissingGraphs2022 · rating: "Confidence: high (3-0 / 2-1)" · trail: GHOST §2. Degradation · from: GHOST:B-0024, GHOST:B-0025, GHOST:B-0026, GHOST:B-0029
- **missingness-degradation.7** EGS degrades gently against a PAGNN baseline: on Cora from 5% to 75% missing, the baseline goes from 81.36 to 74.05 and EGS from 84.77 to 82.13.
  conf: not stated · class: not stated · holds: Cora, 5% to 75% missing; self-reported by the method's authors · src: songDynamicGraphStructure2025 (self-reported) · rating: "Confidence: high." · trail: GHOST §2. Degradation · from: GHOST:B-0027, GHOST:B-0028, GHOST:B-0029

### benchmark-regime: the regime the robustness results come from
needs: missingness-degradation, homophily, missingness
- **benchmark-regime.1** The robustness numbers are regime-bound: they are measured almost entirely on homophilous, sparse bag-of-words citation / co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors.
  conf: not stated · class: not stated · holds: the propagation, SGHFP and EGS results the review gathered · src: rossiUnreasonableEffectivenessFeature2022, leiSelfsupervisedGuidedHypergraph2023, songDynamicGraphStructure2025 · trail: GHOST §Verdict, §2. Degradation · from: GHOST:A-005, GHOST:B-0029
- **benchmark-regime.2** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison": on standard benchmarks the models cannot be distinguished.
  conf: not stated · class: deriv (note: "provably bounds") · holds: standard sparse-feature benchmarks; R7 is a January 2026 arXiv preprint, under review · src: ferriniRethinkingGNNsMissing2026 (under review) · trail: GHOST §Verdict, §5. Bounding · from: GHOST:A-006, GHOST:B-0038, GHOST:B-0050
- **benchmark-regime.3** The dominance of propagation on standard benchmarks may be an artefact of the benchmarks, not a regime-general property.
  conf: not stated · class: reading (note: "so the dominance of propagation on standard benchmarks may be an artifact") · holds: the review's inference from R7's result on sparse benchmarks · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Verdict · from: GHOST:A-006
- **benchmark-regime.4** Dense-feature and non-MCAR (MNAR) missingness regimes are under-evaluated.
  conf: not stated · class: not stated · holds: the benchmarks in use as of R7 (2026) · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §5. Bounding · from: GHOST:B-0038
- **benchmark-regime.5** Ferrini et al. argue that standard benchmarks cannot answer whether propagation robustness survives on dense features and MNAR missingness, and introduce new evaluation protocols; cross-method results under them are not yet established.
  conf: not stated · class: not stated · holds: R7, a 2026 preprint under review · src: ferriniRethinkingGNNsMissing2026 · trail: GHOST §Open Questions · from: GHOST:B-0046, GHOST:B-0047, GHOST:B-0050

### low-variance-defect: the low-variance defect of propagation
needs: feature-propagation
- **low-variance-defect.1** Propagation produces low-variance, near-constant channels that contribute little downstream.
  conf: repl (note: "independently corroborated at a second venue") · class: meas/deriv (note: "established with empirical evidence and a theoretical proof") · holds: R5 (ICML 2025) and R6 (ICLR 2025 track), both among the 2025–2026 preprints / under-review sources · src: umPropagateInjectRevisiting2025, anonymousLowVarianceBottleneck2025 · trail: GHOST §Verdict, §5. Bounding · from: GHOST:A-007, GHOST:B-0036, GHOST:B-0050
- **low-variance-defect.2** The low-variance defect bounds, but does not refute, propagation: the high-variance channels do the work.
  conf: not stated · class: not stated · holds: the review's reading of R5 and R6 · src: none (the reviewer's synthesis) · trail: GHOST §5. Bounding · from: GHOST:B-0037

### structure-only-embedding: structure-only / positional embedding
needs: none
- **structure-only-embedding.1** A distinct family of methods consumes only topology (LLE, Laplacian Eigenmaps, Graph Factorisation, GraRep, HOPE, DeepWalk, node2vec, SDNE, DNGR, LINE), operating on adjacency / similarity matrices; attribute-joint methods are treated as a separate, newer line.
  conf: not stated · class: not stated · holds: the taxonomy of a 2018 survey; the topology-only characterisation of those classical methods remains accurate, but the field has expanded since · src: goyalGraphEmbeddingTechniques2018 · rating: "Confidence: high (3-0)" · trail: GHOST §1. Strategies, §Standing caveats · from: GHOST:B-0015, GHOST:B-0016, GHOST:B-0051
- **structure-only-embedding.2** Structure-only embeddings are regime-dependent with no single winner: higher-order-proximity methods generally win, but node2vec leads on node classification yet loses on a structured SBM graph where labels reflect communities and there is no structural equivalence between nodes.
  conf: not stated · class: not stated · holds: the 2018 survey's comparisons; the field has expanded since · src: goyalGraphEmbeddingTechniques2018, srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019 · trail: GHOST §5. Bounding, §Verdict · from: GHOST:B-0040, GHOST:A-008, GHOST:B-0051

### positional-structural: positional versus structural node representations
needs: structure-only-embedding, gnn
- **positional-structural.1** GNNs cannot capture position when node features are absent or identical: structurally isomorphic but positionally distinct nodes get identical embeddings.
  conf: not stated · class: not stated · holds: strictly true in the featureless / identical-feature regime · src: youPositionawareGraphNeural2019 · trail: GHOST §5. Bounding · from: GHOST:B-0041
- **positional-structural.2** Positional node embeddings are formally samples from a G-equivariant distribution whose expectation is the structural representation; only this formal sampling relationship and its direction (positional = samples of structural) survived verification.
  conf: not stated · class: deriv (note: "formally samples") · holds: a formal relationship; the claim that the two are practically interchangeable for tasks was killed · src: srinivasanEquivalencePositionalNode2020 · trail: GHOST §5. Bounding, §critic · from: GHOST:B-0042, GHOST:C-002
- **positional-structural.3** The strategy of laying out topology separately and then mapping it onto attribute space surfaced only as the conceptual positional-vs-structural distinction, not as a benchmarked layout pipeline.
  conf: not stated · class: search (note: "surfaced only as the conceptual positional-vs-structural distinction") · holds: the review's search (5 search angles, 21 sources fetched) · src: srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019 · trail: GHOST §1. Strategies · from: GHOST:B-0019, GHOST:B-0001

### contamination: whether featureless nodes distort the clusters of feature-bearing nodes
needs: feature-propagation, structure-only-embedding
- **contamination.1** No controlled benchmark was found that measures whether imputed or structure-only nodes contaminate the clusters of feature-bearing nodes.
  conf: not stated · class: search (note: "No controlled head-to-head was found") · holds: the review's search (5 search angles, 21 sources fetched) · src: none (a search result) · trail: GHOST §Verdict, §3. Contamination · from: GHOST:A-009, GHOST:B-0031, GHOST:B-0001
- **contamination.2** Song et al. argue, by molecular-graph analogy, that severe missingness "can alter the semantic information of the graph, leading to changes in the graph structure", which is why they update structure jointly; this is a theoretical / motivational statement, not a measured demonstration.
  conf: not stated · class: assert (note: "theoretical/motivational statement") · holds: a motivational argument by analogy to molecular graphs; no measurement · src: songDynamicGraphStructure2025 (indirect and motivational) · rating: "verification vote 2-1" · trail: GHOST §3. Contamination · from: GHOST:B-0031, GHOST:B-0032, GHOST:B-0033

### layout-distortion: layout distortion on mixed populations
needs: structure-only-embedding, positional-structural
- **layout-distortion.1** No reviewed source measured layout distortion (centroid piling, hub collapse) from topology-only node placement on mixed attributed / featureless populations; the visualisation search angle returned sources, but none yielded a confirmed claim.
  conf: not stated · class: search (note: "No reviewed source measured this") · holds: the review's retrieved corpus, including its visualisation search angle · src: none (a search result) · trail: GHOST §Verdict, §4. Layout · from: GHOST:A-009, GHOST:B-0034

### default-strategy: which strategy the evidence supports as a default
needs: missingness-degradation, benchmark-regime, low-variance-defect, structure-only-embedding
- **default-strategy.1** The review's verdict is (c), regime-dependent: neighbour feature propagation is a defensible default only in the homophilous, sparse-feature regime where its robustness has been demonstrated; outside that regime the evidence does not support it as a default, and structure-only / positional embedding becomes a live alternative.
  conf: not stated · class: reading (note: "So propagation is the right default where the graph is homophilous and features are sparse") · holds: the review's reading of its evidence; the brief's options (a) propagation and (b) structure-only / positional embedding · src: goyalGraphEmbeddingTechniques2018, srinivasanEquivalencePositionalNode2020, youPositionawareGraphNeural2019 · trail: GHOST §Verdict · from: GHOST:A-001, GHOST:A-008

## Do not say

- **dns.1** "FP robustness (~4% at 99% missing) is a general fact."
  why: killed in verification (vote 1-2); the unscoped version fails, and only the homophilous-sparse-MCAR-scoped version survives (R1, contra R7) · instead: missingness-degradation.1, missingness-degradation.2, benchmark-regime.1 · trail: GHOST §critic · from: GHOST:C-001, GHOST:B-0003
- **dns.2** "Positional and structural representations are practically interchangeable for tasks."
  why: killed in verification (vote 0-3); only the formal sampling relationship and its direction survived · instead: positional-structural.2 · trail: GHOST §critic · from: GHOST:C-002, GHOST:B-0003
- **dns.3** The propagation results are "a clean win for option (a)".
  why: the note says it is not, for three reasons the verification confirmed: the numbers are regime-bound, the benchmark hides the differences, and propagation has a low-variance defect · instead: default-strategy.1, benchmark-regime.1, benchmark-regime.2, low-variance-defect.1 · trail: GHOST §Verdict · from: GHOST:A-003, GHOST:A-004
- **dns.4** The absence of evidence on contamination and layout distortion as "a point in favour of any option".
  why: the note says to report it as "no controlled evidence found" · instead: contamination.1, layout-distortion.1 · trail: GHOST §Verdict · from: GHOST:A-010
- **dns.5** Song et al. as "a measured demonstration that featureless nodes distort feature-bearing nodes' clusters".
  why: the note says it is a theoretical / motivational statement and to cite it as indirect only · instead: contamination.2 · trail: GHOST §3. Contamination · from: GHOST:B-0032, GHOST:B-0033
- **dns.6** "FP outperforms previous methods", said of the present.
  why: the note says it is a 2022 historical fact, not current SOTA; FP is now a baseline · instead: feature-propagation.3, feature-propagation.4 · trail: GHOST §Standing caveats, §2. Degradation · from: GHOST:B-0052, GHOST:B-0021

## Gaps

- **gap.1** Whether inserting imputed or structure-only nodes measurably distorts the clusters of feature-bearing nodes: no controlled mixed-population benchmark was found.
  blocks: contamination · origin: open question the review says the literature leaves unanswered (brief item 3) · from: GHOST:B-0043, GHOST:B-0044
- **gap.2** Layout distortion (centroid piling, hub collapse) on mixed attributed / featureless populations: unmeasured in the retrieved corpus.
  blocks: layout-distortion · origin: open question the review says the literature leaves unanswered (brief item 4) · from: GHOST:B-0035, GHOST:B-0045
- **gap.3** Whether propagation robustness survives on dense, semantically meaningful features and structural / feature-dependent (MNAR) missingness; cross-method results under Ferrini et al.'s protocols are not yet established.
  blocks: benchmark-regime, missingness-degradation, default-strategy · origin: open question; R7 under review · src: ferriniRethinkingGNNsMissing2026 · from: GHOST:B-0046, GHOST:B-0047
- **gap.4** The crossover point: at what featureless fraction or graph sparsity neighbour aggregation becomes too sparse to help and loses to structure-only embedding; degradation is quantified within propagation but never located against structure-only baselines across regimes.
  blocks: default-strategy, missingness-degradation, structure-only-embedding · origin: open question · from: GHOST:B-0048, GHOST:B-0049
- **gap.5** The note contradicts itself on how many strategies the field uses: it says "The literature splits cleanly into two families plus a model-internal approach", then lists four (adding "Dynamic / joint reconstruction").
  blocks: attribute-missing-graph.2 · origin: a note that contradicts itself · from: GHOST:B-0008, GHOST:B-0017

## Out of scope

## Sources

```bibtex
@inproceedings{rossiUnreasonableEffectivenessFeature2022,
  author = {Rossi, E. and Kenlay, H. and Gorinova, M. I. and Chamberlain, B. P. and Dong, X. and Bronstein, M. M.},
  title = {On the Unreasonable Effectiveness of Feature Propagation in Learning on Graphs with Missing Node Features},
  booktitle = {Proceedings of the First Learning on Graphs Conference (LoG 2022)},
  series = {PMLR},
  volume = {198},
  pages = {11:1--11:16},
  year = {2022},
  eprint = {2111.12128},
  archiveprefix = {arXiv},
  url = {https://proceedings.mlr.press/v198/rossi22a.html},
  note = {access: not stated; cited as: GHOST [R1]}
}

@inproceedings{leiSelfsupervisedGuidedHypergraph2023,
  author = {Lei, C. and Fu, J. and Wang, X. and Qiu, X. and Hu, Z. and Peng, Y. and You, J.},
  title = {Self-supervised Guided Hypergraph Feature Propagation for Semi-supervised Classification with Missing Node Features},
  booktitle = {ICASSP 2023 -- IEEE International Conference on Acoustics, Speech and Signal Processing},
  year = {2023},
  eprint = {2302.08250},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2302.08250},
  note = {access: not stated (verified per-dataset from Table 2); cited as: GHOST [R2]; incomplete: pages}
}

@article{chenLearningAttributeMissingGraphs2022,
  author = {Chen, X. and Chen, S. and Yao, J. and Zheng, H. and Zhang, Y. and Tsang, I. W.},
  title = {Learning on Attribute-Missing Graphs},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume = {44},
  number = {2},
  pages = {740--757},
  year = {2022},
  doi = {10.1109/TPAMI.2020.3032189},
  eprint = {2011.01623},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2011.01623},
  note = {access: not stated; cited as: GHOST [R3]}
}

@article{songDynamicGraphStructure2025,
  author = {Song and others},
  title = {Dynamic graph structure evolution for node classification with missing attributes},
  journal = {Scientific Reports},
  volume = {15},
  year = {2025},
  doi = {10.1038/s41598-025-09840-z},
  url = {https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12264138/},
  note = {access: not stated; cited as: GHOST [R4]; PMC12264138; incomplete: author (the note gives "Song, [et al.], Zhou, Wang, Liu" and says the list is partial), pages}
}

@inproceedings{umPropagateInjectRevisiting2025,
  author = {Um, D. and Kim, J. and Park and others},
  title = {Propagate and Inject: Revisiting Propagation-Based Feature Imputation for Graphs with Partially Observed Features},
  booktitle = {ICML 2025},
  year = {2025},
  url = {https://openreview.net/forum?id=QfKrcgyase},
  note = {access: not stated; type: 2025--2026 preprint / under review (the note's standing caveats); cited as: GHOST [R5]; OpenReview id=QfKrcgyase; code: github.com/daehoum1/fisf; incomplete: author (the note gives "Um, D., Kim, J., Park, [et al.], Lim, Ahn, Park" and says the list is partial), pages}
}

@misc{anonymousLowVarianceBottleneck2025,
  author = {Anonymous},
  title = {Low Variance: A Bottleneck in Diffusion-Based Graph Imputation},
  howpublished = {ICLR 2025 track, OpenReview id=4dhTYe5pjD},
  year = {2025},
  url = {https://openreview.net/forum?id=4dhTYe5pjD},
  note = {access: not stated; type: 2025--2026 preprint / under review (the note's standing caveats); cited as: GHOST [R6]; incomplete: author}
}

@misc{ferriniRethinkingGNNsMissing2026,
  author = {Ferrini, F. and Lachi, V. and Longa, A. and Lepri, B. and Akiyoshi and others},
  title = {Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution},
  year = {2026},
  eprint = {2601.04855},
  archiveprefix = {arXiv},
  howpublished = {arXiv:2601.04855 (Jan 2026; under review, OpenReview gvFOB8VCMr)},
  url = {https://arxiv.org/abs/2601.04855},
  note = {access: not stated; type: 2025--2026 preprint / under review (the note's standing caveats); cited as: GHOST [R7]; incomplete: author (the note gives "Ferrini, F., Lachi, V., Longa, A., Lepri, B., Akiyoshi, [et al.], Passerini, A., Liu, Jaeger" and says the list is partial)}
}

@article{goyalGraphEmbeddingTechniques2018,
  author = {Goyal, P. and Ferrara, E.},
  title = {Graph Embedding Techniques, Applications, and Performance: A Survey},
  journal = {Knowledge-Based Systems},
  volume = {151},
  pages = {78--94},
  year = {2018},
  doi = {10.1016/j.knosys.2018.03.022},
  eprint = {1705.02801},
  archiveprefix = {arXiv},
  url = {https://doi.org/10.1016/j.knosys.2018.03.022},
  note = {access: not stated; cited as: GHOST [R8]}
}

@inproceedings{srinivasanEquivalencePositionalNode2020,
  author = {Srinivasan, B. and Ribeiro, B.},
  title = {On the Equivalence between Positional Node Embeddings and Structural Graph Representations},
  booktitle = {ICLR 2020},
  year = {2020},
  eprint = {1910.00452},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/1910.00452},
  note = {access: not stated; cited as: GHOST [R9]}
}

@inproceedings{youPositionawareGraphNeural2019,
  author = {You, J. and Ying, R. and Leskovec, J.},
  title = {Position-aware Graph Neural Networks (P-GNN)},
  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML 2019)},
  series = {PMLR},
  volume = {97},
  year = {2019},
  eprint = {1906.04817},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/1906.04817},
  note = {access: not stated; cited as: GHOST [R10]; incomplete: pages}
}

@inproceedings{kipfSemiSupervisedClassificationGraph2017,
  author = {Kipf, Thomas N. and Welling, Max},
  title = {Semi-Supervised Classification with Graph Convolutional Networks},
  booktitle = {International Conference on Learning Representations (ICLR 2017)},
  year = {2017},
  eprint = {1609.02907},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/1609.02907},
  note = {background}
}

@article{mcphersonBirdsFeatherHomophily2001,
  author = {McPherson, Miller and Smith-Lovin, Lynn and Cook, James M.},
  title = {Birds of a Feather: Homophily in Social Networks},
  journal = {Annual Review of Sociology},
  volume = {27},
  number = {1},
  pages = {415--444},
  year = {2001},
  doi = {10.1146/annurev.soc.27.1.415},
  note = {background}
}

@article{rubinInferenceMissingData1976,
  author = {Rubin, Donald B.},
  title = {Inference and missing data},
  journal = {Biometrika},
  volume = {63},
  number = {3},
  pages = {581--592},
  year = {1976},
  doi = {10.1093/biomet/63.3.581},
  note = {background}
}
```
