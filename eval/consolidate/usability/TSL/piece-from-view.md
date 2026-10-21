# How labelling methods judge whether a word is general or specific

Suppose you have clustered a few thousand documents and want to name each cluster. One word is rarely enough. A useful label runs from broad to narrow, so a reader sees first what field a cluster belongs to and then what it is actually about, the way "disease" might head a label that ends in "influenza". To build one, a method has to decide two things about every candidate term: how specific it is, and where it sits relative to the other terms. The first question has several well-tested answers. The second has far fewer.

## Rarity as a stand-in for specificity

The oldest and most widely used signal is document frequency: the number of documents in the whole collection that contain a term. Spärck Jones proposed in 1972 that matches on rarer terms should count for more, because rarer terms tend to be more specific. Her inverse document frequency (idf) weight puts that into practice, and it still underlies most term-weighting schemes. The rule is simple: the fewer documents a term appears in, the more specific it is taken to be.

This is a proxy with an obvious failure. A word can be rare because it is a typo, an optical-character-recognition error or an identifier code, none of which makes it specific. Frequency describes how a term is used; it does not define specificity.

## Information content: position in a hierarchy

A second signal comes from work on lexical taxonomies, chiefly WordNet, a machine-readable database of English words organised into "is-a" hierarchies (a parent concept subsumes its children). Resnik defined the information content of a concept as IC(c) = −log P(c), where P(c) is the probability of encountering that concept in a corpus. Because a parent's count includes all its children's counts, P(c) can only stay level or rise as you climb the hierarchy. The root has a probability of 1 and an information content of 0. General concepts have high probability and low information content; specific ones the reverse.

That built-in monotonicity is what makes information content attractive for ordering. Height in the taxonomy and generality line up by construction, giving a principled scale of altitude that raw document frequency lacks. The catch is that the measure needs a single root to sum into, and WordNet does not naturally have one. Of all the specificity signals, these two, document frequency and information content, have the strongest direct evidence behind them, and they agree with each other.

## The cluster-level version

Methods that label clusters often move the frequency idea from documents to groups. The best-known current example is class-based TF-IDF (c-TF-IDF), used in the BERTopic topic-modelling tool (Grootendorst, 2022). It treats each cluster as if it were one large document, normalises term frequencies so that big clusters do not dominate, and down-weights each term with a logarithmic factor based on its frequency summed across all clusters. That frequency is a total count of occurrences, not a count of how many clusters contain the term, a distinction the tool's own documentation blurs.

c-TF-IDF is a sensible engineering application of the inverse-frequency principle. Nobody has benchmarked it as a measure of specificity, though, and no study has compared it head to head with collection frequency or information content.

## How well does frequency order terms?

The direct test of whether document frequency orders terms correctly used parent-child pairs from WordNet, where the right answer is known. Overall, frequency put about 74% of pairs in the right order. The success was not spread evenly. Near the bottom of the hierarchy, in its two most specific levels, accuracy was roughly 74–83%. Higher up, among general terms, it fell to about 55–68%; for a choice between two terms, the lower end of that range is not far above a coin toss. Caraballo and Charniak (1999) found the same shape independently: about 86% correct at lower levels and 45.5% at upper ones.

Frequency, then, separates a narrow term from a slightly broader one reasonably well, and struggles to tell one broad term from another, which is exactly where the top of a multi-level label gets built.

One response is to stop looking for a single signal. Yang and Callan (2009), building taxonomies automatically, learned a separate scoring function for each level of abstraction. Different evidence won at different heights: co-occurrence statistics alone worked best at the abstract levels, while the concrete levels needed contextual, co-occurrence, pattern-based and syntactic features combined. Their result suggests that no one fixed measure serves every altitude.

## Bands or a continuous scale?

A tempting shortcut is to sort terms into frequency bands, such as common, middling and rare, and assign each band a level in the label. The trouble is the shape of the data. Term frequencies are heavily skewed, with a long tail of rare words that make up most of the distinct vocabulary. They are often described as following Zipf's power law, but Petersen and colleagues (2016) found a power law fitted best in only 5 of 24 corpora. A discrete Yule distribution fitted 19 of them better, and a continuous generalised extreme value distribution did best overall, particularly in the rare-word tail.

Under skew like this, cutoffs behave unpredictably. In one study the same relative cutoff, 1%, shrank the vocabulary by 9.3% in a collection of a few long documents and by 74.1% in one of many short documents. Cutoffs above 4% could remove a short-text vocabulary entirely. Nobody appears to have tested frequency bands as a way of ordering labels. Logarithmic binning has been proposed for recovering the structure of the tail, but that proposal concerns analysing distributions, remains disputed against maximum-likelihood fitting, and has not been tried for labels.

The signals with the best support, namely idf, information content and c-TF-IDF weights, are all continuous scores. The evidence points towards ranking terms on a continuous scale rather than binning them.

## Pruning the vocabulary first

Almost every pipeline discards some terms before scoring: words that occur only once, terms found in fewer than about 0.5–1% of documents, and terms found in more than 99%, which are treated as collection-specific stopwords. These are conventions, not tested optima. The survey that examined them noted that no systematic study had existed, and its own tests used only simulated corpora for one kind of topic model (latent Dirichlet allocation). In those tests about 30% of a vocabulary could go without visible loss of topic quality, whichever criterion chose what went. Claims that heavier pruning is safe across the board did not survive checking.

## What is not known

Other familiar weighting signals, including BM25's saturating term-frequency curve, pointwise mutual information and measures of how "bursty" a term's occurrences are, turn up in this literature without any verified link to altitude. Whether the pruning and banding results carry over from simulated topic models to real corpora and to tools like BERTopic is untested. So is how choosing multi-word phrases over single words, or handling stopwords and several languages, changes the specificity of rare terms.

The gap that matters most for labelling is plainer still. Nobody appears to have run a controlled comparison of collection frequency, cluster-level frequency and information content as ways of ordering cluster labels from general to specific. The nearest evidence comes from WordNet and taxonomy construction, related tasks but not the same one. That absence counts for none of the three signals and against none. What a method has in the meantime is a principled altitude scale in information content, wherever a taxonomy exists, and a frequency signal that can be trusted at the specific end and much less at the general one.
