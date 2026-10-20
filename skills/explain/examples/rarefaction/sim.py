"""Rarefaction exemplar data: one simulated community, two samples at different depths.

Every number the exemplars show comes from here (seed fixed). Run it to print them.
"""
import numpy as np

SEED, N_TAXA, DEEP, SHALLOW, DRAWS = 7, 300, 20000, 2000, 200


def community(seed=SEED):
    rng = np.random.default_rng(seed)
    w = rng.lognormal(mean=0, sigma=1.8, size=N_TAXA)
    return w / w.sum()


def sample(p, depth, rng):
    """Reads per taxon when `depth` reads are drawn from community proportions p."""
    return rng.multinomial(depth, p)


def observed(counts):
    return int((counts > 0).sum())


def rarefy(counts, depth, rng):
    """Subsample `depth` reads without replacement from a sample's reads."""
    reads = np.repeat(np.arange(len(counts)), counts)
    pick = rng.choice(reads, size=depth, replace=False)
    return np.bincount(pick, minlength=len(counts))


def curve(counts, depths, rng, reps=20):
    """Mean observed richness when the sample is rarefied to each depth."""
    return np.array([np.mean([observed(rarefy(counts, d, rng)) for _ in range(reps)]) if d < counts.sum()
                     else observed(counts) for d in depths])


def data():
    rng = np.random.default_rng(SEED + 1)
    p = community()
    deep, shallow = sample(p, DEEP, rng), sample(p, SHALLOW, rng)
    draws = [observed(rarefy(deep, SHALLOW, rng)) for _ in range(DRAWS)]
    return dict(p=p, deep=deep, shallow=shallow, obs_deep=observed(deep), obs_shallow=observed(shallow),
                rare_draws=np.array(draws), rare_mean=float(np.mean(draws)),
                rare_lo=int(round(np.percentile(draws, 2.5))), rare_hi=int(round(np.percentile(draws, 97.5))))


if __name__ == "__main__":
    d = data()
    print(f"taxa in community {N_TAXA}; deep {DEEP} reads -> {d['obs_deep']} taxa; shallow {SHALLOW} reads -> {d['obs_shallow']} taxa")
    print(f"deep rarefied to {SHALLOW}: mean {d['rare_mean']:.1f}, 95% of draws {d['rare_lo']}-{d['rare_hi']}")
    rng = np.random.default_rng(3)
    ds = [500, 1000, 2000, 5000, 10000, 20000]
    print("curve deep:", dict(zip(ds, np.round(curve(d['deep'], ds, rng), 1))))
