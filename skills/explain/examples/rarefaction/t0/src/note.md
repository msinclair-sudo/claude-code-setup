# Deeper sequencing finds more taxa, even in the same community

<p class="x-message">Compare richness only at a common depth: rarefy both samples to the smaller one first.</p>

<span class="x-label">simulated</span> In a simulated community of 300 taxa, a sample with 20,000 reads shows 288 taxa and a sample with 2,000 reads shows 221. Both come from the same community, so the gap of 67 taxa is depth, not biology.

Rarefaction estimates the number of taxa expected in a random subsample of a smaller, common size, so samples of unequal size can be compared (Hurlbert 1971; Gotelli and Colwell 2001). Rarefied to 2,000 reads, the deep sample shows 218 taxa on average, and the middle 95% of 200 subsamples span 208 to 228. The difference is gone.

The cost: rarefying throws reads away. McMurdie and Holmes (2014) showed in simulations that it loses statistical power when testing which taxa differ in abundance, so use it for comparing richness, not for that.

<div class="x-sources">Sources: Hurlbert (1971) Ecology 52: 577–586, doi:10.2307/1934145. Gotelli and Colwell (2001) Ecology Letters 4: 379–391, doi:10.1046/j.1461-0248.2001.00230.x. McMurdie and Holmes (2014) PLoS Computational Biology 10: e1003531, doi:10.1371/journal.pcbi.1003531. Simulation: sim.py, seed 7.</div>
