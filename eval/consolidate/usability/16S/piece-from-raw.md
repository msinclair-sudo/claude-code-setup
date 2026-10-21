# Counting microbes by one gene: what a 16S survey can and cannot tell you

A 16S survey takes a scoop of soil, a water filter or a stool sample and returns a table. Each row is a taxon, each column a sample, and each cell a count of DNA sequences. Everything a microbiome paper says about who is present, how much of each, and how communities differ is computed from that table. It looks like a census. It is closer to a heavily processed poll, and knowing how the poll was run tells you which of its numbers to lean on.

## From sample to table

The method reads a single gene, the one encoding the 16S ribosomal RNA. Every bacterium and archaeon carries it, and its sequence differs enough between lineages to be matched against reference databases.

The sample is preserved (frozen, in ethanol, on a card, or not at all), and DNA is extracted from everything in it, usually by shaking cells open with beads. A PCR then copies a short stretch of the gene, often the V4 region, using primers designed to match as many organisms as possible, over roughly 25 to 35 cycles. Each sample's product is tagged with a short index sequence, and the tagged products are pooled and sequenced together, commonly on an Illumina MiSeq.

Software sorts reads back to their samples by index, discards poor reads and merges read pairs. It then collapses reads into units: clusters of sequences at least 97% or 99% identical (OTUs), or exact sequence variants (ASVs) inferred by modelling sequencing error. Chimeras, artificial hybrids of two templates formed during PCR, are screened out. Each unit is named by comparison with a reference database, and suspected contaminants are removed, ideally with help from blank controls, which only 30% of community-sequencing papers in one 2018 survey reported running.

Every step has several accepted options, and the field has settled few of them.

## How far the counts can be trusted

Whenever a known mixture of organisms, a "mock community", has been put through the workflow, the composition that came out differed from what went in. The errors come in two kinds worth keeping apart: how much of each taxon there is, and which taxa there are.

**Proportions.** Organisms differ in how easily their cells break open, how well their gene matches the primers and how efficiently it amplifies. In one closely studied mixture of seven vaginal bacteria, extraction alone distorted the ratio between pairs of taxa by up to 36.6-fold (5.5-fold on average), with PCR adding less. That extraction is generally the worst step rests mainly on this one dataset; another mock found two extraction methods gave very similar results. In a gut mock, 35 PCR cycles biased relative abundances by a factor of 2.6 on average. And one V4 primer pair under-counted SAR11, an abundant marine group, roughly 4- to 10-fold in seawater against about 2-fold in mocks, so bias measured on mocks can understate the real thing.

The gene adds its own distortion. A bacterial genome carries between 1 and about 15 copies of it (recent database releases include genomes with 21 or 22), and a cell can hold more than one genome, from one to hundreds in cultured species depending on growth phase. Reads track gene copies, not cells. Correcting for this is harder than it sounds. Copy number has to be predicted from sequenced relatives, predictions fail beyond about 15% sequence divergence, and about half of known OTUs sit further than that from any sequenced genome. On ten mock communities, uncorrected data fitted slightly better than corrected data.

One model gives a useful frame. If each step multiplies each taxon by its own fixed efficiency, the error in the ratio of two taxa is the same in every sample, while the error in a taxon's proportion shifts in size and even direction with whatever else is present. The seven-taxon mixture supported this. Stool and field data show bias varying between samples, so whether it holds generally is open.

**Which taxa, and how many.** Here the trouble is sequences that should not be there. Chimeras made up 0.9% to 18.2% of reads at 30 cycles, depending on the polymerase. Between a fraction of a percent and several percent of reads are assigned to the wrong sample (mostly measured outside 16S work), planting false presences of abundant taxa elsewhere. Reagents carry their own DNA: as one mock was serially diluted, contaminant reads rose from 0.1% to 80.1% and ASVs from 18 to 381. Two older pipelines returned 10 to 200 times the expected number of units on mocks, though relative abundances of the expected taxa varied far less between pipelines.

**Sampling noise.** The reads are a draw from the amplified pool, so a rare taxon can be present and simply not drawn. When the same soil DNA was sequenced twice, the replicates shared only a sixth to a third of their OTUs, yet weighted by abundance they overlapped 95% at 160,000 reads. Chance explains part of this, probably not all: presence-or-absence overlap levelled off below 45% however deep the sequencing, and replicates on separate runs agreed less.

**Load.** The table is relative. A taxon's share can fall while its absolute numbers rise, and total microbial load varied up to tenfold among healthy people's stool and by over six orders of magnitude between sites in the mouse gut. The counts carry no record of it.

## Comparing samples

Reads per sample can vary about 100-fold within a single study, and observed richness climbs with depth, so a deeply sequenced sample looks more diverse. How to compare samples fairly is among the most argued questions in the field.

The oldest fix, borrowed from ecology, is rarefying: subsample every sample to the same number of reads. In simulations built from twelve real datasets, where samples differed only by random sampling, averaging over many such subsamples was the only method that removed the link between depth and both richness and between-sample distances, and the only one that held false positives at 5% when depth differed between groups. An influential earlier simulation reached the opposite verdict, and its design has since been disputed; a statistical argument also holds that rarefied richness is biased. Simulations on both sides leave out taxon-specific bias and differences in load, and their verdicts flip with what they assume.

Each alternative has a catch. Proportions and log-ratio distances stayed depth-sensitive in those same simulations. Scaling methods imported from RNA sequencing assume most taxa do not change. Richness estimators such as Chao1 remain tied to depth and break when singleton reads are removed, as some denoising tools do by default. To find which taxa differ between groups, fourteen methods applied to the same 38 datasets called anywhere from 0.8% to 40.5% of ASVs significant.

Measuring total load by qPCR, flow cytometry or a spike-in of known DNA has reversed conclusions drawn from proportions alone. It leaves taxon-specific bias in place, and the methods disagree: qPCR and flow cytometry matched on a mock but diverged on stool, and spike-in recovery ranged from 40% to 84% across samples.

So the numbers in a 16S table deserve different amounts of trust. A change in the ratio of two taxa across identically processed samples is, in principle, the best-protected quantity, because fixed per-taxon biases cancel. A taxon's proportion compared across very different communities is less safe. Counts of taxa, the presence of rare ones and absolute richness depend heavily on depth, pipeline and contamination, most of all in low-biomass samples. Of any reported difference, it is fair to ask whether it survives a change of normalisation, and whether the authors checked.
