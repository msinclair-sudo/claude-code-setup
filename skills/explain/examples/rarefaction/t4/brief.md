# Brief

- **Audience:** researchers starting with microbiome metabarcoding; they know what bacteria and PCR are, not how counts get from soil to reads.
- **Message:** a shallower sample finds fewer taxa because sequencing reads only some barcodes; rarefying to equal depth makes richness comparable but leaves every earlier bias in place.
- **Delivery:** presented (narrated, system-paced).
- **Sources:** the MB-01 literature review (vault `Topics/Biology/Research/Results/From sample to count table in 16S rRNA gene amplicon sequencing ...`), read critic block first; every literature claim in `claims.yaml` names its paper. Counts come from one simulated community (`../pipeline.py`, seed 7), calibrated where a measurement exists (copy-number range, PCR bias spread, cycle number).
- **Not in scope:** alternatives to rarefying beyond naming them (coverage-based standardisation, log-ratio methods, extrapolation), real datasets, how to choose the depth, contamination and low-biomass samples.
