/* Inject the Cloze Mode toggle (button + CSS + JS) into all 4 study guides.
   Idempotent — re-running just replaces the previous block (delimited by markers). */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const FILES = [
  'study-guide-exam1.html',
  'study-guide-exam2.html',
  'study-guide-exam3.html',
  'study-guide.html', // cumulative final (added 2026-05-02 per audit Issue 3)
];

const BLOCK = `
<!-- ===== CLOZE MODE + TERM HOVER TOOLTIPS — auto-injected by scripts/inject-cloze-mode.js ===== -->
<!-- BEGIN CLOZE MODE -->
<style id="cloze-mode-styles">
  /* Floating toggle button (top-right, off-screen for print) */
  #clozeToggleBtn {
    position: fixed;
    top: 14px; right: 14px;
    z-index: 9999;
    background: #fff; color: #5b3a06;
    border: 1.5px solid #a8651a; border-radius: 22px;
    padding: 8px 16px; font-family: system-ui, -apple-system, sans-serif;
    font-size: 13px; font-weight: 700; cursor: pointer;
    box-shadow: 0 2px 12px rgba(0,0,0,0.12);
    user-select: none;
  }
  #clozeToggleBtn:hover { background: #fff4e2; }
  #clozeToggleBtn.cloze-on {
    background: #a8651a; color: #fff;
    border-color: #a8651a;
  }
  @media print { #clozeToggleBtn { display: none !important; } }

  /* Hover tooltip for bolded terms (works in both normal AND cloze mode) */
  #termTooltip {
    position: absolute;
    z-index: 10000;
    max-width: 360px;
    background: #1f1812;
    color: #fff8e7;
    border: 1px solid #a8651a;
    border-radius: 8px;
    padding: 10px 13px;
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 12.5px;
    line-height: 1.5;
    box-shadow: 0 6px 22px rgba(0,0,0,0.35);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.12s;
  }
  #termTooltip.visible { opacity: 1; pointer-events: auto; }
  #termTooltip .tt-term {
    display: block;
    color: #f5c264;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 4px;
    font-family: 'Fraunces', Georgia, serif;
  }
  #termTooltip .tt-term.hidden-term { color: #888; }
  #termTooltip .tt-def { color: #fff8e7; }
  #termTooltip .tt-source { display: block; font-size: 10.5px; color: #c89b2e; margin-top: 5px; font-style: italic; }
  @media print { #termTooltip { display: none !important; } }
  /* Hint that bolded terms are interactive */
  .doc b, .doc strong, [contenteditable] b, [contenteditable] strong {
    cursor: help;
  }

  /* Cloze blank — the redacted span. The original text is preserved in
     a data attribute and stripped of inner color/styling so the blank stands out. */
  .cloze-blank {
    display: inline-block;
    background: #f0e6d2;
    color: transparent;
    border-bottom: 2px solid #a8651a;
    border-radius: 3px;
    padding: 0 4px;
    margin: 0 1px;
    cursor: pointer;
    user-select: none;
    transition: background 0.15s, color 0.15s;
    min-width: 30px;
    text-align: center;
  }
  .cloze-blank::before {
    content: attr(data-blank-text);
    color: #a8651a;
    letter-spacing: 0;
  }
  .cloze-blank.revealed {
    background: #fff36b;
    color: #111;
    border-bottom-color: transparent;
    cursor: default;
    user-select: text;
  }
  .cloze-blank.revealed::before { content: ''; display: none; }
  /* Help banner shown briefly when cloze is turned on */
  #clozeHelp {
    position: fixed;
    top: 60px; right: 14px;
    z-index: 9998;
    background: #fff;
    border: 1px solid #d8d2c5;
    border-radius: 8px;
    padding: 12px 16px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.10);
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 12.5px;
    color: #3a2e15;
    max-width: 260px;
    line-height: 1.5;
    transition: opacity 0.4s;
  }
  #clozeHelp b { color: #a8651a; }
  #clozeHelp.hide { opacity: 0; pointer-events: none; }
</style>

<button id="clozeToggleBtn" type="button" title="Toggle Cloze Study Mode — hides bolded terms; click any blank to reveal">🎯 Cloze Mode</button>

<script>
(function () {
  // Storage key per study guide (each exam page has its own toggle state)
  const KEY = 'evolution-cloze-' + (document.title || location.pathname).replace(/\\W+/g, '-').slice(0, 40);
  const btn = document.getElementById('clozeToggleBtn');
  if (!btn) return;

  // Find the editable content container — it's #docArea, #doc, the .doc element,
  // or [contenteditable=true]. Falls back to <body>.
  function getContentRoot() {
    return document.getElementById('docArea')
        || document.getElementById('doc')
        || document.querySelector('.doc')
        || document.querySelector('[contenteditable="true"]')
        || document.body;
  }

  // Cloze candidates: <b> and <strong> elements with non-trivial text content.
  // Skip elements inside the toolbar, the cloze help banner, or this button itself.
  function getCandidates(root) {
    const skipParents = ['toolbar', 'clozeToggleBtn', 'clozeHelp', 'shortcutsBack',
                         'galleryBack', 'findBack', 'replaceBack'];
    const els = Array.from(root.querySelectorAll('b, strong'));
    return els.filter(el => {
      if (!el.textContent || el.textContent.trim().length < 1) return false;
      // Must not be inside any skip-parent
      for (let n = el.parentElement; n; n = n.parentElement) {
        if (n.id && skipParents.includes(n.id)) return false;
        if (n.classList && n.classList.contains('cloze-blank')) return false;
      }
      // Must not contain other block elements
      if (el.querySelector('p, div, ul, ol, table')) return false;
      return true;
    });
  }

  function applyCloze() {
    const root = getContentRoot();
    const candidates = getCandidates(root);
    candidates.forEach(el => {
      // Wrap the bold's text content in a cloze-blank span. Preserve original.
      const original = el.innerHTML;
      el.dataset.clozeOriginal = original;
      const text = el.textContent;
      // Use ___ length matching word count
      const blank = '_'.repeat(Math.min(20, Math.max(4, text.length)));
      el.innerHTML = '<span class="cloze-blank" data-blank-text="' + blank + '" data-revealed="0">' + escapeHtml(text) + '</span>';
    });
    // Wire click → reveal on each blank
    root.querySelectorAll('.cloze-blank').forEach(span => {
      span.addEventListener('click', revealBlank);
    });
  }

  function removeCloze() {
    const root = getContentRoot();
    root.querySelectorAll('b[data-cloze-original], strong[data-cloze-original]').forEach(el => {
      el.innerHTML = el.dataset.clozeOriginal;
      delete el.dataset.clozeOriginal;
    });
  }

  function revealBlank(e) {
    e.stopPropagation();
    const span = e.currentTarget;
    span.classList.add('revealed');
    span.dataset.revealed = '1';
  }

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function showHelp(text) {
    const id = 'clozeHelp';
    let el = document.getElementById(id);
    if (!el) {
      el = document.createElement('div');
      el.id = id;
      document.body.appendChild(el);
    }
    el.innerHTML = text;
    el.classList.remove('hide');
    setTimeout(() => el.classList.add('hide'), 4500);
  }

  function setMode(on) {
    if (on) {
      // Disable contenteditable so clicks don't insert cursors / change content
      const root = getContentRoot();
      root.dataset.clozeEditableWas = root.getAttribute('contenteditable') || '';
      root.setAttribute('contenteditable', 'false');
      applyCloze();
      btn.classList.add('cloze-on');
      btn.textContent = '🎯 Cloze Mode: ON';
      const count = root.querySelectorAll('.cloze-blank').length;
      showHelp('<b>Cloze Mode is ON</b> &mdash; ' + count + ' bolded terms are hidden. Click any blank to reveal it. Toggle off to restore.');
    } else {
      removeCloze();
      const root = getContentRoot();
      if (root.dataset.clozeEditableWas !== undefined) {
        root.setAttribute('contenteditable', root.dataset.clozeEditableWas || 'true');
        delete root.dataset.clozeEditableWas;
      }
      btn.classList.remove('cloze-on');
      btn.textContent = '🎯 Cloze Mode';
    }
    try { localStorage.setItem(KEY, on ? '1' : '0'); } catch (e) {}
  }

  btn.addEventListener('click', () => {
    const isOn = btn.classList.contains('cloze-on');
    setMode(!isOn);
  });

  // Restore previous state on load (defer so the doc is fully rendered)
  setTimeout(() => {
    try {
      if (localStorage.getItem(KEY) === '1') setMode(true);
    } catch (e) {}
    // Wire hover tooltips on every bolded term (independent of cloze mode)
    setupTermTooltips(getContentRoot());
  }, 200);

  // ---- Hover tooltip on every bolded term -----------------------------------
  // The tooltip extracts a contextual definition from the surrounding sentence:
  //   1) Find the parent block element (p, li, h2, etc.)
  //   2) Walk forward from the term to the next sentence-ending punctuation
  //      (. ; or em-dash) and use that as the hint
  //   3) If no good "after-term" context, fall back to the parent block text
  //      with the term itself stripped out
  function setupTermTooltips(root) {
    if (!root || root.dataset.tooltipsWired === '1') return;
    root.dataset.tooltipsWired = '1';
    let tipEl = document.getElementById('termTooltip');
    if (!tipEl) {
      tipEl = document.createElement('div');
      tipEl.id = 'termTooltip';
      tipEl.innerHTML = '<span class="tt-term"></span><span class="tt-def"></span><span class="tt-source"></span>';
      document.body.appendChild(tipEl);
    }
    // Use event delegation so we cover dynamic elements (e.g. cloze blanks)
    root.addEventListener('mouseover', (e) => {
      const t = e.target;
      const isBold = (t.tagName === 'B' || t.tagName === 'STRONG') && !t.querySelector('p, div, ul, ol');
      const isCloze = t.classList && t.classList.contains('cloze-blank');
      // A bold is "cloze-wrapped" when it contains a .cloze-blank child — meaning the
      // user is currently in cloze mode for this term. Treat it the same as cloze
      // to avoid leaking the answer when hovering the bold's outer box.
      const boldHasClozeChild = isBold && t.querySelector('.cloze-blank');
      if (!isBold && !isCloze) return;
      // For cloze blanks (or cloze-wrapped bolds), the term lives in the data-cloze-original
      const wrap = isCloze ? t.parentElement : (boldHasClozeChild ? t : null);
      const term = wrap ? (wrap.dataset?.clozeOriginal || wrap.textContent) : t.textContent;
      const hint = extractContextHint(t, term);
      const inClozeMode = btn.classList.contains('cloze-on');
      const treatAsCloze = (isCloze || boldHasClozeChild) && inClozeMode;
      tipEl.querySelector('.tt-term').className = 'tt-term' + (treatAsCloze ? ' hidden-term' : '');
      tipEl.querySelector('.tt-term').textContent = treatAsCloze ? '(answer hidden — guess first!)' : (term.replace(/<[^>]+>/g, '').trim().slice(0, 80));
      tipEl.querySelector('.tt-def').textContent = hint;
      tipEl.querySelector('.tt-source').textContent = 'From study guide context';
      // Position near the cursor
      const rect = t.getBoundingClientRect();
      const top = window.scrollY + rect.bottom + 6;
      let left = window.scrollX + rect.left;
      // Constrain to viewport (don't go off the right edge)
      const maxLeft = window.scrollX + window.innerWidth - 380;
      if (left > maxLeft) left = maxLeft;
      if (left < 8) left = 8;
      tipEl.style.top = top + 'px';
      tipEl.style.left = left + 'px';
      tipEl.classList.add('visible');
    });
    root.addEventListener('mouseout', (e) => {
      const t = e.target;
      const isBold = (t.tagName === 'B' || t.tagName === 'STRONG');
      const isCloze = t.classList && t.classList.contains('cloze-blank');
      if (!isBold && !isCloze) return;
      tipEl.classList.remove('visible');
    });
  }

  function extractContextHint(termEl, termText) {
    // Find the parent block element
    let block = termEl;
    for (let n = termEl; n && n !== document.body; n = n.parentElement) {
      const tag = n.tagName;
      if (tag === 'P' || tag === 'LI' || tag === 'H1' || tag === 'H2' || tag === 'H3' || tag === 'H4' || tag === 'TD' || tag === 'BLOCKQUOTE' || tag === 'DIV') {
        block = n; break;
      }
    }
    const fullText = (block.innerText || block.textContent || '').replace(/\\s+/g, ' ').trim();
    const cleanTerm = (termText || '').replace(/<[^>]+>/g, '').trim();
    if (!cleanTerm || !fullText) return 'No context found.';
    // Find the term in the block text (case-insensitive, first match)
    const lc = fullText.toLowerCase();
    const tlc = cleanTerm.toLowerCase();
    const idx = lc.indexOf(tlc);
    if (idx === -1) {
      // Fallback: return first ~140 chars of block, minus the term
      return fullText.replace(new RegExp(escapeRe(cleanTerm), 'gi'), '___').slice(0, 200);
    }
    // Extract the chunk AFTER the term — that's usually the definition
    const after = fullText.slice(idx + cleanTerm.length).trim();
    // Trim leading punctuation/whitespace, then take up to next sentence end
    const cleaned = after.replace(/^[\\s.,;:—–-]+/, '');
    const sentenceEnd = cleaned.search(/[.;](?:\\s|$)|—\\s+(?=[A-Z])/);
    let hint = sentenceEnd > 30 ? cleaned.slice(0, sentenceEnd + 1) : cleaned.slice(0, 200);
    if (hint.length < 25) {
      // Too short — try the chunk BEFORE the term as well
      const before = fullText.slice(0, idx).trim().slice(-180);
      hint = before + ' [' + cleanTerm + '] ' + cleaned.slice(0, 120);
    }
    return hint.replace(new RegExp(escapeRe(cleanTerm), 'gi'), '___').trim();
  }

  function escapeRe(s) { return s.replace(/[.*+?^\${}()|[\\]\\\\]/g, '\\\\$&'); }
})();
</script>
<!-- END CLOZE MODE -->
`;

const START = '<!-- BEGIN CLOZE MODE -->';
const END = '<!-- END CLOZE MODE -->';

let updated = 0;
for (const fname of FILES) {
  const filePath = path.join(ROOT, fname);
  let html = fs.readFileSync(filePath, 'utf8');
  // CRITICAL: use a function as the replacement so the BLOCK is treated as literal text.
  // Otherwise `$&`, `$1`, etc. inside the BLOCK string would be interpreted as regex
  // back-reference tokens by String.replace() and corrupt the output.
  const literalBlock = () => BLOCK.trim() + '\n';

  // First, aggressively strip ANY existing CLOZE MODE content (handles corrupted re-injects too):
  // remove from the FIRST `<!-- ===== CLOZE MODE` through the LAST `<!-- END CLOZE MODE -->`.
  const firstStartIdx = html.indexOf('<!-- ===== CLOZE MODE');
  const lastEndIdx = html.lastIndexOf('<!-- END CLOZE MODE -->');
  if (firstStartIdx !== -1 && lastEndIdx !== -1 && lastEndIdx > firstStartIdx) {
    const after = lastEndIdx + '<!-- END CLOZE MODE -->'.length;
    html = html.slice(0, firstStartIdx) + html.slice(after).replace(/^\s+/, '\n');
  }

  // Now insert the fresh BLOCK before </body>.
  html = html.replace(/(<\/body>\s*<\/html>\s*)$/, (_m, tail) => '\n' + literalBlock() + tail);
  fs.writeFileSync(filePath, html, 'utf8');
  updated++;
  console.log('✓ Injected Cloze Mode into', fname);
}
console.log(`\n${updated}/${FILES.length} study guides updated.`);
