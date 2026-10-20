# Blind fact-check, 2026-10-20

A fresh subagent saw only `claims.yaml` and `sim.py` (and the web for the cited papers); never a storyboard or render.

- c1-c8, c10: supported. c10 nuance noted: Gotelli and Colwell warn that standardising by samples and by individuals "may produce very different results".
- **c9: inaccurate as first written** ("95% of 200 subsamples fall between 208 and 228"). The 2.5th and 97.5th percentiles are exactly 208 and 228, and draws tie on those values, so 194 of 200 (97%) fall inside. Rewritten: "the middle 95% of 200 subsamples span 208 to 228 taxa".
- c11: supported; "showed" made exact as "showed in simulations".
- Bibliographic details of all three papers match Crossref.

This is the error the check exists for: a percentile range stated as a coverage share, the kind of slip that reads as right on a polished slide.

# Blind fact-check of the metabarcoding tier 4, 2026-10-20

Same rules: the reader saw only `t4/claims.yaml` and `pipeline.py`, plus the cited papers.

- Supported: m1, m2, m4, m5, m9-m14, m16, c10, c11.
- **m3 overstated:** "carried by every bacterium" is in neither source (Caporaso et al. support the marker role). Now "a gene that bacteria carry"; rrnDB backs "one or more copies" per genome.
- **m6 wrong mechanism:** Suzuki and Giovannoni (1996) found reannealing pulling template ratios toward 1:1, with one primer pair; not per-template efficiency differences. The model's efficiencies are now labelled as the model's, and the paper is cited only for "PCR can distort template ratios".
- **m7:** arithmetic slip in the source line (1.95^25 is 17.8 million, not 17.6).
- **m8 slightly overstated:** McLaren et al. show a consistent multiplier *for a fixed protocol*; the claim now says so.
- **m15 number:** the 2.5th percentile is 58.975; `int()` truncated it to 58. Rounded, 59: "between 59 and 68". pipeline.py and sim.py now round.

Lesson for the skill: a citation can be right about the paper and wrong about the mechanism; the blind check opened the full text and caught it.

## Tier 4, metabarcoding rebuild from MB-01 (2026-10-20)

Blind check of t4/claims.yaml (29 claims), sources opened by DOI; access per line. Verdicts as returned:

# Fact-check: rarefaction/t4/claims.yaml

pipeline.py was run (seed 7) and its output matches every simulation number below. Extra checks: P(|ln b| > ln 4) with sd 1.06 is 0.191; 30 binomial repeats of the top share at depth 500 ran 41.6-49.4% (mean 45.8%).

- m1: supported. Access: code. N_TAXA = 80, CELLS = 100_000, lognormal sigma 2.0.
- m2: supported. Access: run. cells[0] = 23,000 (23.0%). 6 taxa are above 5% and 61 of 80 are below 1%, so "a few common, most rare" holds.
- m3: supported. Access: full text (PMC4504704). Abstract: "a large increase in DNA from Gram-positive bacteria (up to 400%)". Also: "The effect of bead beating intensity correlated with cell-wall strength". Activated sludge, one study, as the claim says.
- m4: supported. Access: full text (PMC3063599). "Studies of 16S rRNA provide a view of which microbial taxa are present in a given sample".
- m5: supported. Access: full text (PMC4383981). "from 1–15 in bacteria and 1–4 in archaea".
- m6: supported (illustrative). Access: run. copies[0] = 7, copies[2] = 1, drawn from 1-15 with weights 0.7^(k-1). The realised maximum is 9.
- m7: overstated. Access: full text (PMC3592464). Klindworth says nothing about doubling per cycle. It only says "conserved broad-range PCR primers" and "overall coverage of variable regions". The conserved/variable layout is in the Illumina guide ("nine variable regions interspersed between conserved regions"), not in Klindworth. Suggested: "primers bind conserved stretches of the 16S rRNA gene either side of a variable region, and PCR copies that short stretch (the barcode)". Drop "each cycle can nearly double it", or cite a PCR-kinetics source for it.
- m8: supported for the numbers, with a minor scope widening. Access: Illumina 15044223 Rev. B full PDF (Amplicon PCR "25 cycles", Index PCR "8 cycles"); EMP page (program "repeated 35 cycles"). Two protocols are generalised to "16S amplicon protocols run 25 to 35". Suggested: "two widely used 16S protocols run 25 to 35 PCR cycles (Illumina's two-step guide 25 amplicon cycles plus 8 index cycles; the Earth Microbiome Project 35); the simulation uses 35".
- m9: unsupported as written. Access: full text (PMC8284789). The claim joins two different experiments.
  - The 2.6 comes from the 10-isolate mock calibration sample (amplified for 10 to 35 cycles): "On average, the relative abundance of each taxon was biased by a factor of 2.6 (95% credible set 2.3 to 2.9)". The paper gives no share of mock taxa beyond fourfold.
  - The 19% comes from four artificial gut communities inoculated from donor stool: "35 cycles of PCR induces a substantial bias in estimated relative abundances" ... "approximately 19% of taxa being subject to over a factor of 4 bias". That is the cycle-35 proportion compared with a model-inferred cycle-0 proportion.
  - Suggested: "in one study, after 35 PCR cycles about 1 taxon in 5 (19%) in lab-grown gut communities came out more than fourfold off; in a 10-strain mock community the average bias was 2.6-fold". The pipeline.py docstring ("as in one mock community") repeats the same conflation.
- m10: supported for the numbers, with caveats. Access: run. 15 of 80 taxa are beyond fourfold (18.75%; expected 19.1%).
  - The "1/16 to 16" axis is not in pipeline.py, so it cannot be checked there. One taxon's bias (0.032) falls below 1/16 and would sit off that axis.
  - "Matches that calibration" inherits the m9 error.
  - Suggested: "the simulation is set to match the 19% figure; 15 of its 80 taxa end more than fourfold off". Widen the axis, or note that one taxon is clipped.
- m11: supported. Access: run. Taxon 1: 23.0 -> 31.4 -> 49.5 -> 45.8%. Taxon 3: 7.5 -> 4.2 -> 0.9 -> 0.5%.
- m12: supported. Access: Illumina full PDF ("dual-index barcodes ... up to 96 libraries can be pooled together for sequencing"); Kozich abstract only ("large numbers of samples could be multiplexed and sequenced in parallel").
- m13: supported (illustrative). Access: code. sequence() = rng.multinomial(depth, pool).
- m14: supported. Access: full text (PMC10900887). Table 1 gives Bioethanol as 3,690-356,027 (96.5-fold); the paper's Discussion says "as much as 97-fold". The ledger's source note is wrong on one point: the other datasets run about 1.3- to 69-fold (Rice 2,777-192,200; Stream about 44-fold), not 1.3- to 41-fold. Fix the note; the claim text is fine.
- m15: supported. Access: Edgar full text (bioRxiv preprint), Minich abstract. Edgar: "cross-talk occurred for ~2% of the reads in one Illumina GAIIx run and eleven Illumina MiSeq runs" (16S mock data). Minich: "while barcode leakage was negligible". Edgar is a preprint, as the ledger already notes.
- m16: supported. Access: Bokulich 2013 full text (PMC3531572); Illumina PDF. Bokulich: filter parameters "have a marked effect on α– diversity and estimates of taxonomic composition". Illumina: "the ends of each read are overlapped to generate high-quality, full-length reads". Bokulich does not cover read merging; the Illumina guide does.
- m17: overstated (minor scope). Access: Nearing full text (PMC6087418); Callahan abstract only. The ASV counts are exact ("Deblur called 8270 ASVs", "DADA2 called 16609 ASVs"). The 97% OTU pipeline is named in Nearing. But the source is "The soil data set collected from blueberry fields", which is many samples, not "one soil". Suggested: "on one soil dataset, pipelines found 8,270 to 16,609 ASVs".
- m18: supported. Access: full text (PMC6531881). "After 30 rounds of PCR, the Platinum polymerase had the highest chimera rate (i.e., 18.2%)" ... "Accuprime (i.e., 0.9%)". "The sensitivity of UCHIME varied between 50 and 87.0% when at least 25 cycles were used." The figures come from a mock community. Optional: "in one mock-community test at 30 cycles".
- m19: supported. Access: full text (PMC5956843). Sequences are "compared against an annotated reference sequence database to determine the likely taxonomic origin". The paper does not describe counting reads into a taxa-by-samples table; that part is standard practice.
- m20: supported (illustrative). Access: code. The docstring says: "Left out on purpose ... chimeras, index misassignment, sequencing errors and spurious ASVs".
- m21: supported. Access: run. 42, 64 and 78 taxa at 500, 5,000 and 50,000 reads.
- m22: supported. Access: run plus recompute. pool[0] = 0.458. A multinomial or binomial draw is unbiased for each pool share. 30 repeats at depth 500 ranged 41.6-49.4%. scene.py was not opened, so the repeat draw is checked against the model, not the scene code.
- m23: supported. Access: run. Deep (50,000 reads) shows 78 taxa; shallow (2,000 reads) shows 56.
- m24: supported. Access: run. Mean 56.9; 2.5-97.5 percentiles 51.975 and 61, rounded to 52-61, over 200 draws. 56 falls inside.
- m25: overstated / partly unsupported. Access: Schloss 2024b full text; Schloss 2024a full text; Hurlbert and Gotelli abstracts only (OpenAlex).
  - Schloss 2024b reports null-model results for rarefaction only: "Rarefaction eliminates the correlation between sequencing depth and alpha diversity". It does not test a single subsample on that question.
  - Schloss 2024a compares a single subsample with rarefaction on clustering accuracy, not on the depth-richness link.
  - Hurlbert supports the last clause: "expected number of species in a sample of n individuals".
  - Suggested: "rarefying draws one random subsample to a common depth; rarefaction repeats it and averages, and in null-model simulations it removed the link between richness and depth; it estimates the taxa expected in a subsample of the smaller size".
- m26: supported. Access: arithmetic plus code; McLaren full text (PMC6739870). 50,000 - 2,000 = 48,000. rarefy() subsamples the already-biased reads. McLaren: "Many bias mechanisms are thought to act multiplicatively on the taxon abundances"; extraction and PCR are named as sources.
- m27: overstated in part. Access: Sze full text; McLaren full text; Parada abstract only.
  - Sze supports it: the distance between the 25-round and 30/35-round communities "varied considerably between samples". Note that Sze also says the bias "appeared to be consistent within each sample".
  - Parada supports it: "biases with 515F-Y/806R against SAR11 in field samples (∼4-10-fold)" against "mock communities (∼2-fold)".
  - McLaren argues the opposite about bias itself: "the error in the ratios was consistent across samples" while "the error in the proportions varied dramatically in both magnitude and direction". In McLaren the bias is constant; the error in shares varies with composition.
  - Suggested: "the bias, or at least its effect on each taxon's share, can differ between samples". Alternatively, drop McLaren as support for bias varying.
- m28: supported. Access: abstracts of McMurdie & Holmes, Weiss, Willis, Schloss 2024a; Schloss 2024b full text.
  - McMurdie & Holmes: "avoid rarefying altogether".
  - Weiss: rarefying helps clustering ("more clearly clusters samples"), and for differential abundance it brings "a loss of sensitivity".
  - Schloss argues for rarefaction for alpha and beta diversity.
  - Together these show the disagreement and that the answer splits by analysis type.
- m29: overstated. Access: abstracts of Vandeputte and Tkacz. Vandeputte: relative data "cannot provide information about the extent or directionality" of load changes; load was measured by "flow cytometric enumeration of microbial cells". Tkacz uses synthetic spikes in soil. Neither source mentions qPCR, and flow cytometry is left out of the claim. Suggested: "shares (relative abundances) cannot show total microbial load; measuring it takes an extra measurement, such as cell counts by flow cytometry or added spike-ins (qPCR is another common option)", with a qPCR source cited if it is kept.

**Fixed before the final render:** m9 split into its two experiments (19% beyond fourfold in lab-grown gut communities; 2.6-fold average in the 10-strain mock), narration and pipeline docstring to match; m25 clause without support dropped, Cameron 2021 added for the noise of one subsample; m27 reworded to the bias or its effect on shares; m29 qPCR replaced by cell counts (flow cytometry) and spike-ins, as the sources measured; m7 sourced (Illumina guide for the layout, Kelly 2019 for per-cycle amplification); m17 "one soil dataset"; m8 "two common protocols"; m10 axis widened to 1/32-32 so every taxon is on it; m14 source note corrected to 1.3- to 69-fold.

## Tier 4, pacing and wording remake (MB-02, NP-01), 2026-10-21

Blind check of the new and changed claims (m2, m5, m9, m11, m30, m31). Verdicts as returned:

# Blind fact-check, rarefaction t4 claims (round 2): m2, m5, m9, m11, m30, m31

- **m2: supported.** Access: ran pipeline.py (seed 7). cells[0] = 23,000 of 100,000 (23.0%). 5 of 80 taxa hold 51.9% of cells and 10 hold 69.7%. 61 of 80 taxa are below 1% and 20 are below 0.1% (median share 0.31%). "A few hold most" and "most at low abundance" both hold. No change needed.
- **m5: supported** (one soft spot). Access: Stoddard 2015 full text (Europe PMC) says "from 1–15 in bacteria and 1–4 in archaea" (stated per rRNA operon, citing rrnDB). Vetrovsky 2013 full text: 1,690 genomes, "1–15 per genome", "average of 4.2", "maximum value was 15". MB-02 review (critic block read first): rrnDB v5.6/v5.10 maxima of 21 and 22 are the reviewer's own derivation, "No source I found checked whether these extremes survive scrutiny of assembly quality". The review names only "several" genomes at 20 to 21 and gives no share above 15, so "rarely" is an inference, though a fair one. Optional wording: "a genome carries 1 to about 15 copies, depending on the taxon; a few recent database genomes list up to 22".
- **m9: supported.** Access: Silverman et al. 2021, full text (Europe PMC PMC8284789). "35 cycles of PCR induces a substantial bias ... with approximately 19% of taxa being subject to over a factor of 4 bias". Bias is defined as the cycle-35 proportion against the "inferred taxon proportions at cycle 0". The communities are "artificial gut vessels" seeded from four donors' faecal samples, so "lab-grown gut communities" fits (taxa are genera, 68 of them). Mock community: "On average, the relative abundance of each taxon was biased by a factor of 2.6 (95% credible set 2.3 to 2.9)". This is the calibration sample, an equal mix of DNA from 10 isolates, after 35 cycles (S2 Fig). Nuance: the mock was mixed from extracted DNA, not cells. That does not affect the claim.
- **m11: supported.** Access: ran pipeline.py. Taxon 1: true 23.0%, dna 31.4%, templates 49.5%, pool 45.8% (rounds to 46%). Taxon 3: true 7.5%, dna 4.2%, templates 0.9%, pool 0.5%. Each stage changes the shares. Minor ambiguity: the 49.5% is the share of 16S copies in the extracted DNA (cells x yield x copies), not in the cells. Optional wording: "49.5% of the extracted 16S gene copies".
- **m30: supported.** Access: Pecoraro et al. 2011, full text (Europe PMC PMC3031548), plus the MB-02 critic block. Pecoraro: C. crescentus 2.1 and W. succinogenes 0.9, both "monoploid". P. putida about "20 origins and 14 termini". The paper's own Table 5 and text go higher: A. vinelandii "40" in fast growth ("&gt;40 genome copies") and a methanogen with "about 50 genome copies". Ploidy is "correlated with growth rate" (E. coli 6.8 vs 2.5 origins). So "one to dozens or more, depending on species and growth" holds, but the "dozens" rests on the Table 5 and methanogen figures, not on the P. putida figure the ledger cites. Soil: the review found only indirect evidence, "1.5 to 15 fg DNA per cell", which "cannot separate genome size from copy number". The critic adds "Nothing comparable was found for soil". "Barely been measured" is a fair plain reading. A tighter version: "in soil, genome copies per cell have not been measured directly; only DNA per cell, which cannot tell genome size from copy number". Suggested source note: add "A. vinelandii about 40 in fast growth (Pecoraro Table 5, from another lab)" to support "dozens or more".
- **m31: supported.** Access: Delgado-Baquerizo et al. 2018, full text (NOAA repository PDF); Europe PMC has the abstract only. "only 2% of the bacterial phylotypes (511 out of 25,224 phylotypes) were dominant ... accounted for, on average, 41% of 16S rRNA gene sequences across all samples". Dominant means "top 10% most common phylotypes ... and ubiquitous (found in more than half of the 237 soil samples)". The claim's "abundant and widespread" and "average sample" match. Do not reach for the abstract's "almost half"; 41% is the body figure. No change needed.

**Applied:** m30 source now cites the Azotobacter and methanogen figures behind "dozens or more". Kept: m5 "rarely more" (the 21 to 22 maxima are a derivation from rrnDB, said so in the source); m11 wording (the narration says "of the gene copies", after extraction).

## Tier 4, text, terms and charts revision (owner review of v3), 2026-10-21

Blind check of new and changed claims (m7, m32, m33, m34, m35). Verdicts as returned:

# Fact-check t4 claims, round 3 (m7, m32, m33, m34, m35)

- m7: OVERSTATED. Access: Illumina guide 15044223 Rev B full PDF text; Klindworth 2013 full text (Europe PMC XML, PMC3592464); Kelly 2019 full text (Europe PMC XML, PMC6702206). Conserved/variable: Illumina says the gene "contains nine variable regions interspersed between conserved regions. Variable regions of 16S rRNA are frequently used in phylogenetic classifications such as genus or species", which supports that part; "almost the same in every bacterium" is a gloss, not in the source. Per-cycle: Kelly models A_i = D_i (a_i + 1)^N_PCR with a_i drawn from a Beta distribution (0 to 1), so "can nearly double" is supported. Overstated part, "one pair fits nearly every bacterium": Klindworth's recommended pair S-D-Bact-0341-b-S-17/S-D-Bact-0785-a-A-21 has "B: 86.2%" coverage with no mismatches and "B: 94.5%" "If one mismatch is tolerated", and of the recommended primers "none of them are perfect". Term note: "barcode" for the amplicon is the metabarcoding meaning, but the cited Illumina guide uses "barcodes" for the index tags ("dual-index barcodes"). Suggested: "...primers bind two conserved stretches, so one pair fits most bacteria (no pair fits all), and PCR copies the variable region between them (the barcode); each cycle can at most double it."
- m32: SUPPORTED (with a note on "often"). Access: EMP 16S protocol page (live fetch); Caporaso 2011 on PMC (PMC3063599); Europe PMC metadata for the citation (PNAS 108 Suppl 1: 4516-4522, correct). EMP: "Primers 515F–806R target the V4 region of the 16S SSU rRNA"; the current EMP primers are the revised "515F (Parada)" and "806R (Apprill)". Caporaso: "The PCR primers (F515/R806) were developed against the V4 region of the 16S rRNA". Neither source says V4 is used "often"; that is a generalisation from two V4 protocols, and the Illumina guide cited in m7/m8 targets V3–V4. Suggested (optional): "the variable region copied is often V4 (Illumina's guide uses V3–V4); the Earth Microbiome Project protocol amplifies V4 (primers 515F and 806R)".
- m33: SUPPORTED. Access: ran pipeline.py via scripts/x. Output: true 0.23/0.07476 = 3.077; templates 0.49459/0.0093575 = 52.86; pool 0.45759/0.0053951 = 84.82. Rounds to 3, 53, 85; the source line's figures match. Note: "templates" in pipeline.py = cells x extraction yield x copy number, so the 53:1 ratio includes extraction yield as well as copy number. "16S gene copies" (in the extracted DNA) is still accurate.
- m34: SUPPORTED as illustrative. Access: claims ledger only (scene.py not opened, as instructed). The text says "illustrative". A peak near 250 bases is plausible for merged V4 reads (Kozich: V4 "length, ca. 250 bp"), and a 200-base length cut-off is a plausible filter.
- m35: SUPPORTED. Access: Illumina guide full PDF text; Kozich 2013 on PMC (PMC3753973); Europe PMC metadata (AEM 79(17): 5112-5120, correct). Illumina: "Using paired 300-bp reads ... the ends of each read are overlapped to generate high-quality, full-length reads of the V3 and V4 region"; amplicons should have "at least ~50 bp of overlapping sequence in the middle". Kozich: V4 "(length, ca. 250 bp)", "The entire V4 region was covered by two reads", and "Contigs between read pairs were assembled". "Read pair" is used in its field meaning. Term note: "barcode" here means the amplicon, while the Illumina source uses "barcodes" for index tags. Suggested (optional): "the sequencer reads each amplicon from both ends...".

Housekeeping: claims.yaml has duplicate "kind:" keys in m2 and m8. Those claims were outside my scope and I did not check them.

**Applied:** m7 "one pair fits nearly every bacterium" overstated (best broad pair about 86% exact, 94.5% with one mismatch): now "most bacteria", and "conserved" glossed as "much the same across bacteria" in claim, narration and legend; m32 "often" replaced by "one widely used choice", with Illumina's V3-V4 noted. The reported duplicate kind keys in m2 and m8 were not there (one each).

## t4 fifth version (2026-10-21): read filtering, m36 to m38

Blind checker, sources only (DADA2 Pipeline Tutorial 1.16; Bokulich et al. 2013; Kopylova et al. 2016). References correctly identified.
- m36 supported: V4 tutorial data, distinct sequences 251 to 255 bases (most 253). They are ASVs, not reads; the narration now says "distinct sequences". "Taxa differ by a few bases" is an inference from the tutorial's "biological length variation", labelled so.
- m37 overstated, fixed: the tutorial says off-length sequences "may be" from non-specific priming (narration: "can make"); quality falling at read ends is "common in Illumina sequencing" (narration: "on Illumina machines, quality tends to fall").
- m38 supported except "every sample", which is shown in practice (one filterAndTrim call) but stated by no source: narration now "usually".

