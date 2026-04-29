/* Stim Mode — practice exam simulator with Grade-with-Claude flow.
   Reads window.STIM_BANK / window.STIM_INDEX (loaded from stim-bank.js).
   Persists state to localStorage under stim_session, stim_history, stim_topic_stats. */
(function () {
  'use strict';

  const LS_SESSION = 'evol_stim_session';
  const LS_HISTORY = 'evol_stim_history';
  const LS_STATS   = 'evol_stim_topic_stats';
  const LS_SETTINGS = 'evol_stim_settings';
  const LS_DASH    = 'evol_stim_dash_prefs';
  const LS_REVIEW  = 'evol_stim_review_filter';

  // dashboard preference defaults
  const DASH_DEFAULTS = { granularity: 'lecture', showPct: true, onlyAttempted: false };

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

  // Some questions are tagged with multiple sections (e.g. "A,B" — the
  // question covers material from both section A and section B of the
  // lecture). For heat-map purposes we attribute the question to EACH
  // section it touches, so a weak answer surfaces in each related cell.
  function splitSections(s) {
    if (s == null || s === '') return ['?'];
    const out = String(s).split(/[,\s/]+/).map(x => x.trim()).filter(Boolean);
    return out.length ? out : ['?'];
  }

  // Build a static index of every (lecture, section, topic) cell that EXISTS
  // in the bank, regardless of whether the user has answered any questions
  // for it yet. Multi-section questions are expanded into one entry per
  // section. Used so the heatmap can show empty/un-attempted cells too.
  let _bankIdxCache = null;
  function buildBankIndex() {
    if (_bankIdxCache) return _bankIdxCache;
    const idx = { lectures: [], sections: {}, topics: {}, lecSections: {} };
    if (!Array.isArray(window.STIM_BANK)) return idx;
    const lecSet = new Set();
    window.STIM_BANK.forEach(q => {
      const lec = q.lecture || '?';
      const top = q.topic || '(general)';
      lecSet.add(lec);
      splitSections(q.section).forEach(sec => {
        const sk = `${lec}§${sec}`;
        if (!idx.sections[sk]) idx.sections[sk] = { lecture: lec, section: sec, q_count: 0, topics: new Set() };
        idx.sections[sk].q_count++;
        idx.sections[sk].topics.add(top);
        if (!idx.lecSections[lec]) idx.lecSections[lec] = new Set();
        idx.lecSections[lec].add(sec);
        const tk = `${sk}::${top}`;
        if (!idx.topics[tk]) idx.topics[tk] = { lecture: lec, section: sec, topic: top, q_count: 0 };
        idx.topics[tk].q_count++;
      });
    });
    idx.lectures = [...lecSet].sort();
    Object.values(idx.sections).forEach(s => s.topics = [...s.topics].sort());
    Object.keys(idx.lecSections).forEach(l => idx.lecSections[l] = [...idx.lecSections[l]].sort());
    _bankIdxCache = idx;
    return idx;
  }

  // Map qid -> { lecture, section (raw string from bank), topic }. For
  // multi-section attribution use splitSections(meta.section).
  function qMeta(qid) {
    const q = findQ(qid);
    if (!q) return { lecture: '?', section: '?', topic: '' };
    return { lecture: q.lecture, section: q.section || '?', topic: q.topic || '' };
  }

  // Color ramp shared by all heat renderers.
  function heatColor(pct) {
    if (pct == null) return '#444';
    return pct < 0.4 ? '#c74e4e' : pct < 0.6 ? '#d69b4e' : pct < 0.8 ? '#d6c84e' : '#5fb87a';
  }

  // -------- entry point --------
  window.StimMode = {
    activate: function () {
      if (!bankReady()) {
        renderEmpty();
        return;
      }
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
    if (settings.lecture == null) settings.lecture = 'all';
    const stats = computeStats();

    const examChip = (n, label) => `<button class="stim-chip${settings.exam===n?' active':''}" data-set="exam" data-val="${n}">${label}</button>`;
    const countChip = n => `<button class="stim-chip${settings.count===n?' active':''}" data-set="count" data-val="${n}">${n===0?'All':n}</button>`;
    const typeChip = (v, l) => `<button class="stim-chip${settings.type===v?' active':''}" data-set="type" data-val="${v}">${l}</button>`;
    const timerChip = (s, l) => `<button class="stim-chip${settings.timer===s?' active':''}" data-set="timer" data-val="${s}">${l}</button>`;
    const lecChip = (v, l) => `<button class="stim-chip${settings.lecture===v?' active':''}" data-set="lecture" data-val="${v}">${l}</button>`;

    const idx = window.STIM_INDEX || { byExam: {}, byLecture: {} };
    const examCounts = idx.byExam || {};
    const lectureCounts = idx.byLecture || {};
    const totalQs = Array.isArray(window.STIM_BANK) ? window.STIM_BANK.length : 0;

    // Lectures in scope for the currently-selected exam (Cumulative shows all).
    const examSet = settings.exam === 0 ? null : new Set(examCounts[settings.exam] || []);
    const lectureKeys = Object.keys(lectureCounts).filter(lec => {
      if (examSet === null) return true;
      return (lectureCounts[lec] || []).some(qid => examSet.has(qid));
    }).sort();

    // If user previously chose a lecture that isn't in the current exam, drop back to All.
    if (settings.lecture !== 'all' && !lectureKeys.includes(settings.lecture)) {
      settings.lecture = 'all';
      saveJSON(LS_SETTINGS, settings);
    }

    const lectureChipsHtml = [
      lecChip('all', 'All lectures'),
      ...lectureKeys.map(lec => {
        const ids = lectureCounts[lec] || [];
        const count = examSet === null ? ids.length : ids.filter(qid => examSet.has(qid)).length;
        return lecChip(lec, `${lec} (${count})`);
      })
    ].join('');

    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-back-bar">${backBtnHTML()}</div>
        <div class="stim-eyebrow">Stim Mode · Practice Exam</div>
        <h1 class="stim-title">Take a real practice exam.</h1>
        <p class="stim-subtitle">${totalQs} questions across all three exams. Mix MC + short answer. Short-answer questions get a <strong>Grade with Claude</strong> button so you can verify your answer against an expert grader.</p>

        <div class="stim-card">
          <div class="stim-row">
            <label>Exam</label>
            ${examChip(1, 'Exam 1 ('+((examCounts[1]||[]).length)+')')}
            ${examChip(2, 'Exam 2 ('+((examCounts[2]||[]).length)+')')}
            ${examChip(3, 'Exam 3 ('+((examCounts[3]||[]).length)+')')}
            ${examChip(0, 'Cumulative ('+totalQs+')')}
          </div>
          <div class="stim-row">
            <label>Lecture</label>
            ${lectureChipsHtml}
          </div>
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

    // wire chips
    root().querySelectorAll('.stim-chip[data-set]').forEach(b => {
      b.addEventListener('click', () => {
        const k = b.dataset.set, v = b.dataset.val;
        settings[k] = (k === 'type' || k === 'lecture') ? v : Number(v);
        saveJSON(LS_SETTINGS, settings);
        // re-render to update active states
        renderSetup();
      });
    });
    $('#stimStart').addEventListener('click', () => startSession(settings));
    $('#stimDashOpen').addEventListener('click', () => {
      const el = $('#stimDashboard');
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
    });
    wireDashboardCommon();
    wireBackBtn();
  }

  function startSession(settings) {
    const bank = window.STIM_BANK;
    let pool = bank.filter(q => settings.exam === 0 || q.exam === settings.exam);
    if (settings.lecture && settings.lecture !== 'all') {
      pool = pool.filter(q => q.lecture === settings.lecture);
    }
    if (settings.type === 'mc') pool = pool.filter(q => q.type === 'mc');
    if (settings.type === 'sa') pool = pool.filter(q => q.type === 'sa');
    if (pool.length === 0) {
      alert('No questions match those filters.');
      return;
    }
    const sessionId = 'sess_' + Date.now();
    const shuffled = shuffleSeeded(pool, sessionId);
    const target = settings.count === 0 ? shuffled.length : Math.min(settings.count, shuffled.length);
    const selected = shuffled.slice(0, target);

    session = {
      id: sessionId,
      exam: settings.exam,
      count: target,
      type: settings.type,
      timer_sec: settings.timer,
      started_at: Date.now(),
      remaining_sec: settings.timer,
      qids: selected.map(q => q.id),
      current: 0,
      answers: {},   // qid -> { mc_idx | sa_text }
      flags: {},     // qid -> true
      finished: false,
      results: null
    };
    saveJSON(LS_SESSION, session);
    renderExam();
  }

  // -------- exam view --------
  function findQ(id) { return window.STIM_BANK.find(q => q.id === id); }

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

    root().innerHTML = `
      <div class="stim-exam-bar">
        <div class="stim-progress">
          <strong>Q ${session.current + 1} / ${total}</strong>
          <span style="color:var(--ink-faint,#b0a796)">${q.lecture} · ${q.type.toUpperCase()} · ${q.points} pt${q.points>1?'s':''}</span>
        </div>
        <div style="display:flex;gap:12px;align-items:center">
          ${session.timer_sec > 0 ? `<span class="stim-timer" id="stimTimer">--:--</span>` : ''}
          ${backBtnHTML()}
          <button class="stim-btn stim-btn-ghost" id="stimFlag">${flagged?'★ Flagged':'☆ Flag'}</button>
          <button class="stim-btn stim-btn-danger" id="stimSubmit">Submit Exam</button>
        </div>
      </div>
      <div class="stim-pager">${pager}</div>
      <div class="stim-shell">
        <div class="stim-q-meta">
          <span>${esc(q.lecture)}${q.section?' · §'+esc(q.section):''}</span>
          <span>${esc(q.topic||'')}</span>
          <span>${esc(q.difficulty||'')}</span>
        </div>
        <div class="stim-q-stem">${esc(q.q)}</div>
        ${q.type === 'mc' ? '<div class="stim-choices">' + mcChoices + '</div>' : saArea}
        <div class="stim-nav">
          <button class="stim-btn stim-btn-ghost" id="stimPrev" ${session.current===0?'disabled':''}>← Prev</button>
          <div style="display:flex;gap:8px">
            <button class="stim-btn stim-btn-ghost" id="stimSkip">Skip</button>
            <button class="stim-btn" id="stimNext">${session.current === total - 1 ? 'Review →' : 'Next →'}</button>
          </div>
        </div>
      </div>`;

    // wire MC clicks
    root().querySelectorAll('.stim-choice').forEach(b => {
      b.addEventListener('click', () => {
        const idx = Number(b.dataset.mc);
        session.answers[q.id] = { mc_idx: idx };
        saveJSON(LS_SESSION, session);
        root().querySelectorAll('.stim-choice').forEach(x => x.classList.remove('selected'));
        b.classList.add('selected');
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
    $('#stimPrev').addEventListener('click', () => { session.current = Math.max(0, session.current - 1); saveJSON(LS_SESSION, session); renderExam(); });
    $('#stimNext').addEventListener('click', () => {
      if (session.current === total - 1) submitConfirm();
      else { session.current++; saveJSON(LS_SESSION, session); renderExam(); }
    });
    $('#stimSkip').addEventListener('click', () => {
      if (session.current < total - 1) { session.current++; saveJSON(LS_SESSION, session); renderExam(); }
    });
    $('#stimFlag').addEventListener('click', () => {
      session.flags[q.id] = !session.flags[q.id];
      saveJSON(LS_SESSION, session);
      renderExam();
    });
    $('#stimSubmit').addEventListener('click', submitConfirm);
    wireBackBtn();

    // Timer
    if (session.timer_sec > 0) {
      const tick = () => {
        const elapsed = Math.floor((Date.now() - session.started_at) / 1000);
        const remaining = session.timer_sec - elapsed;
        const tEl = $('#stimTimer');
        if (!tEl) return;
        if (remaining <= 0) {
          clearInterval(timerHandle);
          tEl.textContent = '00:00';
          finishSession();
          return;
        }
        const mm = String(Math.floor(remaining / 60)).padStart(2, '0');
        const ss = String(remaining % 60).padStart(2, '0');
        tEl.textContent = `${mm}:${ss}`;
        tEl.classList.toggle('urgent', remaining < 300);
      };
      tick();
      timerHandle = setInterval(tick, 1000);
    }
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
    const results = session.qids.map(id => {
      const q = findQ(id);
      const ans = session.answers[id] || {};
      const result = {
        qid: id,
        lecture: q.lecture,
        section: q.section || '?',
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
      results: sess.results.map(r => {
        const meta = qMeta(r.qid);
        return { qid: r.qid, lecture: r.lecture, section: meta.section, topic: r.topic, type: r.type, score: r.score, max: r.max };
      })
    });
    // cap to last 50
    if (hist.length > 50) hist.splice(0, hist.length - 50);
    saveJSON(LS_HISTORY, hist);
    rebuildStats();
  }

  function rebuildStats() {
    const hist = loadJSON(LS_HISTORY, []);
    const stats = {}; // topic -> { lecture, seen, total_pts, scored_pts, last_seen }
    hist.forEach(s => {
      s.results.forEach(r => {
        if (r.score == null) return; // ungraded SA
        const key = r.topic || r.lecture;
        if (!stats[key]) stats[key] = { lecture: r.lecture, topic: r.topic || '', seen: 0, total_pts: 0, scored_pts: 0, last_seen: 0 };
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
    let totalPts = 0, scoredPts = 0, sessionCount = hist.length;

    // Per (lec § section :: topic) — re-derived from the bank so older
    // history records (which don't store section) still aggregate correctly.
    // Multi-section questions ("A,B") contribute to each section.
    const byTopic = {};
    hist.forEach(s => s.results.forEach(r => {
      if (r.score == null) return;
      totalPts += r.max; scoredPts += r.score;
      const meta = qMeta(r.qid);
      const lec = r.lecture || meta.lecture;
      const top = r.topic || meta.topic || '(general)';
      splitSections(r.section || meta.section).forEach(sec => {
        const key = `${lec}§${sec}::${top}`;
        if (!byTopic[key]) byTopic[key] = { lecture: lec, section: sec, topic: top, seen: 0, total_pts: 0, scored_pts: 0, last_seen: 0 };
        byTopic[key].seen++;
        byTopic[key].total_pts += r.max;
        byTopic[key].scored_pts += r.score;
        byTopic[key].last_seen = Math.max(byTopic[key].last_seen, s.finished_at || s.started_at);
      });
    }));

    // Roll up to (lec § section)
    const bySection = {};
    Object.values(byTopic).forEach(t => {
      const k = `${t.lecture}§${t.section}`;
      if (!bySection[k]) bySection[k] = { lecture: t.lecture, section: t.section, total_pts: 0, scored_pts: 0, seen: 0 };
      bySection[k].total_pts += t.total_pts;
      bySection[k].scored_pts += t.scored_pts;
      bySection[k].seen += t.seen;
    });

    // Roll up to lecture
    const byLec = {};
    Object.values(bySection).forEach(s => {
      if (!byLec[s.lecture]) byLec[s.lecture] = { total_pts: 0, scored_pts: 0, seen: 0 };
      byLec[s.lecture].total_pts += s.total_pts;
      byLec[s.lecture].scored_pts += s.scored_pts;
      byLec[s.lecture].seen += s.seen;
    });

    const accuracy = totalPts > 0 ? Math.round(100 * scoredPts / totalPts) : null;
    const weak = Object.values(byTopic)
      .filter(t => t.seen >= 2 && t.total_pts > 0)
      .map(t => ({ ...t, pct: t.scored_pts / t.total_pts }))
      .sort((a, b) => a.pct - b.pct)
      .slice(0, 8);

    // Persist legacy LS_STATS shape for backwards compat (keyed by topic alone)
    const legacy = {};
    Object.values(byTopic).forEach(t => { legacy[t.topic || t.lecture] = t; });
    saveJSON(LS_STATS, legacy);

    return { totalSessions: sessionCount, accuracy, byLec, bySection, byTopic, weak };
  }

  function renderDashboardHTML(stats) {
    const prefs = Object.assign({}, DASH_DEFAULTS, loadJSON(LS_DASH, {}));
    const bankIdx = buildBankIndex();

    const granChip = (v, l) => `<button class="stim-chip stim-dash-chip${prefs.granularity===v?' active':''}" data-dash="granularity" data-val="${v}">${l}</button>`;
    const toggleChip = (k, l) => `<button class="stim-chip stim-dash-chip${prefs[k]?' active':''}" data-dash="${k}">${l}: ${prefs[k]?'ON':'OFF'}</button>`;

    let heat = '';
    let heatLabel = '';
    if (prefs.granularity === 'lecture') {
      heat = renderLectureHeatmap(stats, bankIdx, prefs);
      heatLabel = 'Per-lecture heatmap';
    } else if (prefs.granularity === 'section') {
      heat = renderSectionHeatmap(stats, bankIdx, prefs);
      heatLabel = 'Per-section heatmap (rows = lecture, columns = section A-E)';
    } else {
      heat = renderMechanismHeatmap(stats, bankIdx, prefs);
      heatLabel = 'Per-mechanism heatmap (one bar per topic)';
    }

    const weakList = stats.weak.length ? stats.weak.map(t =>
      `<li><strong>${esc(t.topic)}</strong> · ${t.lecture} §${t.section} · ${Math.round(t.pct * 100)}% (${t.scored_pts}/${t.total_pts} pts in ${t.seen} attempts)</li>`
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

      <div class="stim-dash-controls">
        <div class="stim-dash-row">
          <label>Granularity</label>
          ${granChip('lecture', 'Lecture')}
          ${granChip('section', 'Section (A-E)')}
          ${granChip('mechanism', 'Mechanism · Concept · Rule')}
        </div>
        <div class="stim-dash-row">
          <label>Display</label>
          ${toggleChip('showPct', 'Show %')}
          ${toggleChip('onlyAttempted', 'Only attempted')}
        </div>
      </div>

      <div style="margin:14px 0 6px;font-size:13px;color:var(--ink-faint,#b0a796);">${heatLabel} — red &lt; 40% · orange &lt; 60% · yellow &lt; 80% · green &ge; 80%</div>
      <div class="stim-heat-wrap">${heat || '<em style="color:var(--ink-faint,#b0a796)">No data yet.</em>'}</div>
      <div style="margin:18px 0 6px;font-size:13px;color:var(--ink-faint,#b0a796);">Topics to work on</div>
      <ul style="margin:0;padding-left:20px;font-size:13px;line-height:1.7;">${weakList}</ul>
      <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:20px;padding-top:16px;border-top:1px solid var(--rule,rgba(255,255,255,0.08));">
        <button class="stim-btn stim-btn-ghost" data-action="reset-progress">Reset progress</button>
      </div>
    `;
  }

  function renderLectureHeatmap(stats, bankIdx, prefs) {
    const lectures = bankIdx.lectures.length ? bankIdx.lectures : Object.keys(stats.byLec).sort();
    const cells = lectures.map(lec => {
      const v = stats.byLec[lec];
      const pct = v && v.total_pts > 0 ? v.scored_pts / v.total_pts : null;
      if (prefs.onlyAttempted && pct == null) return '';
      const color = heatColor(pct);
      const label = prefs.showPct && pct != null ? `${lec}<br><span class="stim-heat-pct">${Math.round(pct*100)}%</span>` : lec;
      const title = `${lec} — ${pct==null?'no attempts':Math.round(pct*100)+'% ('+v.scored_pts+'/'+v.total_pts+' pts, '+v.seen+' Qs)'}`;
      return `<div class="stim-heat-cell" style="background:${color};color:#1a1a1a" title="${esc(title)}">${label}</div>`;
    }).join('');
    return `<div class="stim-heatmap">${cells}</div>`;
  }

  function renderSectionHeatmap(stats, bankIdx, prefs) {
    const lectures = bankIdx.lectures;
    if (lectures.length === 0) return '';
    // determine union of section letters across all lectures (typically A-E or A-F)
    const allSections = new Set();
    Object.values(bankIdx.lecSections).forEach(arr => arr.forEach(s => allSections.add(s)));
    const sections = [...allSections].sort();

    const headerCells = sections.map(s => `<div class="stim-grid-head">§${s}</div>`).join('');
    const rows = lectures.map(lec => {
      const cells = sections.map(s => {
        const k = `${lec}§${s}`;
        const inBank = bankIdx.sections[k];
        if (!inBank) return `<div class="stim-grid-cell empty" title="No questions for ${lec} §${s}"></div>`;
        const v = stats.bySection[k];
        const pct = v && v.total_pts > 0 ? v.scored_pts / v.total_pts : null;
        if (prefs.onlyAttempted && pct == null) {
          return `<div class="stim-grid-cell empty" title="${lec} §${s} — no attempts"></div>`;
        }
        const color = heatColor(pct);
        const pctTxt = prefs.showPct && pct != null ? `<span class="stim-grid-pct">${Math.round(pct*100)}%</span>` : '';
        const seenTxt = v ? `<span class="stim-grid-n">${v.seen}/${inBank.q_count}</span>` : `<span class="stim-grid-n">0/${inBank.q_count}</span>`;
        const title = `${lec} §${s} — ${pct==null?'no attempts':Math.round(pct*100)+'%'} · ${v?v.scored_pts+'/'+v.total_pts+' pts':'0 pts'} · ${v?v.seen:0}/${inBank.q_count} Qs`;
        return `<div class="stim-grid-cell" style="background:${color};color:#1a1a1a" title="${esc(title)}">${pctTxt}${seenTxt}</div>`;
      }).join('');
      return `<div class="stim-grid-row"><div class="stim-grid-lab">${lec}</div>${cells}</div>`;
    }).join('');

    return `
      <div class="stim-grid">
        <div class="stim-grid-row stim-grid-header"><div class="stim-grid-lab"></div>${headerCells}</div>
        ${rows}
      </div>
    `;
  }

  function renderMechanismHeatmap(stats, bankIdx, prefs) {
    // Group bank topics by (lecture, section), render each group as a labeled
    // band of horizontal bars — one bar per topic.
    const lectures = bankIdx.lectures;
    if (lectures.length === 0) return '';

    let html = '<div class="stim-mech-list">';
    lectures.forEach(lec => {
      const lecSecs = bankIdx.lecSections[lec] || [];
      lecSecs.forEach(sec => {
        const sk = `${lec}§${sec}`;
        const sectionInfo = bankIdx.sections[sk];
        if (!sectionInfo) return;
        const topics = sectionInfo.topics;
        // build per-topic rows
        const rows = topics.map(top => {
          const tk = `${sk}::${top}`;
          const t = stats.byTopic[tk];
          const inBank = bankIdx.topics[tk];
          const pct = t && t.total_pts > 0 ? t.scored_pts / t.total_pts : null;
          if (prefs.onlyAttempted && pct == null) return '';
          const color = heatColor(pct);
          const widthPct = pct == null ? 0 : Math.max(4, pct * 100);
          const pctTxt = prefs.showPct && pct != null ? `${Math.round(pct*100)}%` : (pct == null ? '—' : '');
          const meta = `${t?t.seen:0}/${inBank?inBank.q_count:0} Q · ${t?t.scored_pts:0}/${t?t.total_pts:0} pt`;
          return `
            <div class="stim-mech-row">
              <div class="stim-mech-name" title="${esc(top)}">${esc(top)}</div>
              <div class="stim-mech-bar"><div class="stim-mech-fill" style="width:${widthPct}%;background:${color};"></div></div>
              <div class="stim-mech-pct">${pctTxt}</div>
              <div class="stim-mech-n">${meta}</div>
            </div>`;
        }).filter(Boolean).join('');
        if (!rows) return;
        html += `
          <details class="stim-mech-group" ${prefs.onlyAttempted ? 'open' : ''}>
            <summary><strong>${lec} §${sec}</strong> <span class="stim-mech-summary-meta">${topics.length} topics · ${sectionInfo.q_count} Qs</span></summary>
            <div class="stim-mech-rows">${rows}</div>
          </details>`;
      });
    });
    html += '</div>';
    return html;
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
    // Dashboard preference chips — re-render the dashboard in place so the
    // user keeps their scroll position relative to the Your-progress card.
    document.querySelectorAll('.stim-dash-chip').forEach(b => {
      b.addEventListener('click', () => {
        const prefs = Object.assign({}, DASH_DEFAULTS, loadJSON(LS_DASH, {}));
        const k = b.dataset.dash;
        const v = b.dataset.val;
        if (k === 'granularity') prefs.granularity = v;
        else prefs[k] = !prefs[k]; // boolean toggles
        saveJSON(LS_DASH, prefs);
        // Re-render the dashboard card in place (don't blow away the whole view)
        const dash = document.getElementById('stimDashboard');
        if (dash) {
          dash.innerHTML = `<h3 style="margin-top:0;font-family:var(--ff-display,serif);">Your progress</h3>${renderDashboardHTML(computeStats())}`;
          wireDashboardCommon();
        }
      });
    });
  }

  // -------- back-to-study button --------
  function backBtnHTML() {
    return `<button class="stim-btn stim-btn-ghost stim-back-btn" id="stimBackToStudy" title="Switch to Study mode (your STIM session is auto-saved)">← Back to Study</button>`;
  }
  function wireBackBtn() {
    const b = document.getElementById('stimBackToStudy');
    if (b) b.addEventListener('click', () => {
      if (typeof window.setMode === 'function') window.setMode('study');
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
    const mcPts = mcResults.reduce((a, x) => a + (x.score || 0), 0);
    const mcMax = mcResults.reduce((a, x) => a + x.max, 0);
    const saPts = saGraded.reduce((a, x) => a + (x.score || 0), 0);
    const saMax = saGraded.reduce((a, x) => a + x.max, 0);
    const overallPts = mcPts + saPts;
    const overallMax = mcMax + saMax;
    const overallPct = overallMax > 0 ? Math.round(100 * overallPts / overallMax) : 0;
    const elapsed = Math.round((session.finished_at - session.started_at) / 1000);
    const mm = Math.floor(elapsed / 60), ss = elapsed % 60;

    const stats = computeStats();

    const ungradedSAs = saResults.filter(x => x.score == null && (x.user_sa_text || '').trim());
    const batchBtn = ungradedSAs.length > 0
      ? `<button class="stim-btn" id="stimBatchGrade" title="Send all your answered SA responses to Claude in one prompt">Grade all my SAs (${ungradedSAs.length})</button>`
      : '';

    root().innerHTML = `
      <div class="stim-shell">
        <div class="stim-back-bar">${backBtnHTML()}</div>
        <div class="stim-eyebrow">Stim Mode · Results</div>
        <h1 class="stim-title">${overallPct}% — ${session.exam===0?'Cumulative':'Exam '+session.exam} practice</h1>
        <p class="stim-subtitle">${overallPts}/${overallMax} pts · ${mcCorrect}/${mcTotal} MC · ${saGraded.length}/${saResults.length} SA graded · ${mm}m ${ss}s elapsed</p>

        <div class="stim-result-summary">
          <div class="stim-stat"><div class="stim-stat-num">${overallPct}%</div><div class="stim-stat-lbl">Overall</div></div>
          <div class="stim-stat"><div class="stim-stat-num">${mcCorrect}/${mcTotal}</div><div class="stim-stat-lbl">MC correct</div></div>
          <div class="stim-stat"><div class="stim-stat-num">${saUngraded}</div><div class="stim-stat-lbl">SA awaiting grade</div></div>
        </div>

        <div class="stim-row" style="margin:16px 0 22px">
          <button class="stim-btn" id="stimNew">New exam</button>
          <button class="stim-btn stim-btn-ghost" id="stimReview">Review questions</button>
          <button class="stim-btn stim-btn-ghost" id="stimDashToggle">Toggle dashboard</button>
          ${batchBtn}
        </div>

        <div id="stimBatchGradeArea" style="display:none"></div>

        <div class="stim-card" id="stimDashboard">
          <h3 style="margin-top:0;font-family:var(--ff-display,serif);">Your progress</h3>
          ${renderDashboardHTML(stats)}
        </div>

        <div id="stimReviewSection" style="display:none">
          <h2 style="font-family:var(--ff-display,serif);font-size:24px;margin:32px 0 12px;">Question-by-question review</h2>
          <div class="stim-review-filter" id="stimReviewFilter">${renderReviewFilterChips()}</div>
          <div id="stimReviewList">${renderFilteredReview(r)}</div>
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
        wireReviewFilterChips();
        el.scrollIntoView({ behavior: 'smooth' });
      }
    });
    $('#stimDashToggle').addEventListener('click', () => {
      const el = $('#stimDashboard');
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
    });
    if (batchBtn) {
      $('#stimBatchGrade').addEventListener('click', openBatchGrade);
    }
    wireDashboardCommon();
    wireBackBtn();
  }

  // ---- Review filter chips (All / Answered / Unanswered / Wrong / Ungraded) ----
  function renderReviewFilterChips() {
    const f = loadJSON(LS_REVIEW, 'all');
    const chip = (v, l) => `<button class="stim-chip stim-review-chip${f===v?' active':''}" data-rfilter="${v}">${l}</button>`;
    return `
      <span class="stim-dash-row-label">Show</span>
      ${chip('all', 'All')}
      ${chip('answered', 'Answered')}
      ${chip('unanswered', 'Unanswered')}
      ${chip('wrong', 'Wrong / Partial')}
      ${chip('ungraded', 'Ungraded SAs')}
    `;
  }

  function isAnswered(res, q) {
    if (!q) return false;
    if (q.type === 'mc') return res.user_mc_idx != null;
    return !!(res.user_sa_text && res.user_sa_text.trim());
  }

  function renderFilteredReview(results) {
    const f = loadJSON(LS_REVIEW, 'all');
    const filtered = results.filter(res => {
      const q = findQ(res.qid);
      if (!q) return false;
      const answered = isAnswered(res, q);
      if (f === 'all') return true;
      if (f === 'answered') return answered;
      if (f === 'unanswered') return !answered;
      if (f === 'wrong') {
        if (q.type === 'mc') return answered && !res.correct;
        return res.score != null && res.score < q.points;
      }
      if (f === 'ungraded') return q.type === 'sa' && answered && res.score == null;
      return true;
    });
    if (filtered.length === 0) {
      return `<div style="padding:18px;color:var(--ink-faint,#b0a796);font-style:italic">No questions match this filter.</div>`;
    }
    return filtered.map((res, i) => renderResultCardHTML(res, results.indexOf(res))).join('');
  }

  function wireReviewFilterChips() {
    document.querySelectorAll('.stim-review-chip').forEach(b => {
      b.addEventListener('click', () => {
        saveJSON(LS_REVIEW, b.dataset.rfilter);
        document.getElementById('stimReviewFilter').innerHTML = renderReviewFilterChips();
        document.getElementById('stimReviewList').innerHTML = renderFilteredReview(session.results);
        wireResultCardHandlers();
        wireReviewFilterChips();
      });
    });
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

  // -------- batch grade with claude --------
  function openBatchGrade() {
    const ungraded = session.results.filter(r => {
      const q = findQ(r.qid);
      return q && q.type === 'sa' && r.score == null && (r.user_sa_text || '').trim();
    });
    if (ungraded.length === 0) {
      alert('No ungraded short-answer responses to grade.');
      return;
    }

    const blocks = ungraded.map((r, i) => {
      const q = findQ(r.qid);
      const rubricLines = (q.rubric && q.rubric.criteria || []).map(c => `- ${c.pts} pt: ${c.desc}`).join('\n');
      const max = q.rubric ? q.rubric.total : q.points;
      return `========== Q${i+1} of ${ungraded.length} · qid: ${r.qid} (${max} pts) ==========
QUESTION:
${q.q}

STUDENT ANSWER:
${r.user_sa_text}

RUBRIC (total ${max} pts):
${rubricLines}

MODEL ANSWER (reference; don't penalize alternative correct answers):
${q.model_answer || '(none provided)'}`;
    }).join('\n\n');

    const prompt = `You are grading ${ungraded.length} BIOL 4230 (Evolution) short-answer responses in one batch.

For EACH question, grade strictly per rubric. Be fair but accurate. Then reply with ONLY a single JSON array, no other text before or after — one object per question, in the SAME ORDER as the questions appear below:

[
  {
    "qid": "<qid string from the header>",
    "score": <integer>,
    "max": <integer>,
    "per_criterion": [{"pts_awarded": 0|1, "feedback": "specific feedback for this criterion"}],
    "topics_to_work_on": ["specific topic 1", "specific topic 2"],
    "overall_feedback": "1-3 sentences"
  },
  ...
]

QUESTIONS TO GRADE:

${blocks}

End of questions. Reply with the JSON array only.`;

    const copy = (text) => {
      if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
      const ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand('copy');
      document.body.removeChild(ta);
      return Promise.resolve();
    };

    const area = document.getElementById('stimBatchGradeArea');
    area.style.display = 'block';
    area.innerHTML = `
      <div class="stim-card" id="stimBatchCard">
        <h3 style="margin-top:0;font-family:var(--ff-display,serif);">Batch grade · ${ungraded.length} short answers</h3>
        <ol style="font-size:13px;line-height:1.6;color:var(--ink-faint,#b0a796);padding-left:20px;">
          <li>Prompt was copied to your clipboard. claude.ai is opening in a new tab.</li>
          <li>Paste the prompt into Claude. Wait for the JSON array reply.</li>
          <li>Copy Claude's reply (the entire JSON array) and paste it into the box below.</li>
          <li>Click <strong>Apply all grades</strong> — every score is updated and your dashboard rebuilds.</li>
        </ol>
        <textarea class="stim-grade-paste" id="stimBatchPaste" placeholder="Paste Claude's JSON array here…" style="min-height:160px"></textarea>
        <div style="display:flex;gap:8px;margin-top:8px;flex-wrap:wrap">
          <button class="stim-btn" id="stimBatchApply">Apply all grades</button>
          <button class="stim-btn stim-btn-ghost" id="stimBatchRecopy">Re-copy prompt</button>
          <button class="stim-btn stim-btn-ghost" id="stimBatchCancel">Close</button>
        </div>
        <div class="stim-grade-msg" id="stimBatchMsg" style="font-size:13px;margin-top:8px"></div>
      </div>
    `;

    copy(prompt).then(() => {
      window.open('https://claude.ai/new', '_blank', 'noopener');
      const msg = document.getElementById('stimBatchMsg');
      msg.style.color = '#5fb87a';
      msg.textContent = `✓ Prompt for ${ungraded.length} questions copied. Paste into Claude → paste reply below.`;
    }).catch(() => {
      alert('Could not copy. The prompt is too long to display here — please use the per-question grade buttons instead.');
    });

    document.getElementById('stimBatchApply').addEventListener('click', () => applyBatchGrade(ungraded));
    document.getElementById('stimBatchRecopy').addEventListener('click', () => {
      copy(prompt).then(() => {
        const msg = document.getElementById('stimBatchMsg');
        msg.style.color = '#5fb87a';
        msg.textContent = '✓ Prompt re-copied to clipboard.';
      });
    });
    document.getElementById('stimBatchCancel').addEventListener('click', () => {
      area.style.display = 'none';
      area.innerHTML = '';
    });

    area.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function applyBatchGrade(ungraded) {
    const ta = document.getElementById('stimBatchPaste');
    const msg = document.getElementById('stimBatchMsg');
    const raw = (ta && ta.value || '').trim();
    if (!raw) {
      msg.style.color = '#c74e4e';
      msg.textContent = '✗ Paste Claude\'s JSON array first.';
      return;
    }
    // Try to extract a JSON array — tolerate leading/trailing text.
    const m = raw.match(/\[[\s\S]*\]/);
    if (!m) {
      msg.style.color = '#c74e4e';
      msg.textContent = '✗ Could not find a JSON array in the pasted text.';
      return;
    }
    let parsed;
    try { parsed = JSON.parse(m[0]); }
    catch (e) {
      msg.style.color = '#c74e4e';
      msg.textContent = '✗ JSON failed to parse: ' + e.message;
      return;
    }
    if (!Array.isArray(parsed)) {
      msg.style.color = '#c74e4e';
      msg.textContent = '✗ Expected a JSON array but got ' + (typeof parsed) + '.';
      return;
    }

    let applied = 0, missed = [];
    parsed.forEach(item => {
      if (!item || !item.qid) return;
      const res = session.results.find(r => r.qid === item.qid);
      const q = findQ(item.qid);
      if (!res || !q) { missed.push(item.qid); return; }
      const max = q.rubric ? q.rubric.total : q.points;
      const score = Math.max(0, Math.min(max, Number(item.score) || 0));
      res.score = score;
      res.claude_grade = item;
      applied++;
    });

    if (applied === 0) {
      msg.style.color = '#c74e4e';
      msg.textContent = '✗ No qids in your paste matched this session. Did you paste the wrong array?';
      return;
    }

    saveJSON(LS_SESSION, session);
    // Update history record for this session
    const hist = loadJSON(LS_HISTORY, []);
    if (hist.length) {
      const last = hist[hist.length - 1];
      if (last.id === session.id) {
        parsed.forEach(item => {
          const histRes = last.results.find(r => r.qid === item.qid);
          if (histRes) histRes.score = Math.max(0, Math.min(histRes.max, Number(item.score) || 0));
        });
        saveJSON(LS_HISTORY, hist);
      }
    }
    rebuildStats();

    msg.style.color = '#5fb87a';
    msg.textContent = `✓ Applied ${applied}/${parsed.length} grades. ${missed.length ? '(' + missed.length + ' qid mismatches: ' + missed.slice(0,3).join(', ') + (missed.length>3?'…':'') + ')' : ''} Reloading results…`;
    setTimeout(() => renderResults(), 1100);
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
