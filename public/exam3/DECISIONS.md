# DECISIONS — Exam 3 PDF Site Build

## Deployment route
**Chosen:** Subfolder `public/exam3/` of existing `evolution-study-guide` repo.
**Rejected:** Standalone `evolution-exam3.pages.dev` Cloudflare Pages project.
**Reason:** Existing project already has Cloudflare Pages + GitHub auto-deploy wired up. Adding a subfolder ships on push with zero new infra. URL will be `https://evolution-study-guide.pages.dev/exam3/`.

## Site architecture
**Chosen:** Single-page HTML (`index.html`) with sidebar TOC, all 7 sections stacked.
**Rejected:** Seven `/sections/*.html` files.
**Reason:** Single page = Ctrl+K search works trivially across all verbatim content, no cross-file nav round-trips, faster deploy. At ~50KB of text the page stays snappy.

## Text preservation
- Native pdftotext (layout mode) is the PRIMARY source for every sentence.
- For pages with native_text_chars < 100 AND OCR_text_chars > 200 (i.e. image-only pages 39, 43, 48-50, 55-58, 62-76), OCR output is preserved verbatim in the body under a "**Page [N] (OCR'd text)**" heading, so no image-rendered text is lost.
- Broken grammar / misspellings from the source PDF (e.g. "raidoactive", "debri", "Cytocine", "domincated") are KEPT as-is per Hard Rule #1.

## Figures
- 138 embedded figures extracted via pymupdf, filtered to w≥80 & h≥80 (drops the page-border fillers that show up as 1-pixel-wide strips).
- Stored at `public/exam3/assets/figures/pNNN_imgM.{ext}` — name keeps page of origin for easy provenance.
- Each figure has its own OCR (psm 6) stored in `recon.json` and rendered under the figure in a `<details>` block titled "Text in this figure".
- Figures kept in page order (no redraws, no restyle, no crop beyond pymupdf's native extract).

## Interactive layer
- **Sidebar TOC** with active-section highlighting via `IntersectionObserver`.
- **Ctrl+K search** across all verbatim text with highlight + scroll-to-first-match.
- **Flashcard deck** auto-pulled from every "Key Terms" bullet and every "Potential Exam Qs" list using the same FSRS-light interval scheduler as the sibling exam3_review page (localStorage, grade Again/Hard/Good/Easy).
- **Geologic timeline** — horizontal scrubber with clickable eras (Ordovician → Cenozoic) that scroll to the matching verbatim block.
- **Big Five extinctions panel** — 5-column comparison grid from page 56 OCR + page 57 article.
- **Mnemonic slots** — empty `<!-- MNEMONIC SLOT -->` HTML comments left after every Key Concepts block so the user can drop in memory aids later.

## Accessibility
- Every `<img>` has alt = original caption + OCR'd in-figure text.
- Collapsible `<details>` for figure OCR so screen readers get the text at demand.

## Source stats (verified in recon.json)
- 76 pages
- 138 figures
- Native pdftotext: 927 lines, ~45 KB
- Native + OCR combined: ~120 KB — OCR recovers ~75 KB of text that pdftotext misses.
