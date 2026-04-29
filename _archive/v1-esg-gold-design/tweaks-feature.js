/* ============================================================
   PORTABLE TWEAKS CAPTURE FEATURE
   Self-contained: injects CSS + DOM + handlers on load.
   Works on any site (with or without CSS variables — uses fallback colors).
   Detects "current section" by finding the closest <h1>/<h2>/<h3> above scroll.

   How to use:
     <script src="tweaks-feature.js" defer></script>
   ============================================================ */
(function() {
  if (window.__TWEAKS_LOADED__) return;
  window.__TWEAKS_LOADED__ = true;

  // -------- CONFIG --------
  // localStorage key namespaced by hostname + pathname so each site has its own list
  const STORAGE_KEY = 'tweaks-v1::' + (location.host || 'local');
  const MAX_IMAGE_BYTES = 800 * 1024;
  const SITE_TITLE = (document.title || 'site').split('—')[0].split('|')[0].trim().slice(0, 60) || 'site';

  // -------- CSS --------
  const CSS = `
.tweak-fab {
  position: fixed; right: 18px; bottom: 24px; z-index: 999990;
  display: inline-flex; align-items: center; gap: 6px;
  padding: 9px 14px;
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 999px;
  background: color-mix(in oklab, var(--bg, #0c0e12) 90%, transparent);
  color: var(--ink, #e6dfd0);
  font-family: var(--ff-ui, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  font-size: 13px; font-weight: 500;
  cursor: pointer;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
  transition: transform .12s, background .12s, border-color .12s;
}
.tweak-fab:hover { transform: translateY(-1px); background: var(--bg-elev, #1a1d24); border-color: var(--accent, #c89b2e); }
.tweak-fab .tweak-plus { color: var(--accent, #c89b2e); font-weight: 700; font-size: 16px; line-height: 1; }
.tweak-fab .tweak-count {
  background: var(--accent-soft, #5b4412); color: var(--accent-ink, #f1d278);
  border-radius: 8px; padding: 1px 7px;
  font-family: var(--ff-mono, "JetBrains Mono", ui-monospace, monospace);
  font-size: 11px; margin-left: 4px;
}
.tweak-fab .tweak-count[data-empty] { display: none; }
.tweak-fab.list-mode { background: var(--accent-soft, #5b4412); border-color: var(--accent-soft, #5b4412); color: var(--accent-ink, #f1d278); }
@media print { .tweak-fab, .tweak-modal-scrim, .tweak-panel-scrim, .tweak-toast { display: none !important; } }
.tweak-modal-scrim, .tweak-panel-scrim {
  position: fixed; inset: 0; z-index: 999995;
  background: rgba(0,0,0,0.55);
  display: none; align-items: flex-start; justify-content: center;
  padding: 60px 18px 24px; overflow-y: auto;
}
.tweak-modal-scrim.open, .tweak-panel-scrim.open { display: flex; }
.tweak-modal, .tweak-panel {
  background: var(--bg-elev, #1a1d24);
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 8px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.5);
  width: 100%; max-width: 540px;
  padding: 22px;
  font-family: var(--ff-ui, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  color: var(--ink, #e6dfd0);
}
.tweak-panel { max-width: 720px; max-height: calc(100vh - 100px); display: flex; flex-direction: column; }
.tweak-modal h3, .tweak-panel-head h3 {
  margin: 0 0 4px;
  font-family: var(--ff-display, var(--ff-ui, Georgia, serif));
  font-size: 22px; font-weight: 600;
}
.tweak-section-tag {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--ff-mono, "JetBrains Mono", monospace);
  font-size: 11px; color: var(--ink-faint, #8a8474);
  text-transform: uppercase; letter-spacing: 0.06em;
  margin-bottom: 14px;
}
.tweak-section-tag::before { content: "📍"; font-size: 14px; }
.tweak-modal textarea {
  width: 100%; min-height: 110px; padding: 10px 12px;
  font-family: inherit; font-size: 14px; line-height: 1.5;
  color: var(--ink, #e6dfd0);
  background: var(--bg, #0c0e12);
  border: 1px solid var(--rule, #2a2d33); border-radius: 6px;
  resize: vertical;
}
.tweak-modal textarea:focus { outline: 2px solid var(--accent, #c89b2e); outline-offset: 1px; }
.tweak-img-tray {
  display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; min-height: 24px;
}
.tweak-img-tray:empty::before {
  content: "Tip: paste a screenshot here (Ctrl/Cmd-V) — Win+Shift+S, then paste";
  font-size: 12px; color: var(--ink-faint, #8a8474); font-style: italic;
}
.tweak-img {
  position: relative; width: 100px; height: 70px;
  border: 1px solid var(--rule, #2a2d33); border-radius: 4px; overflow: hidden;
  background: var(--bg, #0c0e12);
}
.tweak-img img { width: 100%; height: 100%; object-fit: cover; }
.tweak-img-x {
  position: absolute; top: 2px; right: 2px;
  width: 18px; height: 18px; border: 0; border-radius: 50%;
  background: rgba(0,0,0,0.7); color: white;
  font-size: 11px; line-height: 1; cursor: pointer; padding: 0;
}
.tweak-actions { margin-top: 16px; display: flex; gap: 8px; justify-content: flex-end; flex-wrap: wrap; }
.tweak-actions button, .tweak-panel-actions button {
  padding: 7px 14px; border-radius: 5px;
  font-family: inherit; font-size: 13px; font-weight: 500;
  cursor: pointer;
  border: 1px solid var(--rule, #2a2d33);
  background: var(--bg, #0c0e12); color: var(--ink, #e6dfd0);
  transition: background .1s, border-color .1s;
}
.tweak-actions button.primary, .tweak-panel-actions button.primary {
  background: var(--accent, #c89b2e); color: var(--bg-sunk, #060709); border-color: var(--accent, #c89b2e);
}
.tweak-actions button.primary:hover, .tweak-panel-actions button.primary:hover { background: var(--accent-ink, #f1d278); }
.tweak-actions button.secondary:hover, .tweak-panel-actions button:hover { background: var(--bg-sunk, #060709); }
.tweak-actions button.danger, .tweak-panel-actions button.danger { color: #d97757; border-color: #d97757; }
.tweak-actions button.danger { margin-right: auto; }
.tweak-actions button.danger:hover, .tweak-panel-actions button.danger:hover { background: rgba(217,119,87,0.15); }
.tweak-modal-meta {
  margin-top: 10px;
  font-family: var(--ff-mono, monospace);
  font-size: 10px; color: var(--ink-faint, #8a8474); letter-spacing: 0.04em;
}
.tweak-panel-head {
  display: flex; align-items: baseline; gap: 14px;
  margin-bottom: 14px; flex-wrap: wrap;
}
.tweak-panel-count {
  font-family: var(--ff-mono, monospace);
  font-size: 11px; color: var(--ink-faint, #8a8474);
  letter-spacing: 0.04em; text-transform: uppercase;
}
.tweak-panel-actions { margin-left: auto; display: flex; gap: 6px; flex-wrap: wrap; }
.tweak-panel-actions button { padding: 6px 11px; font-size: 12px; }
.tweak-panel-body { overflow-y: auto; margin: 0 -8px; padding: 0 8px; }
.tweak-group { margin-top: 16px; }
.tweak-group:first-child { margin-top: 4px; }
.tweak-group-h {
  font-family: var(--ff-mono, monospace);
  font-size: 10px; text-transform: uppercase;
  letter-spacing: 0.14em; color: var(--accent, #c89b2e);
  margin-bottom: 6px; padding-bottom: 4px;
  border-bottom: 1px solid var(--rule, #2a2d33);
}
.tweak-item {
  background: var(--bg, #0c0e12);
  border: 1px solid var(--rule, #2a2d33);
  border-radius: 5px;
  padding: 10px 12px; margin-top: 6px;
}
.tweak-item-row1 {
  display: flex; gap: 10px; align-items: baseline;
  margin-bottom: 4px; flex-wrap: wrap;
}
.tweak-item-time {
  font-family: var(--ff-mono, monospace);
  font-size: 10px; color: var(--ink-faint, #8a8474);
  letter-spacing: 0.04em;
}
.tweak-item-actions { margin-left: auto; display: flex; gap: 4px; }
.tweak-item-actions button {
  padding: 3px 9px; border: 1px solid var(--rule, #2a2d33); border-radius: 3px;
  background: transparent; color: var(--ink-dim, #b8b09e);
  font-family: inherit; font-size: 11px; cursor: pointer;
}
.tweak-item-actions button:hover { background: var(--bg-elev, #1a1d24); color: var(--ink, #e6dfd0); }
.tweak-item-actions button.danger { color: #d97757; }
.tweak-item-actions button.danger:hover { background: rgba(217,119,87,0.18); border-color: #d97757; }
.tweak-item-note {
  font-size: 14px; line-height: 1.45;
  color: var(--ink, #e6dfd0);
  white-space: pre-wrap; word-wrap: break-word;
}
.tweak-item-imgs { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
.tweak-item-imgs img {
  height: 60px; border: 1px solid var(--rule, #2a2d33);
  border-radius: 3px; cursor: zoom-in;
}
.tweak-empty {
  text-align: center; padding: 40px 20px;
  color: var(--ink-faint, #8a8474);
  font-size: 13px; font-style: italic;
}
.tweak-toast {
  position: fixed; bottom: 24px; left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--ink, #e6dfd0); color: var(--bg, #0c0e12);
  padding: 9px 18px; border-radius: 5px;
  font-family: var(--ff-ui, system-ui, sans-serif);
  font-size: 13px; z-index: 999999;
  opacity: 0; pointer-events: none;
  transition: opacity .18s, transform .18s;
}
.tweak-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
`;

  function injectStyles() {
    const s = document.createElement('style');
    s.id = 'tweak-feature-styles';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function injectDOM() {
    const html = `
<button class="tweak-fab" id="tweakFab" type="button" title="Add a tweak (T)">
  <span class="tweak-plus">+</span>
  <span>Tweak</span>
  <span class="tweak-count" id="tweakCount" data-empty>0</span>
</button>
<div class="tweak-modal-scrim" id="tweakModalScrim" aria-hidden="true">
  <div class="tweak-modal" role="dialog" aria-label="Add or edit tweak">
    <h3 id="tweakModalTitle">Add tweak</h3>
    <div class="tweak-section-tag" id="tweakSectionTag">—</div>
    <textarea id="tweakNote" placeholder="What needs to change here?" autocomplete="off"></textarea>
    <div class="tweak-img-tray" id="tweakImgTray" tabindex="0"></div>
    <div class="tweak-actions">
      <button type="button" class="danger" id="tweakDelete" style="display:none;">Delete</button>
      <button type="button" class="secondary" id="tweakCancel">Cancel</button>
      <button type="button" class="primary" id="tweakSave">Save</button>
    </div>
    <div class="tweak-modal-meta" id="tweakModalMeta"></div>
  </div>
</div>
<div class="tweak-panel-scrim" id="tweakPanelScrim" aria-hidden="true">
  <div class="tweak-panel" role="dialog" aria-label="Tweaks list">
    <div class="tweak-panel-head">
      <h3>Tweaks</h3>
      <span class="tweak-panel-count" id="tweakPanelCount">0</span>
      <div class="tweak-panel-actions">
        <button type="button" class="primary" id="tweakCopyAll" title="Copy text to clipboard">Copy text</button>
        <button type="button" id="tweakDownloadMd" title="Download .md (with embedded images)">.md</button>
        <button type="button" id="tweakDownloadZip" title="Download .zip (TWEAKS.md + images/)">.zip</button>
        <button type="button" class="danger" id="tweakClearAll">Clear all</button>
        <button type="button" id="tweakPanelClose">Close</button>
      </div>
    </div>
    <div class="tweak-panel-body" id="tweakPanelBody"></div>
  </div>
</div>
<div class="tweak-toast" id="tweakToast" role="status" aria-live="polite"></div>
`;
    const wrap = document.createElement('div');
    wrap.innerHTML = html;
    while (wrap.firstChild) document.body.appendChild(wrap.firstChild);
  }

  // -------- HEADING-BASED CURRENT-SECTION DETECTION --------
  function getCurrentSection() {
    // Find the closest h1/h2/h3 above the scroll position
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
    const id = best.h.id || '';
    return { id, label: text || SITE_TITLE };
  }

  function init() {
    if (document.getElementById('tweakFab')) return;
    injectStyles();
    injectDOM();

    const fab = document.getElementById('tweakFab');
    const countEl = document.getElementById('tweakCount');
    const modalScrim = document.getElementById('tweakModalScrim');
    const modalTitle = document.getElementById('tweakModalTitle');
    const sectionTag = document.getElementById('tweakSectionTag');
    const noteEl = document.getElementById('tweakNote');
    const imgTray = document.getElementById('tweakImgTray');
    const saveBtn = document.getElementById('tweakSave');
    const cancelBtn = document.getElementById('tweakCancel');
    const deleteBtn = document.getElementById('tweakDelete');
    const metaEl = document.getElementById('tweakModalMeta');
    const panelScrim = document.getElementById('tweakPanelScrim');
    const panelBody = document.getElementById('tweakPanelBody');
    const panelCount = document.getElementById('tweakPanelCount');
    const copyAllBtn = document.getElementById('tweakCopyAll');
    const downloadMdBtn = document.getElementById('tweakDownloadMd');
    const downloadZipBtn = document.getElementById('tweakDownloadZip');
    const clearAllBtn = document.getElementById('tweakClearAll');
    const panelCloseBtn = document.getElementById('tweakPanelClose');
    const toastEl = document.getElementById('tweakToast');

    let tweaks = [];
    let editingId = null;
    let pendingImgs = [];

    function load() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        tweaks = raw ? JSON.parse(raw) : [];
        if (!Array.isArray(tweaks)) tweaks = [];
      } catch (e) { tweaks = []; }
    }
    function save() {
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(tweaks)); return true; }
      catch (e) { toast('Storage full — remove old screenshots'); return false; }
    }
    function uid() { return 't_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2,7); }
    function fmtTime(ts) {
      const d = new Date(ts);
      const today = new Date();
      const isToday = d.toDateString() === today.toDateString();
      return isToday ? d.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'}) : d.toLocaleDateString() + ' ' + d.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
    }
    function escHtml(s) { return (s||'').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]); }
    function toast(msg, ms) {
      toastEl.textContent = msg;
      toastEl.classList.add('show');
      clearTimeout(toast._t);
      toast._t = setTimeout(() => toastEl.classList.remove('show'), ms || 1800);
    }
    function refreshCount() {
      countEl.textContent = String(tweaks.length);
      if (tweaks.length === 0) countEl.setAttribute('data-empty', '');
      else countEl.removeAttribute('data-empty');
      panelCount.textContent = tweaks.length + (tweaks.length === 1 ? ' tweak' : ' tweaks');
    }

    function renderImgTray() {
      imgTray.innerHTML = '';
      pendingImgs.forEach((dataUrl, i) => {
        const wrap = document.createElement('div');
        wrap.className = 'tweak-img';
        const img = document.createElement('img');
        img.src = dataUrl; img.alt = 'Screenshot ' + (i+1);
        wrap.appendChild(img);
        const x = document.createElement('button');
        x.type = 'button'; x.className = 'tweak-img-x';
        x.textContent = '×'; x.title = 'Remove';
        x.addEventListener('click', () => { pendingImgs.splice(i, 1); renderImgTray(); });
        wrap.appendChild(x);
        imgTray.appendChild(wrap);
      });
    }

    function openModal(opts) {
      opts = opts || {};
      editingId = opts.tweakId || null;
      const sec = getCurrentSection();
      if (editingId) {
        const t = tweaks.find(x => x.id === editingId);
        if (!t) { editingId = null; return; }
        modalTitle.textContent = 'Edit tweak';
        sectionTag.textContent = t.sectionLabel || sec.label;
        sectionTag.dataset.sectionId = t.sectionId || sec.id;
        noteEl.value = t.note || '';
        pendingImgs = (t.screenshots || []).slice();
        deleteBtn.style.display = '';
        metaEl.textContent = 'Created ' + fmtTime(t.ts) + (t.editedTs ? ' · edited ' + fmtTime(t.editedTs) : '');
      } else {
        modalTitle.textContent = 'Add tweak';
        sectionTag.textContent = sec.label;
        sectionTag.dataset.sectionId = sec.id;
        noteEl.value = '';
        pendingImgs = [];
        deleteBtn.style.display = 'none';
        metaEl.textContent = sec.id ? '#' + sec.id : '';
      }
      renderImgTray();
      modalScrim.classList.add('open');
      modalScrim.setAttribute('aria-hidden', 'false');
      setTimeout(() => noteEl.focus(), 50);
    }
    function closeModal() {
      modalScrim.classList.remove('open');
      modalScrim.setAttribute('aria-hidden', 'true');
      editingId = null; pendingImgs = [];
    }

    function commitSave() {
      const note = noteEl.value.trim();
      if (!note && pendingImgs.length === 0) { toast('Add a note or paste a screenshot'); return; }
      if (editingId) {
        const t = tweaks.find(x => x.id === editingId);
        if (t) { t.note = note; t.screenshots = pendingImgs.slice(); t.editedTs = Date.now(); }
      } else {
        const sec = { id: sectionTag.dataset.sectionId || '', label: sectionTag.textContent || 'Top of page' };
        tweaks.push({
          id: uid(), ts: Date.now(),
          sectionId: sec.id, sectionLabel: sec.label,
          note, screenshots: pendingImgs.slice(),
          page: location.pathname
        });
      }
      if (save()) { refreshCount(); renderPanel(); closeModal(); toast(editingId ? 'Updated' : 'Saved'); }
    }
    function commitDelete() {
      if (!editingId) return;
      if (!confirm('Delete this tweak?')) return;
      tweaks = tweaks.filter(t => t.id !== editingId);
      if (save()) { refreshCount(); renderPanel(); closeModal(); toast('Deleted'); }
    }

    document.addEventListener('paste', e => {
      if (!modalScrim.classList.contains('open')) return;
      const items = (e.clipboardData || (e.originalEvent && e.originalEvent.clipboardData))?.items || [];
      let handled = false;
      for (const item of items) {
        if (item.kind === 'file' && item.type.startsWith('image/')) {
          const f = item.getAsFile();
          if (!f) continue;
          if (f.size > MAX_IMAGE_BYTES * 1.5) { toast('Image too large (' + Math.round(f.size/1024) + ' KB)'); continue; }
          const reader = new FileReader();
          reader.onload = () => { pendingImgs.push(reader.result); renderImgTray(); toast('Screenshot attached'); };
          reader.readAsDataURL(f);
          handled = true;
        }
      }
      if (handled) e.preventDefault();
    });

    function renderPanel() {
      if (tweaks.length === 0) {
        panelBody.innerHTML = '<div class="tweak-empty">No tweaks yet.<br>Click <strong>+ Tweak</strong> while reading to flag an issue.<br>Press <kbd>T</kbd> to add quickly.</div>';
        return;
      }
      const groups = {};
      tweaks.forEach(t => {
        const k = t.sectionLabel || '(no section)';
        if (!groups[k]) groups[k] = [];
        groups[k].push(t);
      });
      const keys = Object.keys(groups).sort();
      panelBody.innerHTML = keys.map(k => {
        const items = groups[k].sort((a,b) => a.ts - b.ts);
        const itemsHtml = items.map(t => {
          const imgs = (t.screenshots || []).map(d => `<img src="${d}" alt="screenshot" loading="lazy">`).join('');
          const pageInfo = t.page && t.page !== location.pathname ? ` · <em>${escHtml(t.page)}</em>` : '';
          return `<div class="tweak-item" data-id="${t.id}">
            <div class="tweak-item-row1">
              <span class="tweak-item-time">${escHtml(fmtTime(t.ts))}${t.editedTs ? ' · edited ' + escHtml(fmtTime(t.editedTs)) : ''}${pageInfo}</span>
              <div class="tweak-item-actions">
                <button class="tweak-edit" data-id="${t.id}">Edit</button>
                <button class="danger tweak-del" data-id="${t.id}">Delete</button>
              </div>
            </div>
            <div class="tweak-item-note">${escHtml(t.note)}</div>
            ${imgs ? `<div class="tweak-item-imgs">${imgs}</div>` : ''}
          </div>`;
        }).join('');
        return `<div class="tweak-group"><div class="tweak-group-h">${escHtml(k)}</div>${itemsHtml}</div>`;
      }).join('');
      panelBody.querySelectorAll('.tweak-edit').forEach(b => b.addEventListener('click', () => {
        panelScrim.classList.remove('open');
        openModal({ tweakId: b.dataset.id });
      }));
      panelBody.querySelectorAll('.tweak-del').forEach(b => b.addEventListener('click', () => {
        const id = b.dataset.id;
        if (!confirm('Delete this tweak?')) return;
        tweaks = tweaks.filter(t => t.id !== id);
        if (save()) { refreshCount(); renderPanel(); toast('Deleted'); }
      }));
      panelBody.querySelectorAll('.tweak-item-imgs img').forEach(img => {
        img.addEventListener('click', () => {
          const w = window.open();
          if (w) w.document.write('<img src="' + img.src + '" style="max-width:100%;">');
        });
      });
    }

    function buildMarkdown(opts) {
      opts = opts || {};
      const today = new Date().toLocaleDateString();
      const groups = {};
      tweaks.forEach(t => { const k = t.sectionLabel || '(no section)'; (groups[k] = groups[k] || []).push(t); });
      const lines = ['# Tweaks for ' + SITE_TITLE + ' — ' + today, '', 'Total: ' + tweaks.length + ' tweak' + (tweaks.length===1?'':'s') + '.', ''];
      let imgCounter = 0;
      const imageMap = [];
      Object.keys(groups).sort().forEach(k => {
        lines.push('## ' + k, '');
        groups[k].sort((a,b)=>a.ts-b.ts).forEach(t => {
          const pageInfo = t.page ? ' [page: ' + t.page + ']' : '';
          lines.push('- **' + new Date(t.ts).toLocaleString() + '**' + pageInfo + ' — ' + (t.note || '_(image only)_'));
          (t.screenshots || []).forEach(dataUrl => {
            imgCounter++;
            const m = dataUrl.match(/^data:image\/(\w+);base64,/) || [null, 'png'];
            const ext = m[1] === 'jpeg' ? 'jpg' : m[1];
            const filename = String(imgCounter).padStart(2, '0') + '.' + ext;
            imageMap.push({ idx: imgCounter, dataUrl, ext, filename });
            if (opts.embedBase64) lines.push('  ', '  ![screenshot ' + imgCounter + '](' + dataUrl + ')', '');
            else if (opts.imageFolderRef) lines.push('  ', '  ![screenshot ' + imgCounter + '](images/' + filename + ')', '');
            else lines.push('  _[screenshot ' + imgCounter + ' attached]_');
          });
        });
        lines.push('');
      });
      return { text: lines.join('\n'), imageMap };
    }

    function copyAllText() {
      if (!tweaks.length) { toast('Nothing to copy'); return; }
      const { text } = buildMarkdown();
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
    function downloadMd() {
      if (!tweaks.length) { toast('Nothing to download'); return; }
      const { text } = buildMarkdown({ embedBase64: true });
      const blob = new Blob([text], { type: 'text/markdown' });
      triggerDownload(blob, 'tweaks-' + datestamp() + '.md');
      toast('Downloaded .md');
    }
    function downloadZipFn() {
      if (!tweaks.length) { toast('Nothing to download'); return; }
      const { text, imageMap } = buildMarkdown({ imageFolderRef: true });
      const enc = new TextEncoder();
      const files = [{ name: 'TWEAKS.md', data: enc.encode(text) }];
      imageMap.forEach(im => {
        const bytes = base64ToBytes(im.dataUrl.split(',')[1]);
        files.push({ name: 'images/' + im.filename, data: bytes });
      });
      const blob = buildZip(files);
      triggerDownload(blob, 'tweaks-' + datestamp() + '.zip');
      toast('Downloaded ' + files.length + ' files');
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
    function base64ToBytes(b64) {
      const bin = atob(b64);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      return bytes;
    }
    const __crcTable = (() => {
      const t = new Uint32Array(256);
      for (let i = 0; i < 256; i++) {
        let c = i;
        for (let j = 0; j < 8; j++) c = (c & 1) ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
        t[i] = c;
      }
      return t;
    })();
    function crc32(data) {
      let c = 0xffffffff;
      for (let i = 0; i < data.length; i++) c = __crcTable[(c ^ data[i]) & 0xff] ^ (c >>> 8);
      return (c ^ 0xffffffff) >>> 0;
    }
    function buildZip(files) {
      const enc = new TextEncoder();
      const blobs = []; const central = [];
      let offset = 0;
      files.forEach(f => {
        const nameBytes = enc.encode(f.name);
        const crc = crc32(f.data); const size = f.data.length;
        const lh = new Uint8Array(30 + nameBytes.length);
        const lhv = new DataView(lh.buffer);
        lhv.setUint32(0, 0x04034b50, true);
        lhv.setUint16(4, 20, true); lhv.setUint16(6, 0, true); lhv.setUint16(8, 0, true);
        lhv.setUint16(10, 0, true); lhv.setUint16(12, 0, true);
        lhv.setUint32(14, crc, true); lhv.setUint32(18, size, true); lhv.setUint32(22, size, true);
        lhv.setUint16(26, nameBytes.length, true); lhv.setUint16(28, 0, true);
        lh.set(nameBytes, 30);
        blobs.push(lh, f.data);
        const cd = new Uint8Array(46 + nameBytes.length);
        const cdv = new DataView(cd.buffer);
        cdv.setUint32(0, 0x02014b50, true);
        cdv.setUint16(4, 20, true); cdv.setUint16(6, 20, true); cdv.setUint16(8, 0, true);
        cdv.setUint16(10, 0, true); cdv.setUint16(12, 0, true); cdv.setUint16(14, 0, true);
        cdv.setUint32(16, crc, true); cdv.setUint32(20, size, true); cdv.setUint32(24, size, true);
        cdv.setUint16(28, nameBytes.length, true); cdv.setUint16(30, 0, true);
        cdv.setUint16(32, 0, true); cdv.setUint16(34, 0, true); cdv.setUint16(36, 0, true);
        cdv.setUint32(38, 0, true); cdv.setUint32(42, offset, true);
        cd.set(nameBytes, 46);
        central.push(cd);
        offset += lh.length + size;
      });
      const centralStart = offset;
      let centralSize = 0;
      central.forEach(c => centralSize += c.length);
      const eocd = new Uint8Array(22);
      const ev = new DataView(eocd.buffer);
      ev.setUint32(0, 0x06054b50, true);
      ev.setUint16(4, 0, true); ev.setUint16(6, 0, true);
      ev.setUint16(8, files.length, true); ev.setUint16(10, files.length, true);
      ev.setUint32(12, centralSize, true); ev.setUint32(16, centralStart, true);
      ev.setUint16(20, 0, true);
      return new Blob([...blobs, ...central, eocd], { type: 'application/zip' });
    }

    function clearAll() {
      if (!tweaks.length) return;
      if (!confirm('Delete ALL ' + tweaks.length + ' tweaks?')) return;
      tweaks = []; save(); refreshCount(); renderPanel(); toast('Cleared');
    }
    function openPanel() {
      renderPanel();
      panelScrim.classList.add('open');
      panelScrim.setAttribute('aria-hidden', 'false');
      fab.classList.add('list-mode');
    }
    function closePanel() {
      panelScrim.classList.remove('open');
      panelScrim.setAttribute('aria-hidden', 'true');
      fab.classList.remove('list-mode');
    }

    let touchTimer = null;
    fab.addEventListener('click', e => { if (e.shiftKey) { openPanel(); return; } openModal(); });
    fab.addEventListener('contextmenu', e => { e.preventDefault(); openPanel(); });
    fab.addEventListener('touchstart', () => { touchTimer = setTimeout(() => { touchTimer = null; openPanel(); }, 600); });
    fab.addEventListener('touchend', () => { if (touchTimer) { clearTimeout(touchTimer); touchTimer = null; } });
    countEl.addEventListener('click', e => { e.stopPropagation(); openPanel(); });

    saveBtn.addEventListener('click', commitSave);
    cancelBtn.addEventListener('click', closeModal);
    deleteBtn.addEventListener('click', commitDelete);
    modalScrim.addEventListener('click', e => { if (e.target === modalScrim) closeModal(); });
    copyAllBtn.addEventListener('click', copyAllText);
    downloadMdBtn.addEventListener('click', downloadMd);
    downloadZipBtn.addEventListener('click', downloadZipFn);
    clearAllBtn.addEventListener('click', clearAll);
    panelCloseBtn.addEventListener('click', closePanel);
    panelScrim.addEventListener('click', e => { if (e.target === panelScrim) closePanel(); });

    noteEl.addEventListener('keydown', e => {
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
      if (e.key === 't' || e.key === 'T') { e.preventDefault(); openModal(); }
    });

    load();
    refreshCount();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
