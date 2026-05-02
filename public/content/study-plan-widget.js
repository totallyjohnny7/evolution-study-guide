/* study-plan-widget.js — Adaptive daily study plan widget for the
 * exam crunch (Mon 2026-05-04). Lives as a floating panel in the
 * bottom-right and surfaces:
 *
 *   - Live clock + countdown to exam
 *   - Today's plan: time-blocks for Flash / Stim / Boss Mode / Review
 *   - Block status: upcoming · now · done · missed (red-tagged)
 *   - Stacking: missed blocks push forward into the next free slot
 *   - Activity-driven completion: detects when leitner cards-seen or
 *     stim questions answered crosses the block's target since start
 *
 * Storage: study-plan-v1
 *   {
 *     examDate: '2026-05-04',
 *     plansByDay: {
 *       '2026-04-30': { blocks: [{ id, start, end, title, deckId, mode, target, ... }], baselineCards }
 *     },
 *     completion: { [blockId]: { startedAt, completedAt, cardsAtStart, cardsAtEnd, hit } },
 *     visible: true
 *   }
 *
 * Pure side: no edits to flashcards.js. Reads existing localStorage.
 */
(function () {
  'use strict';

  const KEY_STATE = 'study-plan-v1';
  const PLAN_SCHEMA = 2; // bump to force regenerate today's plan after a generator change
  const KEY_LEITNER_HIST = 'leitner-history-v1';
  const KEY_LEITNER_PROG = 'leitner-progress-v1';
  const KEY_LEITNER_SESS = 'leitner-session-v1';
  const KEY_STIM_SESS = 'evol_stim_session';

  const EXAM_ISO = '2026-05-04'; // Monday
  const EXAM_NAME = 'BIOL 4230 Final';

  // ============================================================ utility

  function isoDate(d) {
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }
  function dayOfWeek(d) {
    return ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][d.getDay()];
  }
  function fmtDate(d) {
    const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    return `${months[d.getMonth()]} ${d.getDate()} · ${dayOfWeek(d)}`;
  }
  function fmtClock(d) {
    const hh = String(d.getHours()).padStart(2, '0');
    const mm = String(d.getMinutes()).padStart(2, '0');
    const ss = String(d.getSeconds()).padStart(2, '0');
    return `${hh}:${mm}:${ss}`;
  }
  function fmtHM(d) {
    const hh = String(d.getHours()).padStart(2, '0');
    const mm = String(d.getMinutes()).padStart(2, '0');
    return `${hh}:${mm}`;
  }
  function parseHM(hm, baseDate) {
    const [h, m] = hm.split(':').map(Number);
    const d = new Date(baseDate.getTime());
    d.setHours(h, m, 0, 0);
    return d;
  }
  function daysBetween(d1, d2) {
    const a = new Date(d1.getFullYear(), d1.getMonth(), d1.getDate());
    const b = new Date(d2.getFullYear(), d2.getMonth(), d2.getDate());
    return Math.round((b - a) / 86400000);
  }
  function load(k, d) {
    try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); }
    catch (e) { return d; }
  }
  function save(k, v) {
    try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {}
  }
  function escHTML(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, c => (
      { '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]
    ));
  }

  // ============================================================ activity

  function totalCardsSeen() {
    const h = load(KEY_LEITNER_HIST, {});
    const live = load(KEY_LEITNER_SESS, null);
    const liveCount = live && !live.endedAt ? (live.cardSeen || 0) : 0;
    return (h.totalCardsSeen || 0) + liveCount;
  }

  // ============================================================ deck coverage

  // How many UNIQUE cards in the full deck the user has touched / mastered.
  // Reads from leitner-progress-v1 + the live session for in-flight grades.
  function deckCoverage() {
    const decks = (typeof window !== 'undefined' && window.FLASHCARD_DECKS) || {};
    const all = decks.all || [];
    const total = Array.isArray(all) ? all.length : 0;

    const progress = load(KEY_LEITNER_PROG, {}) || {};
    let covered = 0, mastered = 0;
    Object.values(progress).forEach(v => {
      if (!v || !v.state) return;
      if (v.state === 'got_it') { mastered++; covered++; }
      else if (v.state === 'miss' || v.state === 'shaky') { covered++; }
    });

    // Best-effort: include in-flight grades from the live session
    const live = load(KEY_LEITNER_SESS, null);
    if (live && !live.endedAt && Array.isArray(live.todayGotIt)) {
      // todayGotIt holds card keys that haven't yet been persisted to progress
      // (persistence is debounced) — count any not already in progress
      live.todayGotIt.forEach(k => {
        if (!progress[k] || progress[k].state !== 'got_it') {
          // already counted or not counted — best-effort, no double-count guaranteed
        }
      });
    }
    return { total, covered, mastered };
  }
  function totalStimAnswered() {
    const s = load(KEY_STIM_SESS, null);
    if (!s) return 0;
    return (s.stats?.answered) || (s.answered) || (Array.isArray(s.history) ? s.history.length : 0) || 0;
  }
  function cardsMissedToday() {
    const h = load(KEY_LEITNER_HIST, {});
    return (h.todayMisses || []).length;
  }

  // ============================================================ plan generators

  // Each block: { id, start: 'HH:MM', end: 'HH:MM', title, kind, deckId?, target: { cardsSeen?, stimQs? }, note }
  // kind ∈ 'flash' | 'stim' | 'boss' | 'review' | 'rest'

  function generateDayBlocks(daysOut /* days to exam */, dateISO) {
    // Newbie cram plan — exam covers ALL cards. Starting from zero on Day 1.
    // Total deck is roughly ~330 cards across L01-L20. Day 1 = full first pass,
    // Day 2 = drill weak + second pass, Day 3 = mock + cleanup, Day 4 = exam.
    const id = (k) => `${dateISO}__${k}`;
    if (daysOut === 3) {
      // Fri — Day 1: First exposure pass through every lecture. Heavy day.
      // No Boss Mode yet (no misses to drill). Pure flash, deck-by-deck.
      return [
        { id: id('a'), start: '09:00', end: '10:00', title: 'L01–L04 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'Intro, evolutionary thinking, genes, populations · just see them all' },
        { id: id('b'), start: '10:15', end: '11:15', title: 'L05 + L07 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'Quant gen, selection types, empirical · mark anything fuzzy' },
        { id: id('c'), start: '13:30', end: '14:30', title: 'L08 + L09 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'Complex adaptations, coevolution · short break after' },
        { id: id('d'), start: '15:00', end: '16:00', title: 'L11 + L12 + L13 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'Sex, life history, social behavior' },
        { id: id('e'), start: '19:00', end: '20:00', title: 'L14–L17 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'History of life, phylogenetics, species, biogeography' },
        { id: id('f'), start: '20:15', end: '21:00', title: 'L18–L20 · First pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'Conservation, human evolution, evo medicine · last block, skim mode is fine' },
      ];
    }
    if (daysOut === 2) {
      // Sat — Day 2: Drill yesterday's misses, second pass through all decks,
      // first stim quiz to measure baseline.
      return [
        { id: id('a'), start: '09:00', end: '09:45', title: 'Boss Mode · yesterday\'s misses', kind: 'boss', target: { cardsSeen: 50 }, note: 'starts with cards you flagged or missed yesterday' },
        { id: id('b'), start: '10:00', end: '11:00', title: 'L01–L07 · Second pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'should feel faster than Day 1' },
        { id: id('c'), start: '13:30', end: '14:30', title: 'L08–L13 · Second pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'mid-semester core' },
        { id: id('d'), start: '15:00', end: '16:00', title: 'Stim · 30 Qs warmup', kind: 'stim', target: { stimQs: 30 }, note: 'first quiz · note which lectures you bomb' },
        { id: id('e'), start: '16:15', end: '17:00', title: 'Boss Mode · today\'s misses', kind: 'boss', target: { cardsSeen: 30 }, note: 'clean up everything that broke' },
        { id: id('f'), start: '19:30', end: '20:30', title: 'L14–L20 · Second pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'last lectures · lighter, you\'re tired' },
      ];
    }
    if (daysOut === 1) {
      // Sun — Day 3: Mock exam + targeted cleanup + final pass
      return [
        { id: id('a'), start: '09:00', end: '10:00', title: 'Mock exam · 50 Stim Qs', kind: 'stim', target: { stimQs: 50 }, note: 'phone away, time it, no peeking' },
        { id: id('b'), start: '10:15', end: '11:00', title: 'Review missed Stim Qs', kind: 'review', target: {}, note: 'understand WHY each was wrong · don\'t skip' },
        { id: id('c'), start: '13:30', end: '14:30', title: 'Boss Mode · top misses (all)', kind: 'boss', target: { cardsSeen: 50 }, note: 'every miss/shaky from Days 1–3' },
        { id: id('d'), start: '15:00', end: '15:30', title: 'Cheatsheet read-through', kind: 'review', target: {}, note: 'read aloud if possible · /cheatsheet.html' },
        { id: id('e'), start: '16:00', end: '17:00', title: 'Final pass · all decks', kind: 'flash', deckId: 'all', target: { cardsSeen: 100 }, note: 'fast pace · should mostly be Got-it' },
        { id: id('f'), start: '19:00', end: '19:30', title: 'Last Boss · weakest 25', kind: 'boss', target: { cardsSeen: 25 }, note: 'short final cleanup · sleep early' },
      ];
    }
    if (daysOut === 0) {
      // Exam day — rest, one cheatsheet skim
      return [
        { id: id('a'), start: '07:30', end: '08:00', title: 'Cheatsheet final skim', kind: 'review', target: {}, note: '~1 hr before exam · quick pass · NO new content' },
        { id: id('b'), start: '08:15', end: '08:30', title: 'Top 10 misses · last look', kind: 'boss', target: { cardsSeen: 10 }, note: '15 min only · then close the laptop' },
        { id: id('c'), start: '09:00', end: '09:00', title: 'EXAM · ' + EXAM_NAME, kind: 'rest', target: {}, note: 'good luck!' },
      ];
    }
    if (daysOut < 0) {
      return [
        { id: id('a'), start: '12:00', end: '12:00', title: 'Exam done · plan exhausted', kind: 'rest', target: {}, note: 'add a new exam date in study-plan-v1 to refresh' },
      ];
    }
    // 4+ days out — pacing block, get ahead
    return [
      { id: id('a'), start: '10:00', end: '10:45', title: 'Get ahead · L01–L05', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'banking cards before crunch' },
      { id: id('b'), start: '15:00', end: '15:30', title: 'Stim 20', kind: 'stim', target: { stimQs: 20 } },
      { id: id('c'), start: '19:30', end: '20:00', title: 'Get ahead · L06–L10', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 } },
    ];
  }

  // ============================================================ state

  // If most blocks are already past, compress remaining work into a few shorter
  // blocks running from now → bedtime. Always leaves the user with at least
  // one actionable block while they're awake.
  function adaptBlocksForCurrentTime(blocks, dateISO) {
    const now = new Date();
    if (isoDate(now) !== dateISO) return blocks;

    // Keep blocks whose END is at least 10 minutes from now (still actionable)
    const stillReachable = blocks.filter(b => {
      const endD = parseHM(b.end, now);
      return endD.getTime() - now.getTime() > 10 * 60 * 1000;
    });

    if (stillReachable.length >= 2) return blocks; // morning/early enough — keep full plan

    // Late start: build short blocks from now → bedtime (default 23:30).
    const bedtimeD = new Date(now.getTime()); bedtimeD.setHours(23, 30, 0, 0);
    const minutesLeft = Math.floor((bedtimeD - now) / 60000);

    if (minutesLeft < 20) {
      // Almost bedtime — single 15-min sweep
      const startD = new Date(now.getTime() + 5 * 60 * 1000);
      const endD = new Date(startD.getTime() + 15 * 60 * 1000);
      return [{
        id: `${dateISO}__late`,
        start: fmtHM(startD), end: fmtHM(endD),
        title: 'Quick sweep · Top misses',
        kind: 'boss', deckId: 'all',
        target: { cardsSeen: 10 },
        note: 'Late start — 15-min focused pass before sleep',
      }];
    }

    // Compress: pick high-priority blocks from the original plan, pack them
    // back-to-back from now+5min toward bedtime.
    // Priority: 'now'/upcoming targeted blocks > review blocks > anything else.
    const prioritized = blocks
      .map(b => ({ ...b, priority: b.target?.cardsSeen ? 1 : b.target?.stimQs ? 2 : 3 }))
      .sort((a, b) => a.priority - b.priority);

    const compressed = [];
    let cursor = new Date(now.getTime() + 5 * 60 * 1000);
    let i = 0;
    while (i < prioritized.length && (bedtimeD - cursor) > 15 * 60 * 1000) {
      const src = prioritized[i++];
      // 25-min default, shorter if running out of time
      const remain = Math.floor((bedtimeD - cursor) / 60000);
      const dur = Math.min(30, Math.max(15, Math.floor(remain / Math.max(1, prioritized.length - i + 1))));
      const end = new Date(cursor.getTime() + dur * 60 * 1000);
      compressed.push({
        id: `${dateISO}__c${i}`,
        start: fmtHM(cursor),
        end: fmtHM(end),
        title: src.title,
        kind: src.kind,
        deckId: src.deckId,
        target: src.target ? {
          cardsSeen: src.target.cardsSeen ? Math.max(8, Math.round(src.target.cardsSeen * (dur / 45))) : undefined,
          stimQs: src.target.stimQs ? Math.max(5, Math.round(src.target.stimQs * (dur / 45))) : undefined,
        } : {},
        note: (src.note || '') + ' · compressed for late start',
      });
      cursor = new Date(end.getTime() + 5 * 60 * 1000); // 5min buffer between blocks
    }
    if (compressed.length === 0) {
      // Fallback: single 25-min block
      const startD = new Date(now.getTime() + 5 * 60 * 1000);
      const endD = new Date(startD.getTime() + 25 * 60 * 1000);
      compressed.push({
        id: `${dateISO}__late0`,
        start: fmtHM(startD), end: fmtHM(endD),
        title: 'Focus block',
        kind: 'flash', deckId: 'all',
        target: { cardsSeen: 15 },
        note: 'Late start — focused pass',
      });
    }
    return compressed;
  }

  function ensureTodayPlan() {
    const now = new Date();
    const todayISO = isoDate(now);

    let state = load(KEY_STATE, null);
    if (!state) {
      state = { examDate: EXAM_ISO, examName: EXAM_NAME, plansByDay: {}, completion: {}, visible: true };
    }
    // Read the examDate from state (user may have changed it), not the hardcoded constant
    const examDateStr = state.examDate || EXAM_ISO;
    const exam = new Date(examDateStr + 'T08:00:00');
    const daysOut = daysBetween(now, exam);

    const existing = state.plansByDay[todayISO];
    const needsRegen =
      !existing ||
      !Array.isArray(existing.blocks) ||
      existing.blocks.length === 0 ||
      (existing.schemaVersion || 0) < PLAN_SCHEMA ||
      (existing.examDateAtCreate && existing.examDateAtCreate !== examDateStr);

    if (needsRegen) {
      const rawBlocks = generateDayBlocks(daysOut, todayISO);
      const blocks = adaptBlocksForCurrentTime(rawBlocks, todayISO);
      state.plansByDay[todayISO] = {
        blocks,
        baselineCards: existing?.baselineCards ?? totalCardsSeen(),
        baselineStim: existing?.baselineStim ?? totalStimAnswered(),
        compressed: blocks !== rawBlocks,
        examDateAtCreate: examDateStr,
        schemaVersion: PLAN_SCHEMA,
      };
      // Drop completion entries for regenerated blocks (block IDs may have shifted)
      const oldIds = new Set((existing?.blocks || []).map(b => b.id));
      Object.keys(state.completion || {}).forEach(k => {
        if (oldIds.has(k)) delete state.completion[k];
      });
    }
    save(KEY_STATE, state);
    return { state, todayISO, daysOut };
  }

  // ============================================================ block status

  function blockStatus(block, dateISO, state) {
    const now = new Date();
    if (isoDate(now) !== dateISO) return 'unknown';
    const startD = parseHM(block.start, now);
    const endD = parseHM(block.end, now);
    const c = (state.completion || {})[block.id];
    if (c && c.hit) return 'done';

    if (now < startD) return 'upcoming';
    if (now >= startD && now <= endD) return 'now';
    // past end time
    if (block.kind === 'rest') return 'done';
    if (c && c.completedAt) return 'done';
    if (block.target?.cardsSeen || block.target?.stimQs) return 'missed';
    return 'missed';
  }

  // Detect activity-driven completion: cardsSeen or stimQs since plan start
  function checkBlockCompletion(state, dateISO) {
    const plan = state.plansByDay[dateISO];
    if (!plan) return false;
    let changed = false;
    const now = new Date();
    plan.blocks.forEach(block => {
      const target = block.target || {};
      if (!target.cardsSeen && !target.stimQs) return;
      const completion = state.completion[block.id] || {};
      if (completion.hit) return;

      const startD = parseHM(block.start, now);
      // only count activity FROM block start onward
      const activeFromTs = startD.getTime();
      // We approximate: read total counters, subtract baseline at plan creation,
      // and additionally store per-block baselines once block enters 'now'.
      if (now >= startD && !completion.startedAt) {
        completion.startedAt = now.getTime();
        completion.cardsAtStart = totalCardsSeen();
        completion.stimAtStart = totalStimAnswered();
        state.completion[block.id] = completion;
        changed = true;
      }

      if (completion.startedAt) {
        const cardsDelta = totalCardsSeen() - (completion.cardsAtStart || 0);
        const stimDelta = totalStimAnswered() - (completion.stimAtStart || 0);
        let hit = false;
        if (target.cardsSeen && cardsDelta >= target.cardsSeen) hit = true;
        if (target.stimQs && stimDelta >= target.stimQs) hit = true;
        if (hit) {
          completion.hit = true;
          completion.completedAt = now.getTime();
          completion.cardsAtEnd = totalCardsSeen();
          completion.stimAtEnd = totalStimAnswered();
          state.completion[block.id] = completion;
          changed = true;
        }
      }
    });
    if (changed) save(KEY_STATE, state);
    return changed;
  }

  // Stack missed blocks: append shadow blocks for missed-but-targeted items.
  // Just renders them as overflow at the bottom — doesn't mutate stored plan.
  function buildOverflow(blocks, dateISO, state) {
    const now = new Date();
    if (isoDate(now) !== dateISO) return [];
    const out = [];
    blocks.forEach(b => {
      if (blockStatus(b, dateISO, state) === 'missed' && (b.target?.cardsSeen || b.target?.stimQs)) {
        out.push({ ...b, isOverflow: true });
      }
    });
    return out;
  }

  // ============================================================ rendering

  const COLORS = {
    bg: '#14171d', bgSunk: '#090a0e', rule: '#22262f', ruleStrong: '#2e333d',
    ink: '#e6dfd0', inkDim: '#a59a83', inkFaint: '#6b6353',
    accent: '#c89b2e', accentInk: '#f1d278', accentSoft: '#5b4412',
    miss: '#c25d52', shaky: '#c89b2e', got: '#5fa871', upcoming: '#6b6353', now: '#7fb6e0',
  };

  function injectStyles() {
    if (document.getElementById('sp-styles')) return;
    const css = document.createElement('style');
    css.id = 'sp-styles';
    css.textContent = `
      .sp-fab {
        position: fixed; right: 18px; bottom: 18px; z-index: 990;
        background: ${COLORS.accent}; color: ${COLORS.bg};
        border: none; border-radius: 24px; padding: 10px 16px;
        font-family: 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600;
        cursor: pointer; box-shadow: 0 6px 24px rgba(0,0,0,0.35);
        display: flex; gap: 8px; align-items: center;
      }
      .sp-fab:hover { background: ${COLORS.accentInk}; }
      .sp-fab .sp-fab-clock { font-variant-numeric: tabular-nums; opacity: 0.85; font-weight: 500; }
      .sp-fab .sp-fab-dot { width: 8px; height: 8px; border-radius: 50%; background: ${COLORS.bg}; opacity: 0.6; }

      .sp-panel {
        position: fixed; right: 18px; bottom: 18px; z-index: 991;
        width: 360px; max-height: 80vh; overflow-y: auto;
        background: ${COLORS.bg};
        color: ${COLORS.ink};
        border: 1px solid ${COLORS.rule};
        border-radius: 12px;
        font-family: 'Inter', system-ui, sans-serif;
        box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      }
      .sp-head {
        padding: 14px 16px 10px; border-bottom: 1px solid ${COLORS.rule};
        display: flex; justify-content: space-between; align-items: baseline;
      }
      .sp-head-title {
        font-family: 'Fraunces', Georgia, serif; font-size: 16px; font-weight: 600;
      }
      .sp-head-clock {
        font-variant-numeric: tabular-nums;
        font-size: 13px; color: ${COLORS.inkDim};
      }
      .sp-head-x {
        background: none; border: none; color: ${COLORS.inkDim};
        font-size: 18px; cursor: pointer; padding: 0 4px;
      }
      .sp-head-x:hover { color: ${COLORS.ink}; }
      .sp-meta {
        display: flex; justify-content: space-between;
        padding: 8px 16px; font-size: 11px; color: ${COLORS.inkDim};
        border-bottom: 1px solid ${COLORS.rule};
        text-transform: uppercase; letter-spacing: 0.06em;
      }
      .sp-meta strong { color: ${COLORS.accentInk}; font-weight: 600; }
      .sp-meta-countdown { color: ${COLORS.accent}; font-weight: 700; }

      .sp-coverage {
        padding: 10px 16px 12px;
        border-bottom: 1px solid ${COLORS.rule};
        display: flex; flex-direction: column; gap: 6px;
      }
      .sp-coverage-row {
        display: flex; justify-content: space-between; align-items: baseline;
        font-size: 11px; color: ${COLORS.inkDim};
      }
      .sp-coverage-lbl {
        text-transform: uppercase; letter-spacing: 0.08em;
        font-weight: 600; color: ${COLORS.inkFaint};
      }
      .sp-coverage-num { font-variant-numeric: tabular-nums; }
      .sp-coverage-num strong { color: ${COLORS.ink}; font-size: 14px; font-weight: 700; }
      .sp-coverage-pct {
        margin-left: 6px;
        color: ${COLORS.accentInk};
        font-weight: 700;
      }
      .sp-coverage-bar {
        height: 6px;
        background: ${COLORS.bgSunk};
        border-radius: 3px;
        overflow: hidden;
        display: flex;
      }
      .sp-coverage-bar-mastered {
        height: 100%;
        background: ${COLORS.got};
        transition: width 0.3s;
      }
      .sp-coverage-bar-touched {
        height: 100%;
        background: ${COLORS.shaky};
        opacity: 0.55;
        transition: width 0.3s;
      }
      .sp-coverage-sub {
        font-size: 10px; text-transform: uppercase;
        letter-spacing: 0.06em;
      }
      .sp-coverage-mastered { color: ${COLORS.got}; font-weight: 700; }
      .sp-coverage-todo { color: ${COLORS.inkFaint}; }

      .sp-stats {
        display: grid; grid-template-columns: 1fr 1fr 1fr;
        padding: 10px 16px; gap: 6px;
        border-bottom: 1px solid ${COLORS.rule};
      }
      .sp-stat { display: flex; flex-direction: column; gap: 2px; }
      .sp-stat-num { font-size: 16px; font-weight: 700; color: ${COLORS.ink}; font-variant-numeric: tabular-nums; }
      .sp-stat-lbl { font-size: 9px; color: ${COLORS.inkFaint}; text-transform: uppercase; letter-spacing: 0.08em; }

      .sp-blocks { padding: 6px 0; }
      .sp-block {
        padding: 10px 16px; border-left: 3px solid transparent;
        cursor: pointer; transition: background 0.15s;
      }
      .sp-block:hover { background: ${COLORS.bgSunk}; }
      .sp-block.now { border-left-color: ${COLORS.accent}; background: rgba(200, 155, 46, 0.08); }
      .sp-block.done { border-left-color: ${COLORS.got}; opacity: 0.7; }
      .sp-block.missed { border-left-color: ${COLORS.miss}; background: rgba(194, 93, 82, 0.08); }
      .sp-block.upcoming { border-left-color: ${COLORS.rule}; }

      .sp-block-row1 {
        display: flex; justify-content: space-between; align-items: baseline;
        gap: 8px; margin-bottom: 3px;
      }
      .sp-block-time {
        font-variant-numeric: tabular-nums; font-size: 11px; color: ${COLORS.inkDim};
        font-weight: 600;
      }
      .sp-block-title { font-size: 13px; font-weight: 600; color: ${COLORS.ink}; flex: 1; }
      .sp-block-status {
        font-size: 9px; text-transform: uppercase; letter-spacing: 0.1em;
        padding: 2px 6px; border-radius: 3px; font-weight: 700;
      }
      .sp-block.now .sp-block-status { color: ${COLORS.accentInk}; background: ${COLORS.accentSoft}; }
      .sp-block.done .sp-block-status { color: ${COLORS.got}; background: rgba(95, 168, 113, 0.15); }
      .sp-block.missed .sp-block-status { color: ${COLORS.miss}; background: rgba(194, 93, 82, 0.15); }
      .sp-block.upcoming .sp-block-status { color: ${COLORS.inkFaint}; }

      .sp-block-note {
        font-size: 11px; color: ${COLORS.inkDim};
        margin-top: 2px; line-height: 1.35;
      }
      .sp-block-progress {
        margin-top: 6px; height: 4px; background: ${COLORS.bgSunk};
        border-radius: 2px; overflow: hidden;
      }
      .sp-block-progress-bar { height: 100%; background: ${COLORS.accent}; transition: width 0.3s; }

      .sp-overflow-head {
        padding: 12px 16px 4px; font-size: 10px;
        text-transform: uppercase; letter-spacing: 0.12em;
        color: ${COLORS.miss}; font-weight: 700;
        border-top: 1px solid ${COLORS.rule}; margin-top: 6px;
      }
      .sp-foot {
        padding: 8px 16px; border-top: 1px solid ${COLORS.rule};
        font-size: 10px; color: ${COLORS.inkFaint};
        display: flex; justify-content: space-between;
      }
      .sp-foot a, .sp-foot button {
        color: ${COLORS.inkDim}; background: none; border: none;
        cursor: pointer; font-size: 10px; padding: 0;
      }
      .sp-foot a:hover, .sp-foot button:hover { color: ${COLORS.accentInk}; }
    `;
    document.head.appendChild(css);
  }

  function statusLabel(status) {
    return ({ now: 'NOW', done: 'DONE', missed: 'MISS', upcoming: 'NEXT' })[status] || '';
  }

  function blockProgressPct(block, state) {
    const c = state.completion[block.id];
    if (!c || !c.startedAt) return 0;
    const target = block.target || {};
    if (target.cardsSeen) {
      const delta = totalCardsSeen() - (c.cardsAtStart || 0);
      return Math.min(100, Math.round((delta / target.cardsSeen) * 100));
    }
    if (target.stimQs) {
      const delta = totalStimAnswered() - (c.stimAtStart || 0);
      return Math.min(100, Math.round((delta / target.stimQs) * 100));
    }
    return 0;
  }

  function renderPanel(root, state, todayISO, daysOut) {
    const now = new Date();
    const plan = state.plansByDay[todayISO];
    const blocks = plan.blocks.map(b => ({ ...b, status: blockStatus(b, todayISO, state) }));
    const overflow = buildOverflow(plan.blocks, todayISO, state).map(b => ({ ...b, status: 'missed' }));

    const examDate = new Date(state.examDate + 'T08:00:00');
    const dayLabel = daysOut === 0 ? 'EXAM DAY' :
                    daysOut === 1 ? '1 day' :
                    daysOut < 0 ? 'past exam' :
                    `${daysOut} days`;

    const cardsToday = state.plansByDay[todayISO]
      ? Math.max(0, totalCardsSeen() - (state.plansByDay[todayISO].baselineCards || 0))
      : 0;
    const stimToday = state.plansByDay[todayISO]
      ? Math.max(0, totalStimAnswered() - (state.plansByDay[todayISO].baselineStim || 0))
      : 0;

    const blockHTML = (b) => {
      const t = b.target || {};
      const targetTxt = t.cardsSeen ? `${t.cardsSeen} cards` : t.stimQs ? `${t.stimQs} Qs` : '';
      const pct = blockProgressPct(b, state);
      const showProgress = (t.cardsSeen || t.stimQs) && (b.status === 'now' || (b.status === 'missed' && pct > 0));
      return `
        <div class="sp-block ${b.status}" data-block="${escHTML(b.id)}">
          <div class="sp-block-row1">
            <span class="sp-block-time">${escHTML(b.start)}–${escHTML(b.end)}</span>
            <span class="sp-block-title">${escHTML(b.title)}</span>
            <span class="sp-block-status">${statusLabel(b.status)}</span>
          </div>
          ${b.note ? `<div class="sp-block-note">${escHTML(b.note)}${targetTxt ? ` · target ${targetTxt}` : ''}</div>` : ''}
          ${showProgress ? `<div class="sp-block-progress"><div class="sp-block-progress-bar" style="width:${pct}%"></div></div>` : ''}
        </div>
      `;
    };

    const cov = deckCoverage();
    const coveredPct = cov.total ? Math.round((cov.covered / cov.total) * 100) : 0;
    const masteredPct = cov.total ? Math.round((cov.mastered / cov.total) * 100) : 0;

    root.innerHTML = `
      <div class="sp-head">
        <span class="sp-head-title">Today's plan</span>
        <span class="sp-head-clock" id="spClock">${fmtClock(now)}</span>
        <button class="sp-head-x" id="spClose" title="Hide">×</button>
      </div>
      <div class="sp-meta">
        <span><strong>${fmtDate(now)}</strong></span>
        <span class="sp-meta-countdown">${dayLabel} to ${escHTML(state.examName || 'exam')}</span>
      </div>
      <div class="sp-coverage" title="Cards you've touched at least once · cards in Got-it state">
        <div class="sp-coverage-row">
          <span class="sp-coverage-lbl">Cards covered</span>
          <span class="sp-coverage-num"><strong>${cov.covered}</strong> / ${cov.total} <span class="sp-coverage-pct">${coveredPct}%</span></span>
        </div>
        <div class="sp-coverage-bar">
          <div class="sp-coverage-bar-mastered" style="width:${masteredPct}%" title="${cov.mastered} mastered (${masteredPct}%)"></div>
          <div class="sp-coverage-bar-touched" style="width:${coveredPct - masteredPct}%" title="${cov.covered - cov.mastered} seen but not mastered"></div>
        </div>
        <div class="sp-coverage-row sp-coverage-sub">
          <span class="sp-coverage-mastered">● ${cov.mastered} mastered</span>
          <span class="sp-coverage-todo">${Math.max(0, cov.total - cov.covered)} untouched</span>
        </div>
      </div>
      <div class="sp-stats">
        <div class="sp-stat"><span class="sp-stat-num" id="spCardsToday">${cardsToday}</span><span class="sp-stat-lbl">Cards today</span></div>
        <div class="sp-stat"><span class="sp-stat-num" id="spStimToday">${stimToday}</span><span class="sp-stat-lbl">Stim Qs today</span></div>
        <div class="sp-stat"><span class="sp-stat-num">${cardsMissedToday()}</span><span class="sp-stat-lbl">Misses today</span></div>
      </div>
      <div class="sp-blocks">
        ${blocks.map(blockHTML).join('')}
      </div>
      ${overflow.length ? `
        <div class="sp-overflow-head">⚠ Stacked from missed blocks · ${
          (() => {
            let cards = 0, qs = 0;
            overflow.forEach(b => {
              cards += (b.target?.cardsSeen || 0);
              qs += (b.target?.stimQs || 0);
            });
            const parts = [];
            if (cards) parts.push(cards + ' cards');
            if (qs) parts.push(qs + ' Qs');
            return parts.join(' + ') + ' carried over';
          })()
        }</div>
        <div class="sp-blocks">${overflow.map(blockHTML).join('')}</div>
      ` : ''}
      <div class="sp-mastery-host" id="spMasteryHost"></div>
      <div class="sp-foot">
        <button id="spReset">Reset today</button>
        <button id="spChangeDate">Set exam date</button>
      </div>
    `;

    const closeBtn = root.querySelector('#spClose');
    if (closeBtn) closeBtn.addEventListener('click', () => {
      state.visible = false; save(KEY_STATE, state);
      mountFAB(state, todayISO, daysOut);
    });

    const resetBtn = root.querySelector('#spReset');
    if (resetBtn) resetBtn.addEventListener('click', () => {
      if (!confirm('Regenerate today\'s plan? Completion progress will be cleared.')) return;
      delete state.plansByDay[todayISO];
      // Clear today's completion entries
      Object.keys(state.completion || {}).forEach(k => {
        if (k.startsWith(todayISO + '__')) delete state.completion[k];
      });
      save(KEY_STATE, state);
      mountWidget();
    });

    const changeBtn = root.querySelector('#spChangeDate');
    if (changeBtn) changeBtn.addEventListener('click', () => {
      const next = prompt('Exam date (YYYY-MM-DD):', state.examDate);
      if (next && /^\d{4}-\d{2}-\d{2}$/.test(next)) {
        state.examDate = next;
        // Clear forward plans only — keep history
        const todayD = new Date();
        Object.keys(state.plansByDay).forEach(d => {
          if (new Date(d + 'T00:00:00') >= todayD) delete state.plansByDay[d];
        });
        save(KEY_STATE, state);
        mountWidget();
      }
    });

    // Click a block: navigate / launch the matching mode
    root.querySelectorAll('.sp-block').forEach(el => {
      el.addEventListener('click', (e) => {
        const id = el.dataset.block;
        const block = blocks.find(b => b.id === id) || overflow.find(b => b.id === id);
        if (!block) return;
        launchBlock(block);
      });
    });

    // Render mastery heat-map compact view
    const masteryHost = root.querySelector('#spMasteryHost');
    if (masteryHost && window.masteryMap) {
      masteryHost.classList.add('mh-section');
      window.masteryMap.compact(masteryHost);
    }
  }

  function launchBlock(block) {
    if (block.kind === 'flash' || block.kind === 'boss') {
      // Persist preferred deck + cardCount for the Leitner setup screen
      const targetCards = block.target?.cardsSeen || 50;
      // Snap to one of the preset chips so the setup UI shows a selection
      const presets = [25, 50, 100, 999];
      const snapped = presets.reduce((best, p) =>
        Math.abs(p - targetCards) < Math.abs(best - targetCards) ? p : best, presets[0]);
      const prev = load('leitner-settings-v1', {}) || {};
      const settings = Object.assign({}, prev, {
        deckId: block.deckId || 'all',
        cardCount: snapped,
      });
      try { localStorage.setItem('leitner-settings-v1', JSON.stringify(settings)); } catch (e) {}
      const flashBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Flash');
      if (flashBtn) flashBtn.click();
      return;
    }
    if (block.kind === 'stim') {
      const stimBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Stim');
      if (stimBtn) stimBtn.click();
      return;
    }
    if (block.kind === 'review') {
      // Open cheatsheet in new tab as a default review action
      window.open('/cheatsheet.html', '_blank');
      return;
    }
    // 'rest' / unknown — no-op
  }

  function mountFAB(state, todayISO, daysOut) {
    let fab = document.getElementById('spFab');
    let panel = document.getElementById('spPanel');
    if (panel) panel.remove();
    if (!fab) {
      fab = document.createElement('button');
      fab.id = 'spFab'; fab.className = 'sp-fab';
      document.body.appendChild(fab);
      fab.addEventListener('click', () => {
        state.visible = true; save(KEY_STATE, state);
        mountWidget();
      });
    }
    const now = new Date();
    fab.innerHTML = `<span class="sp-fab-dot"></span><span>Plan</span><span class="sp-fab-clock">${fmtHM(now)}</span>`;
  }

  function mountWidget() {
    const { state, todayISO, daysOut } = ensureTodayPlan();
    injectStyles();

    let fab = document.getElementById('spFab'); if (fab) fab.remove();
    let panel = document.getElementById('spPanel'); if (panel) panel.remove();

    if (!state.visible) { mountFAB(state, todayISO, daysOut); return; }

    panel = document.createElement('div');
    panel.id = 'spPanel'; panel.className = 'sp-panel';
    document.body.appendChild(panel);
    renderPanel(panel, state, todayISO, daysOut);
  }

  // ============================================================ ticker

  function tick() {
    const now = new Date();
    const clockEl = document.getElementById('spClock');
    if (clockEl) clockEl.textContent = fmtClock(now);

    const fabClockEl = document.querySelector('.sp-fab-clock');
    if (fabClockEl) fabClockEl.textContent = fmtHM(now);
  }

  function reEvaluate() {
    const { state, todayISO } = ensureTodayPlan();
    const changed = checkBlockCompletion(state, todayISO);
    // Re-render if something changed OR if a block's status (now/missed) flipped due to time
    const panel = document.getElementById('spPanel');
    if (panel && state.visible) {
      // Always re-render so block status reflects current time
      renderPanel(panel, state, todayISO, daysBetween(new Date(), new Date(state.examDate + 'T08:00:00')));
    }
  }

  // ============================================================ boot

  function boot() {
    mountWidget();
    setInterval(tick, 1000);
    setInterval(reEvaluate, 30 * 1000);

    // Re-render on Leitner / Stim activity (best-effort: poll every 5s while visible)
    setInterval(() => {
      const panel = document.getElementById('spPanel');
      if (!panel) return;
      const { state, todayISO } = ensureTodayPlan();
      const cardsEl = document.getElementById('spCardsToday');
      const stimEl = document.getElementById('spStimToday');
      if (cardsEl) {
        const baseline = state.plansByDay[todayISO]?.baselineCards || 0;
        cardsEl.textContent = String(Math.max(0, totalCardsSeen() - baseline));
      }
      if (stimEl) {
        const baseline = state.plansByDay[todayISO]?.baselineStim || 0;
        stimEl.textContent = String(Math.max(0, totalStimAnswered() - baseline));
      }
      checkBlockCompletion(state, todayISO);
    }, 5000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  // expose for debugging
  window.studyPlan = {
    state: () => load(KEY_STATE, null),
    reset: () => { localStorage.removeItem(KEY_STATE); mountWidget(); },
    setExamDate: (iso) => {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(iso)) { console.warn('setExamDate: expected YYYY-MM-DD, got', iso); return; }
      const s = load(KEY_STATE, null) || {};
      s.examDate = iso;
      // Clear forward plans so they regenerate against the new exam date
      const todayD = new Date(); todayD.setHours(0, 0, 0, 0);
      Object.keys(s.plansByDay || {}).forEach(d => {
        if (new Date(d + 'T00:00:00') >= todayD) delete s.plansByDay[d];
      });
      save(KEY_STATE, s);
      mountWidget();
    },
    setExamName: (name) => {
      const s = load(KEY_STATE, null) || {}; s.examName = name; save(KEY_STATE, s); mountWidget();
    },
  };

  console.log('[study-plan] widget mounted. studyPlan.state() / .reset() / .setExamDate(iso)');
})();
