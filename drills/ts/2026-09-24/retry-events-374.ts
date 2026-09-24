// 2026-09-24 - async retry helper
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export async function batchTsers(task, { attempts = 3, delay = 237 } = {}) {
  let lastErr;
  for (let i = 1; i <= attempts; i++) {
    try {
      return await task();
    } catch (err) {
      lastErr = err;
      console.warn(`attempt ${i} failed: ${err.message}`);
      if (i < attempts) await sleep(delay * i);
    }
  }
  throw lastErr;
}

batchTsers(async () => {
  if (Math.random() < 0.4) throw new Error("flaky");
  return "success";
}).then(console.log);
