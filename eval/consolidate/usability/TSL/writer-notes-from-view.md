# Notes on writing the piece

## 1. Wanted or needed, and not in the material

- **How a multi-level labeller actually builds a general-to-specific sequence.** The question asks this directly, but the material only gives signals (df, IC, c-TF-IDF) and one taxonomy-induction method (Yang & Callan). There is no worked description of any hierarchical or multi-granular labelling system choosing a term per level, so the "how they order terms" half of the piece rests on IC monotonicity and the WordNet tests, not on labelling systems.
- **Graph-based keyphrase extraction, topic-model labelling and faceted tagging.** Named in the question, absent from the answer and the concepts. I could not say anything about them.
- **What the 74% / 74–83% / 55–68% accuracy measures.** I read it as "for a WordNet parent-child pair, the parent has the higher df", with 50% as chance, but the material never says so. "Near-random" for 68% also needed that reading to make sense (and 68% is not really near random; I hedged to "the lower end").
- **Who ran the direct df test.** The figures are not attributed. Joho & Sanderson are named elsewhere as one of the "closest tests", so they are probably the source, but I could not confirm it and left the test unattributed.
- **Which WordNet levels are "the bottom two" and what Yang & Callan's L2–L6 are.** No definition of the level numbering, so I wrote "abstract" and "concrete" levels.
- **What Caraballo & Charniak (1999) were testing.** Only the numbers and "same pattern" are given.
- **The c-TF-IDF formula's A.** log(1 + A/f_t) is given but A is never defined. I described the weight qualitatively.
- **How P(c) is estimated and how the missing WordNet root is handled in practice.** "IC needs a unified root; WordNet has none naturally" is stated with no fix.
- **The study behind 9.3% vs 74.1%.** Not named. The Gaps section implies it is the same simulated-LDA study as the pruning survey, but this is not stated outright; I said "in one study" and later "simulated topic models".
- **Exactly what a "1% relative cutoff" removes** (terms below 1% of documents? above?). Not stated; I kept the wording generic.
- **Full references.** Only author-year (sometimes author only: Milojević 2010, Petersen et al. 2016, Denny & Spirling, Maier et al.). No titles or venues, so a reader cannot follow anything up. First names (e.g. for Spärck Jones, Resnik) are not given and I left them out.
- **A concrete example of a general and a specific term.** None in the material. I used "disease" ... "influenza" as an illustration of my own; it makes no claim about WordNet or any source.
- **Expansions I supplied from general knowledge:** OCR (optical character recognition) and LDA (latent Dirichlet allocation). The WordNet gloss came from the material's own background line, which it flags as not from the research.

## 2. Hard to use in the material

- **The D1 answer is written against a brief the reader never sees.** "(a)", "(b)", "(c)-flavoured nuance", "the band-collapse question the brief's routing flagged" all refer to options in an absent brief. I had to reconstruct what the options were to know what "not (b) group-df alone" meant.
- **Dense bold-heavy answer paragraph.** Everything in D1 is repeated, slightly differently, in the Concepts section; the two had to be read against each other to see they say the same thing (e.g. the 74% overall figure appears only in Concepts).
- **Standing brackets are sparse.** Only four claims carry one (three `single`, one `repl`). Most claims, including the c-TF-IDF and threshold ones, have no standing, so I could not tell how firm they are beyond the prose.
- **Schofield et al. (2017).** "Removing very-low-frequency terms has negligible impact, partly undermining the 'too specific to matter' belief" reads backwards: negligible impact from removing rare terms would seem to support the idea that they do not matter. I could not work out the intended point and left it out.
- **"Do not say" entries without a replacement.** "df-as-specificity was largely untested before Joho & Sanderson 2007" was killed 1-2, with no "say instead" and no explanation of what was wrong (the date? "untested"?). It also left me unsure whether the 2007 date is safe to use, so I avoided it. Same for the "pruning + sampling boosts performance" claim.
- **"No controlled head-to-head exists" vs "Apparently not done".** The answer states it flatly; the Gaps section hedges. I went with "nobody appears to have run".
- **BM25, PMI, burstiness.** Named in the question and dismissed in one line ("no surviving verified claim"), with no hint whether that means the sources found nothing or the claims failed checking. I could only list them as unlinked.
- **"Limited by access"** is defined in the header but never used, which made me wonder whether something was missing.
