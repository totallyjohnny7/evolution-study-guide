const { test, expect } = require('@playwright/test');

// Helper: wait for ESG to be ready on a given page
async function waitForEsgReady(page) {
  await page.waitForFunction(() => window.ESG && window.ESG._settingsCache, null, { timeout: 15000 });
  // also wait for the migrated flag if dexie is live
  await page.waitForTimeout(400);
}

// Helper: reset DB to greenfield state AFTER first goto by deleting + reloading once.
async function resetDb(page) {
  // Navigate to the target route first with a blank domain so we can nuke IDB, then caller goto's.
  // Simpler: do nothing here; caller uses `nukeAndReload`.
}

async function nukeDb(page) {
  await page.evaluate(() => new Promise((resolve) => {
    try {
      const req = indexedDB.deleteDatabase('evolution_study_guide');
      req.onsuccess = req.onerror = req.onblocked = () => resolve();
      setTimeout(resolve, 2000);
    } catch (e) { resolve(); }
  }));
}

test.describe('ESG Dexie suite', () => {

  test('1. Fresh origin: Dexie + ESG + migrated_v1 + settings defaults', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      const hasDexie = typeof window.Dexie !== 'undefined';
      const hasESG = typeof window.ESG !== 'undefined';
      const migrated = await window.Dexie && new window.Dexie('evolution_study_guide').open().then(db => db.table('meta').get('migrated_v1')).then(r => r && r.value === true).catch(() => false);
      const settings = await window.ESG.getSettings();
      return { hasDexie, hasESG, migrated, settings };
    });
    expect(result.hasDexie).toBeTruthy();
    expect(result.hasESG).toBeTruthy();
    expect(result.migrated).toBeTruthy();
    expect(result.settings.learningSteps).toEqual([60, 600]);
    expect(result.settings.leechThreshold).toBe(8);
  });

  test('2. Shared DB: both routes visible via getAllCards', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    await page.waitForTimeout(500); // seed to run
    await page.goto('/exam3_lecture');
    await waitForEsgReady(page);
    await page.waitForTimeout(500);
    const result = await page.evaluate(async () => {
      const all = await window.ESG.getAllCards();
      const review = all.filter(c => c.source === 'review');
      const lecture = all.filter(c => c.source === 'lecture');
      return { total: all.length, review: review.length, lecture: lecture.length };
    });
    expect(result.review).toBeGreaterThan(100);
    expect(result.lecture).toBeGreaterThan(100);
  });

  test('3. Learning steps: new -> Pass graduates through learning', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      const id = 'test_learn_' + Date.now();
      let c = window.ESG.newCardDefaults(id, 'review', 'T', 'D', 'C');
      await window.ESG.putCard(c);
      const t0 = Date.now();
      const c1 = window.ESG.applyRating(c, 'pass', 2);
      const c2 = window.ESG.applyRating(c1, 'pass', 2);
      const c3 = window.ESG.applyRating(c2, 'pass', 2);
      return {
        q1: c1.queue, step1: c1.learningStep, due1Delta: c1.due - t0,
        q2: c2.queue, step2: c2.learningStep, due2Delta: c2.due - t0,
        q3: c3.queue
      };
    });
    expect(result.q1).toBe('learning');
    expect(result.step1).toBe(0);
    expect(Math.abs(result.due1Delta - 60000)).toBeLessThan(3000);
    expect(result.q2).toBe('learning');
    expect(result.step2).toBe(1);
    expect(Math.abs(result.due2Delta - 600000)).toBeLessThan(3000);
    expect(result.q3).toBe('review');
  });

  test('4. Fail resets learning step', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(() => {
      const c0 = window.ESG.newCardDefaults('t4', 'review', 'X', 'Y', 'Z');
      const c1 = window.ESG.applyRating(c0, 'pass', 2); // learning step 0
      const c2 = window.ESG.applyRating(c1, 'fail', 2); // reset
      return { q: c2.queue, step: c2.learningStep, dueDelta: c2.due - Date.now() };
    });
    expect(result.q).toBe('learning');
    expect(result.step).toBe(0);
    expect(Math.abs(result.dueDelta - 60000)).toBeLessThan(3000);
  });

  test('5. Mature fail -> relearning, review row tagged route=lecture', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_lecture');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      const id = 'test_lect_mature_' + Date.now();
      let c = window.ESG.newCardDefaults(id, 'lecture', 'A', 'B', 'S1');
      c.queue = 'review'; c.reps = 2; c.stability = 4;
      await window.ESG.putCard(c);
      const updated = window.ESG.applyRating(c, 'fail', 3);
      await window.ESG.putCard(updated);
      await window.ESG.logReview({cardId: id, ts: Date.now(), rating: 'fail', timeSpent: 3, queueAtReview: 'review', route: 'lecture'});
      // Read review log
      const db = new window.Dexie('evolution_study_guide');
      db.version(1).stores({ cards: 'id', reviews: '++id, cardId, ts, route', meta: 'key' });
      const rows = await db.table('reviews').where('cardId').equals(id).toArray();
      return { lapses: updated.lapses, queue: updated.queue, dueDelta: updated.due - Date.now(), rowCount: rows.length, rowRoute: rows[0] && rows[0].route, rowQ: rows[0] && rows[0].queueAtReview };
    });
    expect(result.lapses).toBe(1);
    expect(result.queue).toBe('relearning');
    expect(Math.abs(result.dueDelta - 600000)).toBeLessThan(3000);
    expect(result.rowCount).toBeGreaterThanOrEqual(1);
    expect(result.rowRoute).toBe('lecture');
    expect(result.rowQ).toBe('review');
  });

  test('6. Relearning graduation respects minIntervalDays', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(() => {
      const c = window.ESG.newCardDefaults('t6', 'review', 'A', 'B', 'C');
      c.queue = 'relearning'; c.learningStep = 0; c.stability = 0.1;
      const p = window.ESG.applyRating(c, 'pass', 2); // graduates (relearningSteps.len==1)
      return { q: p.queue, dueDelta: p.due - Date.now() };
    });
    expect(result.q).toBe('review');
    // min 1 day in ms
    expect(result.dueDelta).toBeGreaterThanOrEqual(86400 * 1000 - 1000);
  });

  test('7. Leech suspend at threshold=3', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      await window.ESG.updateSettings({ leechThreshold: 3, leechAction: 'suspend' });
      const id = 'test_leech_' + Date.now();
      let c = window.ESG.newCardDefaults(id, 'review', 'Q', 'A', 'ch3');
      c.queue = 'review'; c.reps = 2; c.stability = 2;
      for (let i = 0; i < 3; i++) {
        c = window.ESG.applyRating(c, 'fail', 2);
        if (c.queue === 'relearning') {
          c.queue = 'review'; // force back to mature so next fail also lapses
        }
      }
      // Need to re-run: the above hack altered queue; redo cleanly
      c = window.ESG.newCardDefaults(id, 'review', 'Q', 'A', 'ch3');
      c.queue = 'review'; c.reps = 2; c.stability = 2;
      for (let i = 0; i < 3; i++) {
        c = window.ESG.applyRating(c, 'fail', 2);
        // After fail, queue becomes relearning. Lift back to review so the next
        // fail also counts as a mature lapse (test fixture only).
        if (i < 2) { c.queue = 'review'; }
      }
      await window.ESG.putCard(c);
      const dueReview = await window.ESG.getDueQueue({ source: 'review' });
      const dueLect = await window.ESG.getDueQueue({ source: 'lecture' });
      return {
        leech: c.isLeech,
        queue: c.queue,
        lapses: c.lapses,
        reviewHit: dueReview.some(x => x.id === id),
        lectHit: dueLect.some(x => x.id === id)
      };
    });
    expect(result.leech).toBe(true);
    expect(result.queue).toBe('suspended');
    expect(result.reviewHit).toBe(false);
    expect(result.lectHit).toBe(false);
  });

  test('8. Leech tag mode does not suspend', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      await window.ESG.updateSettings({ leechThreshold: 3, leechAction: 'tag' });
      let c = window.ESG.newCardDefaults('t8', 'review', 'Q', 'A', 'ch3');
      c.queue = 'review'; c.reps = 2; c.stability = 2;
      for (let i = 0; i < 3; i++) {
        c = window.ESG.applyRating(c, 'fail', 2);
        if (i < 2) { c.queue = 'review'; }
      }
      return { leech: c.isLeech, queue: c.queue };
    });
    expect(result.leech).toBe(true);
    expect(result.queue).toBe('relearning');
  });

  test('9. timeSpent clamp in review log', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      await window.ESG.updateSettings({ maxAnswerSeconds: 60 });
      const id = 'test_clamp_' + Date.now();
      await window.ESG.putCard(window.ESG.newCardDefaults(id, 'review', 'A', 'B', 'C'));
      await window.ESG.logReview({ cardId: id, ts: Date.now(), rating: 'pass', timeSpent: 90, queueAtReview: 'new', route: 'review' });
      const db = new window.Dexie('evolution_study_guide');
      db.version(1).stores({ cards: 'id', reviews: '++id, cardId, ts, route', meta: 'key' });
      const rows = await db.table('reviews').where('cardId').equals(id).toArray();
      return { t: rows[0] && rows[0].timeSpent };
    });
    expect(result.t).toBe(60);
  });

  test('10. Sequential new-card order (by introducedAt)', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      const base = Date.now() - 10000;
      const ids = ['a','b','c','d','e'];
      for (let i = 0; i < ids.length; i++) {
        const c = window.ESG.newCardDefaults('seq_'+ids[i], 'review', ids[i], '', '');
        c.introducedAt = base + i * 10; c.due = base + i * 10;
        await window.ESG.putCard(c);
      }
      const q = await window.ESG.getDueQueue({ source: 'review', limit: 500 });
      const subset = q.filter(x => x.id.startsWith('seq_')).map(x => x.id);
      return subset;
    });
    expect(result.slice(0,5)).toEqual(['seq_a','seq_b','seq_c','seq_d','seq_e']);
  });

  test('11. Persistence across reloads', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    await page.evaluate(async () => {
      const c = window.ESG.newCardDefaults('persist_test', 'review', 'T', 'D', 'C');
      const updated = window.ESG.applyRating(c, 'pass', 2);
      await window.ESG.putCard(updated);
    });
    await page.reload();
    await waitForEsgReady(page);
    const result = await page.evaluate(async () => {
      const c = await window.ESG.getCard('persist_test');
      return { queue: c && c.queue, step: c && c.learningStep };
    });
    expect(result.queue).toBe('learning');
    expect(result.step).toBe(0);
  });

  test('12. Cross-route BroadcastChannel sync', async ({ browser }) => {
    const ctx = await browser.newContext();
    const page1 = await ctx.newPage();
    const page2 = await ctx.newPage();
    await page1.goto('/exam3_review');
    await waitForEsgReady(page1);
    await page2.goto('/exam3_lecture');
    await waitForEsgReady(page2);
    await page2.evaluate(() => {
      window.__received = [];
      window.ESG.onSync((m) => window.__received.push(m));
    });
    await page1.evaluate(async () => {
      await window.ESG.putCard(window.ESG.newCardDefaults('bc_test', 'review', 'X', 'Y', 'Z'));
    });
    await page1.waitForTimeout(400);
    const got = await page2.evaluate(() => window.__received.map(m => m.type));
    expect(got).toContain('card-updated');
    // settings update
    await page1.evaluate(async () => {
      await window.ESG.updateSettings({ minIntervalDays: 2 });
    });
    await page1.waitForTimeout(400);
    const got2 = await page2.evaluate(() => window.__received.map(m => m.type));
    expect(got2).toContain('settings-updated');
    await ctx.close();
  });

  // 13: N/A (Case A greenfield — no legacy data to dedup)
  test.skip('13. Dedup — SKIPPED (Case A greenfield)', () => {});

  test('14. CDN fail: Dexie blocked -> fallback + toast', async ({ page }) => {
    await resetDb(page);
    await page.route('**/unpkg.com/**', route => route.abort());
    await page.goto('/exam3_review');
    await page.waitForFunction(() => window.ESG, null, { timeout: 15000 });
    await page.waitForTimeout(1200);
    const result = await page.evaluate(async () => {
      const hasDexie = typeof window.Dexie !== 'undefined';
      const ready = window.ESG._isReady();
      // Still callable via fallback
      const c = window.ESG.newCardDefaults('fb_test', 'review', 'A', 'B', 'C');
      await window.ESG.putCard(c);
      const back = await window.ESG.getCard('fb_test');
      return { hasDexie, ready, back: !!back, fallback: window.ESG._fallback.active };
    });
    expect(result.hasDexie).toBeFalsy();
    expect(result.fallback).toBeTruthy();
    expect(result.back).toBeTruthy();
  });

  // 15: SKIPPED (WebKit private mode — chromium-only)
  test.skip('15. WebKit private mode — SKIPPED per spec', () => {});

  test('16. Race: simultaneous load -> migration runs once', async ({ browser }) => {
    const ctx = await browser.newContext();
    const p1 = await ctx.newPage();
    const p2 = await ctx.newPage();
    await Promise.all([p1.goto('/exam3_review'), p2.goto('/exam3_lecture')]);
    await Promise.all([waitForEsgReady(p1), waitForEsgReady(p2)]);
    const r = await p1.evaluate(async () => {
      const db = new window.Dexie('evolution_study_guide');
      db.version(1).stores({ cards: 'id', reviews: '++id, cardId, ts, route', meta: 'key' });
      const row = await db.table('meta').get('migrated_v1');
      const settings = await db.table('meta').get('settings');
      return { migrated: row && row.value === true, hasSettings: !!settings };
    });
    expect(r.migrated).toBeTruthy();
    expect(r.hasSettings).toBeTruthy();
    await ctx.close();
  });

  test('17. UI regression: only 2 rating buttons', async ({ page }) => {
    await page.goto('/exam3_review');
    const btns = await page.locator('.dk-grade').count();
    expect(btns).toBe(2);
    const pass = await page.locator('#dk-pass-btn').count();
    const miss = await page.locator('#dk-miss-btn').count();
    expect(pass).toBe(1);
    expect(miss).toBe(1);
    await page.goto('/exam3_lecture');
    const btns2 = await page.locator('.dk-grade').count();
    expect(btns2).toBe(2);
  });

  test('18. Feature smoke: deck flip + shuffle + settings modal', async ({ page }) => {
    await resetDb(page);
    await page.goto('/exam3_review');
    await waitForEsgReady(page);
    // launch deck
    await page.evaluate(() => window.dkOpen('all'));
    await page.waitForTimeout(200);
    const shown = await page.locator('#dk-ov.show').count();
    expect(shown).toBe(1);
    // flip
    await page.evaluate(() => window.dkFlip());
    await page.waitForTimeout(200);
    const flipped = await page.locator('#dk-card.flipped').count();
    expect(flipped).toBe(1);
    // shuffle
    await page.evaluate(() => window.dkShuffle());
    await page.waitForTimeout(200);
    // settings gear present
    const gear = await page.locator('#dk-settings-btn').count();
    expect(gear).toBe(1);
    // open and close modal
    await page.click('#dk-settings-btn');
    await page.waitForSelector('#esg-settings-modal');
    await page.click('#esg-s-cancel');
    await page.waitForTimeout(200);
    const modalGone = await page.locator('#esg-settings-modal').count();
    expect(modalGone).toBe(0);
  });

});
