"""Tier 1 figures for the rarefaction exemplar (data from ../../sim.py)."""
import importlib.util
from pathlib import Path

import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
import numpy as np

_spec = importlib.util.spec_from_file_location("sim", Path(__file__).resolve().parents[2] / "sim.py")
sim = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(sim)


def style(t):
    c = t["color"]
    plt.rcParams.update({
        "font.family": t["font"]["manim"], "svg.fonttype": "path", "font.size": 20,
        "axes.edgecolor": c["muted"], "axes.labelcolor": c["fg"], "text.color": c["fg"],
        "xtick.color": c["muted"], "ytick.color": c["muted"],
        "axes.spines.top": False, "axes.spines.right": False, "axes.titlelocation": "left",
        "axes.titlesize": 22, "axes.titleweight": "bold",
    })
    return c


def make(out: Path, t: dict):
    c = style(t)
    d = sim.data()
    deep, shallow = c["accent"], c["accent2"]

    # fig1: small multiples, as sequenced vs at a common depth
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.6), sharey=True)
    a, b = axes
    a.bar([0, 1], [d["obs_deep"], d["obs_shallow"]], color=[deep, shallow], width=0.6)
    a.set_title("As sequenced")
    a.set_xticks([0, 1], ["deep\n20,000 reads", "shallow\n2,000 reads"])
    for x, v in ((0, d["obs_deep"]), (1, d["obs_shallow"])):
        a.text(x, v + 6, str(v), ha="center", va="bottom", fontsize=20)
    b.bar([0, 1], [d["rare_mean"], d["obs_shallow"]], color=[deep, shallow], width=0.6)
    b.errorbar([0], [d["rare_mean"]], yerr=[[d["rare_mean"] - d["rare_lo"]], [d["rare_hi"] - d["rare_mean"]]],
               color=c["fg"], capsize=6, lw=1.5)
    b.set_title("Both at 2,000 reads")
    b.set_xticks([0, 1], ["deep, rarefied", "shallow"])
    b.text(0, d["rare_hi"] + 6, f"{round(d['rare_mean'])}", ha="center", va="bottom", fontsize=20)
    b.text(1, d["obs_shallow"] + 6, str(d["obs_shallow"]), ha="center", va="bottom", fontsize=20)
    a.set_ylabel("taxa observed"); a.set_ylim(0, 330)
    for ax in axes:
        ax.tick_params(axis="x", length=0)
    fig.tight_layout(); fig.savefig(out / "fig1.svg", transparent=True); plt.close(fig)

    # fig2: the deep sample's rarefaction curve, with the shallow sample on it
    rng = np.random.default_rng(3)
    depths = np.unique(np.r_[np.linspace(100, 2000, 12), np.linspace(2000, sim.DEEP, 16)].astype(int))
    curve = sim.curve(d["deep"], depths, rng, reps=10)
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.plot(depths, curve, color=deep, lw=2.5)
    ax.scatter([sim.SHALLOW], [d["obs_shallow"]], s=70, color=shallow, zorder=3)
    ax.annotate("shallow sample", (sim.SHALLOW, d["obs_shallow"]), xytext=(18, -26), textcoords="offset points",
                color=shallow, fontsize=20)
    ax.annotate("deep sample, subsampled", (12000, curve[np.searchsorted(depths, 12000)]), xytext=(0, -30),
                textcoords="offset points", color=deep, fontsize=20, ha="center")
    ax.set_title("")  # the slide title says it
    ax.set_xlabel("reads"); ax.set_ylabel("taxa observed")
    ax.set_ylim(0, 330); ax.set_xlim(0, sim.DEEP * 1.02)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{int(v):,}"))
    fig.tight_layout(); fig.savefig(out / "fig2.svg", transparent=True); plt.close(fig)
