# Zip iOS Drop-in worker retrieval queries

## Q1 — Purpose, flow and version scope

**Query:** What does the Zip iOS Drop-in page add to an existing integration, and which endpoint and SDK-version routes does it distinguish?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-ios-drop-in.md` → `raw/adyen/docs/payment-methods/zip/ios-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/zip/ios-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/zip/ios-drop-in/2026-09-15.md`, `# Zip Drop-in integration` lines 15–26, `### Tab: /sessions` lines 32–44, `### Tab: /payments` lines 681–694, and `## Drop-in configuration` lines 1391–1399. Sessions is called default for Drop-in v5.0.0+, while Payments is an additional use case. Neither the examples nor test setup proves current live eligibility or payment success.

## Q2 — Request data, redirect and recurring qualifications

**Query:** What does the Zip iOS guide say about shopper/order data, pickup, redirect action, token creation and live setup?

**Expected route:** Same root → Adyen index → online-payments concept → Zip iOS Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: Sessions field table lines 36–44, Payments table lines 685–694, `/payments` redirect action lines 1375–1389, `## Recurring payments` lines 1401–1434, and `## Test and go live` lines 1634–1640. Preserve blank Required cells, conditional click-and-collect, optional imageURL limit, AU/AUD example scope, and `RedirectShopper` as an intermediate action. Token webhook follows settlement and future payments require stored ID, same shopper reference and recurring parameters. The Payments curl has literal hint markup in JSON (lines 698–722); the recurring Java example omits shopperReference and uses an older-looking token field relative to the prose (lines 1459–1487). Live use requires a request in live Customer Area.
