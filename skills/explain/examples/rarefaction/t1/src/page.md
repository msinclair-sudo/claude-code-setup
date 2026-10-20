# Deeper sequencing finds more taxa, even in the same community

<p class="x-message">Compare richness only at a common depth: rarefy both samples to the smaller one first.</p>

Two samples drawn from one simulated community of 300 taxa. The deep sample has ten times as many reads, and it shows 67 more taxa. Nothing about the community differs.

<figure><img class="x-wide-only" src="fig1.svg" alt="Left: the deep sample shows 288 taxa and the shallow sample 221. Right: rarefied to 2,000 reads, the deep sample shows 218 taxa, within a range of 208 to 228, beside the shallow sample's 221."><img class="x-narrow-only" src="fig1-narrow.svg" alt="Left: the deep sample shows 288 taxa and the shallow sample 221. Right: rarefied to 2,000 reads, the deep sample shows 218 taxa, within a range of 208 to 228, beside the shallow sample's 221."><figcaption><span class="x-label">simulated</span>Rarefied to 2,000 reads, the deep sample shows 218 taxa on average; the middle 95% of 200 subsamples span 208 to 228, and the shallow sample's 221 falls inside that range. The gap is gone.</figcaption></figure>

Rarefaction estimates the number of taxa expected in a random subsample of a smaller, common size, so samples of unequal size can be compared (Hurlbert 1971; Gotelli and Colwell 2001). The curve shows why it is needed: subsample the deep sample's reads at increasing depths, and the count of taxa rises steeply at first, then slowly. The shallow sample lands on that curve.

<figure><img src="fig2.svg" alt="A curve rising steeply then flattening as reads increase; the shallow sample's single point lies on the deep sample's curve at 2,000 reads."><figcaption><span class="x-label">simulated</span>At the same depth, the two samples agree: the shallow sample falls on the deep sample's curve.</figcaption></figure>

The cost: rarefying throws reads away. McMurdie and Holmes (2014) showed in simulations that it loses statistical power when testing which taxa differ in abundance, so use it to compare richness, not for that.

<div class="x-sources">Sources: Hurlbert (1971) Ecology 52: 577–586, doi:10.2307/1934145. Gotelli and Colwell (2001) Ecology Letters 4: 379–391, doi:10.1046/j.1461-0248.2001.00230.x. McMurdie and Holmes (2014) PLoS Computational Biology 10: e1003531, doi:10.1371/journal.pcbi.1003531. Simulation: sim.py, seed 7.</div>
