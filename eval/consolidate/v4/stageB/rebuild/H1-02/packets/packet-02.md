## filters-corrections.3 (claim)

The contig-length filter and the relaxed core threshold, tested on real data, reduced the artefact without removing it.

- conf: not stated
- class: not stated
- holds: only n = 8 and n = 5 gut E. coli pairs
- src: mezitiReliabilityMetagenomeassembledGenomes2021, liCriticalAssessmentPangenomic2022
- trail: H1-02 §Verdict as delivered, §5. Verdicts

From the note:

> H1-02:A-003 [quote: Verdict as delivered] The contig-length filter [1] and relaxed core threshold [2] were tested on real data but only in n = 8 and n = 5 gut E. coli pairs, and they reduced the artefact without removing it.
>
> H1-02:A-024 [5. Verdicts] The filters tested on real samples [1, 2] reduce the artefact in small gut E. coli sets and were not shown to remove it.
>

## filters-corrections.4 (claim)

No filter has been validated on real samples as removing the artefact.

- conf: not stated
- class: not stated
- search: not stated
- holds: the filters tested on real samples, in small gut E. coli sets
- src: none (the reviewer's synthesis)
- trail: H1-02 §Verdict as delivered, §critic

From the note:

> H1-02:A-002 [quote: Verdict as delivered] No filter has been validated on real samples as removing the artefact.
>
> H1-02:C-005 [danger: Critic: verdict partly supported] No filter has been validated on real samples as removing the artefact.
>
> H1-02:A-024 [5. Verdicts] The filters tested on real samples [1, 2] reduce the artefact in small gut E. coli sets and were not shown to remove it.
>

## filters-corrections.5 (claim)

Eisenhofer's completeness-model correction (a GLM) was validated on mock-community subsamples and over-corrected some genomes.

- conf: not stated
- class: not stated
- holds: mock-community subsamples, not natural-sample MAGs
- src: eisenhoferImpactMicrobialGenome2023
- trail: H1-02 §2.7

From the note:

> H1-02:B-0112 [2.7 Filters and corrections: real-sample validation] - Completeness-model corrections: Eisenhofer's GLM [3] was validated on mock-community subsamples and over-corrected some genomes.
>

Not found in the cited text (where to look, not what is wrong): holds: natural-sample; holds: mags

## filters-corrections.6 (claim)

CELEBRIMBOR was validated on simulations, and its authors state that non-random loss violates its missing-at-random assumption.

- conf: not stated
- class: not stated
- holds: simulations
- src: hellewellCELEBRIMBORCoreAccessory2024
- trail: H1-02 §2.7

From the note:

> H1-02:B-0113 [2.7 Filters and corrections: real-sample validation] CELEBRIMBOR [19] was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption. mOTUpan [14] was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
>

## filters-corrections.7 (claim)

mOTUpan was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".

- conf: not stated
- class: not stated
- holds: a few closed Prochlorococcus genomes plus bootstraps
- src: buckMOTUpanRobustBayesian2022
- trail: H1-02 §2.7

From the note:

> H1-02:B-0113 [2.7 Filters and corrections: real-sample validation] CELEBRIMBOR [19] was validated on simulations, and the authors state that non-random loss violates its missing-at-random assumption. mOTUpan [14] was checked against a few closed Prochlorococcus genomes plus bootstraps, and its authors state that genes hard to assemble or bin leave "an inevitable underestimate of the accessory genomes".
>

## filters-corrections.8 (claim)

MetaPathPredict was tested on random annotation downsampling only.

- conf: not stated
- class: not stated
- holds: random annotation downsampling
- src: gellermcgrathPredictingMetabolicModules2024
- trail: H1-02 §2.7

From the note:

> H1-02:B-0114 [2.7 Filters and corrections: real-sample validation] MetaPathPredict [15] was tested on random annotation downsampling only.
>

## filters-corrections.9 (claim)

No completeness or missingness correction has been validated against ground truth on natural-sample MAGs with real, non-random gaps.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction, and missing-at-random pangenome correction")
- holds: Eisenhofer's GLM, CELEBRIMBOR, mOTUpan and MetaPathPredict, and the review's search for others; the critic: supported by the named search routes and the authors' own stated assumptions (CELEBRIMBOR, mOTUpan)
- src: eisenhoferImpactMicrobialGenome2023, hellewellCELEBRIMBORCoreAccessory2024, buckMOTUpanRobustBayesian2022, gellermcgrathPredictingMetabolicModules2024
- trail: H1-02 §2.7, §Search record, §Adversarial

From the note:

> H1-02:B-0112 [2.7 Filters and corrections: real-sample validation] - Completeness-model corrections: Eisenhofer's GLM [3] was validated on mock-community subsamples and over-corrected some genomes.
>
> H1-02:B-0115 [2.7 Filters and corrections: real-sample validation] None of these was validated against ground truth on natural-sample MAGs with real, non-random gaps.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0184 [Search record] (2) A completeness or missingness correction validated on natural-sample MAGs with non-random gaps against ground truth.
>
> H1-02:B-0185 [Search record] Routes: Europe PMC and WebSearch on mOTUpan, CELEBRIMBOR, MetaPathPredict, completeness bias correction, and missing-at-random pangenome correction.
>
> H1-02:B-0014 [info: Provenance] Not-found routes: WebSearch and Europe PMC title and abstract queries on MAGs against same-sample isolates in soil and sediment; completeness and missingness corrections validated on real MAGs; scaling of content artefacts with diversity or depth; and annotation-coverage differences between samples.
>
> H1-02:B-0015 [info: Provenance] None returned a qualifying study.
>
> H1-02:C-094 [warning: Adversarial critique, full findings] That corrections are not validated on real natural-sample MAGs is supported by the named search routes and the authors' own stated assumptions (CELEBRIMBOR, mOTUpan).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## filters-corrections.10 (claim)

Artefacts persist above completeness thresholds: module fullness bias above 90%; ribosomal-protein, CRISPR and transposase deficits above 90%; chimerism in MIMAG high-quality sets; contaminant genes below the 5% contamination threshold. No source showed that a completeness threshold removes the problem.

- conf: not stated
- class: not stated
- search: not stated
- holds: module fullness, ribosomal-protein and mobile-gene deficits, chimerism and contaminant genes, each from one source; the critic: the ribosomal-protein and contaminant figures have direct support in full text, while the module-fullness and chimerism sources rest on agent reads
- src: eisenhoferImpactMicrobialGenome2023, miseUnexpectedAbsenceRibosomal2022, orakovGUNCDetectionChimerism2021, majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.7, §5. Verdicts, §Adversarial

From the note:

> H1-02:B-0116 [2.7 Filters and corrections: real-sample validation] - Completeness thresholds: module fullness bias persists above 90% [3]; ribosomal-protein, CRISPR and transposase deficits persist above 90% [6]; chimerism persists in MIMAG high-quality sets [9]; contaminant genes sat below the 5% threshold [22].
>
> H1-02:B-0117 [2.7 Filters and corrections: real-sample validation] No source showed that a completeness threshold removes the problem.
>
> H1-02:A-023 [5. Verdicts] The loss of variable and mobile genes, and contamination-driven gains, were measured directly [1, 12, 22] and persist through completeness filters [3, 6, 9, 22].
>
> H1-02:C-092 [warning: Adversarial critique, full findings] Persistence above completeness thresholds has direct support in full text: [6] reports '20-40% of near-complete' MAGs lacking ribosomal protein genes, and [22] reports contaminants below 5% CheckM contamination that GUNC did not flag.
>
> H1-02:C-093 [warning: Adversarial critique, full findings] [3] and [9] rest on agent reads.
>

Not found in the cited text (where to look, not what is wrong): holds: mobile-gene

## filters-corrections.11 (claim)

Gene-to-species correlation filtering classified contaminants with AUROC 0.97 on real gut data, judged against BLAST rather than ground truth.

- conf: not stated
- class: not stated
- holds: real gut data (the cirrhosis cohort); the comparison is BLAST, not ground truth
- src: majernikSmallAmountsMisassembly2025
- trail: H1-02 §2.7

From the note:

> H1-02:B-0120 [2.7 Filters and corrections: real-sample validation] - Gene-to-species correlation filtering classified contaminants with AUROC 0.97 on real gut data, against BLAST rather than ground truth [22].
>
> H1-02:B-0045 [2.2 Real-data artefacts without an isolate reference (natural)] Majernik et al. [22] re-analysed a cirrhosis case-control gut cohort with UHGG/MIDAS2 pangenomes.
>

## annotation-coverage.1 (claim)

UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns.

- conf: not stated
- class: meas (note: "These are measured, gut only")
- holds: human gut only (UHGG)
- src: almeidaUnifiedCatalog2042020
- trail: H1-02 §3.6

From the note:

> H1-02:B-0156 [3.6 Annotation coverage] UHGG core genes had KEGG annotation for a median of 69% of genes, while accessory genes had significantly more unknowns [10].
>
> H1-02:B-0158 [3.6 Annotation coverage] These are measured, gut only.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## annotation-coverage.2 (claim)

Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria.

- conf: not stated
- class: meas (note: "These are measured, gut only")
- holds: one infant gut catalogue; the critic: not re-opened at synthesis, resting on search-agent reads
- src: marangaComprehensiveFunctionalAnnotation2023
- trail: H1-02 §3.6, §Adversarial

From the note:

> H1-02:B-0157 [3.6 Annotation coverage] Orthology-based GO coverage in an infant gut catalogue was 12%, and it favoured Gammaproteobacteria [35].
>
> H1-02:B-0158 [3.6 Annotation coverage] These are measured, gut only.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>

Not found in the cited text (where to look, not what is wrong): holds: search-agent

## annotation-coverage.3 (claim)

No source measured how annotation coverage differs between samples or environments for the same lineage.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Route: WebSearch on annotation coverage bias for novel lineages")
- holds: the review's search; one route only
- src: none (a search result)
- trail: H1-02 §3.6, §Search record

From the note:

> H1-02:B-0159 [3.6 Annotation coverage] No source measured how annotation coverage differs between samples or environments for the same lineage.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0188 [Search record] (4) Between-sample or between-environment differences in annotation coverage for one lineage.
>
> H1-02:B-0189 [Search record] Route: WebSearch on annotation coverage bias for novel lineages.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## artefact-size.1 (claim)

Recovery artefacts in the gene or pathway content of related recovered genomes have been measured and are material, but only in natural human gut and, from a single source, coastal marine samples. Part A for gut rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study; the loss of variable and mobile genes, and contamination-driven gains, were measured directly in those sources.

- conf: single (critic: C-016)
- class: not stated
- rating: "MEASURED AND MATERIAL" (critic: C-001: only in natural human gut and, from a single source, coastal marine samples)
- holds: natural human gut (same-sample isolate pairs, n = 8 E. coli pairs; contamination of differential gene calls) and natural coastal marine (read-technology gene-count difference at equal estimated completeness); the critic: each of the three direct sources is single-source and has caveats the verdict leaves out
- src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023
- trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic

From the note:

> H1-02:A-001 [quote: Verdict as delivered] **A. Size of recovery artefacts in gene or pathway content of related recovered genomes**: MEASURED AND MATERIAL, in natural human gut samples (direct same-sample isolate comparisons, n = 8 E. coli pairs [1]; real-data contamination of differential gene calls [22]) and in natural coastal marine samples (read-technology gene-count difference at equal estimated completeness [12]), with gene-class-specific losses across seawater, gut, chicken gut and phyllosphere catalogues [6].
>
> H1-02:A-022 [5. Verdicts] **Part A: measured and material** (natural human gut and marine).
>
> H1-02:A-023 [5. Verdicts] The loss of variable and mobile genes, and contamination-driven gains, were measured directly [1, 12, 22] and persist through completeness filters [3, 6, 9, 22].
>
> H1-02:C-001 [danger: Critic: verdict partly supported] **Reformulated verdict:** Part A: MEASURED AND MATERIAL, but only in natural human gut and, from a single source, coastal marine samples.
>
> H1-02:C-016 [danger: Critic: verdict partly supported] Part A mostly stands, but its three direct sources are each single-source and have caveats the verdict leaves out.
>
> H1-02:C-019 [danger: Critic: verdict partly supported] So Part A for gut rests on one isolate-comparison study (n = 8, one species) plus one mechanism-adjacent study.
>

## artefact-size.2 (claim)

Effect sizes are not commensurable across the three direct sources: the isolate comparison reports percentages of population core or variable genes, the read-technology study a median gene count, and the contamination study a fraction of differentially prevalent genes; they are reported separately and not pooled.

- conf: not stated
- class: not stated
- holds: the three direct natural-sample sources: same-sample isolate pairs, contamination-driven differential gene calls and matched read-technology pairs
- src: mezitiReliabilityMetagenomeassembledGenomes2021, orellanaComparingGenomesRecovered2023, majernikSmallAmountsMisassembly2025
- trail: H1-02 §4. Where

From the note:

> H1-02:B-0160 [4. Where the evidence is strongest, and its limits] The strongest evidence that recovery produces material content differences comes from three natural-sample sources that do not depend on each other: same-sample isolate pairs [1], contamination-driven differential gene calls [22], and matched read-technology pairs [12].
>
> H1-02:B-0164 [4. Where the evidence is strongest, and its limits] Effect sizes are not commensurable across them: [1] reports percentages of population core or variable genes, [12] reports a median gene count, and [22] reports a fraction of differentially prevalent genes.
>
> H1-02:B-0165 [4. Where the evidence is strongest, and its limits] They are reported separately here and not pooled.
>

## artefact-size.3 (claim)

Each of the three direct sources is single in its setting: two are human gut and one is coastal marine, and they measure different things.

- conf: single (note: "SINGLE SOURCE")
- class: not stated
- holds: same-sample isolate pairs and contamination-driven differential gene calls (human gut); matched read-technology pairs (coastal marine)
- src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023
- trail: H1-02 §4. Where, §Adversarial

From the note:

> H1-02:B-0160 [4. Where the evidence is strongest, and its limits] The strongest evidence that recovery produces material content differences comes from three natural-sample sources that do not depend on each other: same-sample isolate pairs [1], contamination-driven differential gene calls [22], and matched read-technology pairs [12].
>
> H1-02:B-0162 [4. Where the evidence is strongest, and its limits] All three direct sources are SINGLE SOURCE in their setting.
>
> H1-02:B-0163 [4. Where the evidence is strongest, and its limits] Two are human gut and one is coastal marine.
>
> H1-02:C-047 [warning: Adversarial critique, full findings] They measure different things in two environments, and each is single in its setting.
>

## artefact-size.4 (claim)

Removing Meziti et al. would leave Part A as "measured and material" on the contamination and read-technology sources, but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes, since Li and Yin reuse its data.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: mezitiReliabilityMetagenomeassembledGenomes2021, majernikSmallAmountsMisassembly2025, orellanaComparingGenomesRecovered2023, liCriticalAssessmentPangenomic2022
- trail: H1-02 §5. Verdicts

From the note:

> H1-02:A-038 [5. Verdicts] **Sensitivity to single sources.** Removing Meziti et al. [1] would leave Part A as "measured and material" on [22] and [12], but would remove the only natural same-sample isolate comparison and every figure for missed core and variable genes ([2] reuses [1]'s data).
>
> H1-02:B-0160 [4. Where the evidence is strongest, and its limits] The strongest evidence that recovery produces material content differences comes from three natural-sample sources that do not depend on each other: same-sample isolate pairs [1], contamination-driven differential gene calls [22], and matched read-technology pairs [12].
>

Not found in the cited text (where to look, not what is wrong): holds: review

## sample-dependence.1 (claim)

Part B is the weakest area for gene content: the sample-property dependence that has been measured concerns yield, completeness, chimerism or assembled fraction, not gene content.

- conf: not stated
- class: not stated
- holds: all sample types in the review
- src: none (the reviewer's synthesis)
- trail: H1-02 §4. Where, §critic

From the note:

> H1-02:B-0166 [4. Where the evidence is strongest, and its limits] The weakest area is Part B for gene content.
>
> H1-02:B-0167 [4. Where the evidence is strongest, and its limits] The sample-property dependence that has been measured concerns yield, completeness, chimerism or assembled fraction.
>
> H1-02:C-020 [danger: Critic: verdict partly supported] The Part B gut verdict ('measured and systematic for study of origin') contradicts the review's own Section 4, which says the measured dependence 'concerns yield, completeness, chimerism or assembled fraction', not gene content.
>

Not found in the cited text (where to look, not what is wrong): holds: in

## sample-dependence.2 (claim)

No study was found measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: the review's search
- src: none (a search result)
- trail: H1-02 §Search record

From the note:

> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## gut-dependence.1 (claim)

In the human gut, dependence of gene or pathway content artefacts on sample properties has not been measured. Proxies (chimerism rate, aligned fraction, ribosomal-protein absence by catalogue) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures: the body supports "not measured for gene content, indirect proxy evidence varies by catalogue".

- conf: not stated
- class: not stated
- rating: "MEASURED AND SYSTEMATIC for study of origin (pipeline)" (critic: C-007: NOT MEASURED for gene or pathway content)
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: natural human gut; none of the three catalogue sources measures artefact size in gene content against a study variable with sample set held constant, apart from aligned fraction, which is split by quality tier
- src: orakovGUNCDetectionChimerism2021, almeidaUnifiedCatalog2042020, miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §critic, §Adversarial, §Verdict as delivered

From the note:

> H1-02:C-007 [danger: Critic: verdict partly supported] Part B, human gut: NOT MEASURED for gene or pathway content.
>
> H1-02:C-008 [danger: Critic: verdict partly supported] Proxies (chimerism rate [9], aligned fraction [10], ribosomal-protein absence by catalogue [6]) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures.
>
> H1-02:C-020 [danger: Critic: verdict partly supported] The Part B gut verdict ('measured and systematic for study of origin') contradicts the review's own Section 4, which says the measured dependence 'concerns yield, completeness, chimerism or assembled fraction', not gene content.
>
> H1-02:C-023 [danger: Critic: verdict partly supported] The body therefore supports 'not measured for gene content, indirect proxy evidence varies by catalogue'.
>
> H1-02:C-087 [warning: Adversarial critique, full findings] - The Part B gut verdict relabels pipeline or catalogue differences as 'study of origin' dependence of gene-content artefacts. That is a reviewer construction: none of [6], [9] or [10] measures artefact size in gene content against a study variable with sample set held constant, apart from [10]'s aligned fraction, which is split by quality tier.
>
> H1-02:A-006 [quote: Verdict as delivered] **B. Dependence on sample properties: human gut (natural)**: MEASURED AND SYSTEMATIC for study of origin (pipeline): chimerism rates in CheckM-filtered catalogues differ about twofold between studies [9]; conspecific genomes from the same samples differ in aligned fraction by quality tier [10]; ribosomal-protein-gene absence differs by catalogue [6].
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

## gut-dependence.2 (claim)

For the same 1,554 gut samples binned by three studies, conspecific genomes had a median aligned fraction of 94.5% at 90% completeness or more and 86.6% at medium quality, so different pipelines applied to identical reads disagreed on roughly 5% to 13% of aligned sequence, with the gap set by quality tier.

- conf: not stated
- class: meas (note: "measured; gene content was not compared")
- holds: natural human gut; aligned sequence, not genes; reported by quality tier, not by study
- src: almeidaUnifiedCatalog2042020
- trail: H1-02 §3.1, §critic

From the note:

> H1-02:B-0121 [3.1 Human gut (natural)] For the same 1,554 gut samples binned by three studies, conspecific genomes had a median aligned fraction of 94.5% at 90% completeness or more and 86.6% at medium quality [10].
>
> H1-02:B-0122 [3.1 Human gut (natural)] Different pipelines applied to identical reads therefore disagreed on roughly 5% to 13% of aligned sequence, with the gap set by quality tier (measured; gene content was not compared).
>
> H1-02:C-022 [danger: Critic: verdict partly supported] [10] reports aligned fraction by quality tier, not by study.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## gut-dependence.3 (claim)

Chimerism in CheckM-prefiltered gut catalogues ranged from 15.1% to 29.9% by study, about twofold between studies; study of origin is confounded with pipeline and sample set.

- conf: not stated
- class: not stated
- holds: natural human gut MAG catalogues; chimerism, not gene content
- src: orakovGUNCDetectionChimerism2021
- trail: H1-02 §3.1, §critic

From the note:

> H1-02:B-0123 [3.1 Human gut (natural)] Chimerism in CheckM-prefiltered catalogues ranged from 15.1% to 29.9% by study [9].
>
> H1-02:A-006 [quote: Verdict as delivered] **B. Dependence on sample properties: human gut (natural)**: MEASURED AND SYSTEMATIC for study of origin (pipeline): chimerism rates in CheckM-filtered catalogues differ about twofold between studies [9]; conspecific genomes from the same samples differ in aligned fraction by quality tier [10]; ribosomal-protein-gene absence differs by catalogue [6].
>
> H1-02:C-021 [danger: Critic: verdict partly supported] In [9], study of origin is confounded with pipeline and sample set.
>

Not found in the cited text (where to look, not what is wrong): holds: mag

## gut-dependence.4 (claim)

Ribosomal-protein-gene absence was present or absent depending on the catalogue.

- conf: not stated
- class: not stated
- holds: natural gut MAG catalogues; catalogue is confounded with pipeline and sample set
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §3.1, §critic

From the note:

> H1-02:B-0124 [3.1 Human gut (natural)] Ribosomal-protein-gene absence was present or absent depending on the catalogue [6].
>
> H1-02:C-008 [danger: Critic: verdict partly supported] Proxies (chimerism rate [9], aligned fraction [10], ribosomal-protein absence by catalogue [6]) differ between catalogues, but catalogue is confounded with pipeline and sample set, and the review's own Section 4 says these are not gene-content measures.
>

Not found in the cited text (where to look, not what is wrong): holds: gut; holds: mag

## gut-dependence.5 (claim)

GUNC-flagged chimerism varied by binner, and Kim et al. state that it "did not correlate with sequencing depth": an unquantified sentence from one benchmark, with no reported statistic, figure panel or stated dataset range, and it is unclear which datasets it covers; the chimerism figures shown are gut datasets. It is the only negative result on depth and has no ground truth.

- conf: single (note: "SINGLE SOURCE")
- class: assert (critic: C-043)
- holds: real gut datasets (the chimerism figures shown); one benchmark of binning tools
- src: kimComprehensiveBenchmarkingMetagenomic2026
- trail: H1-02 §3.1, §critic, §Adversarial, §5. Verdicts

From the note:

> H1-02:B-0125 [3.1 Human gut (natural)] Kim et al. [27] found that GUNC-flagged chimerism in real gut, ocean and soil samples varied by binner and "did not correlate with sequencing depth".
>
> H1-02:B-0126 [3.1 Human gut (natural)] This is the one explicit negative result on depth.
>
> H1-02:B-0127 [3.1 Human gut (natural)] It has no ground truth and is a SINGLE SOURCE.
>
> H1-02:C-009 [danger: Critic: verdict partly supported] The depth null [27] is an unquantified sentence from one benchmark, and it is unclear which datasets it covers.
>
> H1-02:C-033 [danger: Critic: verdict partly supported] (iv) [27]'s 'did not correlate with sequencing depth' has no reported statistic.
>
> H1-02:C-034 [danger: Critic: verdict partly supported] The review extends it to 'real gut, ocean and soil samples', but the chimerism figures shown are gut datasets.
>
> H1-02:C-043 [warning: Adversarial critique, full findings] - Kim et al. [27]: the depth-chimerism statement is a sentence with no statistic, figure panel or stated dataset range. It is asserted-class evidence and was tagged as a measured negative result.
>
> H1-02:A-009 [quote: Verdict as delivered] That study had no ground truth and is a SINGLE SOURCE.
>
> H1-02:A-030 [5. Verdicts] Chimerism was reported as not correlated with depth [27] (single source, no ground truth).
>
> H1-02:A-041 [5. Verdicts] Removing Kim et al. [27] would remove the only negative result on depth.
>
> H1-02:B-0168 [4. Where the evidence is strongest, and its limits] The one negative result (chimerism against depth [27]) has no ground truth.
>

## gut-dependence.6 (claim)

Dependence of gene-content artefacts on community diversity and sequencing depth has not been measured in the gut: no gut study measured how gene-content artefacts scale with community diversity.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: natural human gut
- src: none (a search result)
- trail: H1-02 §3.1, §Verdict as delivered, §5. Verdicts

From the note:

> H1-02:A-007 [quote: Verdict as delivered] Dependence on community diversity and sequencing depth: NOT MEASURED for gene content in the gut.
>
> H1-02:A-029 [5. Verdicts] Not measured for diversity.
>
> H1-02:B-0128 [3.1 Human gut (natural)] No gut study measured how gene-content artefacts scale with community diversity.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

Not found in the cited text (where to look, not what is wrong): holds: human

## marine-dependence.1 (claim)

In marine samples, dependence of gene content on a sample property has been measured for read technology only, in a single source, and confounded with depth: one study of 4 samples.

- conf: single (critic: C-010)
- class: not stated
- rating: "MEASURED AND SYSTEMATIC for read technology" (critic: C-024: 'systematic' is too strong for n = 1 study)
- holds: natural coastal marine; 4 North Sea samples, one time series
- src: orellanaComparingGenomesRecovered2023
- trail: H1-02 §critic, §Adversarial, §Verdict as delivered

From the note:

> H1-02:C-010 [danger: Critic: verdict partly supported] Part B, marine: MEASURED for read technology only, SINGLE SOURCE [12], confounded with depth.
>
> H1-02:C-024 [danger: Critic: verdict partly supported] The marine read-technology verdict rests on one study of 4 samples with a depth confound, so 'systematic' is too strong for n = 1 study.
>
> H1-02:C-049 [warning: Adversarial critique, full findings] - Marine Part B verdict 'measured and systematic for read technology' rests on Orellana et al. [12]: 4 North Sea samples, one time series. 'Systematic' is a field-level phrasing for n = 1 study.
>
> H1-02:A-010 [quote: Verdict as delivered] **B. Dependence on sample properties: marine / seawater (natural)**: MEASURED AND SYSTEMATIC for read technology, but this rests on a SINGLE SOURCE for gene content: about 9% fewer predicted genes in short-read than long-read MAG pairs from the same DNA, at equal CheckM completeness [12].
>

Not found in the cited text (where to look, not what is wrong): holds: coastal

## marine-dependence.2 (claim)

In marine samples, dependence of gene content on diversity or depth has not been measured; the evidence covers MAG yield only.

- conf: not stated
- class: search (note: "Not found, with routes")
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: natural marine and seawater
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §Verdict as delivered, §critic, §5. Verdicts

From the note:

> H1-02:A-012 [quote: Verdict as delivered] Dependence on diversity and depth: NOT MEASURED for gene content.
>
> H1-02:A-013 [quote: Verdict as delivered] The evidence covers MAG yield only [16].
>
> H1-02:C-011 [danger: Critic: verdict partly supported] NOT MEASURED for diversity or depth.
>
> H1-02:A-032 [5. Verdicts] Not measured for diversity or depth.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

Not found in the cited text (where to look, not what is wrong): holds: marine; holds: seawater

## marine-dependence.3 (claim)

In one rarefied surface-ocean data set, MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.

- conf: not stated
- class: not stated
- holds: one surface-ocean data set; yield, not content
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §3.2

From the note:

> H1-02:B-0130 [3.2 Marine (natural)] For depth, Royalty and Steen [16] rarefied one surface-ocean data set: MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.
>
> H1-02:B-0131 [3.2 Marine (natural)] That result concerns yield, not content.
>

## marine-dependence.4 (claim)

The ribosomal-protein deficit disappeared in long-read catalogues, which supports the read-technology dependence across catalogues rather than in matched samples.

- conf: not stated
- class: not stated
- holds: a cross-catalogue comparison, not matched samples; indirect for gene content
- src: miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §3.2, §Verdict as delivered, §5. Verdicts

From the note:

> H1-02:B-0129 [3.2 Marine (natural)] Read technology changed the gene count of the same populations [12], and the ribosomal-protein deficit disappeared in long-read catalogues [6] (a cross-catalogue comparison, not matched samples).
>
> H1-02:A-011 [quote: Verdict as delivered] Mise and Iwasaki [6] support it across catalogues rather than matched samples.
>
> H1-02:A-031 [5. Verdicts] - Marine: **measured and systematic** for read technology [12] (SINGLE SOURCE for gene content; [6] indirect).
>

## marine-dependence.5 (claim)

Removing Orellana et al. would change the marine Part B verdict to "not measured" for gene content, and marine Part A would then rest on Mise and Iwasaki alone.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: orellanaComparingGenomesRecovered2023, miseUnexpectedAbsenceRibosomal2022
- trail: H1-02 §5. Verdicts

From the note:

> H1-02:A-039 [5. Verdicts] Removing Orellana et al. [12] would change the marine Part B verdict to "not measured" for gene content, and marine Part A would then rest on [6] alone.
>
> H1-02:B-0050 [2.2 Real-data artefacts without an isolate reference (natural)] Mise and Iwasaki [6] examined more than 190,000 MAGs.
>
> H1-02:B-0063 [2.3 Read technology on the same DNA (natural, marine)] Orellana et al. [12] sequenced the same North Sea DNA extracts with Illumina and PacBio HiFi.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## soil-sediment.1 (claim)

For soils and sediments, a gene-content comparison between related recovered genomes and a closed or isolate reference has not been measured in the sources found. The critic: the search missed relevant data (Alneberg et al. 2018, a MAG-against-SAG comparison; Mise and Iwasaki's own soil assemblies), so the absence reflects the search more than the literature, and it echoes the absence the brief expected.

- conf: not stated
- class: search (note: "No equivalent study was found")
- rating: "NOT MEASURED"
- search: searched, not found (note: "No equivalent study was found for soil, sediment or any other high-diversity natural environment")
- holds: natural soils, sediments and other high-diversity environments; routes: WebSearch and Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons; the closest hit (mangrove long-read, 2023) reported no gene-content difference
- src: none (a search result)
- trail: H1-02 §1. Scope, §Search record, §critic, §Adversarial

From the note:

> H1-02:A-004 [quote: Verdict as delivered] For soils and sediments, a gene-content comparison between related recovered genomes and a closed or isolate reference was NOT MEASURED in the sources found.
>
> H1-02:A-025 [5. Verdicts] For soils and sediments the setting has **not been measured** at gene-content level.
>
> H1-02:C-006 [danger: Critic: verdict partly supported] Soil and sediment: NOT MEASURED IN THIS SETTING.
>
> H1-02:C-025 [danger: Critic: verdict partly supported] Soil and sediment 'not measured' is consistent with the body, but the search missed relevant data (Alneberg et al. 2018 MAG-against-SAG comparison; Mise and Iwasaki's own soil assemblies).
>
> H1-02:C-095 [warning: Adversarial critique, full findings] The soil and sediment 'not measured' verdict echoes the brief's expected absence.
>
> H1-02:C-096 [warning: Adversarial critique, full findings] It is partly search-limited: the search missed SAG-referenced comparisons (Alneberg 2018) and soil assembly data inside a source it already cites ([6]).
>
> H1-02:C-097 [warning: Adversarial critique, full findings] The absence therefore reflects the search more than the literature, and the Search record should say so.
>
> H1-02:B-0031 [1. Scope of the evidence] No equivalent study was found for soil, sediment or any other high-diversity natural environment (routes in the Search record).
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0182 [Search record] Routes: WebSearch ("soil metagenome-assembled genomes compared to isolate genomes from the same soil sample gene content"), Europe PMC title and abstract queries on MAG against isolate same sample, and long-read sediment comparisons.
>
> H1-02:B-0183 [Search record] The closest hit (mangrove long-read, 2023) reported no gene-content difference.
>

## soil-sediment.2 (claim)

In soil, gene or pathway content of related recovered genomes has not been measured; there is indirect recovery-quality evidence only.

- conf: not stated
- class: search (note: "Not found, with routes")
- rating: "NOT MEASURED IN THIS SETTING"
- search: searched, not found (note: "Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth")
- holds: natural soil; none of the soil studies measures the gene or pathway content of related genomes recovered from different soil samples
- src: none (a search result)
- trail: H1-02 §3.3, §Verdict as delivered, §critic

From the note:

> H1-02:A-014 [quote: Verdict as delivered] **B. Dependence on sample properties: soil (natural)**: NOT MEASURED IN THIS SETTING for gene or pathway content of related recovered genomes.
>
> H1-02:A-033 [5. Verdicts] - Soil: **not measured in this setting**.
>
> H1-02:C-012 [danger: Critic: verdict partly supported] Part B, soil and sediment: NOT MEASURED IN THIS SETTING, with indirect recovery-quality evidence only.
>
> H1-02:B-0141 [3.3 Soil (natural)] None of it measures the gene or pathway content of related genomes recovered from different soil samples.
>
> H1-02:B-0181 [Search record] Not found, with routes: (1) A soil or sediment study comparing gene content of MAGs with isolate or closed genomes of the same lineage.
>
> H1-02:B-0186 [Search record] (3) Any study measuring how gene-content artefacts between conspecific MAGs scale with community diversity or depth across samples.
>
> H1-02:B-0187 [Search record] Routes: WebSearch and Europe PMC on sequencing effort against binning, batch or study effects in MAG catalogues, and soil MAG against depth.
>

## soil-sediment.3 (claim)

Recovery (assembly fraction, MAG yield, bin quality) in soil depends systematically on diversity, depth, habitat and binner, and short-read assembly loss tracks within-sample coverage and population sequence variation.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: natural soils; recovery quality, not gene content; the critic: several of the figures behind it are unverified second-hand figures, resting on search-agent reads
- src: johansenUnveilingSoilMicrobial2025, sereikaGenomeresolvedLongreadSequencing2025, kimComprehensiveBenchmarkingMetagenomic2026, panDeepSiameseNeural2022, bergComparisonShortreadLongread2025
- trail: H1-02 §3.3, §Verdict as delivered, §5. Verdicts, §Adversarial

From the note:

> H1-02:A-015 [quote: Verdict as delivered] Indirect support only: recovery (assembly fraction, MAG yield, bin quality) depends systematically on field diversity and depth [28], habitat [17] and binner [27, 31], and short-read assembly loss tracks within-sample coverage and population sequence variation [26].
>
> H1-02:A-034 [5. Verdicts] There is indirect evidence that recovery quality varies systematically with diversity, depth, habitat and binner [17, 26, 27, 28, 31].
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>
> H1-02:C-042 [warning: Adversarial critique, full findings] These are not breaches as such, but they are unverified second-hand figures, and several carry weight in the soil Part B indirect evidence.
>

Not found in the cited text (where to look, not what is wrong): holds: search-agent

## soil-sediment.4 (claim)

Danish agricultural soils sequenced to a mean depth of 107 Gb reached 73% Nonpareil coverage in the less diverse clay field against 47% in sandy fields, and reads assembled into contigs longer than 2 kb were 57% (clay) against 27% (sandy); co-assembly raised both.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: natural Danish agricultural soils; the critic: not re-opened at synthesis, an unverified second-hand figure resting on search-agent reads
- src: johansenUnveilingSoilMicrobial2025
- trail: H1-02 §3.3, §Adversarial

From the note:

> H1-02:B-0132 [3.3 Soil (natural)] - Johansen et al. [28] sequenced Danish agricultural soils to a mean depth of 107 Gb.
>
> H1-02:B-0133 [3.3 Soil (natural)] The less diverse clay field reached 73% Nonpareil coverage, against 47% for sandy fields.
>
> H1-02:B-0134 [3.3 Soil (natural)] Reads assembled into contigs longer than 2 kb were 57% (clay) against 27% (sandy), and co-assembly raised both.
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>

Not found in the cited text (where to look, not what is wrong): holds: second-hand

## soil-sediment.5 (claim)

Agricultural soils had the lowest assembled fraction and MAG yield, and coastal samples still yielded more MAGs after depth normalisation.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: natural terrestrial habitats, long-read sequencing; n = 3 + 3 for the depth-normalised comparison; the critic: not re-opened at synthesis
- src: sereikaGenomeresolvedLongreadSequencing2025
- trail: H1-02 §3.3, §Adversarial

From the note:

> H1-02:B-0135 [3.3 Soil (natural)] - Sereika et al. 2025 [17] found the lowest assembled fraction and MAG yield in agricultural soils, and coastal samples still yielded more MAGs after depth normalisation (n = 3 + 3).
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:R-0118 [References] Genome-resolved long-read sequencing expands known microbial diversity across terrestrial habitats.
>

Not found in the cited text (where to look, not what is wrong): holds: depth-normalised

## soil-sediment.6 (claim)

Rarefaction gave the longest MAG-yield lag for maize soil (6.1 Gbp).

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: one maize soil data set, rarefied; yield, not content
- src: royaltyTheoreticalSimulationBasedInvestigation2019
- trail: H1-02 §3.3, §3.2

From the note:

> H1-02:B-0136 [3.3 Soil (natural)] - Royalty and Steen [16] give the longest lag for maize soil (6.1 Gbp).
>
> H1-02:B-0130 [3.2 Marine (natural)] For depth, Royalty and Steen [16] rarefied one surface-ocean data set: MAG yield followed a Gompertz curve (lag 1.2 Gbp) and declined above about 25 Gbp.
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>

## soil-sediment.7 (claim)

Most binners struggled to recover high-quality soil genomes at depths comparable to gut and ocean.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: natural soil, gut and ocean data in one benchmark of binning tools
- src: kimComprehensiveBenchmarkingMetagenomic2026
- trail: H1-02 §3.3

From the note:

> H1-02:B-0137 [3.3 Soil (natural)] - Kim et al. [27] report that most binners struggled to recover high-quality soil genomes at depths comparable to gut and ocean.
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>

## soil-sediment.8 (claim)

SemiBin's gains over other binners were largest in soil.

- conf: not stated
- class: meas (note: "All of this is measured and natural")
- holds: microbiome datasets across different environments; the critic: not re-opened at synthesis
- src: panDeepSiameseNeural2022
- trail: H1-02 §3.3, §Adversarial

From the note:

> H1-02:B-0138 [3.3 Soil (natural)] - SemiBin gains over other binners were largest in soil [31].
>
> H1-02:B-0140 [3.3 Soil (natural)] All of this is measured and natural, and it shows that recovery quality in soil depends systematically on diversity, depth and binner.
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:R-0161 [References] A deep siamese neural network improves metagenome-assembled genomes in microbiome datasets across different environments.
>

## soil-sediment.9 (claim)

For sediments, the only evidence is one estuarine sediment rarefaction (MAG yield; lag 3.7 Gbp, lowest maximum yield) and habitat-level yield for coastal sediments; nothing was found on content artefacts.

- conf: not stated
- class: search (note: "Nothing was found on content artefacts")
- rating: "NOT MEASURED IN THIS SETTING"
- search: searched, not found (note: "Nothing was found on content artefacts")
- holds: natural sediments; MAG yield only; the critic: deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, were not searched by name
- src: royaltyTheoreticalSimulationBasedInvestigation2019, sereikaGenomeresolvedLongreadSequencing2025
- trail: H1-02 §3.4, §Verdict as delivered, §5. Verdicts, §Adversarial

From the note:

> H1-02:B-0144 [3.4 Sediment (natural)] The only evidence is one estuarine sediment rarefaction (MAG yield; lag 3.7 Gbp, lowest maximum yield) [16] and habitat-level yield for coastal sediments [17].
>
> H1-02:B-0145 [3.4 Sediment (natural)] Nothing was found on content artefacts.
>
> H1-02:A-016 [quote: Verdict as delivered] **B. Dependence on sample properties: sediment (natural)**: NOT MEASURED IN THIS SETTING.
>
> H1-02:A-017 [quote: Verdict as delivered] The only data are MAG yield against depth in one estuarine data set [16] and habitat-level yield for coastal sediments [17].
>
> H1-02:A-035 [5. Verdicts] - Sediment: **not measured in this setting** (yield only [16, 17]).
>
> H1-02:C-077 [warning: Adversarial critique, full findings] - gap: Sediments: only yield data.
>
> H1-02:C-078 [warning: Adversarial critique, full findings] Deep-sea, freshwater and estuarine sediment long-read against short-read comparisons, and sediment SAG-MAG comparisons, were not searched by name.
>

## soil-sediment.10 (claim)

A long-read mangrove sediment study compares MAG counts and collinearity between Illumina, PacBio and hybrid assemblies and reports no gene-content difference.

- conf: not stated
- class: not stated
- holds: mangrove sediments; full text obtained but not used as a finding; the critic: the review did not report its gene-content statements
- src: zhangLongreadAssembledMetagenomic2023
- trail: H1-02 §Sources not obtained, §Search record, §Adversarial

From the note:

> H1-02:R-0057 [failure: Sources not obtained] - Long-read mangrove sediment study: Long-read assembled metagenomic approaches improve our understanding on metabolic potentials of microbial community in mangrove sediments.
>
> H1-02:R-0058 [failure: Sources not obtained] Microbiome (2023). https://doi.org/10.1186/s40168-023-01630-x (PMC10464287) (routes tried: Full text obtained via Europe PMC; it compares MAG counts and collinearity between Illumina, PacBio and hybrid assemblies but reports no gene-content difference; not used as a finding; reference not Crossref-checked)
>
> H1-02:R-0068 [failure: Sources not obtained] - Long-read assembled metagenomic approaches improve our understanding on metabolic potentials of microbial community in mangrove sediments.
>
> H1-02:R-0069 [failure: Sources not obtained] Microbiome (2023). https://doi.org/10.1186/s40168-023-01630-x (authors not Crossref-checked) (routes tried: Full text obtained (PMC10464287); reports MAG counts and collinearity but no gene-content difference; not used.)
>
> H1-02:B-0183 [Search record] The closest hit (mangrove long-read, 2023) reported no gene-content difference.
>
> H1-02:C-079 [warning: Adversarial critique, full findings] The mangrove study was obtained but its gene-content statements were not reported.; setting_or_class: Marine, estuarine and freshwater sediments; brief_bullet: Targeted search: 'sediment long-read metagenome MAG gene content short-read comparison'; 'subseafloor SAG MAG'.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## soil-sediment.11 (claim)

No Part B verdict in soil or sediment depends on any single source, because none reaches gene content.

- conf: not stated
- class: not stated
- holds: the review's sensitivity analysis
- src: none (the reviewer's synthesis)
- trail: H1-02 §5. Verdicts

From the note:

> H1-02:A-042 [5. Verdicts] No Part B verdict in soil or sediment depends on any single source, because none reaches gene content.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## engineered-simulated.1 (claim)

Mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies; genomes with close relatives assembled far worse, and strain diversity degraded completeness and purity.

- conf: not stated
- class: model (note: "modelled")
- holds: the CAMI II benchmark
- src: meyerCriticalAssessmentMetagenome2022
- trail: H1-02 §3.5, §Verdict as delivered

From the note:

> H1-02:B-0146 [3.5 Engineered systems and simulations (kept separate)] In CAMI II [7], mean bin completeness fell from 36.9% (marine gold-standard assembly) to 18.2% under high strain diversity, and to 5.2% on MEGAHIT assemblies.
>
> H1-02:B-0147 [3.5 Engineered systems and simulations (kept separate)] Genomes with close relatives assembled far worse (modelled).
>
> H1-02:A-018 [quote: Verdict as delivered] **B. Dependence on sample properties: engineered systems and simulations (kept separate)**: MEASURED AND SYSTEMATIC in simulations (strain diversity degrades completeness and purity [7]; depth effects are pipeline-dependent [34]).
>

## engineered-simulated.2 (claim)

No clear effect of close relatives was found in a 30-genome community.

- conf: not stated
- class: model (note: "modelled")
- holds: one low-complexity simulation (30 genomes)
- src: maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §3.5, §Verdict as delivered

From the note:

> H1-02:B-0148 [3.5 Engineered systems and simulations (kept separate)] Maguire et al. [4] found no clear effect of close relatives in a 30-genome community (modelled).
>
> H1-02:A-019 [quote: Verdict as delivered] One low-complexity simulation found no effect of close relatives [4].
>

## engineered-simulated.3 (claim)

Completeness correlated with depth at ρ = 0.20 and with taxonomic complexity at ρ = −0.55.

- conf: not stated
- class: model (note: "modelled")
- holds: Kim et al.'s simulations
- src: kimComprehensiveBenchmarkingMetagenomic2026
- trail: H1-02 §3.5

From the note:

> H1-02:B-0149 [3.5 Engineered systems and simulations (kept separate)] Kim et al.'s simulations [27] gave completeness correlations of ρ = 0.20 with depth and ρ = −0.55 with taxonomic complexity (modelled).
>

## engineered-simulated.4 (claim)

Depth effects on true-positive recovery reversed between pipelines around 60 million reads: depth effects are pipeline-dependent.

- conf: not stated
- class: model (note: "modelled")
- holds: simulations of 69 microbial communities; the critic: not re-opened at synthesis
- src: rochaSimulation69Microbial2024
- trail: H1-02 §3.5, §Adversarial

From the note:

> H1-02:B-0150 [3.5 Engineered systems and simulations (kept separate)] Rocha et al. [34] found that depth effects on true-positive recovery reversed between pipelines around 60 million reads (modelled).
>
> H1-02:A-018 [quote: Verdict as delivered] **B. Dependence on sample properties: engineered systems and simulations (kept separate)**: MEASURED AND SYSTEMATIC in simulations (strain diversity degrades completeness and purity [7]; depth effects are pipeline-dependent [34]).
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:R-0170 [References] Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in prokaryotic metagenome-assembled genome recovery.
>

## engineered-simulated.5 (claim)

In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs, and microdiversity increased fragmentation.

- conf: not stated
- class: not stated
- holds: engineered; one anaerobic digester sample
- src: sereikaOxfordNanoporeR102022
- trail: H1-02 §3.5

From the note:

> H1-02:B-0151 [3.5 Engineered systems and simulations (kept separate)] In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs, and microdiversity increased fragmentation [29].
>
> H1-02:B-0153 [3.5 Engineered systems and simulations (kept separate)] Both are engineered.
>

## engineered-simulated.6 (claim)

Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases.

- conf: not stated
- class: not stated
- holds: engineered; activated sludge
- src: singletonConnectingStructureFunction2021
- trail: H1-02 §3.5

From the note:

> H1-02:B-0152 [3.5 Engineered systems and simulations (kept separate)] Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases [30].
>
> H1-02:B-0153 [3.5 Engineered systems and simulations (kept separate)] Both are engineered.
>

## engineered-simulated.7 (claim)

In engineered bioreactors, read technology changes contiguity and rRNA recovery.

- conf: not stated
- class: not stated
- holds: one anaerobic digester sample and activated sludge
- src: sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021
- trail: H1-02 §Verdict as delivered, §3.5

From the note:

> H1-02:A-020 [quote: Verdict as delivered] In engineered bioreactors, read technology changes contiguity and rRNA recovery [29, 30].
>
> H1-02:B-0151 [3.5 Engineered systems and simulations (kept separate)] In one anaerobic digester sample, long reads gave far more high-quality, less fragmented MAGs, and microdiversity increased fragmentation [29].
>
> H1-02:B-0152 [3.5 Engineered systems and simulations (kept separate)] Long-read activated-sludge MAGs carried full rRNA operons in 91.3% of cases [30].
>
> H1-02:B-0153 [3.5 Engineered systems and simulations (kept separate)] Both are engineered.
>

## engineered-simulated.8 (claim)

Multi-sample binning identified 22% to 30% more potential ARG hosts than single-sample binning, so processing mode alone changes how many genomes carry an annotated trait.

- conf: not stated
- class: meas (note: "measured; mixed natural and engineered")
- holds: real marine, cheese, gut and sludge data; the critic: an unverified second-hand figure, resting on search-agent reads with no cross-agent confirmation
- src: hanBenchmarkingMetagenomicBinning2025
- trail: H1-02 §3.5, §Adversarial

From the note:

> H1-02:B-0154 [3.5 Engineered systems and simulations (kept separate)] Han et al. [32] found that multi-sample binning identified 22% to 30% more potential ARG hosts than single-sample binning on real marine, cheese, gut and sludge data.
>
> H1-02:B-0155 [3.5 Engineered systems and simulations (kept separate)] Processing mode alone thus changes how many genomes carry an annotated trait (measured; mixed natural and engineered).
>
> H1-02:C-040 [warning: Adversarial critique, full findings] - Nayfach et al. 2019 [21], Pasolli et al. [25], Gautreau et al. [20], Johansen et al. [28], Sereika et al. [17], Pan et al. [31], Han et al. [32], Rocha et al. [34] and Maranga et al. [35]: none was re-opened at synthesis.
>
> H1-02:C-041 [warning: Adversarial critique, full findings] Their figures rest on search-agent reads with no cross-agent confirmation, including the Han 22% to 30% ARG-host figure, Johansen's 57% against 27% and 73% against 47%, and Gautreau's 55 of 78 species.
>

Not found in the cited text (where to look, not what is wrong): holds: second-hand

## engineered-simulated.9 (claim)

In simulations and engineered systems, strain diversity and read technology have systematic effects, with one null for close relatives; these do not answer the question for natural samples.

- conf: not stated
- class: not stated
- rating: "MEASURED AND SYSTEMATIC in simulations"
- holds: simulations and engineered bioreactors; the critic accepts this verdict as stated
- src: meyerCriticalAssessmentMetagenome2022, rochaSimulation69Microbial2024, sereikaOxfordNanoporeR102022, singletonConnectingStructureFunction2021, maguireMetagenomeAssembledGenomeBinning2020
- trail: H1-02 §Verdict as delivered, §5. Verdicts, §critic

From the note:

> H1-02:A-018 [quote: Verdict as delivered] **B. Dependence on sample properties: engineered systems and simulations (kept separate)**: MEASURED AND SYSTEMATIC in simulations (strain diversity degrades completeness and purity [7]; depth effects are pipeline-dependent [34]).
>
> H1-02:A-021 [quote: Verdict as delivered] None of these answers the question for natural samples.
>
> H1-02:A-036 [5. Verdicts] - Engineered systems and simulations: systematic effects of strain diversity and read technology [7, 29, 30, 34], with one null for close relatives [4].
>
> H1-02:A-037 [5. Verdicts] These do not answer the natural-sample question.
>
> H1-02:C-014 [danger: Critic: verdict partly supported] Engineered systems and simulations: as stated, and they do not answer the natural-sample question.
>

Not found in the cited text (where to look, not what is wrong): holds: bioreactors

## dns.1 (do not say)

"Meziti et al. found true recovery 16.9% to 20.4% below the completeness estimates."

- why: The two figures are not a range: they are average shortfalls against two estimators, 16.9% against MiGA and 20.4% against CheckM.
- instead: completeness-estimates.2
- trail: H1-02 §critic

From the note:

> H1-02:B-0119 [2.7 Filters and corrections: real-sample validation] Meziti et al. found true recovery 16.9% to 20.4% below the estimates [1] (measured, natural, single source).
>
> H1-02:C-026 [danger: Critic: verdict partly supported] Figure-level errors: (i) [1]'s '16.9% to 20.4%' is not a range.
>
> H1-02:C-027 [danger: Critic: verdict partly supported] The paper reports average shortfalls against two estimators: 'lower than the completeness assessments of MiGA and CheckM, by 16.9% and 20.4%, respectively, on average'.
>

Not found in the cited text (where to look, not what is wrong): "Meziti et al. found true recovery 16.9% to 20.4% below the completeness estimates."

## dns.2 (do not say)

"The MAGs had CheckM/MiGA completeness estimates of 81.1% to 97.2%."

- why: The range mixes estimator columns; the paper's text gives MiGA MAG completeness as 81.1% to 95.5%.
- instead: completeness-estimates.3
- trail: H1-02 §critic

From the note:

> H1-02:B-0033 [2.1 Direct same-sample comparisons (natural, human gut)] The MAGs had CheckM/MiGA completeness estimates of 81.1% to 97.2%.
>
> H1-02:C-028 [danger: Critic: verdict partly supported] (ii) The quoted completeness range 81.1% to 97.2% mixes estimator columns.
>
> H1-02:C-029 [danger: Critic: verdict partly supported] The paper's text gives MiGA MAG completeness as 81.1% to 95.5%.
>

## dns.3 (do not say)

"The main mechanism of gene loss in MAGs was mis-binning among co-occurring relatives, not a failure to sequence."

- why: That is the reviewer's inference and over-reads the paper, which attributes the low-identity share of missed genes to sequence divergence from the isolate or to assembly errors, so part of the loss may be biology and not recovery.
- instead: content-loss.3
- trail: H1-02 §critic, §Adversarial

From the note:

> H1-02:B-0038 [2.1 Direct same-sample comparisons (natural, human gut)] The main mechanism was therefore mis-binning among co-occurring relatives, not a failure to sequence.
>
> H1-02:C-030 [danger: Critic: verdict partly supported] (iii) The claim that 'the main mechanism was therefore mis-binning' over-reads [1].
>
> H1-02:C-031 [danger: Critic: verdict partly supported] The low-identity share of missed genes is attributed to sequence divergence from the isolate or to assembly errors.
>
> H1-02:C-084 [warning: Adversarial critique, full findings] - Section 2.1 states 'The main mechanism was therefore mis-binning among co-occurring relatives'.
>
> H1-02:C-085 [warning: Adversarial critique, full findings] That is the reviewer's inference.
>
> H1-02:C-086 [warning: Adversarial critique, full findings] [1] attributes low-identity missed genes to sequence differences from the isolate or to assembly errors, so part of the 'loss' may be biology and not recovery.
>

Not found in the cited text (where to look, not what is wrong): MAGs; "The main mechanism of gene loss in MAGs was mis-binning among co-occurring relatives, not a failure to sequence."

## dns.4 (do not say)

"Contamination produced apparent content differences between sample groups of recovered genomes."

- why: The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated; they are not content differences between genomes recovered from different samples.
- instead: contamination-gain.7
- trail: H1-02 §Adversarial

From the note:

> H1-02:B-0049 [2.2 Real-data artefacts without an isolate reference (natural)] The case is relevant here because the contamination did more than add noise: it produced apparent content differences between sample groups.
>
> H1-02:C-081 [warning: Adversarial critique, full findings] - [22] is presented as a case where contamination 'produced apparent content differences between sample groups' of recovered genomes.
>
> H1-02:C-082 [warning: Adversarial critique, full findings] The differential calls come from MIDAS2 read mapping to a reference pangenome that was partly contaminated.
>
> H1-02:C-083 [warning: Adversarial critique, full findings] They are not content differences between genomes recovered from different samples, so the review stretches [22] toward the brief's question without stating the mechanism difference.
>

Not found in the cited text (where to look, not what is wrong): "Contamination produced apparent content differences between sample groups of recovered genomes."

## dns.5 (do not say)

"The contamination filters in common use leave chimeric material in place."

- why: It generalises to the filters in common use from one chimerism survey plus one species-level case study.
- instead: contamination-gain.11
- trail: H1-02 §Adversarial

From the note:

> H1-02:B-0062 [2.2 Real-data artefacts without an isolate reference (natural)] Taken with [22], it shows that the contamination filters in common use leave chimeric material in place.
>
> H1-02:C-048 [warning: Adversarial critique, full findings] - 'Taken with [22], it shows that the contamination filters in common use leave chimeric material in place' (Section 2.2) generalises to 'filters in common use' from one chimerism survey [9] plus one species-level case study [22].
>

## dns.6 (do not say)

"A gene-count difference of about 9% between short- and long-read MAGs depended on read technology."

- why: It omits the paper's reported 3-fold difference in sequenced bases between platforms and attributes the effect to technology alone; read technology and depth are confounded.
- instead: read-technology.3
- trail: H1-02 §Adversarial

From the note:

> H1-02:B-0066 [2.3 Read technology on the same DNA (natural, marine)] Reviewer's reading: a gene-count difference of about 9%, which depended on read technology, was invisible to completeness estimates.
>
> H1-02:C-017 [danger: Critic: verdict partly supported] [12]'s gene-count gap is confounded with depth: the paper reports about 36 Gbp per sample for Illumina against 12 Gbp for PacBio.
>
> H1-02:C-088 [warning: Adversarial critique, full findings] - The Orellana reading ('a gene-count difference of about 9%, which depended on read technology') omits the paper's reported 3-fold difference in sequenced bases between platforms. It attributes the effect to technology alone.
>

Not found in the cited text (where to look, not what is wrong): MAGs; "A gene-count difference of about 9% between short- and long-read MAGs depended on read technology."

## dns.7 (do not say)

"Three natural-sample sources that do not depend on each other establish that recovery produces material content differences."

- why: The three sources measure different things in two environments, and each is single in its setting; together they do not establish a field-level finding.
- instead: artefact-size.1, artefact-size.3
- trail: H1-02 §Adversarial

From the note:

> H1-02:B-0160 [4. Where the evidence is strongest, and its limits] The strongest evidence that recovery produces material content differences comes from three natural-sample sources that do not depend on each other: same-sample isolate pairs [1], contamination-driven differential gene calls [22], and matched read-technology pairs [12].
>
> H1-02:C-046 [warning: Adversarial critique, full findings] Section 4 still presents [1], [22] and [12] as 'three natural-sample sources that do not depend on each other' as though together they establish a field-level finding.
>
> H1-02:C-047 [warning: Adversarial critique, full findings] They measure different things in two environments, and each is single in its setting.
>

Not found in the cited text (where to look, not what is wrong): "Three natural-sample sources that do not depend on each other establish that recovery produces material content differences."

## dns.8 (do not say)

"Only one natural-sample study has ever compared MAGs with isolate genomes of the same lineage from the same sample at gene level."

- why: The review frames it as a structural fact of the literature, but it is a statement about the search, and it omits SAG-referenced comparisons (Alneberg et al. 2018).
- instead: mag-recovery.3
- trail: H1-02 §Adversarial

From the note:

> H1-02:B-0029 [1. Scope of the evidence] Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level [1]: eight E. coli pairs from human stool.
>
> H1-02:C-052 [warning: Adversarial critique, full findings] - 'Only one natural-sample study compared MAGs with isolate genomes of the same lineage from the same sample at gene level' is framed as a structural fact of the literature. It is a statement about the search, and it omits SAG-referenced comparisons (Alneberg et al. 2018).
>

Not found in the cited text (where to look, not what is wrong): "Only one natural-sample study has ever compared MAGs with isolate genomes of the same lineage from the same sample at gene level."

## dns.9 (do not say)

"In the human gut, gene-content artefacts are measured and systematic for study of origin (pipeline)."

- why: The verdict contradicts the review's own Section 4, which says the measured dependence concerns yield, completeness, chimerism or assembled fraction, not gene content; study of origin is confounded with pipeline and sample set, and aligned fraction is reported by quality tier, not by study.
- instead: gut-dependence.1
- trail: H1-02 §critic, §Adversarial

From the note:

> H1-02:A-006 [quote: Verdict as delivered] **B. Dependence on sample properties: human gut (natural)**: MEASURED AND SYSTEMATIC for study of origin (pipeline): chimerism rates in CheckM-filtered catalogues differ about twofold between studies [9]; conspecific genomes from the same samples differ in aligned fraction by quality tier [10]; ribosomal-protein-gene absence differs by catalogue [6].
>
> H1-02:A-028 [5. Verdicts] - Human gut: **measured and systematic** for study of origin (pipeline) [6, 9, 10].
>
> H1-02:C-007 [danger: Critic: verdict partly supported] Part B, human gut: NOT MEASURED for gene or pathway content.
>
> H1-02:C-020 [danger: Critic: verdict partly supported] The Part B gut verdict ('measured and systematic for study of origin') contradicts the review's own Section 4, which says the measured dependence 'concerns yield, completeness, chimerism or assembled fraction', not gene content.
>
> H1-02:C-021 [danger: Critic: verdict partly supported] In [9], study of origin is confounded with pipeline and sample set.
>
> H1-02:C-022 [danger: Critic: verdict partly supported] [10] reports aligned fraction by quality tier, not by study.
>
> H1-02:C-023 [danger: Critic: verdict partly supported] The body therefore supports 'not measured for gene content, indirect proxy evidence varies by catalogue'.
>
> H1-02:C-087 [warning: Adversarial critique, full findings] - The Part B gut verdict relabels pipeline or catalogue differences as 'study of origin' dependence of gene-content artefacts. That is a reviewer construction: none of [6], [9] or [10] measures artefact size in gene content against a study variable with sample set held constant, apart from [10]'s aligned fraction, which is split by quality tier.
>

Not found in the cited text (where to look, not what is wrong): "In the human gut, gene-content artefacts are measured and systematic for study of origin (pipeline)."

## dns.10 (do not say)

"Without Orakov et al., the gut study-of-origin verdict would still be systematic on aligned sequence and ribosomal-protein absence."

- why: It rests on the gut verdict 'measured and systematic for study of origin', which the critic corrects to not measured for gene content, with indirect proxy evidence varying by catalogue.
- instead: gut-dependence.1
- trail: H1-02 §critic

From the note:

> H1-02:A-040 [5. Verdicts] Removing Orakov et al. [9] would leave the gut study-of-origin verdict on [10] (aligned sequence, not genes) and [6], which is weaker but still systematic.
>
> H1-02:C-020 [danger: Critic: verdict partly supported] The Part B gut verdict ('measured and systematic for study of origin') contradicts the review's own Section 4, which says the measured dependence 'concerns yield, completeness, chimerism or assembled fraction', not gene content.
>
> H1-02:C-023 [danger: Critic: verdict partly supported] The body therefore supports 'not measured for gene content, indirect proxy evidence varies by catalogue'.
>

Not found in the cited text (where to look, not what is wrong): "Without Orakov et al., the gut study-of-origin verdict would still be systematic on aligned sequence and ribosomal-protein absence."

## dns.11 (do not say)

"GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples."

- why: The statement is one unquantified sentence in Kim et al. with no reported statistic; the review extends it to real gut, ocean and soil samples, but the chimerism figures shown are gut datasets.
- instead: gut-dependence.5
- trail: H1-02 §critic, §Adversarial

From the note:

> H1-02:A-008 [quote: Verdict as delivered] One bounding fact is that GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples [27].
>
> H1-02:C-033 [danger: Critic: verdict partly supported] (iv) [27]'s 'did not correlate with sequencing depth' has no reported statistic.
>
> H1-02:C-034 [danger: Critic: verdict partly supported] The review extends it to 'real gut, ocean and soil samples', but the chimerism figures shown are gut datasets.
>
> H1-02:C-050 [warning: Adversarial critique, full findings] - Gut depth null: 'GUNC-estimated chimerism did not correlate with depth across real gut, ocean and soil samples' rests on one unquantified sentence in Kim et al. [27]. The review flags it as single source but still widens its regime.
>

