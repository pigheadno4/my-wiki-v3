# Atome Android Drop-in worker retrieval queries

## Q1 — Purpose and flow scope

**Query:** What does the Atome Android Drop-in page add, and what Sessions versus Advanced prerequisites does it state?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-android-drop-in.md` → `raw/adyen/docs/payment-methods/atome/android-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/atome/android-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/atome/android-drop-in/2026-09-15.md`, `# Atome Android Drop-in` lines 15–23, `## Sessions flow Drop-in` requirements lines 25–34, `## Advanced flow Drop-in` requirements lines 768–776, and no-extra-configuration statements lines 730–734 and 778–782. It is an add-on to existing integrations, not proof of a configured merchant or successful payment.

## Q2 — Request, redirect and operational gates

**Query:** Which Atome request fields and MY/SG currency pairs does the Android guide specify, and how should its redirect response, refunds and test/live instructions be interpreted?

**Expected route:** Same root → Adyen index → online-payments concept → Atome Android Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Add additional parameters to your /sessions request` lines 38–50, `## Add additional parameters to your /payments request` lines 786–799, redirect response lines 1516–1528, partial-refund instructions lines 1530–1538, and `## Test and go live` lines 1540–1558. Preserve required versus conditionally optional delivery address, MY/MYR and SG/SGD, and `RedirectShopper` as an action rather than final success. The curl examples lack the `-X POST` shell continuation (lines 54–60, 803–809), Sessions duplicates `countryCode` (lines 68–76), and the Android Advanced example uses a web `returnUrl` while Sessions uses an app scheme (lines 64–67, 817–824). Test accounts are per country/region and live setup requires Support.
