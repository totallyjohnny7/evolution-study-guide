/* Blink Reminder
 * Floating toggle that plays a gentle tone + flashes a visual cue every N seconds.
 * Helpful during long study sessions where blink rate drops, causing eye strain.
 *
 * Controls:
 *   - Click button         → toggle ON/OFF
 *   - Right-click button   → cycle interval (4s/6s/8s/12s/20s/30s)
 *   - Keyboard 'b'         → toggle (when not in input field)
 *
 * State persisted in localStorage:
 *   evol-blink-on        '1' | '0'
 *   evol-blink-interval  number of seconds
 */
(function () {
  if (window.__blinkReminderInstalled) return;
  window.__blinkReminderInstalled = true;

  const LS_ON = 'study-blink-on';
  const LS_INT = 'study-blink-interval';
  const INTERVALS = [3, 4, 5, 6, 8, 10, 15, 20, 30];

  let on = localStorage.getItem(LS_ON) === '1';
  let intervalSec = parseInt(localStorage.getItem(LS_INT), 10);
  if (!INTERVALS.includes(intervalSec)) intervalSec = 5;

  let timer = null;
  let audioCtx = null;
  let lastTickTs = 0;

  function ensureAudio() {
    if (!audioCtx) {
      try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      } catch (e) {}
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume().catch(function () {});
    }
  }

  function playBlinkTone() {
    if (!audioCtx) return;
    try {
      const t = audioCtx.currentTime;
      const o = audioCtx.createOscillator();
      const g = audioCtx.createGain();
      o.connect(g);
      g.connect(audioCtx.destination);
      o.type = 'sine';
      o.frequency.setValueAtTime(660, t);
      o.frequency.linearRampToValueAtTime(880, t + 0.05);
      g.gain.setValueAtTime(0, t);
      g.gain.linearRampToValueAtTime(0.06, t + 0.01);
      g.gain.exponentialRampToValueAtTime(0.001, t + 0.18);
      o.start(t);
      o.stop(t + 0.2);
    } catch (e) {}
  }

  function flashCue() {
    const cue = document.createElement('div');
    cue.id = 'blinkReminderCue';
    cue.innerHTML = '👁 <span>blink</span>';
    cue.style.cssText =
      'position:fixed;top:24px;left:50%;transform:translateX(-50%);' +
      'background:rgba(15,23,42,.92);color:#fbbf24;font:700 16px system-ui;' +
      'padding:8px 18px;border-radius:24px;z-index:99999;pointer-events:none;' +
      'box-shadow:0 4px 12px rgba(0,0,0,.35);' +
      'animation:blinkReminderCueAnim 1.2s ease-out forwards;letter-spacing:.5px;';
    document.body.appendChild(cue);
    setTimeout(function () {
      if (cue && cue.parentNode) cue.parentNode.removeChild(cue);
    }, 1300);
  }

  function tick() {
    const now = Date.now();
    if (now - lastTickTs < (intervalSec * 1000) - 200) return;
    lastTickTs = now;
    flashCue();
    playBlinkTone();
  }

  function start() {
    ensureAudio();
    stop();
    lastTickTs = Date.now();
    timer = setInterval(tick, intervalSec * 1000);
  }

  function stop() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  function setOn(value) {
    on = !!value;
    localStorage.setItem(LS_ON, on ? '1' : '0');
    if (on) start();
    else stop();
    updateUI();
  }

  function cycleInterval() {
    const idx = INTERVALS.indexOf(intervalSec);
    intervalSec = INTERVALS[(idx + 1) % INTERVALS.length];
    localStorage.setItem(LS_INT, String(intervalSec));
    if (on) start();
    updateUI();
    flashCue(); // preview the new cadence visually
  }

  function updateUI() {
    if (!btn) return;
    btn.classList.toggle('on', on);
    btn.innerHTML =
      '<span class="br-eye">👁</span>' +
      '<span class="br-label">' + (on ? 'Blink Reminder · ON' : 'Blink Reminder') + '</span>' +
      '<span class="br-int">' + intervalSec + 's</span>';
  }

  // ---------- inject styles ----------
  const css =
    '@keyframes blinkReminderCueAnim {' +
    '  0%   { opacity:0; transform:translateX(-50%) translateY(-8px) scale(.95); }' +
    '  20%  { opacity:1; transform:translateX(-50%) translateY(0) scale(1); }' +
    '  60%  { opacity:1; }' +
    '  100% { opacity:0; transform:translateX(-50%) translateY(-4px) scale(1); }' +
    '}' +
    '#blinkReminderBtn {' +
    '  position:fixed; bottom:80px; right:16px; z-index:9999;' +
    '  display:inline-flex; gap:8px; align-items:center;' +
    '  background:#1e293b; color:#cbd5e1; border:1px solid #475569;' +
    '  padding:8px 13px; border-radius:24px;' +
    '  font:600 12px/1 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;' +
    '  cursor:pointer; user-select:none;' +
    '  box-shadow:0 2px 6px rgba(0,0,0,.25); transition:all .15s;' +
    '  -webkit-tap-highlight-color: transparent;' +
    '}' +
    '#blinkReminderBtn:hover { transform:translateY(-1px); box-shadow:0 4px 10px rgba(0,0,0,.3); }' +
    '#blinkReminderBtn.on {' +
    '  background:linear-gradient(135deg,#15803d,#22c55e); color:#ecfdf5;' +
    '  border-color:#86efac;' +
    '  box-shadow:0 0 0 0 rgba(34,197,94,.5); animation:blinkBtnPulse 2s infinite;' +
    '}' +
    '#blinkReminderBtn .br-eye { font-size:14px; line-height:1; }' +
    '#blinkReminderBtn .br-int {' +
    '  background:rgba(0,0,0,.3); color:#fde68a;' +
    '  padding:2px 7px; border-radius:10px;' +
    '  font-weight:800; font-size:10.5px; letter-spacing:.3px;' +
    '}' +
    '@keyframes blinkBtnPulse {' +
    '  0%   { box-shadow:0 0 0 0 rgba(34,197,94,.45); }' +
    '  70%  { box-shadow:0 0 0 9px rgba(34,197,94,0); }' +
    '  100% { box-shadow:0 0 0 0 rgba(34,197,94,0); }' +
    '}' +
    '@media print { #blinkReminderBtn, #blinkReminderCue { display:none !important; } }' +
    '@media (max-width:540px) {' +
    '  #blinkReminderBtn { bottom:74px; right:10px; padding:7px 10px; font-size:11px; }' +
    '  #blinkReminderBtn .br-label { display:none; }' +
    '}';
  const style = document.createElement('style');
  style.id = 'blinkReminderStyles';
  style.textContent = css;
  (document.head || document.documentElement).appendChild(style);

  // ---------- build button ----------
  const btn = document.createElement('button');
  btn.id = 'blinkReminderBtn';
  btn.type = 'button';
  btn.title = 'Blink reminder — click to toggle, right-click to change interval, press B';
  btn.setAttribute('aria-label', 'Toggle blink reminder');

  function attachWhenReady() {
    if (!document.body) {
      return setTimeout(attachWhenReady, 50);
    }
    document.body.appendChild(btn);
    updateUI();
  }
  attachWhenReady();

  btn.addEventListener('click', function (e) {
    ensureAudio();
    setOn(!on);
  });
  btn.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    ensureAudio();
    cycleInterval();
  });

  // Keyboard shortcut: 'b'
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'b' && e.key !== 'B') return;
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    const t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    e.preventDefault();
    ensureAudio();
    setOn(!on);
  });

  // Resume audio on first user interaction (browsers block silent autoplay)
  function unlockAudioOnce() {
    ensureAudio();
    document.removeEventListener('click', unlockAudioOnce);
    document.removeEventListener('keydown', unlockAudioOnce);
    document.removeEventListener('touchstart', unlockAudioOnce);
  }
  document.addEventListener('click', unlockAudioOnce, { once: true });
  document.addEventListener('keydown', unlockAudioOnce, { once: true });
  document.addEventListener('touchstart', unlockAudioOnce, { once: true });

  if (on) start();
})();
