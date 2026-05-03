/* Inject a mobile-responsive CSS block into every study-guide HTML.
   Idempotent — re-runnable. Inserts a <style id="mobile-responsive-styles">
   block right before </head>. Strip+replace if it already exists.

   Fixes:
     • .doc width:8.5in fixed → 100% on small screens (no horizontal scroll)
     • Cloze toggle button → 44px min touch target on mobile
     • Tooltip max-width → fits within viewport on narrow screens
     • Toolbar groups wrap nicely
*/
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const FILES = ['study-guide-exam1.html', 'study-guide-exam2.html', 'study-guide-exam3.html'];

const BLOCK = `
<!-- ===== MOBILE RESPONSIVE — auto-injected by scripts/inject-mobile-css.js ===== -->
<style id="mobile-responsive-styles">
  /* Tablet + small laptop */
  @media (max-width: 900px) {
    .doc { padding: 0.5in 0.5in; }
  }
  /* Phone */
  @media (max-width: 640px) {
    .doc {
      width: 100% !important;
      min-height: 0 !important;
      padding: 14px 12px !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      font-size: 11.5pt;
    }
    .pageWrap, .wrap { padding: 4px !important; }
    body { font-size: 14px; }
    /* Editor toolbar — stack rows + wrap groups, keep buttons tappable */
    #toolbar, .tb { padding: 6px !important; }
    .tb-row { flex-wrap: wrap !important; gap: 4px !important; }
    .tb-row .grp { flex-wrap: wrap !important; }
    .tb button, .tb select, .tb input[type=color] {
      min-height: 36px !important;
      padding: 6px 9px !important;
      font-size: 12.5px !important;
    }
    /* Cloze toggle — bigger tap target on mobile */
    #clozeToggleBtn {
      min-height: 44px !important;
      padding: 10px 16px !important;
      font-size: 13.5px !important;
      top: 8px !important;
      right: 8px !important;
    }
    /* Tooltip — narrower so it fits within phone viewport */
    #termTooltip {
      max-width: calc(100vw - 16px) !important;
      font-size: 12.5px !important;
    }
    /* Cloze help banner — push down so it doesn't cover the toggle */
    #clozeHelp {
      top: 56px !important;
      right: 8px !important;
      max-width: calc(100vw - 16px) !important;
    }
    /* Bolded terms in body — keep wrappable on mobile so super-long terms don't overflow */
    .doc b, .doc strong { word-break: break-word; }
    /* Cloze blanks — readable on mobile */
    .cloze-blank { min-width: 24px; padding: 0 5px; }
  }
</style>
<!-- END MOBILE RESPONSIVE -->
`;

const START = '<!-- ===== MOBILE RESPONSIVE';
const END = '<!-- END MOBILE RESPONSIVE -->';

let updated = 0;
for (const fname of FILES) {
  const filePath = path.join(ROOT, fname);
  if (!fs.existsSync(filePath)) { console.warn('SKIP missing:', fname); continue; }
  let html = fs.readFileSync(filePath, 'utf8');
  // Idempotent strip: remove any existing block (handles partial corruption too)
  const startIdx = html.indexOf(START);
  const endIdx = html.lastIndexOf(END);
  if (startIdx !== -1 && endIdx !== -1 && endIdx > startIdx) {
    html = html.slice(0, startIdx) + html.slice(endIdx + END.length).replace(/^\s+/, '\n');
  }
  // Insert before </head> (function form so any $& in BLOCK is treated literally)
  html = html.replace(/(<\/head>)/i, (_m) => BLOCK.trim() + '\n' + _m);
  fs.writeFileSync(filePath, html, 'utf8');
  updated++;
  console.log('✓ Injected mobile CSS into', fname);
}
console.log(`\n${updated}/${FILES.length} study guides updated.`);
