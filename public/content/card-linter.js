/* card-linter.js — Pure-function linter for flashcards.
 *
 * Usage from browser console:
 *   cardLinter.lintCard(someCard)         -> { errors: [], warnings: [], info: [] }
 *   cardLinter.report()                   -> prints per-rule summary across all decks
 *   cardLinter.report({ deck: 'L08' })    -> filter to one deck
 *   cardLinter.leeches()                  -> list cards with >5 lifetime misses (rule 7)
 *
 * Implements the 7 card-design laws from docs/redesign-plan.md §5E.
 * Not wired to any editor — runs on demand. Skipping a rule is safe.
 */
(function () {
  'use strict';

  // ============================================================ rules

  const RULES = {
    atomicity: 'Atomicity — one fact per card',
    frontProbe: "Front contains ?, ___, or {{c#::}}",
    coreAnswerLen: 'Core answer ≤25 words',
    clozeDetect: 'Cloze {{c#::}} syntax detection',
    hookPresent: 'Hook (mnem/analogy/exAnswer) present',
    siblingType: 'Sibling cards via conceptId need ≥1 application',
    leech: 'Leech: >5 lifetime misses or 2× consecutive Shaky',
  };

  // ============================================================ helpers

  function wordCount(s) {
    return String(s || '').replace(/<[^>]+>/g, ' ').trim().split(/\s+/).filter(Boolean).length;
  }

  function sentenceCount(s) {
    return String(s || '').replace(/<[^>]+>/g, ' ').split(/[.!?]\s/).filter(t => t.trim().length > 5).length;
  }

  function hasFrontProbe(term) {
    if (!term) return false;
    return /\?|___+|\{\{c\d+::/.test(String(term));
  }

  function hasCloze(s) {
    return /\{\{c\d+::[^}]+\}\}/.test(String(s || ''));
  }

  function hasHook(card) {
    return Boolean(
      (card.mnem && card.mnem.length) ||
      (card.analogy && card.analogy.length) ||
      (card.hook && card.hook.length) ||
      (card.exAnswer && card.exAnswer.length)
    );
  }

  function getAllCards() {
    const decks = window.FLASHCARD_DECKS || {};
    const out = [];
    Object.entries(decks).forEach(([deckId, arr]) => {
      if (deckId === 'all' || !Array.isArray(arr)) return;
      arr.forEach(c => out.push({ deckId, card: c }));
    });
    return out;
  }

  function loadProgress() {
    try { return JSON.parse(localStorage.getItem('leitner-progress-v1') || '{}'); }
    catch (e) { return {}; }
  }

  function cardKey(c) {
    return String(c?.term || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim().slice(0, 100);
  }

  // ============================================================ lintCard

  function lintCard(card) {
    const errors = [];
    const warnings = [];
    const info = [];

    if (!card || typeof card !== 'object') {
      errors.push({ rule: 'shape', msg: 'Card is not an object' });
      return { errors, warnings, info };
    }

    // Rule 1 — Atomicity
    // Only flag when the SHAPE of the card suggests splitting would help —
    // either the term covers a comparison ("X vs Y") with a long def, or the
    // def is extremely long (≥500 chars / ≥6 sentences) regardless of term.
    // Mastery cards with rich single-concept defs (300–500 chars) are NOT flagged.
    const defLen = (card.def || '').length;
    const sents = sentenceCount(card.def);
    const termHasMulti = /\s(and|vs|versus)\s/i.test(card.term || '') || /,/.test(card.term || '');
    if (defLen > 500 || sents > 6) {
      warnings.push({ rule: 'atomicity', msg: `def is very long (${defLen} chars, ~${sents} sentences); consider coreAnswer + deepDive split` });
    } else if (termHasMulti && (defLen > 280 || sents > 4)) {
      warnings.push({ rule: 'atomicity', msg: 'term covers a comparison and def is long — consider splitting into sibling cards via conceptId' });
    }

    // Rule 2 — Front probe
    if (!hasFrontProbe(card.term)) {
      warnings.push({ rule: 'frontProbe', msg: "front lacks '?', '___', or '{{c#::}}' — would benefit from a question form" });
    }

    // Rule 3 — Core answer ≤25 words
    const ca = card.coreAnswer || card.def || '';
    const wc = wordCount(ca);
    if (wc > 25) {
      warnings.push({ rule: 'coreAnswerLen', msg: `coreAnswer is ${wc} words (>25). Consider tighter coreAnswer with full text in deepDive` });
    }

    // Rule 4 — Cloze detection (info only)
    if (hasCloze(card.term) || hasCloze(card.def)) {
      info.push({ rule: 'clozeDetect', msg: 'cloze syntax detected — would render as cloze if cardType set' });
    }

    // Rule 5 — Hook present
    if (!hasHook(card)) {
      warnings.push({ rule: 'hookPresent', msg: 'no mnem/analogy/exAnswer/hook — adding one helps recall' });
    }

    // Rule 6 — sibling check is cross-card; reported in report() not per-card

    return { errors, warnings, info };
  }

  // ============================================================ siblings

  function siblingReport(cardsList) {
    const groups = {};
    cardsList.forEach(({ deckId, card }) => {
      const cid = card.conceptId;
      if (!cid) return;
      groups[cid] = groups[cid] || [];
      groups[cid].push({ deckId, card });
    });

    const lonely = [];
    const noApp = [];
    Object.entries(groups).forEach(([cid, group]) => {
      if (group.length === 1) {
        lonely.push({ conceptId: cid, only: group[0].card.term });
      } else {
        const types = group.map(g => g.card.cardType || 'definition');
        const hasApp = types.includes('application');
        if (!hasApp) {
          noApp.push({ conceptId: cid, terms: group.map(g => g.card.term), types });
        }
      }
    });

    return { lonely, noApp, totalGroups: Object.keys(groups).length };
  }

  // ============================================================ leeches

  function leeches() {
    const progress = loadProgress();
    const out = [];
    getAllCards().forEach(({ deckId, card }) => {
      const k = cardKey(card);
      const p = progress[k];
      if (!p) return;
      if ((p.missCount || 0) > 5) {
        out.push({ deckId, term: card.term, missCount: p.missCount, state: p.state });
      }
    });
    out.sort((a, b) => b.missCount - a.missCount);
    return out;
  }

  // ============================================================ report

  function report(opts) {
    opts = opts || {};
    const all = getAllCards().filter(({ deckId }) => !opts.deck || deckId === opts.deck);
    const tally = {
      atomicity: 0,
      frontProbe: 0,
      coreAnswerLen: 0,
      hookPresent: 0,
      clozeDetect: 0,
      cards: all.length,
    };

    const samples = {
      atomicity: [],
      frontProbe: [],
      coreAnswerLen: [],
      hookPresent: [],
    };

    all.forEach(({ deckId, card }) => {
      const r = lintCard(card);
      r.warnings.forEach(w => {
        tally[w.rule] = (tally[w.rule] || 0) + 1;
        if (samples[w.rule] && samples[w.rule].length < 3) {
          samples[w.rule].push(`[${deckId}] ${(card.term || '').slice(0, 60)}`);
        }
      });
      r.info.forEach(i => { tally[i.rule] = (tally[i.rule] || 0) + 1; });
    });

    const sib = siblingReport(all);
    const leechList = leeches();

    /* eslint-disable no-console */
    console.group('%c[card-linter] Report' + (opts.deck ? ' · ' + opts.deck : ''),
                  'color:#c89b2e;font-weight:600');
    console.log('Cards examined:', tally.cards);
    console.log('');
    console.group('%cWarnings by rule', 'color:#e8b94a;font-weight:600');
    Object.entries(RULES).forEach(([key, label]) => {
      if (key === 'siblingType' || key === 'leech') return;
      const n = tally[key] || 0;
      if (n === 0) {
        console.log('%c✓ %s%c — clean', 'color:#5fa871;font-weight:600', label, '');
      } else {
        console.log('%c⚠ %s%c — %d card(s)',
                    'color:#e8b94a;font-weight:600', label, '',
                    n);
        if (samples[key] && samples[key].length) {
          samples[key].forEach(s => console.log('   · ' + s));
        }
      }
    });
    console.groupEnd();
    console.log('');
    console.group('%cSibling check (rule 6)', 'color:#e8b94a;font-weight:600');
    console.log('conceptId groups:', sib.totalGroups);
    if (sib.lonely.length) {
      console.log(`⚠ ${sib.lonely.length} lonely conceptId(s) — only one card per group:`);
      sib.lonely.forEach(l => console.log('   ·', l.conceptId, '→', l.only));
    }
    if (sib.noApp.length) {
      console.log(`⚠ ${sib.noApp.length} group(s) without an "application" sibling card`);
      sib.noApp.forEach(g => console.log('   ·', g.conceptId, '→', g.terms.join(' / ')));
    } else if (sib.totalGroups > 0) {
      console.log('✓ all multi-card groups include at least one application');
    }
    console.groupEnd();
    console.log('');
    console.group('%cLeech check (rule 7)', 'color:#e8b94a;font-weight:600');
    if (!leechList.length) {
      console.log('✓ no cards with >5 lifetime misses');
    } else {
      console.log(`⚠ ${leechList.length} leech card(s):`);
      leechList.forEach(l => console.log('   ·', `[${l.deckId}]`, l.term, '— misses:', l.missCount));
    }
    console.groupEnd();
    console.groupEnd();
    /* eslint-enable no-console */

    return { tally, samples, siblings: sib, leeches: leechList };
  }

  // ============================================================ export

  window.cardLinter = {
    lintCard,
    report,
    leeches,
    siblingReport: () => siblingReport(getAllCards()),
    rules: RULES,
  };

  console.log('[card-linter] loaded — call cardLinter.report() in console for the full audit.');
})();
