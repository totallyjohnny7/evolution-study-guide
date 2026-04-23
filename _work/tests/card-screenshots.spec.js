// Screenshot verification + mnemonic/image spot checks for deployed flashcards.
// Runs against production pages.dev URL.
const { test, expect } = require('@playwright/test');
const path = require('path');
const fs = require('fs');

const BASE = process.env.ESG_BASE || 'https://evolution-study-guide.pages.dev';
const SHOT_DIR = path.resolve(__dirname, '..', 'screenshots');

function ensureDir(p) { fs.mkdirSync(p, { recursive: true }); }

test.setTimeout(180000);

// ------------ REVIEW PAGE ------------
test('review: chapter screenshots + flip + spot check', async ({ browser }) => {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  const failures = [];
  page.on('pageerror', e => failures.push('pageerror: ' + String(e)));

  await page.goto(BASE + '/exam3_review', { waitUntil: 'domcontentloaded' });
  // Enter card mode
  await page.evaluate(() => {
    document.body.classList.remove('study-mode','test-mode');
    document.body.classList.add('card-mode');
    const sect = document.getElementById('fc-section');
    if (sect) sect.classList.add('show');
    const filt = document.getElementById('fc-filter');
    if (filt) filt.style.display = 'flex';
  });
  await page.waitForTimeout(400);

  ensureDir(path.join(SHOT_DIR, 'review'));

  // Screenshot each chapter section
  const chapters = await page.$$eval('.fc-chapter', els => els.map(e => e.getAttribute('data-ch')));
  console.log('Review chapters:', chapters);
  for (const ch of chapters) {
    const el = await page.$(`.fc-chapter[data-ch="${ch}"]`);
    if (el) {
      await el.scrollIntoViewIfNeeded();
      await page.waitForTimeout(200);
      await el.screenshot({ path: path.join(SHOT_DIR, 'review', `chapter_${ch}_front.png`) });
    }
  }

  // Flip a sample of cards (first 4 visible) and screenshot the flipped state
  const cards = await page.$$('.fc2');
  const flipSample = cards.slice(0, 4);
  for (let i = 0; i < flipSample.length; i++) {
    await flipSample[i].scrollIntoViewIfNeeded();
    await flipSample[i].click();
  }
  await page.waitForTimeout(800);
  // Screenshot the first chapter again in flipped state
  const firstCh = await page.$('.fc-chapter');
  if (firstCh) {
    await firstCh.scrollIntoViewIfNeeded();
    await firstCh.screenshot({ path: path.join(SHOT_DIR, 'review', `chapter_flipped_sample.png`) });
  }

  // -------- Spot check: 10 random cards for mnemonic + image presence --------
  // Unflip first
  await page.evaluate(() => {
    document.querySelectorAll('.fc2.flipped').forEach(c => c.classList.remove('flipped'));
  });
  await page.waitForTimeout(200);

  const totalCards = cards.length;
  console.log('Review total cards:', totalCards);
  expect(totalCards).toBeGreaterThanOrEqual(152);

  // Random sample
  const sampleIdx = new Set();
  while (sampleIdx.size < Math.min(10, totalCards)) {
    sampleIdx.add(Math.floor(Math.random() * totalCards));
  }
  const mnemonicFails = [];
  const imageFails = [];
  const checkSample = Array.from(sampleIdx);
  for (const idx of checkSample) {
    const card = cards[idx];
    const info = await card.evaluate((el) => {
      const front = el.querySelector('.ff2');
      const back = el.querySelector('.fb2');
      const img = back ? back.querySelector('img') : null;
      const hasMn = back ? (
        (back.querySelector('.fc-mn') !== null) ||
        (back.textContent.includes('🧠')) ||
        (/remember\s*it/i.test(back.textContent)) ||
        (back.querySelector('.mn') !== null)
      ) : false;
      return {
        question: front ? (front.textContent || '').trim().slice(0, 80) : '',
        hasMn,
        imgSrc: img ? img.getAttribute('src') : null,
        cardId: el.getAttribute('data-id') || el.id || null
      };
    });
    const cid = info.cardId || `review_card_${idx}`;
    if (!info.hasMn) {
      mnemonicFails.push({ cid, q: info.question, reason: 'no mnemonic/remember-it indicator' });
    }
    const src = info.imgSrc || '';
    const goodSrc = src.startsWith('/img/fc/') || src.startsWith('/exam3/figures/') || src.startsWith('img/fc/') || src.startsWith('exam3/figures/');
    if (!src || !goodSrc) {
      imageFails.push({ cid, q: info.question, reason: src ? `bad src: ${src}` : 'no img in .fb2' });
    }
  }

  fs.writeFileSync(path.join(SHOT_DIR, 'review', '_spotcheck.json'), JSON.stringify({
    totalCards, sampledIdx: checkSample, mnemonicFails, imageFails, pageerrors: failures
  }, null, 2));

  console.log('Review spot-check: mnemonic fails=' + mnemonicFails.length + '/' + checkSample.length + ', image fails=' + imageFails.length + '/' + checkSample.length);

  await ctx.close();
});

// ------------ LECTURE PAGE ------------
test('lecture: section screenshots + flip + spot check', async ({ browser }) => {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  const failures = [];
  page.on('pageerror', e => failures.push('pageerror: ' + String(e)));

  await page.goto(BASE + '/exam3_lecture', { waitUntil: 'domcontentloaded' });
  // Enter card mode
  await page.evaluate(() => {
    try { if (typeof setLMode === 'function') setLMode('card'); } catch(e){}
    document.body.classList.add('card-mode');
  });
  await page.waitForTimeout(900);

  ensureDir(path.join(SHOT_DIR, 'lecture'));

  // Take per-section screenshots by filtering
  const sections = ['s1','s2','s3','s4','s5','s6','s7'];
  for (const s of sections) {
    // Click the filter button for this section
    const filtered = await page.evaluate((sec) => {
      try {
        if (typeof filterLCards === 'function') {
          // Find a button whose onclick uses this sec
          const btn = Array.from(document.querySelectorAll('#fc-filter .flt-btn')).find(b => (b.getAttribute('onclick')||'').includes(`'${sec}'`));
          if (btn) { btn.click(); return true; }
        }
        return false;
      } catch(e) { return false; }
    }, s);
    await page.waitForTimeout(350);
    const grid = await page.$('#fc-grid, .fc-grid');
    if (grid) {
      await grid.scrollIntoViewIfNeeded();
      await page.waitForTimeout(150);
      await grid.screenshot({ path: path.join(SHOT_DIR, 'lecture', `section_${s}.png`) });
    } else {
      // Fallback: full page
      await page.screenshot({ path: path.join(SHOT_DIR, 'lecture', `section_${s}_full.png`), fullPage: false });
    }
  }

  // Restore "All" filter
  await page.evaluate(() => {
    const allBtn = Array.from(document.querySelectorAll('#fc-filter .flt-btn')).find(b => (b.getAttribute('onclick')||'').includes(`'all'`));
    if (allBtn) allBtn.click();
  });
  await page.waitForTimeout(400);

  // Flip sample
  const cards = await page.$$('.fc2');
  const sample = cards.slice(0, 4);
  for (let i = 0; i < sample.length; i++) {
    await sample[i].scrollIntoViewIfNeeded();
    await sample[i].click();
  }
  await page.waitForTimeout(700);
  if (cards[0]) {
    await cards[0].scrollIntoViewIfNeeded();
    // screenshot the grid with flipped cards
    const grid = await page.$('#fc-grid, .fc-grid');
    if (grid) await grid.screenshot({ path: path.join(SHOT_DIR, 'lecture', 'flipped_sample.png') });
  }

  // Unflip
  await page.evaluate(() => {
    document.querySelectorAll('.fc2.flipped').forEach(c => c.classList.remove('flipped'));
  });

  const totalCards = cards.length;
  console.log('Lecture total cards:', totalCards);
  // Spot check 10
  const sampleIdx = new Set();
  while (sampleIdx.size < Math.min(10, totalCards)) {
    sampleIdx.add(Math.floor(Math.random() * totalCards));
  }
  const mnemonicFails = [];
  const imageFails = [];
  const checkSample = Array.from(sampleIdx);
  for (const idx of checkSample) {
    const card = cards[idx];
    const info = await card.evaluate((el) => {
      const front = el.querySelector('.ff2');
      const back = el.querySelector('.fb2');
      const img = back ? back.querySelector('img') : null;
      const hasMn = back ? (
        (back.querySelector('.fc-mn') !== null) ||
        (back.textContent.includes('🧠')) ||
        (/remember\s*it/i.test(back.textContent)) ||
        (back.querySelector('.mn') !== null)
      ) : false;
      return {
        question: front ? (front.textContent || '').trim().slice(0, 80) : '',
        hasMn,
        imgSrc: img ? img.getAttribute('src') : null,
        cardId: el.getAttribute('data-id') || el.id || null
      };
    });
    const cid = info.cardId || `lecture_card_${idx}`;
    if (!info.hasMn) {
      mnemonicFails.push({ cid, q: info.question, reason: 'no mnemonic/remember-it indicator' });
    }
    const src = info.imgSrc || '';
    const goodSrc = src.startsWith('/img/fc/') || src.startsWith('/exam3/figures/') || src.startsWith('img/fc/') || src.startsWith('exam3/figures/');
    if (!src || !goodSrc) {
      imageFails.push({ cid, q: info.question, reason: src ? `bad src: ${src}` : 'no img in .fb2' });
    }
  }

  fs.writeFileSync(path.join(SHOT_DIR, 'lecture', '_spotcheck.json'), JSON.stringify({
    totalCards, sampledIdx: checkSample, mnemonicFails, imageFails, pageerrors: failures
  }, null, 2));

  console.log('Lecture spot-check: mnemonic fails=' + mnemonicFails.length + '/' + checkSample.length + ', image fails=' + imageFails.length + '/' + checkSample.length);

  await ctx.close();
});
