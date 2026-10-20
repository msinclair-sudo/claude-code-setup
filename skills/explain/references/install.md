# Installing the explain tools (maintainer notes)

`scripts/install-env.sh` builds everything; `scripts/check.sh` says whether it worked. Both are safe to re-run.

## What goes where
- **`report` conda env** (`~/miniforge3/envs/report`, about 3 GB): Python 3.12, manim 0.22.0, ffmpeg 9.0.2 (gpl build), cairo, pango, graphviz, matplotlib, pandas, scipy. pip layer: manim-voiceover 0.4.0, kokoro-onnx 0.6.1, plotly 7.1.0, kaleido 1.5.0, playwright 1.60.0.
- **`$REPORT_HOME/models`**: `kokoro-v1.0.onnx` (310 MB), `voices-v1.0.bin` (27 MB), from the kokoro-onnx `model-files-v1.0` release.
- **`$REPORT_HOME/vendor`**: `reveal.js-6.0.2`, `axe-core-4.14.0`, unpacked from `npm pack`. Pages inline these; nothing loads from a CDN.
- **Checksums**: `env/assets.sha256`. A mismatch deletes the file and stops the install.
- **Keys**: the script prints a `REPORT_*` block; append it to `~/.env`. `config.sh` reads only `REPORT_*`.

## Pitfalls met (2026-10-20)
- conda-forge names the soundfile package `pysoundfile`.
- conda-forge `sox` (14.4.2) pins `xz=5.0` and cannot coexist with ffmpeg 9; it is left out. manim-voiceover then logs "SoX could not be found!" on import. Only its recorder and some services use SoX; the Kokoro path does not.
- manim-voiceover is installed `--no-deps`, then its requirements minus manim, so pip never swaps out conda's manim.
- Python 3.13+ removed `audioop`, which pydub needs; keep the env at 3.12.
- Playwright is pinned to the biblion env's version so the cached `chromium-1243` is reused; `REPORT_CHROME` points at it for kaleido and stills.
- `grep -q` on `ffmpeg -encoders | …` trips `pipefail` (SIGPIPE); capture the output first.
- TeX Live (latex, dvisvgm) and pandoc come from the system, not the env.
