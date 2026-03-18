# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese Academy of Sciences (UCAS) Master's thesis written in LaTeX, using the `ucasthesis` template. The thesis covers porting and optimizing the Android Runtime (ART) execution engine to the LoongArch architecture.

## Build Command

```bash
cd /workspace/ucasthesis && ./artratex.sh xa Thesis.tex
```

This runs xelatex + bibtex (full compilation: xelatex → bibtex → xelatex × 2). Output goes to `Tmp/Thesis.pdf`.

The `artratex.sh` script accepts `<engine><bib>` parameters: engine = `x` (xelatex), `p` (pdflatex), `l` (lualatex); bib = `a` (bibtex), `b` (biber), omit to skip bibliography.

## Architecture

- `Thesis.tex` — Document root. Loads class/style, then includes all content files in order.
- `Style/` — Template layer (do not modify unless fixing template bugs):
  - `ucasthesis.cls` — Document class (page layout, title pages, TOC, declarations)
  - `ucasthesis.cfg` — Chinese/English label strings and declaration text
  - `artratex.sty` — Font detection, bibliography setup, headers/footers, listings config
  - `artracom.sty` — User-defined math macros and graphical helpers
- `Tex/` — All thesis content:
  - `Frontinfo.tex` — Title/author/advisor metadata (Chinese + English)
  - `Frontmatter.tex` — Cover pages, declaration, abstracts
  - `Mainmatter.tex` — Chains the six chapter files
  - `Chap_Intro.tex` through `Chap_Conclusion.tex` — Chapters 1–6
  - `Appendix.tex`, `Backmatter.tex` — Appendix, acknowledgements, publications
- `Biblio/ref.bib` — Bibliography database (GB/T 7714 citation styles)
- `Img/` — Figures (PDF and PNG)
- `Tmp/` — Build output (compiled PDF, aux files). Never edit or commit these files.

## External Dependencies

The actual ART source code and experiment data live outside this repo:
- ART code: `/workspace/aosp/art`
- Benchmark data & reports: `/workspace/aosp/tmp/MyBenchMark`

When modifying thesis content about implementation details, experiments, or performance results, always cross-check against those directories first.

## Conventions

- New chapters use `Tex/Chap_*.tex` naming.
- One commit = one type of change. Don't mix `Tmp/` artifacts or unrelated images.
- Validation = successful compilation with no reference/citation errors.
- `Report/` contains an independent mid-term report sub-project; keep it separate from main thesis commits.
