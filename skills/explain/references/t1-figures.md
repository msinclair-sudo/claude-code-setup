# Tier 1: figure report (static page)

## Cheat sheet (verified 2026-10-20)

- **The page must pass `explainlib.static_check`** (a verbatim copy of the harness's publish check): no script, link, audio, video, form, `@import` or external `url()`; images are `.svg .png .jpg .gif .webp` files beside `index.html` or `data:image` URIs; at most 30 images, 10 MB each, 40 MB together; `index.html` at most 2 MiB. `x run python -m explainlib.static_check <dir>` prints the faults.
- **Fonts:** system stacks only (`theme.css` gives `Lato, 'Noto Sans', 'Segoe UI', system-ui`); webfonts would need `url()` and are refused.
- **matplotlib:** `matplotlib.use("svg")`; `rcParams["svg.fonttype"] = "path"` (text as outlines, renders the same everywhere); `savefig(..., transparent=True)` or the figure sits in a white box on the page colour. Lowest invalid-chart rate of the libraries tested in the literature; prefer it over seaborn.
- **Graphviz:** `graphviz.Digraph(...).pipe()` with `format="svg"`; `rankdir="BT"` draws hierarchies upward; `bgcolor="transparent"`. Text stays as `<text>` in the font named; Lato is on this machine, a reader without it gets the fallback.
- **Maths:** `scripts/tex2svg.sh 'tex' out.svg [hex] [scale]`: LaTeX, then dvisvgm with glyphs as paths. Scale defaults to 1.8 (10 pt type is tiny beside 18 px body text).
- **Alt text:** every `<img>` has `alt` saying what the figure shows ("Curve rising steeply then flattening near 400 taxa by 10,000 reads"), not what it is ("a line chart").
- **Measure is about 72 characters:** `main { max-width: 72ch }` from the tokens.
