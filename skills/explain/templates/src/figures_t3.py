"""Tier 3 figures. figures(t) returns {id: plotly Figure}; page.md places each with {{plot:id}}.

The default view (no interaction) must carry the message. At most 2 controls on the page.
Partial frames name their traces (traces=[1]); build passes auto_play=False.
"""
import plotly.graph_objects as go


def figures(t: dict) -> dict:
    xs = [1000, 3000, 6000, 9000]
    f1 = go.Figure([go.Scatter(x=[0, 10000], y=[0, 400], mode="lines", line=dict(width=3)),
                    go.Scatter(x=[xs[0]], y=[100], mode="markers", marker=dict(size=14))])
    f1.frames = [go.Frame(data=[go.Scatter(x=[x], y=[x / 25])], traces=[1], name=str(x)) for x in xs]
    f1.update_layout(title="A title that states what to notice", showlegend=False,
                     xaxis_title="x (unit)", yaxis_title="y (unit)",
                     sliders=[dict(active=0, pad=dict(t=60), currentvalue=dict(prefix="x: "),
                                   steps=[dict(label=str(x), method="animate",
                                               args=[[str(x)], dict(mode="immediate", frame=dict(duration=0))])
                                          for x in xs])])
    return {"f1": f1}
