/* ============================================================
   PORTABLE FLASHCARD CREATOR
   Self-contained: injects CSS + DOM + handlers on load.
   Works on any site (uses CSS variable fallbacks).
   Auto-detects "current section" via closest <h1>/<h2>/<h3> above scroll.

   Usage:
     <script src="flashcard-creator.js" defer></script>

   Storage keys (namespaced by hostname so each site has its own list):
     fc-cards-v1::<hostname>
     fc-instructions-v1::<hostname>
   ============================================================ */
(function() {
  if (window.__FC_CREATOR_LOADED__) return;
  window.__FC_CREATOR_LOADED__ = true;

  const HOST = location.host || 'local';
  const STORAGE_CARDS = 'fc-cards-v1::' + HOST;
  const STORAGE_INSTR = 'fc-instructions-v1::' + HOST;
  const SITE_TITLE = (document.title || 'site').split('—')[0].split('|')[0].trim().slice(0, 60) || 'site';

  const CSS = `
.fc-fab {
  position: fixed; left: 18px; bottom: 24px; z-index: 999990;
  display: inline-flex; align-items: center; gap: 6px;
  padding: 9px 14px;
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 999px;
  background: color-mix(in oklab, var(--bg, #0c0e12) 90%, transparent);
  color: var(--ink, #e6dfd0);
  font-family: var(--ff-ui, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  font-size: 13px; font-weight: 500; cursor: pointer;
  backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
  transition: transform .12s, background .12s, border-color .12s;
}
.fc-fab:hover { transform: translateY(-1px); background: var(--bg-elev, #1a1d24); border-color: #4a8fc9; }
.fc-fab .fc-plus { color: #4a8fc9; font-weight: 700; font-size: 16px; line-height: 1; }
.fc-fab .fc-count {
  background: rgba(74,143,201,0.25); color: #6cb8ff;
  border-radius: 8px; padding: 1px 7px;
  font-family: var(--ff-mono, "JetBrains Mono", ui-monospace, monospace);
  font-size: 11px; margin-left: 4px;
}
.fc-fab .fc-count[data-empty] { display: none; }
@media print { .fc-fab, .fc-modal-scrim, .fc-panel-scrim, .fc-toast { display: none !important; } }

.fc-modal-scrim, .fc-panel-scrim {
  position: fixed; inset: 0; z-index: 999995;
  background: rgba(0,0,0,0.55);
  display: none; align-items: flex-start; justify-content: center;
  padding: 60px 18px 24px; overflow-y: auto;
}
.fc-modal-scrim.open, .fc-panel-scrim.open { display: flex; }
.fc-modal, .fc-creator-panel {
  background: var(--bg-elev, #1a1d24);
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 8px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.5);
  width: 100%; max-width: 560px; padding: 22px 24px;
  font-family: var(--ff-ui, system-ui, sans-serif);
  color: var(--ink, #e6dfd0);
}
.fc-creator-panel { max-width: 760px; max-height: calc(100vh - 100px); display: flex; flex-direction: column; }
.fc-modal h3, .fc-creator-panel h3 {
  margin: 0 0 4px;
  font-family: var(--ff-display, var(--ff-ui, Georgia, serif));
  font-size: 22px; font-weight: 600;
}
.fc-modal .fc-section-tag {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--ff-mono, "JetBrains Mono", monospace);
  font-size: 11px; color: var(--ink-faint, #8a8474);
  text-transform: uppercase; letter-spacing: 0.06em;
  margin-bottom: 12px;
}
.fc-modal .fc-section-tag::before { content: "📍"; font-size: 14px; }
.fc-field { margin-bottom: 12px; }
.fc-field-label {
  display: block;
  font-family: var(--ff-mono, monospace);
  font-size: 10px; color: var(--ink-faint, #8a8474);
  letter-spacing: 0.12em; text-transform: uppercase;
  margin-bottom: 4px; font-weight: 600;
}
.fc-modal input[type="text"], .fc-modal textarea, .fc-creator-panel textarea {
  width: 100%; padding: 8px 12px;
  font-family: inherit; font-size: 14px; line-height: 1.5;
  color: var(--ink, #e6dfd0);
  background: var(--bg, #0c0e12);
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 5px; resize: vertical;
}
.fc-modal textarea { min-height: 90px; }
.fc-modal input[type="text"]:focus, .fc-modal textarea:focus, .fc-creator-panel textarea:focus { outline: 2px solid #4a8fc9; outline-offset: 1px; }

.fc-actions { margin-top: 16px; display: flex; gap: 8px; justify-content: flex-end; flex-wrap: wrap; }
.fc-actions button {
  padding: 7px 16px; border-radius: 5px;
  font-family: inherit; font-size: 13px; font-weight: 500;
  cursor: pointer;
  border: 1px solid var(--rule, #2a2d33);
  background: var(--bg, #0c0e12); color: var(--ink, #e6dfd0);
}
.fc-actions button.primary { background: #4a8fc9; color: white; border-color: #4a8fc9; }
.fc-actions button.primary:hover { background: #6cb8ff; }
.fc-actions button.secondary:hover { background: var(--bg-sunk, #060709); }
.fc-actions button.danger { color: #d97757; border-color: #d97757; margin-right: auto; }
.fc-actions button.danger:hover { background: rgba(217,119,87,0.15); }

.fc-creator-panel .fc-creator-head {
  display: flex; align-items: baseline; gap: 14px;
  margin-bottom: 14px; flex-wrap: wrap;
}
.fc-creator-panel .fc-panel-count {
  font-family: var(--ff-mono, monospace);
  font-size: 11px; color: var(--ink-faint, #8a8474);
  letter-spacing: 0.04em; text-transform: uppercase;
}
.fc-creator-panel .fc-panel-actions { margin-left: auto; display: flex; gap: 6px; flex-wrap: wrap; }
.fc-creator-panel .fc-panel-actions button {
  padding: 6px 12px; border-radius: 4px;
  font-family: inherit; font-size: 12px; font-weight: 500;
  cursor: pointer;
  border: 1px solid var(--rule, #2a2d33);
  background: var(--bg, #0c0e12); color: var(--ink, #e6dfd0);
}
.fc-creator-panel .fc-panel-actions button.primary { background: #4a8fc9; color: white; border-color: #4a8fc9; }
.fc-creator-panel .fc-panel-actions button.primary:hover { background: #6cb8ff; }
.fc-creator-panel .fc-panel-actions button:hover { background: var(--bg-sunk, #060709); }
.fc-creator-panel .fc-panel-actions button.danger { color: #d97757; border-color: rgba(217, 119, 87, 0.4); }

.fc-instructions {
  margin-bottom: 14px; padding: 12px;
  background: var(--bg, #0c0e12);
  border: 1px dashed #4a8fc9;
  border-radius: 5px;
}
.fc-instructions-label {
  font-family: var(--ff-mono, monospace);
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.14em;
  color: #4a8fc9; margin-bottom: 6px; font-weight: 600;
}
.fc-instructions textarea {
  min-height: 60px;
  border: 1px solid var(--rule, #2a2d33);
  background: var(--bg-sunk, #060709);
  font-size: 13px;
}
.fc-creator-body { overflow-y: auto; margin: 0 -8px; padding: 0 8px; }
.fc-card-item {
  background: var(--bg, #0c0e12);
  border: 1px solid var(--rule, #2a2d33);
  border-left: 3px solid #4a8fc9;
  border-radius: 5px; padding: 10px 12px; margin-top: 8px;
}
.fc-card-item-row1 {
  display: flex; gap: 10px; align-items: baseline;
  margin-bottom: 4px; flex-wrap: wrap;
}
.fc-card-item-section {
  font-family: var(--ff-mono, monospace);
  font-size: 10px; color: var(--ink-faint, #8a8474);
  letter-spacing: 0.04em;
}
.fc-card-item-actions { margin-left: auto; display: flex; gap: 4px; }
.fc-card-item-actions button {
  padding: 3px 9px; border: 1px solid var(--rule, #2a2d33); border-radius: 3px;
  background: transparent; color: var(--ink-dim, #b8b09e);
  font-family: inherit; font-size: 11px; cursor: pointer;
}
.fc-card-item-actions button:hover { background: var(--bg-elev, #1a1d24); color: var(--ink, #e6dfd0); }
.fc-card-item-actions button.danger { color: #d97757; }
.fc-card-item-actions button.danger:hover { background: rgba(217,119,87,0.18); }
.fc-card-term {
  font-family: var(--ff-display, var(--ff-ui, Georgia, serif));
  font-size: 16px; font-weight: 600;
  color: var(--ink, #e6dfd0); margin-bottom: 2px;
}
.fc-card-def {
  font-size: 13px; line-height: 1.45;
  color: var(--ink-dim, #b8b09e);
  white-space: pre-wrap; word-wrap: break-word;
}
.fc-card-mnemonic {
  margin-top: 6px; padding-left: 10px;
  border-left: 2px solid var(--accent, #c89b2e);
  font-family: var(--ff-display, italic);
  font-style: italic; font-size: 13px;
  color: var(--accent-ink, #f1d278);
}
.fc-empty {
  text-align: center; padding: 40px 20px;
  color: var(--ink-faint, #8a8474);
  font-size: 13px; font-style: italic;
}
.fc-toast {
  position: fixed; bottom: 24px; left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--ink, #e6dfd0); color: var(--bg, #0c0e12);
  padding: 9px 18px; border-radius: 5px;
  font-family: inherit; font-size: 13px; z-index: 999999;
  opacity: 0; pointer-events: none;
  transition: opacity .18s, transform .18s;
}
.fc-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
`;

  function injectStyles() {
    const s = document.createElement('style');
    s.id = 'fc-creator-styles';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function injectDOM() {
    const html = `
<button class="fc-fab" id="fcFab" type="button" title="Create flashcard (C)">
  <span class="fc-plus">+</span><span>Card</span>
  <span class="fc-count" id="fcCount" data-empty>0</span>
</button>
<div class="fc-modal-scrim" id="fcModalScrim" aria-hidden="true">
  <div class="fc-modal" role="dialog" aria-label="Create or edit flashcard">
    <h3 id="fcModalTitle">Create flashcard</h3>
    <div class="fc-section-tag" id="fcSectionTag">—</div>
    <div class="fc-field">
      <label class="fc-field-label" for="fcTerm">Term · front</label>
      <input type="text" id="fcTerm" placeholder="e.g. Sliding filament model" autocomplete="off">
    </div>
    <div class="fc-field">
      <label class="fc-field-label" for="fcDef">Definition · back</label>
      <textarea id="fcDef" placeholder="Plain-English explanation. HTML allowed."></textarea>
    </div>
    <div class="fc-field">
      <label class="fc-field-label" for="fcMnemonic">Memory hook · optional</label>
      <input type="text" id="fcMnemonic" placeholder="e.g. A = Always constant" autocomplete="off">
    </div>
    <div class="fc-field">
      <label class="fc-field-label" for="fcTags">Tags · comma-separated</label>
      <input type="text" id="fcTags" placeholder="muscle, exam-likely" autocomplete="off">
    </div>
    <div class="fc-actions">
      <button type="button" class="danger" id="fcDelete" style="display:none;">Delete</button>
      <button type="button" class="secondary" id="fcCancel">Cancel</button>
      <button type="button" class="primary" id="fcSave">Save card</button>
    </div>
  </div>
</div>
<div class="fc-panel-scrim" id="fcPanelScrim" aria-hidden="true">
  <div class="fc-creator-panel" role="dialog" aria-label="Flashcards list">
    <div class="fc-creator-head">
      <h3>Flashcards</h3>
      <span class="fc-panel-count" id="fcPanelCount">0</span>
      <div class="fc-panel-actions">
        <button type="button" class="primary" id="fcCopyText" title="Copy as text">Copy text</button>
        <button type="button" id="fcDownloadTxt" title="Download .txt">.txt</button>
        <button type="button" id="fcDownloadMd" title="Download .md">.md</button>
        <button type="button" id="fcDownloadJson" title="Download .json">.json</button>
        <button type="button" class="danger" id="fcClearAll">Clear all</button>
        <button type="button" id="fcPanelClose">Close</button>
      </div>
    </div>
    <div class="fc-instructions">
      <div class="fc-instructions-label">Instructions for Claude Code (included in every export)</div>
      <textarea id="fcInstructions" placeholder="e.g. 'Add these to the flashcards data file. Match existing schema. Group by tag.'"></textarea>
    </div>
    <div class="fc-creator-body" id="fcCreatorBody"></div>
  </div>
</div>
<div class="fc-toast" id="fcToast" role="status" aria-live="polite"></div>
`;
    const wrap = document.createElement('div');
    wrap.innerHTML = html;
    while (wrap.firstChild) document.body.appendChild(wrap.firstChild);
  }

  function getCurrentSection() {
    const headings = [...document.querySelectorAll('h1, h2, h3')].filter(h => h.offsetParent !== null);
    if (!headings.length) return { id: '', label: SITE_TITLE };
    const offset = 100;
    let best = null;
    for (const h of headings) {
      const r = h.getBoundingClientRect();
      if (r.top <= offset) {
        if (!best || r.top > best.r.top) best = { h, r };
      }
    }
    if (!best) best = { h: headings[0], r: headings[0].getBoundingClientRect() };
    const text = best.h.textContent.trim().slice(0, 80);
    return { id: best.h.id || '', label: text || SITE_TITLE };
  }

  function init() {
    if (document.getElementById('fcFab')) return;
    injectStyles();
    injectDOM();

    const fab = document.getElementById('fcFab');
    const countEl = document.getElementById('fcCount');
    const modalScrim = document.getElementById('fcModalScrim');
    const modalTitle = document.getElementById('fcModalTitle');
    const sectionTag = document.getElementById('fcSectionTag');
    const termEl = document.getElementById('fcTerm');
    const defEl = document.getElementById('fcDef');
    const mnemEl = document.getElementById('fcMnemonic');
    const tagsEl = document.getElementById('fcTags');
    const saveBtn = document.getElementById('fcSave');
    const cancelBtn = document.getElementById('fcCancel');
    const deleteBtn = document.getElementById('fcDelete');
    const panelScrim = document.getElementById('fcPanelScrim');
    const panelCount = document.getElementById('fcPanelCount');
    const panelBody = document.getElementById('fcCreatorBody');
    const instructionsEl = document.getElementById('fcInstructions');
    const copyTextBtn = document.getElementById('fcCopyText');
    const dlTxtBtn = document.getElementById('fcDownloadTxt');
    const dlMdBtn = document.getElementById('fcDownloadMd');
    const dlJsonBtn = document.getElementById('fcDownloadJson');
    const clearAllBtn = document.getElementById('fcClearAll');
    const panelCloseBtn = document.getElementById('fcPanelClose');
    const toastEl = document.getElementById('fcToast');

    let cards = [];
    let editingId = null;

    function load() {
      try {
        cards = JSON.parse(localStorage.getItem(STORAGE_CARDS) || '[]');
        if (!Array.isArray(cards)) cards = [];
        instructionsEl.value = localStorage.getItem(STORAGE_INSTR) || '';
      } catch (e) { cards = []; }
    }
    function save() {
      try {
        localStorage.setItem(STORAGE_CARDS, JSON.stringify(cards));
        localStorage.setItem(STORAGE_INSTR, instructionsEl.value || '');
        return true;
      } catch (e) { toast('Storage full'); return false; }
    }
    function uid() { return 'c_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2,7); }
    function escHtml(s) { return (s||'').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]); }
    function fmtTime(ts) {
      const d = new Date(ts);
      const today = new Date();
      return d.toDateString() === today.toDateString() ? d.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'}) : d.toLocaleDateString();
    }
    function toast(msg, ms) {
      toastEl.textContent = msg;
      toastEl.classList.add('show');
      clearTimeout(toast._t);
      toast._t = setTimeout(() => toastEl.classList.remove('show'), ms || 1800);
    }
    function refreshCount() {
      countEl.textContent = String(cards.length);
      if (cards.length === 0) countEl.setAttribute('data-empty', '');
      else countEl.removeAttribute('data-empty');
      panelCount.textContent = cards.length + (cards.length === 1 ? ' card' : ' cards');
    }

    function openModal(opts) {
      opts = opts || {};
      editingId = opts.cardId || null;
      const sec = getCurrentSection();
      if (editingId) {
        const c = cards.find(x => x.id === editingId);
        if (!c) { editingId = null; return; }
        modalTitle.textContent = 'Edit flashcard';
        sectionTag.textContent = c.sectionLabel || sec.label;
        sectionTag.dataset.sectionId = c.sectionId || sec.id;
        termEl.value = c.term || '';
        defEl.value = c.def || '';
        mnemEl.value = c.mnemonic || '';
        tagsEl.value = (c.tags || []).join(', ');
        deleteBtn.style.display = '';
      } else {
        modalTitle.textContent = 'Create flashcard';
        sectionTag.textContent = sec.label;
        sectionTag.dataset.sectionId = sec.id;
        termEl.value = ''; defEl.value = ''; mnemEl.value = ''; tagsEl.value = '';
        deleteBtn.style.display = 'none';
      }
      modalScrim.classList.add('open');
      modalScrim.setAttribute('aria-hidden', 'false');
      setTimeout(() => termEl.focus(), 50);
    }
    function closeModal() {
      modalScrim.classList.remove('open');
      modalScrim.setAttribute('aria-hidden', 'true');
      editingId = null;
    }

    function commitSave() {
      const term = termEl.value.trim();
      const def = defEl.value.trim();
      if (!term && !def) { toast('Add a term or definition'); return; }
      const data = {
        term, def,
        mnemonic: mnemEl.value.trim(),
        tags: tagsEl.value.split(',').map(t => t.trim()).filter(Boolean),
        sectionId: sectionTag.dataset.sectionId || '',
        sectionLabel: sectionTag.textContent || '',
        page: location.pathname
      };
      if (editingId) {
        const c = cards.find(x => x.id === editingId);
        if (c) { Object.assign(c, data); c.editedTs = Date.now(); }
      } else {
        cards.push({ id: uid(), ts: Date.now(), ...data });
      }
      if (save()) { refreshCount(); renderPanel(); closeModal(); toast(editingId ? 'Updated' : 'Saved'); }
    }
    function commitDelete() {
      if (!editingId) return;
      if (!confirm('Delete this card?')) return;
      cards = cards.filter(c => c.id !== editingId);
      if (save()) { refreshCount(); renderPanel(); closeModal(); toast('Deleted'); }
    }

    function renderPanel() {
      if (cards.length === 0) {
        panelBody.innerHTML = '<div class="fc-empty">No cards yet.<br>Click <strong>+ Card</strong> while reading to author one.<br>Press <kbd>C</kbd> for quick-add.</div>';
        return;
      }
      const groups = {};
      cards.forEach(c => { const k = c.sectionLabel || '(unsorted)'; (groups[k] = groups[k] || []).push(c); });
      panelBody.innerHTML = Object.keys(groups).sort().map(k => {
        const items = groups[k].sort((a,b) => a.ts - b.ts);
        const itemsHtml = items.map(c => `
          <div class="fc-card-item" data-id="${c.id}">
            <div class="fc-card-item-row1">
              <span class="fc-card-item-section">${escHtml(fmtTime(c.ts))}${c.tags?.length ? ' · ' + escHtml(c.tags.join(', ')) : ''}${c.page && c.page !== location.pathname ? ' · ' + escHtml(c.page) : ''}</span>
              <div class="fc-card-item-actions">
                <button class="fc-edit" data-id="${c.id}">Edit</button>
                <button class="danger fc-del" data-id="${c.id}">Delete</button>
              </div>
            </div>
            <div class="fc-card-term">${escHtml(c.term || '(no term)')}</div>
            <div class="fc-card-def">${escHtml(c.def || '')}</div>
            ${c.mnemonic ? `<div class="fc-card-mnemonic">↻ ${escHtml(c.mnemonic)}</div>` : ''}
          </div>`).join('');
        return `<div style="margin-top:14px;"><div style="font-family:var(--ff-mono, monospace); font-size:10px; text-transform:uppercase; letter-spacing:0.14em; color:#4a8fc9; padding-bottom:4px; border-bottom:1px solid var(--rule, #2a2d33);">${escHtml(k)}</div>${itemsHtml}</div>`;
      }).join('');
      panelBody.querySelectorAll('.fc-edit').forEach(b => b.addEventListener('click', () => {
        panelScrim.classList.remove('open');
        openModal({ cardId: b.dataset.id });
      }));
      panelBody.querySelectorAll('.fc-del').forEach(b => b.addEventListener('click', () => {
        const id = b.dataset.id;
        if (!confirm('Delete this card?')) return;
        cards = cards.filter(c => c.id !== id);
        if (save()) { refreshCount(); renderPanel(); toast('Deleted'); }
      }));
    }

    function buildPlainText() {
      const today = new Date().toLocaleDateString();
      const lines = [];
      lines.push('FLASHCARDS — created ' + today);
      lines.push('Site: ' + HOST);
      lines.push('Total cards: ' + cards.length);
      lines.push('');
      lines.push('=== INSTRUCTIONS FOR CLAUDE CODE ===');
      lines.push(instructionsEl.value.trim() || '(no instructions provided)');
      lines.push('');
      lines.push('=== CARDS ===');
      lines.push('');
      const groups = {};
      cards.forEach(c => { const k = c.sectionLabel || '(unsorted)'; (groups[k] = groups[k] || []).push(c); });
      Object.keys(groups).sort().forEach(k => {
        lines.push('## ' + k);
        lines.push('');
        groups[k].sort((a,b)=>a.ts-b.ts).forEach((c, i) => {
          lines.push('CARD ' + (i+1));
          lines.push('  Term: ' + (c.term || ''));
          lines.push('  Definition: ' + (c.def || ''));
          if (c.mnemonic) lines.push('  Mnemonic: ' + c.mnemonic);
          if (c.tags?.length) lines.push('  Tags: ' + c.tags.join(', '));
          if (c.page) lines.push('  Page: ' + c.page);
          lines.push('');
        });
      });
      return lines.join('\n');
    }
    function buildMarkdown() {
      const today = new Date().toLocaleDateString();
      const lines = [];
      lines.push('# Flashcards — ' + today);
      lines.push('');
      lines.push('**Site:** `' + HOST + '`  ');
      lines.push('**Total cards:** ' + cards.length);
      lines.push('');
      lines.push('## Instructions for Claude Code');
      lines.push('');
      lines.push('> ' + (instructionsEl.value.trim().replace(/\n/g, '\n> ') || '_(no instructions)_'));
      lines.push('');
      lines.push('## Cards');
      lines.push('');
      const groups = {};
      cards.forEach(c => { const k = c.sectionLabel || '(unsorted)'; (groups[k] = groups[k] || []).push(c); });
      Object.keys(groups).sort().forEach(k => {
        lines.push('### ' + k);
        lines.push('');
        groups[k].sort((a,b)=>a.ts-b.ts).forEach(c => {
          lines.push('- **' + (c.term || '(no term)') + '** — ' + (c.def || ''));
          if (c.mnemonic) lines.push('  - *Hook:* ' + c.mnemonic);
          if (c.tags?.length) lines.push('  - *Tags:* ' + c.tags.map(t=>'`'+t+'`').join(' '));
        });
        lines.push('');
      });
      return lines.join('\n');
    }
    function buildJson() {
      return JSON.stringify({
        site: HOST,
        generated: new Date().toISOString(),
        instructions: instructionsEl.value.trim(),
        total: cards.length,
        cards: cards.map(c => ({
          term: c.term || '', def: c.def || '',
          mnemonic: c.mnemonic || '', tags: c.tags || [],
          sectionId: c.sectionId || '', sectionLabel: c.sectionLabel || '',
          page: c.page || '', createdAt: new Date(c.ts).toISOString()
        }))
      }, null, 2);
    }

    function copyText() {
      if (!cards.length) { toast('No cards yet'); return; }
      const text = buildPlainText();
      if (navigator.clipboard?.writeText) {
        navigator.clipboard.writeText(text).then(() => toast('Copied'), () => fallbackCopy(text));
      } else fallbackCopy(text);
    }
    function fallbackCopy(text) {
      const ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); toast('Copied'); }
      catch (e) { toast('Copy failed'); console.log(text); }
      document.body.removeChild(ta);
    }
    function triggerDownload(blob, filename) {
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = filename;
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    }
    function datestamp() {
      const d = new Date();
      return d.getFullYear() + String(d.getMonth()+1).padStart(2,'0') + String(d.getDate()).padStart(2,'0');
    }
    function downloadTxt() {
      if (!cards.length) { toast('No cards yet'); return; }
      triggerDownload(new Blob([buildPlainText()], { type: 'text/plain' }), 'flashcards-' + datestamp() + '.txt');
      toast('Downloaded .txt');
    }
    function downloadMd() {
      if (!cards.length) { toast('No cards yet'); return; }
      triggerDownload(new Blob([buildMarkdown()], { type: 'text/markdown' }), 'flashcards-' + datestamp() + '.md');
      toast('Downloaded .md');
    }
    function downloadJson() {
      if (!cards.length) { toast('No cards yet'); return; }
      triggerDownload(new Blob([buildJson()], { type: 'application/json' }), 'flashcards-' + datestamp() + '.json');
      toast('Downloaded .json');
    }

    function clearAll() {
      if (!cards.length) return;
      if (!confirm('Delete ALL ' + cards.length + ' cards? Instructions kept.')) return;
      cards = []; save(); refreshCount(); renderPanel(); toast('Cleared');
    }
    function openPanel() {
      renderPanel();
      panelScrim.classList.add('open');
      panelScrim.setAttribute('aria-hidden', 'false');
    }
    function closePanel() {
      save();
      panelScrim.classList.remove('open');
      panelScrim.setAttribute('aria-hidden', 'true');
    }

    fab.addEventListener('click', e => { if (e.shiftKey) { openPanel(); return; } openModal(); });
    fab.addEventListener('contextmenu', e => { e.preventDefault(); openPanel(); });
    countEl.addEventListener('click', e => { e.stopPropagation(); openPanel(); });

    saveBtn.addEventListener('click', commitSave);
    cancelBtn.addEventListener('click', closeModal);
    deleteBtn.addEventListener('click', commitDelete);
    modalScrim.addEventListener('click', e => { if (e.target === modalScrim) closeModal(); });
    copyTextBtn.addEventListener('click', copyText);
    dlTxtBtn.addEventListener('click', downloadTxt);
    dlMdBtn.addEventListener('click', downloadMd);
    dlJsonBtn.addEventListener('click', downloadJson);
    clearAllBtn.addEventListener('click', clearAll);
    panelCloseBtn.addEventListener('click', closePanel);
    panelScrim.addEventListener('click', e => { if (e.target === panelScrim) closePanel(); });
    instructionsEl.addEventListener('change', save);
    instructionsEl.addEventListener('blur', save);

    defEl.addEventListener('keydown', e => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') { e.preventDefault(); commitSave(); }
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        if (modalScrim.classList.contains('open')) closeModal();
        else if (panelScrim.classList.contains('open')) closePanel();
      }
    });
    document.addEventListener('keydown', e => {
      const tag = e.target.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA') return;
      if (e.metaKey || e.ctrlKey || e.altKey || e.shiftKey) return;
      if (e.key === 'c' || e.key === 'C') { e.preventDefault(); openModal(); }
    });

    load();
    refreshCount();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
