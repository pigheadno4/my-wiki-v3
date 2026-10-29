# Atome Web Component worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Atome Web Component guide add to an existing integration, and which server-side flows does it cover?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-web-component.md` → `raw/adyen/docs/payment-methods/atome/web-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/atome/web-component`; full pinned raw `raw/adyen/docs/payment-methods/atome/web-component/2026-09-15.md`, `# Atome Web Component` lines 15–23, `## Sessions flow Component`/requirements lines 25–36 and `## Advanced flow Component`/requirements lines 854–862. It is method-specific guidance, and this snapshot does not prove merchant enablement or a completed payment.

## Q2 — Central requirements, lifecycle and warnings

**Query:** For Atome Web Components, which request data and country/currency pairs are specified, how are shopper fields displayed, and what do the redirect response and test/live steps mean?

**Expected route:** Same root → Adyen index → online-payments concept → Atome Web Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Add additional parameters to your /sessions request` lines 40–52, `## Add additional configuration for Atome` lines 746–804, `## Add additional parameters to your /payments request` lines 894–907, response lines 1624–1635, partial refunds lines 1638–1646, and `## Test and go live` lines 1648–1666. Preserve required fields versus conditionally optional delivery address, MY/MYR and SG/SGD, hidden Component delivery/company fields versus server payload, and redirect-action versus final payment. The Sessions curl has duplicate `countryCode`, a custom-scheme Web return URL, and missing shell continuation before `-d`; the Advanced curl shares the continuation issue (lines 58–78, 913–919). The Sessions visibility example omits a closing brace (lines 794–806). Testing needs separate Atome sandbox accounts by country/region and live setup needs Support.
