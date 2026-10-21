# Notes on writing the 16S piece

## 1. Wanted or needed, and not in the material

- **Why the 16S gene at all.** The material never says why this gene is used: that it is present in all bacteria and archaea, has conserved stretches where universal primers bind and variable regions that tell taxa apart. An outsider needs this in the first paragraph. I wrote only what the material implies (every genome carries 1 or more copies; regions V1 to V9; "universal" primers) and left out the conserved/variable logic, so the piece's opening is thinner than it should be.
- **What a mock community is.** Used throughout, never defined. I defined it from context ("known composition").
- **Basic mechanism of several steps.** What bead beating does (breaks cells open), what an index is for (lets samples share a run), what a chimera is (I inferred "hybrid of two parent templates" from the word "parents" in the ChimeraSlayer item). All are background I supplied.
- **Definitions of the metrics.** Bray-Curtis, UniFrac, Jaccard, Shannon, inverse Simpson, Chao1, ACE, PERMANOVA and FDR appear with no definition or scale. I used Bray-Curtis without saying what 0.35 or 0.08 means in plain terms, because the material does not give its range.
- **What "compositional" means and why the table is relative.** The material says 16S data are "compositions" and that load measurements change conclusions, but never states plainly that sequencing fixes the total so counts carry only proportions. I wrote "the table is relative" as a bridge; that sentence is mine.
- **Typical or default practice.** How often each choice is made is explicitly unmeasured, so I could not say what a "typical" study does (most common platform, region, pipeline, whether rarefying is the norm). This forced hedged wording ("for example", "documented protocols") where a reader would want a baseline.
- **A worked example of the ratio-versus-proportion point.** The multiplicative-bias argument is central but the material gives it only as a model statement; a two-taxon numerical illustration would help, and none is given.
- **A bottom line from the research.** The material gives no overall guidance on what is safe to conclude from a count table (and its "Do not say" list warns against the reviewer's framing on this). My last sentence is my own synthesis of the findings.
- **Whether the two soil replicate-overlap figures (44% presence-absence, 95% abundance-weighted) come from the same sample.** They appear in separate bullets, one marked replicated and one not; I hedged to "replicates of one soil".
- **Primer choice and abundance distributions in plain consequence terms**, e.g. how much a typical V4 study would mis-state a dominant taxon. Only per-mock magnitudes exist.
- Nanopore, and any independent long-read benchmark, are absent (the material says so).

## 2. Hard to use in the material

- **Organisation by research question, then by concept, then a "Do not say" list.** The same finding appears up to three times (answer, concept bullet, corrected wording), with slightly different qualifiers. I had to cross-check every number against the "Do not say" list before using it, which is the most time-consuming part.
- **Density of caveats.** Nearly every bullet carries source, sample size, access status and standing. That is right for an audit but makes it hard to tell which findings are the load-bearing ones for a general reader. A short ranked list of the strongest, most general findings would have saved a lot of sorting.
- **Author-year citations without a reference list.** "Brooks 2015", "McLaren 2019", "Schloss 2024b", "MBQC" etc. are used as if the reader knows them. For a standalone piece I could not cite them meaningfully, so I referred to "one study" or "one dataset".
- **Half the material (MB-02) is off-topic for this piece.** Ploidy, rare-biosphere definitions, core microbiome thresholds and soil abundance-occupancy are detailed and heavily caveated but mostly not about how a sample becomes a count table. Sorting out what was usable took effort; I used only the copy-number-per-genome and correction parts.
- **Soil bias.** Much of the replicate, abundance-distribution and occupancy evidence is from soil (often one Oklahoma dataset, one lab), and the material is thin on water and host samples, so general statements had to be hedged or dropped.
- **Standing tags are inconsistent in meaning.** `(repl)` sometimes sits on a bullet that elsewhere is described as resting on overlapping sources (e.g. the 1 to 15 copy range), and some bullets have no tag at all, so I could not rely on tags to gauge strength.
- **Internal contradictions flagged but unresolved**: Kozich error rates from two angles, Zhou 2011 abstract versus discussion overlaps, Custer's temporal effect, the archaeal copy maximum. These are noted, but I avoided all of them rather than pick a value.
- **Unexplained shorthand**: "angle", "the critic", "the body", "Common rule 6", "stage 2 check", "brief". These refer to the research process and mean nothing to a writer outside it.
- **Background lines are rare and marked.** Only the OTU/ASV definition is labelled as background; everywhere else the material assumes the reader already knows the field.
