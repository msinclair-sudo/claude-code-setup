## denitrification-pathway.1 (claim)

The denitrification pathway is a four-step dissimilatory reduction, NO₃⁻→NO₂⁻→NO→N₂O→N₂, catalysed by nitrate reductase (Nar/Nap), nitrite reductase (NirK/NirS), nitric oxide reductase (cNor/qNor, norBC) and nitrous oxide reductase (NosZ).

- conf: not stated
- class: not stated
- holds: the full canonical heterotrophic chain, as the review describes it; no organism named
- src: none (the note cites no source for it)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0007 [TL;DR] A genome-scale or community FBA model that resolves the full canonical heterotrophic chain NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four discrete fluxes with N₂O as an explicit truncation/accumulation output has NOT been published.
>
> C-STEPDEN:B-0020 [What "the method" has actually represented] The denitrification pathway is a four-step dissimilatory reduction, NO₃⁻→NO₂⁻→NO→N₂O→N₂, catalysed by nitrate reductase (Nar/Nap), nitrite reductase (NirK/NirS), nitric oxide reductase (cNor/qNor, *norBC*), and nitrous oxide reductase (NosZ), consuming 10 electrons per two nitrate ions converted to dinitrogen.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## denitrification-pathway.2 (claim)

The four-step reduction consumes 10 electrons per two nitrate ions converted to dinitrogen.

- conf: not stated
- class: not stated
- holds: the full pathway from nitrate to dinitrogen
- src: none (the note cites no source for it)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0020 [What "the method" has actually represented] The denitrification pathway is a four-step dissimilatory reduction, NO₃⁻→NO₂⁻→NO→N₂O→N₂, catalysed by nitrate reductase (Nar/Nap), nitrite reductase (NirK/NirS), nitric oxide reductase (cNor/qNor, *norBC*), and nitrous oxide reductase (NosZ), consuming 10 electrons per two nitrate ions converted to dinitrogen.
>

## constraint-based-model.1 (claim)

In constraint-based modelling, the four denitrification reactions can in principle be encoded as separate fluxes balanced against an electron donor pool (NADH/quinone) with proton translocation.

- conf: not stated
- class: not stated
- holds: stated as possible in principle, for the pathway NO₃⁻→NO₂⁻→NO→N₂O→N₂
- src: none (the reviewer's synthesis)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0020 [What "the method" has actually represented] The denitrification pathway is a four-step dissimilatory reduction, NO₃⁻→NO₂⁻→NO→N₂O→N₂, catalysed by nitrate reductase (Nar/Nap), nitrite reductase (NirK/NirS), nitric oxide reductase (cNor/qNor, *norBC*), and nitrous oxide reductase (NosZ), consuming 10 electrons per two nitrate ions converted to dinitrogen.
>
> C-STEPDEN:B-0021 [What "the method" has actually represented] In constraint-based modelling, these reactions can in principle be encoded as separate fluxes balanced against an electron donor pool (NADH/quinone) with proton translocation.
>

## constraint-based-model.2 (claim)

The boundary between "constraint-based" and "kinetic" models is occasionally blurred in the literature (for example dynamic FBA and cybernetic models); the review classified each model by whether its core engine is stoichiometric LP optimization (FBA family) or rate-equation integration (kinetic/ODE family).

- conf: not stated
- class: not stated
- holds: the classification used throughout the review
- src: none (the reviewer's method statement)
- trail: C-STEPDEN §Caveats

From the note:

> C-STEPDEN:B-0073 [Caveats] - The boundary between "constraint-based" and "kinetic" is occasionally blurred in the literature (e.g., dynamic FBA, cybernetic models); models were classified by whether their core engine is stoichiometric LP optimization (FBA family) versus rate-equation integration (kinetic/ODE family).
>

Not found in the cited text (where to look, not what is wrong): holds: review

## constraint-based-model.3 (claim)

Standard FBA biomass-maximization does not naturally predict byproduct (N-oxide) overflow without additional constraints, a general limitation noted across the byproduct-secretion modelling literature.

- conf: not stated
- class: not stated
- holds: standard FBA with a biomass-maximization objective; the note names no specific study
- src: none (the note names the byproduct-secretion modelling literature without a reference)
- trail: C-STEPDEN §How stepwise

From the note:

> C-STEPDEN:B-0044 [How stepwise N-cycle reactions enter a stoichiometric model] The documented difficulty specific to N₂O is indirect but real: balancing the cytochrome/N-oxide reactions for mass and charge is error-prone, and standard FBA biomass-maximization does not naturally predict byproduct (N-oxide) overflow without additional constraints — a general limitation noted across the byproduct-secretion modelling literature.
>

## kinetic-trait-models.1 (claim)

Stepwise denitrification with N₂O as an explicit intermediate or terminal product is resolved in the kinetic/ODE and trait-based modelling families (the Activated Sludge Model for Nitrogen, electron-competition models, the cybernetic models of Song & Liu, the Kampschreur Agrobacterium model, and the PNAS/bioRxiv OMZ modular-denitrification ecosystem model); these are not constraint-based FBA models.

- conf: not stated
- class: not stated
- holds: kinetic/ODE, cybernetic and trait-based families, not FBA
- src: hiattUpdatedProcessModel2008, pan, songDynamicMetabolicModeling2015, songRegulationStructuredDynamicMetabolic2017, kampschreurMetabolicModelingDenitrification2012, zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024
- trail: C-STEPDEN §TL;DR, §Key Findings
- rating: "well established"

From the note:

> C-STEPDEN:B-0009 [TL;DR] - The work that genuinely resolves stepwise denitrification with N₂O as an intermediate/terminal product sits in the KINETIC/ODE and trait-based families (Activated Sludge Model for Nitrogen, electron-competition models, the cybernetic models of Song & Liu, the Kampschreur *Agrobacterium* model, and the PNAS/bioRxiv OMZ modular-denitrification ecosystem model), NOT in the FBA/constraint-based family.
>
> C-STEPDEN:B-0018 [Key Findings] **Stepwise denitrification with N₂O as an explicit intermediate/terminal product is well established in the KINETIC/ODE and trait-based literature.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt & Grady) incorporates four-step denitrification with reaction-specific parameters; electron-competition models, the cybernetic models of Song & Liu, the Kampschreur *Agrobacterium tumefaciens* model, and the PNAS OMZ modular-denitrification ecosystem model all resolve sub-steps and N₂O.
>
> C-STEPDEN:B-0019 [Key Findings] These are not constraint-based FBA models.
>

## kinetic-trait-models.2 (claim)

The Activated Sludge Model for Nitrogen (ASMN; Hiatt & Grady, 2008) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters."

- conf: not stated
- class: not stated
- holds: an activated sludge process model (Water Environment Research 80(11):2145–2156), outside the FBA/constraint-based family
- src: hiattUpdatedProcessModel2008
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0018 [Key Findings] **Stepwise denitrification with N₂O as an explicit intermediate/terminal product is well established in the KINETIC/ODE and trait-based literature.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt & Grady) incorporates four-step denitrification with reaction-specific parameters; electron-competition models, the cybernetic models of Song & Liu, the Kampschreur *Agrobacterium tumefaciens* model, and the PNAS OMZ modular-denitrification ecosystem model all resolve sub-steps and N₂O.
>
> C-STEPDEN:B-0047 [Bounding and negative facts] - **The N₂O-resolving denitrification work sits outside the FBA/constraint-based family.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt WC & Grady CP Jr., 2008, *Water Environment Research* 80(11):2145–2156) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters.
>

## kinetic-trait-models.3 (claim)

Electron-competition models (Pan et al., ES&T) explicitly model competition among the four denitrification steps for electrons to predict N₂O accumulation.

- conf: not stated
- class: not stated
- holds: kinetic models, outside the FBA/constraint-based family
- src: pan
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0047 [Bounding and negative facts] - **The N₂O-resolving denitrification work sits outside the FBA/constraint-based family.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt WC & Grady CP Jr., 2008, *Water Environment Research* 80(11):2145–2156) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters.
>
> C-STEPDEN:B-0048 [Bounding and negative facts] Electron-competition models (Pan et al., *ES&T*) explicitly model competition among the four steps for electrons to predict N₂O accumulation.
>

## kinetic-trait-models.4 (claim)

The cybernetic models of Song & Liu (2015, Ind. Eng. Chem. Res.) and Song et al. (2017, Frontiers in Microbiology) resolve sequential N-oxide intermediates with dynamic regulation.

- conf: not stated
- class: not stated
- holds: cybernetic dynamic metabolic models of denitrifying bacterial growth, outside the FBA/constraint-based family
- src: songDynamicMetabolicModeling2015, songRegulationStructuredDynamicMetabolic2017
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0047 [Bounding and negative facts] - **The N₂O-resolving denitrification work sits outside the FBA/constraint-based family.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt WC & Grady CP Jr., 2008, *Water Environment Research* 80(11):2145–2156) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters.
>
> C-STEPDEN:B-0049 [Bounding and negative facts] The cybernetic models of Song & Liu (2015, *Ind.
>
> C-STEPDEN:B-0050 [Bounding and negative facts] Res.*) and Song et al. (2017, *Frontiers in Microbiology*) resolve sequential N-oxide intermediates with dynamic regulation.
>
> C-STEPDEN:B-0105 [Full reference list] Song HS, Liu C. Dynamic metabolic modeling of denitrifying bacterial growth: the cybernetic approach.
>

## kinetic-trait-models.5 (claim)

The Kampschreur et al. (2012) Agrobacterium tumefaciens model resolves Nap/NirK/NorB with transcriptional/kinetic regulation and reproduces NO/N₂O emission from incomplete pathway expression; it is a kinetic ODE network, not FBA.

- conf: not stated
- class: model (note: "reproduces NO/N₂O emission")
- holds: Agrobacterium tumefaciens; a kinetic ODE metabolic network
- src: kampschreurMetabolicModelingDenitrification2012
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0051 [Bounding and negative facts] The Kampschreur et al. (2012, *Frontiers in Microbiology*) *Agrobacterium tumefaciens* model resolves Nap/NirK/NorB with transcriptional/kinetic regulation and reproduces NO/N₂O emission from incomplete pathway expression — but it is a kinetic ODE network, not FBA.
>

## kinetic-trait-models.6 (claim)

The review's model index gives the Agrobacterium tumefaciens model's N₂O mechanism as "incomplete/unbalanced enzyme expression during oxic-anoxic transition", and lists its sub-steps (Nap, NirK, NorB; regulation) as resolved.

- conf: not stated
- class: not stated
- holds: Agrobacterium tumefaciens; framework given as KINETIC/ODE metabolic network (not FBA)
- src: kampschreurMetabolicModelingDenitrification2012
- trail: C-STEPDEN §Compact JSON

From the note:

> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

Not found in the cited text (where to look, not what is wrong): N₂O

## kinetic-trait-models.7 (claim)

The Domingo-Félez & Smets NDHA model and ASM3-based extensions are pseudo-mechanistic ODE models.

- conf: not stated
- class: not stated
- holds: outside the FBA/constraint-based family
- src: domingofelez
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0052 [Bounding and negative facts] The Domingo-Félez & Smets NDHA model and ASM3-based extensions are pseudo-mechanistic ODE models.
>

Not found in the cited text (where to look, not what is wrong): holds: fba; holds: constraint-based

## kinetic-trait-models.8 (claim)

Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂, neglecting NO, using redox thermodynamics, biomass-yield traits and resource-competition theory; trait-based/thermodynamic ecosystem models like this resolve denitrification modules and N₂O ecologically, not via FBA.

- conf: not stated
- class: not stated
- holds: ocean (OMZ) denitrifier functional types; NO not represented
- src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0053 [Bounding and negative facts] - **Trait-based/thermodynamic ecosystem models resolve denitrification modules and N₂O ecologically, not via FBA.** Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂ (neglecting NO) using redox thermodynamics, biomass-yield traits, and resource-competition theory — explicitly noting that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.
>
> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

## kinetic-trait-models.9 (claim)

Zakem and colleagues note that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.

- conf: not stated
- class: not stated
- holds: ocean biogeochemical models; denitrifying microbes in the ocean
- src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0053 [Bounding and negative facts] - **Trait-based/thermodynamic ecosystem models resolve denitrification modules and N₂O ecologically, not via FBA.** Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂ (neglecting NO) using redox thermodynamics, biomass-yield traits, and resource-competition theory — explicitly noting that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.
>

## kinetic-trait-models.10 (claim)

In the Zakem modular-denitrification model, N₂O cycling emerges from community-level niche partitioning: one functional type does NO₃⁻→NO₂⁻, another N₂O→N₂.

- conf: not stated
- class: not stated
- holds: a trait-based ocean ecosystem model of denitrifier functional types
- src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0053 [Bounding and negative facts] - **Trait-based/thermodynamic ecosystem models resolve denitrification modules and N₂O ecologically, not via FBA.** Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂ (neglecting NO) using redox thermodynamics, biomass-yield traits, and resource-competition theory — explicitly noting that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.
>
> C-STEPDEN:B-0054 [Bounding and negative facts] N₂O cycling emerges from community-level niche partitioning (one functional type does NO₃⁻→NO₂⁻, another N₂O→N₂).
>

## kinetic-trait-models.11 (claim)

The Zakem model is the conceptual realization of the user's "community-level pathway gaps" mechanism, but implemented as a trait-based ecosystem model, not a stoichiometric/constraint-based GEM.

- conf: not stated
- class: not stated
- holds: the review's comparison with the user's mechanism
- src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0053 [Bounding and negative facts] - **Trait-based/thermodynamic ecosystem models resolve denitrification modules and N₂O ecologically, not via FBA.** Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂ (neglecting NO) using redox thermodynamics, biomass-yield traits, and resource-competition theory — explicitly noting that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.
>
> C-STEPDEN:B-0055 [Bounding and negative facts] This is the conceptual realization of the user's "community-level pathway gaps" mechanism, but implemented as a trait-based ecosystem model, not a stoichiometric/constraint-based GEM.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## kinetic-trait-models.12 (claim)

The body of work that resolves all four steps with N₂O as an accumulating or terminal product, driven by missing or inhibited NosZ, electron competition, or community pathway gaps, lives in kinetic/ODE, cybernetic and trait-based ecosystem modelling, not in the FBA/constraint-based stoichiometric family; these families already deliver stepwise N₂O (ASMN, electron-competition models, Song & Liu, Kampschreur, Zakem et al. 2024).

- conf: not stated
- class: not stated
- holds: the review's grouping of the cases it located
- src: hiattUpdatedProcessModel2008, pan, songDynamicMetabolicModeling2015, kampschreurMetabolicModelingDenitrification2012, zakemEcologicalDynamicsModular2024
- trail: C-STEPDEN §How the cases, §Recommendations
- contrary: not stated

From the note:

> C-STEPDEN:B-0056 [How the cases relate] The field bifurcates cleanly.
>
> C-STEPDEN:B-0059 [How the cases relate] Meanwhile, the rich body of work that does resolve all four steps with N₂O as an accumulating/terminal product — driven by missing/inhibited NosZ, electron competition, or community pathway gaps — lives in kinetic/ODE, cybernetic, and trait-based ecosystem modelling, not in the FBA/constraint-based stoichiometric family.
>
> C-STEPDEN:B-0065 [Recommendations] **If the goal is to model N₂O accumulation mechanistically now:** Use the kinetic/ODE or cybernetic families (ASMN, electron-competition models, Song & Liu, Kampschreur), or the trait-based ecosystem approach (Zakem et al. 2024) for community pathway-gap scenarios.
>
> C-STEPDEN:B-0066 [Recommendations] These already deliver stepwise N₂O.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## nitrifier-denitrification-models.1 (claim)

Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of Nitrosomonas europaea energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes, the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).

- conf: not stated
- class: model (note: "used FBA to quantify NO and N₂O production")
- holds: N. europaea energy metabolism, an ammonia-oxidizing bacterium
- src: perezgarciaClarifyingRegulationNO2014 (full-text Methods/reaction tables partially inaccessible; reaction counts and mechanisms corroborated from abstracts, verbatim snippets and the companion 2016 paper)
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0006 [TL;DR] - **Partially demonstrated.** Constraint-based/FBA models that carry individual nitrogen-oxide reduction steps as separate fluxes AND emit N₂O as a distinct readout exist, but only for the *nitrifier-denitrification* branch in ammonia-oxidizing bacteria (*Nitrosomonas europaea*), where N₂O is necessarily terminal because the organism lacks *nosZ*.
>
> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>
> C-STEPDEN:B-0069 [Caveats] - Full-text Methods/reaction tables for Perez-Garcia et al. (2014) and Mellbye et al. (2018) were partially inaccessible (publisher bot detection); the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim.
>
> C-STEPDEN:B-0070 [Caveats] Reaction counts, mechanisms, and N₂O-output facts are corroborated from abstracts, verbatim snippets, the Methods text recovered for Mellbye, and the companion 2016 paper.
>

## nitrifier-denitrification-models.2 (claim)

In the Perez-Garcia SMN, N₂O is an explicit output and, because N. europaea lacks nosZ, necessarily a terminal product.

- conf: not stated
- class: not stated
- holds: N. europaea, which has no nosZ
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0011 [Key Findings] N₂O is an explicit output, and because *N. europaea* lacks *nosZ*, it is necessarily a terminal product.
>
> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>
> C-STEPDEN:B-0024 [What "the method" has actually represented] N₂O is a terminal output because *N. europaea* has no *nosZ*.
>

## nitrifier-denitrification-models.3 (claim)

The Perez-Garcia SMN is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).

- conf: not stated
- class: not stated
- holds: N. europaea SMN (51 reactions, 44 metabolites)
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>

## nitrifier-denitrification-models.4 (claim)

The Perez-Garcia SMN was validated against measured yield ratios: "These estimates matched well, deviating on average by 15% from values for 17 M yield ratios reported for non-limiting oxygen and ammonium concentrations."

- conf: not stated
- class: model/meas (note: "validated against measured yield ratios")
- holds: 17 M yield ratios under non-limiting oxygen and ammonium concentrations; N. europaea
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>
> C-STEPDEN:B-0026 [What "the method" has actually represented] The model was validated against measured yield ratios; verbatim, "These estimates matched well, deviating on average by 15% from values for 17 M yield ratios reported for non-limiting oxygen and ammonium concentrations.
>

## nitrifier-denitrification-models.5 (claim)

Perez-Garcia et al. (2016, Biotechnology and Bioengineering) extended this lineage to a multispecies metabolic network that "captures the nitrogen respiratory pathways inferred from genomes of eight AOB and NOB species," resolving specific NO redox reactions (NirK, CytP460, cytochrome c554, flavohemoglobins, cNor).

- conf: not stated
- class: not stated
- holds: eight AOB and NOB species, pathways inferred from genomes
- src: perezgarciaAssessmentNitricOxide2016
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0027 [What "the method" has actually represented] This lineage was extended in Perez-Garcia et al. (2016, *Biotechnology and Bioengineering*) to a multispecies metabolic network that "captures the nitrogen respiratory pathways inferred from genomes of eight AOB and NOB species," resolving specific NO redox reactions (NirK, CytP460, cytochrome c554, flavohemoglobins, cNor); verbatim, "Simulations showed that NO oxidation to NO2(-) decreased N2O formation by 60% without changing culture's NO2(-) production rate."
>

## nitrifier-denitrification-models.6 (claim)

In the 2016 multispecies network, "Simulations showed that NO oxidation to NO2(-) decreased N2O formation by 60% without changing culture's NO2(-) production rate."

- conf: not stated
- class: model (note: "Simulations showed")
- holds: simulations of the eight-species AOB/NOB metabolic network during nitrification
- src: perezgarciaAssessmentNitricOxide2016
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0027 [What "the method" has actually represented] This lineage was extended in Perez-Garcia et al. (2016, *Biotechnology and Bioengineering*) to a multispecies metabolic network that "captures the nitrogen respiratory pathways inferred from genomes of eight AOB and NOB species," resolving specific NO redox reactions (NirK, CytP460, cytochrome c554, flavohemoglobins, cNor); verbatim, "Simulations showed that NO oxidation to NO2(-) decreased N2O formation by 60% without changing culture's NO2(-) production rate."
>

## nitrifier-denitrification-models.7 (claim)

The review's model index gives the 2016 multispecies network's N₂O mechanism as "NO redox balance; CytP460 reduces N2O by 60%", with N₂O explicit and sub-steps partly resolved (NO redox reactions, NirK, CytP460, cNor).

- conf: not stated
- class: not stated
- holds: eight AOB/NOB species; stoichiometric network with FBA
- src: perezgarciaAssessmentNitricOxide2016
- trail: C-STEPDEN §Compact JSON

From the note:

> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

Not found in the cited text (where to look, not what is wrong): N₂O

## nitrifier-denitrification-models.8 (claim)

The Mellbye et al. (2018) coculture model tracks NO, NO₂ and N₂O as separate N-oxide species, and is the closest community-level and strongest community-scale constraint-based demonstration of explicit N₂O output.

- conf: not stated
- class: not stated
- holds: a coculture of N. europaea and N. winogradskyi
- src: mellbyeGenomeScaleConstraintBased2018 (full-text Methods/reaction tables partially inaccessible; facts corroborated from abstracts, verbatim snippets and the Methods text recovered)
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0013 [Key Findings] **The Mellbye et al. (2018) coculture model emits NO, NO₂, and N₂O as separate species and is the closest community-level demonstration.** It integrates two genome-scale reconstructions (iFC578 for *N. europaea*; iFC579 for *N. winogradskyi*) with abiotic gas/aqueous NO oxidation reactions.
>
> C-STEPDEN:B-0028 [What "the method" has actually represented] The Mellbye et al. (2018, *mSystems*) coculture model is the strongest community-scale constraint-based demonstration.
>
> C-STEPDEN:B-0029 [What "the method" has actually represented] It tracks NO, NO₂, and N₂O as separate N-oxide species and combines genome-scale reconstructions iFC578 (*N. europaea*) and iFC579 (*N. winogradskyi*) with abiotic NO-oxidation reactions in gas and aqueous phases.
>
> C-STEPDEN:B-0061 [Recommendations] These are the only published FBA/stoichiometric models located that emit N₂O as a distinct flux, and the Mellbye model (github.com/chaplenf/microBiome-v2.1) is the only community-scale one.
>
> C-STEPDEN:B-0069 [Caveats] - Full-text Methods/reaction tables for Perez-Garcia et al. (2014) and Mellbye et al. (2018) were partially inaccessible (publisher bot detection); the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim.
>
> C-STEPDEN:B-0070 [Caveats] Reaction counts, mechanisms, and N₂O-output facts are corroborated from abstracts, verbatim snippets, the Methods text recovered for Mellbye, and the companion 2016 paper.
>

## nitrifier-denitrification-models.9 (claim)

The Mellbye coculture model integrates two genome-scale reconstructions, iFC578 for N. europaea and iFC579 for N. winogradskyi, with abiotic NO-oxidation reactions in gas and aqueous phases.

- conf: not stated
- class: not stated
- holds: N. europaea and N. winogradskyi coculture
- src: mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0013 [Key Findings] **The Mellbye et al. (2018) coculture model emits NO, NO₂, and N₂O as separate species and is the closest community-level demonstration.** It integrates two genome-scale reconstructions (iFC578 for *N. europaea*; iFC579 for *N. winogradskyi*) with abiotic gas/aqueous NO oxidation reactions.
>
> C-STEPDEN:B-0029 [What "the method" has actually represented] It tracks NO, NO₂, and N₂O as separate N-oxide species and combines genome-scale reconstructions iFC578 (*N. europaea*) and iFC579 (*N. winogradskyi*) with abiotic NO-oxidation reactions in gas and aqueous phases.
>

## nitrifier-denitrification-models.10 (claim)

In the Mellbye model N₂O production is tied to the presence of a NOR-encoding gene: "The genome-scale model also does not consider the minute N2O production observed by N. winogradskyi, since its genome does not contain any known NOR-encoding gene," an explicit gene-content rationale for emission.

- conf: not stated
- class: not stated
- holds: N. winogradskyi, whose genome has no known NOR-encoding gene
- src: mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0014 [Key Findings] N₂O production is tied to the presence of a NOR-encoding gene; verbatim, "The genome-scale model also does not consider the minute N2O production observed by N. winogradskyi, since its genome does not contain any known NOR-encoding gene.
>
> C-STEPDEN:B-0030 [What "the method" has actually represented] N₂O production is mechanistically tied to NOR gene presence — the model deliberately excludes the minute N₂O produced by *N. winogradskyi* because its genome lacks a NOR-encoding gene, an explicit gene-content rationale for emission.
>

## nitrifier-denitrification-models.11 (claim)

The Mellbye model attributes elevated coculture N-oxide emission to a microaerobic environment created by coupled metabolism, when the O₂ demand of ammonia oxidation is exacerbated by NOB activity.

- conf: not stated
- class: not stated
- holds: the N. europaea and N. winogradskyi coculture
- src: mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Key Findings, §What

From the note:

> C-STEPDEN:B-0015 [Key Findings] Emission is driven by a microaerobic environment created by coupled metabolism.
>
> C-STEPDEN:B-0031 [What "the method" has actually represented] The model attributes elevated coculture N-oxide emission to a microaerobic environment created when the O₂ demand of ammonia oxidation is exacerbated by NOB activity.
>

## nitrifier-denitrification-models.12 (claim)

The iFC578 and iFC579 reconstructions were "based upon the Department of Energy (DOE) Joint Genome Institute (JGI) sequences… with automatic annotation and model building through the SEED… followed by hand annotation using the Kyoto Encyclopedia of Genes and Genomes (KEGG) database," and were "calibrated either to maximize biomass production or energy substrate uptake."

- conf: not stated
- class: not stated
- holds: the Methods of the Mellbye coculture model
- src: mellbyeGenomeScaleConstraintBased2018 (Methods text recovered)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0032 [What "the method" has actually represented] Per the Methods, the reconstructions were "based upon the Department of Energy (DOE) Joint Genome Institute (JGI) sequences… with automatic annotation and model building through the SEED… followed by hand annotation using the Kyoto Encyclopedia of Genes and Genomes (KEGG) database," and were "calibrated either to maximize biomass production or energy substrate uptake.
>
> C-STEPDEN:B-0070 [Caveats] Reaction counts, mechanisms, and N₂O-output facts are corroborated from abstracts, verbatim snippets, the Methods text recovered for Mellbye, and the companion 2016 paper.
>

## nitrifier-denitrification-models.13 (claim)

The integrated Mellbye coculture model is posted at github.com/chaplenf/microBiome-v2.1.

- conf: not stated
- class: not stated
- holds: microBiome-v2.1, the integrated iFC578 and iFC579 model
- src: mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §What, §Recommendations

From the note:

> C-STEPDEN:B-0033 [What "the method" has actually represented] The integrated model is posted at github.com/chaplenf/microBiome-v2.1.
>
> C-STEPDEN:B-0061 [Recommendations] These are the only published FBA/stoichiometric models located that emit N₂O as a distinct flux, and the Mellbye model (github.com/chaplenf/microBiome-v2.1) is the only community-scale one.
>

Not found in the cited text (where to look, not what is wrong): holds: ifc578; holds: ifc579

## nitrifier-denitrification-models.14 (claim)

The review's model index classes the iFC578 + iFC579 coculture model (microBiome-v2.1) as genome-scale dynamic FBA with abiotic reactions (SEED/KEGG), its N₂O mechanism as microaerobic conditions and NOR gene presence.

- conf: not stated
- class: not stated
- holds: N. europaea and Nitrobacter winogradskyi coculture
- src: mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Compact JSON

From the note:

> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

Not found in the cited text (where to look, not what is wrong): N₂O

## nitrifier-denitrification-models.15 (claim)

Perez-Garcia et al. (2014) and Mellbye et al. (2018) are the only published FBA/stoichiometric models the review located that emit N₂O as a distinct flux, and the Mellbye model is the only community-scale one.

- conf: not stated
- class: search (note: "the only published FBA/stoichiometric models located")
- search: searched, not found (note: "the only published FBA/stoichiometric models located")
- holds: published FBA/stoichiometric models located by the review's search
- src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §Recommendations

From the note:

> C-STEPDEN:B-0060 [Recommendations] **If the goal is an existing constraint-based model with explicit N₂O output:** Start from Perez-Garcia et al. (2014) and Mellbye et al. (2018).
>
> C-STEPDEN:B-0061 [Recommendations] These are the only published FBA/stoichiometric models located that emit N₂O as a distinct flux, and the Mellbye model (github.com/chaplenf/microBiome-v2.1) is the only community-scale one.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## nitrifier-denitrification-models.16 (claim)

The 2022 iGC535 reconstruction of N. europaea (Canto-Encalada et al., PLoS Computational Biology), a substantially re-curated successor in this lineage, reached over 90% prediction accuracy, predicting growth and oxygen uptake rates with 90.52% accuracy under chemolithotrophic and chemolithoorganotrophic conditions.

- conf: not stated
- class: not stated
- holds: N. europaea under chemolithotrophic and chemolithoorganotrophic conditions; growth and oxygen uptake rates
- src: cantoencaladaFluxBalanceAnalysis2022
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0035 [What "the method" has actually represented] The 2022 iGC535 reconstruction of *N. europaea* (Canto-Encalada et al., *PLoS Computational Biology*) — which reached over 90% prediction accuracy (predicting growth and oxygen uptake rates with 90.52% accuracy under chemolithotrophic and chemolithoorganotrophic conditions) — was a substantially re-curated successor, indicating that N-oxide reaction balancing in this lineage required considerable manual curation effort.
>

## nitrifier-denitrification-models.17 (claim)

The review's model index records iGC535 (N. europaea ATCC19718, genome-scale FBA in COBRA) as not resolving the N-oxide sub-steps, its focus being pollutant oxidation and growth, and as having no explicit N₂O output.

- conf: not stated
- class: not stated
- holds: N. europaea ATCC19718
- src: cantoencaladaFluxBalanceAnalysis2022
- trail: C-STEPDEN §Compact JSON

From the note:

> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

Not found in the cited text (where to look, not what is wrong): N-oxide; N₂O

## electron-overflow.1 (claim)

Perez-Garcia et al. (2014) found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460."

- conf: not stated
- class: model (note: "in these models")
- holds: the N. europaea SMN
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §Key Findings

From the note:

> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0012 [Key Findings] **N₂O emission in these models is mechanistically attributed to electron imbalance, not to a pathway gap in a four-step chain.** Perez-Garcia et al. found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460," and, verbatim, that "N2O is produced due to electron flow imbalances in the cell," with "Cytochromes play a key role in N2O production by directing electron flow" and "The cytochrome P460 reaction can potentially mitigate N2O emissions."
>

## electron-overflow.2 (claim)

Perez-Garcia et al. (2014) found that "N2O is produced due to electron flow imbalances in the cell."

- conf: not stated
- class: model (note: "in these models")
- holds: the N. europaea SMN
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §Key Findings

From the note:

> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0012 [Key Findings] **N₂O emission in these models is mechanistically attributed to electron imbalance, not to a pathway gap in a four-step chain.** Perez-Garcia et al. found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460," and, verbatim, that "N2O is produced due to electron flow imbalances in the cell," with "Cytochromes play a key role in N2O production by directing electron flow" and "The cytochrome P460 reaction can potentially mitigate N2O emissions."
>

## electron-overflow.3 (claim)

Perez-Garcia et al. (2014) found that "Cytochromes play a key role in N2O production by directing electron flow."

- conf: not stated
- class: model (note: "in these models")
- holds: the N. europaea SMN
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §Key Findings

From the note:

> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0012 [Key Findings] **N₂O emission in these models is mechanistically attributed to electron imbalance, not to a pathway gap in a four-step chain.** Perez-Garcia et al. found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460," and, verbatim, that "N2O is produced due to electron flow imbalances in the cell," with "Cytochromes play a key role in N2O production by directing electron flow" and "The cytochrome P460 reaction can potentially mitigate N2O emissions."
>

## electron-overflow.4 (claim)

Perez-Garcia et al. (2014) found that "The cytochrome P460 reaction can potentially mitigate N2O emissions."

- conf: not stated
- class: model (note: "in these models")
- holds: the N. europaea SMN
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §Key Findings

From the note:

> C-STEPDEN:B-0010 [Key Findings] **Discrete sub-steps + explicit N₂O output is demonstrated only for nitrifier denitrification in constraint-based models.** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of *N. europaea* energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes — the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
>
> C-STEPDEN:B-0012 [Key Findings] **N₂O emission in these models is mechanistically attributed to electron imbalance, not to a pathway gap in a four-step chain.** Perez-Garcia et al. found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460," and, verbatim, that "N2O is produced due to electron flow imbalances in the cell," with "Cytochromes play a key role in N2O production by directing electron flow" and "The cytochrome P460 reaction can potentially mitigate N2O emissions."
>

## electron-overflow.5 (claim)

The Perez-Garcia (2014) model's central, validated finding is that NO/N₂O emission is an electron-overflow phenomenon: nitrifier denitrification is "activated when the availability of electron donors exceeds that of electron sinks," dissipating excess reducing equivalents when O₂ is limiting.

- conf: not stated
- class: not stated
- holds: N. europaea under O₂ limitation
- src: perezgarciaClarifyingRegulationNO2014
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0023 [What "the method" has actually represented] **(A) Constraint-based/stoichiometric models that explicitly emit N₂O — the nitrifier-denitrification lineage.** The Perez-Garcia et al. (2014) SMN of *N. europaea* (51 reactions, 44 metabolites) is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
>
> C-STEPDEN:B-0025 [What "the method" has actually represented] The model's central, validated finding is that NO/N₂O emission is an electron-overflow phenomenon: nitrifier denitrification is "activated when the availability of electron donors exceeds that of electron sinks," dissipating excess reducing equivalents when O₂ is limiting.
>

## electron-overflow.6 (claim)

Both Perez-Garcia et al. (2014) and Mellbye et al. (2018) attribute N₂O emission to an intracellular electron-equivalent imbalance under O₂ limitation, not to a missing nosZ or a pathway gap in a four-step chain.

- conf: not stated
- class: not stated
- holds: the two stoichiometric/FBA models of nitrifier denitrification
- src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §TL;DR, §Key Findings

From the note:

> C-STEPDEN:B-0008 [TL;DR] - The strongest constraint-based matches are Perez-Garcia et al. (2014, *Water Research*) and Mellbye et al. (2018, *mSystems*): both stoichiometric/FBA models emit NO and N₂O as distinct outputs, and both attribute N₂O emission to an intracellular electron-equivalent imbalance under O₂ limitation, not to a missing *nosZ* in a four-step chain.
>
> C-STEPDEN:B-0012 [Key Findings] **N₂O emission in these models is mechanistically attributed to electron imbalance, not to a pathway gap in a four-step chain.** Perez-Garcia et al. found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460," and, verbatim, that "N2O is produced due to electron flow imbalances in the cell," with "Cytochromes play a key role in N2O production by directing electron flow" and "The cytochrome P460 reaction can potentially mitigate N2O emissions."
>
> C-STEPDEN:B-0057 [How the cases relate] Constraint-based/FBA models that explicitly output N₂O do so only where N₂O is a forced electron-overflow terminus in an organism lacking *nosZ* (nitrifier denitrification in *N. europaea*).
>

## electron-overflow.7 (claim)

In the demonstrated nitrifier-denitrification models, each transformation is encoded as a distinct reaction tied to its enzyme (NO₂⁻→NO by NirK; NO→N₂O by NorB), with N-oxides as intracellular species that can be drained by exchange reactions.

- conf: not stated
- class: not stated
- holds: the nitrifier-denitrification cases the review calls demonstrated
- src: none (the reviewer's synthesis of the nitrifier-denitrification models)
- trail: C-STEPDEN §How stepwise

From the note:

> C-STEPDEN:B-0041 [How stepwise N-cycle reactions enter a stoichiometric model] In the demonstrated nitrifier-denitrification cases, each transformation is encoded as a distinct reaction tied to its enzyme (e.g., NO₂⁻→NO by NirK; NO→N₂O by NorB), with N-oxides appearing as intracellular species that can be drained by exchange reactions.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## electron-overflow.8 (claim)

In these models the electron-balance logic is what forces emission: N₂O/NO appear when reducing-equivalent production outruns the available electron sink (O₂).

- conf: not stated
- class: not stated
- holds: the nitrifier-denitrification models
- src: none (the reviewer's synthesis of the nitrifier-denitrification models)
- trail: C-STEPDEN §How stepwise

From the note:

> C-STEPDEN:B-0041 [How stepwise N-cycle reactions enter a stoichiometric model] In the demonstrated nitrifier-denitrification cases, each transformation is encoded as a distinct reaction tied to its enzyme (e.g., NO₂⁻→NO by NirK; NO→N₂O by NorB), with N-oxides appearing as intracellular species that can be drained by exchange reactions.
>
> C-STEPDEN:B-0042 [How stepwise N-cycle reactions enter a stoichiometric model] The electron-balance logic is what forces emission: N₂O/NO appear when reducing-equivalent production outruns the available electron sink (O₂).
>

Not found in the cited text (where to look, not what is wrong): holds: models

## electron-overflow.9 (claim)

The constraint-based representation works for nitrifier denitrification because the model treats N-oxide release as an electron-overflow valve rather than as the controlled, regulated sequential respiration of a canonical denitrifier.

- conf: not stated
- class: not stated
- holds: nitrifier denitrification, contrasted with canonical denitrifiers
- src: none (the reviewer's synthesis)
- trail: C-STEPDEN §How stepwise

From the note:

> C-STEPDEN:B-0043 [How stepwise N-cycle reactions enter a stoichiometric model] This is precisely why the constraint-based representation works for nitrifier denitrification — the model treats N-oxide release as an electron-overflow valve rather than as the controlled, regulated sequential respiration of a canonical denitrifier.
>

## electron-overflow.10 (claim)

Constraint-based/FBA models that explicitly output N₂O do so only where N₂O is a forced electron-overflow terminus in an organism lacking nosZ (nitrifier denitrification in N. europaea); their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation.

- conf: not stated
- class: not stated
- holds: Perez-Garcia et al. (2014) and Mellbye et al. (2018); N. europaea
- src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018
- trail: C-STEPDEN §How the cases, §Recommendations

From the note:

> C-STEPDEN:B-0057 [How the cases relate] Constraint-based/FBA models that explicitly output N₂O do so only where N₂O is a forced electron-overflow terminus in an organism lacking *nosZ* (nitrifier denitrification in *N. europaea*).
>
> C-STEPDEN:B-0060 [Recommendations] **If the goal is an existing constraint-based model with explicit N₂O output:** Start from Perez-Garcia et al. (2014) and Mellbye et al. (2018).
>
> C-STEPDEN:B-0062 [Recommendations] Note their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation.
>

## n-oxide-balancing.1 (claim)

The detailed mass- and charge-balancing of the N-oxide reactions in iFC578/iFC579 (electron donors, quinone/cytochrome/NADH coupling) could not be confirmed from the text the review could access.

- conf: not stated
- class: not stated
- holds: the Mellbye coculture reconstructions iFC578 and iFC579
- src: mellbyeGenomeScaleConstraintBased2018
- limit: access (note: "could not be confirmed from accessible text")
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0034 [What "the method" has actually represented] A caveat from this review's investigation: the detailed mass-/charge-balancing of the N-oxide reactions in iFC578/iFC579 (electron donors, quinone/cytochrome/NADH coupling) could not be confirmed from accessible text.
>

Not found in the cited text (where to look, not what is wrong): holds: mellbye

## n-oxide-balancing.2 (claim)

For Perez-Garcia et al. (2014) and Mellbye et al. (2018), the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim, because their full-text Methods and reaction tables were partially inaccessible (publisher bot detection).

- conf: not stated
- class: not stated
- holds: the two nitrifier-denitrification models
- src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018
- limit: access (note: "partially inaccessible (publisher bot detection)")
- trail: C-STEPDEN §Caveats

From the note:

> C-STEPDEN:B-0069 [Caveats] - Full-text Methods/reaction tables for Perez-Garcia et al. (2014) and Mellbye et al. (2018) were partially inaccessible (publisher bot detection); the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim.
>

Not found in the cited text (where to look, not what is wrong): holds: nitrifier-denitrification; holds: models

## n-oxide-balancing.3 (claim)

That iGC535 (2022) was a substantially re-curated successor of the N. europaea reconstruction indicates, in the review's reading, that N-oxide reaction balancing in this lineage required considerable manual curation effort.

- conf: not stated
- class: reading (note: "indicating that N-oxide reaction balancing in this lineage required considerable manual curation effort")
- holds: the N. europaea reconstruction lineage
- src: cantoencaladaFluxBalanceAnalysis2022
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0035 [What "the method" has actually represented] The 2022 iGC535 reconstruction of *N. europaea* (Canto-Encalada et al., *PLoS Computational Biology*) — which reached over 90% prediction accuracy (predicting growth and oxygen uptake rates with 90.52% accuracy under chemolithotrophic and chemolithoorganotrophic conditions) — was a substantially re-curated successor, indicating that N-oxide reaction balancing in this lineage required considerable manual curation effort.
>

## n-oxide-balancing.4 (claim)

The documented difficulty specific to N₂O is "indirect but real": balancing the cytochrome/N-oxide reactions for mass and charge is error-prone.

- conf: not stated
- class: not stated
- holds: models balancing cytochrome/N-oxide reactions
- src: none (the note cites no source for it)
- trail: C-STEPDEN §How stepwise

From the note:

> C-STEPDEN:B-0044 [How stepwise N-cycle reactions enter a stoichiometric model] The documented difficulty specific to N₂O is indirect but real: balancing the cytochrome/N-oxide reactions for mass and charge is error-prone, and standard FBA biomass-maximization does not naturally predict byproduct (N-oxide) overflow without additional constraints — a general limitation noted across the byproduct-secretion modelling literature.
>

Not found in the cited text (where to look, not what is wrong): holds: models

## denitrifier-gems.1 (claim)

Single-strain denitrifier genome-scale models (GEMs) exist for Paracoccus denitrificans Pd1222, Thauera sp. MZ1T (iThauera861), Pseudomonas stutzeri A1501 (iPB890, iQY1018) and Pseudomonas aeruginosa (iMO1056, iSD1509); they represent denitrification but were built and validated for biomass yield, substrate utilization and polymer production, not for resolving N₂O as a distinct truncation output, so they collapse or do not feature N₂O as a resolved terminal readout.

- conf: not stated
- class: not stated
- holds: single-strain GEMs of canonical denitrifiers
- src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025, babaeiGenomescaleReconstructionMetabolic2015, yuanReconstructionMetabolicProfiling2023, oberhardt2008, dahalGenomescaleModelPseudomonas2023
- trail: C-STEPDEN §Key Findings

From the note:

> C-STEPDEN:B-0016 [Key Findings] **Single-strain denitrifier genome-scale models exist but collapse or do not feature N₂O as a resolved terminal readout.** GEMs exist for *Paracoccus denitrificans* Pd1222, *Thauera* sp. MZ1T (iThauera861), *Pseudomonas stutzeri* A1501 (iPB890, iQY1018), and *Pseudomonas aeruginosa* (iMO1056, iSD1509).
>
> C-STEPDEN:B-0017 [Key Findings] These represent denitrification but were built and validated for biomass yield, substrate utilization, and polymer production — not for resolving N₂O as a distinct truncation output.
>

## denitrifier-gems.2 (claim)

The Paracoccus denitrificans Pd1222 GEM (Bordel et al., 2024, mSystems; 972 genes, 1,371 reactions, 1,388 metabolites; reconstructed in RAST/SEED, simulated in COBRA-style FBA) was built and validated for biomass yields on carbon sources, including with NO₃⁻ as electron acceptor.

- conf: not stated
- class: not stated
- holds: P. denitrificans Pd1222; carbon-source biomass yields
- src: bordelGenomescaleMetabolicModel2024
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0036 [What "the method" has actually represented] **(B) Single-strain canonical denitrifier GEMs — sub-steps present in genome content, but N₂O not a resolved readout.** The *Paracoccus denitrificans* Pd1222 GEM (Bordel et al., 2024, *mSystems*; 972 genes, 1,371 reactions, 1,388 metabolites; reconstructed in RAST/SEED, simulated in COBRA-style FBA) was built and validated for biomass yields on carbon sources, including with NO₃⁻ as electron acceptor.
>

Not found in the cited text (where to look, not what is wrong): holds: carbon-source

## denitrifier-gems.3 (claim)

P. denitrificans is the textbook complete denitrifier (Nap, NirS, cNor, NosZ), yet the Pd1222 GEM publication's validated outputs concern carbon-source yields, not stepwise N-oxide fluxes or N₂O emission.

- conf: not stated
- class: not stated
- holds: P. denitrificans Pd1222
- src: bordelGenomescaleMetabolicModel2024
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0036 [What "the method" has actually represented] **(B) Single-strain canonical denitrifier GEMs — sub-steps present in genome content, but N₂O not a resolved readout.** The *Paracoccus denitrificans* Pd1222 GEM (Bordel et al., 2024, *mSystems*; 972 genes, 1,371 reactions, 1,388 metabolites; reconstructed in RAST/SEED, simulated in COBRA-style FBA) was built and validated for biomass yields on carbon sources, including with NO₃⁻ as electron acceptor.
>
> C-STEPDEN:B-0037 [What "the method" has actually represented] *P. denitrificans* is the textbook complete denitrifier (Nap, NirS, cNor, NosZ), yet the publication's validated outputs concern carbon-source yields, not stepwise N-oxide fluxes or N₂O emission.
>

## denitrifier-gems.4 (claim)

The Thauera sp. MZ1T model iThauera861 (Tec-Campos et al., 2025, PLoS Computational Biology; 861 genes, 2,384 reactions, 1,744 metabolites) explicitly notes that the organism makes denitrification intermediates including nitrous and nitric oxide, but the model was deployed for PHB/EPS polymer production and pollutant degradation, not N₂O resolution.

- conf: not stated
- class: not stated
- holds: Thauera sp. MZ1T
- src: teccamposGenomescaleMetabolicModel2025
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0038 [What "the method" has actually represented] The *Thauera* sp. MZ1T model iThauera861 (Tec-Campos et al., 2025, *PLoS Computational Biology*; 861 genes, 2,384 reactions, 1,744 metabolites) explicitly notes the organism makes denitrification intermediates including nitrous and nitric oxide, but the model was deployed for PHB/EPS polymer production and pollutant degradation, not N₂O resolution.
>

## denitrifier-gems.5 (claim)

The Pseudomonas stutzeri A1501 models (iPB890, Babaei et al., 2015; iQY1018, Yuan et al., 2023) and P. aeruginosa models (iMO1056, Oberhardt et al., 2008; iSD1509, Dahal et al., 2023) include denitrification for anaerobic growth but treat it as a route to N₂ and energy, not as a resolved N₂O-emitting sub-step chain.

- conf: not stated
- class: not stated
- holds: P. stutzeri A1501 and P. aeruginosa
- src: babaeiGenomescaleReconstructionMetabolic2015, yuanReconstructionMetabolicProfiling2023, oberhardt2008, dahalGenomescaleModelPseudomonas2023
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0039 [What "the method" has actually represented] *Pseudomonas stutzeri* A1501 models (iPB890, Babaei et al., 2015; iQY1018, Yuan et al., 2023) and *P. aeruginosa* models (iMO1056, Oberhardt et al., 2008; iSD1509, Dahal et al., 2023) include denitrification for anaerobic growth but treat it as a route to N₂/energy, not as a resolved N₂O-emitting sub-step chain.
>

## denitrifier-gems.6 (claim)

The review's model index records iSD1509 as a Pseudomonas aeruginosa PA14 genome-scale FBA model (BiGG), and iQY1018 as carrying the denitrification chain for N2 without resolving N2O.

- conf: not stated
- class: not stated
- holds: P. aeruginosa PA14; P. stutzeri A1501
- src: dahalGenomescaleModelPseudomonas2023, yuanReconstructionMetabolicProfiling2023
- trail: C-STEPDEN §Compact JSON

From the note:

> C-STEPDEN:B-0074 [Compact JSON index of key models] [ {"model":"SMN of Nitrosomonas europaea","organism":"Nitrosomonas europaea (AOB)","framework":"stoichiometric network + FBA","substeps_resolved":"partial (nitrifier denitrification NO2->NO->N2O; no nosZ)","n2o_explicit":true,"n2o_mechanism":"electron-equivalent imbalance / cytochrome P460","doi":"10.1016/j.watres.2014.04.049"}, {"model":"Multispecies AOB/NOB metabolic network","organism":"8 AOB/NOB species","framework":"stoichiometric network + FBA","substeps_resolved":"partial (NO redox reactions, NirK, CytP460, cNor)","n2o_explicit":true,"n2o_mechanism":"NO redox balance; CytP460 reduces N2O by 60%","doi":"10.1002/bit.25880"}, {"model":"iFC578 + iFC579 coculture (microBiome-v2.1)","organism":"N. europaea + Nitrobacter winogradskyi","framework":"genome-scale dynamic FBA + abiotic reactions (SEED/KEGG)","substeps_resolved":"partial (NO, NO2, N2O distinct; N2O tied to NOR gene)","n2o_explicit":true,"n2o_mechanism":"microaerobic conditions; NOR gene presence","doi":"10.1128/mSystems.00170-17"}, {"model":"iGC535","organism":"Nitrosomonas europaea ATCC19718","framework":"genome-scale FBA (COBRA)","substeps_resolved":"no (focus on pollutant oxidation/growth)","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1009828"}, {"model":"P. denitrificans Pd1222 GEM","organism":"Paracoccus denitrificans Pd1222","framework":"genome-scale FBA (RAST/SEED, COBRA)","substeps_resolved":"genes present (Nap,NirS,cNor,NosZ) but not resolved as N2O readout","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1128/msystems.01077-23"}, {"model":"iThauera861","organism":"Thauera sp. MZ1T","framework":"genome-scale FBA","substeps_resolved":"genes present; deployed for polymers/pollutants","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1371/journal.pcbi.1012736"}, {"model":"iPB890","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1039/c5mb00086f"}, {"model":"iQY1018","organism":"Pseudomonas stutzeri A1501","framework":"genome-scale FBA","substeps_resolved":"denitrification chain for N2; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1016/j.synbio.2023.10.001"}, {"model":"iSD1509","organism":"Pseudomonas aeruginosa PA14","framework":"genome-scale FBA (BiGG)","substeps_resolved":"denitrification for anaerobic growth; not N2O-resolved","n2o_explicit":false,"n2o_mechanism":null,"doi":"10.1038/s42003-023-04540-8"}, {"model":"Agrobacterium tumefaciens denitrification model","organism":"Agrobacterium tumefaciens","framework":"KINETIC/ODE metabolic network (not FBA)","substeps_resolved":"yes (Nap,NirK,NorB; regulation)","n2o_explicit":true,"n2o_mechanism":"incomplete/unbalanced enzyme expression during oxic-anoxic transition","doi":"10.3389/fmicb.2012.00370"}, {"model":"Modular denitrification OMZ ecosystem model","organism":"marine denitrifier functional types (community)","framework":"trait-based / thermodynamic ecosystem (not FBA)","substeps_resolved":"yes (modules of NO3->NO2->N2O->N2)","n2o_explicit":true,"n2o_mechanism":"community pathway gaps / niche partitioning","doi":"10.1073/pnas.2417421121"} ]
>

## denitrifier-gems.7 (claim)

Automated CarveMe drafts of P. stutzeri were noted to lack a functional anaerobic nitrate-respiration chain entirely.

- conf: not stated
- class: not stated
- holds: automated CarveMe draft reconstructions of P. stutzeri
- src: none (the note names CarveMe drafts without a reference)
- trail: C-STEPDEN §What

From the note:

> C-STEPDEN:B-0040 [What "the method" has actually represented] Automated CarveMe drafts of *P. stutzeri* were noted to lack a functional anaerobic nitrate-respiration chain entirely.
>

## denitrifier-gems.8 (claim)

Canonical complete-denitrifier GEMs carry the genes for all four steps but were neither built nor validated to emit N₂O as a resolved truncation product.

- conf: not stated
- class: not stated
- holds: complete-denitrifier GEMs the review located
- src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025
- trail: C-STEPDEN §How the cases

From the note:

> C-STEPDEN:B-0058 [How the cases relate] Canonical complete-denitrifier GEMs carry the genes for all four steps but were neither built nor validated to emit N₂O as a resolved truncation product.
>

Not found in the cited text (where to look, not what is wrong): holds: review

## denitrifier-gems.9 (claim)

The Pd1222 GEM (github.com/SergioBordel/ModelParacoccus) and iThauera861 both contain the full denitrification gene complement (nar/nap, nir, nor, nos); the review calls them the best-curated starting points for a complete-denitrifier GEM to extend.

- conf: not stated
- class: not stated
- holds: P. denitrificans Pd1222 and Thauera sp. MZ1T
- src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025
- trail: C-STEPDEN §Recommendations

From the note:

> C-STEPDEN:B-0063 [Recommendations] **If the goal is a complete-denitrifier GEM to extend:** The *Paracoccus denitrificans* Pd1222 GEM (github.com/SergioBordel/ModelParacoccus) and *Thauera* iThauera861 are the best-curated starting points; both contain the full denitrification gene complement (*nar/nap*, *nir*, *nor*, *nos*).
>

Not found in the cited text (where to look, not what is wrong): holds: mz1t

## community-models.1 (claim)

Community constraint-based models report aggregate process capability, not resolved denitrification sub-steps: reviews of community metabolic modelling (for example the "More is Different" review in mSystems, 2023) describe FBA/constraint-based community methods as inferring flux distributions and exchange/cross-feeding fluxes.

- conf: not stated
- class: not stated
- holds: community metabolic modelling as described by reviews
- src: anonMoreDifferentReview2023
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0045 [Bounding and negative facts] - **Community constraint-based models report aggregate process capability, not resolved denitrification sub-steps.** Reviews of community metabolic modelling (e.g., the "More is Different" review in *mSystems*, 2023) describe FBA/constraint-based community methods as inferring flux distributions and exchange/cross-feeding fluxes, with no instance located of resolving the four denitrification sub-steps with N₂O as a community-level truncation output.
>

## community-models.2 (claim)

The review located no instance of a community constraint-based model resolving the four denitrification sub-steps with N₂O as a community-level truncation output.

- conf: not stated
- class: search (note: "no instance located")
- search: searched, not found (note: "no instance located")
- holds: community metabolic modelling literature the review searched
- src: anonMoreDifferentReview2023
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0045 [Bounding and negative facts] - **Community constraint-based models report aggregate process capability, not resolved denitrification sub-steps.** Reviews of community metabolic modelling (e.g., the "More is Different" review in *mSystems*, 2023) describe FBA/constraint-based community methods as inferring flux distributions and exchange/cross-feeding fluxes, with no instance located of resolving the four denitrification sub-steps with N₂O as a community-level truncation output.
>

## community-models.3 (claim)

AGORA/AGORA2 gut reconstructions and gut community constraint-based models (CBM) include nitrate/nitrite reductase reactions but do not resolve a stepwise denitrification-to-N₂O readout.

- conf: not stated
- class: not stated
- holds: gut reconstructions and gut community models
- src: none (the note names AGORA/AGORA2 without a reference)
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0046 [Bounding and negative facts] AGORA/AGORA2 gut reconstructions and gut community CBM include nitrate/nitrite reductase reactions but do not resolve a stepwise denitrification-to-N₂O readout.
>

Not found in the cited text (where to look, not what is wrong): holds: models

