## collection-df.1 (claim)

Collection document frequency (df, idf) is the seminal specificity signal (Spärck Jones 1972): terms are weighted by collection frequency so that matches on rarer, more specific terms count for more, and specificity is inversely related to df (lower df = more specific); but df is a frequency proxy, not a definition of semantic specificity, and low df from typos, OCR or identifiers does not imply true specificity.

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

## information-content.1 (claim)

Information content IC(c) = −log P(c) in an is-a taxonomy (Resnik 1995/1999) gives general concepts high P and low IC (root P = 1, IC = 0) and specific concepts low P and high IC; P(c) is monotonically nondecreasing up the taxonomy by construction (a parent cumulatively subsumes its children's counts), so altitude maps directly onto generality; it needs a unified root, and WordNet has none naturally.

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

## information-content.3 (claim)

Information content needs a unified root, and WordNet has none naturally.

- conf: not stated
- class: not stated
- holds: is-a taxonomies, WordNet
- src: resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §1. Specificity

From the note:

> TSL:A-002 [Verdict] The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> TSL:B-0012 [1. Specificity signals the field uses] - **Information content IC(c) = −log P(c)** [S2] — Resnik (1995/1999): general concepts have high P, low IC (root P=1, IC=0); specific concepts low P, high IC.
>
> TSL:B-0015 [1. Specificity signals the field uses] *Confidence: high (3-0).* Caveat: needs a unified root; WordNet has none naturally.
>

## class-df.1 (claim)

Class-based TF-IDF (c-TF-IDF, BERTopic; Grootendorst 2022) treats each cluster as one document, L1-normalises term frequency for cluster size and down-weights via log(1 + A/f_t), operationalising the inverse-frequency principle at the cluster level, but it is an engineering instantiation, not an independently validated specificity measure.

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

## altitude-ordering.5 (claim)

The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet and taxonomies, sound for those and indirect for ordering descriptive cluster labels, so the verdict's altitude claim rests on principled monotonicity (IC) plus indirect empirical support.

- conf: not stated
- class: not stated
- holds: WordNet and is-a taxonomies
- src: johoDocumentFrequencyTerm2007, yangMetricbasedFrameworkAutomatic2009, resnikUsingInformationContent1995, resnikSemanticSimilarityTaxonomy1999
- trail: TSL §Standing caveats, §Verdict

From the note:

> TSL:A-002 [Verdict] The strongest, most direct primary evidence establishes two foundational, mutually consistent signals: **collection df / idf** (lower df = more specific) [S1] and **information content IC(c) = −log P(c)** in an is-a taxonomy, where corpus probability is monotonic up the hierarchy so altitude maps directly onto generality [S2].
>
> TSL:B-0026 [2. How multi-level systems order general→specific] Indirect:* this is is-a taxonomy induction, not cluster-label ordering.
>
> TSL:B-0045 [Standing caveats on the corpus] The altitude-axis evidence (Joho & Sanderson; Yang & Callan; Resnik) is over WordNet/taxonomies — sound for those, *indirect* for descriptive cluster-label ordering.
>
> TSL:B-0046 [Standing caveats on the corpus] The verdict's altitude claim therefore rests on principled monotonicity (IC) plus indirect empirical support, with the direct label-ordering head-to-head genuinely absent.
>
> TSL:A-015 [Verdict] The closest tests [S4, S5] are over WordNet / taxonomy induction — indirect for the label-ordering task.
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
> TSL:R-0024 [References] *Latent Dirichlet Allocation.* JMLR, 3, 993–1022. · Denny, M. J., & Spirling, A. (2018).
>
> TSL:R-0025 [References] *Text Preprocessing for Unsupervised Learning: Why It Matters, When It Misleads, and What to Do about It.* Political Analysis, 26(2), 168–189. · Grimmer, J., & Stewart, B. M. (2013).
>
> TSL:R-0026 [References] *Text as Data.* Political Analysis, 21(3), 267–297. · Maier, D., et al. (2018).
>
> TSL:R-0027 [References] *Applying LDA to Social Science Research.* Communication Methods and Measures, 12(2–3), 93–118. · Schofield, A., Magnusson, M., & Mimno, D. (2017).
>
> TSL:R-0028 [References] *Pulling Out the Stops: Rethinking Stopword Removal for Topic Models.* EACL 2017, 432–436.
>

Not found in the cited text (where to look, not what is wrong): holds: in

