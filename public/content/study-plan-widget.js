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
  const KEY_LEITNER_HIST = 'leitner-history-v1';
  const KEY_LEITNER_PROG = 'leitner-progress-v1';
  const KEY_LEITNER_SESS = 'leitner-session-v1';
  const KEY_STIM_SESS = 'evol_stim_session';

  const EXAM_ISO = '2026-05-04'; // Monday
  const EXAM_NAME = 'BIOL 4230 Exam 2';

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
    // 4-day plan tuned for Exam 2 (Ch 10-16, L08/L09/L11/L12/L13).
    const id = (k) => `${dateISO}__${k}`;
    if (daysOut >= 4) {
      // Today (Thu) — Exam-2 chapter sweep (heaviest day)
      return [
        { id: id('a'), start: '09:00', end: '09:45', title: 'L08 Flash · Complex Adaptations', kind: 'flash', deckId: 'L08', target: { cardsSeen: 26 }, note: 'eye, regulatory, Hox, heterochrony' },
        { id: id('b'), start: '11:00', end: '11:45', title: 'L09 + L11 Flash · Coevolution + Sex', kind: 'flash', deckId: 'all', target: { cardsSeen: 38 }, note: 'mutualism, mimicry, anisogamy, sexual conflict' },
        { id: id('c'), start: '14:00', end: '14:45', title: 'L12 Flash · Life History', kind: 'flash', deckId: 'L12', target: { cardsSeen: 19 }, note: 'tradeoffs, senescence theories, r/K, Seychelles' },
        { id: id('d'), start: '16:00', end: '16:45', title: 'L13 Flash · Social Behavior', kind: 'flash', deckId: 'L13', target: { cardsSeen: 21 }, note: 'Hamilton, ESS, RPS lizards, reciprocity' },
        { id: id('e'), start: '19:30', end: '20:15', title: 'Stim · 20 Exam-2 Qs', kind: 'stim', target: { stimQs: 20 }, note: 'mixed L08-L13' },
      ];
    }
    if (daysOut === 3) {
      // Fri — Boss Mode + cumulative review + first full Stim
      return [
        { id: id('a'), start: '09:00', end: '09:30', title: 'Boss Mode · yesterday\'s misses', kind: 'boss', target: { cardsSeen: 15 }, note: 'today\'s misses + shakies' },
        { id: id('b'), start: '11:00', end: '12:00', title: 'Cumulative Flash · L02-L05 review', kind: 'flash', deckId: 'all', target: { cardsSeen: 50 }, note: 'HWE math, selection types, Darwin' },
        { id: id('c'), start: '14:00', end: '14:45', title: 'L11 + L12 mixed Flash', kind: 'flash', deckId: 'all', target: { cardsSeen: 30 }, note: 'sexual selection + life history' },
        { id: id('d'), start: '16:00', end: '17:00', title: 'Stim · 30 Exam-2 Qs', kind: 'stim', target: { stimQs: 30 }, note: 'full Exam-2 mix' },
        { id: id('e'), start: '19:30', end: '20:30', title: 'L05 + L13 final pass', kind: 'flash', deckId: 'all', target: { cardsSeen: 35 }, note: 'breeder eq, ESS, Hamilton' },
      ];
    }
    if (daysOut === 2) {
      // Sat — Mock exam day
      return [
        { id: id('a'), start: '09:00', end: '10:00', title: 'Mock Exam 2 · Stim 50 Qs', kind: 'stim', target: { stimQs: 50 }, note: 'simulate exam conditions' },
        { id: id('b'), start: '10:30', end: '11:00', title: 'Review missed Stim Qs', kind: 'review', target: { cardsSeen: 15 }, note: 'understand each miss' },
        { id: id('c'), start: '14:00', end: '15:00', title: 'Boss Mode · top misses', kind: 'boss', target: { cardsSeen: 30 }, note: 'leech-flagged + repeat misses' },
        { id: id('d'), start: '16:00', end: '16:45', title: 'Cheatsheet skim · flag weak', kind: 'review', target: {}, note: 'note any concept still murky' },
        { id: id('e'), start: '19:30', end: '20:00', title: 'L08-L13 quick sweep', kind: 'flash', deckId: 'all', target: { cardsSeen: 40 }, note: 'fast pace, anything unsure → mark' },
      ];
    }
    if (daysOut === 1) {
      // Sun — Light load, top misses only
      return [
        { id: id('a'), start: '10:00', end: '10:45', title: 'Top misses · Boss Mode', kind: 'boss', target: { cardsSeen: 25 }, note: 'final cleanup' },
        { id: id('b'), start: '14:00', end: '14:30', title: 'Cheatsheet read-through', kind: 'review', target: {}, note: 'aloud if possible' },
        { id: id('c'), start: '16:00', end: '16:30', title: '5 Stim Qs per Exam-2 lecture', kind: 'stim', target: { stimQs: 25 }, note: 'sanity check across L08-L13' },
        { id: id('d'), start: '19:30', end: '19:50', title: 'Light flash · all decks (20)', kind: 'flash', deckId: 'all', target: { cardsSeen: 20 }, note: 'short, low-stress, sleep early' },
      ];
    }
    if (daysOut === 0) {
      // Exam day — rest, maybe one cheatsheet skim
      return [
        { id: id('a'), start: '08:00', end: '08:20', title: 'Cheatsheet final skim', kind: 'review', target: {}, note: '~1 hr before exam · quick pass · NO new content' },
        { id: id('b'), start: '09:00', end: '09:00', title: 'EXAM · ' + EXAM_NAME, kind: 'rest', target: {}, note: 'good luck!' },
      ];
    }
    if (daysOut < 0) {
      return [
        { id: id('a'), start: '12:00', end: '12:00', title: 'Exam done · plan exhausted', kind: 'rest', target: {}, note: 'add a new exam date in study-plan-v1 to refresh' },
      ];
    }
    // 5+ days out — generic study block
    return [
      { id: id('a'), start: '10:00', end: '10:45', title: 'Daily review', kind: 'flash', deckId: 'all', target: { cardsSeen: 30 } },
      { id: id('b'), start: '15:00', end: '15:30', title: 'Stim 15', kind: 'stim', target: { stimQs: 15 } },
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

    if (!state.plansByDay[todayISO] || !Array.isArray(state.plansByDay[todayISO].blocks) || state.plansByDay[todayISO].blocks.length === 0) {
      const rawBlocks = generateDayBlocks(daysOut, todayISO);
      const blocks = adaptBlocksForCurrentTime(rawBlocks, todayISO);
      state.plansByDay[todayISO] = {
        blocks,
        baselineCards: totalCardsSeen(),
        baselineStim: totalStimAnswered(),
        compressed: blocks !== rawBlocks,
        examDateAtCreate: examDateStr, // track what we generated for
      };
    } else if (state.plansByDay[todayISO].examDateAtCreate &&
               state.plansByDay[todayISO].examDateAtCreate !== examDateStr) {
      // Exam date changed since this plan was generated → regenerate
      const rawBlocks = generateDayBlocks(daysOut, todayISO);
      const blocks = adaptBlocksForCurrentTime(rawBlocks, todayISO);
      state.plansByDay[todayISO] = {
        blocks,
        baselineCards: state.plansByDay[todayISO].baselineCards,
        baselineStim: state.plansByDay[todayISO].baselineStim,
        compressed: blocks !== rawBlocks,
        examDateAtCreate: examDateStr,
      };
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
      // Persist preferred deck + minutes for the Leitner setup screen
      const minutes = (() => {
        const [sh, sm] = block.start.split(':').map(Number);
        const [eh, em] = block.end.split(':').map(Number);
        const total = (eh * 60 + em) - (sh * 60 + sm);
        if (total <= 12) return 10;
        if (total <= 25) return 20;
        return 30;
      })();
      const settings = { deckId: block.deckId || 'all', minutes };
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
