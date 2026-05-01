/* leitner-session.js — Compressed in-session Leitner-style flashcards.
 *
 * Replaces FSRS interval scheduling with a session loop:
 *  - 3-button grading (1=Miss, 2=Shaky, 3=Got it)
 *  - Re-queue on Miss (~+4) and Shaky (~+12)
 *  - Got it leaves session, parked for tomorrow
 *  - Session timer 10 / 20 / 30 min, counts down
 *  - Trap cards every ~12 cards (auto-MC from recent misses)
 *  - Triple-miss rescue
 *  - End-of-session: stats, top misses, Boss Mode, tomorrow's deck builder
 *  - Persistence: every action saved; resume on page reopen
 *
 * Storage:
 *  leitner-progress-v1   per-card state across sessions (state, missCount, lastSeen)
 *  leitner-session-v1    live session for resume
 *  leitner-history-v1    rolling stats + tomorrow's deck seeds
 *  leitner-settings-v1   last-used deck + minutes
 */
(function () {
  'use strict';

  const KEYS = {
    PROGRESS: 'leitner-progress-v1',
    SESSION:  'leitner-session-v1',
    HISTORY:  'leitner-history-v1',
    SETTINGS: 'leitner-settings-v1',
  };

  // ============================================================ utility

  function cardKey(c) {
    return (c?.term || '')
      .replace(/<[^>]+>/g, '')
      .replace(/\s+/g, ' ')
      .trim()
      .slice(0, 100);
  }

  function shuffle(a) {
    const x = a.slice();
    for (let i = x.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [x[i], x[j]] = [x[j], x[i]];
    }
    return x;
  }

  function loadJSON(k, d) {
    try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); }
    catch (e) { return d; }
  }
  function saveJSON(k, v) {
    try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {}
  }

  function fmtTime(ms) {
    if (!isFinite(ms) || ms <= 0) return '0:00';
    const s = Math.ceil(ms / 1000);
    const m = Math.floor(s / 60);
    const r = s - m * 60;
    return m + ':' + (r < 10 ? '0' + r : r);
  }

  function escHTML(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, c => (
      { '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]
    ));
  }

  function findCardByKey(key) {
    const decks = window.FLASHCARD_DECKS || {};
    for (const id in decks) {
      if (id === 'all' || !Array.isArray(decks[id])) continue;
      for (const c of decks[id]) {
        if (cardKey(c) === key) return c;
      }
    }
    return null;
  }

  function reinsertOffset(target, jitter) {
    const min = Math.max(2, target - jitter);
    const max = target + jitter;
    return min + Math.floor(Math.random() * (max - min + 1));
  }

  // ============================================================ migration

  function migrateOnce() {
    if (localStorage.getItem(KEYS.PROGRESS)) return;
    const out = {};

    try {
      const v2 = JSON.parse(localStorage.getItem('biol-fc-progress-v2') || '{}');
      Object.entries(v2).forEach(([k, v]) => {
        if (v === 'missed') out[k] = { state: 'miss', missCount: 1, lastSeen: 0 };
        else if (v === 'known') out[k] = { state: 'got_it', missCount: 0, lastSeen: 0 };
      });
    } catch (e) {}

    try {
      const v1 = JSON.parse(localStorage.getItem('evol-fc-progress-v1') || '{}');
      Object.values(v1).forEach(deckMap => {
        Object.entries(deckMap || {}).forEach(([k, v]) => {
          if (out[k]) return;
          if (v === 'missed') out[k] = { state: 'miss', missCount: 1, lastSeen: 0 };
          else if (v === 'known') out[k] = { state: 'got_it', missCount: 0, lastSeen: 0 };
        });
      });
    } catch (e) {}

    saveJSON(KEYS.PROGRESS, out);
  }

  // ============================================================ progress

  let progress = {};
  function loadProgress() { progress = loadJSON(KEYS.PROGRESS, {}); }
  function saveProgress() { saveJSON(KEYS.PROGRESS, progress); }

  function getCardState(card) {
    return progress[cardKey(card)] || { state: 'unseen', missCount: 0, lastSeen: 0 };
  }
  function setCardState(card, patch) {
    const k = cardKey(card);
    progress[k] = Object.assign({}, getCardState(card), patch, { lastSeen: Date.now() });
    saveProgress();
  }

  // ============================================================ session

  let S = null;
  let saveDebounceId = null;

  function persistSession() {
    if (!S) { localStorage.removeItem(KEYS.SESSION); return; }
    if (saveDebounceId) clearTimeout(saveDebounceId);
    saveDebounceId = setTimeout(() => saveJSON(KEYS.SESSION, S), 200);
  }
  function clearSession() {
    S = null;
    localStorage.removeItem(KEYS.SESSION);
  }
  function hasSavedSession() {
    const s = loadJSON(KEYS.SESSION, null);
    if (!s || !Array.isArray(s.queue) || !s.queue.length) return false;
    if (s.endedAt) return false;
    if ((s.remainingMs || 0) <= 0) return false;
    return true;
  }

  function getDeckCards(deckId) {
    const decks = window.FLASHCARD_DECKS || {};
    if (deckId === 'all') {
      const out = [];
      const seen = new Set();
      Object.entries(decks).forEach(([id, arr]) => {
        if (id === 'all' || !Array.isArray(arr)) return;
        arr.forEach(c => {
          const k = cardKey(c);
          if (!k) return;
          if (!seen.has(k)) { seen.add(k); out.push(c); }
        });
      });
      return out;
    }
    return (decks[deckId] || []).slice();
  }

  function buildQueue(deckId, mode) {
    const all = getDeckCards(deckId);
    const hist = loadJSON(KEYS.HISTORY, {});

    if (mode === 'boss') {
      const failKeys = new Set([
        ...(hist.todayMisses || []),
        ...(hist.todayShakies || []),
      ]);
      return all
        .filter(c => failKeys.has(cardKey(c)))
        .map(c => ({ card: c, sessionMisses: 0, isNew: false }));
    }

    const buckets = { miss: [], shaky: [], unseen: [], got_it: [] };
    all.forEach(c => {
      const s = (getCardState(c).state) || 'unseen';
      (buckets[s] || buckets.unseen).push(c);
    });

    let queue = [
      ...shuffle(buckets.miss),
      ...shuffle(buckets.shaky),
      ...shuffle(buckets.unseen),
    ];

    if (queue.length < 3 && buckets.got_it.length) {
      queue = queue.concat(shuffle(buckets.got_it));
    }

    return queue.map(c => ({
      card: c,
      sessionMisses: 0,
      isNew: getCardState(c).state === 'unseen',
    }));
  }

  function startSession(deckId, minutes, mode) {
    mode = mode || 'normal';
    const queue = buildQueue(deckId, mode);
    if (!queue.length) {
      alert('No cards to study in this deck.');
      return;
    }
    S = {
      deckId,
      mode,
      minutes,
      startedAt: Date.now(),
      endsAt:    Date.now() + minutes * 60 * 1000,
      remainingMs: minutes * 60 * 1000,
      pausedAt:  null,

      queue,
      currentIdx: 0,
      flipped:    false,

      cardSeen:       0,
      firstTryGotIt:  0,
      streak:         0,
      bestStreak:     0,

      missCounts:      {},
      todayMisses:     [],
      todayShakies:    [],
      todayGotIt:      [],

      cardsSinceTrap:       0,
      cardsSinceBreakCheck: 0,
      breakOfferedAt8:      false,
      breakForcedAt8:       false,

      history:        [],
      currentTrap:    null,
      currentRescue:  null,

      endedAt:   null,
      endReason: null,
      version:   1,
    };
    persistSession();
    UI.startTimerLoop();
    UI.render();
  }

  function resumeSession() {
    const saved = loadJSON(KEYS.SESSION, null);
    if (!saved) return false;
    S = saved;
    if (S.pausedAt) {
      // stay paused; render will reflect
    } else {
      S.endsAt = Date.now() + (S.remainingMs || 0);
    }
    UI.startTimerLoop();
    UI.render();
    return true;
  }

  function tickTimer() {
    if (!S || S.endedAt) return;
    if (S.pausedAt) return;
    S.remainingMs = Math.max(0, S.endsAt - Date.now());
    const el = document.getElementById('lzTimer');
    if (el) el.textContent = fmtTime(S.remainingMs);
    if (S.remainingMs <= 0) {
      endSession('timer');
    }
  }

  function endSession(reason) {
    if (!S) return;
    S.endedAt = Date.now();
    S.endReason = reason;

    saveProgress();

    const hist = loadJSON(KEYS.HISTORY, {});
    hist.todayMisses    = S.todayMisses;
    hist.todayShakies   = S.todayShakies;
    hist.lastSessionEnd = Date.now();
    hist.totalCardsSeen = (hist.totalCardsSeen || 0) + S.cardSeen;
    hist.totalSessions  = (hist.totalSessions || 0) + 1;
    saveJSON(KEYS.HISTORY, hist);

    persistSession();
    UI.renderEnd();
  }

  function pauseSession() {
    if (!S || S.pausedAt) return;
    S.pausedAt = Date.now();
    persistSession();
  }
  function unpauseSession() {
    if (!S || !S.pausedAt) return;
    const pausedFor = Date.now() - S.pausedAt;
    S.endsAt += pausedFor;
    S.pausedAt = null;
    persistSession();
  }

  function currentItem() {
    if (!S || !S.queue || !S.queue.length) return null;
    if (S.currentIdx >= S.queue.length) S.currentIdx = 0;
    return S.queue[S.currentIdx] || null;
  }

  // ============================================================ actions

  function flip() {
    if (!S || S.endedAt) return;
    if (S.currentTrap || S.currentRescue) return;
    S.flipped = !S.flipped;
    persistSession();
    UI.renderCard();
  }

  function grade(rating) {
    if (!S || S.endedAt) return;
    if (!S.flipped) return;                    // gating: must flip first
    if (S.currentTrap || S.currentRescue) return;
    if (rating !== 1 && rating !== 2 && rating !== 3) return;

    const item = currentItem();
    if (!item) return;
    const k = cardKey(item.card);

    // Snapshot for undo
    S.history.push({
      action: 'grade',
      rating,
      currentIdx:           S.currentIdx,
      flipped:              true,
      streak:               S.streak,
      bestStreak:           S.bestStreak,
      cardSeen:             S.cardSeen,
      firstTryGotIt:        S.firstTryGotIt,
      cardsSinceTrap:       S.cardsSinceTrap,
      cardsSinceBreakCheck: S.cardsSinceBreakCheck,
      itemSnap:             { card: item.card, sessionMisses: item.sessionMisses, isNew: item.isNew },
      missCount:            S.missCounts[k] || 0,
      prevProgress:         Object.assign({}, getCardState(item.card)),
      addedToMisses:        false,
      addedToShakies:       false,
      addedToGotIt:         false,
    });
    if (S.history.length > 20) S.history.shift();
    const snap = S.history[S.history.length - 1];

    S.cardSeen++;
    S.cardsSinceTrap++;
    S.cardsSinceBreakCheck++;

    // Remove current item from queue first
    S.queue.splice(S.currentIdx, 1);

    if (rating === 1) {
      // Miss
      S.missCounts[k] = (S.missCounts[k] || 0) + 1;
      item.sessionMisses++;
      S.streak = 0;
      if (!S.todayMisses.includes(k)) {
        S.todayMisses.push(k);
        snap.addedToMisses = true;
      }
      const offset = reinsertOffset(4, 1);
      const insertAt = Math.min(S.queue.length, S.currentIdx + offset);
      S.queue.splice(insertAt, 0, item);
      setCardState(item.card, {
        state: 'miss',
        missCount: (getCardState(item.card).missCount || 0) + 1,
      });

      if (S.missCounts[k] >= 3 && !S.currentRescue) {
        S.currentRescue = { key: k, card: item.card };
        S.flipped = false;
        if (S.currentIdx >= S.queue.length) S.currentIdx = 0;
        persistSession();
        UI.render();
        return;
      }
    } else if (rating === 2) {
      // Shaky
      item.sessionMisses++;
      S.streak = 0;
      if (!S.todayShakies.includes(k) && !S.todayMisses.includes(k)) {
        S.todayShakies.push(k);
        snap.addedToShakies = true;
      }
      const offset = reinsertOffset(12, 2);
      const insertAt = Math.min(S.queue.length, S.currentIdx + offset);
      S.queue.splice(insertAt, 0, item);
      setCardState(item.card, { state: 'shaky' });
    } else {
      // Got it
      if (item.sessionMisses === 0) {
        S.firstTryGotIt++;
        S.streak++;
        if (S.streak > S.bestStreak) S.bestStreak = S.streak;
      } else {
        S.streak = 0;
      }
      S.todayGotIt.push(k);
      snap.addedToGotIt = true;
      setCardState(item.card, { state: 'got_it' });
    }

    S.flipped = false;
    if (S.currentIdx >= S.queue.length) S.currentIdx = 0;

    if (S.queue.length === 0) {
      endSession('clear');
      return;
    }

    maybeOfferBreak();
    maybeInjectTrap();

    persistSession();
    UI.render();
  }

  function skip() {
    if (!S || S.endedAt) return;
    if (S.currentTrap || S.currentRescue) return;
    if (!S.queue.length || S.queue.length === 1) return;
    const item = S.queue.splice(S.currentIdx, 1)[0];
    S.queue.push(item);
    S.flipped = false;
    if (S.currentIdx >= S.queue.length) S.currentIdx = 0;
    persistSession();
    UI.render();
  }

  function undo() {
    if (!S || !S.history.length) return;
    const h = S.history.pop();
    if (h.action !== 'grade') return;

    const k = cardKey(h.itemSnap.card);

    // Roll back scalars
    S.cardSeen             = h.cardSeen;
    S.firstTryGotIt        = h.firstTryGotIt;
    S.streak               = h.streak;
    S.bestStreak           = h.bestStreak;
    S.cardsSinceTrap       = h.cardsSinceTrap;
    S.cardsSinceBreakCheck = h.cardsSinceBreakCheck;
    S.missCounts[k]        = h.missCount;

    // Roll back today lists if this action added them
    if (h.addedToMisses)  { const i = S.todayMisses.lastIndexOf(k);  if (i >= 0) S.todayMisses.splice(i, 1); }
    if (h.addedToShakies) { const i = S.todayShakies.lastIndexOf(k); if (i >= 0) S.todayShakies.splice(i, 1); }
    if (h.addedToGotIt)   { const i = S.todayGotIt.lastIndexOf(k);   if (i >= 0) S.todayGotIt.splice(i, 1); }

    // Restore the item at the original currentIdx (remove copies, then insert)
    S.queue = S.queue.filter(it => cardKey(it.card) !== k);
    const idx = Math.min(h.currentIdx, S.queue.length);
    S.queue.splice(idx, 0, h.itemSnap);
    S.currentIdx = idx;
    S.flipped = h.flipped;

    // Restore persistent state
    progress[k] = h.prevProgress;
    saveProgress();

    S.currentRescue = null;
    persistSession();
    UI.render();
  }

  // ============================================================ trap cards

  function maybeInjectTrap() {
    if (!S || S.mode === 'boss') return;
    if (S.cardsSinceTrap < 12) return;
    const recent = S.todayMisses.slice(-6);
    if (recent.length < 2) return;

    const a = findCardByKey(recent[recent.length - 1]);
    let b = null;
    for (let i = recent.length - 2; i >= 0; i--) {
      const c = findCardByKey(recent[i]);
      if (c && cardKey(c) !== cardKey(a)) { b = c; break; }
    }
    if (!a || !b) return;

    // 50/50 which order
    const correctIsA = Math.random() < 0.5;
    S.currentTrap = {
      promptCard: a,
      decoyCard:  b,
      correctIsA,
      answeredCorrectly: null,
    };
    S.cardsSinceTrap = 0;
  }

  function answerTrap(picked) {
    if (!S || !S.currentTrap) return;
    const correct = (picked === 'A' && S.currentTrap.correctIsA) ||
                    (picked === 'B' && !S.currentTrap.correctIsA);
    S.currentTrap.answeredCorrectly = correct;
    persistSession();
    UI.renderTrap();
    if (correct) {
      setTimeout(() => {
        if (!S) return;
        S.currentTrap = null;
        persistSession();
        UI.render();
      }, 850);
    } else {
      // Inject a comparison card next
      const t = S.currentTrap;
      const compCard = {
        term: 'Compare: ' + (t.promptCard.term || '') + ' vs ' + (t.decoyCard.term || ''),
        def:
          '<div style="margin-bottom:12px"><b>' + (t.promptCard.term || '') + ':</b> ' + (t.promptCard.def || '') + '</div>' +
          '<div><b>' + (t.decoyCard.term || '') + ':</b> ' + (t.decoyCard.def || '') + '</div>',
        ctx: 'Comparison · auto-injected after trap miss',
      };
      const insertAt = Math.min(S.queue.length, S.currentIdx);
      S.queue.splice(insertAt, 0, { card: compCard, sessionMisses: 0, isNew: false });
      setTimeout(() => {
        if (!S) return;
        S.currentTrap = null;
        persistSession();
        UI.render();
      }, 1500);
    }
  }

  // ============================================================ pacing

  function maybeOfferBreak() {
    if (!S) return;
    const elapsedSec = (Date.now() - S.startedAt) / 1000;
    if (elapsedSec < 8 * 60) return;
    if (S.breakOfferedAt8 || S.breakForcedAt8) return;

    const rate = S.cardSeen > 0 ? S.firstTryGotIt / S.cardSeen : 1;
    if (rate < 0.6) {
      S.breakForcedAt8 = true;
      pauseSession();
      UI.showForcedBreak();
    } else if (rate < 0.75) {
      S.breakOfferedAt8 = true;
      UI.showSoftBreakOffer();
    }
  }

  // ============================================================ UI

  const UI = {
    timerLoopId: null,

    startTimerLoop() {
      if (UI.timerLoopId) clearInterval(UI.timerLoopId);
      UI.timerLoopId = setInterval(tickTimer, 250);
    },
    stopTimerLoop() {
      if (UI.timerLoopId) { clearInterval(UI.timerLoopId); UI.timerLoopId = null; }
    },

    ensureRoot() {
      if (document.getElementById('lzRoot')) return;
      const root = document.createElement('div');
      root.id = 'lzRoot';
      root.className = 'lz-root';
      document.body.appendChild(root);

      const modal = document.createElement('div');
      modal.id = 'lzModalRoot';
      modal.className = 'lz-modal-root';
      modal.style.display = 'none';
      document.body.appendChild(modal);
    },

    render() {
      UI.ensureRoot();
      const root = document.getElementById('lzRoot');
      if (!root) return;

      if (!S) {
        UI.renderSetup();
        return;
      }
      if (S.endedAt) {
        UI.renderEnd();
        return;
      }
      root.innerHTML = UI.html.session();
      UI.renderCard();
      UI.bindCardActions();

      if (S.pausedAt) {
        const pb = document.getElementById('lzPause');
        if (pb) pb.textContent = '▶';
      }

      const modal = document.getElementById('lzModalRoot');
      if (modal) { modal.style.display = 'none'; modal.innerHTML = ''; }

      if (S.currentRescue) UI.renderRescue();
      else if (S.currentTrap) UI.renderTrap();
    },

    renderSetup() {
      const root = document.getElementById('lzRoot');
      if (!root) return;
      const decks = window.FLASHCARD_DECKS || {};
      const labels = window.FLASHCARD_LABELS || {};
      const lectureIds = (window.FC_DECKS || []).filter(id => id !== 'all');
      const settings = loadJSON(KEYS.SETTINGS, { deckId: 'all', minutes: 20 });

      let resumeBlock = '';
      if (hasSavedSession()) {
        const s = loadJSON(KEYS.SESSION, {}) || {};
        resumeBlock = `
          <div class="lz-resume">
            <h3>Resume previous session?</h3>
            <div class="lz-resume-meta">
              ${(s.cardSeen || 0)} cards seen · ${Array.isArray(s.queue) ? s.queue.length : 0} left · ${fmtTime(s.remainingMs || 0)} on the clock
            </div>
            <div class="lz-resume-buttons">
              <button class="lz-btn lz-btn-primary" id="lzResume">Resume</button>
              <button class="lz-btn lz-btn-ghost" id="lzDiscard">Start over</button>
            </div>
          </div>
        `;
      }

      const deckOpts = ['all', ...lectureIds].map(id => {
        const lbl = labels[id] || id;
        const n = (decks[id] || []).length;
        const sel = id === settings.deckId ? 'selected' : '';
        const dis = n === 0 ? 'disabled' : '';
        return `<option value="${escHTML(id)}" ${sel} ${dis}>${escHTML(lbl)}${n ? ' · ' + n : ' · empty'}</option>`;
      }).join('');

      const minOpts = [10, 20, 30].map(m =>
        `<button type="button" class="lz-time-chip ${m === settings.minutes ? 'active' : ''}" data-min="${m}">${m} min</button>`
      ).join('');

      root.innerHTML = `
        <div class="lz-setup">
          <header class="lz-setup-head">
            <h2>Session</h2>
            <button class="lz-icon-btn lz-close" id="lzCloseSetup" title="Close (Esc)">×</button>
          </header>
          ${resumeBlock}
          <div class="lz-setup-body">
            <label class="lz-field">
              <span class="lz-field-label">Deck</span>
              <select id="lzDeck" class="lz-select">${deckOpts}</select>
            </label>
            <label class="lz-field">
              <span class="lz-field-label">Length</span>
              <div class="lz-time-chips" id="lzTimeChips">${minOpts}</div>
            </label>
            <button class="lz-btn lz-btn-primary lz-btn-go" id="lzStart">Start session</button>
            <p class="lz-setup-hint">
              <kbd>1</kbd> Miss · <kbd>2</kbd> Shaky · <kbd>3</kbd> Got it · <kbd>Space</kbd> flip · <kbd>U</kbd> undo · <kbd>J</kbd> skip
            </p>
          </div>
        </div>
      `;

      const close = document.getElementById('lzCloseSetup');
      if (close) close.addEventListener('click', () => UI.exit());

      document.querySelectorAll('#lzTimeChips .lz-time-chip').forEach(c => {
        c.addEventListener('click', () => {
          document.querySelectorAll('#lzTimeChips .lz-time-chip').forEach(x => x.classList.remove('active'));
          c.classList.add('active');
        });
      });

      const startBtn = document.getElementById('lzStart');
      if (startBtn) startBtn.addEventListener('click', () => {
        const deckId = document.getElementById('lzDeck').value;
        const activeChip = document.querySelector('#lzTimeChips .lz-time-chip.active');
        const minutes = parseInt(activeChip ? activeChip.dataset.min : '20', 10);
        saveJSON(KEYS.SETTINGS, { deckId, minutes });
        clearSession();
        startSession(deckId, minutes, 'normal');
      });

      const resumeBtn = document.getElementById('lzResume');
      if (resumeBtn) resumeBtn.addEventListener('click', () => { resumeSession(); });

      const discardBtn = document.getElementById('lzDiscard');
      if (discardBtn) discardBtn.addEventListener('click', () => {
        clearSession();
        UI.renderSetup();
      });
    },

    renderCard() {
      const item = currentItem();
      if (!item) return;
      const card = item.card;

      const qEl = document.getElementById('lzQuestion');
      const aEl = document.getElementById('lzAnswer');
      const eEl = document.getElementById('lzExample');
      const mEl = document.getElementById('lzMnemonic');
      const cEl = document.getElementById('lzCtx');
      const flipBtn = document.getElementById('lzFlip');
      const counterEl = document.getElementById('lzCounter');
      const streakEl = document.getElementById('lzStreak');

      if (qEl) qEl.innerHTML = card.term || '';
      if (cEl) cEl.textContent = card.ctx || '';

      if (counterEl) {
        const seen = S.cardSeen + 1;
        counterEl.textContent = `Card ${seen} · ${S.queue.length} left`;
      }
      if (streakEl) streakEl.innerHTML = `<span class="lz-streak-flame">🔥</span><span class="lz-streak-num">${S.streak}</span>`;

      const card3d = document.getElementById('lzCard');
      if (card3d) card3d.classList.toggle('lz-flipped', !!S.flipped);

      if (S.flipped) {
        if (aEl) {
          aEl.innerHTML = card.def || '';
          aEl.style.display = '';
        }
        const exHTML = card.example;
        if (exHTML && eEl) {
          eEl.innerHTML = '<span class="lz-example-label">Apply it</span>' + exHTML;
          eEl.style.display = '';
        } else if (eEl) {
          eEl.style.display = 'none';
        }
        const mnemHTML = card.mnem || card.mnemonic;
        const analHTML = card.analogy;
        if (mnemHTML && mEl) {
          mEl.innerHTML = '<span class="lz-mnem-label">Mnemonic</span>' + mnemHTML;
          mEl.style.display = '';
        } else if (analHTML && mEl) {
          mEl.innerHTML = '<span class="lz-mnem-label">Analogy</span>' + analHTML;
          mEl.style.display = '';
        } else if (mEl) {
          mEl.style.display = 'none';
        }
        if (flipBtn) flipBtn.textContent = 'Hide answer';
      } else {
        if (aEl) aEl.style.display = 'none';
        if (eEl) eEl.style.display = 'none';
        if (mEl) mEl.style.display = 'none';
        if (flipBtn) flipBtn.textContent = 'Flip (Space)';
      }

      ['lzGrade1','lzGrade2','lzGrade3'].forEach(id => {
        const b = document.getElementById(id);
        if (b) b.disabled = !S.flipped;
      });

      const tEl = document.getElementById('lzTimer');
      if (tEl) tEl.textContent = fmtTime(S.remainingMs);
    },

    bindCardActions() {
      const card = document.getElementById('lzCard');
      if (card) {
        card.addEventListener('click', (e) => {
          if (e.target.closest('button')) return;
          flip();
        });
      }
      const flipBtn = document.getElementById('lzFlip');
      if (flipBtn) flipBtn.addEventListener('click', flip);

      const g1 = document.getElementById('lzGrade1'); if (g1) g1.addEventListener('click', () => grade(1));
      const g2 = document.getElementById('lzGrade2'); if (g2) g2.addEventListener('click', () => grade(2));
      const g3 = document.getElementById('lzGrade3'); if (g3) g3.addEventListener('click', () => grade(3));

      const skipBtn = document.getElementById('lzSkip'); if (skipBtn) skipBtn.addEventListener('click', skip);
      const undoBtn = document.getElementById('lzUndo'); if (undoBtn) undoBtn.addEventListener('click', undo);

      const exitBtn = document.getElementById('lzExit');
      if (exitBtn) exitBtn.addEventListener('click', () => {
        if (S && !S.endedAt) {
          if (!confirm('Exit session? Progress is saved — you can resume later.')) return;
        }
        UI.exit();
      });

      const pauseBtn = document.getElementById('lzPause');
      if (pauseBtn) pauseBtn.addEventListener('click', () => {
        if (!S) return;
        if (S.pausedAt) {
          unpauseSession();
          pauseBtn.textContent = '⏸';
        } else {
          pauseSession();
          pauseBtn.textContent = '▶';
        }
      });
    },

    renderRescue() {
      const overlay = document.getElementById('lzModalRoot');
      if (!overlay || !S || !S.currentRescue) return;
      const card = S.currentRescue.card;
      overlay.innerHTML = `
        <div class="lz-modal lz-rescue">
          <span class="lz-rescue-label">Triple miss · slow down</span>
          <h3>${escHTML((card.term || '').replace(/<[^>]+>/g, ''))}</h3>
          <div class="lz-rescue-card">
            <div class="lz-rescue-def">${card.def || ''}</div>
            ${card.example ? `<div class="lz-rescue-ex"><span class="lz-rescue-sublabel">Apply it</span>${card.example}</div>` : ''}
            ${(card.mnem || card.mnemonic) ? `<div class="lz-rescue-mnem"><span class="lz-rescue-sublabel">Mnemonic</span>${card.mnem || card.mnemonic}</div>` : ''}
          </div>
          <div class="lz-rescue-buttons">
            <button class="lz-btn lz-btn-ghost" id="lzRescuePark">Park for tomorrow</button>
            <button class="lz-btn lz-btn-primary" id="lzRescueContinue">Keep drilling</button>
          </div>
        </div>
        <div class="lz-modal-backdrop"></div>
      `;
      overlay.style.display = '';
      const park = document.getElementById('lzRescuePark');
      if (park) park.addEventListener('click', () => {
        const k = S.currentRescue.key;
        const c = S.currentRescue.card;
        S.queue = S.queue.filter(it => cardKey(it.card) !== k);
        S.todayGotIt.push(k);
        setCardState(c, { state: 'got_it' });
        S.currentRescue = null;
        S.flipped = false;
        if (S.currentIdx >= S.queue.length) S.currentIdx = 0;
        overlay.style.display = 'none';
        overlay.innerHTML = '';
        if (S.queue.length === 0) { endSession('clear'); return; }
        persistSession();
        UI.render();
      });
      const cont = document.getElementById('lzRescueContinue');
      if (cont) cont.addEventListener('click', () => {
        S.currentRescue = null;
        overlay.style.display = 'none';
        overlay.innerHTML = '';
        persistSession();
        UI.render();
      });
    },

    renderTrap() {
      const overlay = document.getElementById('lzModalRoot');
      if (!overlay || !S || !S.currentTrap) return;
      const t = S.currentTrap;

      if (t.answeredCorrectly === null) {
        const promptTerm = (t.promptCard.term || '').replace(/<[^>]+>/g, '');
        const correctDef = t.promptCard.def || '';
        const wrongDef = t.decoyCard.def || '';
        const choiceA = t.correctIsA ? correctDef : wrongDef;
        const choiceB = t.correctIsA ? wrongDef : correctDef;
        overlay.innerHTML = `
          <div class="lz-modal lz-trap">
            <span class="lz-trap-label">Trap card · pick the right def</span>
            <h3>Which definition matches <em>${escHTML(promptTerm)}</em>?</h3>
            <div class="lz-trap-choices">
              <button class="lz-trap-choice" id="lzTrapA">
                <span class="lz-trap-choice-letter">A</span>
                <span class="lz-trap-choice-def">${choiceA}</span>
              </button>
              <button class="lz-trap-choice" id="lzTrapB">
                <span class="lz-trap-choice-letter">B</span>
                <span class="lz-trap-choice-def">${choiceB}</span>
              </button>
            </div>
          </div>
          <div class="lz-modal-backdrop"></div>
        `;
        overlay.style.display = '';
        const a = document.getElementById('lzTrapA'); if (a) a.addEventListener('click', () => answerTrap('A'));
        const b = document.getElementById('lzTrapB'); if (b) b.addEventListener('click', () => answerTrap('B'));
      } else if (t.answeredCorrectly) {
        overlay.innerHTML = `
          <div class="lz-modal lz-trap-toast lz-trap-toast-correct">
            <span class="lz-trap-toast-icon">✓</span>
            Right — moving on
          </div>
        `;
        overlay.style.display = '';
      } else {
        overlay.innerHTML = `
          <div class="lz-modal lz-trap lz-trap-wrong">
            <span class="lz-trap-label lz-wrong">Trap caught you</span>
            <h3>Comparison card injected next</h3>
            <div class="lz-trap-explain">
              <div><b>${t.promptCard.term || ''}:</b> ${t.promptCard.def || ''}</div>
              <div style="margin-top:10px"><b>${t.decoyCard.term || ''}:</b> ${t.decoyCard.def || ''}</div>
            </div>
          </div>
          <div class="lz-modal-backdrop"></div>
        `;
        overlay.style.display = '';
      }
    },

    showSoftBreakOffer() {
      const t = document.createElement('div');
      t.className = 'lz-toast';
      t.innerHTML = `
        <span class="lz-toast-msg">8 min in. 30-second break?</span>
        <button class="lz-toast-yes" id="lzBreakYes">Yes</button>
        <button class="lz-toast-no" id="lzBreakNo">Skip</button>
      `;
      document.body.appendChild(t);

      const yes = t.querySelector('#lzBreakYes');
      yes.addEventListener('click', () => {
        pauseSession();
        t.innerHTML = `<span class="lz-toast-msg">Stretch · breathe</span><span class="lz-toast-count" id="lzBreakCount">30</span>`;
        let n = 30;
        const ti = setInterval(() => {
          n--;
          const ce = document.getElementById('lzBreakCount');
          if (ce) ce.textContent = n;
          if (n <= 0) {
            clearInterval(ti);
            unpauseSession();
            const pb = document.getElementById('lzPause'); if (pb) pb.textContent = '⏸';
            if (t.parentNode) t.remove();
          }
        }, 1000);
      });
      const no = t.querySelector('#lzBreakNo');
      no.addEventListener('click', () => { if (t.parentNode) t.remove(); });

      setTimeout(() => { if (t.parentNode && !t.querySelector('.lz-toast-count')) t.remove(); }, 8000);
    },

    showForcedBreak() {
      const overlay = document.getElementById('lzModalRoot');
      if (!overlay) return;
      overlay.innerHTML = `
        <div class="lz-modal lz-break-forced">
          <span class="lz-rescue-label">Pacing break · take 60 seconds</span>
          <h3>Time for a real break</h3>
          <p class="lz-break-body">8 min in and the rate is dipping. Look out a window — eyes off the screen — back in a minute.</p>
          <div class="lz-break-count" id="lzBreakBig">60</div>
          <button class="lz-btn lz-btn-ghost" id="lzBreakSkip">Skip break</button>
        </div>
        <div class="lz-modal-backdrop"></div>
      `;
      overlay.style.display = '';
      let n = 60;
      const ti = setInterval(() => {
        n--;
        const ce = document.getElementById('lzBreakBig');
        if (ce) ce.textContent = n;
        if (n <= 0) {
          clearInterval(ti);
          unpauseSession();
          overlay.style.display = 'none';
          overlay.innerHTML = '';
          UI.render();
        }
      }, 1000);
      const sk = document.getElementById('lzBreakSkip');
      if (sk) sk.addEventListener('click', () => {
        clearInterval(ti);
        unpauseSession();
        overlay.style.display = 'none';
        overlay.innerHTML = '';
        UI.render();
      });
    },

    renderEnd() {
      const root = document.getElementById('lzRoot');
      if (!root || !S) return;
      UI.stopTimerLoop();

      const elapsedMs = (S.endedAt || Date.now()) - S.startedAt;
      const elapsedMin = Math.floor(elapsedMs / 60000);
      const elapsedSec = Math.floor((elapsedMs % 60000) / 1000);
      const rate = S.cardSeen > 0 ? Math.round(S.firstTryGotIt / S.cardSeen * 100) : 0;

      const topMisses = Object.entries(S.missCounts || {})
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([k, n]) => {
          const c = findCardByKey(k);
          return c ? { card: c, count: n } : null;
        })
        .filter(Boolean);

      const failedKeys = [...new Set([...(S.todayMisses || []), ...(S.todayShakies || [])])];
      const canBoss = failedKeys.length > 0;
      const tomorrowCount = (S.todayMisses || []).length + (S.todayShakies || []).length;

      const reasonLabel = S.endReason === 'timer' ? 'Time up'
        : S.endReason === 'clear' ? 'Queue cleared'
        : 'Ended';

      root.innerHTML = `
        <div class="lz-end">
          <header class="lz-end-head">
            <h2>Session done</h2>
            <span class="lz-end-reason">${reasonLabel}</span>
            <button class="lz-icon-btn lz-close" id="lzEndClose" title="Close">×</button>
          </header>
          <div class="lz-end-stats">
            <div class="lz-stat"><span class="lz-stat-num">${elapsedMin}m ${elapsedSec}s</span><span class="lz-stat-lbl">Time</span></div>
            <div class="lz-stat"><span class="lz-stat-num">${S.cardSeen}</span><span class="lz-stat-lbl">Cards seen</span></div>
            <div class="lz-stat"><span class="lz-stat-num">${rate}%</span><span class="lz-stat-lbl">First-try Got it</span></div>
            <div class="lz-stat"><span class="lz-stat-num">🔥 ${S.bestStreak}</span><span class="lz-stat-lbl">Best streak</span></div>
          </div>
          ${topMisses.length ? `
            <div class="lz-end-misses">
              <h3>Top misses</h3>
              <ul>${topMisses.map(m => `
                <li>
                  <div class="lz-end-miss-row">
                    <span class="lz-end-miss-term">${m.card.term || ''}</span>
                    <span class="lz-end-miss-count">${m.count}×</span>
                  </div>
                  <div class="lz-end-miss-def">${(m.card.def || '').slice(0, 240)}${(m.card.def || '').length > 240 ? '…' : ''}</div>
                </li>
              `).join('')}</ul>
            </div>
          ` : ''}
          <div class="lz-end-buttons">
            ${canBoss ? `<button class="lz-btn lz-btn-primary" id="lzBossMode">Boss Mode · drill ${failedKeys.length} failed</button>` : ''}
            <button class="lz-btn lz-btn-ghost" id="lzEndExit">Close out</button>
          </div>
          <p class="lz-end-tomorrow">Tomorrow's deck: ${tomorrowCount} drill cards seeded · fresh unseen will mix in.</p>
        </div>
      `;

      const cls = document.getElementById('lzEndClose');
      if (cls) cls.addEventListener('click', () => UI.exit());
      const xt = document.getElementById('lzEndExit');
      if (xt) xt.addEventListener('click', () => UI.exit());
      const boss = document.getElementById('lzBossMode');
      if (boss) boss.addEventListener('click', () => {
        const hist = loadJSON(KEYS.HISTORY, {});
        hist.todayMisses  = S.todayMisses;
        hist.todayShakies = S.todayShakies;
        saveJSON(KEYS.HISTORY, hist);
        const deckId = S.deckId;
        clearSession();
        startSession(deckId, 10, 'boss');
      });
    },

    exit() {
      UI.stopTimerLoop();
      const root = document.getElementById('lzRoot');
      if (root) root.innerHTML = '';
      const overlay = document.getElementById('lzModalRoot');
      if (overlay) { overlay.style.display = 'none'; overlay.innerHTML = ''; }
      if (typeof window.setMode === 'function') {
        window.setMode('study');
      } else {
        document.body.classList.remove('fc-mode');
      }
    },

    html: {
      session() {
        return `
          <div class="lz-shell">
            <header class="lz-top">
              <span class="lz-counter" id="lzCounter">Card 1</span>
              <span class="lz-streak" id="lzStreak"><span class="lz-streak-flame">🔥</span><span class="lz-streak-num">0</span></span>
              <span class="lz-timer" id="lzTimer">0:00</span>
              <button class="lz-icon-btn" id="lzPause" title="Pause/resume">⏸</button>
              <button class="lz-icon-btn lz-close" id="lzExit" title="Exit (Esc)">×</button>
            </header>
            <div class="lz-card-stage">
              <div class="lz-card" id="lzCard">
                <div class="lz-ctx" id="lzCtx"></div>
                <div class="lz-question" id="lzQuestion"></div>
                <div class="lz-answer" id="lzAnswer" style="display:none"></div>
                <div class="lz-example" id="lzExample" style="display:none"></div>
                <div class="lz-mnem" id="lzMnemonic" style="display:none"></div>
              </div>
            </div>
            <div class="lz-grade-bar">
              <button type="button" class="lz-grade-btn lz-grade-1" id="lzGrade1" disabled>
                <span class="lz-grade-key">1</span>
                <span class="lz-grade-lbl">Miss</span>
              </button>
              <button type="button" class="lz-grade-btn lz-grade-2" id="lzGrade2" disabled>
                <span class="lz-grade-key">2</span>
                <span class="lz-grade-lbl">Shaky</span>
              </button>
              <button type="button" class="lz-grade-btn lz-grade-3" id="lzGrade3" disabled>
                <span class="lz-grade-key">3</span>
                <span class="lz-grade-lbl">Got it</span>
              </button>
            </div>
            <div class="lz-bottom-row">
              <button type="button" class="lz-btn-small" id="lzFlip">Flip (Space)</button>
              <button type="button" class="lz-btn-small" id="lzUndo">Undo (U)</button>
              <button type="button" class="lz-btn-small" id="lzSkip">Skip (J)</button>
            </div>
          </div>
        `;
      }
    }
  };

  // ============================================================ keyboard

  document.addEventListener('keydown', (e) => {
    if (!document.body.classList.contains('fc-mode')) return;
    if (!document.getElementById('lzRoot')) return;
    const t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
    // Don't intercept inside trap modal — its buttons handle keyboard naturally
    if (e.key === ' ' || e.code === 'Space') { e.preventDefault(); flip(); }
    else if (e.key === '1') { e.preventDefault(); grade(1); }
    else if (e.key === '2') { e.preventDefault(); grade(2); }
    else if (e.key === '3') { e.preventDefault(); grade(3); }
    else if (e.key === 'u' || e.key === 'U') { e.preventDefault(); undo(); }
    else if (e.key === 'j' || e.key === 'J') { e.preventDefault(); skip(); }
    else if (e.key === 'Escape') {
      if (S && !S.endedAt) {
        if (confirm('Exit session? Progress is saved — you can resume later.')) UI.exit();
      } else {
        UI.exit();
      }
    }
  });

  // ============================================================ styles

  function injectStyles() {
    if (document.getElementById('lz-styles')) return;
    const css = document.createElement('style');
    css.id = 'lz-styles';
    css.textContent = `
      /* Hide the old fc-overlay so the new system owns flash mode */
      body.fc-mode .fc-overlay { display: none !important; }

      .lz-root {
        display: none;
        position: fixed; inset: 0;
        z-index: 1000;
        background: var(--bg, #0c0e12);
        color: var(--ink, #e6dfd0);
        font-family: var(--ff-ui, 'Inter', system-ui, sans-serif);
        overflow: auto;
      }
      body.fc-mode .lz-root { display: block; }

      /* --- setup screen --- */
      .lz-setup {
        max-width: 560px;
        margin: 6vh auto 0;
        padding: 32px 28px;
        background: var(--bg-elev, #14171d);
        border: 1px solid var(--rule, #22262f);
        border-radius: 12px;
      }
      .lz-setup-head {
        display: flex; justify-content: space-between; align-items: baseline;
        border-bottom: 1px solid var(--rule, #22262f);
        padding-bottom: 12px; margin-bottom: 20px;
      }
      .lz-setup-head h2 {
        font-family: var(--ff-display, 'Fraunces', Georgia, serif);
        font-size: 28px; font-weight: 600;
        color: var(--ink, #e6dfd0);
        margin: 0;
      }
      .lz-setup-body { display: flex; flex-direction: column; gap: 20px; }
      .lz-field { display: flex; flex-direction: column; gap: 8px; }
      .lz-field-label {
        font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--ink-faint, #6b6353);
      }
      .lz-select {
        background: var(--bg-sunk, #090a0e);
        color: var(--ink, #e6dfd0);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 10px 12px;
        font-family: inherit;
        font-size: 14px;
      }
      .lz-time-chips { display: flex; gap: 8px; flex-wrap: wrap; }
      .lz-time-chip {
        flex: 1 1 0;
        background: var(--bg-sunk, #090a0e);
        color: var(--ink-dim, #a59a83);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 12px 16px;
        font-family: inherit;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.15s;
      }
      .lz-time-chip:hover { color: var(--ink, #e6dfd0); border-color: var(--rule-strong, #2e333d); }
      .lz-time-chip.active {
        background: var(--accent-soft, #5b4412);
        color: var(--accent-ink, #f1d278);
        border-color: var(--accent, #c89b2e);
      }
      .lz-btn {
        background: var(--bg-sunk, #090a0e);
        color: var(--ink, #e6dfd0);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 12px 20px;
        font-family: inherit;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.15s;
      }
      .lz-btn:hover { border-color: var(--rule-strong, #2e333d); }
      .lz-btn-primary {
        background: var(--accent, #c89b2e);
        color: var(--bg, #0c0e12);
        border-color: var(--accent, #c89b2e);
      }
      .lz-btn-primary:hover { filter: brightness(1.08); }
      .lz-btn-ghost { background: transparent; }
      .lz-btn-go {
        font-size: 16px;
        padding: 16px 20px;
        margin-top: 8px;
      }
      .lz-setup-hint {
        font-size: 12px;
        color: var(--ink-faint, #6b6353);
        text-align: center;
        margin-top: 8px;
        line-height: 1.6;
      }
      .lz-setup-hint kbd {
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 3px;
        padding: 1px 6px;
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 11px;
        margin: 0 2px;
      }
      .lz-resume {
        background: var(--accent-soft, #5b4412);
        border: 1px solid var(--accent, #c89b2e);
        border-radius: 8px;
        padding: 16px 18px;
        margin-bottom: 20px;
      }
      .lz-resume h3 {
        font-size: 14px;
        font-weight: 600;
        color: var(--accent-ink, #f1d278);
        margin: 0 0 6px;
      }
      .lz-resume-meta {
        font-size: 12px;
        color: var(--ink-dim, #a59a83);
        margin-bottom: 12px;
      }
      .lz-resume-buttons { display: flex; gap: 8px; }
      .lz-icon-btn {
        background: transparent;
        color: var(--ink-dim, #a59a83);
        border: 1px solid transparent;
        border-radius: 4px;
        padding: 4px 10px;
        font-size: 18px;
        cursor: pointer;
        line-height: 1;
        font-family: inherit;
      }
      .lz-icon-btn:hover { color: var(--ink, #e6dfd0); border-color: var(--rule, #22262f); }
      .lz-close { font-size: 24px; padding: 0 10px; }

      /* --- session screen --- */
      .lz-shell {
        max-width: 920px;
        margin: 0 auto;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        padding: 0 24px;
      }
      .lz-top {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 18px 0 14px;
        border-bottom: 1px solid var(--rule, #22262f);
      }
      .lz-counter {
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 12px;
        color: var(--ink-faint, #6b6353);
        letter-spacing: 0.04em;
      }
      .lz-streak {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        font-size: 14px;
        color: var(--ink-dim, #a59a83);
      }
      .lz-streak-flame { font-size: 14px; }
      .lz-streak-num { font-weight: 600; color: var(--accent-ink, #f1d278); }
      .lz-timer {
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 18px;
        color: var(--ink, #e6dfd0);
        margin-left: auto;
        font-variant-numeric: tabular-nums;
      }
      .lz-card-stage {
        flex: 1;
        display: flex;
        align-items: stretch;
        padding: 28px 0;
      }
      .lz-card {
        flex: 1;
        background: var(--bg-elev, #14171d);
        border: 1px solid var(--rule, #22262f);
        border-radius: 12px;
        padding: 36px 40px;
        cursor: pointer;
        transition: transform 0.18s ease, opacity 0.18s ease;
        display: flex;
        flex-direction: column;
        gap: 18px;
      }
      .lz-card:hover { border-color: var(--rule-strong, #2e333d); }
      .lz-card.lz-flipped { animation: lzFlipIn 0.22s ease; }
      @keyframes lzFlipIn {
        from { opacity: 0.55; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
      }
      .lz-ctx {
        font-size: 11px;
        color: var(--ink-faint, #6b6353);
        text-transform: uppercase;
        letter-spacing: 0.08em;
      }
      .lz-question {
        font-family: var(--ff-display, 'Fraunces', Georgia, serif);
        font-size: 32px;
        font-weight: 600;
        line-height: 1.18;
        color: var(--ink, #e6dfd0);
      }
      .lz-question em {
        font-style: italic;
        color: var(--accent-ink, #f1d278);
      }
      .lz-answer {
        font-size: 17px;
        line-height: 1.55;
        color: var(--ink, #e6dfd0);
        padding-top: 18px;
        border-top: 1px solid var(--rule, #22262f);
      }
      .lz-answer b, .lz-answer strong { color: var(--accent-ink, #f1d278); }
      .lz-example {
        background: rgba(122, 143, 168, 0.1);
        border-left: 3px solid var(--info, #7a8fa8);
        padding: 12px 14px 12px 14px;
        border-radius: 4px;
        font-size: 14px;
        line-height: 1.55;
        color: var(--ink-dim, #a59a83);
      }
      .lz-example-label {
        display: block;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--info, #7a8fa8);
        font-weight: 600;
        margin-bottom: 4px;
      }
      .lz-mnem {
        background: rgba(200, 155, 46, 0.08);
        border: 1.5px solid var(--accent, #c89b2e);
        border-radius: 6px;
        padding: 14px 16px;
        font-size: 15px;
        line-height: 1.55;
        color: var(--accent-ink, #f1d278);
        font-style: italic;
      }
      .lz-mnem-label {
        display: block;
        font-style: normal;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--accent, #c89b2e);
        font-weight: 700;
        margin-bottom: 4px;
      }

      .lz-grade-bar {
        display: flex;
        gap: 10px;
        padding-top: 8px;
      }
      .lz-grade-btn {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background: var(--bg-elev, #14171d);
        color: var(--ink, #e6dfd0);
        border: 1px solid var(--rule, #22262f);
        border-radius: 8px;
        padding: 16px 20px;
        font-family: inherit;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.15s;
      }
      .lz-grade-btn:not(:disabled):hover { border-color: currentColor; }
      .lz-grade-btn:disabled { opacity: 0.35; cursor: not-allowed; }
      .lz-grade-1 { color: var(--wrong, #c86462); }
      .lz-grade-2 { color: var(--warn, #c89b2e); }
      .lz-grade-3 { color: var(--correct, #5fa871); }
      .lz-grade-key {
        display: inline-block;
        min-width: 22px;
        height: 22px;
        line-height: 22px;
        text-align: center;
        background: rgba(255,255,255,0.06);
        border-radius: 4px;
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 12px;
        font-weight: 600;
      }
      .lz-grade-lbl { font-weight: 500; }

      .lz-bottom-row {
        display: flex;
        gap: 8px;
        justify-content: center;
        padding: 14px 0 22px;
      }
      .lz-btn-small {
        background: transparent;
        color: var(--ink-faint, #6b6353);
        border: 1px solid var(--rule, #22262f);
        border-radius: 4px;
        padding: 6px 12px;
        font-family: inherit;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.15s;
      }
      .lz-btn-small:hover { color: var(--ink, #e6dfd0); border-color: var(--rule-strong, #2e333d); }

      /* --- modal layer --- */
      .lz-modal-root {
        position: fixed; inset: 0;
        z-index: 2000;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
      }
      .lz-modal-backdrop {
        position: absolute; inset: 0;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(2px);
        z-index: 0;
      }
      .lz-modal {
        position: relative;
        z-index: 1;
        background: var(--bg-elev, #14171d);
        border: 1px solid var(--rule-strong, #2e333d);
        border-radius: 12px;
        padding: 28px 28px 24px;
        max-width: 540px;
        width: 100%;
        max-height: 86vh;
        overflow: auto;
        animation: lzModalIn 0.18s ease;
      }
      @keyframes lzModalIn {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      .lz-rescue-label, .lz-trap-label {
        display: inline-block;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 700;
        color: var(--accent, #c89b2e);
        margin-bottom: 8px;
      }
      .lz-trap-label.lz-wrong { color: var(--wrong, #c86462); }
      .lz-modal h3 {
        font-family: var(--ff-display, 'Fraunces', Georgia, serif);
        font-size: 22px;
        font-weight: 600;
        margin: 0 0 14px;
        color: var(--ink, #e6dfd0);
      }
      .lz-rescue-card {
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 18px;
      }
      .lz-rescue-def { font-size: 15px; line-height: 1.5; margin-bottom: 12px; color: var(--ink, #e6dfd0); }
      .lz-rescue-ex {
        background: rgba(122, 143, 168, 0.1);
        border-left: 3px solid var(--info, #7a8fa8);
        padding: 10px 12px;
        font-size: 13px;
        line-height: 1.5;
        color: var(--ink-dim, #a59a83);
        border-radius: 3px;
        margin-bottom: 10px;
      }
      .lz-rescue-mnem {
        background: rgba(200, 155, 46, 0.08);
        border: 1px solid var(--accent, #c89b2e);
        padding: 10px 12px;
        font-size: 13px;
        line-height: 1.5;
        color: var(--accent-ink, #f1d278);
        font-style: italic;
        border-radius: 4px;
      }
      .lz-rescue-sublabel {
        display: block;
        font-style: normal;
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 700;
        color: var(--accent, #c89b2e);
        margin-bottom: 4px;
      }
      .lz-rescue-ex .lz-rescue-sublabel { color: var(--info, #7a8fa8); }
      .lz-rescue-buttons {
        display: flex;
        gap: 10px;
        justify-content: flex-end;
      }

      .lz-trap-choices { display: flex; flex-direction: column; gap: 10px; }
      .lz-trap-choice {
        display: flex; align-items: flex-start; gap: 12px;
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 14px 16px;
        text-align: left;
        font-family: inherit;
        font-size: 14px;
        color: var(--ink, #e6dfd0);
        cursor: pointer;
        transition: all 0.15s;
        line-height: 1.5;
      }
      .lz-trap-choice:hover { border-color: var(--accent, #c89b2e); }
      .lz-trap-choice-letter {
        flex: 0 0 auto;
        width: 24px; height: 24px;
        background: var(--accent-soft, #5b4412);
        color: var(--accent-ink, #f1d278);
        border-radius: 4px;
        display: flex; align-items: center; justify-content: center;
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 12px;
        font-weight: 600;
      }
      .lz-trap-choice-def { flex: 1; }
      .lz-trap-toast {
        background: var(--bg-elev, #14171d);
        border: 1.5px solid var(--correct, #5fa871);
        padding: 18px 22px;
        font-size: 16px;
        color: var(--correct, #5fa871);
        display: flex; align-items: center; gap: 10px;
      }
      .lz-trap-toast-icon {
        font-size: 20px;
        font-weight: 700;
      }
      .lz-trap-explain {
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 14px 16px;
        font-size: 14px;
        line-height: 1.55;
      }

      .lz-break-forced { text-align: center; }
      .lz-break-body { color: var(--ink-dim, #a59a83); font-size: 14px; line-height: 1.5; margin: 8px 0 18px; }
      .lz-break-count {
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 64px;
        font-weight: 600;
        color: var(--accent-ink, #f1d278);
        margin: 12px 0 18px;
        font-variant-numeric: tabular-nums;
      }

      .lz-toast {
        position: fixed;
        bottom: 24px; left: 50%;
        transform: translateX(-50%);
        background: var(--bg-elev, #14171d);
        border: 1px solid var(--accent, #c89b2e);
        border-radius: 8px;
        padding: 12px 16px;
        z-index: 1500;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 13px;
        color: var(--ink, #e6dfd0);
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      }
      .lz-toast button {
        background: transparent;
        color: var(--accent-ink, #f1d278);
        border: 1px solid var(--accent, #c89b2e);
        border-radius: 4px;
        padding: 4px 10px;
        font-size: 12px;
        cursor: pointer;
        font-family: inherit;
      }
      .lz-toast .lz-toast-no {
        color: var(--ink-faint, #6b6353);
        border-color: var(--rule, #22262f);
      }
      .lz-toast-count {
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 16px;
        color: var(--accent-ink, #f1d278);
        margin-left: 4px;
      }

      /* --- end screen --- */
      .lz-end {
        max-width: 720px;
        margin: 4vh auto 0;
        padding: 32px 28px;
        background: var(--bg-elev, #14171d);
        border: 1px solid var(--rule, #22262f);
        border-radius: 12px;
      }
      .lz-end-head {
        display: flex; align-items: baseline; gap: 14px;
        border-bottom: 1px solid var(--rule, #22262f);
        padding-bottom: 16px; margin-bottom: 22px;
      }
      .lz-end-head h2 {
        font-family: var(--ff-display, 'Fraunces', Georgia, serif);
        font-size: 28px; font-weight: 600;
        color: var(--ink, #e6dfd0);
        margin: 0;
      }
      .lz-end-reason {
        font-size: 11px;
        color: var(--ink-faint, #6b6353);
        text-transform: uppercase;
        letter-spacing: 0.08em;
      }
      .lz-end-head .lz-icon-btn { margin-left: auto; }
      .lz-end-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 24px;
      }
      .lz-stat {
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 14px 12px;
        display: flex;
        flex-direction: column;
        gap: 4px;
        text-align: center;
      }
      .lz-stat-num {
        font-family: var(--ff-display, 'Fraunces', Georgia, serif);
        font-size: 22px;
        font-weight: 600;
        color: var(--accent-ink, #f1d278);
      }
      .lz-stat-lbl {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--ink-faint, #6b6353);
      }

      .lz-end-misses { margin-bottom: 22px; }
      .lz-end-misses h3 {
        font-size: 13px;
        font-weight: 600;
        color: var(--ink-dim, #a59a83);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 0 0 10px;
      }
      .lz-end-misses ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; }
      .lz-end-misses li {
        background: var(--bg-sunk, #090a0e);
        border: 1px solid var(--rule, #22262f);
        border-radius: 6px;
        padding: 12px 14px;
      }
      .lz-end-miss-row {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 6px;
      }
      .lz-end-miss-term {
        font-size: 15px; font-weight: 500;
        color: var(--ink, #e6dfd0);
      }
      .lz-end-miss-count {
        font-family: var(--ff-mono, ui-monospace, monospace);
        font-size: 12px;
        color: var(--wrong, #c86462);
      }
      .lz-end-miss-def {
        font-size: 13px; line-height: 1.5;
        color: var(--ink-dim, #a59a83);
      }
      .lz-end-buttons {
        display: flex; gap: 10px; justify-content: flex-end;
        margin-bottom: 12px;
      }
      .lz-end-tomorrow {
        font-size: 12px;
        color: var(--ink-faint, #6b6353);
        text-align: center;
        margin: 0;
      }

      /* --- responsive --- */
      @media (max-width: 720px) {
        .lz-shell { padding: 0 14px; }
        .lz-card { padding: 26px 20px; }
        .lz-question { font-size: 24px; }
        .lz-answer { font-size: 15px; }
        .lz-grade-btn { padding: 14px 10px; font-size: 13px; }
        .lz-grade-btn .lz-grade-lbl { display: none; }
        .lz-grade-key { font-size: 14px; min-width: 28px; height: 28px; line-height: 28px; }
        .lz-grade-1::after { content: ' Miss'; font-weight: 500; font-size: 13px; }
        .lz-grade-2::after { content: ' Shaky'; font-weight: 500; font-size: 13px; }
        .lz-grade-3::after { content: ' Got it'; font-weight: 500; font-size: 13px; }
        .lz-end-stats { grid-template-columns: repeat(2, 1fr); }
        .lz-setup { margin: 4vh auto 0; padding: 24px 18px; }
      }
    `;
    document.head.appendChild(css);
  }

  // ============================================================ entry

  function open() {
    UI.ensureRoot();
    migrateOnce();
    loadProgress();
    UI.startTimerLoop();
    if (S) {
      // already running in memory
    } else if (hasSavedSession()) {
      // setup screen will offer resume
    }
    UI.render();
  }

  window.LeitnerSession = {
    open,
    startSession,
    resumeSession,
    endSession,
    grade,
    flip,
    skip,
    undo,
    _S: () => S,
    _progress: () => progress,
  };

  function init() {
    injectStyles();
    UI.ensureRoot();
    migrateOnce();
    loadProgress();

    // Watch for fc-mode entering
    const obs = new MutationObserver(() => {
      const inFlash = document.body.classList.contains('fc-mode');
      const root = document.getElementById('lzRoot');
      if (inFlash) {
        if (root && !root.innerHTML.trim()) open();
      } else {
        UI.stopTimerLoop();
      }
    });
    obs.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    if (document.body.classList.contains('fc-mode')) open();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
