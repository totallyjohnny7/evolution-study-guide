# Phase 1 Migration Plan — Dexie + Anki-style Binary Pass/Fail Scheduler

## Case: A (greenfield)
No legacy review-state data anywhere. No localStorage keys to drain. One shared Dexie DB across `/exam3_review` and `/exam3_lecture`.

## Unified Dexie schema — DB name `evolution_study_guide`
```js
db.version(1).stores({
  cards:   'id, due, queue, source, lastReview, [queue+due], [source+queue+due]',
  reviews: '++id, cardId, ts, route',
  meta:    'key'
});
```

## Card document
```js
{
  id: 'review_ch3_0' | 'lecture_s1_0' | ...,   // stable across reloads
  source: 'review' | 'lecture',
  term: string,
  def:  string,                 // review cards allow inline HTML
  chip: string,                 // section/chapter label
  queue: 'new' | 'learning' | 'review' | 'relearning' | 'suspended',
  due: number,                  // epoch ms
  lastReview: number | null,
  stability: number,
  difficulty: number,           // 1..10
  reps: number,
  lapses: number,
  learningStep: number,
  isLeech: boolean,
  introducedAt: number
}
```

## New-card initialization
`queue='new', stability=0, difficulty=5, reps=0, lapses=0, learningStep=0, isLeech=false, introducedAt=now, due=now, lastReview=null`

## Review log row
```js
{ cardId, ts, rating: 'pass'|'fail', timeSpent, queueAtReview, route }
```

## Settings doc (meta key='settings')
```js
{
  learningSteps: [60, 600],         // seconds
  relearningSteps: [600],
  minIntervalDays: 1,
  leechThreshold: 8,
  leechAction: 'suspend',           // or 'tag'
  maxAnswerSeconds: 60,
  newCardOrder: 'sequential'        // or 'random'
}
```

## Card ID derivation (deterministic)
- Review: `review_<data-ch>_<running index within that chapter in DOM order>`
- Lecture: `lecture_<c.sec>_<running index within that section in FLASH array order>`

## State machine — binary Pass/Fail
Time constants in seconds → multiply by 1000 for due (ms).

- new + Pass → queue='learning', learningStep=0, due=now+learningSteps[0]*1000
- learning[N] + Pass:
  - if N+1 < learningSteps.length → learningStep=N+1, due=now+learningSteps[N+1]*1000
  - else → queue='review', reps++, stability=max(1, stability*2 || 1), due=now+stability*86400*1000
- learning + Fail → learningStep=0, due=now+learningSteps[0]*1000
- review + Pass → stability=stability*(2.5 - difficulty*0.1), reps++, due=now+stability*86400*1000
- review + Fail → lapses++, queue='relearning', learningStep=0, difficulty=min(10, difficulty+1), due=now+relearningSteps[0]*1000
  - if lapses>=leechThreshold:
    - leechAction='suspend' → queue='suspended'
    - else → isLeech=true
- relearning[N] + Pass:
  - if N+1 < relearningSteps.length → learningStep=N+1, due=now+relearningSteps[N+1]*1000
  - else → queue='review', stability=max(1, stability*1.5), due=now+max(stability*86400, minIntervalDays*86400)*1000
- relearning + Fail → learningStep=0, due=now+relearningSteps[0]*1000
- suspended → applyRating is a no-op; getDueQueue filters these out

## Rating encoding
Preserved as string `'pass'` / `'fail'`. UI label remains "Miss" but stored rating is `'fail'`.

## Source tagging
Case A: `source='review'` for cards from /exam3_review, `source='lecture'` for /exam3_lecture. No shared cards.

## Settings defaults
`learningSteps:[60,600], relearningSteps:[600], minIntervalDays:1, leechThreshold:8, leechAction:'suspend', maxAnswerSeconds:60, newCardOrder:'sequential'`

## BroadcastChannel
Channel name `evolution_study_guide_sync`; messages `{type:'card-updated', cardId}` and `{type:'settings-updated'}`.

## Migration flow
`migrateIfNeeded()` uses `navigator.locks` (when available) to ensure exactly-once seed. Case A action: if `meta.migrated_v1` absent, write default settings + set `migrated_v1=true`. No legacy drain needed.

## Files to be touched
- CREATE `public/js/esg-db.js` (shared module)
- EDIT `public/exam3_review.html` — add 2 script tags in `<head>`, mark `_cardShownAt` in `dkRender`, wrap Pass/Miss handlers with ESG calls, add Settings gear button + modal, build-time card ID assignment
- EDIT `public/exam3_lecture.html` — same pattern as above
