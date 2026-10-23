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
> C-STEPDEN:B-0065 [Recommendations] **If the goal is to model N₂O accumulation mechanistically now:** Use the kinetic/ODE or cybernetic families (ASMN, electron-competition models, Song & Liu, Kampschreur), or the trait-based ecosystem approach (Zakem et al. 2024) for community pathway-gap scenarios.
>

## kinetic-trait-models.7 (claim)

The Domingo-Félez & Smets NDHA model and ASM3-based extensions are pseudo-mechanistic ODE models.

- conf: not stated
- class: not stated
- holds: outside the FBA/constraint-based family
- src: domingofelez
- trail: C-STEPDEN §Bounding

From the note:

> C-STEPDEN:B-0047 [Bounding and negative facts] - **The N₂O-resolving denitrification work sits outside the FBA/constraint-based family.** The Activated Sludge Model for Nitrogen (ASMN; Hiatt WC & Grady CP Jr., 2008, *Water Environment Research* 80(11):2145–2156) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters.
>
> C-STEPDEN:B-0052 [Bounding and negative facts] The Domingo-Félez & Smets NDHA model and ASM3-based extensions are pseudo-mechanistic ODE models.
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
> C-STEPDEN:B-0084 [Full reference list] Perez-Garcia O, Chandran K, Villas-Boas SG, Singhal N. Assessment of nitric oxide (NO) redox reactions contribution to nitrous oxide (N₂O) formation during nitrification using a multispecies metabolic network model.
>

## n-oxide-balancing.2 (claim)

For Perez-Garcia et al. (2014) and Mellbye et al. (2018), the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim, because their full-text Methods and reaction tables were partially inaccessible (publisher bot detection).

- conf: not stated
- class: not stated
- holds: the two nitrifier-denitrification models
- src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018
- limit: access (note: "partially inaccessible (publisher bot detection)")
- trail: C-STEPDEN §Caveats

From the note:

> C-STEPDEN:A-001 [Verdict] **PARTIALLY DEMONSTRATED.** Constraint-based/FBA models *have* represented N-oxide reduction as discrete enzymatic reactions with N₂O as an explicit, distinct modelled output — but only in the nitrifier-denitrification branch of ammonia-oxidizing bacteria (Perez-Garcia et al. 2014, 2016; Mellbye et al. 2018), where N₂O is terminal because the organism lacks *nosZ* and emission is mechanistically framed as electron-equivalent overflow under O₂ limitation.
>
> C-STEPDEN:B-0069 [Caveats] - Full-text Methods/reaction tables for Perez-Garcia et al. (2014) and Mellbye et al. (2018) were partially inaccessible (publisher bot detection); the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim.
>

