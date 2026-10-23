## standardisation.1 (claim)

Because covariates have different units and scales, all distance constructions require prior commensuration; incommensurable variables are made comparable by z-score standardisation, range scaling, PCA/whitening, or Mahalanobis covariance-scaling, and this is itself a design choice, not a convention.

- conf: not stated
- class: not stated
- holds: distance constructions in continuous covariate space
- src: none (the reviewer's synthesis)
- trail: C-COVDIST §Key Findings, §Standardisation

From the note:

> C-COVDIST:A-001 [TL;DR] - There is **no settled, single standard** for judging out-of-distribution (OOD) status in continuous covariate space; practice is irreducibly **plural**, and the dominant constructions split cleanly into two modes — **near-neighbour** (is there a close training analogue?) and **envelope/centroid** (is the point outside overall coverage of the training cloud?).
>
> C-COVDIST:A-006 [Key Findings] **Standardisation and correlation handling are themselves a design choice, not a convention.** Incommensurable variables are made comparable by z-score standardisation, range scaling, PCA/whitening, or Mahalanobis covariance-scaling.
>
> C-COVDIST:B-0051 [3. Standardisation across scales/units and handling of inter-variable correlation] Because covariates have different units and scales, all distance constructions require prior commensuration:
>

