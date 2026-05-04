/* ============================================================
   EVOLUTION GLOBAL SEARCH WIDGET
   Always-visible launcher chip + modal palette.
   Indexes the current page synchronously, then lazy-fetches
   every other page and adds chapters / sections / qcards /
   headings / figures (figcaption + img alt) to the index.
   Bindings: Ctrl+F · Cmd+K (if not already taken) · "/"
   ============================================================ */
(function () {
  if (window.__BSEARCH_WIDGET) return;
  window.__BSEARCH_WIDGET = true;

  const PAGES = [
    { path: 'index.html',             label: 'Study Guide' },
    { path: 'mastery.html',           label: 'Mastery' },
    { path: 'match.html',             label: 'Match' },
    { path: 'cheatsheet.html',        label: 'Cheat Sheet' },
    { path: 'guides.html',            label: 'Guides Hub' },
    { path: 'study-guide.html',       label: 'Cumulative Guide' },
    { path: 'study-guide-exam1.html', label: 'Exam 1 Guide' },
    { path: 'study-guide-exam2.html', label: 'Exam 2 Guide' },
    { path: 'study-guide-exam3.html', label: 'Exam 3 Guide' },
  ];

  const CACHE_KEY = 'evol-search.allIdx.v1';
  const CACHE_TTL = 1000 * 60 * 60 * 24 * 7; // 7 days

  /* ---------- helpers ---------- */
  const stripHtml = h => (h || '').replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/gi, ' ').replace(/\s+/g, ' ').trim();
  const esc = s => (s || '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const norm = s => (s || '').toLowerCase().replace(/\s+/g, ' ').trim();
  const currentPage = () => {
    const p = (location.pathname.split('/').pop() || '').toLowerCase();
    if (!p) return 'index.html';
    if (p.endsWith('.html')) return p;
    const withExt = p + '.html';
    if (PAGES.some(x => x.path === withExt)) return withExt;
    return 'index.html';
  };

  function assignSyntheticIds(doc) {
    const counts = { h1: 0, h2: 0, h3: 0, fig: 0, qc: 0, chapter: 0, section: 0, lec: 0, sec: 0, lesson: 0, deck: 0 };
    function tag(el, kind) {
      if (el.id) return el.id;
      counts[kind] = (counts[kind] || 0) + 1;
      const id = 'es-' + kind + '-' + counts[kind];
      el.id = id;
      return id;
    }
    return { tag, counts };
  }

  function indexDoc(doc, pagePath, pageLabel) {
    const out = [];
    const { tag } = assignSyntheticIds(doc);

    // Top-level page entry
    const pageTitle = (doc.querySelector('title')?.textContent || pageLabel).replace(/\s+/g, ' ').trim();
    const pageHero = stripHtml(doc.querySelector('.hero-title, h1')?.innerHTML || '');
    out.push({ kind: 'page', tag: 'Page', title: pageLabel, body: pageHero || pageTitle, path: pagePath, page: pageLabel, id: '' });

    // Lectures (index.html div.chapter id="L01"…)
    doc.querySelectorAll('.chapter').forEach(ch => {
      const t = ch.querySelector('.chapter-title, h2');
      const num = ch.querySelector('.chapter-num');
      if (!t) return;
      out.push({
        kind: 'chapter', tag: (num?.textContent || '').trim() || ch.id || 'Lec',
        title: stripHtml(t.innerHTML), path: pagePath, page: pageLabel,
        id: ch.id || tag(ch, 'chapter')
      });
    });
    doc.querySelectorAll('.section, .subsection').forEach(sec => {
      const t = sec.querySelector('.section-title, h3, h4');
      const num = sec.querySelector('.section-num');
      if (!t) return;
      out.push({
        kind: 'section', tag: (num?.textContent || '').trim() || sec.id || '§',
        title: stripHtml(t.innerHTML), path: pagePath, page: pageLabel,
        id: sec.id || tag(sec, 'section')
      });
    });
    doc.querySelectorAll('article.qcard').forEach(qc => {
      const q = qc.querySelector('.qcard-q'); if (!q) return;
      const idTag = qc.querySelector('.qcard-id')?.textContent.trim() || qc.id || 'Q';
      const qt = stripHtml(q.innerHTML);
      const choices = [...qc.querySelectorAll('.choice-text')].map(c => stripHtml(c.innerHTML)).join(' · ');
      const why = stripHtml(qc.querySelector('.explain')?.innerHTML || '');
      out.push({
        kind: 'quiz', tag: idTag,
        title: qt.slice(0, 110) + (qt.length > 110 ? '…' : ''),
        body: (qt + ' ' + choices + ' ' + why).slice(0, 400),
        path: pagePath, page: pageLabel,
        id: qc.id || tag(qc, 'qc')
      });
    });

    // Cheatsheet / study-guide structure (.lec, .sec)
    doc.querySelectorAll('.lec, .sec').forEach(el => {
      const h = el.querySelector('h2, h3, h4'); if (!h) return;
      out.push({
        kind: 'section', tag: el.classList.contains('lec') ? 'Lec' : '§',
        title: stripHtml(h.innerHTML), path: pagePath, page: pageLabel,
        id: el.id || tag(el, el.classList.contains('lec') ? 'lec' : 'sec')
      });
    });

    // Mastery deck cards
    doc.querySelectorAll('.deck-card, [data-deck]').forEach(d => {
      const n = d.querySelector('.deck-name, .deck-title');
      const t = n ? stripHtml(n.innerHTML) : (d.dataset.deck || '');
      if (!t) return;
      out.push({
        kind: 'deck', tag: 'Deck',
        title: t, path: pagePath, page: pageLabel,
        id: d.id || tag(d, 'deck')
      });
    });

    // Generic top-level headings
    const skipInside = el => el.closest('.tb, .toolbar, .findbar, .chrome, nav, header, .help-panel, .search-panel');
    doc.querySelectorAll('h2, h3').forEach(h => {
      if (skipInside(h)) return;
      if (h.closest('.chapter, .section, .subsection, .lec, .sec, article.lesson, article.qcard')) return;
      const txt = stripHtml(h.innerHTML); if (!txt || txt.length < 2) return;
      const kind = h.tagName === 'H2' ? 'h2' : 'h3';
      out.push({
        kind: 'heading', tag: h.tagName,
        title: txt, path: pagePath, page: pageLabel,
        id: h.id || tag(h, kind)
      });
    });

    function harvestContext(el) {
      let heading = '';
      let qaText = '';
      let p = el.previousElementSibling;
      let safety = 12;
      while (p && safety-- > 0) {
        if (/^H[1-6]$/.test(p.tagName)) { heading = stripHtml(p.innerHTML); break; }
        if (p.classList?.contains('a')) qaText = stripHtml(p.innerHTML) + (qaText ? ' · ' + qaText : '');
        if (p.classList?.contains('q') && !qaText) qaText = stripHtml(p.innerHTML);
        p = p.previousElementSibling;
      }
      if (!heading) {
        const par = el.closest('.section, .chapter, .subsection, .lec, .sec, article.lesson');
        if (par) {
          const h = par.querySelector('.section-title, .chapter-title, h2, h3');
          if (h) heading = stripHtml(h.innerHTML);
        }
      }
      return { heading, qaText };
    }

    // Figures
    doc.querySelectorAll('figure').forEach(f => {
      if (skipInside(f)) return;
      const cap = f.querySelector('figcaption');
      const img = f.querySelector('img');
      const capText = cap ? stripHtml(cap.innerHTML) : '';
      const altText = img ? (img.getAttribute('alt') || '').trim() : '';
      const title = altText || capText.split(/[.·—]/)[0].trim() || 'Diagram';
      if (!title) return;
      const { heading, qaText } = harvestContext(f);
      const lecMatch = capText.match(/Lecture\s+(\d+[A-Z]?)/i);
      const lecTag = lecMatch ? `L${lecMatch[1]} · ` : '';
      const body = (capText + (qaText ? ' — ' + qaText : '') + (altText && !capText.includes(altText) ? ' [' + altText + ']' : '')).trim();
      out.push({
        kind: 'figure', tag: lecTag ? lecTag.replace(' · ', '') : 'Figure',
        title: title.slice(0, 110),
        body: body.slice(0, 1200),
        ctx: heading || pageLabel,
        path: pagePath, page: pageLabel,
        id: f.id || tag(f, 'fig')
      });
    });

    // SVG diagrams
    doc.querySelectorAll('.diagram').forEach(d => {
      if (skipInside(d)) return;
      const svg = d.querySelector('svg');
      if (!svg) return;
      const texts = [...svg.querySelectorAll('text')];
      if (!texts.length) return;
      const titleEl = texts.find(t => parseFloat(t.getAttribute('font-weight') || 0) >= 600 || (t.getAttribute('letter-spacing') || '')) || texts[0];
      const titleRaw = titleEl.textContent.trim();
      const allLabels = texts.map(t => t.textContent.trim()).filter(Boolean);
      const { heading, qaText } = harvestContext(d);
      let prose = '';
      const proseBlock = d.closest('.prose');
      if (proseBlock) {
        const pars = [...proseBlock.querySelectorAll(':scope > p, :scope > .subhead, :scope > .callout')];
        prose = pars.slice(-3).map(p => stripHtml(p.innerHTML)).join(' · ');
      }
      const body = (allLabels.join(' · ') + (prose ? ' — ' + prose : '') + (qaText ? ' — ' + qaText : '')).trim();
      out.push({
        kind: 'figure', tag: 'SVG',
        title: titleRaw.slice(0, 110) || (heading + ' diagram').slice(0, 110),
        body: body.slice(0, 1400),
        ctx: heading || pageLabel,
        path: pagePath, page: pageLabel,
        id: d.id || tag(d, 'fig')
      });
    });

    // Loose images with alt
    doc.querySelectorAll('img[alt]').forEach(img => {
      if (img.closest('figure')) return;
      if (skipInside(img)) return;
      const alt = (img.getAttribute('alt') || '').trim();
      if (!alt || alt.length < 3) return;
      const { heading } = harvestContext(img);
      out.push({
        kind: 'figure', tag: 'Image',
        title: alt.slice(0, 90), body: alt,
        ctx: heading || pageLabel,
        path: pagePath, page: pageLabel,
        id: img.id || tag(img, 'fig')
      });
    });

    return out;
  }

  let LOCAL_INDEX = [];
  let CROSS_INDEX = [];
  let crossLoaded = false;
  let crossLoading = null;
  let DEFS = [];
  let defsLoading = null;
  let MASTERY_DEFS = [];
  let masteryLoading = null;

  /* Load flashcard term/def pairs (lazily fetches content/flashcards.js when not present). */
  function loadDefinitions() {
    if (DEFS.length || defsLoading) return defsLoading || Promise.resolve(DEFS);
    if (window.FLASHCARD_DECKS && Object.keys(window.FLASHCARD_DECKS).length) {
      DEFS = collectDefs(window.FLASHCARD_DECKS);
      return Promise.resolve(DEFS);
    }
    defsLoading = new Promise(resolve => {
      const s = document.createElement('script');
      s.src = 'content/flashcards.js';
      s.onload = () => {
        DEFS = collectDefs(window.FLASHCARD_DECKS || {});
        resolve(DEFS);
      };
      s.onerror = () => { defsLoading = null; resolve([]); };
      document.head.appendChild(s);
    });
    return defsLoading;
  }
  function collectDefs(decks) {
    const out = [];
    for (const [deckKey, deck] of Object.entries(decks)) {
      if (!Array.isArray(deck)) continue;
      for (const card of deck) {
        if (!card?.term || !card?.def) continue;
        const term = stripHtml(card.term).trim();
        if (!term) continue;
        out.push({
          term,
          termNorm: norm(term),
          def: card.def,
          defText: stripHtml(card.def),
          ctx: stripHtml(card.ctx || ''),
          deckKey,
          source: 'flashcards'
        });
      }
    }
    return out;
  }

  /* Load mastery cards (lazily fetches mastery JSON files via mastery-decks.js). */
  function loadMasteryDefs() {
    if (MASTERY_DEFS.length || masteryLoading) return masteryLoading || Promise.resolve(MASTERY_DEFS);
    if (window.MASTERY_DECKS && Object.keys(window.MASTERY_DECKS).length) {
      MASTERY_DEFS = collectMastery(window.MASTERY_DECKS);
      return Promise.resolve(MASTERY_DEFS);
    }
    if (window.MASTERY_READY && typeof window.MASTERY_READY.then === 'function') {
      masteryLoading = window.MASTERY_READY.then(() => {
        MASTERY_DEFS = collectMastery(window.MASTERY_DECKS || {});
        return MASTERY_DEFS;
      });
      return masteryLoading;
    }
    // Need to load mastery-decks.js first
    masteryLoading = new Promise(resolve => {
      const s = document.createElement('script');
      s.src = 'content/mastery-decks.js';
      s.onload = () => {
        const ready = window.MASTERY_READY || Promise.resolve();
        ready.then(() => {
          MASTERY_DEFS = collectMastery(window.MASTERY_DECKS || {});
          resolve(MASTERY_DEFS);
        });
      };
      s.onerror = () => { masteryLoading = null; resolve([]); };
      document.head.appendChild(s);
    });
    return masteryLoading;
  }
  function collectMastery(decks) {
    const out = [];
    for (const [deckId, deck] of Object.entries(decks)) {
      if (!deck?.cards) continue;
      const label = deck.label || deckId;
      for (const c of deck.cards) {
        if (!c?.term || !c?.definition) continue;
        out.push({
          term: c.term,
          termNorm: norm(c.term),
          def: c.definition,
          defText: c.definition,
          ctx: (c.sourceTag || '') + ' · ' + label,
          deckKey: deckId,
          source: 'mastery'
        });
      }
    }
    return out;
  }

  function findDefs(q) {
    const all = DEFS.concat(MASTERY_DEFS);
    if (!all.length) return [];
    const qn = norm(q);
    if (!qn) return [];
    const scored = [];
    for (const d of all) {
      let s = 0;
      if (d.termNorm === qn) s = 1000;
      else if (d.termNorm.split(/[^a-z0-9]+/).includes(qn)) s = 500;
      else if (d.termNorm.startsWith(qn)) s = 300;
      else if (d.termNorm.includes(qn)) s = 100 - (d.termNorm.length - qn.length);
      else if (norm(d.defText.slice(0, 200)).includes(qn)) s = 20;
      if (s > 0) scored.push({ d, s });
    }
    scored.sort((a, b) => b.s - a.s);
    return scored.slice(0, 4).map(x => x.d);
  }

  function buildLocalIndex() {
    LOCAL_INDEX = indexDoc(document, currentPage(), pageLabelFor(currentPage()));
  }
  function pageLabelFor(p) {
    return PAGES.find(x => x.path === p)?.label || p;
  }

  async function loadCrossIndex() {
    if (crossLoaded) return CROSS_INDEX;
    if (crossLoading) return crossLoading;
    const here = currentPage();
    try {
      const cached = JSON.parse(localStorage.getItem(CACHE_KEY) || 'null');
      if (cached && (Date.now() - cached.t) < CACHE_TTL && Array.isArray(cached.idx)) {
        CROSS_INDEX = cached.idx.filter(x => x.path !== here);
        crossLoaded = true;
        return CROSS_INDEX;
      }
    } catch (_) { }

    crossLoading = (async () => {
      const tasks = PAGES.filter(p => p.path !== here).map(async p => {
        try {
          const r = await fetch(p.path, { credentials: 'same-origin' });
          if (!r.ok) return [];
          const html = await r.text();
          const doc = new DOMParser().parseFromString(html, 'text/html');
          return indexDoc(doc, p.path, p.label);
        } catch (e) {
          console.warn('[esearch] failed to fetch', p.path, e);
          return [];
        }
      });
      const all = await Promise.all(tasks);
      CROSS_INDEX = all.flat();
      crossLoaded = true;
      try {
        const allIdx = LOCAL_INDEX.concat(CROSS_INDEX);
        localStorage.setItem(CACHE_KEY, JSON.stringify({ t: Date.now(), idx: allIdx }));
      } catch (_) { }
      return CROSS_INDEX;
    })();
    return crossLoading;
  }

  function score(item, terms) {
    if (!terms.length) return 0;
    const hay = norm((item.title || '') + ' ' + (item.body || '') + ' ' + (item.ctx || '') + ' ' + (item.tag || '') + ' ' + (item.page || ''));
    const title = norm(item.title || '');
    let s = 0;
    for (const t of terms) {
      if (!t) continue;
      if (!hay.includes(t)) return -1;
      s += 8;
      if (title.includes(t)) s += 16;
      if (title.startsWith(t)) s += 24;
      if (new RegExp('\\b' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b').test(hay)) s += 6;
    }
    const kindBoost = { page: 8, chapter: 6, section: 5, heading: 4, figure: 5, deck: 3, quiz: 2 }[item.kind] || 0;
    s += kindBoost;
    if (item.path === currentPage()) s += 3;
    return s;
  }

  function highlight(text, terms) {
    let out = esc(text || '');
    for (const t of terms) {
      if (!t) continue;
      const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
      out = out.replace(re, '<mark>$1</mark>');
    }
    return out;
  }

  const STYLE = `
  .esw-launcher{
    position:fixed;top:14px;right:14px;z-index:99998;
    display:inline-flex;align-items:center;gap:6px;
    background:#1a1d24;color:#e6dfd0;border:1px solid #2e333d;
    border-radius:999px;padding:8px 14px;
    font:600 12px/1 'Inter',system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;
    cursor:pointer;box-shadow:0 6px 18px rgba(0,0,0,.35);
    transition:transform .12s, border-color .12s, box-shadow .12s;
  }
  .esw-launcher:hover{ transform:translateY(-1px); border-color:#c89b2e; box-shadow:0 8px 22px rgba(200,155,46,.25); }
  .esw-launcher svg{ width:13px;height:13px;stroke:#c89b2e;stroke-width:2;fill:none; }
  .esw-launcher kbd{
    background:#0c0e12;color:#a59a83;border:1px solid #2e333d;border-radius:4px;
    padding:1px 5px;font:600 10px/1 'JetBrains Mono',monospace;
  }
  body.esw-on .esw-launcher{ display:none; }
  @media (max-width:560px){ .esw-launcher .esw-lbl{display:none} .esw-launcher{padding:8px 10px} }

  .esw-scrim{
    position:fixed;top:14px;right:14px;z-index:99999;display:none;
    pointer-events:none;
  }
  body.esw-on .esw-scrim{ display:block; }
  .esw-panel{
    pointer-events:auto;
    width:min(440px, calc(100vw - 28px));
    max-height:min(72vh, 720px);
    background:#14171d;border:1px solid #2e333d;border-radius:14px;
    box-shadow:0 24px 80px rgba(0,0,0,.55), 0 4px 12px rgba(0,0,0,.35);
    display:flex;flex-direction:column;overflow:hidden;
    color:#e6dfd0;font-family:'Inter',system-ui,sans-serif;
    resize:both;min-width:320px;min-height:240px;
  }
  body.esw-on{ scroll-padding-top:88px; }
  @media (max-width:560px){
    .esw-scrim{ top:auto;bottom:14px;right:14px;left:14px; }
    .esw-panel{ width:auto;max-height:60vh;resize:none; }
  }
  .esw-close, .esw-mintoggle{
    background:transparent;border:0;color:#a59a83;cursor:pointer;
    width:30px;height:30px;border-radius:6px;display:inline-flex;align-items:center;justify-content:center;
  }
  .esw-close:hover, .esw-mintoggle:hover{ color:#f1d278;background:#1a1d24; }
  .esw-close svg, .esw-mintoggle svg{ width:14px;height:14px;stroke:currentColor;stroke-width:2.2;fill:none; }
  .esw-head{ display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid #22262f; }
  .esw-head svg{ width:18px;height:18px;stroke:#c89b2e;stroke-width:2;fill:none; }
  .esw-input{
    flex:1;background:transparent;border:0;outline:0;color:#f1d278;
    font:500 16px/1.3 'Inter',system-ui,sans-serif;letter-spacing:.01em;
  }
  .esw-input::placeholder{ color:#6b6353; }
  .esw-results{ flex:1;overflow-y:auto;padding:6px 0; }
  .esw-results::-webkit-scrollbar{ width:8px; }
  .esw-results::-webkit-scrollbar-thumb{ background:#2e333d;border-radius:4px; }
  .esw-grp{ font:700 10px/1 'Inter',system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#6b6353;padding:14px 18px 6px; }
  .esw-item{
    display:flex;align-items:flex-start;gap:10px;padding:10px 18px;border-left:2px solid transparent;
    cursor:pointer;color:#e6dfd0;text-decoration:none;font-size:13px;line-height:1.4;
  }
  .esw-item.active, .esw-item:hover{ background:#1a1d24;border-left-color:#c89b2e; }
  .esw-tag{
    flex-shrink:0;font:700 10px/1 'JetBrains Mono',monospace;
    background:#0c0e12;color:#c89b2e;border:1px solid #2e333d;border-radius:4px;padding:4px 7px;
    min-width:54px;text-align:center;
  }
  .esw-item[data-kind="page"] .esw-tag{ background:#c89b2e;color:#0c0e12;border-color:#c89b2e; }
  .esw-mid{ flex:1;min-width:0; }
  .esw-title{ color:#e6dfd0;font-weight:600;font-size:13.5px;word-break:break-word; }
  .esw-sub{ color:#a59a83;font-size:11.5px;margin-top:2px; }
  .esw-body{ color:#c9c0ad;font-size:12px;line-height:1.45;margin-top:5px;
    display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden; }
  .esw-body-fig{ display:block;max-height:180px;overflow-y:auto;
    border-left:2px solid rgba(200,155,46,.35);padding:4px 8px;background:rgba(200,155,46,.04);border-radius:0 4px 4px 0; }
  body.day-mode .esw-body{ color:#3a342a; }
  .esw-page{ font:600 9.5px/1 'Inter',system-ui,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#7a8fa8;margin-left:6px; }
  .esw-item mark{ background:rgba(200,155,46,.22);color:#f1d278;padding:0 1px;border-radius:2px; }
  .esw-empty{ padding:24px 18px;color:#a59a83;font-size:13px;text-align:center;line-height:1.6; }
  .esw-grp-def{ color:#c89b2e !important; }
  .esw-defcard{
    margin:0 14px 10px;padding:12px 14px;
    background:linear-gradient(180deg,rgba(200,155,46,.10) 0%,rgba(200,155,46,.04) 100%);
    border:1px solid rgba(200,155,46,.42);border-left:3px solid #c89b2e;border-radius:8px;
  }
  .esw-deftitle{ font:700 14px/1.3 'Inter',system-ui,sans-serif;color:#f1d278;margin-bottom:6px; }
  .esw-defctx{ font:600 10.5px/1 'Inter',system-ui,sans-serif;color:#a59a83;margin-left:8px;letter-spacing:.06em;text-transform:uppercase; }
  .esw-defbody{ color:#d6cdb8;font-size:12.5px;line-height:1.55;max-height:260px;overflow-y:auto; }
  .esw-defbody p{ margin:4px 0; }
  .esw-defbody ul{ margin:4px 0 4px 18px;padding:0; }
  .esw-defbody li{ margin:2px 0; }
  .esw-defbody b, .esw-defbody strong{ color:#f1d278;font-weight:700; }
  .esw-defbody i, .esw-defbody em{ color:#cfc4ab; }
  .esw-foot{
    display:flex;justify-content:space-between;align-items:center;padding:8px 14px;
    border-top:1px solid #22262f;font:500 11px/1 'Inter',system-ui,sans-serif;color:#6b6353;
  }
  .esw-foot kbd{ background:#0c0e12;border:1px solid #2e333d;border-radius:3px;padding:2px 5px;font:600 10px/1 'JetBrains Mono',monospace;color:#a59a83;margin:0 2px; }
  .esw-flash{
    animation:eswFlash 2.4s ease-out 1;
    scroll-margin-top:120px;
    scroll-margin-bottom:80px;
  }
  @keyframes eswFlash{
    0%{ box-shadow:0 0 0 4px rgba(200,155,46,.75),0 0 32px rgba(200,155,46,.55); }
    100%{ box-shadow:0 0 0 0 rgba(200,155,46,0); }
  }
  .esw-panel.esw-min .esw-results,
  .esw-panel.esw-min .esw-foot{ display:none; }
  .esw-panel.esw-min{ resize:none;min-height:0;height:auto; }
  /* Day-mode adjustments */
  body.day-mode .esw-launcher{ background:#fff;color:#3a2e15;border-color:#d4cdb8; }
  body.day-mode .esw-launcher kbd{ background:#f5f1e8;color:#7a7158;border-color:#d4cdb8; }
  body.day-mode .esw-panel{ background:#fff;color:#1a1814;border-color:#d4cdb8; }
  body.day-mode .esw-head{ border-bottom-color:#eae4d5; }
  body.day-mode .esw-input{ color:#6b4a0a; }
  body.day-mode .esw-input::placeholder{ color:#a89f85; }
  body.day-mode .esw-tag{ background:#f5e6c2;color:#6b4a0a;border-color:#d4cdb8; }
  body.day-mode .esw-item{ color:#1a1814; }
  body.day-mode .esw-item.active, body.day-mode .esw-item:hover{ background:#fdf8eb;border-left-color:#c89b2e; }
  body.day-mode .esw-title{ color:#1a1814; }
  body.day-mode .esw-sub{ color:#5a503e; }
  body.day-mode .esw-foot{ color:#7a7158;border-top-color:#eae4d5; }
  body.day-mode .esw-defcard{ background:linear-gradient(180deg,rgba(200,155,46,.16) 0%,rgba(200,155,46,.06) 100%);border-color:#c89b2e; }
  body.day-mode .esw-deftitle{ color:#6b4a0a; }
  body.day-mode .esw-defbody{ color:#3a342a; }
  body.day-mode .esw-defbody b, body.day-mode .esw-defbody strong{ color:#6b4a0a; }
  `;

  function injectUI() {
    const s = document.createElement('style');
    s.id = 'esw-style';
    s.textContent = STYLE;
    document.head.appendChild(s);

    const launcher = document.createElement('button');
    launcher.className = 'esw-launcher';
    launcher.id = 'eswLauncher';
    launcher.type = 'button';
    launcher.title = 'Search across all pages (Ctrl+F · ⌘K · /)';
    launcher.innerHTML = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg><span class="esw-lbl">Search</span><kbd>Ctrl+F</kbd>';
    document.body.appendChild(launcher);

    const scrim = document.createElement('div');
    scrim.className = 'esw-scrim';
    scrim.id = 'eswScrim';
    scrim.innerHTML = `
      <div class="esw-panel" role="dialog" aria-label="Site search">
        <div class="esw-head">
          <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
          <input id="eswInput" class="esw-input" type="text" placeholder="Search lectures, sections, diagrams, cards…" autocomplete="off" spellcheck="false">
          <button class="esw-mintoggle" id="eswMin" type="button" aria-label="Minimize" title="Minimize / restore results">
            <svg id="eswMinIcon" viewBox="0 0 24 24"><path d="M5 12h14"/></svg>
          </button>
          <button class="esw-close" id="eswClose" type="button" aria-label="Close (Esc)" title="Close (Esc)">
            <svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>
          </button>
        </div>
        <div class="esw-results" id="eswResults" role="listbox"></div>
        <div class="esw-foot">
          <span><kbd>↑</kbd><kbd>↓</kbd> nav · <kbd>↵</kbd> jump · <kbd>esc</kbd> close</span>
          <span id="eswStats">—</span>
        </div>
      </div>`;
    document.body.appendChild(scrim);
  }

  let activeIdx = 0;
  let lastItems = [];

  function render(q) {
    const terms = q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    const idx = LOCAL_INDEX.concat(CROSS_INDEX);

    if (!terms.length) {
      const sample = [];
      const seen = new Set();
      for (const p of PAGES) {
        const pageEntry = idx.find(x => x.path === p.path && x.kind === 'page');
        if (pageEntry && !seen.has(p.path)) { sample.push(pageEntry); seen.add(p.path); }
      }
      for (const p of PAGES) {
        if (seen.has(p.path)) continue;
        sample.push({ kind: 'page', tag: 'Page', title: p.label, body: '', path: p.path, page: p.label, id: '' });
        seen.add(p.path);
      }
      lastItems = sample;
      renderList(sample, [], `${idx.length} items indexed${crossLoaded ? '' : ' · loading other pages…'}`);
      return;
    }

    const scored = [];
    for (const item of idx) {
      const sc = score(item, terms);
      if (sc >= 0) scored.push({ item, sc });
    }
    scored.sort((a, b) => b.sc - a.sc);
    const top = scored.slice(0, 60).map(x => x.item);
    const defs = findDefs(q);
    lastItems = top;
    renderList(top, terms, `${top.length} of ${idx.length} · "${q.trim()}"${crossLoaded ? '' : ' · still indexing'}`, defs);
  }

  function renderList(items, terms, stats, defs) {
    activeIdx = 0;
    const results = document.getElementById('eswResults');
    const statsEl = document.getElementById('eswStats');
    statsEl.textContent = stats;
    if (!items.length && !(defs && defs.length)) {
      results.innerHTML = '<div class="esw-empty">No matches. Try a shorter query, a different word, or wait for the cross-page index to finish loading.</div>';
      return;
    }
    let defsHtml = '';
    if (defs && defs.length) {
      defsHtml += '<div class="esw-grp esw-grp-def">Definition · ' + defs.length + '</div>';
      for (const d of defs) {
        defsHtml += `<div class="esw-defcard">
          <div class="esw-deftitle">${highlight(d.term, terms)}${d.ctx ? `<span class="esw-defctx">· ${esc(d.ctx)}</span>` : ''}</div>
          <div class="esw-defbody">${d.def}</div>
        </div>`;
      }
    }
    const groups = { page: [], chapter: [], section: [], heading: [], figure: [], deck: [], quiz: [] };
    items.forEach(x => (groups[x.kind] || (groups[x.kind] = [])).push(x));
    const groupTitles = { page: 'Pages', chapter: 'Lectures', section: 'Sections', heading: 'Headings', figure: 'Diagrams & figures', deck: 'Decks', quiz: 'Questions' };
    const order = ['page', 'chapter', 'section', 'heading', 'figure', 'deck', 'quiz'];
    let html = '';
    let flat = 0;
    for (const k of order) {
      const arr = groups[k] || []; if (!arr.length) continue;
      html += `<div class="esw-grp">${groupTitles[k] || k} · ${arr.length}</div>`;
      for (const it of arr) {
        const subParts = [];
        if (it.ctx) subParts.push(esc(it.ctx));
        if (it.tag && it.kind !== 'figure' && it.kind !== 'deck') subParts.push(esc(it.tag));
        const subText = subParts.join(' · ');
        const showBody = it.body && (it.kind === 'figure' || it.kind === 'quiz' || terms.some(t => norm(it.body).includes(t)));
        const bodyClass = it.kind === 'figure' ? 'esw-body esw-body-fig' : 'esw-body';
        const bodyMax = it.kind === 'figure' ? 900 : 280;
        const bodyTrim = it.body ? it.body.slice(0, bodyMax) : '';
        const bodyText = showBody && bodyTrim
          ? `<div class="${bodyClass}">${highlight(bodyTrim, terms)}${it.body.length > bodyMax ? '…' : ''}</div>`
          : '';
        html += `<a class="esw-item" data-idx="${flat}" data-path="${esc(it.path)}" data-id="${esc(it.id || '')}" data-kind="${it.kind}" href="${esc(it.path)}#${esc(it.id || '')}">
          <span class="esw-tag">${esc(it.tag || '')}</span>
          <span class="esw-mid">
            <div class="esw-title">${highlight(it.title || '', terms)}<span class="esw-page">· ${esc(it.page || '')}</span></div>
            ${subText ? `<div class="esw-sub">${subText}</div>` : ''}
            ${bodyText}
          </span>
        </a>`;
        flat++;
      }
    }
    results.innerHTML = defsHtml + html;
    const els = results.querySelectorAll('.esw-item');
    els.forEach(el => {
      el.addEventListener('mouseenter', () => {
        els.forEach(x => x.classList.remove('active'));
        el.classList.add('active');
        activeIdx = parseInt(el.dataset.idx, 10);
      });
      el.addEventListener('click', e => {
        e.preventDefault();
        choose(el);
      });
    });
    if (els[0]) els[0].classList.add('active');
  }

  function ensureVisible(target) {
    if (!target) return;
    let p = target;
    let safety = 30;
    while (p && p !== document.body && safety-- > 0) {
      if (p.tagName === 'DETAILS' && !p.open) p.open = true;
      if (p.style) {
        if (p.style.display === 'none') p.style.display = '';
        if (p.style.visibility === 'hidden') p.style.visibility = '';
      }
      if (p.classList?.contains('card')) {
        const body = p.querySelector(':scope > .card-body');
        if (body && getComputedStyle(body).display === 'none') {
          const header = p.querySelector(':scope > .card-header');
          if (header) header.click();
        }
      }
      if (p.classList?.contains('reveal') && !p.classList.contains('in-view')) {
        p.classList.add('in-view');
      }
      p = p.parentElement;
    }
    if (target.offsetParent === null) {
      if (typeof window.setMode === 'function') {
        try { window.setMode('study'); } catch (_) { }
      }
      const studyBtn = document.querySelector('[data-mode="study"]');
      if (studyBtn && !studyBtn.classList.contains('active')) {
        try { studyBtn.click(); } catch (_) { }
      }
    }
  }

  function setMinimized(on) {
    const panel = document.querySelector('.esw-panel');
    if (!panel) return;
    panel.classList.toggle('esw-min', !!on);
    const icon = document.getElementById('eswMinIcon');
    if (icon) {
      icon.innerHTML = on
        ? '<path d="M5 9l7 7 7-7"/>'
        : '<path d="M5 12h14"/>';
    }
    const btn = document.getElementById('eswMin');
    if (btn) btn.title = on ? 'Show results' : 'Minimize (results hidden, search stays)';
  }

  function choose(el) {
    const path = el.dataset.path;
    const id = el.dataset.id;
    const kind = el.dataset.kind;
    const here = currentPage();
    if (path === here) {
      if (kind === 'page' || !id) {
        setMinimized(true);
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      const target = document.getElementById(id);
      if (target) {
        ensureVisible(target);
        setMinimized(true);
        requestAnimationFrame(() => {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          target.classList.add('esw-flash');
          setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }), 220);
          setTimeout(() => target.classList.remove('esw-flash'), 2400);
        });
      } else {
        location.hash = id;
      }
    } else {
      location.href = path + (id ? '#' + id : '');
    }
  }

  function openWidget() {
    document.body.classList.add('esw-on');
    const inp = document.getElementById('eswInput');
    inp.value = '';
    render('');
    setTimeout(() => inp.focus(), 30);
    if (!crossLoaded) loadCrossIndex().then(() => render(document.getElementById('eswInput').value));
    if (!DEFS.length) loadDefinitions().then(() => render(document.getElementById('eswInput').value));
    if (!MASTERY_DEFS.length) loadMasteryDefs().then(() => render(document.getElementById('eswInput').value));
  }
  function closeWidget() { document.body.classList.remove('esw-on'); }

  function ready() {
    injectUI();
    buildLocalIndex();
    const tryHash = (hash) => {
      const idStr = hash.slice(1);
      if (!idStr) return;
      const t = document.getElementById(idStr);
      if (!t) return;
      setTimeout(() => {
        ensureVisible(t);
        requestAnimationFrame(() => {
          t.scrollIntoView({ behavior: 'smooth', block: 'start' });
          t.classList.add('esw-flash');
          setTimeout(() => t.scrollIntoView({ behavior: 'smooth', block: 'start' }), 240);
          setTimeout(() => t.classList.remove('esw-flash'), 2400);
        });
      }, 80);
    };
    if (location.hash) tryHash(location.hash);
    document.getElementById('eswLauncher').addEventListener('click', openWidget);
    document.getElementById('eswClose').addEventListener('click', closeWidget);
    document.getElementById('eswMin').addEventListener('click', () => {
      const panel = document.querySelector('.esw-panel');
      setMinimized(!panel.classList.contains('esw-min'));
    });
    const inp = document.getElementById('eswInput');
    inp.addEventListener('focus', () => setMinimized(false));
    inp.addEventListener('input', () => { setMinimized(false); render(inp.value); });

    document.addEventListener('keydown', e => {
      const isInput = ['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName) || e.target.isContentEditable;
      const ctrlF = (e.key === 'f' || e.key === 'F') && (e.ctrlKey || e.metaKey) && !e.shiftKey && !e.altKey;
      const slash = e.key === '/' && !isInput;
      const cmdK = (e.key === 'k' || e.key === 'K') && (e.ctrlKey || e.metaKey);
      const cmdKTakeOver = cmdK && !window.__BSEARCH_CMDK_TAKEN_BY_HOST;
      if (ctrlF || slash || cmdKTakeOver) {
        e.preventDefault();
        if (document.body.classList.contains('esw-on')) {
          inp.focus(); inp.select();
        } else {
          openWidget();
        }
        return;
      }
      if (!document.body.classList.contains('esw-on')) return;
      if (e.key === 'Escape') { e.preventDefault(); closeWidget(); return; }
      const items = document.querySelectorAll('#eswResults .esw-item');
      if (!items.length) return;
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        activeIdx = Math.min(items.length - 1, activeIdx + 1);
        items.forEach(x => x.classList.remove('active'));
        items[activeIdx].classList.add('active');
        items[activeIdx].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        activeIdx = Math.max(0, activeIdx - 1);
        items.forEach(x => x.classList.remove('active'));
        items[activeIdx].classList.add('active');
        items[activeIdx].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault();
        const el = items[activeIdx]; if (el) choose(el);
      }
    }, true);

    if ('requestIdleCallback' in window) {
      requestIdleCallback(loadCrossIndex, { timeout: 4000 });
      requestIdleCallback(loadDefinitions, { timeout: 6000 });
      requestIdleCallback(loadMasteryDefs, { timeout: 8000 });
    } else {
      setTimeout(loadCrossIndex, 1500);
      setTimeout(loadDefinitions, 2200);
      setTimeout(loadMasteryDefs, 3000);
    }

    if (currentPage() === 'index.html' && typeof window.openSearch === 'function') {
      window.__BSEARCH_CMDK_TAKEN_BY_HOST = true;
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready);
  else ready();
})();
