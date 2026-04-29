/* Stim Mode — practice exam simulator with Grade-with-Claude flow.
   Reads window.STIM_BANK / window.STIM_INDEX (loaded from stim-bank.js).
   Persists state to localStorage under stim_session, stim_history, stim_topic_stats. */
(function () {
  'use strict';

  const LS_SESSION = 'evol_stim_session';
  const LS_HISTORY = 'evol_stim_history';
  const LS_STATS   = 'evol_stim_topic_stats';
  const LS_SETTINGS = 'evol_stim_settings';

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
    const settings = loadJSON(LS_SETTINGS, { exam: 1, count: 25, type: 'mixed', timer: 0 });
    const stats = computeStats();

    const examChip = (n, label) => `<button class="stim-chip${settings.exam===n?' active':''}" data-set="exam" data-val="${n}">${label}</button>`;
    const countChip = n => `<button class="stim-chip${settings.count===n?' active':''}" data-set="count" data-val="${n}">${n===0?'All':n}</button>`;
    const typeChip = (v, l) => `<button class="stim-chip${settings.type===v?' active':''}" data-set="type" data-val="${v}">${l}</button>`;
    const timerChip = (s, l) => `<button class="stim-chip${settings.timer===s?' active':''}" data-set="timer" data-val="${s}">${l}</button>`;

    const idx = window.STIM_INDEX || { byExam: {}, byLecture: {} };
    const examCounts = idx.byExam || {};
    const totalQs = Array.isArray(window.STIM_BANK) ? window.STIM_BANK.length : 0;

    root().innerHTML = `
      <div class="stim-shell">
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
        settings[k] = (k === 'type') ? v : Number(v);
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
  }

  function startSession(settings) {
    const bank = window.STIM_BANK;
    let pool = bank.filter(q => settings.exam === 0 || q.exam === settings.exam);
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
    const stats = loadJSON(LS_STATS, {});
    let totalPts = 0, scoredPts = 0, sessionCount = hist.length;
    hist.forEach(s => s.results.forEach(r => {
      if (r.score == null) return;
      totalPts += r.max; scoredPts += r.score;
    }));
    const accuracy = totalPts > 0 ? Math.round(100 * scoredPts / totalPts) : null;
    // by lecture
    const byLec = {};
    Object.values(stats).forEach(t => {
      if (!byLec[t.lecture]) byLec[t.lecture] = { total_pts: 0, scored_pts: 0, seen: 0 };
      byLec[t.lecture].total_pts += t.total_pts;
      byLec[t.lecture].scored_pts += t.scored_pts;
      byLec[t.lecture].seen += t.seen;
    });
    // weak topics (min 3 seen, sorted by score_pct ascending)
    const weak = Object.values(stats)
      .filter(t => t.seen >= 2 && t.total_pts > 0)
      .map(t => ({ ...t, pct: t.scored_pts / t.total_pts }))
      .sort((a, b) => a.pct - b.pct)
      .slice(0, 8);
    return { totalSessions: sessionCount, accuracy, byLec, weak };
  }

  function renderDashboardHTML(stats) {
    const lecKeys = Object.keys(stats.byLec).sort();
    const heat = lecKeys.map(k => {
      const v = stats.byLec[k];
      const pct = v.total_pts > 0 ? v.scored_pts / v.total_pts : null;
      const color = pct == null ? '#444' : pct < 0.4 ? '#c74e4e' : pct < 0.6 ? '#d69b4e' : pct < 0.8 ? '#d6c84e' : '#5fb87a';
      return `<div class="stim-heat-cell" style="background:${color};color:#1a1a1a" title="${k} — ${pct==null?'no data':Math.round(pct*100)+'%'}">${k}</div>`;
    }).join('');
    const weakList = stats.weak.length ? stats.weak.map(t =>
      `<li><strong>${esc(t.topic)}</strong> · ${t.lecture} · ${Math.round(t.pct * 100)}% (${t.scored_pts}/${t.total_pts} pts in ${t.seen} attempts)</li>`
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
      <div style="margin:18px 0 6px;font-size:13px;color:var(--ink-faint,#b0a796);">Per-lecture heatmap (red = weak, green = strong)</div>
      <div class="stim-heatmap">${heat || '<em style="color:var(--ink-faint,#b0a796)">No data yet.</em>'}</div>
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

    root().innerHTML = `
      <div class="stim-shell">
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
