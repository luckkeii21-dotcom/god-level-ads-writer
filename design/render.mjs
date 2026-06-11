import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const file = process.argv[2] || 'slide-01.html';
const out = process.argv[3] || file.replace(/\.html$/, '.png');

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--force-color-profile=srgb', '--font-render-hinting=none'],
});
const page = await browser.newPage({
  viewport: { width: 1080, height: 1350 },
  deviceScaleFactor: 2,
});
await page.goto('file://' + path.join(__dirname, file));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const el = await page.$('.canvas');
await el.screenshot({ path: path.join(__dirname, out) });
await browser.close();
console.log('rendered', out);
