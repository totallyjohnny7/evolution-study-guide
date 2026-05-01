/* mastery-heatmap.js — Visualize how well you've drilled each card.
 *
 * Reads window.FLASHCARD_DECKS + leitner-progress-v1 (your per-card state)
 * and renders:
 *
 *   - Compact: 18 stacked horizontal bars (one per lecture) showing the
 *     proportion of cards you've mastered (got_it / shaky / miss / unseen).
 *     Click a bar to open the modal pre-filtered to that lecture.
 *
 *   - Modal: full grid of every card as a colored cell, filterable by deck
 *     and state. Click a cell to drop into a 1-card Flash session for it.
 *
 * Public API: window.masteryMap = {
 *   compact(containerEl, opts?) -> void
 *   modal(opts?) -> void
 *   stats(deckId?) -> { total, got_it, shaky, miss, unseen, pct }
 *   close() -> void
 * }
 *
 * Side: updates DOM only. Reads localStorage but doesn't write.
 * Update on activity: caller should re-call compact() to refresh.
 */
(function () {
  'use strict';

  const KEY_PROGRESS = 'leitner-progress-v1';

  const STATE_COLORS = {
    got_it: '#5fa871',   // green
    shaky:  '#c89b2e',   // gold/amber
    miss:   '#c25d52',   // red
    unseen: '#3c4150',   // muted gray-blue
  };

  const STATE_LABELS = {
    got_it: 'Got it',
    shaky:  'Shaky',
    miss:   'Miss',
    unseen: 'Unseen',
  };

  const ACCENT = '#c89b2e';
  const INK = '#e6dfd0';
  const INK_DIM = '#a59a83';
  const INK_FAINT = '#6b6353';
  const RULE = '#22262f';
  const BG = '#14171d';
  const BG_SUNK = '#090a0e';

  // ============================================================ helpers

  function load(k, d) {
    try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); }
    catch (e) { return d; }
  }

  function cardKey(c) {
    return String(c?.term || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim().slice(0, 100);
  }

  function escHTML(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, c => (
      { '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]
    ));
  }

  function deckList() {
    const fc = window.FC_DECKS || [];
    return fc.filter(id => id !== 'all');
  }

  function lectureLabel(deckId) {
    const labels = window.FLASHCARD_LABELS || {};
    return labels[deckId] || deckId;
  }

  // Get [card, state] pairs for one deck, deduped by cardKey, preferring richer cards
  function deckCardStates(deckId) {
    const decks = window.FLASHCARD_DECKS || {};
    const arr = decks[deckId] || [];
    const progress = load(KEY_PROGRESS, {});
    const byKey = new Map();
    arr.forEach(c => {
      const k = cardKey(c);
      if (!k) return;
      const richness = (c.exAnswer ? 4 : 0) + (c.conceptId ? 2 : 0) + ((c.mnem || c.analogy) ? 2 : 0) + (c.cardType ? 1 : 0);
      const existing = byKey.get(k);
      if (!existing || richness > existing.richness) {
        byKey.set(k, { card: c, key: k, richness });
      }
    });
    const out = [];
    byKey.forEach(({ card, key }) => {
      const state = progress[key]?.state || 'unseen';
      const missCount = progress[key]?.missCount || 0;
      out.push({ card, key, state, missCount });
    });
    return out;
  }

  function statsForDeck(deckId) {
    const list = deckCardStates(deckId);
    const counts = { total: list.length, got_it: 0, shaky: 0, miss: 0, unseen: 0 };
    list.forEach(({ state }) => {
      counts[state] = (counts[state] || 0) + 1;
    });
    counts.pct = list.length === 0 ? 0 : Math.round((counts.got_it / list.length) * 100);
    return counts;
  }

  function statsAll() {
    const out = { total: 0, got_it: 0, shaky: 0, miss: 0, unseen: 0 };
    deckList().forEach(deckId => {
      const s = statsForDeck(deckId);
      out.total += s.total;
      out.got_it += s.got_it;
      out.shaky += s.shaky;
      out.miss += s.miss;
      out.unseen += s.unseen;
    });
    out.pct = out.total === 0 ? 0 : Math.round((out.got_it / out.total) * 100);
    return out;
  }

  // ============================================================ styles

  function injectStyles() {
    if (document.getElementById('mh-styles')) return;
    const css = document.createElement('style');
    css.id = 'mh-styles';
    css.textContent = `
      .mh-section {
        padding: 8px 16px 12px;
        border-top: 1px solid ${RULE};
      }
      .mh-section-head {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 8px;
      }
      .mh-section-title {
        font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em;
        color: ${INK_DIM}; font-weight: 600;
      }
      .mh-section-title strong { color: ${ACCENT}; font-weight: 700; }
      .mh-section-link {
        background: none; border: none;
        color: ${INK_DIM}; font-size: 10px; cursor: pointer;
        text-transform: uppercase; letter-spacing: 0.06em;
      }
      .mh-section-link:hover { color: ${ACCENT}; }
      .mh-overall {
        display: flex; gap: 8px; align-items: center; margin-bottom: 8px;
        font-size: 11px; color: ${INK_DIM};
      }
      .mh-overall-pct { font-size: 18px; font-weight: 700; color: ${ACCENT}; font-variant-numeric: tabular-nums; }
      .mh-overall-bar { flex: 1; height: 6px; border-radius: 3px; overflow: hidden; background: ${BG_SUNK}; display: flex; }
      .mh-overall-bar > div { height: 100%; }

      .mh-row {
        display: grid; grid-template-columns: 32px 1fr 50px;
        gap: 8px; align-items: center;
        padding: 4px 0;
        cursor: pointer;
        border-radius: 3px;
      }
      .mh-row:hover { background: ${BG_SUNK}; }
      .mh-row-id {
        font-size: 10px; font-weight: 700; color: ${INK_DIM};
        text-align: right; font-variant-numeric: tabular-nums;
      }
      .mh-row-bar {
        display: flex; height: 8px;
        border-radius: 2px; overflow: hidden;
        background: ${BG_SUNK};
      }
      .mh-row-bar > div { height: 100%; transition: width 0.4s; }
      .mh-row-counts {
        font-size: 10px; color: ${INK_FAINT};
        font-variant-numeric: tabular-nums;
      }
      .mh-row-counts strong { color: ${INK}; font-weight: 600; }

      .mh-legend {
        display: flex; gap: 10px; margin-top: 6px; font-size: 10px;
        color: ${INK_FAINT};
      }
      .mh-legend-item { display: flex; gap: 4px; align-items: center; }
      .mh-legend-dot { width: 8px; height: 8px; border-radius: 2px; }

      /* Modal */
      .mh-modal {
        position: fixed; inset: 0; z-index: 1100;
        background: rgba(8, 9, 14, 0.94);
        display: flex; flex-direction: column;
        font-family: 'Inter', system-ui, sans-serif;
        color: ${INK};
      }
      .mh-modal-head {
        padding: 16px 24px; border-bottom: 1px solid ${RULE};
        display: flex; justify-content: space-between; align-items: center;
        background: ${BG};
      }
      .mh-modal-title {
        font-family: 'Fraunces', Georgia, serif;
        font-size: 22px; font-weight: 600;
      }
      .mh-modal-x {
        background: none; border: none; color: ${INK_DIM};
        font-size: 24px; cursor: pointer; padding: 0 8px;
      }
      .mh-modal-x:hover { color: ${INK}; }
      .mh-modal-controls {
        padding: 12px 24px; border-bottom: 1px solid ${RULE};
        display: flex; gap: 12px; flex-wrap: wrap; align-items: center;
        background: ${BG};
      }
      .mh-filter-chip {
        background: ${BG_SUNK};
        color: ${INK_DIM};
        border: 1px solid ${RULE};
        border-radius: 14px;
        padding: 4px 12px;
        font-size: 11px;
        cursor: pointer;
        transition: all 0.15s;
      }
      .mh-filter-chip:hover { color: ${INK}; }
      .mh-filter-chip.active {
        color: #0c0e12;
        background: ${ACCENT};
        border-color: ${ACCENT};
        font-weight: 600;
      }
      .mh-modal-body {
        flex: 1; overflow-y: auto;
        padding: 20px 24px;
        background: ${BG};
      }
      .mh-deck-block { margin-bottom: 22px; }
      .mh-deck-head {
        display: flex; gap: 12px; align-items: baseline;
        margin-bottom: 6px;
      }
      .mh-deck-title {
        font-size: 14px; font-weight: 600; color: ${INK};
      }
      .mh-deck-meta {
        font-size: 11px; color: ${INK_FAINT};
        font-variant-numeric: tabular-nums;
      }
      .mh-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
        gap: 6px;
      }
      .mh-cell {
        font-size: 11px; line-height: 1.3;
        padding: 8px 10px;
        border-radius: 4px;
        cursor: pointer;
        border: 1px solid transparent;
        background: ${BG_SUNK};
        color: ${INK_DIM};
        position: relative;
        overflow: hidden;
      }
      .mh-cell:hover {
        border-color: ${ACCENT};
        color: ${INK};
      }
      .mh-cell.s-got_it { border-left: 3px solid ${STATE_COLORS.got_it}; }
      .mh-cell.s-shaky  { border-left: 3px solid ${STATE_COLORS.shaky}; }
      .mh-cell.s-miss   { border-left: 3px solid ${STATE_COLORS.miss}; }
      .mh-cell.s-unseen { border-left: 3px solid ${STATE_COLORS.unseen}; }
      .mh-cell-term {
        font-weight: 500;
        color: ${INK};
        max-height: 2.6em; overflow: hidden;
      }
      .mh-cell-meta {
        font-size: 9px; color: ${INK_FAINT};
        text-transform: uppercase; letter-spacing: 0.06em;
        margin-top: 4px;
      }
      .mh-modal-foot {
        padding: 10px 24px; border-top: 1px solid ${RULE};
        background: ${BG};
        display: flex; justify-content: space-between; align-items: center;
        font-size: 11px; color: ${INK_FAINT};
      }
      .mh-modal-foot strong { color: ${ACCENT}; }
    `;
    document.head.appendChild(css);
  }

  // ============================================================ compact

  function renderCompact(container, opts) {
    if (!container) return;
    injectStyles();
    opts = opts || {};
    const overall = statsAll();

    const overallBar = `
      <div class="mh-overall-bar">
        <div style="width:${(overall.got_it / Math.max(1,overall.total)) * 100}%; background:${STATE_COLORS.got_it}"></div>
        <div style="width:${(overall.shaky / Math.max(1,overall.total)) * 100}%; background:${STATE_COLORS.shaky}"></div>
        <div style="width:${(overall.miss / Math.max(1,overall.total)) * 100}%; background:${STATE_COLORS.miss}"></div>
        <div style="width:${(overall.unseen / Math.max(1,overall.total)) * 100}%; background:${STATE_COLORS.unseen}"></div>
      </div>
    `;

    const decks = deckList();
    const rows = decks.map(deckId => {
      const s = statsForDeck(deckId);
      const total = Math.max(1, s.total);
      const seg = (n, color) => `<div style="width:${(n/total)*100}%; background:${color}"></div>`;
      return `
        <div class="mh-row" data-deck="${escHTML(deckId)}">
          <div class="mh-row-id">${escHTML(deckId)}</div>
          <div class="mh-row-bar">
            ${seg(s.got_it, STATE_COLORS.got_it)}
            ${seg(s.shaky, STATE_COLORS.shaky)}
            ${seg(s.miss, STATE_COLORS.miss)}
            ${seg(s.unseen, STATE_COLORS.unseen)}
          </div>
          <div class="mh-row-counts"><strong>${s.got_it}</strong>/${s.total}</div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="mh-section-head">
        <span class="mh-section-title">Mastery · <strong>${overall.pct}%</strong></span>
        <button class="mh-section-link" id="mhOpenModal">View all ▸</button>
      </div>
      <div class="mh-overall">
        <span class="mh-overall-pct">${overall.pct}%</span>
        ${overallBar}
      </div>
      <div class="mh-rows">${rows}</div>
      <div class="mh-legend">
        <span class="mh-legend-item"><span class="mh-legend-dot" style="background:${STATE_COLORS.got_it}"></span>Got it</span>
        <span class="mh-legend-item"><span class="mh-legend-dot" style="background:${STATE_COLORS.shaky}"></span>Shaky</span>
        <span class="mh-legend-item"><span class="mh-legend-dot" style="background:${STATE_COLORS.miss}"></span>Miss</span>
        <span class="mh-legend-item"><span class="mh-legend-dot" style="background:${STATE_COLORS.unseen}"></span>New</span>
      </div>
    `;

    // Wire row clicks → open modal pre-filtered to that deck
    container.querySelectorAll('.mh-row').forEach(el => {
      el.addEventListener('click', () => {
        openModal({ deckId: el.dataset.deck });
      });
    });
    const openBtn = container.querySelector('#mhOpenModal');
    if (openBtn) openBtn.addEventListener('click', () => openModal({}));
  }

  // ============================================================ modal

  function openModal(opts) {
    opts = opts || {};
    injectStyles();
    closeModal();

    const wrap = document.createElement('div');
    wrap.id = 'mhModal';
    wrap.className = 'mh-modal';
    document.body.appendChild(wrap);

    const filters = { state: 'all', deckId: opts.deckId || 'all' };
    const overall = statsAll();

    function render() {
      const decks = deckList();
      const filteredDecks = filters.deckId === 'all' ? decks : [filters.deckId];

      const stateChip = (key, label, count) => `
        <button class="mh-filter-chip ${filters.state === key ? 'active' : ''}" data-state="${key}">
          ${label} ${count != null ? `· ${count}` : ''}
        </button>`;

      const deckChip = (id, label) => `
        <button class="mh-filter-chip ${filters.deckId === id ? 'active' : ''}" data-deck="${id}">
          ${escHTML(label)}
        </button>`;

      const blocks = filteredDecks.map(deckId => {
        const cards = deckCardStates(deckId);
        const visible = filters.state === 'all' ? cards : cards.filter(c => c.state === filters.state);
        if (visible.length === 0 && filters.state !== 'all') return '';
        const stats = statsForDeck(deckId);
        const cells = visible.map(({ card, key, state, missCount }) => `
          <div class="mh-cell s-${state}" data-key="${escHTML(key)}" title="${escHTML(card.term || '')} — ${STATE_LABELS[state]}">
            <div class="mh-cell-term">${escHTML(card.term || '').slice(0, 90)}</div>
            <div class="mh-cell-meta">${STATE_LABELS[state]}${missCount > 0 ? ` · ${missCount} miss` : ''}</div>
          </div>
        `).join('');
        return `
          <div class="mh-deck-block">
            <div class="mh-deck-head">
              <span class="mh-deck-title">${escHTML(lectureLabel(deckId))}</span>
              <span class="mh-deck-meta">${stats.got_it}/${stats.total} mastered · ${visible.length} shown</span>
            </div>
            <div class="mh-grid">${cells}</div>
          </div>
        `;
      }).filter(Boolean).join('');

      wrap.innerHTML = `
        <div class="mh-modal-head">
          <span class="mh-modal-title">Mastery — ${overall.pct}% (${overall.got_it}/${overall.total})</span>
          <button class="mh-modal-x" id="mhX" title="Close (Esc)">×</button>
        </div>
        <div class="mh-modal-controls">
          <span style="color:${INK_FAINT}; font-size:10px; text-transform:uppercase; letter-spacing:0.08em">State:</span>
          ${stateChip('all', 'All')}
          ${stateChip('got_it', 'Got it', overall.got_it)}
          ${stateChip('shaky', 'Shaky', overall.shaky)}
          ${stateChip('miss', 'Miss', overall.miss)}
          ${stateChip('unseen', 'New', overall.unseen)}
        </div>
        <div class="mh-modal-controls" style="border-top: none">
          <span style="color:${INK_FAINT}; font-size:10px; text-transform:uppercase; letter-spacing:0.08em">Deck:</span>
          ${deckChip('all', 'All decks')}
          ${decks.map(id => deckChip(id, id)).join('')}
        </div>
        <div class="mh-modal-body">${blocks || '<div style="text-align:center; padding:40px; color:#a59a83">No cards match the current filters.</div>'}</div>
        <div class="mh-modal-foot">
          <span>Click a card to drill it. Esc to close.</span>
          <span><strong>${overall.got_it}</strong> got it · <strong>${overall.shaky}</strong> shaky · <strong>${overall.miss}</strong> miss · <strong>${overall.unseen}</strong> new</span>
        </div>
      `;

      wrap.querySelector('#mhX').addEventListener('click', closeModal);
      wrap.querySelectorAll('[data-state]').forEach(el => {
        el.addEventListener('click', () => { filters.state = el.dataset.state; render(); });
      });
      wrap.querySelectorAll('[data-deck]').forEach(el => {
        el.addEventListener('click', () => { filters.deckId = el.dataset.deck; render(); });
      });
      wrap.querySelectorAll('.mh-cell').forEach(el => {
        el.addEventListener('click', () => {
          const key = el.dataset.key;
          drillCard(key);
        });
      });
    }
    render();

    // Esc closes modal
    function escHandler(e) {
      if (e.key === 'Escape') { closeModal(); document.removeEventListener('keydown', escHandler); }
    }
    document.addEventListener('keydown', escHandler);
  }

  function closeModal() {
    const m = document.getElementById('mhModal');
    if (m) m.remove();
  }

  // Drill a single card: stash a 1-card "boss" deck in localStorage so the
  // Leitner system picks it up when started.
  function drillCard(cardKeyStr) {
    // Find the card
    const decks = window.FLASHCARD_DECKS || {};
    let foundCard = null, foundDeck = null;
    for (const id in decks) {
      if (id === 'all') continue;
      const arr = decks[id] || [];
      for (const c of arr) {
        if (cardKey(c) === cardKeyStr) { foundCard = c; foundDeck = id; break; }
      }
      if (foundCard) break;
    }
    if (!foundCard) return;
    closeModal();
    // Pre-set the Leitner setup for the matching deck and 10-min session
    try {
      localStorage.setItem('leitner-settings-v1', JSON.stringify({ deckId: foundDeck, minutes: 10 }));
    } catch (e) {}
    const flash = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Flash');
    if (flash) flash.click();
  }

  // ============================================================ export

  window.masteryMap = {
    compact: renderCompact,
    modal: openModal,
    close: closeModal,
    stats: statsForDeck,
    statsAll: statsAll,
  };

  console.log('[mastery-heatmap] loaded — masteryMap.modal() / .stats(deckId)');
})();
