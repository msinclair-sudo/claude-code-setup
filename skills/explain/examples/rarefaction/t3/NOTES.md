# Tier 3 interactive page: what the loop did
- Automated rounds caught a tick collision in the chart corner, a title running into the Play button, the marker trace in the legend as "trace 2", and a log axis stopping short of 20,000.
- Fresh reader, blocking: the "deep" and "shallow" labels sat beside the wrong dots (position was their only link to a dot). Now each label is coloured like its dot and sits on opposite sides. At 390 px the title still touched the button: titles now wrap with `<br>` and Play sits below the chart.
- Also: titles state the point, a shaded band shows the middle 95% (208 to 228), "288 at 20,000 reads" marks the deep curve's end, "log scale" on the axis.
- Four automated reruns, one reader review per round (a round is build, check and review; reruns to clear automated faults inside a round do not count). Passed.
- Plotly text is drawn at run time, so the orphan-number check does not see it; the plot's numbers come from sim.py like every claim.
