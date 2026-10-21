# Verdicts: packet-01 and packet-02

## packet-01

extraction.5: ok
extraction.7: ok
extraction.9: ok
primers.3: ok
primers.5: ok
copy-number.1: ok
copy-number.4: conf: `class: meas` rests on "measured from genomes", but the same quoted sentence labels the class explicitly as "derived class", so the text states deriv, not meas.
copy-number.14: ok
ploidy.6: ok
ploidy.19: ok
ploidy.22: ok
ploidy.25: absent: `holds` says the critic names the Prochlorococcus cell-cycle literature as the source that would supply such shares, but the quoted critique (MB-02:C-018) names no literature and no taxon; it says only that the review read the abstract.
copy-number-correction.4: holds: "genome-based prediction studies" is not in the quoted text, and the one quoted Edgar 2017 finding concerns read frequencies in mocks, not genome-based prediction.
copy-number-correction.12: ok
copy-number-correction.16: ok
community-copy-number.3: holds: the setting "EMP predictions" does not appear in the quoted text, which speaks only of copy-number estimates "for environments".
library-prep.4: ok
sequencing-platform.2: ok
index-misassignment.3: ok
quality-filtering.5: holds: the quoted 93% sentence gives no setting; "73 MiSeq datasets" comes from a different Schirmer 2015 finding (library preparation and primer bias, MB-01:I-0041) and is not stated as the setting of the error-correction result.
denoising-clustering.3: ok
denoising-clustering.4: ok
denoising-clustering.5: ok
chimeras.3: holds: "mock" is not in the quoted text; MB-01:B-0170 and A-073 give chimera rates and UCHIME sensitivity for Sze and Schloss 2019 without naming a mock community as the setting.
contamination.9: ok
workflow-bias.9: ok
workflow-bias.10: ok
bias-consistency.1: ok
bias-consistency.8: ok
bias-consistency.9: ok
read-depth.7: ok
abundance-distribution.1: ok
abundance-distribution.10: ok
abundance-distribution.19: ok
sampling-model.1: ok
sampling-model.3: ok
sampling-model.4: ok
sampling-model.5: ok
technical-replicates.1: ok
technical-replicates.4: ok
technical-replicates.8: holds: the text marks Smith and Peay 2014 as ITS (MB-01:B-0347), and `holds` omits it, so an ITS result stands in the no-effect group without its marker.
technical-replicates.10: ok
technical-variation.2: ok
technical-variation.4: ok
technical-variation.5: ok
technical-variation.8: ok
technical-variation.9: ok
alpha-diversity.2: ok
alpha-diversity.3: ok
alpha-diversity.5: ok
alpha-diversity.6: ok
beta-diversity.2: ok
beta-diversity.5: ok
rarefying.11: ok
richness-estimators.2: ok
richness-estimators.3: ok
richness-estimators.4: ok
compositional-analysis.1: ok
compositional-analysis.3: ok
differential-abundance.3: ok

## packet-02

differential-abundance.5: ok
differential-abundance.7: ok
differential-abundance.9: ok
absolute-quantification.1: ok
absolute-quantification.2: ok
absolute-quantification.6: ok
absolute-quantification.9: ok
absolute-quantification.14: ok
rare-biosphere.3: ok
rare-biosphere.4: ok
rare-biosphere.5: ok
rare-biosphere.7: ok
rare-biosphere.10: ok
global-classes.2: ok
core-microbiome.1: ok
core-microbiome.2: ok
core-microbiome.7: ok
abundance-occupancy.3: ok
abundance-occupancy.7: ok
abundance-occupancy.8: ok
abundance-occupancy.11: ok
term-sensitivity.5: ok
dns.5: ok
dns.20: ok
dns.33: stronger: `why` says A. vinelandii and M. acetivorans "rise in stationary phase", but the quoted critique qualifies the M. acetivorans case as "in slow growth" (MB-02:C-087, C-129), and the why drops that qualifier.
dns.34: absent: `why` says Bruck 2023 is "open in PMC"; the quoted text says only "an open full text" and never names PMC.
dns.39: ok

## Counts

Entries checked: 87 (60 in packet-01, 27 in packet-02). ok: 78. Faults: 9.

- stronger: 1
- conf: 1
- numbers: 0
- absent: 2
- critic: 0
- merged: 0
- holds: 5
