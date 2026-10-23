# First pass: 16S

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 68/560 = 12.1%** (Wilson 9.7% to 15.1%).
- Checker A alone 52, checker B alone 63, both 47; agree (ok against fault) on 539 of 560.
- Per 100 entries: holds + absent 9.5; stronger + numbers 1.8; conf 0.5; critic 0.2; merged 0.2.
- Kinds (entries): holds 45, stronger 10, absent 10, conf 3, critic 1, merged 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 0 | 2 | 2 | 58 |
| packet-02.md | 60 | 5 | 7 | 8 | 56 |
| packet-03.md | 60 | 4 | 5 | 5 | 59 |
| packet-04.md | 60 | 10 | 11 | 11 | 59 |
| packet-05.md | 60 | 3 | 3 | 4 | 58 |
| packet-06.md | 60 | 10 | 10 | 11 | 58 |
| packet-07.md | 60 | 9 | 14 | 14 | 55 |
| packet-08.md | 60 | 6 | 6 | 6 | 60 |
| packet-09.md | 60 | 5 | 5 | 7 | 56 |
| packet-10.md | 20 | 0 | 0 | 0 | 20 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| primers.2 | stronger | stronger: The entry says "V4 primers under-represented SAR11 and over-represented Gammaproteobacteria", widening the text's "The original 515F/806R V4 primers" to V4 primers in general. |
| ploidy.3 | stronger | stronger: the entry says this "is the only direct origin and terminus count for E. coli at two growth rates" outright, but the text says only that removing Pecoraro 2011 "would remove the only direct origin and terminus counts" from the review's evidence. |
| ploidy.18 | stronger | stronger: the entry says "but A. vinelandii rises" where the text says it "is reported to rise ... (SECONDARY, via Bruck et al. 2023 full text)", dropping the hedge and the secondary standing. |
| ploidy.22 | stronger | stronger: the text says "No source I found measured 16S copies per cell directly in environmental cells", but the entry drops "I found" and states "No source measured 16S copies per cell directly in environmental cells" as a general fact. / stronger: the entry says "No source measured 16S copies per cell directly in environmental cells" where the text says "No source I found measured", dropping the search scope. |
| community-copy-number.5 | stronger | stronger: the entry says "the EMP gives about 2.2" with no sign that the value is predicted, though its cited critique (C-024) says these copy numbers "are predictions from one source". |
| denoising-clustering.4 | stronger | stronger: "pipeline choice biased interpretations" is firmer than the critique's "Straub 2020 reports pipeline-dependent interpretations". / stronger: the entry says "pipeline choice biased interpretations", where the text (C-087) says only that Straub 2020 "reports pipeline-dependent interpretations". |
| bias-consistency.1 | stronger | stronger: the closing clause "bias behaves as a multiplicative factor per taxon that calibration controls can correct" is stated as a general property, dropping the "one dataset modelled for this question" scope the text gives (I-0002 "One reanalysis finds it consistent") and the field evidence of inconsistency in C-129. |
| scaling-normalisation.4 | stronger | stronger: the text marks the RNA-seq origin citations "(Bullard 2010; Robinson and Oshlack 2010; Anders and Huber 2010, indirect)", but the entry drops "indirect" from both its wording and its src labels. / stronger: the text marks the RNA-seq origin sources "indirect", and the entry drops that qualifier from both the claim and holds. |
| beta-diversity.5 | stronger | stronger: the text gives a contrary finding, proportions "still depth-sensitive under Schloss's null", which the entry drops while keeping conf single. |
| abundance-occupancy.8 | stronger | stronger: the entry says "detection limits and neutral or sampling models predict a positive relationship without selection" but drops the text's scope for the detection-limits evidence, "[76, a single 454-era study at one site]". |
