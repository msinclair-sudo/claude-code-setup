# How specific is a word? Ordering labels from general to specific

Say you have sorted ten thousand abstracts into groups, and the groups nest: a broad group about soil microbes contains a narrower one about nitrogen cycling, which contains a narrower one still. Each group needs a label, and the labels should sit at the right height. "Microbiology" belongs near the top, "ammonia oxidation" further down. Getting this right takes two things: a number that says how specific a term is, and some evidence that sorting terms by that number puts them in the right order. The literature on the first is old and solid. The literature on the second is thinner than you might expect.

## Rarity as a stand-in for specificity

The founding idea comes from information retrieval. Spärck Jones (1972) proposed weighting search terms by their document frequency, the number of documents in a collection that contain the term. A term that turns up in few documents is treated as more specific, so a match on it counts for more than a match on a term that turns up everywhere. This inverse relationship is the "idf" (inverse document frequency) in the familiar TF-IDF weighting.

Document frequency is a proxy, and it fails in predictable ways. A typo, an optical-character-recognition error or a sample identifier can be extremely rare without meaning anything specific. Rarity is evidence of specificity, not a definition of it.

## Information content: specificity with a built-in order

Resnik (1995, 1999) worked from a different starting point: a taxonomy, a hierarchy in which every concept is a kind of its parent. He estimated the probability P(c) of meeting a concept c in a corpus by counting occurrences of the concept and of everything beneath it. The information content of the concept is then IC(c) = −log P(c). The root of the hierarchy covers everything, so its probability is 1 and its information content is 0. Specific concepts near the leaves have low probability and high information content.

What makes this attractive for ordering is that a parent's count includes all its children's counts. Probability therefore can never fall as you move up the hierarchy, and information content can never rise. The ordering from general to specific is guaranteed by construction. The cost is that you need the hierarchy first, with a single root at the top; WordNet, the hierarchy of English words most of this work uses, does not have one naturally, so one has to be added.

## Does rarity actually put terms in order?

The most direct test is by Joho and Sanderson (2007). They took pairs of words from WordNet where one is the parent of the other and asked whether the more general word has the higher document frequency. Overall it did about 74% of the time. That average hides a split. Among the most specific terms, in the bottom two levels of the hierarchy, accuracy was roughly 74–83%. Among general terms it fell to 55–68%. For a choice between two words, guessing gets half right, so at the general end document frequency is not much better than a coin. An earlier study by Caraballo and Charniak (1999) found the same pattern more sharply: about 86% correct at the lower levels and 45.5% at the upper ones.

So document frequency tells specific terms apart well and general terms apart badly.

Yang and Callan (2009), building taxonomies automatically, reached a compatible conclusion from another direction. The evidence that worked best differed by level. Word co-occurrence alone served for the abstract upper levels; the concrete lower levels needed co-occurrence combined with surrounding context, lexical patterns and syntax. Their framework learns a separate scoring function for each level of abstraction rather than trusting one signal across the whole range.

## From words to groups of documents

Labelling clusters adds a step: you want the terms that characterise one group against the others. The widely used BERTopic method (Grootendorst, 2022) does this with a class-based TF-IDF. Each cluster is treated as a single document. A term's frequency within the cluster is normalised so that large clusters do not dominate, then multiplied by a factor of the form log(1 + A/f), where f is the term's total frequency summed across all clusters. Terms that are frequent across the collection get pushed down.

Two cautions. First, f is a total count, not the number of clusters the term appears in, so a term that is very frequent inside one cluster is penalised much like one spread thinly across many. Second, class-based TF-IDF is an engineering application of the inverse-frequency idea. Nobody has tested it as a measure of specificity in its own right.

## Continuous scores versus frequency bands

It is tempting to sort terms into bands such as common, middling and rare, and to assign labels by band. The shape of word-frequency distributions makes this fragile. Frequencies are heavy-tailed, with a few very common words and a long tail of rare ones, but the tail is not reliably the textbook power law. Petersen and colleagues (2016) found a power law fit best in only 5 of 24 corpora. The discrete Yule distribution fitted 19 of them better, and a continuous generalised extreme value distribution fitted best overall, especially in the sparse rare-term tail where power-law and Yule fits break down. That tail is exactly where the specific terms live.

Fixed cutoffs behave differently from corpus to corpus. Bystrov and colleagues (2023) applied the same relative document-frequency cutoff to different corpora. It removed 9.3% of the vocabulary from a corpus of a few long documents and 74.1% from one of many short documents, and cutoffs above 4% could empty a short-text vocabulary altogether. Logarithmic binning has been proposed as a better way to study heavy-tailed distributions (Milojević, 2010), but it is contested even for that purpose and has never been tested for ordering labels. All the measures above give continuous scores, and the evidence favours keeping them continuous.

## Minimum support

Before scoring, most pipelines discard terms with too little support. The usual rules are to drop terms that occur only once (Blei and colleagues, 2003), to drop terms found in fewer than 0.5–1% of documents (Denny and Spirling, 2018), and to treat terms found in more than 99% of documents as corpus-specific stopwords (Grimmer and Stewart, 2013; Maier and colleagues, 2018). Bystrov and colleagues found that about 30% of a vocabulary could be removed without a visible loss of topic quality, whichever frequency measure was used to choose what went.

These are conventions, not tested optima. The pruning evidence comes mainly from one study of simulated corpora under a single topic model, latent Dirichlet allocation, and the stronger claim that heavy pruning is always harmless did not survive checking.

## What has not been tested

No one appears to have compared collection document frequency, cluster-based frequency and information content head-to-head on the task that matters here: ordering descriptive cluster labels from general to specific. Every ordering result above comes from word hierarchies such as WordNet, which is sound for those hierarchies and indirect for cluster labels. Whether single words or multi-word phrases make better labels, and how stopwords and multilingual text affect the rare tail, went unaddressed in the work reviewed.

What can be said is modest. Information content gives a guaranteed general-to-specific order when a hierarchy exists. Document frequency is a good guide among specific terms and a poor one among general terms. Class-based TF-IDF is reasonable engineering with no validation as a specificity measure. Continuous scores hold up better than fixed bands, and the standard pruning thresholds are habits that have not been benchmarked.
