## evidence-base.1 (claim)

Several key sources the review rests on are 2025–2026 preprints or under review, at high-quality venues but not all finalised.

- conf: not stated
- class: not stated
- holds: the sources the note numbers R5, R6 and R7 (Um et al. 2025; the anonymous 2025 low-variance paper; Ferrini et al. 2026)
- src: umPropagateInjectRevisiting2025, anonymousLowVarianceBottleneck2025, ferriniRethinkingGNNsMissing2026
- trail: GHOST §Standing caveats

From the note:

> GHOST:B-0050 [Standing caveats on the corpus] Several key sources are 2025–2026 preprints / under-review (R5, R6, R7) — high-quality venues but not all finalized.
>
> GHOST:R-0012 [References] [R5] Um, D., Kim, J., Park, [et al.], Lim, Ahn, Park (2025).
>
> GHOST:R-0016 [References] [R6] Anonymous (2025).
>
> GHOST:R-0017 [References] *Low Variance: A Bottleneck in Diffusion-Based Graph Imputation.* ICLR 2025 track.
>
> GHOST:R-0019 [References] [R7] Ferrini, F., Lachi, V., Longa, A., Lepri, B., Akiyoshi, [et al.], Passerini, A., Liu, Jaeger (2026).
>

## default-strategy.2 (claim)

Propagation's marginal degradation, against the collapse of model-internal imputation, looks like a clean win for option (a), but it is not, for three reasons the verification surfaced and confirmed: the robustness numbers are regime-bound, a 2026 result proves the benchmark itself hides the differences, and propagation has a proven low-variance defect.

- conf: not stated
- class: not stated
- holds: the review's verdict on option (a)
- src: none (the review's verdict)
- contrary: not stated
- trail: GHOST §Verdict

From the note:

> GHOST:A-002 [Verdict] The single most replicated empirical result is that diffusion/propagation imputation (Feature Propagation and variants) reconstructs entirely-missing node features from observed neighbours and degrades only marginally — ~2–4% relative node-classification accuracy at 99% missing — while model-internal imputation (GCNMF) collapses to ~35% on the same benchmark [R1, R2, R3].
>
> GHOST:A-003 [Verdict] That looks like a clean win for option (a).
>
> GHOST:A-004 [Verdict] It is not, for three reasons that the verification surfaced and confirmed:
>
> GHOST:A-005 [Verdict] **The robustness numbers are regime-bound.** They are measured almost entirely on homophilous, sparse bag-of-words citation/co-purchase graphs (Cora, Citeseer, PubMed, Photo) under Missing-Completely-At-Random missingness, and many are self-reported by the method authors [R1, R2, R4].
>
> GHOST:A-006 [Verdict] **A 2026 result proves the benchmark itself hides the differences.** High feature sparsity provably bounds the information loss from missingness, "making all models appear robust and preventing a meaningful comparison" — so the dominance of propagation on standard benchmarks may be an artifact, not a regime-general property [R7].
>
> GHOST:A-007 [Verdict] **Propagation has a proven systematic defect.** It produces low-variance channels that contribute little downstream — established with empirical evidence *and* a theoretical proof, and independently corroborated at a second venue [R5, R6].
>

Not found in the cited text (where to look, not what is wrong): holds: review

