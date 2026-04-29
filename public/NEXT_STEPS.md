# Evolution Study Guide v2 — Where things stand

## What's done

- **Architecture**: cloned the biol3020-exam4 single-file SPA shell; CSS tokens (background `#0c0e12`, ink `#e6dfd0`, accent `#c89b2e`, Fraunces serif + Inter sans) all preserved.
- **Branding swap**: `BIOL 3020` → `BIOL 4230`, "Cellular Biology · Cooper & Adams" → "Evolution · Zimmer & Emlen", localStorage prefix `biol-` → `evol-` so this site does not collide with the cell-bio site in the same browser.
- **Cell-bio content stripped**: removed the four hardcoded chapter divs (ch14/18/19/20) — 535 KB of cell-bio prose, qcards, SVG diagrams, and table content gone.
- **Dynamic renderer**: Study mode now reads `window.MANUAL_LECTURE_GUIDES` and paints the chapter bar (`#chNav`), dashboard cards (`#ch-grid-final`), and full lecture articles (`#lectureHost`) from JSON.
- **Stim Mode is live**: 17 hand-authored questions (9 Exam 1, 4 Exam 2, 4 Exam 3) — setup chips render correct counts; clicking Start launches the runner with the real question stem; session state persists to `evol_stim_session`.
- **Course metadata**: 17 lectures (L01–L19, skipping L06 and L10 since L05 covers the combined "5,6" lecture and L10 is the online Dinosaurs quiz) mapped to Exam 1 / 2 / 3 / Cumulative.
- **Merge scripts**: `scripts-v2/merge-lecture-guides.py` and `scripts-v2/merge-stim-bank.py` regenerate the content bundles from the per-lecture JSON files. Run after every authoring batch.
- **Deploy script**: `public-v2/deploy.bat` set up to push to Cloudflare Pages project `evolution-study-guide`. Not run yet — the live site at https://evolution-study-guide.pages.dev still shows v1.

## What's authored (4 of 17 lectures)

| Lecture | Sections | Stim Qs |
|---|---|---|
| L01 — Intro | 3 (defining evolution / unifying theory / 4 mechanisms) | 4 |
| L04 — Hardy-Weinberg | 4 (allele freqs / equation / deviations / worked computation) | 5 |
| L09 — Coevolution | 5 (definition / arms races / mutualism / mimicry / geographic mosaic) | 4 |
| L15 — Phylogenetics | 4 (reading trees / synapomorphies / mono-para-poly / species concepts) | 4 |

Each lecture file lives at `public-v2/data/lecture-guides/L{NN}.json`; each stim file at `public-v2/data/stim-bank/L{NN}.json`. Schema matches biol3020-exam4 verbatim.

## What still needs authoring (the bulk of the work)

### Lecture guides — 13 lectures left

Exam 1 (4 lectures left): **L02** Evolutionary thinking · **L03** Genes and heritable variation · **L05** Quantitative genetics, selection, plasticity

Exam 2 (5 lectures left): **L07** Empirical studies of natural selection · **L08** Complex adaptations · **L11** Sex and sexual selection · **L12** Life history evolution · **L13** Evolution of social behavior

Exam 3 (5 lectures left): **L14** History of life · **L16** Species concepts and reproductive isolation · **L17** Biogeography, speciation, and extinction · **L18** Conservation and humans as selective force · **L19** Human evolution

### Stim bank — ~133 questions left to hit the planned 150 target

Current: 9 / 4 / 4 (Exam 1 / 2 / 3). Plan target: ~50 / 50 / 50.

Each question must be hand-written from the source materials per the user's quality bar. Schema constraints:
- MC: include `q`, `choices` (4), `correct` (0-3 index), `why`, `choice_why[]` (one per choice), `source` tag
- SA: include `q`, `rubric { total, criteria[] }`, `model_answer`, `source` tag
- Tag every question with `exam`, `lecture`, `section`, `topic`, `difficulty`, `points`

### Authoring workflow

1. Open the source: `Study Guide Exam {1,2,3} - Short.pdf` in Downloads + the matching PPTX (`Lecture #{N} ... .pptx`) + Zimmer & Emlen relevant chapter.
2. Edit (or create) `public-v2/data/lecture-guides/L{NN}.json` — see L01.json or L04.json as templates.
3. Edit (or create) `public-v2/data/stim-bank/L{NN}.json` with 8–12 questions per lecture.
4. Run from `evolution-study-guide/`:
   ```
   python scripts-v2/merge-lecture-guides.py
   python scripts-v2/merge-stim-bank.py
   ```
5. Reload the local preview (or run `deploy.bat`).

## Deferred to v2

- **Slide images** from the 18 PPTX lectures — extract via LibreOffice headless or `python-pptx` into `public-v2/slide-images/L{NN}-S{MM}-img{K}.png`, then add to `image_slides[]` arrays in the lecture-guides.
- **Flashcards mode** — currently stubbed (`content/flashcards.js` is empty). Author hand-curated cards (~10 per lecture) and add a `merge-flashcards.py` script.
- **Quiz mode** — currently stubbed; hard-questioned about whether to revive it given Stim mode covers the same ground better.
- **Comp / Ref modes** — placeholder banners visible; no content compiled yet.

## Cutover plan (when content is far enough along)

1. Final local verification on `http://localhost:4210` (or whatever `npx serve` port is assigned).
2. Move `public/` → `_archive/v1-esg-gold-design/`.
3. Rename `public-v2/` → `public/`.
4. From the new `public/` directory: `./deploy.bat` (or update `../deploy.sh` if the user prefers the existing GitHub-Actions flow).
5. Smoke-test https://evolution-study-guide.pages.dev in incognito.

## Known issues / open items

- The **Help panel** (`?` button) still references "Cumulative review across Exams 1–3 (Lectures 1–19)" — accurate enough for now but copy could be tightened.
- The **Search palette** (`⌘K`) is wired up but the search index is built off whatever lecture content is loaded; will improve as more lectures are authored.
- The **Tweaks panel** (gear icon) writes to `evol-tweaks` localStorage — no collisions, but the export-to-zip filename uses `evol4230-tweaks-{date}.zip` which is fine.
- **`content/study-content.js`** is a stub; if the original biol3020 had study-content rendering hooks that go beyond `MANUAL_LECTURE_GUIDES`, those won't fire.
