# Notes on writing the piece

## 1. Wanted or needed, not in the material

- **A concrete example.** The material has no worked example of a term being scored or two labels being ordered. The soil-microbe / "ammonia oxidation" opening is mine, purely illustrative. A real pair from one of the studies (e.g. a WordNet parent-child pair and its two df values) would have been better.
- **What WordNet is.** Used throughout as the test bed but never described. I called it "the hierarchy of English words most of this work uses", inferred from context. How many levels it has, and how "bottom two levels" and "general terms" were defined in Joho & Sanderson, is not given.
- **The idf formula.** The material names idf but gives no formula, so the piece describes it only in words.
- **The constant A in c-TF-IDF.** log(1 + A/f_t) is quoted with A undefined. I wrote the factor out without saying what A is.
- **What "information function" means** in Yang & Callan. I translated it as "a separate scoring function for each level", which may be looser than their usage.
- **Chance level for the df test.** The material calls 55-68% "near-random" without stating the baseline. I assumed a pairwise choice with a 50% baseline. That fits Caraballo & Charniak's 45.5% (below chance), but the material never says so.
- **Why df fails at the general end.** The material reports the failure and gives no explanation. I drafted one and cut it as unsupported.
- **The cutoff in the 9.3% vs 74.1% result.** One passage says "same relative cutoff", another "same 1% cutoff". Whether that means 1% of documents (a df threshold) or something else is not stated. I wrote "the same relative document-frequency cutoff" and left the number out.
- **Corpus details for Bystrov et al.** Real or simulated for the 9.3%/74.1% figures? The material says the evidence is "a single simulated-corpus LDA study" but labels the two corpora only by document length.
- **What "topic quality" was measured by**, behind the ~30%-removable finding.
- **Evidence on ordering cluster labels specifically.** The material says outright that none exists. That gap is the piece's main limitation, and I report it as such.
- **Phrases vs single words, and multilingual/stopword handling at the rare tail.** Flagged as uncovered, so the piece only mentions them as untested.
- **Authors' first names.** Not in the material. I used surnames only.

## 2. Hard to use in the material

- **Pipeline jargon written for the person who commissioned it.** Vote tallies ("3-0", "1-2"), "killed" claims, "confidence: high", "altitude", "band-collapse question", and a verdict picking option "(a)" over "(b)" with a "(c)-flavoured nuance". Options (a)-(c) are defined in a brief I don't have, so (c) is never explained.
- **Inconsistent accuracy figures for Joho & Sanderson.** The verdict gives "~74-83%" at the bottom two levels; section 2 gives "~74% overall". I reported both as overall vs bottom-level, which is my reading.
- **Tension between pruning claims.** "~30% of vocabulary removable without qualitative topic loss" sits beside a refuted claim that "extensive relative pruning doesn't compromise topic quality". The boundary between the two (how much is too much) is not stated. I kept the 30% figure and said the stronger claim did not survive checking.
- **The Schofield et al. (2017) sentence.** "Removing very-low-frequency terms has negligible impact, partly undermining the 'too specific to matter' belief". The direction of the argument is unclear, and the cited paper's title is about stopwords, not rare terms. I left it out.
- **Secondhand conventions.** The [S8] minimum-support conventions are "cited within [S7]", not checked against the originals, and the footnote warns that author and page metadata are partly unverified.
- **Reference metadata mismatch.** Resnik [S2] lists arXiv:cmp-lg/9511007 but links cmp-lg/9709008.
- **The refuted claim about df's history.** "df-as-specificity was largely untested before Joho & Sanderson 2007" was refuted, yet the verdict calls Joho & Sanderson "the only direct empirical test". I kept the piece neutral on priority and called it "the most direct test".
- **BM25, PMI, burstiness.** Named as present in the sources but with nothing usable said about them, so they're left out.
