# Blind comparison: piece A vs piece B

Both pieces are about 1,270 words, so length is not a factor. They draw on the same evidence base and share most of their numbers: the 74% / 74–83% / 55–68% ordering result, Caraballo and Charniak's 86% / 45.5%, Petersen's 5 of 24 corpora, the 9.3% / 74.1% cutoff result, the ~30% pruning result. Most of the differences are in order, attribution and what each does with the facts.

## 1. Coverage: points one has and the other lacks

**In A, not in B**

- **Attribution throughout.** A names Joho and Sanderson (2007) for the direct ordering test, Bystrov and colleagues (2023) for the cutoff and pruning results, Blei et al., Denny and Spirling, Grimmer and Stewart, and Maier et al. for the pruning conventions, Milojević (2010) for logarithmic binning, and dates Resnik (1995, 1999). B leaves the central ordering test unattributed ("The direct test ..."), and the same goes for the cutoff study ("In one study"), the pruning survey ("The survey that examined them") and the binning proposal. Resnik is undated. A reader who wants to follow anything up can do so from A and mostly can't from B.
- **Why the c-TF-IDF total-count detail matters.** Both say the down-weighting uses a total count of occurrences, not the number of clusters containing the term. Only A gives the consequence: a term concentrated in one cluster is penalised about as much as one spread thinly across many. That is the point a labeller needs, because it works against exactly the cluster-specific terms you want.
- **How Resnik's P(c) is estimated.** A says it is estimated by counting occurrences of the concept and of everything beneath it, which is what makes the monotonicity argument concrete. B gets to the same place ("a parent's count includes all its children's counts") but less explicitly.
- **The c-TF-IDF formula** (log(1 + A/f)). It is a partial gain at best, since A never defines A (see section 2).
- **Linking the distribution-fitting result to specificity.** A says the rare tail, where power-law and Yule fits break down, "is exactly where the specific terms live." B gives the same fit results but doesn't say why the tail matters for specificity.

**In B, not in A**

- **Other weighting signals.** B notes that BM25's saturating term frequency, pointwise mutual information and burstiness appear in the literature with no verified link to specificity. A is silent on them, which leaves the reader unsure whether they were looked at.
- **Transfer as an open question.** B asks whether the pruning and banding results, drawn from simulated LDA corpora, carry over to real corpora and to tools like BERTopic. A raises the simulated-corpora limit for pruning but not the transfer question, and not for banding.
- **The pruning survey's own admission** that no systematic study of pruning had existed before it.
- **A sharper account of binning.** B says logarithmic binning is disputed specifically against maximum-likelihood fitting. A says only that it is "contested".
- **The specific cutoff value** (1%). A says "the same relative document-frequency cutoff" without giving the number.
- **Tying the frequency weakness back to the task.** B says frequency is weakest "exactly where the top of a multi-level label gets built." A states the weakness but leaves the reader to make that connection.
- **The documentation claim.** B says BERTopic's own documentation blurs the total-count versus cluster-count distinction.
- **The null result framed as neutral.** B points out that the missing head-to-head comparison favours none of the three signals and counts against none.
- **Zipf by name**, and the fact that rare words make up most of the distinct vocabulary.

**In scope, but missing from both**

The research question names graph-based keyphrase extraction, faceted tagging and topic-model labelling beyond c-TF-IDF. Neither piece says anything about the first two, and neither says whether the research found nothing on them or simply left them out. Both answer the "multi-level systems" half of the question only through Resnik's information content and Yang and Callan's per-level scoring. Neither describes how a working hierarchical labelling system actually assigns terms to levels, for example top-down versus bottom-up, or choosing a parent's label by contrast with its siblings. If the research found nothing on these, one sentence saying so would close the gap in either piece.

## 2. Clarity for a literate outsider

**A**

- The order of sections works: two measures, then the test of whether rarity orders terms, then the move from words to clusters, then bands, pruning and gaps. Each section builds on the one before.
- The opening example (nested soil-microbe groups, "Microbiology" above "ammonia oxidation") is concrete. It also fits hierarchical labelling better than B's framing.
- "log(1 + A/f)": f is defined, A is not. An outside reader will stop at this. Either define A (the average number of words per cluster, in BERTopic) or drop the formula.
- "did not survive checking" (pruning section) reads like a trace of how the piece was written. Checking by whom? The reader has no referent. B has the same phrase.
- Pruning section: Bystrov first appears as the source of the cutoff results, and later the pruning evidence is said to come "mainly from one study of simulated corpora". The reader has to work out that this is the same study, and so whether the 9.3% / 74.1% figures are from simulated corpora too. A says neither.
- The closing paragraph is a useful summary for this reader, though it repeats points made only a few paragraphs earlier.

**B**

- The order of sections is harder to follow. c-TF-IDF comes before the evidence on whether frequency orders terms at all. Worse, the information-content section already asserts that document frequency and information content "have the strongest direct evidence behind them, and they agree with each other", before any evidence has been shown. The reader is handed the conclusion first and the support two sections later.
- "Altitude" turns into a working term ("a principled scale of altitude", "no verified link to altitude", "every altitude") without ever being introduced as one. It is easy to guess from context, but it reads like insider shorthand.
- "That absence counts for none of the three signals and against none" is mannered. Most readers will need to read it twice.
- "The direct test ..." points to a study the reader is never told the name of, so it reads as if the source were withheld.
- The WordNet definition, including the "is-a" gloss, is clearer for an outsider than A's.
- The coin-toss sentence is more careful than A's (see section 3).

## 3. Missing, wrong, inconsistent or overclaimed

**A**

- "at the general end document frequency is not much better than a coin": this fits 55% but not 68%. B's "the lower end of that range is not far above a coin toss" is accurate.
- "The literature on the first is old and solid": a mild overclaim. The piece itself then shows the main specificity proxy is a weak guide among general terms and that c-TF-IDF has never been validated. "Old and well established" would be accurate. "Solid" claims more than the piece goes on to show.
- Caraballo and Charniak's 45.5% at upper levels is *below* chance. A calls it "the same pattern more sharply" without saying that it is worse than guessing. B has the same omission.
- The undefined A in the formula (see section 2).

**B**

- **Internal inconsistency.** In "Bands or a continuous scale?", B lists "idf, information content and c-TF-IDF weights" as "the signals with the best support". Two sections earlier it said nobody has benchmarked c-TF-IDF as a specificity measure. A avoids this by saying only that "all the measures above give continuous scores".
- **Unsupported claim.** Document frequency and information content "agree with each other". No evidence for this agreement appears anywhere in the piece.
- **Overclaim.** "The first question has several well-tested answers." The piece's own evidence supports one well-tested proxy (document frequency, tested only on WordNet pairs), one principled construction (information content), and one untested engineering variant (c-TF-IDF).
- **An assumption presented as fact.** "One word is rarely enough. A useful label runs from broad to narrow." This is a design position about multi-term labels, stated without support. It also frames "multi-level labelling" as a broad-to-narrow string inside a single label, rather than as labels on nested groups, which is the more usual reading.
- Same "did not survive checking" problem as A.
- Same silence on the below-chance 45.5%.

## 4. Which I would give the reader

I would give the reader A, and the margin is moderate rather than large. A is the more trustworthy piece. Its argument runs in a sensible order, its claims are attributed so the reader can follow them up, and it has no internal contradiction. Its point about c-TF-IDF's total count penalising cluster-specific terms is the most useful practical insight in either piece. B has the better gaps section (BM25, PMI and burstiness, transfer from simulated corpora), the more accurate coin-toss sentence, and a nice link between frequency's weakness and the top of a label. Those don't make up for unattributed central results, a conclusion stated before its evidence, and calling c-TF-IDF well supported after saying it was never tested. A would get clearly better with two fixes: define A in the formula and replace "did not survive checking". Adding B's sentence on BM25, PMI and burstiness would help too.
