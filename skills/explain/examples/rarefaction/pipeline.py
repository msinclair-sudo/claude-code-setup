"""Metabarcoding, simulated end to end: cells in the soil -> 16S copies -> PCR -> reads at a sequencing depth.

Every number the metabarcoding exemplar shows comes from here (seed fixed). Run it to print them.
The model is deliberately simple and says so on screen ("simulated"):
  cells        lognormal abundances over N_TAXA taxa (a few common, many rare)
  16S copies   each taxon carries 1 to 10 copies of the 16S rRNA gene per genome
  PCR          each taxon's barcode amplifies with its own efficiency for CYCLES cycles
  sequencing   reads are a random draw (multinomial) from the amplicon pool, at a chosen depth
  rarefying    a random subsample without replacement down to a common depth
"""
import numpy as np

SEED, N_TAXA, CELLS, CYCLES = 7, 80, 100_000, 25
DEPTHS = (500, 5_000, 50_000)
DEEP, SHALLOW, DRAWS = 50_000, 2_000, 200


def community():
    rng = np.random.default_rng(SEED)
    w = np.sort(rng.lognormal(0, 2.0, N_TAXA))[::-1]
    cells = np.maximum(1, np.round(w / w.sum() * CELLS)).astype(int)
    copies = rng.choice(np.arange(1, 11), N_TAXA, p=np.r_[.22, .2, .16, .12, .1, .07, .05, .04, .02, .02])
    eff = rng.uniform(0.88, 0.95, N_TAXA)          # per-cycle amplification efficiency
    return cells, copies, eff


def amplicons(cells, copies, eff):
    """Expected share of the amplicon pool per taxon after PCR."""
    a = cells * copies * (1 + eff) ** CYCLES
    return a / a.sum()


def sequence(pool, depth, rng):
    return rng.multinomial(depth, pool)


def rarefy(counts, depth, rng):
    reads = np.repeat(np.arange(len(counts)), counts)
    return np.bincount(rng.choice(reads, size=depth, replace=False), minlength=len(counts))


def observed(counts):
    return int((counts > 0).sum())


def data():
    cells, copies, eff = community()
    true = cells / cells.sum()
    pool = amplicons(cells, copies, eff)
    rng = np.random.default_rng(SEED + 1)
    runs = {d: sequence(pool, d, rng) for d in DEPTHS}
    deep, shallow = sequence(pool, DEEP, rng), sequence(pool, SHALLOW, rng)
    draws = np.array([observed(rarefy(deep, SHALLOW, rng)) for _ in range(DRAWS)])
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return dict(cells=cells, copies=copies, eff=eff, true=true, pool=pool, runs=runs,
                deep=deep, shallow=shallow, obs_deep=observed(deep), obs_shallow=observed(shallow),
                rare_draws=draws, rare_mean=float(draws.mean()), rare_lo=int(round(lo)), rare_hi=int(round(hi)))


if __name__ == "__main__":
    d = data()
    t, p = d["true"], d["pool"]
    print(f"{N_TAXA} taxa, {CELLS:,} cells; most common {d['cells'][0]} cells ({t[0]:.1%}); "
          f"{(d['cells'] <= 10).sum()} taxa with 10 cells or fewer")
    print("copies 1-10, range in community:", d["copies"].min(), "-", d["copies"].max())
    print(f"PCR: efficiency {d['eff'].min():.2f}-{d['eff'].max():.2f}, {CYCLES} cycles")
    shift = np.abs(p - t)
    k = int(np.argmax(p / t)); j = int(np.argmin(p / t))
    print(f"largest gain from PCR+copies: taxon {k+1} {t[k]:.1%} of cells -> {p[k]:.1%} of amplicons")
    print(f"largest loss: taxon {j+1} {t[j]:.1%} of cells -> {p[j]:.1%} of amplicons")
    print("top 5 cells %:", np.round(t[:5] * 100, 1), " amplicons %:", np.round(p[:5] * 100, 1))
    for dep, c in d["runs"].items():
        rel = c / c.sum()
        print(f"depth {dep:>6,}: {observed(c)} taxa seen; top taxon {rel[0]:.1%} (pool {p[0]:.1%}); "
              f"taxa in pool below 1/{dep}: {(p < 1 / dep).sum()}")
    print(f"two samples: deep {DEEP:,} reads -> {d['obs_deep']} taxa; shallow {SHALLOW:,} -> {d['obs_shallow']} taxa")
    print(f"deep rarefied to {SHALLOW:,}: mean {d['rare_mean']:.1f}, middle 95% {d['rare_lo']}-{d['rare_hi']}; "
          f"shallow inside: {d['rare_lo'] <= d['obs_shallow'] <= d['rare_hi']}")
