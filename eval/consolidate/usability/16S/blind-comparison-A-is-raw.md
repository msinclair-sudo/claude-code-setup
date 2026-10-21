# Blind comparison: 16S pieces A and B

Both pieces are about 1,280 words and both follow the brief's three parts in order. They share most of their evidence: mock communities always come out wrong, the 35-cycle gut mock is off by 2.6-fold, SAR11 is under-counted more in seawater than in mocks, copy number runs from 1 to about 15 (21 to 22 in databases), correction fits worse than no correction on ten mocks, the fixed-efficiency model rests on one seven-taxon dataset, the dilution series (contaminant reads 0.1% to 80.1%, ASVs 18 to 381), soil replicates at 160,000 reads, load varying tenfold to six orders of magnitude, 100-fold depth differences, fourteen differential-abundance methods calling 0.8% to 40.5% significant, and spike-in recovery of 40% to 84%. The differences are in what each adds around that core, and in how each closes.

## 1. Coverage: points one has and the other lacks

**In A, not in B**
- Reads track gene copies, not cells, and a cell can carry one to hundreds of genome copies depending on growth phase. B covers copy number per genome only, and leaves the reader to work out that reads are not cell counts.
- Why copy-number correction fails: predictions break down beyond about 15% sequence divergence, and about half of known OTUs sit further than that.
- Chimeras as a measured share of reads: 0.9% to 18.2% at 30 cycles, depending on the polymerase.
- Index misassignment quantified (a fraction of a percent to several percent, mostly measured outside 16S), with the mechanism: abundant taxa show up falsely in other samples.
- Pipelines disagree far more on how many units there are than on the relative abundances of the expected taxa. This supports A's split between the two kinds of error.
- A single extraction figure (up to 36.6-fold, 5.5-fold on average), plus a counter-case in which two extraction methods gave very similar results.
- More on the rarefying dispute: repeated rarefying held false positives at 5% when depth differed between groups; the earlier opposing simulation's design has been disputed; and there is a statistical argument that rarefied richness is biased.
- The alternatives to rarefying, each with its catch: proportions and log-ratio distances stay depth-sensitive; RNA-seq scaling methods assume most taxa do not change; Chao1 breaks when denoising tools drop singletons. B never mentions log-ratio (compositional) methods or scaling normalisation.
- How load-measurement methods disagree: qPCR and flow cytometry matched on a mock but diverged on stool.
- A closing ranking that follows from the bias model (a change in the ratio of two taxa is best protected, proportions across very different communities less so, richness and rare taxa least), a flag on low-biomass samples, and a question the reader can put to any paper: does the difference survive a change of normalisation?

**In B, not in A**
- The variable regions V1 to V9, the full-length option, PacBio, and read lengths (250 or 300 bases paired).
- The workflow set out as twelve named steps, six at the bench and six on the computer, with the choices at each. Example tools and databases are named: DADA2, Deblur, UNOISE3, SILVA, Greengenes, RDP, GTDB.
- A more precise account of the controls survey: 265 papers in two named journals, 2018, 30% reporting negative controls and 10% positive. It also notes that nobody has measured how often each choice is made across the field.
- Taxa that go missing, not just extra ones: Verrucomicrobia appeared in stool with some primer pairs and not others.
- An absolute example of inflation: about 20 expected taxa became 1,607 to 5,824 OTUs.
- Harder bead beating raised Gram-positive DNA by up to 400% in activated sludge.
- Copy number by taxon: Bacillota about 7, Acidobacteriota about 1.4. It also notes that the database maxima have not been checked against assembly quality.
- The ordering extraction > PCR > sequencing, with the warning that it should not be taken as general.
- The calibration result (Bray-Curtis error dropped from 0.35 to 0.08), plus the spike-in recovery and the cycle effects in four stool samples, presented as evidence against consistent bias.
- Run-level failure: one run lost an archaeal mock member from every sample. Plus the plain summary that abundant taxa replicate well and rare ones do not.
- How depth affects each diversity index: observed richness, Chao1 and ACE rise with depth; Shannon less so; inverse Simpson not at all.
- Chao's estimator ranked a community with twenty times fewer species as ten times richer.
- What the earlier rarefying benchmark actually found: high false-positive rates in differential-abundance tests.
- A concrete reversal from measuring load: the gut Bacteroides–Prevotella trade-off turned out to be an artefact of relative data.
- The observation that no approach has been shown to handle depth, load and taxon bias together.

## 2. Clarity for a scientifically literate outsider

**A**
- The opening ("It looks like a census. It is closer to a heavily processed poll") gives the reader a frame that the rest of the piece fills in. The split into proportions, which taxa, sampling noise and load is easy to hold onto.
- The sampling-noise paragraph is hard to reconcile. It says replicates "shared only a sixth to a third of their OTUs, yet weighted by abundance they overlapped 95% at 160,000 reads". Then it says presence-absence overlap "levelled off below 45% however deep the sequencing". A reader takes these to be the same replicates and can't tell whether the overlap at 160,000 reads was 17–33% or about 44%. They are probably different datasets or depths, but the text doesn't say so.
- The rarefying paragraph is dense, and a little slippery. It introduces "rarefying" as a single subsample, then credits "averaging over many such subsamples" as the method that worked. A quick reader may think plain rarefying was endorsed. "Removed the link between depth and both richness and between-sample distances" is awkward. "An influential earlier simulation reached the opposite verdict" doesn't say what that verdict was.
- The fixed-efficiency model is stated abstractly ("the error in a taxon's proportion shifts in size and even direction with whatever else is present"). It is the piece's central idea, and a three-taxon toy example would have landed it.
- "Denoising tools" appears in the Chao1 sentence, but the piece introduced ASVs only as "inferred by modelling sequencing error" and never connected the two terms.
- "Load" is introduced in the trust section and measured in the comparison section, so the thread is split.

**B**
- The twelve-step tour is complete but reads as a list. The tool and database names (DADA2, Deblur, UNOISE3, SILVA, Greengenes, RDP, GTDB, FTA cards) mean nothing to this reader and add weight without adding understanding.
- It uses more undefined measures: Bray-Curtis dissimilarity (0.35 to 0.08 means nothing without a scale), ACE, Shannon, inverse Simpson.
- "Uncorrected data fitted the truth 7.1% better": 7.1% of what? The figure looks precise but can't be interpreted.
- The Chao example ("ranked a community with twenty times fewer species as ten times richer") is striking, but it has no context, so the reader can't tell whether it was a contrived edge case or a typical failure.
- The rarefying paragraph presents a dispute but sets two findings on different outcomes against each other: false positives in differential-abundance tests, and the link between depth and diversity. The reader learns that rarefying is "contested" but not what the disagreement is about. Neither piece gives the most intuitive objection, that rarefying throws away reads.
- The bias-consistency section is clearer than A's. It explains why proportions shift ("because a proportion depends on what else is present") and then sets the evidence for consistency against the evidence against it, in one place.
- Separating the two soil replicate studies ("Technical replicates ... shared only a third"; "In deeply sequenced replicates of one soil ... near 44%") avoids the confusion A has.

## 3. Missing, wrong, inconsistent or overclaimed

**A**
- The replicate figures above are unclear and look inconsistent (a sixth to a third shared, against presence-absence overlap levelling off below 45%).
- It claims measuring load "has reversed conclusions" but gives no example. B does.
- "Every step has several accepted options, and the field has settled few of them" is a slightly stronger claim than the evidence the piece cites. B's version is more careful: the steps are agreed, the choices aren't, and how often each choice is made hasn't been measured.
- The closing calls the ratio of two taxa "the best-protected quantity". That fits A's model, but A has just said stool and field data show bias varying between samples. "In principle" hedges it, perhaps not enough for a reader who skims to the end.
- Missing: taxa that are lost (primer dropout of whole groups), named variable regions other than V4, positive controls, and a concrete example of a reversal.

**B**
- The closing doesn't fit B's own argument. B explains that under fixed bias the ratio between two taxa is off by the same factor in every sample, while proportions are off by amounts that change from sample to sample. Yet it closes by calling the table "most trustworthy for abundant taxa compared within one study run through a single protocol", without saying that ratios, not proportions, are the protected quantity. A reader could leave thinking a single protocol makes proportions comparable, which B's own model says it does not.
- Mild overstatement: inflation is said to shift the taxon count "by one to two orders of magnitude", but the example given (about 20 taxa becoming 1,607 to 5,824) is roughly 80- to 290-fold, beyond two orders at the top end.
- The Chao example and the 400% bead-beating figure come without context and invite more generalisation than one study supports.
- Missing: the gene-copy versus cell distinction (genomes per cell), the measured chimera and index-misassignment rates, every alternative to rarefying besides absolute load (proportions, log-ratio, scaling), and the singleton problem for richness estimators.
- Neither piece mentions coverage-based standardisation, which the research questions name.

## 4. Which I would give the reader

I would give the reader A, but the margin is modest. Both are accurate in substance, similarly sourced and the same length.

A is organised around one idea the reader can carry away: errors in which taxa are present behave differently from errors in how much of each there is, and fixed per-taxon bias spares ratios but not proportions. Its ending turns that into a ranking and a question to ask of any paper. It also covers more of "how samples are compared", since B never mentions log-ratio or scaling approaches.

B is better on the workflow itself, has the more vivid examples (the Bacteroides–Prevotella artefact, missing Verrucomicrobia, the lost archaeon), and keeps its soil replicate figures straight. But it leans on undefined jargon and tool names. Its closing also blurs the ratio-versus-proportion point that its own model section made.

If A fixed its replicate paragraph and borrowed B's reversal example, the gap would widen. If B's closing named ratios, the gap would close.
