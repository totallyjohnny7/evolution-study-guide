/* ===== ESG Review-Page UI · shared renderer for Exam 1 / 2 / 3 =====
 * Requires: window.COURSE (set by content-exam*.js), window.ESG (from esg-db.js)
 * Renders: sidebar nav, study mode (all content), flashcard mode (ESG-scheduled),
 *          test mode (multiple choice with scoring).
 * Expects DOM: #sb, #mode-bar, #main-content
 * ==================================================================== */
(function(){
  'use strict';

  // -------- Helpers --------
  function $(sel, root){ return (root || document).querySelector(sel); }
  function $$(sel, root){ return Array.from((root || document).querySelectorAll(sel)); }
  function h(tag, attrs, ...kids){
    var el = document.createElement(tag);
    if (attrs){
      for (var k in attrs){
        if (k === 'class') el.className = attrs[k];
        else if (k === 'html') el.innerHTML = attrs[k];
        else if (k.startsWith('on') && typeof attrs[k] === 'function') el.addEventListener(k.slice(2), attrs[k]);
        else if (attrs[k] != null) el.setAttribute(k, attrs[k]);
      }
    }
    kids.flat().forEach(function(kid){
      if (kid == null || kid === false) return;
      if (typeof kid === 'string') el.appendChild(document.createTextNode(kid));
      else el.appendChild(kid);
    });
    return el;
  }
  // Render markdown-ish text: **bold**, newlines -> <br>, digit-bullets keep
  function fmt(text){
    if (!text) return '';
    var s = escapeHtml(text);
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\n/g, '<br>');
    return s;
  }
  function escapeHtml(s){
    // Escape only BARE ampersands — leave existing entities (&ldquo;, &amp;, &#8220;) intact.
    return String(s)
      .replace(/&(?![a-zA-Z][a-zA-Z0-9]*;|#\d+;|#x[0-9a-fA-F]+;)/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  // -------- State --------
  var COURSE = window.COURSE;
  if (!COURSE){ console.error('[ESG-UI] window.COURSE not found'); return; }
  var state = {
    mode: 'study',          // 'study' | 'card' | 'test' | 'visuals'
    testIdx: 0,
    testAnswers: [],
    cardsQueue: [],
    cardIdx: 0,
    cardFlipped: false,
    cardShownAt: 0,
  };

  // -------- Persist test progress per course (localStorage) --------
  // Keys are namespaced by COURSE.id so exam1/2/3/final don't collide.
  function testKey(){ return COURSE.id + '::test'; }
  function saveTestState(){
    try {
      var payload = { testIdx: state.testIdx, testAnswers: state.testAnswers, ts: Date.now() };
      localStorage.setItem(testKey(), JSON.stringify(payload));
    } catch(e){}
  }
  function loadTestState(){
    try {
      var raw = localStorage.getItem(testKey());
      if (!raw) return;
      var p = JSON.parse(raw);
      if (typeof p.testIdx === 'number') state.testIdx = p.testIdx;
      if (Array.isArray(p.testAnswers)) state.testAnswers = p.testAnswers;
    } catch(e){}
  }
  // Run at script load
  loadTestState();

  // -------- Sidebar --------
  function buildSidebar(){
    var sb = $('#sb');
    sb.innerHTML = '';
    sb.appendChild(h('div', {class: 'st'},
      COURSE.title,
      h('span', {}, COURSE.subtitle || '')
    ));
    var lastGroup = null;
    COURSE.chapters.forEach(function(ch){
      // Optional exam/visuals group header (inserted only when the group changes)
      if (ch.group && ch.group !== lastGroup){
        sb.appendChild(h('div', {class: 'grp'}, ch.group));
        lastGroup = ch.group;
      }
      // Visuals anchor — single clickable entry, no sections, switches mode
      if (ch.visualsAnchor){
        var visList = h('div', {class: 'cll'});
        var visLink = h('a', {href: '#', 'data-visuals': '1'}, '🎨 ' + (ch.title || 'Visuals'));
        visLink.addEventListener('click', function(e){
          e.preventDefault();
          setMode('visuals');
          if (window.matchMedia && window.matchMedia('(max-width: 840px)').matches) sb.classList.remove('open');
        });
        visList.appendChild(visLink);
        sb.appendChild(visList);
        return;
      }
      sb.appendChild(h('div', {class: 'cl'}, 'Ch ' + ch.num + ' · ' + ch.title));
      var list = h('div', {class: 'cll'});
      ch.sections.forEach(function(sec){
        var label = (sec.num ? sec.num + ' — ' : '') + sec.title;
        var link = h('a', {href: '#' + sec.id, 'data-sec': sec.id}, label);
        link.addEventListener('click', function(e){
          if (window.matchMedia && window.matchMedia('(max-width: 840px)').matches) {
            sb.classList.remove('open');
          }
          e.preventDefault();
          // Update hash (also bookmark-friendly)
          if (history.replaceState) history.replaceState(null, '', '#' + sec.id);
          var switchMode = state.mode !== 'study';
          if (switchMode) setMode('study');
          // Hammer the scroll — defeats any competing scroll resets from
          // renderStudy's innerHTML wipe or image lazy-load layout shifts.
          var delays = switchMode ? [80, 200, 400, 700, 1100, 1600, 2200] : [0, 80, 200, 500, 1000];
          delays.forEach(function(d){
            setTimeout(function(){
              var t = document.getElementById(sec.id);
              if (!t) return;
              var y = t.getBoundingClientRect().top + (window.scrollY || window.pageYOffset) - 50;
              document.documentElement.scrollTop = y;
              document.body.scrollTop = y;
            }, d);
          });
        });
        list.appendChild(link);
      });
      sb.appendChild(list);
    });
  }

  // -------- Study mode --------
  // Eagerly render every chapter. Images already have loading="lazy", so the
  // cost of building DOM is bounded. Prior attempts at chapter-level lazy
  // render broke hash-nav scroll positioning when later chapters rendered
  // after the target chapter's offsetTop was computed.
  function renderStudy(){
    var root = $('#main-content');
    root.innerHTML = '';
    root.appendChild(h('div', {class: 'ph'},
      h('h1', {}, COURSE.title),
      h('p', {}, COURSE.subtitle || '')
    ));
    var chapters = (COURSE.chapters || []).filter(function(ch){ return !ch.visualsAnchor; });
    chapters.forEach(function(ch){
      var host = h('div', {class: 'ch-host', 'data-ch': ch.id});
      root.appendChild(host);
      // Chapter header
      host.appendChild(h('div', {class: 'chh'},
        h('h2', {},
          h('span', {class: 'cn'}, 'Ch ' + ch.num),
          document.createTextNode(ch.title)
        ),
        ch.tagline ? h('p', {}, ch.tagline) : null
      ));
      // One-page cheat sheet (collapsed by default)
      if (ch.cheatsheet){
        var cs = document.createElement('details');
        cs.className = 'cheatsheet';
        var summary = document.createElement('summary');
        // ch.num is controlled (Roman, digit, or '★') — safe. Title goes through
        // the textContent path below, not innerHTML.
        summary.innerHTML = '📋 <strong>Cheat Sheet</strong> · one-page summary of Ch ' +
          escapeHtml(String(ch.num || ''));
        cs.appendChild(summary);
        var body = h('div', {class: 'cheatsheet-body', html: fmt(ch.cheatsheet).replace(/\n/g, '<br>')});
        cs.appendChild(body);
        host.appendChild(cs);
      }
      (ch.sections || []).forEach(function(sec){
        host.appendChild(renderSection(sec));
      });
    });
    // Inline test questions for every section, once chapters are all rendered
    renderStudyQuestions();
  }
  function renderSection(sec){
    var title = [];
    if (sec.num){
      title.push(h('span', {class: 'num'}, sec.num));
    }
    title.push(document.createTextNode(sec.title));
    var el = h('div', {class: 'sec', id: sec.id},
      h('h3', {}, title)
    );
    (sec.blocks || []).forEach(function(b){
      el.appendChild(renderBlock(b));
    });
    // Placeholder where test questions for this section will go
    el.appendChild(h('div', {'data-qslot': sec.id}));
    return el;
  }
  function renderBlock(b){
    if (b.kind === 'table'){
      var tbl = h('table', {class: 'ct'});
      var thead = h('thead');
      var tr = h('tr');
      (b.head || []).forEach(function(c){ tr.appendChild(h('th', {}, c)); });
      thead.appendChild(tr); tbl.appendChild(thead);
      var tbody = h('tbody');
      (b.rows || []).forEach(function(row){
        var rtr = h('tr');
        row.forEach(function(c){ rtr.appendChild(h('td', {html: fmt(c)})); });
        tbody.appendChild(rtr);
      });
      tbl.appendChild(tbody);
      return tbl;
    }
    if (b.kind === 'figure'){
      var fig = h('figure', {class: 'fb'});
      var img = h('img', {src: b.src, alt: b.caption || '', loading: 'lazy'});
      fig.appendChild(img);
      if (b.caption){
        fig.appendChild(h('figcaption', {}, b.caption));
      }
      return fig;
    }
    if (b.kind === 'svg'){
      var box = h('div', {class: 'svgb', html: b.svg || ''});
      if (b.viz){ box.setAttribute('data-viz', b.viz); }
      // Initialize any interactive widgets after the node is attached
      // to the DOM so measurements are correct.
      setTimeout(function(){
        if (window.ESG_VIZ && typeof window.ESG_VIZ.init === 'function'){
          try { window.ESG_VIZ.init(box); } catch(e){ console.warn('ESG_VIZ init failed', e); }
        }
      }, 0);
      return box;
    }
    var classMap = { wb: 'wb', yb: 'yb', hb: 'hb', trap: 'trap', rem: 'rem', mn: 'mn' };
    var labelMap = {
      wb: ['bl', 'What it is'], yb: ['bl', 'Why it matters'], hb: ['bl', 'How it works'],
      trap: ['tl', b.label || '⚠ Trap'],
      rem: ['rl', b.label || 'The thing to remember'],
      mn:  ['ml', b.label || 'Mnemonic']
    };
    var cls = classMap[b.kind] || 'wb';
    var lm = labelMap[b.kind] || ['bl', ''];
    return h('div', {class: cls},
      h('div', {class: lm[0]}, lm[1]),
      h('div', {html: fmt(b.body)})
    );
  }
  function renderStudyQuestions(){
    // Group test questions by sectionId
    var bySection = {};
    (COURSE.test || []).forEach(function(q){
      var sid = q.sectionId || 'misc';
      if (!bySection[sid]) bySection[sid] = [];
      bySection[sid].push(q);
    });
    Object.keys(bySection).forEach(function(sid){
      var slot = document.querySelector('[data-qslot="' + cssEscape(sid) + '"]');
      if (!slot) return;
      // Guard against double-fill when called repeatedly (e.g., lazy chapter
      // force-renders each re-run renderStudyQuestions for the whole course).
      if (slot.dataset.filled === '1') return;
      slot.dataset.filled = '1';
      bySection[sid].forEach(function(q, i){
        slot.appendChild(renderInlineQ(q, i + 1));
      });
    });
  }
  function cssEscape(s){ return String(s).replace(/[^a-zA-Z0-9_-]/g, '\\$&'); }

  function renderInlineQ(q, n){
    var qb = h('div', {class: 'qb'},
      h('div', {class: 'qh'}, 'Q' + n),
      h('div', {class: 'qq', html: fmt(q.prompt)})
    );
    var ch = h('div', {class: 'ch'});
    q.choices.forEach(function(c, i){
      var btn = h('button', {class: 'cb', type: 'button', 'data-i': i},
        String.fromCharCode(65 + i) + ') ', document.createTextNode(c)
      );
      btn.addEventListener('click', function(){
        $$('button', ch).forEach(function(b, bi){
          b.disabled = true;
          if (bi === q.answer) b.classList.add('correct');
          else if (bi === i) b.classList.add('wrong');
        });
        exp.classList.add('show');
      });
      ch.appendChild(btn);
    });
    qb.appendChild(ch);
    var exp = h('div', {class: 'exp', html: '<strong>Answer: ' + String.fromCharCode(65 + q.answer) + '.</strong> ' + fmt(q.why || '')});
    qb.appendChild(exp);
    return qb;
  }

  // -------- Flashcard mode (ESG-wired) --------
  var ESG_SOURCE = null; // set from COURSE.id
  // A card can declare its own .source (e.g., the Final merges cards from
  // exam1/2/3 and wants progress to carry through). If it does, the stored
  // card keeps that source and its id uses that prefix. Otherwise everything
  // is keyed to the page's COURSE.id — identical to the pre-merge behavior.
  function cardSource(c){ return (c && c.source) || ESG_SOURCE; }
  function cardId(c, i){ return cardSource(c) + '::fc::' + (c && c.sourceIdx != null ? c.sourceIdx : i); }

  // Union getAllCards across every source that appears in COURSE.flashcards.
  // For single-source decks (exam1/2/3 pages) this is exactly one source.
  async function getAllCourseCards(){
    if (!window.ESG) return [];
    var flashcards = COURSE.flashcards || [];
    var sources = {};
    flashcards.forEach(function(c){ sources[cardSource(c)] = true; });
    var sourceList = Object.keys(sources);
    if (sourceList.length === 0) sourceList = [ESG_SOURCE];
    if (sourceList.length === 1) return window.ESG.getAllCards(sourceList[0]);
    var all = [];
    for (var i = 0; i < sourceList.length; i++){
      var got = await window.ESG.getAllCards(sourceList[i]);
      all = all.concat(got);
    }
    return all;
  }

  // Lookup map: card id → COURSE-level metadata (analogy, hint). Populated
  // by seedFlashcardsToESG so renderCard can display those fields without
  // having to widen the IndexedDB schema.
  var cardMeta = {};
  function getCardMeta(id){ return cardMeta[id] || {}; }

  async function seedFlashcardsToESG(){
    var flashcards = COURSE.flashcards || [];
    // Group cards by their source so we can seed each source independently.
    var bySource = {};
    var nextIdx = {};
    flashcards.forEach(function(c, i){
      var src = cardSource(c);
      if (c.sourceIdx == null){
        if (nextIdx[src] == null) nextIdx[src] = 0;
        c.sourceIdx = nextIdx[src]++;
      }
      var id = cardId(c, i);
      // Remember analogy/hint for render-time overlay
      cardMeta[id] = { analogy: c.analogy, hint: c.hint, chapterId: c.chapterId, sectionId: c.sectionId };
      if (!bySource[src]) bySource[src] = [];
      bySource[src].push({ id: id, term: c.q, def: c.a, chip: c.chapterId || '' });
    });
    if (!window.ESG) return;
    var sources = Object.keys(bySource);
    for (var i = 0; i < sources.length; i++){
      await window.ESG.seedCardsIfNeeded(sources[i], bySource[sources[i]]);
    }
  }
  async function loadQueue(){
    if (!window.ESG){
      // Fallback: just use all flashcards in order
      state.cardsQueue = (COURSE.flashcards || []).map(function(c, i){
        return { id: 'fc-' + i, term: c.q, def: c.a, queue: 'new' };
      });
      return;
    }
    var all = await getAllCourseCards();
    var now = Date.now();
    // Due cards first
    var due = all.filter(function(c){ return c.queue !== 'suspended' && c.due <= now; });
    due.sort(function(a, b){
      // Order: learning > review > new, then by due
      var order = { learning: 0, relearning: 0, review: 1, new: 2 };
      var oa = order[a.queue] != null ? order[a.queue] : 3;
      var ob = order[b.queue] != null ? order[b.queue] : 3;
      if (oa !== ob) return oa - ob;
      return a.due - b.due;
    });
    state.cardsQueue = due;
  }
  async function renderCard(){
    var root = $('#main-content');
    root.innerHTML = '';
    var wrap = h('div', {id: 'card-mode', class: 'active'});
    root.appendChild(wrap);
    var deck = h('div', {class: 'card-deck'});
    wrap.appendChild(deck);

    if (!window.ESG || !window.ESG._isReady()){
      deck.appendChild(h('div', {class: 'card-meta'},
        h('span', {}, 'Flashcards · offline mode'),
        h('span', {}, (COURSE.flashcards || []).length + ' cards')
      ));
    } else {
      var all = await getAllCourseCards();
      var now = Date.now();
      var stats = { new: 0, learning: 0, review: 0, due: 0 };
      all.forEach(function(c){
        if (c.queue === 'suspended') return;
        if (c.queue === 'new') stats.new++;
        else if (c.queue === 'learning' || c.queue === 'relearning') stats.learning++;
        else if (c.queue === 'review') stats.review++;
        if (c.due <= now && c.queue !== 'suspended') stats.due++;
      });
      deck.appendChild(h('div', {class: 'card-meta'},
        h('div', {class: 'queue-stats'},
          h('span', {}, h('span', {class: 'dot dot-new'}), 'New ', String(stats.new)),
          h('span', {}, h('span', {class: 'dot dot-learn'}), 'Learning ', String(stats.learning)),
          h('span', {}, h('span', {class: 'dot dot-review'}), 'Review ', String(stats.review))
        ),
        h('span', {}, stats.due + ' due now')
      ));
    }

    if (!state.cardsQueue.length){
      deck.appendChild(h('div', {class: 'card-empty'},
        h('div', {class: 'big'}, 'All caught up'),
        h('p', {}, 'No cards due right now. Come back later — your scheduler will surface them as they ripen.'),
        h('button', {class: 'mode-btn', style: 'margin-top:18px', onclick: async function(){
          // Reset: show all cards again (browse mode)
          if (!window.ESG){
            state.cardsQueue = (COURSE.flashcards || []).map(function(c, i){ return { id: 'fc-' + i, term: c.q, def: c.a, queue: 'new' }; });
          } else {
            state.cardsQueue = await getAllCourseCards();
            state.cardsQueue = state.cardsQueue.filter(function(c){ return c.queue !== 'suspended'; });
          }
          state.cardIdx = 0;
          state.cardFlipped = false;
          renderCard();
        }}, 'Browse all cards')
      ));
      return;
    }

    var card = state.cardsQueue[state.cardIdx];
    if (!card){
      state.cardIdx = 0;
      await loadQueue();
      return renderCard();
    }
    state.cardShownAt = Date.now();

    var queueLabel = 'Card ' + (state.cardIdx + 1) + ' / ' + state.cardsQueue.length;
    if (card.queue) queueLabel += ' · ' + card.queue.toUpperCase();

    var meta = getCardMeta(card.id);
    var backChildren = [
      h('div', {class: 'card-label'}, 'Answer'),
      h('div', {class: 'card-a', html: fmt(card.def || card.a || '')})
    ];
    if (meta.analogy){
      backChildren.push(h('div', {class: 'card-analogy'},
        h('span', {class: 'card-analogy-label'}, '📎 Analogy'),
        h('div', {class: 'card-analogy-body'}, meta.analogy)
      ));
    }
    if (meta.hint){
      backChildren.push(h('div', {class: 'card-hint-block'},
        h('span', {class: 'card-hint-label'}, '💡 Hint'),
        h('div', {class: 'card-hint-body'}, meta.hint)
      ));
    }

    var flip = h('div', {class: 'flipcard' + (state.cardFlipped ? ' flipped' : '')});
    var inner = h('div', {class: 'flipcard-inner'});
    inner.appendChild(h('div', {class: 'flipcard-front'},
      h('div', {class: 'card-label'}, queueLabel),
      h('div', {class: 'card-q', html: fmt(card.term || card.q || '')}),
      h('div', {class: 'card-hint'}, 'Tap / Space to reveal · Swipe → pass · ← fail')
    ));
    inner.appendChild(h('div', {class: 'flipcard-back'}, backChildren));
    flip.appendChild(inner);
    flip.addEventListener('click', function(e){
      // Don't flip when user released a swipe drag
      if (flip.__swipeActive) return;
      state.cardFlipped = !state.cardFlipped;
      flip.classList.toggle('flipped');
    });
    // Swipe gesture (pointer events — works for touch + mouse)
    attachSwipe(flip, function(direction){
      if (!state.cardFlipped) return; // must flip first
      rateCard(direction === 'right' ? 'pass' : 'fail');
    });
    deck.appendChild(flip);

    var controls = h('div', {class: 'card-controls'});
    controls.appendChild(h('button', {class: 'rate-btn rate-fail', onclick: function(){ rateCard('fail'); }},
      'Again ✕', h('small', {}, 'swipe ← or press 1')
    ));
    controls.appendChild(h('button', {class: 'rate-btn rate-pass', onclick: function(){ rateCard('pass'); }},
      'Got it ✓', h('small', {}, 'swipe → or press 2')
    ));
    deck.appendChild(controls);

    // Session stats bar
    var sstats = state.sessionStats || { right: 0, wrong: 0 };
    deck.appendChild(h('div', {class: 'card-session-stats'},
      h('span', {class: 'cs-pass'}, '✓ ' + sstats.right + ' got'),
      h('span', {class: 'cs-fail'}, '✕ ' + sstats.wrong + ' missed'),
      h('span', {class: 'cs-pct'}, (sstats.right + sstats.wrong) > 0
        ? Math.round(100 * sstats.right / (sstats.right + sstats.wrong)) + '% this session'
        : 'Start rating to see stats')
    ));
  }

  function installCardKeybinds(){
    if (window.__cardKeybindsInstalled) return;
    window.__cardKeybindsInstalled = true;
    document.addEventListener('keydown', function(e){
      if (state.mode !== 'card') return;
      if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;
      if (e.code === 'Space' || e.code === 'Enter'){
        e.preventDefault();
        var flip = $('.flipcard');
        if (flip){ state.cardFlipped = !state.cardFlipped; flip.classList.toggle('flipped'); }
      } else if (e.key === '1'){
        e.preventDefault(); rateCard('fail');
      } else if (e.key === '2'){
        e.preventDefault(); rateCard('pass');
      } else if (e.key === 'ArrowRight'){
        if (state.cardFlipped) { e.preventDefault(); rateCard('pass'); }
      } else if (e.key === 'ArrowLeft'){
        if (state.cardFlipped) { e.preventDefault(); rateCard('fail'); }
      }
    });
  }

  // Swipe helper: fires `cb('left'|'right')` once the user drags > 80px
  // horizontally. Green/red tint applied during drag via CSS hooks.
  function attachSwipe(el, cb){
    var startX = 0, startY = 0, dx = 0, active = false, pid = null;
    function reset(){ el.style.transform = ''; el.style.boxShadow = ''; el.classList.remove('swiping-left','swiping-right'); active = false; el.__swipeActive = false; }
    el.addEventListener('pointerdown', function(e){
      // Ignore if the pointer target is a button inside the card
      if (e.target.closest('button')) return;
      pid = e.pointerId; startX = e.clientX; startY = e.clientY; dx = 0;
      active = true; el.__swipeActive = false;
      el.setPointerCapture && el.setPointerCapture(pid);
    });
    el.addEventListener('pointermove', function(e){
      if (!active) return;
      dx = e.clientX - startX;
      var dy = e.clientY - startY;
      if (Math.abs(dy) > Math.abs(dx) * 2) return; // mostly vertical → ignore
      if (Math.abs(dx) > 6) el.__swipeActive = true;
      el.style.transform = 'translateX(' + dx + 'px) rotate(' + (dx * 0.04) + 'deg)';
      el.classList.toggle('swiping-right', dx > 24);
      el.classList.toggle('swiping-left',  dx < -24);
    });
    function end(){
      if (!active) return;
      el.releasePointerCapture && pid && el.releasePointerCapture(pid);
      var finalDx = dx;
      if (Math.abs(finalDx) > 80){
        // Animate off-screen then reset
        el.style.transition = 'transform .25s ease';
        el.style.transform = 'translateX(' + (finalDx > 0 ? 600 : -600) + 'px) rotate(' + (finalDx * 0.04) + 'deg)';
        setTimeout(function(){ el.style.transition = ''; reset(); cb(finalDx > 0 ? 'right' : 'left'); }, 220);
      } else {
        el.style.transition = 'transform .2s ease';
        setTimeout(function(){ el.style.transition = ''; reset(); }, 200);
        el.style.transform = '';
      }
      active = false;
    }
    el.addEventListener('pointerup', end);
    el.addEventListener('pointercancel', end);
  }
  async function rateCard(rating){
    var card = state.cardsQueue[state.cardIdx];
    if (!card) return;
    // Session-level running stats (NOT persisted — wiped on reload)
    if (!state.sessionStats) state.sessionStats = { right: 0, wrong: 0 };
    if (rating === 'pass') state.sessionStats.right++;
    else state.sessionStats.wrong++;
    var timeSpent = Math.round((Date.now() - state.cardShownAt) / 1000);
    if (window.ESG && window.ESG._isReady()){
      var updated = window.ESG.applyRating(card, rating, timeSpent);
      await window.ESG.putCard(updated);
      await window.ESG.logReview({
        cardId: card.id, rating: rating, timeSpent: timeSpent,
        queueAtReview: card.queue, route: location.pathname
      });
    }
    state.cardFlipped = false;
    state.cardIdx++;
    if (state.cardIdx >= state.cardsQueue.length){
      await loadQueue();
      state.cardIdx = 0;
    }
    renderCard();
  }

  // -------- Test mode --------
  function renderTest(){
    var root = $('#main-content');
    root.innerHTML = '';
    var wrap = h('div', {id: 'test-mode', class: 'active'});
    root.appendChild(wrap);
    var qs = (COURSE.test || []);
    if (!qs.length){
      wrap.appendChild(h('div', {class: 'card-empty'},
        h('div', {class: 'big'}, 'No test questions yet')
      ));
      return;
    }
    if (state.testIdx >= qs.length){
      return renderTestResults();
    }
    var q = qs[state.testIdx];
    var pct = Math.round(100 * state.testIdx / qs.length);
    // Null-safe score count (answers may have holes or nulls after reload)
    var scoreCount = state.testAnswers.reduce(function(n, a){ return n + (a && a.correct ? 1 : 0); }, 0);
    wrap.appendChild(h('div', {class: 'ph'},
      h('h1', {}, 'Test Mode'),
      h('p', {}, 'Question ' + (state.testIdx + 1) + ' of ' + qs.length + ' · Score: ' + scoreCount)
    ));
    wrap.appendChild(h('div', {class: 'test-prog'},
      h('div', {class: 'test-prog-fill', style: 'width:' + pct + '%'})
    ));

    var qb = h('div', {class: 'qb test-q'},
      h('div', {class: 'qh'}, 'Question ' + (state.testIdx + 1)),
      h('div', {class: 'qq', html: fmt(q.prompt)})
    );
    // Restore a previously-answered state for this question (Previous nav)
    var prior = state.testAnswers[state.testIdx] || null;
    var selected = prior ? prior.selected : null;
    var ch = h('div', {class: 'ch'});
    q.choices.forEach(function(c, i){
      var btn = h('button', {class: 'cb', type: 'button'},
        String.fromCharCode(65 + i) + ') ', document.createTextNode(c)
      );
      // If already answered, show the historical result immediately
      if (prior){
        btn.disabled = true;
        if (i === q.answer) btn.classList.add('correct');
        else if (i === prior.selected) btn.classList.add('wrong');
      }
      btn.addEventListener('click', function(){
        if (selected != null) return;
        selected = i;
        $$('button', ch).forEach(function(b, bi){
          b.disabled = true;
          if (bi === q.answer) b.classList.add('correct');
          else if (bi === i) b.classList.add('wrong');
        });
        exp.classList.add('show');
        $('#btn-next-test').disabled = false;
        state.testAnswers[state.testIdx] = {
          qIdx: state.testIdx, selected: i, correct: i === q.answer
        };
        saveTestState();
      });
      ch.appendChild(btn);
    });
    qb.appendChild(ch);
    var exp = h('div', {class: 'exp' + (prior ? ' show' : ''), html: '<strong>Answer: ' + String.fromCharCode(65 + q.answer) + '.</strong> ' + fmt(q.why || '')});
    qb.appendChild(exp);
    wrap.appendChild(qb);
    wrap.appendChild(h('div', {class: 'test-actions'},
      h('button', {onclick: function(){
        if (state.testIdx > 0){ state.testIdx--; saveTestState(); renderTest(); }
      }, disabled: state.testIdx === 0 ? '' : null}, '← Previous'),
      h('button', {id: 'btn-next-test', class: 'primary',
        disabled: prior ? null : '',
        onclick: function(){ state.testIdx++; saveTestState(); renderTest(); }}, state.testIdx + 1 === qs.length ? 'Finish →' : 'Next →'),
      h('button', {class: 'ghost', onclick: function(){
        if (!confirm('Reset test progress for this deck?')) return;
        state.testIdx = 0; state.testAnswers = [];
        try { localStorage.removeItem(testKey()); } catch(e){}
        renderTest();
      }}, '↻ Reset')
    ));
  }
  function renderTestResults(){
    var root = $('#main-content');
    root.innerHTML = '';
    var correct = state.testAnswers.filter(function(a){ return a && a.correct; }).length;
    var total = (COURSE.test || []).length;
    var pct = Math.round(100 * correct / total);
    var msg = pct >= 90 ? 'Exam-ready.' : pct >= 75 ? 'Close — drill the traps.' : pct >= 50 ? 'Foundations holding. Keep going.' : 'Restart study mode before retesting.';
    root.appendChild(h('div', {class: 'results'},
      h('div', {class: 'score'}, String(correct), h('small', {}, '/' + total)),
      h('div', {class: 'pct'}, pct + '% correct'),
      h('div', {class: 'msg'}, msg),
      h('button', {class: 'mode-btn active', onclick: function(){
        state.testIdx = 0;
        state.testAnswers = [];
        try { localStorage.removeItem(testKey()); } catch(e){}
        renderTest();
      }}, 'Retake test'),
      ' ',
      h('button', {class: 'mode-btn', onclick: function(){ setMode('study'); }}, 'Back to study')
    ));
  }

  // -------- Mode switcher --------
  function setMode(m){
    state.mode = m;
    $$('#mode-bar .mode-btn').forEach(function(b){ b.classList.toggle('active', b.dataset.mode === m); });
    // Reset transient state when switching
    if (m === 'study'){
      renderStudy();
      // Scroll to current hash if any (instant — smooth scroll lags across
      // 17 chapters and competes with sidebar-click hammer)
      if (location.hash) {
        var t = document.getElementById(location.hash.slice(1));
        if (t) setTimeout(function(){ t.scrollIntoView({behavior: 'auto', block: 'start'}); }, 50);
      }
    } else if (m === 'card'){
      (async function(){
        await seedFlashcardsToESG();
        await loadQueue();
        state.cardIdx = 0;
        state.cardFlipped = false;
        renderCard();
        installCardKeybinds();
      })();
    } else if (m === 'test'){
      renderTest();
    } else if (m === 'visuals'){
      renderVisuals();
    }
    try { localStorage.setItem(COURSE.id + '::mode', m); } catch(e){}
  }

  function renderVisuals(){
    var root = $('#main-content');
    root.innerHTML = '';
    // iframe loads on-demand; browser caches subsequent mode switches.
    var frame = h('iframe', {
      id: 'visuals-frame',
      src: '/visuals.html',
      loading: 'lazy',
      title: 'Interactive Visuals',
      allow: 'clipboard-read; clipboard-write'
    });
    root.appendChild(frame);
  }

  function buildModeBar(){
    var bar = $('#mode-bar');
    bar.innerHTML = '';
    bar.appendChild(h('button', {id: 'sb-toggle', 'aria-label': 'Toggle navigation', onclick: function(e){ e.stopPropagation(); $('#sb').classList.toggle('open'); }}, '☰'));
    bar.appendChild(h('button', {class: 'mode-btn active', 'data-mode': 'study', onclick: function(){ setMode('study'); }}, '📖 Study'));
    bar.appendChild(h('button', {class: 'mode-btn', 'data-mode': 'card', onclick: function(){ setMode('card'); }}, '🃏 Flashcards'));
    bar.appendChild(h('button', {class: 'mode-btn', 'data-mode': 'test', onclick: function(){ setMode('test'); }}, '🎯 Test'));
    if (COURSE.hasVisuals){
      bar.appendChild(h('button', {class: 'mode-btn', 'data-mode': 'visuals', onclick: function(){ setMode('visuals'); }}, '🎨 Visuals'));
    }
    bar.appendChild(h('a', {href: '/', class: 'mode-btn ghost', style: 'text-decoration:none'}, '← Home'));
  }

  // -------- Scroll-spy for sidebar --------
  function initScrollSpy(){
    var links = $$('#sb .cll a');
    var sections = links.map(function(a){
      return { a: a, el: document.getElementById(a.dataset.sec) };
    }).filter(function(x){ return x.el; });
    if (!sections.length) return;
    var main = document.getElementById('main');
    var usesMainScroll = main && main.scrollHeight > main.clientHeight + 1;
    var scroller = usesMainScroll ? main : window;
    function update(){
      // Use viewport-relative top for window, offsetTop for #main
      var pivot = 100;
      var active = sections[0];
      for (var i = 0; i < sections.length; i++){
        var top = usesMainScroll
          ? sections[i].el.offsetTop - main.scrollTop
          : sections[i].el.getBoundingClientRect().top;
        if (top <= pivot) active = sections[i];
      }
      links.forEach(function(a){ a.classList.remove('active'); });
      if (active) active.a.classList.add('active');
    }
    scroller.addEventListener('scroll', update, { passive: true });
    update();
  }

  // Re-align scroll to #hash target when images/layout shift after nav.
  // This runs 250ms + 700ms after every hashchange and once on load.
  function realignToHash(){
    if (!location.hash) return;
    var t = document.getElementById(location.hash.slice(1));
    if (!t) return;
    var y = t.getBoundingClientRect().top + (window.scrollY || window.pageYOffset) - 50;
    document.documentElement.scrollTop = y;
    document.body.scrollTop = y;
  }
  window.addEventListener('hashchange', function(){
    // Hammer the realign until scroll sticks (image loads shift layout)
    [0, 50, 150, 300, 500, 800, 1200, 1800].forEach(function(d){
      setTimeout(realignToHash, d);
    });
  });

  // -------- Boot --------
  function boot(){
    ESG_SOURCE = COURSE.id;
    buildSidebar();
    buildModeBar();
    // Close mobile sidebar when tapping outside of it
    document.addEventListener('click', function(e){
      var sb = $('#sb');
      if (!sb || !sb.classList.contains('open')) return;
      if (e.target.closest('#sb') || e.target.closest('#sb-toggle')) return;
      sb.classList.remove('open');
    });
    // Restore last mode
    var saved = 'study';
    try { saved = localStorage.getItem(COURSE.id + '::mode') || 'study'; } catch(e){}
    setMode(saved);
    if (saved === 'study') setTimeout(initScrollSpy, 100);
  }

  // Guarded boot: only run the real boot once per page load.
  function safeBoot(){
    if (window.__esgUiBooted) return;
    window.__esgUiBooted = true;
    try { boot(); }
    catch (e) {
      console.error('[ESG-UI] boot failed:', e);
      window.__esgUiBooted = false; // allow retry
      // Last-resort surface the error so the user sees something
      var m = document.getElementById('main-content');
      if (m) m.innerHTML = '<div class="ph"><h1>Loading error</h1><p>' + (e && e.message) + '</p></div>';
    }
  }

  // 1. Boot immediately — defer loading guarantees DOM is ready and COURSE is set.
  //    ESG (IndexedDB) is optional for the initial render; flashcard mode waits for it on demand.
  safeBoot();

  // 2. Also listen for esg-ready in case ESG finishes AFTER we've already rendered,
  //    so flashcard seeding can proceed. (No-op if already booted.)
  document.addEventListener('esg-ready', safeBoot);
})();
