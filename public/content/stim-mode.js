/* Stim Mode — practice exam simulator with Grade-with-Claude flow.
   Reads window.STIM_BANK / window.STIM_INDEX (loaded from stim-bank.js).
   Persists state to localStorage under evol_stim_session, evol_stim_history, evol_stim_topic_stats. */
(function () {
  'use strict';

  const LS_SESSION = 'evol_stim_session';
  const LS_HISTORY = 'evol_stim_history';
  const LS_STATS   = 'evol_stim_topic_stats';
  const LS_SETTINGS = 'evol_stim_settings';
  const LS_DASH    = 'evol_stim_dash_prefs';
  const LS_REVIEW  = 'evol_stim_review_filter';
  const LS_MIG_FULL_BANK = 'evol_stim_mig_full_bank_v2';

  // -------- helpers --------
  const $ = sel => document.querySelector(sel);
  const root = () => document.getElementById('stimRoot');
  const esc = s => String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

  function loadJSON(key, fallback) {
    try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; }
    catch (e) { return fallback; }
  }
  function saveJSON(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
  }
  function shuffleSeeded(arr, seed) {
    // Mulberry32 deterministic shuffle by seed string
    let h = 1779033703 ^ seed.length;
    for (let i = 0; i < seed.length; i++) {
      h = Math.imul(h ^ seed.charCodeAt(i), 3432918353);
      h = h << 13 | h >>> 19;
    }
    let s = h >>> 0;
    function rand() { s |= 0; s = s + 0x6D2B79F5 | 0; let t = Math.imul(s ^ s >>> 15, 1 | s); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(rand() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  // -------- state --------
  let session = null; // { id, exam, count, type, timer_sec, started_at, current, answers, flags, finished, results }
  let timerHandle = null;

  function bankReady() { return Array.isArray(window.STIM_BANK) && window.STIM_BANK.length > 0; }

  // -------- entry point --------
  window.StimMode = {
    activate: function () {
      if (!bankReady()) {
        renderEmpty();
        return;
      }
      // One-time migration: reset any in-progress adaptive session so it
      // restarts against the full question bank (old sessions were capped
      // by exam/lecture/count filters).
      try {
        if (!localStorage.getItem(LS_MIG_FULL_BANK)) {
          const existing = loadJSON(LS_SESSION, null);
          if (existing && existing.adaptive && !existing.finished) {
            localStorage.removeItem(LS_SESSION);
          }
          localStorage.setItem(LS_MIG_FULL_BANK, '1');
        }
      } catch (e) {}
      session = loadJSON(LS_SESSION, null);
      if (session && !session.finished) {
        renderExam();
      } else if (session && session.finished) {
        renderResults();
      } else {
        renderSetup();
      }
      try { window.scrollTo({ top: 0, behavior: 'instant' }); } catch (e) { window.scrollTo(0, 0); }
    },
    deactivate: function () {
      if (timerHandle) clearInterval(timerHandle);
      timerHandle = null;
    }
  };

  // -------- empty state --------
  function renderEmpty() {
    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-eyebrow">Stim Mode</div>
        <h1 class="stim-title">Question bank not loaded</h1>
        <p class="stim-subtitle">The Stim question bank file is missing or empty. Run <code>python scripts/merge-stim-bank.py</code> to generate it.</p>
      </div>`;
  }

  // -------- setup view --------
  function renderSetup() {
    const settings = loadJSON(LS_SETTINGS, { exam: 1, count: 25, type: 'mixed', timer: 0, lecture: 'all' });
    // Migrate: legacy single-string lecture -> array; empty -> 'all'
    if (!settings.lecture) settings.lecture = 'all';
    if (typeof settings.lecture === 'string' && settings.lecture !== 'all') {
      settings.lecture = [settings.lecture];
    }
    if (Array.isArray(settings.lecture) && settings.lecture.length === 0) {
      settings.lecture = 'all';
    }
    const stats = computeStats();

    const selectedLectures = Array.isArray(settings.lecture) ? settings.lecture : [];
    const lectureLocked = selectedLectures.length > 0;
    const isLectureActive = L => selectedLectures.includes(L);

    const examChip = (n, label) => `<button class="stim-chip${settings.exam===n?' active':''}${lectureLocked?' disabled':''}" data-set="exam" data-val="${n}"${lectureLocked?' disabled':''}>${label}</button>`;
    const countChip = n => `<button class="stim-chip${settings.count===n?' active':''}" data-set="count" data-val="${n}">${n===0?'All':n}</button>`;
    const typeChip = (v, l) => `<button class="stim-chip${settings.type===v?' active':''}" data-set="type" data-val="${v}">${l}</button>`;
    const timerChip = (s, l) => `<button class="stim-chip${settings.timer===s?' active':''}" data-set="timer" data-val="${s}">${l}</button>`;
    const lectureChip = (L, count) => `<button class="stim-chip${isLectureActive(L)?' active':''}" data-toggle-lec="${L}" title="${count} questions">${L}</button>`;

    const idx = window.STIM_INDEX || { byExam: {}, byLecture: {} };
    const examCounts = idx.byExam || {};
    const totalQs = Array.isArray(window.STIM_BANK) ? window.STIM_BANK.length : 0;

    // Build lecture -> exam map and counts from the bank
    const lectureMap = {}; // 'L02' -> { exam, count }
    (window.STIM_BANK || []).forEach(q => {
      if (!q.lecture) return;
      if (!lectureMap[q.lecture]) lectureMap[q.lecture] = { exam: q.exam, count: 0 };
      lectureMap[q.lecture].count++;
    });
    const lecturesByExam = { 1: [], 2: [], 3: [] };
    Object.keys(lectureMap).sort().forEach(L => {
      const ex = lectureMap[L].exam;
      if (lecturesByExam[ex]) lecturesByExam[ex].push(L);
    });
    const lecGroup = (exNum) => {
      const groupLectures = lecturesByExam[exNum] || [];
      if (!groupLectures.length) return '';
      const allInGroup = groupLectures.every(L => isLectureActive(L));
      const anyInGroup = groupLectures.some(L => isLectureActive(L));
      const btnLabel = allInGroup ? 'Clear' : 'All';
      const btnTitle = allInGroup ? `Deselect all in Exam ${exNum}` : `Select all in Exam ${exNum}`;
      const btnCls = anyInGroup && !allInGroup ? ' active' : '';
      return `
      <div class="stim-lec-group">
        <div class="stim-lec-group-label">
          <span>Exam ${exNum}</span>
          <button class="stim-lec-group-toggle${btnCls}" data-toggle-exam="${exNum}" title="${btnTitle}">${btnLabel}</button>
        </div>
        <div class="stim-lec-group-chips">${groupLectures.map(L => lectureChip(L, lectureMap[L].count)).join('')}</div>
      </div>`;
    };

    let lectureNote = '';
    if (lectureLocked) {
      const totalSelected = selectedLectures.reduce((sum, L) => sum + ((lectureMap[L] && lectureMap[L].count) || 0), 0);
      const sortedSel = selectedLectures.slice().sort();
      const lecLabel = sortedSel.length === 1
        ? `Lecture <strong>${esc(sortedSel[0])}</strong>`
        : `<strong>${sortedSel.length} lectures</strong> (${esc(sortedSel.join(', '))})`;
      lectureNote = `<div class="stim-lec-note">${lecLabel} selected — ${totalSelected} question${totalSelected===1?'':'s'} available. Exam filter is ignored while specific lectures are chosen.</div>`;
    }

    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-eyebrow">Stim Mode · Practice Exam</div>
        <h1 class="stim-title">Take a real practice exam.</h1>
        <p class="stim-subtitle">${totalQs} questions across all three exams. Mix MC + short answer. Short-answer questions get a <strong>Grade with Claude</strong> button so you can verify your answer against an expert grader.</p>

        <div class="stim-card">
          <div class="stim-row">
            <label>Exam</label>
            ${examChip(1, 'Exam 1 ('+(examCounts[1]||0)+')')}
            ${examChip(2, 'Exam 2 ('+(examCounts[2]||0)+')')}
            ${examChip(3, 'Exam 3 ('+(examCounts[3]||0)+')')}
            ${examChip(0, 'Cumulative ('+totalQs+')')}
          </div>
          <div class="stim-row">
            <label>Lecture</label>
            <button class="stim-chip${!lectureLocked?' active':''}" data-toggle-lec="all">All lectures</button>
            ${lectureLocked ? `<button class="stim-chip stim-chip-clear" id="stimClearLectures" title="Clear all lecture selections">Clear (${selectedLectures.length})</button>` : ''}
          </div>
          <div class="stim-lec-grid">
            ${lecGroup(1)}
            ${lecGroup(2)}
            ${lecGroup(3)}
          </div>
          ${lectureNote}
          <div class="stim-row">
            <label>Question count</label>
            ${countChip(10)}
            ${countChip(25)}
            ${countChip(50)}
            ${countChip(100)}
            ${countChip(0)}
          </div>
          <div class="stim-row">
            <label>Type mix</label>
            ${typeChip('mixed', 'Mixed')}
            ${typeChip('mc', 'MC only')}
            ${typeChip('sa', 'SA only')}
          </div>
          <div class="stim-row">
            <label>Mode</label>
            <button class="stim-chip${!settings.adaptive?' active':''}" data-set-bool="adaptive" data-val="0" title="Standard exam — answer each question once, get scored at the end.">📝 Standard</button>
            <button class="stim-chip${settings.adaptive?' active':''}" data-set-bool="adaptive" data-val="1" title="Adaptive — questions you miss come back. Session ends when you've answered EVERY question correctly.">🧠 Adaptive (until 100%)</button>
          </div>
          <div class="stim-row">
            <label>Timer</label>
            ${timerChip(0, 'Off')}
            ${timerChip(1800, '30 min')}
            ${timerChip(3600, '60 min')}
            ${timerChip(5400, '90 min')}
          </div>
          <div class="stim-row">
            <button class="stim-btn" id="stimStart">Start exam</button>
            <button class="stim-btn stim-btn-ghost" id="stimDashOpen">Dashboard</button>
          </div>
        </div>

        <div class="stim-card" id="stimDashboard" style="display:${stats.totalSessions>0?'block':'none'}">
          <h3 style="margin-top:0;font-family:var(--ff-display,serif);">Your progress</h3>
          ${renderDashboardHTML(stats)}
        </div>
      </div>`;

    // wire chips (exam, count, type, timer)
    root().querySelectorAll('.stim-chip[data-set]').forEach(b => {
      b.addEventListener('click', () => {
        const k = b.dataset.set, v = b.dataset.val;
        if (b.disabled) return;
        settings[k] = (k === 'type') ? v : Number(v);
        saveJSON(LS_SETTINGS, settings);
        renderSetup();
      });
    });
    // wire boolean chips (adaptive mode)
    root().querySelectorAll('.stim-chip[data-set-bool]').forEach(b => {
      b.addEventListener('click', () => {
        const k = b.dataset.setBool;
        settings[k] = b.dataset.val === '1';
        saveJSON(LS_SETTINGS, settings);
        renderSetup();
      });
    });

    // wire lecture chips — multi-select toggle
    root().querySelectorAll('[data-toggle-lec]').forEach(b => {
      b.addEventListener('click', () => {
        const L = b.dataset.toggleLec;
        if (L === 'all') {
          settings.lecture = 'all';
        } else {
          let arr = Array.isArray(settings.lecture) ? settings.lecture.slice() : [];
          if (arr.includes(L)) arr = arr.filter(x => x !== L);
          else arr.push(L);
          settings.lecture = arr.length ? arr : 'all';
        }
        saveJSON(LS_SETTINGS, settings);
        renderSetup();
      });
    });

    // wire per-exam group All/Clear toggle
    root().querySelectorAll('[data-toggle-exam]').forEach(b => {
      b.addEventListener('click', () => {
        const exNum = Number(b.dataset.toggleExam);
        const groupLectures = lecturesByExam[exNum] || [];
        if (!groupLectures.length) return;
        let arr = Array.isArray(settings.lecture) ? settings.lecture.slice() : [];
        const allSelected = groupLectures.every(L => arr.includes(L));
        if (allSelected) {
          arr = arr.filter(L => !groupLectures.includes(L));
        } else {
          groupLectures.forEach(L => { if (!arr.includes(L)) arr.push(L); });
        }
        settings.lecture = arr.length ? arr : 'all';
        saveJSON(LS_SETTINGS, settings);
        renderSetup();
      });
    });

    // clear-all lecture selections
    const clearBtn = document.getElementById('stimClearLectures');
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        settings.lecture = 'all';
        saveJSON(LS_SETTINGS, settings);
        renderSetup();
      });
    }

    $('#stimStart').addEventListener('click', () => startSession(settings));
    $('#stimDashOpen').addEventListener('click', () => {
      const el = $('#stimDashboard');
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
    });
    wireDashboardCommon();
  }

  function startSession(settings) {
    const bank = window.STIM_BANK;
    let selected;
    let sessionId = 'sess_' + Date.now();

    // Variation preset: if settings carries an explicit qid list (mastery
    // page launched a specific practice-final variation), use exactly those
    // questions in that order. Bypasses pool filtering and shuffling so
    // Variation A always runs the same 30 questions.
    // Adaptive mode is meant to drill the full bank, so it ignores variation
    // presets (and we clear them so they don't sneak back in next time).
    if (settings.adaptive) {
      delete settings._variationQids;
      delete settings._variationLabel;
      saveJSON(LS_SETTINGS, settings);
    } else if (Array.isArray(settings._variationQids) && settings._variationQids.length > 0) {
      const byId = new Map(bank.map(q => [q.id, q]));
      selected = settings._variationQids.map(id => byId.get(id)).filter(Boolean);
      if (selected.length === 0) {
        alert('Variation question set could not be loaded — falling back to a random pool.');
      } else {
        if (settings._variationLabel) sessionId += '_' + settings._variationLabel;
      }
    }

    if (!selected || selected.length === 0) {
      const selectedLectures = Array.isArray(settings.lecture) ? settings.lecture : [];
      const lectureLocked = selectedLectures.length > 0;
      let pool;
      if (settings.adaptive) {
        // Adaptive mode = drill EVERY question in the bank (still respects
        // type filter so MC-only / SA-only stay meaningful). Exam/lecture
        // filters and the count cap are intentionally ignored.
        pool = bank.slice();
      } else if (lectureLocked) {
        pool = bank.filter(q => selectedLectures.includes(q.lecture));
      } else {
        pool = bank.filter(q => settings.exam === 0 || q.exam === settings.exam);
      }
      if (settings.type === 'mc') pool = pool.filter(q => q.type === 'mc');
      if (settings.type === 'sa') pool = pool.filter(q => q.type === 'sa');
      if (pool.length === 0) {
        alert('No questions match those filters.');
        return;
      }
      const shuffled = shuffleSeeded(pool, sessionId);
      const useAll = settings.adaptive || settings.count === 0;
      const target = useAll ? shuffled.length : Math.min(settings.count, shuffled.length);
      selected = shuffled.slice(0, target);
    }

    const selectedLectures = Array.isArray(settings.lecture) ? settings.lecture : [];
    const lectureLocked = selectedLectures.length > 0;

    session = {
      id: sessionId,
      exam: settings.exam,
      lectures: lectureLocked ? selectedLectures.slice() : null,
      lecture: lectureLocked && selectedLectures.length === 1 ? selectedLectures[0] : null,
      count: selected.length,
      type: settings.type,
      timer_sec: settings.timer,
      started_at: Date.now(),
      remaining_sec: settings.timer,
      qids: selected.map(q => q.id),
      current: 0,
      answers: {},   // qid -> { mc_idx | sa_text }
      flags: {},     // qid -> true
      finished: false,
      results: null,
      variationLabel: settings._variationLabel || null,
      // ----- Adaptive mode -----
      // When `adaptive` is true the session keeps cycling missed questions
      // back into the pool until every qid has been answered correctly.
      adaptive: !!settings.adaptive,
      adaptive_pool: !!settings.adaptive ? selected.map(q => q.id) : null, // qids still needing a correct answer
      adaptive_lapses: {},   // qid -> miss count this session
      adaptive_attempts: {}, // qid -> attempt count this session
      adaptive_mastered: {}, // qid -> true once correctly answered
    };
    saveJSON(LS_SESSION, session);
    renderExam();
  }

  // -------- adaptive helpers --------
  // Decide whether the just-answered question was correct.
  // MC: compare user index to q.correct.
  // SA: auto-pass if answer is non-trivial (≥30 chars) — true grading
  //     would need Claude grader integration; for now we trust the user.
  function adaptiveWasCorrect(q) {
    if (!q) return false;
    const ans = session.answers[q.id];
    if (!ans) return false;
    if (q.type === 'mc') return ans.mc_idx === q.correct;
    if (q.type === 'sa') return !!(ans.sa_text && ans.sa_text.trim().length >= 30);
    return false;
  }

  // Pick the next qid to show in adaptive mode. Always returns the FIRST
  // entry in adaptive_pool — the pool itself is reordered when a question
  // is missed (sent back N positions).
  function adaptivePickNextIndex() {
    const pool = session.adaptive_pool || [];
    if (pool.length === 0) return -1;
    const nextQid = pool[0];
    return session.qids.indexOf(nextQid);
  }

  // Re-insert a missed qid into the pool a few positions back so it cycles
  // back soon but not immediately. Position scales with the lapse count
  // so chronically-missed cards come back faster.
  function reinsertMissedQid(qid) {
    const pool = session.adaptive_pool;
    const lapses = session.adaptive_lapses[qid] || 0;
    // Smaller offset for chronic lapses → re-serve sooner.
    let offset = Math.max(2, 5 - lapses);
    if (offset > pool.length) offset = pool.length;
    pool.splice(offset, 0, qid);
  }

  function advanceAdaptive(q) {
    if (!q) return;
    const wasCorrect = adaptiveWasCorrect(q);
    session.adaptive_attempts[q.id] = (session.adaptive_attempts[q.id] || 0) + 1;

    // Remove the current qid from the front of the pool either way —
    // we'll re-insert it later if missed.
    const pool = session.adaptive_pool;
    const idx = pool.indexOf(q.id);
    if (idx >= 0) pool.splice(idx, 1);

    if (wasCorrect) {
      session.adaptive_mastered[q.id] = true;
    } else {
      session.adaptive_lapses[q.id] = (session.adaptive_lapses[q.id] || 0) + 1;
      reinsertMissedQid(q.id);
    }

    // Clear the user's stored answer so re-served questions appear fresh.
    if (!wasCorrect) delete session.answers[q.id];

    // All mastered → finish session in adaptive completion mode.
    if (pool.length === 0) {
      finishAdaptiveSession();
      return;
    }

    const nextIdx = adaptivePickNextIndex();
    session.current = nextIdx;
    saveJSON(LS_SESSION, session);
    renderExam();
  }

  function skipAdaptive(q) {
    if (!q) return;
    // Skip = move current to the back without grading.
    const pool = session.adaptive_pool;
    const idx = pool.indexOf(q.id);
    if (idx >= 0) {
      pool.splice(idx, 1);
      pool.push(q.id);
    }
    delete session.answers[q.id];
    if (pool.length === 0) return finishAdaptiveSession();
    session.current = adaptivePickNextIndex();
    saveJSON(LS_SESSION, session);
    renderExam();
  }

  function finishAdaptiveSession() {
    // Build a results array similar to finishSession, but flag every
    // question as mastered (since pool empty). Score = points each.
    const results = session.qids.map(id => {
      const q = findQ(id);
      const ans = session.answers[id] || {};
      return {
        qid: id,
        lecture: q.lecture,
        section: q.section,
        topic: q.topic,
        type: q.type,
        difficulty: q.difficulty,
        points: q.points,
        user_mc_idx: ans.mc_idx,
        user_sa_text: ans.sa_text || '',
        max: q.points,
        correct: true,
        score: q.points,
        adaptive_attempts: session.adaptive_attempts[id] || 1,
        adaptive_lapses: session.adaptive_lapses[id] || 0,
      };
    });
    session.finished = true;
    session.finished_at = Date.now();
    session.results = results;
    saveJSON(LS_SESSION, session);
    appendHistory(session);
    renderAdaptiveCompletion();
  }

  function renderAdaptiveCompletion() {
    const totalQs = session.qids.length;
    const totalAttempts = Object.values(session.adaptive_attempts).reduce((a, b) => a + b, 0);
    const totalLapses = Object.values(session.adaptive_lapses).reduce((a, b) => a + b, 0);
    const accuracy = totalAttempts > 0 ? Math.round(100 * (totalAttempts - totalLapses) / totalAttempts) : 100;
    const mins = Math.round((session.finished_at - session.started_at) / 60000);
    // Top-5 most-missed in this session
    const struggle = Object.entries(session.adaptive_lapses)
      .filter(([, n]) => n > 0)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([qid, n]) => {
        const q = findQ(qid);
        return `<li><strong>${n}× missed</strong> — <span style="color:var(--ink-faint,#b0a796)">${esc(q.lecture)}${q.section?' §'+esc(q.section):''}</span> · ${esc((q.q || '').slice(0, 100))}${(q.q||'').length>100?'…':''}</li>`;
      }).join('');
    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-eyebrow" style="color:#5fb87a">🏆 Adaptive run complete</div>
        <h1 class="stim-title">100% — every question answered correctly.</h1>
        <p class="stim-subtitle">You answered all <strong>${totalQs}</strong> question${totalQs===1?'':'s'} correctly in <strong>${mins} min</strong>. Total attempts: ${totalAttempts}. Net accuracy: ${accuracy}%.</p>
        ${struggle ? `<div class="stim-card"><h3 style="margin-top:0">Cards you struggled with (drill these next):</h3><ul style="line-height:1.8">${struggle}</ul></div>` : ''}
        <div class="stim-row" style="margin-top:18px">
          <button class="stim-btn" id="stimAdaptiveAgain">Run again</button>
          <button class="stim-btn stim-btn-ghost" id="stimAdaptiveBack">Back to setup</button>
        </div>
      </div>`;
    $('#stimAdaptiveBack').addEventListener('click', () => {
      session = null;
      localStorage.removeItem(LS_SESSION);
      renderSetup();
    });
    $('#stimAdaptiveAgain').addEventListener('click', () => {
      const settings = loadJSON(LS_SETTINGS, {});
      settings.adaptive = true;
      saveJSON(LS_SETTINGS, settings);
      startSession(settings);
    });
  }

  // -------- exam view --------
  function findQ(id) { return window.STIM_BANK.find(q => q.id === id); }

  // Build a human-readable source / reference citation from a question's metadata.
  // Maps lecture code (L04) → unit name + textbook chapter + study guide location.
  function buildSourceCitation(q) {
    const LEC_MAP = {
      // Exam 1 (Intro, evolutionary thinking, genetics, populations, quantitative)
      'L01': { unit: 'Unit · Intro',                              ch: 'Ch 1',  cs: 'Exam 1 study guide' },
      'L02': { unit: 'Unit · Evolutionary thinking',              ch: 'Ch 2',  cs: 'Exam 1 study guide' },
      'L03': { unit: 'Unit · Genes and heritable variation',      ch: 'Ch 5',  cs: 'Exam 1 study guide' },
      'L04': { unit: 'Unit · Genetic evolution in populations',   ch: 'Ch 6',  cs: 'Exam 1 study guide' },
      'L05': { unit: 'Unit · Quantitative genetics & selection',  ch: 'Ch 7',  cs: 'Exam 1 study guide' },
      // Exam 2 (Selection in nature, complex adaptations, coevolution, sex, life history, social)
      'L07': { unit: 'Unit · Empirical natural selection',        ch: 'Ch 8',  cs: 'Exam 2 study guide' },
      'L08': { unit: 'Unit · Complex adaptations',                ch: 'Ch 10', cs: 'Exam 2 study guide' },
      'L09': { unit: 'Unit · Coevolution',                        ch: 'Ch 15', cs: 'Exam 2 study guide' },
      'L11': { unit: 'Unit · Sex and sexual selection',           ch: 'Ch 11', cs: 'Exam 2 study guide' },
      'L12': { unit: 'Unit · Life history evolution',             ch: 'Ch 12', cs: 'Exam 2 study guide' },
      'L13': { unit: 'Unit · Evolution of social behavior',       ch: 'Ch 16', cs: 'Exam 2 study guide' },
      // Exam 3 / Final (History, phylogenetics, speciation, biogeography, conservation, humans, medicine)
      'L14': { unit: 'Unit · History of life',                    ch: 'Ch 3',  cs: 'Exam 3 / Final study guide' },
      'L15': { unit: 'Unit · Phylogenetics & tree of life',       ch: 'Ch 4',  cs: 'Exam 3 / Final study guide' },
      'L16': { unit: 'Unit · Species concepts & isolation',       ch: 'Ch 13', cs: 'Exam 3 / Final study guide' },
      'L17': { unit: 'Unit · Biogeography, speciation, extinction', ch: 'Ch 14', cs: 'Exam 3 / Final study guide' },
      'L18': { unit: 'Unit · Conservation & humans as selective force', ch: 'Ch 8', cs: 'Exam 3 / Final study guide' },
      'L19': { unit: 'Unit · Human evolution',                    ch: 'Ch 17', cs: 'Exam 3 / Final study guide' },
      'L20': { unit: 'Unit · Evolutionary medicine',              ch: 'Ch 18', cs: 'Exam 3 / Final study guide' },
    };
    const info = LEC_MAP[q.lecture] || { unit: '', ch: '', cs: '' };
    const parts = [];
    parts.push(`<strong>${esc(q.lecture)}</strong>`);
    if (q.section) parts.push(`§${esc(q.section)}`);
    if (info.unit) parts.push(esc(info.unit));
    if (info.ch && info.ch !== '—') parts.push(`Textbook ${esc(info.ch)}`);
    if (q.topic) parts.push(`Topic: ${esc(q.topic)}`);
    if (info.cs) parts.push(`📄 ${esc(info.cs)}`);
    if (q.source) parts.push(`<span style="color:var(--ink-faint,#888);font-size:11px">[${esc(q.source)}]</span>`);
    return parts.join(' · ');
  }

  // Practice-mode: after MC click, lock choices, color them, show per-choice why + overall explanation
  function revealMCFeedback(q, userIdx) {
    const isCorrect = userIdx === q.correct;
    const choices = root().querySelectorAll('.stim-choice');
    choices.forEach((btn, i) => {
      btn.disabled = true;
      btn.classList.remove('selected');
      btn.style.cursor = 'default';
      // Color: green for correct, red for the user's wrong pick, gray for the rest
      if (i === q.correct) btn.classList.add('correct-rev');
      else if (i === userIdx && !isCorrect) btn.classList.add('wrong-rev');
      // Inject per-choice rationale if available — won't duplicate if already present
      if (q.choice_why && q.choice_why[i] && !btn.querySelector('.stim-choice-why')) {
        const why = document.createElement('div');
        why.className = 'stim-choice-why';
        why.textContent = q.choice_why[i];
        btn.appendChild(why);
      }
    });
    // Overall feedback panel
    const choicesWrap = root().querySelector('.stim-choices');
    if (choicesWrap && !root().querySelector('.stim-feedback')) {
      const fb = document.createElement('div');
      fb.className = 'stim-feedback ' + (isCorrect ? 'correct' : 'incorrect');
      const correctLetter = String.fromCharCode(65 + q.correct);
      const sourceCite = buildSourceCitation(q);
      fb.innerHTML = `
        <div class="fb-verdict">${isCorrect ? '✓ Correct!' : '✗ Incorrect'}</div>
        <div class="fb-correct"><strong>Correct answer: ${correctLetter}.</strong> ${esc(q.choices[q.correct])}</div>
        ${q.why ? `<div class="fb-why"><strong>Why:</strong> ${esc(q.why)}</div>` : ''}
        ${!isCorrect && q.choice_why && q.choice_why[userIdx] ? `<div class="fb-user-why"><strong>Why your pick was wrong:</strong> ${esc(q.choice_why[userIdx])}</div>` : ''}
        <div class="fb-source">📚 <strong>From:</strong> ${sourceCite}</div>
        <div class="fb-hint">Click <strong>Next →</strong> below to continue. Use <strong>Prev ←</strong> to revisit.</div>
      `;
      choicesWrap.after(fb);
    }
  }

  function renderExam() {
    if (timerHandle) clearInterval(timerHandle);
    const q = findQ(session.qids[session.current]);
    if (!q) {
      submitConfirm();
      return;
    }
    const total = session.qids.length;
    const ans = session.answers[q.id];
    const flagged = session.flags[q.id];
    const paused = !!session.paused;

    const mcChoices = q.type === 'mc' ? q.choices.map((c, i) => `
      <button class="stim-choice${ans && ans.mc_idx === i ? ' selected' : ''}" data-mc="${i}">
        <span class="stim-choice-key">${String.fromCharCode(65 + i)}.</span>
        <span>${esc(c)}</span>
      </button>`).join('') : '';

    const saArea = q.type === 'sa' ? `
      <textarea class="stim-textarea" id="stimSaInput" placeholder="Type your answer here…" data-qid="${q.id}">${esc(ans && ans.sa_text || '')}</textarea>
      <div class="stim-char-count" id="stimCharCount">0 chars</div>
    ` : '';

    const pager = session.qids.map((id, i) => {
      const a = session.answers[id];
      const isAnswered = a && (a.mc_idx != null || (a.sa_text && a.sa_text.trim()));
      const cls = (isAnswered ? 'answered ' : '') + (i === session.current ? 'current ' : '') + (session.flags[id] ? 'flagged ' : '');
      return `<button class="${cls.trim()}" data-jump="${i}" title="Q${i+1}${session.flags[id]?' (flagged)':''}">${i + 1}</button>`;
    }).join('');

    const pausedBody = `
      <div class="stim-paused-shell">
        <div class="stim-paused-card">
          <div class="stim-paused-eyebrow">Exam paused</div>
          <h2 class="stim-paused-title">Take a breath.</h2>
          <p class="stim-paused-msg">Timer is frozen and the question is hidden so you can step away. Click <strong>Resume</strong> to continue.</p>
          <button class="stim-btn" id="stimResume">▶ Resume exam</button>
        </div>
      </div>`;

    // Adaptive mode hides the pager (questions cycle, pager would lie about position)
    // and rewords nav buttons.
    const showPager = !session.adaptive;
    const nextLabel = session.adaptive
      ? 'Submit & Next →'
      : (session.current === total - 1 ? 'Review →' : 'Next →');
    const skipLabel = session.adaptive ? 'Skip (back of pool)' : 'Skip';
    const showPrev = !session.adaptive;

    const examBody = `
      ${showPager ? `<div class="stim-pager">${pager}</div>` : ''}
      <div class="stim-shell">
        <div class="stim-q-meta">
          <span>${esc(q.lecture)}${q.section?' · §'+esc(q.section):''}</span>
          <span>${esc(q.topic||'')}</span>
          <span>${esc(q.difficulty||'')}</span>
        </div>
        <div class="stim-q-stem">${esc(q.q)}</div>
        ${q.type === 'mc' ? '<div class="stim-choices">' + mcChoices + '</div>' : saArea}
        <div class="stim-nav">
          ${showPrev ? `<button class="stim-btn stim-btn-ghost" id="stimPrev" ${session.current===0?'disabled':''}>← Prev</button>` : '<span></span>'}
          <div style="display:flex;gap:8px">
            <button class="stim-btn stim-btn-ghost" id="stimSkip">${skipLabel}</button>
            <button class="stim-btn" id="stimNext">${nextLabel}</button>
          </div>
        </div>
      </div>`;

    // Adaptive header — replaces "Q X / N" with mastered count + pool size.
    let progressLabel;
    if (session.adaptive) {
      const mastered = Object.keys(session.adaptive_mastered || {}).length;
      const poolLeft = (session.adaptive_pool || []).length;
      const attempts = session.adaptive_attempts[q.id] || 0;
      const lapses = session.adaptive_lapses[q.id] || 0;
      const repeatBadge = attempts > 0
        ? ` <span style="background:#b45309;color:white;padding:1px 6px;border-radius:8px;font-size:11px;font-weight:700">REPEAT × ${attempts}${lapses > 0 ? ' · ' + lapses + ' miss' : ''}</span>`
        : '';
      progressLabel =
        `<strong>🧠 Adaptive — ${mastered} mastered</strong>` +
        `<span style="color:var(--ink-faint,#b0a796)">${poolLeft} card${poolLeft===1?'':'s'} left · ${q.lecture} · ${q.type.toUpperCase()}</span>` +
        repeatBadge;
    } else {
      progressLabel =
        `<strong>Q ${session.current + 1} / ${total}</strong>` +
        `<span style="color:var(--ink-faint,#b0a796)">${q.lecture} · ${q.type.toUpperCase()} · ${q.points} pt${q.points>1?'s':''}</span>`;
    }

    root().innerHTML = `
      <div class="stim-exam-bar">
        <div class="stim-progress">
          ${progressLabel}
        </div>
        <div style="display:flex;gap:12px;align-items:center">
          ${session.timer_sec > 0 ? `<span class="stim-timer${paused?' paused':''}" id="stimTimer">--:--</span>` : ''}
          <button class="stim-btn stim-btn-ghost" id="stimPause" title="${paused?'Resume the exam':'Pause the exam — timer freezes, question hides'}">${paused?'▶ Resume':'⏸ Pause'}</button>
          <button class="stim-btn stim-btn-ghost" id="stimFlag"${paused?' disabled':''}>${flagged?'★ Flagged':'☆ Flag'}</button>
          <button class="stim-btn stim-btn-danger" id="stimSubmit">Submit Exam</button>
        </div>
      </div>
      ${paused ? pausedBody : examBody}`;

    // Pause toggle is always wired
    $('#stimPause').addEventListener('click', togglePause);
    const resumeBtn = $('#stimResume');
    if (resumeBtn) resumeBtn.addEventListener('click', togglePause);
    $('#stimSubmit').addEventListener('click', submitConfirm);

    if (!paused) {
      // If this MC has already been answered AND practice mode is on, render the feedback immediately
      // (so Prev → revisit shows the locked-in answer + explanation)
      const practiceMode = session.practice_mode !== false; // default ON
      const alreadyAnswered = q.type === 'mc' && ans && ans.mc_idx != null;
      if (practiceMode && alreadyAnswered) {
        revealMCFeedback(q, ans.mc_idx);
      }
      // wire MC clicks
      root().querySelectorAll('.stim-choice').forEach(b => {
        b.addEventListener('click', () => {
          // In practice mode, once answered the choices lock — don't allow re-clicks
          if (practiceMode && session.answers[q.id] && session.answers[q.id].mc_idx != null) return;
          const idx = Number(b.dataset.mc);
          session.answers[q.id] = { mc_idx: idx };
          saveJSON(LS_SESSION, session);
          if (practiceMode) {
            revealMCFeedback(q, idx);
          } else {
            root().querySelectorAll('.stim-choice').forEach(x => x.classList.remove('selected'));
            b.classList.add('selected');
          }
        });
      });
      // SA input persistence
      const sa = $('#stimSaInput');
      if (sa) {
        const cc = $('#stimCharCount');
        const update = () => {
          cc.textContent = sa.value.length + ' chars';
          session.answers[q.id] = { sa_text: sa.value };
          saveJSON(LS_SESSION, session);
        };
        sa.addEventListener('input', update);
        update();
      }
      // Pager
      root().querySelectorAll('.stim-pager button').forEach(b => {
        b.addEventListener('click', () => {
          session.current = Number(b.dataset.jump);
          saveJSON(LS_SESSION, session);
          renderExam();
        });
      });
      // Nav
      const prevBtn = $('#stimPrev');
      if (prevBtn) prevBtn.addEventListener('click', () => { session.current = Math.max(0, session.current - 1); saveJSON(LS_SESSION, session); renderExam(); });
      $('#stimNext').addEventListener('click', () => {
        if (session.adaptive) return advanceAdaptive(q);
        if (session.current === total - 1) submitConfirm();
        else { session.current++; saveJSON(LS_SESSION, session); renderExam(); }
      });
      $('#stimSkip').addEventListener('click', () => {
        if (session.adaptive) return skipAdaptive(q);
        if (session.current < total - 1) { session.current++; saveJSON(LS_SESSION, session); renderExam(); }
      });
      $('#stimFlag').addEventListener('click', () => {
        session.flags[q.id] = !session.flags[q.id];
        saveJSON(LS_SESSION, session);
        renderExam();
      });
    }

    // Timer — accounts for paused durations so wall-clock pause does not eat into exam time
    if (session.timer_sec > 0) {
      const tick = () => {
        const tEl = $('#stimTimer');
        if (!tEl) return;
        let pausedMs = session.paused_total_ms || 0;
        if (session.paused && session.paused_at) {
          pausedMs += Date.now() - session.paused_at;
        }
        const elapsed = Math.floor((Date.now() - session.started_at - pausedMs) / 1000);
        const remaining = session.timer_sec - elapsed;
        if (!session.paused && remaining <= 0) {
          clearInterval(timerHandle);
          tEl.textContent = '00:00';
          finishSession();
          return;
        }
        const r = Math.max(0, remaining);
        const mm = String(Math.floor(r / 60)).padStart(2, '0');
        const ss = String(r % 60).padStart(2, '0');
        tEl.textContent = `${mm}:${ss}`;
        tEl.classList.toggle('urgent', !session.paused && r < 300);
        tEl.classList.toggle('paused', !!session.paused);
      };
      tick();
      timerHandle = setInterval(tick, 1000);
    }
  }

  function togglePause() {
    if (!session) return;
    if (session.paused) {
      // Resuming — bank the pause duration into paused_total_ms
      if (session.paused_at) {
        session.paused_total_ms = (session.paused_total_ms || 0) + (Date.now() - session.paused_at);
      }
      session.paused = false;
      session.paused_at = null;
    } else {
      session.paused = true;
      session.paused_at = Date.now();
    }
    saveJSON(LS_SESSION, session);
    renderExam();
  }

  function submitConfirm() {
    const total = session.qids.length;
    const answered = session.qids.filter(id => {
      const a = session.answers[id];
      return a && (a.mc_idx != null || (a.sa_text && a.sa_text.trim()));
    }).length;
    const unanswered = total - answered;
    showModal(`
      <h3>Submit exam?</h3>
      <p>${answered} of ${total} answered${unanswered > 0 ? ` — ${unanswered} unanswered will be marked 0.` : '.'}</p>
      <p>Once submitted you'll see results, MC scoring, and Grade-with-Claude buttons for short answers.</p>
      <div class="stim-modal-actions">
        <button class="stim-btn stim-btn-ghost" data-modal="close">Keep going</button>
        <button class="stim-btn stim-btn-danger" id="stimConfirmSubmit">Submit</button>
      </div>
    `);
    $('#stimConfirmSubmit').addEventListener('click', () => { hideModal(); finishSession(); });
  }

  function finishSession() {
    if (timerHandle) clearInterval(timerHandle);
    timerHandle = null;
    // Commit any in-progress pause into paused_total_ms so elapsed time is accurate
    if (session.paused && session.paused_at) {
      session.paused_total_ms = (session.paused_total_ms || 0) + (Date.now() - session.paused_at);
      session.paused = false;
      session.paused_at = null;
    }
    const results = session.qids.map(id => {
      const q = findQ(id);
      const ans = session.answers[id] || {};
      const result = {
        qid: id,
        lecture: q.lecture,
        topic: q.topic,
        type: q.type,
        difficulty: q.difficulty,
        points: q.points,
        user_mc_idx: ans.mc_idx,
        user_sa_text: ans.sa_text || '',
        max: q.points,
      };
      if (q.type === 'mc') {
        result.correct = ans.mc_idx === q.correct;
        result.score = result.correct ? q.points : 0;
      } else {
        result.score = null; // ungraded until Claude grades it
        result.claude_grade = null;
      }
      return result;
    });
    session.finished = true;
    session.finished_at = Date.now();
    session.results = results;
    saveJSON(LS_SESSION, session);
    appendHistory(session);
    renderResults();
  }

  function appendHistory(sess) {
    const hist = loadJSON(LS_HISTORY, []);
    // store compact summary
    hist.push({
      id: sess.id,
      exam: sess.exam,
      type: sess.type,
      count: sess.qids.length,
      started_at: sess.started_at,
      finished_at: sess.finished_at,
      results: sess.results.map(r => ({ qid: r.qid, lecture: r.lecture, topic: r.topic, type: r.type, score: r.score, max: r.max }))
    });
    // cap to last 50
    if (hist.length > 50) hist.splice(0, hist.length - 50);
    saveJSON(LS_HISTORY, hist);
    rebuildStats();
  }

  function rebuildStats() {
    const hist = loadJSON(LS_HISTORY, []);
    // Per-topic-within-section stats. Key = lecture+'§'+section+'·'+topic.
    // Falls back gracefully when section/topic missing (older history rows).
    const stats = {};
    hist.forEach(s => {
      s.results.forEach(r => {
        if (r.score == null) return; // ungraded SA
        // Look up the question in the bank to enrich older history rows that lack section
        const qref = (window.STIM_BANK || []).find(q => q.id === r.qid);
        const section = r.section || (qref && qref.section) || '';
        const topic = r.topic || (qref && qref.topic) || '';
        const lecture = r.lecture || (qref && qref.lecture) || '';
        const key = lecture + '§' + section + '·' + topic;
        if (!stats[key]) stats[key] = {
          lecture, section, topic,
          seen: 0, total_pts: 0, scored_pts: 0, last_seen: 0
        };
        stats[key].seen++;
        stats[key].total_pts += r.max;
        stats[key].scored_pts += r.score;
        stats[key].last_seen = Math.max(stats[key].last_seen, s.finished_at || s.started_at);
      });
    });
    saveJSON(LS_STATS, stats);
  }

  function computeStats() {
    const hist = loadJSON(LS_HISTORY, []);
    const stats = loadJSON(LS_STATS, {});
    let totalPts = 0, scoredPts = 0, sessionCount = hist.length;
    hist.forEach(s => s.results.forEach(r => {
      if (r.score == null) return;
      totalPts += r.max; scoredPts += r.score;
    }));
    const accuracy = totalPts > 0 ? Math.round(100 * scoredPts / totalPts) : null;
    // by lecture (high-level rollup)
    const byLec = {};
    // by lecture+section (mid-level rollup, e.g. "L02 § A")
    const bySection = {};
    Object.values(stats).forEach(t => {
      if (!byLec[t.lecture]) byLec[t.lecture] = { total_pts: 0, scored_pts: 0, seen: 0, sections: {} };
      byLec[t.lecture].total_pts += t.total_pts;
      byLec[t.lecture].scored_pts += t.scored_pts;
      byLec[t.lecture].seen += t.seen;
      // nested section
      const secKey = t.section || '—';
      if (!byLec[t.lecture].sections[secKey]) byLec[t.lecture].sections[secKey] = { total_pts:0, scored_pts:0, seen:0, topics: [] };
      const secObj = byLec[t.lecture].sections[secKey];
      secObj.total_pts += t.total_pts;
      secObj.scored_pts += t.scored_pts;
      secObj.seen += t.seen;
      secObj.topics.push(t);
      // flat by-section roll for the precise heatmap row
      const flatKey = t.lecture + '§' + (t.section || '—');
      if (!bySection[flatKey]) bySection[flatKey] = { lecture: t.lecture, section: t.section || '—', total_pts: 0, scored_pts: 0, seen: 0, topics: [] };
      bySection[flatKey].total_pts += t.total_pts;
      bySection[flatKey].scored_pts += t.scored_pts;
      bySection[flatKey].seen += t.seen;
      bySection[flatKey].topics.push(t);
    });
    // weak topics (min 2 seen, sorted by score_pct ascending) — uses fine-grain topics
    const weak = Object.values(stats)
      .filter(t => t.seen >= 2 && t.total_pts > 0)
      .map(t => ({ ...t, pct: t.scored_pts / t.total_pts }))
      .sort((a, b) => a.pct - b.pct)
      .slice(0, 10);
    return { totalSessions: sessionCount, accuracy, byLec, bySection, weak, allTopics: stats };
  }

  function renderDashboardHTML(stats) {
    // Color helper
    const heatColor = pct => pct == null ? '#444'
      : pct < 0.4 ? '#c74e4e'
      : pct < 0.6 ? '#d69b4e'
      : pct < 0.8 ? '#d6c84e'
      : '#5fb87a';

    // ----- Tier 1: per-lecture row (rollup) -----
    const lecKeys = Object.keys(stats.byLec).sort();
    const heatLec = lecKeys.map(k => {
      const v = stats.byLec[k];
      const pct = v.total_pts > 0 ? v.scored_pts / v.total_pts : null;
      return `<div class="stim-heat-cell" style="background:${heatColor(pct)};color:#1a1a1a" title="${k} — ${pct==null?'no data':Math.round(pct*100)+'%'} (${v.seen} attempts)" data-lec-cell="${esc(k)}">${k}</div>`;
    }).join('');

    // ----- Tier 2: per-section subpoint grid (lecture § A/B/C…) -----
    // Lookup section title from MANUAL_LECTURE_GUIDES if available
    const guideLookup = (window.MANUAL_LECTURE_GUIDES && typeof window.MANUAL_LECTURE_GUIDES === 'object') ? window.MANUAL_LECTURE_GUIDES : {};
    const sectionTitle = (lec, letter) => {
      const g = guideLookup[lec];
      if (!g || !Array.isArray(g.sections)) return '';
      const s = g.sections.find(x => x.letter === letter);
      return s ? s.title : '';
    };

    let subpointHTML = '';
    if (Object.keys(stats.byLec).length) {
      const blocks = lecKeys.map(lec => {
        const lecObj = stats.byLec[lec];
        const sectionKeys = Object.keys(lecObj.sections).sort();
        const cells = sectionKeys.map(letter => {
          const s = lecObj.sections[letter];
          const pct = s.total_pts > 0 ? s.scored_pts / s.total_pts : null;
          const title = sectionTitle(lec, letter);
          const tip = `${lec} § ${letter}${title ? ' — '+title : ''} · ${pct==null?'no data':Math.round(pct*100)+'% ('+s.scored_pts+'/'+s.total_pts+' pts in '+s.seen+' attempts)'}`;
          return `<div class="stim-heat-sub" style="background:${heatColor(pct)};color:#1a1a1a" title="${esc(tip)}">
            <span class="stim-heat-sub-letter">${esc(letter)}</span>
            ${title ? `<span class="stim-heat-sub-title">${esc(title)}</span>` : ''}
          </div>`;
        }).join('');
        return `<div class="stim-heat-lec-block">
          <div class="stim-heat-lec-label">${esc(lec)} <span style="opacity:.55">·</span> <span style="opacity:.65">${lecObj.seen} att / ${Math.round((lecObj.scored_pts/Math.max(1,lecObj.total_pts))*100)}%</span></div>
          <div class="stim-heat-sub-row">${cells}</div>
        </div>`;
      }).join('');
      subpointHTML = blocks;
    }

    // ----- Tier 3: per-topic precision list (mechanism / term level) -----
    const topicPrecision = Object.values(stats.allTopics || {})
      .filter(t => t.total_pts > 0 && t.topic)
      .sort((a, b) => {
        // sort by pct asc, then by lecture asc, then by section
        const pa = a.scored_pts / a.total_pts, pb = b.scored_pts / b.total_pts;
        if (pa !== pb) return pa - pb;
        if (a.lecture !== b.lecture) return a.lecture < b.lecture ? -1 : 1;
        return (a.section || '') < (b.section || '') ? -1 : 1;
      });
    const topicListHTML = topicPrecision.length
      ? `<div class="stim-heat-topics-table">${topicPrecision.map(t => {
          const pct = t.scored_pts / t.total_pts;
          return `<div class="stim-heat-topic-row" style="border-left-color:${heatColor(pct)}">
            <span class="stim-heat-topic-loc">${esc(t.lecture)}${t.section ? ' § '+esc(t.section) : ''}</span>
            <span class="stim-heat-topic-name">${esc(t.topic)}</span>
            <span class="stim-heat-topic-pct">${Math.round(pct * 100)}% <span style="opacity:.55">(${t.scored_pts}/${t.total_pts} · ${t.seen}×)</span></span>
          </div>`;
        }).join('')}</div>`
      : '<em style="color:var(--ink-faint,#b0a796);font-size:13px;">No topic data yet.</em>';

    const weakList = stats.weak.length ? stats.weak.map(t =>
      `<li><strong>${esc(t.topic)}</strong> · ${esc(t.lecture)}${t.section ? ' § '+esc(t.section) : ''} · ${Math.round(t.pct * 100)}% (${t.scored_pts}/${t.total_pts} pts in ${t.seen} attempts)</li>`
    ).join('') : '<li style="color:var(--ink-faint,#b0a796)">No weak topics yet — take a few exams.</li>';

    return `
      <div class="stim-result-summary">
        <div class="stim-stat">
          <div class="stim-stat-num">${stats.accuracy != null ? stats.accuracy + '%' : '—'}</div>
          <div class="stim-stat-lbl">Lifetime accuracy</div>
        </div>
        <div class="stim-stat">
          <div class="stim-stat-num">${stats.totalSessions}</div>
          <div class="stim-stat-lbl">Sessions taken</div>
        </div>
      </div>

      <div class="stim-heat-section">
        <div class="stim-heat-section-head">
          <span>Per-lecture heatmap</span>
          <span class="stim-heat-legend">red = weak · green = strong</span>
        </div>
        <div class="stim-heatmap">${heatLec || '<em style="color:var(--ink-faint,#b0a796)">No data yet.</em>'}</div>
      </div>

      <div class="stim-heat-section">
        <div class="stim-heat-section-head">
          <span>Per-subpoint precision (lecture § section letter)</span>
          <span class="stim-heat-legend">hover for full title and stats</span>
        </div>
        ${subpointHTML || '<em style="color:var(--ink-faint,#b0a796);font-size:13px;">No section data yet — take an exam.</em>'}
      </div>

      <div class="stim-heat-section">
        <div class="stim-heat-section-head">
          <span>Per-topic precision (mechanism / term)</span>
          <button class="stim-btn stim-btn-ghost stim-heat-collapse-btn" type="button" data-action="toggle-topic-list" style="font-size:11px;padding:4px 10px">Hide</button>
        </div>
        <div id="stimHeatTopicList">${topicListHTML}</div>
      </div>

      <div style="margin:18px 0 6px;font-size:13px;color:var(--ink-faint,#b0a796);">Topics to work on</div>
      <ul style="margin:0;padding-left:20px;font-size:13px;line-height:1.7;">${weakList}</ul>
      <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:20px;padding-top:16px;border-top:1px solid var(--rule,rgba(255,255,255,0.08));">
        <button class="stim-btn stim-btn-ghost" data-action="reset-progress">Reset progress</button>
      </div>
    `;
  }

  function resetProgress() {
    showModal(`
      <h3>Reset all progress?</h3>
      <p>This permanently deletes your session history, accuracy stats, topic heatmap, and any in-progress exam. Your settings (preferred exam, count, timer) are kept.</p>
      <p style="color:var(--ink-faint,#b0a796);font-size:13px;">This cannot be undone.</p>
      <div class="stim-modal-actions">
        <button class="stim-btn stim-btn-ghost" data-modal="close">Cancel</button>
        <button class="stim-btn stim-btn-danger" id="stimResetConfirm">Yes, reset</button>
      </div>
    `);
    document.getElementById('stimResetConfirm').addEventListener('click', () => {
      localStorage.removeItem(LS_SESSION);
      localStorage.removeItem(LS_HISTORY);
      localStorage.removeItem(LS_STATS);
      session = null;
      hideModal();
      renderSetup();
    });
  }

  function wireDashboardCommon() {
    document.querySelectorAll('[data-action="reset-progress"]').forEach(b => {
      b.addEventListener('click', resetProgress);
    });
    document.querySelectorAll('[data-action="toggle-topic-list"]').forEach(b => {
      b.addEventListener('click', () => {
        const el = document.getElementById('stimHeatTopicList');
        if (!el) return;
        const hidden = el.style.display === 'none';
        el.style.display = hidden ? '' : 'none';
        b.textContent = hidden ? 'Hide' : 'Show';
      });
    });
  }

  // -------- results view --------
  function renderResults() {
    if (!session || !session.results) {
      renderSetup();
      return;
    }
    const r = session.results;
    const mcResults = r.filter(x => x.type === 'mc');
    const saResults = r.filter(x => x.type === 'sa');
    const mcCorrect = mcResults.filter(x => x.correct).length;
    const mcTotal = mcResults.length;
    const saGraded = saResults.filter(x => x.score != null);
    const saUngraded = saResults.length - saGraded.length;
    const saUngradedWithText = saResults.filter(x => x.score == null && x.user_sa_text && x.user_sa_text.trim()).length;
    const mcPts = mcResults.reduce((a, x) => a + (x.score || 0), 0);
    const mcMax = mcResults.reduce((a, x) => a + x.max, 0);
    const saPts = saGraded.reduce((a, x) => a + (x.score || 0), 0);
    const saMax = saGraded.reduce((a, x) => a + x.max, 0);
    const overallPts = mcPts + saPts;
    const overallMax = mcMax + saMax;
    const overallPct = overallMax > 0 ? Math.round(100 * overallPts / overallMax) : 0;
    const elapsedMs = Math.max(0, (session.finished_at - session.started_at) - (session.paused_total_ms || 0));
    const elapsed = Math.round(elapsedMs / 1000);
    const mm = Math.floor(elapsed / 60), ss = elapsed % 60;

    const stats = computeStats();

    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-eyebrow">Stim Mode · Results</div>
        <h1 class="stim-title">${overallPct}% — ${
          session.lectures && session.lectures.length > 1
            ? esc(session.lectures.length + ' lectures')
            : (session.lecture ? esc(session.lecture) : (session.exam===0?'Cumulative':'Exam '+session.exam))
        } practice</h1>
        <p class="stim-subtitle">${overallPts}/${overallMax} pts · ${mcCorrect}/${mcTotal} MC · ${saGraded.length}/${saResults.length} SA graded · ${mm}m ${ss}s elapsed</p>

        <div class="stim-result-summary">
          <div class="stim-stat"><div class="stim-stat-num">${overallPct}%</div><div class="stim-stat-lbl">Overall</div></div>
          <div class="stim-stat"><div class="stim-stat-num">${mcCorrect}/${mcTotal}</div><div class="stim-stat-lbl">MC correct</div></div>
          <div class="stim-stat"><div class="stim-stat-num">${saUngraded}</div><div class="stim-stat-lbl">SA awaiting grade</div></div>
        </div>

        <div class="stim-row" style="margin:16px 0 22px;flex-wrap:wrap">
          <button class="stim-btn stim-btn-ghost" id="stimBackToStudy" title="Return to the main study guide">← Study guide</button>
          <button class="stim-btn" id="stimNew">New exam</button>
          <button class="stim-btn stim-btn-ghost" id="stimReview">Review questions</button>
          <button class="stim-btn stim-btn-ghost" id="stimDashToggle">Toggle dashboard</button>
          ${saUngradedWithText > 0 ? `<button class="stim-btn" id="stimGradeAllSA" title="Send all unrated short-answer responses to Claude in one prompt">Grade all SA (${saUngradedWithText}) ↗</button>` : ''}
        </div>

        <div class="stim-card" id="stimDashboard">
          <h3 style="margin-top:0;font-family:var(--ff-display,serif);">Your progress</h3>
          ${renderDashboardHTML(stats)}
        </div>

        <div id="stimReviewSection" style="display:none">
          <h2 style="font-family:var(--ff-display,serif);font-size:24px;margin:32px 0 16px;">Question-by-question review</h2>
          ${r.map((res, i) => renderResultCardHTML(res, i)).join('')}
        </div>
      </div>`;

    $('#stimNew').addEventListener('click', () => {
      session = null;
      localStorage.removeItem(LS_SESSION);
      renderSetup();
    });
    $('#stimReview').addEventListener('click', () => {
      const el = $('#stimReviewSection');
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
      if (el.style.display === 'block') {
        wireResultCardHandlers();
        el.scrollIntoView({ behavior: 'smooth' });
      }
    });
    $('#stimDashToggle').addEventListener('click', () => {
      const el = $('#stimDashboard');
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
    });
    const back = document.getElementById('stimBackToStudy');
    if (back) back.addEventListener('click', () => {
      try { if (typeof window.setMode === 'function') window.setMode('study'); }
      catch (e) { window.location.hash = ''; }
      try { window.scrollTo({ top: 0, behavior: 'smooth' }); } catch(_){ window.scrollTo(0,0); }
    });
    const gradeAll = document.getElementById('stimGradeAllSA');
    if (gradeAll) gradeAll.addEventListener('click', gradeAllUngradedSA);
    wireDashboardCommon();
  }

  function renderResultCardHTML(res, i) {
    const q = findQ(res.qid);
    if (!q) return '';
    let cls = res.correct ? 'correct' : (res.score != null ? 'wrong' : 'ungraded');
    if (q.type === 'sa' && res.score == null) cls = 'ungraded';
    let body = '';
    if (q.type === 'mc') {
      const choices = q.choices.map((c, idx) => {
        let cc = '';
        if (idx === q.correct) cc = ' correct-rev';
        else if (idx === res.user_mc_idx && idx !== q.correct) cc = ' wrong-rev';
        const marker = idx === q.correct ? '✓' : (idx === res.user_mc_idx ? '✗' : ' ');
        return `<div class="stim-choice${cc}" style="cursor:default">
          <span class="stim-choice-key">${marker} ${String.fromCharCode(65+idx)}.</span>
          <span>${esc(c)}<br><span style="font-size:12px;color:var(--ink-faint,#b0a796)">${esc((q.choice_why||[])[idx]||'')}</span></span>
        </div>`;
      }).join('');
      body = `<div class="stim-choices" style="margin:12px 0">${choices}</div>
        <div class="stim-q-result-why">${esc(q.why || '')}</div>`;
    } else {
      const rubricList = (q.rubric && q.rubric.criteria || []).map(c =>
        `<li><strong>${c.pts} pt</strong>: ${esc(c.desc)}</li>`).join('');
      const userText = res.user_sa_text || '<em style="color:var(--ink-faint,#b0a796)">(no answer)</em>';
      const scoreLine = res.score != null
        ? `<div style="margin:8px 0;font-weight:600">Score: ${res.score} / ${q.points}</div>`
        : `<div style="margin:8px 0;font-weight:600;color:#f5b94c">Awaiting grade</div>`;
      const claudeFb = res.claude_grade && res.claude_grade.overall_feedback
        ? `<div style="margin:8px 0;font-size:13px"><em>Claude:</em> ${esc(res.claude_grade.overall_feedback)}</div>` : '';
      const claudeTopics = res.claude_grade && res.claude_grade.topics_to_work_on && res.claude_grade.topics_to_work_on.length
        ? `<div style="margin:8px 0;font-size:13px"><strong>Topics to study:</strong> ${res.claude_grade.topics_to_work_on.map(esc).join(', ')}</div>` : '';
      body = `
        ${scoreLine}
        <div style="margin:8px 0;padding:10px 12px;background:rgba(255,255,255,0.03);border-radius:6px;font-size:13px;line-height:1.5;">
          <strong>Your answer:</strong><br>${typeof userText==='string'?esc(userText):userText}
        </div>
        <div class="stim-q-result-rubric">
          <strong>Rubric (${q.rubric ? q.rubric.total : '?'} pts total):</strong>
          <ul>${rubricList}</ul>
        </div>
        <div class="stim-q-result-rubric">
          <strong>Model answer:</strong><br>${esc(q.model_answer || '')}
        </div>
        ${claudeFb}${claudeTopics}
        ${res.score == null ? `
          <div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
            <button class="stim-btn" data-grade="${res.qid}">Grade with Claude</button>
            <span style="font-size:12px;color:var(--ink-faint,#b0a796);align-self:center">Click → prompt copies, claude.ai opens. Paste reply below ↓</span>
          </div>
          <textarea class="stim-grade-paste" data-paste="${res.qid}" placeholder="Paste Claude's JSON reply here, then click Apply Grade…"></textarea>
          <button class="stim-btn stim-btn-ghost" data-apply="${res.qid}" style="margin-top:8px">Apply grade</button>
          <div class="stim-grade-msg" data-msg="${res.qid}" style="font-size:12px;margin-top:6px"></div>
        ` : ''}
      `;
    }
    return `<div class="stim-q-result ${cls}">
      <div style="display:flex;justify-content:space-between;font-size:11px;color:var(--ink-faint,#b0a796);margin-bottom:6px">
        <span>Q${i+1} · ${q.lecture} · ${q.type.toUpperCase()} · ${q.topic||''}</span>
        <span>${res.score != null ? res.score + '/' + q.points + ' pts' : 'pending'}</span>
      </div>
      <div class="stim-q-result-stem">${esc(q.q)}</div>
      ${body}
      <div class="stim-q-result-source">${esc(q.source || '')}</div>
    </div>`;
  }

  function wireResultCardHandlers() {
    document.querySelectorAll('button[data-grade]').forEach(b => {
      b.addEventListener('click', () => gradeWithClaude(b.dataset.grade));
    });
    document.querySelectorAll('button[data-apply]').forEach(b => {
      b.addEventListener('click', () => applyGrade(b.dataset.apply));
    });
  }

  function gradeWithClaude(qid) {
    const q = findQ(qid);
    const res = session.results.find(r => r.qid === qid);
    if (!q || !res) return;
    const rubricLines = (q.rubric && q.rubric.criteria || []).map(c => `- ${c.pts} pt: ${c.desc}`).join('\n');
    const prompt = `You are grading a BIOL 4230 (Evolution) short-answer exam response.

QUESTION (${qid}, ${q.points} pts):
${q.q}

STUDENT ANSWER:
${res.user_sa_text || '(no answer provided)'}

RUBRIC (total ${q.rubric ? q.rubric.total : q.points} pts):
${rubricLines}

MODEL ANSWER (reference; don't penalize alternative correct answers):
${q.model_answer || '(none provided)'}

Grade strictly per rubric. Be fair but accurate. Reply with ONLY this JSON, no other text before or after:

{
  "score": <integer 0 to ${q.rubric ? q.rubric.total : q.points}>,
  "per_criterion": [{"pts_awarded": 0|1, "feedback": "specific feedback for this criterion"}],
  "topics_to_work_on": ["specific topic 1", "specific topic 2"],
  "overall_feedback": "1-3 sentences"
}`;
    const copy = (text) => {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        return navigator.clipboard.writeText(text);
      }
      // fallback
      const ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand('copy');
      document.body.removeChild(ta);
      return Promise.resolve();
    };
    copy(prompt).then(() => {
      window.open('https://claude.ai/new', '_blank', 'noopener');
      const msgEl = document.querySelector(`[data-msg="${qid}"]`);
      if (msgEl) {
        msgEl.style.color = '#5fb87a';
        msgEl.textContent = '✓ Prompt copied. Paste it into Claude, then paste the reply below.';
      }
    }).catch(() => {
      alert('Could not copy to clipboard. The prompt is shown below — copy it manually.\n\n' + prompt.slice(0, 200) + '…');
    });
  }

  function applyGrade(qid) {
    const q = findQ(qid);
    const res = session.results.find(r => r.qid === qid);
    const ta = document.querySelector(`[data-paste="${qid}"]`);
    const msgEl = document.querySelector(`[data-msg="${qid}"]`);
    if (!ta || !res || !q) return;
    const raw = ta.value;
    const m = raw.match(/\{[\s\S]*\}/);
    if (!m) {
      msgEl.style.color = '#c74e4e';
      msgEl.textContent = '✗ Could not find a JSON block. Make sure Claude\'s reply contains the JSON object.';
      return;
    }
    let parsed;
    try { parsed = JSON.parse(m[0]); }
    catch (e) {
      msgEl.style.color = '#c74e4e';
      msgEl.textContent = '✗ JSON failed to parse: ' + e.message;
      return;
    }
    const max = q.rubric ? q.rubric.total : q.points;
    const score = Math.max(0, Math.min(max, Number(parsed.score) || 0));
    res.score = score;
    res.claude_grade = parsed;
    saveJSON(LS_SESSION, session);
    // also update history (the most recent entry should be this session)
    const hist = loadJSON(LS_HISTORY, []);
    if (hist.length) {
      const last = hist[hist.length - 1];
      if (last.id === session.id) {
        const histRes = last.results.find(r => r.qid === qid);
        if (histRes) histRes.score = score;
        saveJSON(LS_HISTORY, hist);
      }
    }
    rebuildStats();
    msgEl.style.color = '#5fb87a';
    msgEl.textContent = `✓ Graded: ${score}/${max} pts. Topics added to your dashboard.`;
    setTimeout(() => renderResults(), 800);
  }

  // -------- batch SA grading --------
  function gradeAllUngradedSA() {
    if (!session || !session.results) return;
    const ungraded = session.results.filter(r => r.type === 'sa' && r.score == null && r.user_sa_text && r.user_sa_text.trim());
    if (!ungraded.length) {
      alert('No ungraded short-answer responses with text to grade.');
      return;
    }
    const items = ungraded.map((res, i) => {
      const q = findQ(res.qid);
      if (!q) return '';
      const max = q.rubric ? q.rubric.total : q.points;
      const rubricLines = (q.rubric && q.rubric.criteria || []).map(c => `  - ${c.pts} pt: ${c.desc}`).join('\n');
      return `=== ITEM ${i+1} of ${ungraded.length} ===
QID: ${res.qid}
QUESTION (${q.points} pts):
${q.q}

STUDENT ANSWER:
${res.user_sa_text}

RUBRIC (total ${max} pts):
${rubricLines || '  (no explicit rubric — judge against the model answer)'}

MODEL ANSWER (reference; alternative correct answers are fine):
${q.model_answer || '(none)'}`;
    }).join('\n\n');

    const prompt = `You are grading ${ungraded.length} BIOL 4230 (Evolution) short-answer responses. Grade each one strictly per its rubric. Be fair but accurate; do not penalize alternative correct answers.

${items}

Reply with ONLY a JSON array, one object per item in the same order. No prose before or after.

[
  { "qid": "<exact qid from above>", "score": <integer 0..max>, "topics_to_work_on": ["specific term or mechanism"], "overall_feedback": "1-3 sentences" }
]`;

    const copy = (text) => {
      if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
      const ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand('copy');
      document.body.removeChild(ta);
      return Promise.resolve();
    };
    copy(prompt).then(() => {
      try { window.open('https://claude.ai/new', '_blank', 'noopener'); } catch(_){}
      showBatchPasteUI(ungraded.length);
    }).catch(() => {
      alert('Could not copy to clipboard. Use the per-question Grade with Claude buttons instead.');
    });
  }

  function showBatchPasteUI(count) {
    let host = document.getElementById('stimBatchPasteHost');
    if (!host) {
      host = document.createElement('div');
      host.id = 'stimBatchPasteHost';
      host.className = 'stim-card';
      host.style.marginTop = '16px';
      // Insert just after the action row
      const summaryEl = root().querySelector('.stim-result-summary');
      if (summaryEl && summaryEl.parentNode) {
        summaryEl.parentNode.insertBefore(host, summaryEl.nextSibling);
      } else {
        root().appendChild(host);
      }
    }
    host.innerHTML = `
      <h3 style="margin-top:0;font-family:var(--ff-display,serif);">Paste Claude's batch reply</h3>
      <p style="font-size:13px;color:var(--ink-faint,#b0a796);margin:0 0 8px;">Prompt copied + claude.ai opened. After Claude replies, paste the JSON array here and click <strong>Apply all grades</strong>.</p>
      <textarea class="stim-grade-paste" id="stimBatchPasteInput" placeholder='Paste the JSON array of ${count} grades here…'></textarea>
      <div style="display:flex;gap:8px;margin-top:8px;align-items:center;flex-wrap:wrap">
        <button class="stim-btn" id="stimApplyAllGrades">Apply all grades</button>
        <button class="stim-btn stim-btn-ghost" id="stimDismissBatchPaste">Cancel</button>
        <span id="stimBatchMsg" style="font-size:12px;color:var(--ink-faint,#b0a796)"></span>
      </div>
    `;
    document.getElementById('stimApplyAllGrades').addEventListener('click', applyAllStimGrades);
    document.getElementById('stimDismissBatchPaste').addEventListener('click', () => host.remove());
    host.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function applyAllStimGrades() {
    const ta = document.getElementById('stimBatchPasteInput');
    const msg = document.getElementById('stimBatchMsg');
    if (!ta || !msg) return;
    const m = ta.value.match(/\[[\s\S]*\]/);
    if (!m) { msg.style.color = '#c74e4e'; msg.textContent = '✗ No JSON array found.'; return; }
    let arr;
    try { arr = JSON.parse(m[0]); }
    catch (e) { msg.style.color = '#c74e4e'; msg.textContent = '✗ JSON parse failed: ' + e.message; return; }
    if (!Array.isArray(arr)) { msg.style.color = '#c74e4e'; msg.textContent = '✗ Reply was not a JSON array.'; return; }
    let applied = 0, skipped = 0;
    arr.forEach(item => {
      if (!item || !item.qid) { skipped++; return; }
      const res = session.results.find(r => r.qid === item.qid);
      const q = findQ(item.qid);
      if (!res || !q) { skipped++; return; }
      const max = q.rubric ? q.rubric.total : q.points;
      const score = Math.max(0, Math.min(max, Number(item.score) || 0));
      res.score = score;
      res.claude_grade = item;
      applied++;
    });
    if (applied) {
      saveJSON(LS_SESSION, session);
      const hist = loadJSON(LS_HISTORY, []);
      if (hist.length) {
        const last = hist[hist.length - 1];
        if (last.id === session.id) {
          arr.forEach(item => {
            if (!item || !item.qid) return;
            const histRes = last.results.find(r => r.qid === item.qid);
            const q = findQ(item.qid);
            if (histRes && q) {
              const max = q.rubric ? q.rubric.total : q.points;
              histRes.score = Math.max(0, Math.min(max, Number(item.score) || 0));
            }
          });
          saveJSON(LS_HISTORY, hist);
        }
      }
      rebuildStats();
    }
    msg.style.color = applied ? '#5fb87a' : '#c74e4e';
    msg.textContent = applied
      ? `✓ ${applied} graded${skipped ? ', '+skipped+' skipped (qid not matched)' : ''}. Refreshing…`
      : `✗ Nothing applied (${skipped} skipped — check that each qid matches one in this exam).`;
    if (applied) setTimeout(() => renderResults(), 900);
  }

  // -------- modal helpers --------
  function showModal(html) {
    const m = $('#stimModal');
    m.innerHTML = html;
    $('#stimModalBackdrop').classList.add('show');
    m.querySelectorAll('[data-modal="close"]').forEach(b => b.addEventListener('click', hideModal));
  }
  function hideModal() {
    $('#stimModalBackdrop').classList.remove('show');
  }

})();
