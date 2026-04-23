// Playwright config for local-only Dexie verification
const { defineConfig, devices } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './_work/tests',
  timeout: 60000,
  fullyParallel: false,
  workers: 1,
  reporter: 'list',
  use: {
    baseURL: 'http://127.0.0.1:8788',
    headless: true,
    trace: 'off'
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } }
  ]
});
