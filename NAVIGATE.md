# Navigation — Evolution Study Guide

Live: https://evolution-study-guide.pages.dev

## What lives where

All shipping code is under `public/`. Shared CSS + JS are shared across all exam pages.

```
public/
├── index.html                 Home / landing
├── exam1_review.html          Exam 1 · pulls js/content-exam1.js
├── exam2_review.html          Exam 2 · pulls js/content-exam2.js
├── exam3_review.html          Exam 3 · pulls js/content-exam3.js
├── exam3_lecture.html         Verbatim lecture (standalone, 412 KB)
├── textbook.html              Textbook browser (standalone)
├── visuals.html               Interactive visuals (standalone)
├── exam3/index.html           Exam 3 alt layout
├── css/
│   └── esg.css                ONE stylesheet for every review page
├── js/
│   ├── esg-ui.js              Renderer (sidebar, modes, blocks, flashcards, test)
│   ├── esg-db.js              IndexedDB + spaced-repetition scheduler
│   ├── content-exam1.js       window.COURSE for exam 1
│   ├── content-exam2.js       window.COURSE for exam 2
│   └── content-exam3.js       window.COURSE for exam 3
├── images/ img/ textbook_images/   Assets
├── minisearch.min.js          Search lib (textbook)
├── _headers                   Cloudflare caching rules
└── _redirects                 Cloudflare redirects
```

## To edit content

- **Exam N content** → edit `public/js/content-examN.js` only. Each file exports `window.COURSE = { chapters:[…], flashcards:[…], test:[…] }`. Shell HTML + renderer don't need to change.
- **Visual style** → `public/css/esg.css` (all review pages share it). Themes via `html[data-theme="dark|paper|terminal"]`.
- **Mode behavior / rendering / flashcard scheduling** → `public/js/esg-ui.js` (renderer) + `public/js/esg-db.js` (spaced-rep).
- **Lecture / textbook / visuals** → standalone pages; edit directly.

## To deploy

```bash
./deploy.sh "commit message"     # commits to GitHub master + wrangler deploys to Pages main branch
```

Or the raw wrangler command:
```bash
npx wrangler pages deploy public --project-name=evolution-study-guide --branch=main --commit-dirty=true
```

## Backups

Pre-handoff originals in `_backups/pre-handoff/`. Older one-off backups in `_backups/older/`. Ignore unless you need to diff.

## Build-time / one-off scripts (root)

`build-new.js`, `gen_exam3_fc.py`, `download_fc_images.py`, `fix_gaps.py`, `audit_coverage.py` — all one-off generators; results already baked into `public/js/content-exam*.js`. Don't run unless regenerating content.
