/* evolution-study-guide — shared IndexedDB layer (Dexie) + Anki-style binary scheduler
 * Exposed as window.ESG.
 * DB name: evolution_study_guide
 * Schema v1 — cards/reviews/meta. Case A: greenfield; no legacy migration.
 */
(function (global) {
  'use strict';

  var DB_NAME = 'evolution_study_guide';
  var BC_NAME = 'evolution_study_guide_sync';

  var DEFAULT_SETTINGS = {
    learningSteps: [60, 600],
    relearningSteps: [600],
    minIntervalDays: 1,
    leechThreshold: 8,
    leechAction: 'suspend',
    maxAnswerSeconds: 60,
    newCardOrder: 'sequential'
  };

  // ---------- Toast ----------
  function toast(msg, ms) {
    try {
      var el = document.getElementById('esg-toast');
      if (!el) {
        el = document.createElement('div');
        el.id = 'esg-toast';
        el.style.cssText =
          'position:fixed;left:50%;bottom:18px;transform:translateX(-50%);' +
          'background:#1f2937;color:#fff;padding:10px 14px;border-radius:8px;' +
          'font:13px/1.4 system-ui,sans-serif;box-shadow:0 4px 14px rgba(0,0,0,.35);' +
          'z-index:999999;max-width:min(90vw,480px);opacity:0;transition:opacity .2s';
        document.body && document.body.appendChild(el);
      }
      el.textContent = msg;
      requestAnimationFrame(function () { el.style.opacity = '1'; });
      clearTimeout(el._t);
      el._t = setTimeout(function () { el.style.opacity = '0'; }, ms || 3200);
    } catch (e) { /* noop */ }
  }

  // ---------- In-memory fallback ----------
  var fallback = {
    active: false,
    cards: new Map(),
    reviews: [],
    settings: JSON.parse(JSON.stringify(DEFAULT_SETTINGS)),
    migrated_v1: true
  };

  function useFallback(reason) {
    if (!fallback.active) {
      fallback.active = true;
      console.warn('[ESG] Falling back to in-memory store:', reason);
      toast('Offline review state (in-memory). Progress won\'t persist across reloads.');
    }
  }

  // ---------- Dexie bootstrap ----------
  var db = null;
  var dexieReady = false;

  function initDexie() {
    if (global.__dexieLoadFailed || typeof global.Dexie === 'undefined') {
      useFallback('Dexie unavailable');
      return;
    }
    try {
      db = new global.Dexie(DB_NAME);
      db.version(1).stores({
        cards:   'id, due, queue, source, lastReview, [queue+due], [source+queue+due]',
        reviews: '++id, cardId, ts, route',
        meta:    'key'
      });
      dexieReady = true;
    } catch (e) {
      console.error('[ESG] Dexie init failed', e);
      useFallback('init failed: ' + (e && e.message));
    }
  }

  function classifyError(e) {
    var name = e && (e.name || (e.inner && e.inner.name)) || '';
    return {
      quota: /QuotaExceededError/i.test(name),
      invalidState: /InvalidStateError/i.test(name),
      version: /VersionError/i.test(name)
    };
  }

  function handleDbError(e, context) {
    var c = classifyError(e);
    if (c.quota) toast('Storage quota exceeded. Some data may not persist.');
    else if (c.invalidState) toast('Browser blocked IndexedDB (private mode?).');
    else if (c.version) toast('Database version mismatch — reload the page.');
    else toast('Storage error' + (context ? ' (' + context + ')' : ''));
    useFallback((c.quota ? 'quota' : c.invalidState ? 'invalid state' : c.version ? 'version' : 'other') + ': ' + (e && e.message));
  }

  // ---------- Settings ----------
  function getSettings() {
    if (fallback.active || !dexieReady) {
      return Promise.resolve(Object.assign({}, DEFAULT_SETTINGS, fallback.settings));
    }
    return db.meta.get('settings').then(function (row) {
      if (row && row.value) return Object.assign({}, DEFAULT_SETTINGS, row.value);
      return Object.assign({}, DEFAULT_SETTINGS);
    }).catch(function (e) { handleDbError(e, 'getSettings'); return Object.assign({}, DEFAULT_SETTINGS, fallback.settings); });
  }

  function updateSettings(partial) {
    if (fallback.active || !dexieReady) {
      Object.assign(fallback.settings, partial || {});
      broadcast({ type: 'settings-updated' });
      return Promise.resolve(Object.assign({}, DEFAULT_SETTINGS, fallback.settings));
    }
    return db.transaction('rw', db.meta, function () {
      return db.meta.get('settings').then(function (row) {
        var merged = Object.assign({}, DEFAULT_SETTINGS, (row && row.value) || {}, partial || {});
        return db.meta.put({ key: 'settings', value: merged }).then(function () { return merged; });
      });
    }).then(function (merged) {
      broadcast({ type: 'settings-updated' });
      return merged;
    }).catch(function (e) { handleDbError(e, 'updateSettings'); Object.assign(fallback.settings, partial || {}); broadcast({ type: 'settings-updated' }); return Object.assign({}, DEFAULT_SETTINGS, fallback.settings); });
  }

  // ---------- Card CRUD ----------
  function newCardDefaults(id, source, term, def, chip) {
    var now = Date.now();
    return {
      id: id,
      source: source,
      term: term || '',
      def: def || '',
      chip: chip || '',
      queue: 'new',
      due: now,
      lastReview: null,
      stability: 0,
      difficulty: 5,
      reps: 0,
      lapses: 0,
      learningStep: 0,
      isLeech: false,
      introducedAt: now
    };
  }

  function getCard(id) {
    if (fallback.active || !dexieReady) {
      return Promise.resolve(fallback.cards.get(id) || null);
    }
    return db.cards.get(id).catch(function (e) { handleDbError(e, 'getCard'); return fallback.cards.get(id) || null; });
  }

  function putCard(card) {
    if (!card || !card.id) return Promise.resolve(null);
    if (fallback.active || !dexieReady) {
      fallback.cards.set(card.id, card);
      broadcast({ type: 'card-updated', cardId: card.id });
      return Promise.resolve(card);
    }
    return db.cards.put(card).then(function () {
      broadcast({ type: 'card-updated', cardId: card.id });
      return card;
    }).catch(function (e) { handleDbError(e, 'putCard'); fallback.cards.set(card.id, card); broadcast({ type: 'card-updated', cardId: card.id }); return card; });
  }

  function bulkPutCards(cards) {
    if (!cards || !cards.length) return Promise.resolve(0);
    if (fallback.active || !dexieReady) {
      cards.forEach(function (c) { fallback.cards.set(c.id, c); });
      return Promise.resolve(cards.length);
    }
    return db.cards.bulkPut(cards).then(function () { return cards.length; })
      .catch(function (e) { handleDbError(e, 'bulkPutCards'); cards.forEach(function (c) { fallback.cards.set(c.id, c); }); return cards.length; });
  }

  function getAllCards(source) {
    if (fallback.active || !dexieReady) {
      var arr = Array.from(fallback.cards.values());
      if (source) arr = arr.filter(function (c) { return c.source === source; });
      return Promise.resolve(arr);
    }
    var coll = source ? db.cards.where('source').equals(source) : db.cards;
    return coll.toArray().catch(function (e) { handleDbError(e, 'getAllCards'); return []; });
  }

  function getDueQueue(opts) {
    opts = opts || {};
    var now = typeof opts.now === 'number' ? opts.now : Date.now();
    var src = opts.source || null;
    var limit = opts.limit || 500;
    var filter = function (c) {
      if (c.queue === 'suspended') return false;
      if (src && c.source !== src) return false;
      return c.due <= now;
    };
    return getAllCards(src).then(function (all) {
      var filtered = all.filter(filter);
      filtered.sort(function (a, b) {
        if (a.due !== b.due) return a.due - b.due;
        return (a.introducedAt || 0) - (b.introducedAt || 0);
      });
      return filtered.slice(0, limit);
    });
  }

  // ---------- Review log ----------
  function logReview(row) {
    if (!row || !row.cardId) return Promise.resolve(null);
    var clamped = Math.min(row.timeSpent || 0, (row._maxSeconds || 60));
    var normalized = {
      cardId: row.cardId,
      ts: row.ts || Date.now(),
      rating: row.rating === 'pass' ? 'pass' : 'fail',
      timeSpent: clamped,
      queueAtReview: row.queueAtReview || 'new',
      route: row.route || ''
    };
    if (fallback.active || !dexieReady) {
      fallback.reviews.push(normalized);
      return Promise.resolve(normalized);
    }
    return db.reviews.add(normalized).then(function () { return normalized; })
      .catch(function (e) { handleDbError(e, 'logReview'); fallback.reviews.push(normalized); return normalized; });
  }

  // ---------- Scheduler — binary Pass/Fail ----------
  function applyRating(card, rating, timeSpent) {
    // Returns mutated card (new object) per state machine.
    if (!card) return card;
    var s = ESG._settingsCache || DEFAULT_SETTINGS;
    var maxT = s.maxAnswerSeconds || 60;
    var clampedT = Math.min(typeof timeSpent === 'number' ? timeSpent : 0, maxT);
    var out = Object.assign({}, card);
    var now = Date.now();
    var SEC = 1000;
    var DAY = 86400 * 1000;

    // Suspended: no-op.
    if (out.queue === 'suspended') return out;

    var learningSteps = s.learningSteps || DEFAULT_SETTINGS.learningSteps;
    var relearningSteps = s.relearningSteps || DEFAULT_SETTINGS.relearningSteps;
    var minIntervalDays = s.minIntervalDays || 1;
    var leechThreshold = s.leechThreshold || 8;
    var leechAction = s.leechAction || 'suspend';

    out.lastReview = now;

    if (rating === 'pass') {
      if (out.queue === 'new') {
        out.queue = 'learning';
        out.learningStep = 0;
        out.due = now + (learningSteps[0] || 60) * SEC;
      } else if (out.queue === 'learning') {
        var next = out.learningStep + 1;
        if (next < learningSteps.length) {
          out.learningStep = next;
          out.due = now + (learningSteps[next] || 600) * SEC;
        } else {
          out.queue = 'review';
          out.reps = (out.reps || 0) + 1;
          out.stability = Math.max(1, (out.stability || 0) * 2 || 1);
          out.due = now + out.stability * DAY;
          out.learningStep = 0;
        }
      } else if (out.queue === 'review') {
        var mult = 2.5 - (out.difficulty || 5) * 0.1;
        if (mult < 1.1) mult = 1.1;
        out.stability = Math.max(1, (out.stability || 1) * mult);
        out.reps = (out.reps || 0) + 1;
        out.due = now + out.stability * DAY;
      } else if (out.queue === 'relearning') {
        var rNext = out.learningStep + 1;
        if (rNext < relearningSteps.length) {
          out.learningStep = rNext;
          out.due = now + (relearningSteps[rNext] || 600) * SEC;
        } else {
          out.queue = 'review';
          out.stability = Math.max(1, (out.stability || 1) * 1.5);
          var ivSec = Math.max(out.stability * 86400, minIntervalDays * 86400);
          out.due = now + ivSec * SEC;
          out.learningStep = 0;
        }
      }
    } else {
      // rating === 'fail'
      if (out.queue === 'new' || out.queue === 'learning') {
        out.queue = 'learning';
        out.learningStep = 0;
        out.due = now + (learningSteps[0] || 60) * SEC;
      } else if (out.queue === 'review') {
        out.lapses = (out.lapses || 0) + 1;
        out.queue = 'relearning';
        out.learningStep = 0;
        out.difficulty = Math.min(10, (out.difficulty || 5) + 1);
        out.due = now + (relearningSteps[0] || 600) * SEC;
        if (out.lapses >= leechThreshold) {
          if (leechAction === 'suspend') {
            out.queue = 'suspended';
            out.isLeech = true;
          } else {
            out.isLeech = true;
          }
        }
      } else if (out.queue === 'relearning') {
        out.learningStep = 0;
        out.due = now + (relearningSteps[0] || 600) * SEC;
      }
    }

    out._lastRatedTimeSpent = clampedT;
    return out;
  }

  // ---------- Seeding ----------
  function seedCardsIfNeeded(source, cardList) {
    if (!cardList || !cardList.length) return Promise.resolve(0);
    return getAllCards(source).then(function (existing) {
      var haveIds = new Set(existing.map(function (c) { return c.id; }));
      var toInsert = [];
      cardList.forEach(function (c) {
        if (!c || !c.id) return;
        if (!haveIds.has(c.id)) {
          toInsert.push(newCardDefaults(c.id, source, c.term, c.def, c.chip));
        }
      });
      if (!toInsert.length) return 0;
      return bulkPutCards(toInsert);
    });
  }

  // ---------- Migration ----------
  function runMigration() {
    if (fallback.active || !dexieReady) {
      fallback.migrated_v1 = true;
      return getSettings();
    }
    return db.meta.get('migrated_v1').then(function (row) {
      if (row && row.value === true) return null;
      return db.transaction('rw', db.meta, function () {
        return db.meta.get('settings').then(function (sRow) {
          if (!sRow) return db.meta.put({ key: 'settings', value: Object.assign({}, DEFAULT_SETTINGS) });
        }).then(function () {
          return db.meta.put({ key: 'migrated_v1', value: true });
        });
      });
    }).catch(function (e) { handleDbError(e, 'migration'); });
  }

  function migrateIfNeeded() {
    var lockKey = 'evolution_study_guide_migrate_v1';
    if (global.navigator && global.navigator.locks && global.navigator.locks.request) {
      return global.navigator.locks.request(lockKey, { mode: 'exclusive' }, function () {
        return runMigration();
      });
    }
    return runMigration();
  }

  // ---------- BroadcastChannel ----------
  var bc = null;
  function broadcast(msg) {
    if (bc) {
      try { bc.postMessage(msg); } catch (e) { /* noop */ }
    }
  }

  var listeners = [];
  function onSync(fn) { listeners.push(fn); }

  function initBroadcast() {
    if (typeof global.BroadcastChannel === 'undefined') return;
    try {
      bc = new global.BroadcastChannel(BC_NAME);
      bc.onmessage = function (evt) {
        var msg = evt.data || {};
        listeners.forEach(function (fn) { try { fn(msg); } catch (e) { /* noop */ } });
      };
    } catch (e) { /* noop */ }
  }

  // ---------- Debug helpers ----------
  function clearAll() {
    fallback.cards.clear();
    fallback.reviews = [];
    fallback.settings = JSON.parse(JSON.stringify(DEFAULT_SETTINGS));
    fallback.migrated_v1 = false;
    if (!dexieReady) return Promise.resolve();
    return db.delete().then(function () { dexieReady = false; initDexie(); });
  }

  // ---------- Kickoff ----------
  var ESG = {
    DB_NAME: DB_NAME,
    DEFAULT_SETTINGS: DEFAULT_SETTINGS,
    _settingsCache: Object.assign({}, DEFAULT_SETTINGS),
    getSettings: function () { return getSettings().then(function (s) { ESG._settingsCache = s; return s; }); },
    updateSettings: function (p) { return updateSettings(p).then(function (s) { ESG._settingsCache = s; return s; }); },
    getCard: getCard,
    putCard: putCard,
    bulkPutCards: bulkPutCards,
    getAllCards: getAllCards,
    getDueQueue: getDueQueue,
    logReview: function (r) { r._maxSeconds = ESG._settingsCache.maxAnswerSeconds || 60; return logReview(r); },
    applyRating: applyRating,
    seedCardsIfNeeded: seedCardsIfNeeded,
    migrateIfNeeded: migrateIfNeeded,
    onSync: onSync,
    broadcast: broadcast,
    toast: toast,
    clearAll: clearAll,
    newCardDefaults: newCardDefaults,
    _isReady: function () { return dexieReady && !fallback.active; },
    _fallback: fallback
  };

  global.ESG = ESG;

  function boot() {
    initDexie();
    initBroadcast();
    migrateIfNeeded().then(function () {
      return ESG.getSettings();
    }).then(function (s) {
      ESG._settingsCache = s;
      document.dispatchEvent(new CustomEvent('esg-ready', { detail: { ready: true } }));
    }).catch(function (e) {
      console.error('[ESG] boot failed', e);
      useFallback('boot: ' + (e && e.message));
      document.dispatchEvent(new CustomEvent('esg-ready', { detail: { ready: false, fallback: true } }));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})(window);
