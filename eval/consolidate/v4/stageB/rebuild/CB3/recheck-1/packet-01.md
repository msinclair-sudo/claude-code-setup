## food-system.10 (claim)

Tubiello et al. concede that their own land-use-change component is probably too high: "recent studies have estimated that only 80% of deforestation may be linked to agriculture globally ... We are thus likely overestimating the food-related land use change component".

- conf: not stated
- class: not stated
- holds: the land-use-change component of the FAOSTAT food-system estimate
- src: tubielloGreenhouseGasEmissions2021
- trail: CB3-AG-EMISSIONS §6. Where the major

From the note:

> CB3-AG-EMISSIONS:B-0022 [2. Boundary A — the whole food system / agrifood system] **Tubiello et al. 2022 (FAOSTAT)**: 16.5 Gt CO2eq in 2019, **31%** (range 19–43%), from an assigned uncertainty of 30% on farm gate and pre/post-production and 50% on land-use change; AR5 GWP100 [4].
>
> CB3-AG-EMISSIONS:B-0023 [2. Boundary A — the whole food system / agrifood system] The same team's 2021 paper gave 33% for 2018 and explicitly reconciled it with Crippa: "Our estimate of 16 Gt CO2 eq yr−1 in 2018 is consistent with their findings, also considering their stated uncertainty range of 14–22 Gt CO2 eq yr−1" [5].
>
> CB3-AG-EMISSIONS:B-0091 [6. Where the major sources differ, and the reasons they give] Tubiello et al. concede their own land-use-change component is probably too high: "recent studies have estimated that only 80% of deforestation may be linked to agriculture globally ...
>
> CB3-AG-EMISSIONS:B-0092 [6. Where the major sources differ, and the reasons they give] We are thus likely overestimating the food-related land use change component" [5].
>

Not found in the cited text (where to look, not what is wrong): holds: food-system

## afolu.7 (claim)

AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, managed soils and pasture (CO2, N2O) 11%, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, synthetic fertilizer application (N2O) 3%, biomass burning (CH4, N2O) 1%.

- conf: not stated
- class: not stated
- holds: AFOLU, 2019; CH4 and N2O data from EDGAR; shares read off the rendered figure, not the text
- src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure)
- trail: CB3-AG-EMISSIONS §5. Boundary D

From the note:

> CB3-AG-EMISSIONS:B-0054 [5. Boundary D — soils, and nitrous oxide specifically] **Managed soils and pasture within AFOLU.** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, **managed soils and pasture (CO2, N2O) 11%**, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, **synthetic fertilizer application (N2O) 3%**, biomass burning (CH4, N2O) 1%; CH4 and N2O data from EDGAR [1, Fig. 7.3].
>
> CB3-AG-EMISSIONS:B-0055 [5. Boundary D — soils, and nitrous oxide specifically] I read these shares off the rendered figure, not the text.
>

## livestock.1 (claim)

Livestock's Long Shadow (2006) put livestock at 18% of total GHG.

- conf: not stated
- class: not stated
- holds: livestock, a sub-boundary with a documented revision history
- src: anonLivestockSLong2006
- trail: CB3-AG-EMISSIONS §4. Boundary C

From the note:

> CB3-AG-EMISSIONS:B-0049 [4. Boundary C — agricultural production alone (farm gate)] **Livestock, as a sub-boundary, has a documented revision history.** *Livestock's Long Shadow* (2006) put livestock at 18% of total GHG.
>
> CB3-AG-EMISSIONS:B-0050 [4. Boundary C — agricultural production alone (farm gate)] Gerber et al. 2013 revised this to "7.1 gigatonnes CO2-eq per annum, representing **14.5 percent** of all human-induced emissions", and its Annex states the reasons explicitly: a new GIS-based model (GLEAM) instead of statistical tables, a different reference period, IPCC 2006 rather than 2001 guidelines, different GWP values (296/298 for N2O and 23/25 for CH4 across the two reports), a narrower feed boundary, exclusion of soil organic matter losses under constant land use, and land-use-change emissions of 0.65 Gt rather than 2.4 Gt [12].
>

## soil-n2o.2 (claim)

By the reviewer's arithmetic, managed soils and pasture at 11% of 2019 AFOLU emissions (13 Gt) is ~1.4 Gt CO2eq, which against 59 Gt in 2019 is ~2.4% of global emissions.

- conf: not stated
- class: deriv (note: "My arithmetic")
- holds: managed soils and pasture within AFOLU (CO2 and N2O), 2019; AR6 GWP100; EDGAR data via AR6 Figure 7.3, whose shares were read off the rendered figure, not the text
- src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure)
- trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table

From the note:

> CB3-AG-EMISSIONS:B-0054 [5. Boundary D — soils, and nitrous oxide specifically] **Managed soils and pasture within AFOLU.** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, **managed soils and pasture (CO2, N2O) 11%**, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, **synthetic fertilizer application (N2O) 3%**, biomass burning (CH4, N2O) 1%; CH4 and N2O data from EDGAR [1, Fig. 7.3].
>
> CB3-AG-EMISSIONS:B-0055 [5. Boundary D — soils, and nitrous oxide specifically] I read these shares off the rendered figure, not the text.
>
> CB3-AG-EMISSIONS:B-0056 [5. Boundary D — soils, and nitrous oxide specifically] *My arithmetic:* 11% of 13 Gt = ~1.4 Gt CO2eq, which against 59 Gt in 2019 is **~2.4%** of global emissions; synthetic fertiliser application at 3% of 13 Gt = ~0.4 Gt, **~0.7%**.
>
> CB3-AG-EMISSIONS:B-0129 [8. Table of candidate shares] | 24 | Managed soils and pasture within AFOLU | ~2.4% *(my arithmetic)* | ~1.4 GtCO2-eq | 2019 | CO2 + N2O; AR6 GWP100 | AR6 WGIII Ch.7 Fig. 7.3 [1] | figure read from image |
>

## soil-n2o.4 (claim)

By the reviewer's arithmetic, cropland soils' 795 MtCO2 eq, an SRCCL figure given with medium confidence, is ~1.5% of SRCCL's implied total of ~52 Gt.

- conf: not stated
- class: deriv (note: "My arithmetic")
- holds: cropland soils N2O, 2007–2016; AR5 GWP100; against SRCCL's implied total; the 795 MtCO2 eq input carries IPCC's own assessed medium confidence
- src: ipccSummaryPolicymakers2019
- trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table

From the note:

> CB3-AG-EMISSIONS:B-0057 [5. Boundary D — soils, and nitrous oxide specifically] **Cropland soils, SRCCL.** "Cropland soils emitted around 3 MtN2O yr-1 (around 795 MtCO2 eq yr-1) during the period 2007–2016 (medium confidence)" [2, A.3.5].
>
> CB3-AG-EMISSIONS:B-0058 [5. Boundary D — soils, and nitrous oxide specifically] *My arithmetic:* against SRCCL's implied total of ~52 Gt, that is **~1.5%**.
>
> CB3-AG-EMISSIONS:B-0131 [8. Table of candidate shares] | 26 | Cropland soils N2O | ~1.5% *(my arithmetic)* | 795 MtCO2 eq | 2007–2016 | N2O; AR5 GWP100 | IPCC SRCCL A.3.5 [2] | *medium confidence* |
>

## soil-n2o.7 (claim)

Published estimates of N2O from agricultural soils as a share of global GHG emissions range from about 1.5% to 4.1%, depending on whether the category is cropland soils only, managed soils and pasture, or the full inventory "agricultural soils" line, and on the database and metric used; the 4.1% end rests on a single unverified source.

- conf: not stated
- class: not stated
- holds: the range spans SRCCL's cropland soils (~1.5%), EDGAR via AR6's managed soils and pasture (~2.4%), and Climate Watch/WRI's agricultural soils line via Our World in Data (4.1%)
- src: ipccSummaryPolicymakers2019, nabuursAgricultureForestryOther2022, ritchieSectorSectorWhere2020, climate
- trail: CB3-AG-EMISSIONS §9. Verdict, §Verdict

From the note:

> CB3-AG-EMISSIONS:A-004 [quote: Verdict] The review's honest statement of the evidence: published estimates of N₂O from agricultural soils as a share of global GHG range from about **1.5% to 4.1%**, depending on the category, database and metric.
>
> CB3-AG-EMISSIONS:A-006 [9. Verdict: which boundary produces a figure near five per cent?] **Nitrous oxide from agricultural soils (inventory category 3.D-equivalent): 4.1%**, Climate Watch/WRI for 2016, as presented by Our World in Data [11].
>
> CB3-AG-EMISSIONS:A-009 [9. Verdict: which boundary produces a figure near five per cent?] Independent reconstructions of the same quantity come in lower — ~3.5% from the Global N2O Budget [8, my arithmetic], ~2.4% for "managed soils and pasture" from EDGAR via AR6 [1], ~1.5% for cropland soils from SRCCL [2].
>
> CB3-AG-EMISSIONS:A-016 [9. Verdict: which boundary produces a figure near five per cent?] If a claim near 5% must be anchored, the honest statement of the evidence is: published estimates of N2O from agricultural soils as a share of global GHG emissions range from about **1.5% to 4.1%** depending on whether the category is cropland soils only, managed soils and pasture, or the full inventory "agricultural soils" line, and on the database and metric used.
>
> CB3-AG-EMISSIONS:A-017 [9. Verdict: which boundary produces a figure near five per cent?] The 4.1% end rests on a single unverified source.
>

## synthetic-fertiliser.1 (claim)

Field N2O from synthetic fertiliser application, from EDGAR via AR6, is ~3% of AFOLU, ~0.4 Gt CO2eq, in 2019.

- conf: not stated
- class: not stated
- holds: field N2O from synthetic fertiliser application, 2019, one of three numbers on three boundaries; the AFOLU shares read off the rendered AR6 Figure 7.3, not the text
- src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure)
- trail: CB3-AG-EMISSIONS §5. Boundary D

From the note:

> CB3-AG-EMISSIONS:B-0054 [5. Boundary D — soils, and nitrous oxide specifically] **Managed soils and pasture within AFOLU.** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, **managed soils and pasture (CO2, N2O) 11%**, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, **synthetic fertilizer application (N2O) 3%**, biomass burning (CH4, N2O) 1%; CH4 and N2O data from EDGAR [1, Fig. 7.3].
>
> CB3-AG-EMISSIONS:B-0055 [5. Boundary D — soils, and nitrous oxide specifically] I read these shares off the rendered figure, not the text.
>
> CB3-AG-EMISSIONS:B-0070 [5. Boundary D — soils, and nitrous oxide specifically] **Synthetic fertiliser specifically.** Three numbers, three boundaries:
>
> CB3-AG-EMISSIONS:B-0071 [5. Boundary D — soils, and nitrous oxide specifically] - Field N2O from synthetic fertiliser application, EDGAR via AR6: ~3% of AFOLU, ~0.4 Gt CO2eq, 2019 [1].
>

## synthetic-fertiliser.2 (claim)

By the reviewer's arithmetic, synthetic fertiliser application at 3% of 13 Gt is ~0.4 Gt, ~0.7% of global emissions.

- conf: not stated
- class: deriv (note: "My arithmetic")
- holds: synthetic fertiliser application (N2O), 2019; EDGAR via AR6 Figure 7.3, read off the rendered figure; AR6 GWP100; 60% uncertainty on N2O
- src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure)
- trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table

From the note:

> CB3-AG-EMISSIONS:B-0054 [5. Boundary D — soils, and nitrous oxide specifically] **Managed soils and pasture within AFOLU.** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, **managed soils and pasture (CO2, N2O) 11%**, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, **synthetic fertilizer application (N2O) 3%**, biomass burning (CH4, N2O) 1%; CH4 and N2O data from EDGAR [1, Fig. 7.3].
>
> CB3-AG-EMISSIONS:B-0055 [5. Boundary D — soils, and nitrous oxide specifically] I read these shares off the rendered figure, not the text.
>
> CB3-AG-EMISSIONS:B-0056 [5. Boundary D — soils, and nitrous oxide specifically] *My arithmetic:* 11% of 13 Gt = ~1.4 Gt CO2eq, which against 59 Gt in 2019 is **~2.4%** of global emissions; synthetic fertiliser application at 3% of 13 Gt = ~0.4 Gt, **~0.7%**.
>
> CB3-AG-EMISSIONS:B-0133 [8. Table of candidate shares] | 28 | Synthetic fertiliser application (EDGAR) | ~0.7% *(my arithmetic)* | ~0.4 GtCO2-eq | 2019 | N2O; AR6 GWP100 | AR6 WGIII Ch.7 Fig. 7.3 [1] | 60% on N2O |
>

## dns.1 (do not say)

"Agriculture accounts for about 5% of global greenhouse-gas emissions."

- why: No boundary in the current authoritative literature produces exactly five per cent for agriculture; three boundaries land close enough that a 'roughly 5%' claim could have originated from any of them, but five per cent is definitively not agricultural production (10.7–14.6%), not AFOLU (13–22%), not agriculture with land-use change for food (16–27%), and not the food system (21–42%).
- instead: five-per-cent.6, farm-gate.2, farm-gate.6, afolu.1
- trail: CB3-AG-EMISSIONS §9. Verdict

From the note:

> CB3-AG-EMISSIONS:A-005 [9. Verdict: which boundary produces a figure near five per cent?] **No boundary in the current authoritative literature produces exactly five per cent for agriculture, and none produces it for agricultural soils.** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable:
>
> CB3-AG-EMISSIONS:A-014 [9. Verdict: which boundary produces a figure near five per cent?] What five per cent is definitively **not**: it is not agricultural production (10.7–14.6%), not AFOLU (13–22%), not agriculture with land-use change for food (16–27%), and not the food system (21–42%).
>

Not found in the cited text (where to look, not what is wrong): "Agriculture accounts for about 5% of global greenhouse-gas emissions."

## dns.2 (do not say)

"Agricultural soils account for about 5% of global greenhouse-gas emissions."

- why: No boundary in the current authoritative literature produces exactly five per cent for agricultural soils, though three boundaries land close enough that a 'roughly 5%' claim could have originated from any of them; published estimates of N2O from agricultural soils range from about 1.5% to 4.1% of global emissions, and the 4.1% end rests on a single unverified source.
- instead: soil-n2o.7, soil-n2o.5
- trail: CB3-AG-EMISSIONS §9. Verdict

From the note:

> CB3-AG-EMISSIONS:A-005 [9. Verdict: which boundary produces a figure near five per cent?] **No boundary in the current authoritative literature produces exactly five per cent for agriculture, and none produces it for agricultural soils.** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable:
>
> CB3-AG-EMISSIONS:A-016 [9. Verdict: which boundary produces a figure near five per cent?] If a claim near 5% must be anchored, the honest statement of the evidence is: published estimates of N2O from agricultural soils as a share of global GHG emissions range from about **1.5% to 4.1%** depending on whether the category is cropland soils only, managed soils and pasture, or the full inventory "agricultural soils" line, and on the database and metric used.
>
> CB3-AG-EMISSIONS:A-017 [9. Verdict: which boundary produces a figure near five per cent?] The 4.1% end rests on a single unverified source.
>

Not found in the cited text (where to look, not what is wrong): "Agricultural soils account for about 5% of global greenhouse-gas emissions."

## dns.12 (do not say)

"FAO reports that agrifood systems made up 32% of global emissions in 2023."

- why: FAO's web summary says 32% while FAO's own COP30 takeaways document for the same report says 30%; the two FAO communications about one release disagree, and the review could not obtain the brief's own text to adjudicate.
- instead: food-system.13
- trail: CB3-AG-EMISSIONS §2. Boundary A, §7. Bounding

From the note:

> CB3-AG-EMISSIONS:B-0026 [2. Boundary A — the whole food system / agrifood system] The 2025 release for 2023 gives 16.5 Gt and states the share "fell from 38 to 32 percent in 2023" [9] — while FAO's own COP30 takeaways document for the *same* report says the share "decreased from 40 percent to 30 percent" [9a].
>
> CB3-AG-EMISSIONS:B-0027 [2. Boundary A — the whole food system / agrifood system] I could not obtain the brief's own text to adjudicate; two FAO communications about one release disagree by two percentage points.
>
> CB3-AG-EMISSIONS:B-0100 [7. Bounding and negative facts] - **Internal inconsistency in a current release.** FAO's 2025 agrifood figures: 32% per the FAO web summary [9] vs 30% per FAO's own COP30 takeaways for the same report [9a], against 29.7% for 2022 in Brief 94 [6].
>

Not found in the cited text (where to look, not what is wrong): "FAO reports that agrifood systems made up 32% of global emissions in 2023."

