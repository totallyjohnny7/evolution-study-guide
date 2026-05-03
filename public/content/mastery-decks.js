/* Mastery deck loader — fetches JSON files from /data/mastery/ and exposes
   window.MASTERY_DECKS = { deckId: { deckId, label, description, cards:[{term,definition,sourceTag}] } }
   plus window.MASTERY_DECK_ORDER for stable iteration. */
(function () {
  const DECK_FILES = [
    'mechanisms',
    'scenarios',
    'game-theory',
    'compare-contrast',
    'calculations',
    'empirical',
    'phylogeny',
    'cause-effect',
    'cloze',
  ];

  window.MASTERY_DECKS = window.MASTERY_DECKS || {};
  window.MASTERY_DECK_ORDER = DECK_FILES.slice();
  window.MASTERY_READY = new Promise(function (resolve) {
    Promise.all(
      DECK_FILES.map(function (id) {
        return fetch('data/mastery/' + id + '.json')
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (deck) {
            if (deck && deck.deckId) {
              window.MASTERY_DECKS[deck.deckId] = deck;
            } else {
              console.warn('[mastery] failed to load deck', id);
            }
          })
          .catch(function (err) { console.warn('[mastery] error loading', id, err); });
      })
    ).then(function () {
      const total = Object.values(window.MASTERY_DECKS)
        .reduce(function (s, d) { return s + (d.cards ? d.cards.length : 0); }, 0);
      console.log('[mastery] loaded', Object.keys(window.MASTERY_DECKS).length, 'decks /', total, 'cards');
      resolve(window.MASTERY_DECKS);
    });
  });
})();
