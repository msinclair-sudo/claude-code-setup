"""Tier 3 figures for the rarefaction exemplar (data from ../../sim.py).

f1: both rarefaction curves with a depth slider (default 2,000 reads, where the comparison is fair).
f2: hypothetical outcome plot of the deep sample rarefied to 2,000 reads, one subsample per frame.
"""
import importlib.util
from pathlib import Path

import numpy as np
import plotly.graph_objects as go

_spec = importlib.util.spec_from_file_location("sim", Path(__file__).resolve().parents[2] / "sim.py")
sim = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(sim)


def figures(t: dict) -> dict:
    c = t["color"]
    d = sim.data()
    rng = np.random.default_rng(3)
    dd = np.unique(np.r_[np.linspace(100, 2000, 12), np.linspace(2000, sim.DEEP, 16)].astype(int))
    ds = np.unique(np.linspace(100, sim.SHALLOW, 12).astype(int))
    cd, cs = sim.curve(d["deep"], dd, rng, reps=10), sim.curve(d["shallow"], ds, rng, reps=10)
    marks = [500, 1000, 2000]
    at = lambda depths, curve, x: float(np.interp(x, depths, curve))

    def markers(x):
        yd, ys = at(dd, cd, x), at(ds, cs, x)
        if x == sim.SHALLOW:  # the published counts at the comparison depth
            yd, ys = d["rare_mean"], d["obs_shallow"]
        return [go.Scatter(x=[x, x], y=[yd, ys], mode="markers+text",
                           marker=dict(size=[15, 11], color=[c["accent"], c["accent2"]], line=dict(width=2, color=c["bg"])),
                           text=[f"  deep {round(yd)}", f"shallow {round(ys)}  "], textposition=["middle right", "middle left"],
                           textfont=dict(size=16, color=[c["accent"], c["accent2"]]), hoverinfo="skip", showlegend=False,
                           name="at depth")]

    f1 = go.Figure([
        go.Scatter(x=dd, y=cd, mode="lines", line=dict(width=3, color=c["accent"]), name="deep sample (20,000 reads)",
                   hovertemplate="%{x:,} reads: %{y:.0f} taxa<extra>deep</extra>"),
        go.Scatter(x=ds, y=cs, mode="lines", line=dict(width=3, color=c["accent2"]), name="shallow sample (2,000 reads)",
                   hovertemplate="%{x:,} reads: %{y:.0f} taxa<extra>shallow</extra>"),
        *markers(sim.SHALLOW)])
    f1.frames = [go.Frame(data=markers(x), traces=[2], name=str(x)) for x in marks]
    f1.update_layout(
        title="At a depth both reach,<br>the samples agree", height=540,
        annotations=[dict(x=4.301, y=d["obs_deep"], xref="x", yref="y", text=f"{d['obs_deep']} at 20,000 reads",
                          showarrow=False, xanchor="right", yanchor="bottom", font=dict(color=c["accent"], size=14))],
        xaxis=dict(title="reads used (log scale)", type="log", range=[2, 4.4], tickvals=[500, 2000, 20000],
                   ticktext=["500", "2,000", "20,000"]),
        yaxis=dict(title="taxa observed", range=[0, 320]),
        legend=dict(x=0.98, y=0.04, xanchor="right", yanchor="bottom", bgcolor="rgba(0,0,0,0)"),
        sliders=[dict(active=marks.index(sim.SHALLOW), pad=dict(t=70), currentvalue=dict(prefix="compare at: ", suffix=" reads"),
                      steps=[dict(label=f"{x:,}", method="animate",
                                  args=[[str(x)], dict(mode="immediate", frame=dict(duration=0), transition=dict(duration=0))])
                             for x in marks])])

    hops = d["rare_draws"][:20]
    bars = lambda v: [go.Bar(x=["deep, rarefied", "shallow"], y=[v, d["obs_shallow"]],
                             marker_color=[c["accent"], c["accent2"]], text=[str(v), str(d["obs_shallow"])],
                             textposition="outside", textfont=dict(size=15), width=0.5)]
    f2 = go.Figure(bars(int(hops[0])))
    f2.frames = [go.Frame(data=bars(int(v)), name=str(i)) for i, v in enumerate(hops)]
    f2.add_shape(type="rect", xref="x", yref="y", x0=-0.3, x1=0.3, y0=d["rare_lo"], y1=d["rare_hi"],
                 line=dict(width=0), fillcolor=c["fg"], opacity=0.12, layer="above")
    f2.add_annotation(x=-0.3, y=d["rare_hi"], xref="x", yref="y", text=f"middle 95%: {d['rare_lo']} to {d['rare_hi']}",
                      showarrow=False, xanchor="left", yanchor="bottom", yshift=26, font=dict(size=13, color=c["muted"]))
    f2.update_layout(title="Subsamples vary, around<br>the shallow sample's count", height=480, margin=dict(b=110, t=120),
                     yaxis=dict(title="taxa observed", range=[0, 300]), showlegend=False,
                     updatemenus=[dict(type="buttons", x=0, y=-0.18, xanchor="left", yanchor="top", showactive=False,
                                       buttons=[dict(label="Play 20 subsamples", method="animate",
                                                     args=[None, dict(frame=dict(duration=500, redraw=True),
                                                                      transition=dict(duration=0), fromcurrent=False)])])])
    return {"f1": f1, "f2": f2}
