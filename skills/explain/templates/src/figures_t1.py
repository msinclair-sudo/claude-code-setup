"""Tier 1 figures. make(out, t) writes each figure file into `out` (build/)."""
from pathlib import Path

import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt


def style(t):
    c = t["color"]
    plt.rcParams.update({
        "font.family": t["font"]["manim"], "svg.fonttype": "path", "font.size": 12,
        "axes.edgecolor": c["muted"], "axes.labelcolor": c["fg"], "text.color": c["fg"],
        "xtick.color": c["muted"], "ytick.color": c["muted"],
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.titlelocation": "left", "axes.titlesize": 14,
    })
    return c


def make(out: Path, t: dict):
    c = style(t)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot([0, 1, 2], [0, 1, 4], color=c["accent"], lw=2.5)
    ax.set_title("A title that states what to notice")
    ax.set_xlabel("x (unit)"); ax.set_ylabel("y (unit)")
    fig.tight_layout(); fig.savefig(out / "fig1.svg", transparent=True); plt.close(fig)
