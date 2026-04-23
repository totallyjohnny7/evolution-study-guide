// Read-only production verification. Uses throwaway contexts — nothing real persisted.
const { test, expect } = require('@playwright/test');

const URLS = [
  'https://evolution-study-guide.pages.dev/exam3_review',
  'https://evolution-study-guide.pages.dev/exam3_lecture'
];

for (const url of URLS) {
  test('prod verify ' + url, async ({ browser }) => {
    const ctx = await browser.newContext();
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    page.on('console', msg => { if (msg.type() === 'error') errors.push('console.error: ' + msg.text()); });
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded' });
    expect(resp.status()).toBe(200);
    await page.waitForFunction(() => window.ESG && window.ESG._settingsCache, null, { timeout: 20000 });
    await page.waitForTimeout(1200); // allow dexie to migrate
    const r = await page.evaluate(async () => {
      const hasDexie = typeof window.Dexie !== 'undefined';
      const hasESG = typeof window.ESG !== 'undefined';
      let migrated = false;
      try {
        const db = new window.Dexie('evolution_study_guide');
        db.version(1).stores({ cards: 'id', reviews: '++id, cardId, ts, route', meta: 'key' });
        const row = await db.table('meta').get('migrated_v1');
        migrated = !!(row && row.value === true);
      } catch (e) {}
      // Single throwaway apply (transient, context closes)
      const c = window.ESG.newCardDefaults('prod_verify_throwaway', window.location.pathname.includes('lecture') ? 'lecture' : 'review', 'X', 'Y', 'Z');
      const u = window.ESG.applyRating(c, 'pass', 2);
      return { hasDexie, hasESG, migrated, queue: u.queue };
    });
    expect(r.hasDexie).toBeTruthy();
    expect(r.hasESG).toBeTruthy();
    expect(r.migrated).toBeTruthy();
    expect(r.queue).toBe('learning');
    expect(errors).toEqual([]);
    await ctx.close();
  });
}
