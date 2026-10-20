# Tier 3: interactive page (Plotly 7)

## Rules
- **The default view carries the message** with nothing touched: about 5% of readers move a slider. Write `default_view` in the storyboard first; if the default view needs the control to make sense, the page is not ready.
- **At most two controls on the page**, each changing something the text names ("move the depth: richness keeps climbing").
- **Uncertainty as outcomes:** a hypothetical-outcome plot (one draw per frame, Play to step) reads better than error bars alone.
- **Optional predict-then-reveal:** ask the reader to guess before a step shows the answer.
- **Nothing moves on load.** No autoplay; the check fails a page whose plots change by themselves.
- **It must still read at 390 px wide.**

## Cheat sheet (verified on plotly 7.1.0, kaleido 1.5.0, 2026-10-20)

- **Offline page:** first figure `pio.to_html(fig, include_plotlyjs=True, full_html=False, div_id="f1", auto_play=False)`, later figures `include_plotlyjs=False`. Plotly.js inline costs about 4.6 MB once per page. Never `'cdn'`.
- **`auto_play=False`, always.** The default (`True`) plays every frame on load: the smoke page's slider jumped through all its values in 1.5 s, so the view a reader lands on was the last frame, not the default.
- **Partial frames name their traces.** A frame that updates only the marker must say `go.Frame(data=[...], traces=[1])`; without `traces`, the frame's data is mapped onto trace 0 and the wrong thing moves.
- **Slider below an axis title:** give the slider `pad=dict(t=60)`, or its current-value label overlaps the x-axis title.
- **HOPs (hypothetical outcome plots):** one frame per draw, a Play button (`updatemenus` with `method="animate"`, `frame.duration` about 400 ms), a fixed axis range so frames are comparable.
- **Theme:** `fig.update_layout(**theme.plotly_layout(t))` sets font, background, colourway and grid from the tokens.
- **SVG fallback for `static/`:** `pio.write_image(fig, "f1.svg", width=900, height=500)` through kaleido (about 2.5 s). Kaleido needs Chrome: `BROWSER_PATH=$REPORT_CHROME`.
- **Live state in Playwright:** `document.getElementById('f1').data[1].x` and `.layout.sliders[0].active` show what the reader actually sees; screenshot after setting each control state.
