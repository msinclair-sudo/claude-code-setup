## four-step-truncation.1 (claim)

Constraint-based/FBA models have represented N-oxide reduction as discrete enzymatic reactions (separate fluxes) with N₂O as an explicit, distinct modelled output, but only in the nitrifier-denitrification branch of ammonia-oxidizing bacteria (Nitrosomonas europaea; Perez-Garcia et al. 2014, 2016; Mellbye et al. 2018), where N₂O is terminal because the organism lacks nosZ and emission is mechanistically framed as electron-equivalent overflow under O₂ limitation.

- conf: not stated
- class: not stated
- holds: the nitrifier-denitrification branch of ammonia-oxidizing bacteria
- src: perezgarciaClarifyingRegulationNO2014, perezgarciaAssessmentNitricOxide2016, mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Verdict, §TL;DR
- rating: "PARTIALLY DEMONSTRATED"
- contrary: not stated

From the note:

> C-STEPDEN:A-001 [Verdict] **PARTIALLY DEMONSTRATED.** Constraint-based/FBA models *have* represented N-oxide reduction as discrete enzymatic reactions with N₂O as an explicit, distinct modelled output — but only in the nitrifier-denitrification branch of ammonia-oxidizing bacteria (Perez-Garcia et al. 2014, 2016; Mellbye et al. 2018), where N₂O is terminal because the organism lacks *nosZ* and emission is mechanistically framed as electron-equivalent overflow under O₂ limitation.
>
> C-STEPDEN:B-0006 [TL;DR] - **Partially demonstrated.** Constraint-based/FBA models that carry individual nitrogen-oxide reduction steps as separate fluxes AND emit N₂O as a distinct readout exist, but only for the *nitrifier-denitrification* branch in ammonia-oxidizing bacteria (*Nitrosomonas europaea*), where N₂O is necessarily terminal because the organism lacks *nosZ*.
>

## four-step-truncation.2 (claim)

A genome-scale or community FBA model resolving NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four separate fluxes (nar/nap, nirK/nirS, norBC, nosZ) with N₂O emerging as a truncation/accumulation product, due to a missing or regulated nosZ or a community pathway gap, was not found in the constraint-based literature; that capability currently resides exclusively in the kinetic/ODE, cybernetic and trait-based ecosystem modelling families.

- conf: not stated
- class: search (note: "was NOT found in the constraint-based literature")
- search: searched, not found (note: "absence of evidence in a thorough but finite search")
- holds: published, locatable constraint-based literature as of June 2026; the review says an unpublished or very recent model could exist
- src: none (the review's search)
- trail: C-STEPDEN §Verdict, §TL;DR, §Caveats, §Recommendations
- contrary: not stated

From the note:

> C-STEPDEN:A-002 [Verdict] The specific full target — a genome-scale or community FBA model resolving NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four separate fluxes (nar/nap, nirK/nirS, norBC, nosZ) with N₂O emerging as a truncation/accumulation product due to a missing/regulated *nosZ* or community pathway gap — was NOT found in the constraint-based literature; that capability currently resides exclusively in the kinetic/ODE, cybernetic, and trait-based ecosystem modelling families.
>
> C-STEPDEN:B-0007 [TL;DR] A genome-scale or community FBA model that resolves the full canonical heterotrophic chain NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four discrete fluxes with N₂O as an explicit truncation/accumulation output has NOT been published.
>
> C-STEPDEN:B-0068 [Recommendations] As of June 2026, no such publication was located.
>
> C-STEPDEN:B-0071 [Caveats] - "NOT FOUND" for the full four-step heterotrophic case reflects the absence of evidence in a thorough but finite search; an unpublished or very recent model could exist.
>
> C-STEPDEN:B-0072 [Caveats] The negative claim is bounded to published, locatable constraint-based literature as of June 2026.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## four-step-truncation.3 (claim)

The literature has encoded denitrification reactions in constraint-based models in two clearly distinguishable ways: nitrifier-denitrification models that explicitly emit N₂O, and single-strain canonical denitrifier GEMs whose genome content carries the sub-steps but in which N₂O is not a resolved readout.

- conf: not stated
- class: not stated
- holds: constraint-based models the review located
- src: none (the reviewer's synthesis)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0022 [What "the method" has actually represented] The empirical literature shows the field has done this in two clearly distinguishable ways.
>
> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>
> C-STEPDEN:B-0036 [What "the method" has actually represented] **(B) Single-strain canonical denitrifier GEMs — sub-steps present in genome content, but N₂O not a resolved readout.** The *Paracoccus denitrificans* Pd1222 GEM (Bordel et al., 2024, *mSystems*; 972 genes, 1,371 reactions, 1,388 metabolites; reconstructed in RAST/SEED, simulated in COBRA-style FBA) was built and validated for biomass yields on carbon sources, including with NO₃⁻ as electron acceptor.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## four-step-truncation.4 (claim)

Resolving N₂O as an explicit output in a complete-denitrifier GEM would require adding per-step exchange reactions, explicit electron-donor/quinone coupling for each reductase, and constraints (for example capping nosZ flux to mimic Cu limitation or regulatory lag), an extension not yet published.

- conf: not stated
- class: not stated
- holds: complete-denitrifier GEMs such as the P. denitrificans Pd1222 GEM and iThauera861
- src: none (the reviewer's synthesis)
- trail: C-STEPDEN §Recommendations

From the note:

> C-STEPDEN:B-0063 [Recommendations] **If the goal is a complete-denitrifier GEM to extend:** The *Paracoccus denitrificans* Pd1222 GEM (github.com/SergioBordel/ModelParacoccus) and *Thauera* iThauera861 are the best-curated starting points; both contain the full denitrification gene complement (*nar/nap*, *nir*, *nor*, *nos*).
>
> C-STEPDEN:B-0064 [Recommendations] Resolving N₂O as an explicit output would require adding per-step exchange reactions, explicit electron-donor/quinone coupling for each reductase, and constraints (e.g., capping *nosZ* flux to mimic Cu limitation or regulatory lag) — an extension not yet published.
>

## four-step-truncation.5 (claim)

The review sets the benchmark that would change its verdict to DEMONSTRATED: a published, mass- and charge-balanced genome-scale or community constraint-based model in which (a) nar/nap, nir, nor and nos are each separate reactions, (b) N₂O appears as a terminal exchange or accumulating product, and (c) the stated cause is a pathway gap (absent or capped nosZ, or cross-organism division of labour) rather than electron overflow alone; as of June 2026 no such publication was located.

- conf: not stated
- class: search (note: "no such publication was located")
- search: searched, not found (note: "no such publication was located")
- holds: published literature as of June 2026
- src: none (the reviewer's criteria)
- trail: C-STEPDEN §Recommendations

From the note:

> C-STEPDEN:B-0067 [Recommendations] **Benchmarks that would change this verdict to DEMONSTRATED:** A published, mass-/charge-balanced genome-scale or community constraint-based model in which (a) *nar/nap*, *nir*, *nor*, and *nos* are each separate reactions, (b) N₂O appears as a terminal exchange or accumulating product, and (c) the stated cause is a pathway gap (absent/capped *nosZ* or cross-organism division of labour) rather than electron overflow alone.
>
> C-STEPDEN:B-0068 [Recommendations] As of June 2026, no such publication was located.
>

## dns.1 (do not say)

"No genome-scale or community FBA model of four-step denitrification with N₂O as a truncation output has been published."

- why: The note says its NOT FOUND reflects the absence of evidence in a thorough but finite search, that an unpublished or very recent model could exist, and that the negative claim is bounded to published, locatable constraint-based literature as of June 2026.
- instead: four-step-truncation.2
- trail: C-STEPDEN §Caveats

From the note:

> C-STEPDEN:B-0007 [TL;DR] A genome-scale or community FBA model that resolves the full canonical heterotrophic chain NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four discrete fluxes with N₂O as an explicit truncation/accumulation output has NOT been published.
>
> C-STEPDEN:B-0071 [Caveats] - "NOT FOUND" for the full four-step heterotrophic case reflects the absence of evidence in a thorough but finite search; an unpublished or very recent model could exist.
>
> C-STEPDEN:B-0072 [Caveats] The negative claim is bounded to published, locatable constraint-based literature as of June 2026.
>

Not found in the cited text (where to look, not what is wrong): "No genome-scale or community FBA model of four-step denitrification with N₂O as a truncation output has been published."

## dns.2 (do not say)

"Perez-Garcia et al. (2014) and Mellbye et al. (2018) model N₂O as the truncation product of four-step heterotrophic denitrification."

- why: The note says their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation.
- instead: electron-overflow.10, four-step-truncation.1
- trail: C-STEPDEN §Recommendations

From the note:

> C-STEPDEN:B-0060 [Recommendations] **If the goal is an existing constraint-based model with explicit N₂O output:** Start from Perez-Garcia et al. (2014) and Mellbye et al. (2018).
>
> C-STEPDEN:B-0062 [Recommendations] Note their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation.
>

Not found in the cited text (where to look, not what is wrong): "Perez-Garcia et al. (2014) and Mellbye et al. (2018) model N₂O as the truncation product of four-step heterotrophic denitrification."

