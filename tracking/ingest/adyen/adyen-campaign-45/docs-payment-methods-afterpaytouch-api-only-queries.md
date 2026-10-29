# Afterpay API-only retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-afterpaytouch-api-only`
**Full pinned raw:** `raw/adyen/docs/payment-methods/afterpaytouch/api-only/2026-09-15.md`
**Verified locators:** `# Afterpay for API only`, lines 15–21; `## Requirements`, lines 23–30; `## How it works`, lines 32–38; `## Get Afterpay as an available payment method`, lines 52–91.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-api-only.md` → pinned raw.
**Answer boundary:** This is a method add-on for an existing API-only redirect integration. Captured discovery pairs, TEST examples and sandbox country choices do not prove current merchant availability, shopper approval or successful live payment.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** required shopper/line-item fields lines 40–48 and 93–107; discovery pairs 52–60; redirect sample 822–836; capture/refund 838–868; tokenization 906–1130; live request 1151.
**Answer boundary:** Merchant builds the form, supplies risk-check data, uses `afterpaytouch`, handles redirect and captures. Discovery pairs are AU/AUD, NZ/NZD and CA/CAD; recurring/on-file tokenization is limited to AU/NZ, with shopper approval and a token webhook. The illustrated later on-file request uses `shopperInteraction: ContAuth` and `recurringProcessingModel: CardOnFile` (raw lines 1042–1108) and skips repeat redirect after prior shopper approval; it does not establish that processing model for every recurring subscription. Capture within 13 days (one day in TEST); partial capture needs manual capture, and unclaimed amount is cancelled unless multiple partial capture is enabled. The discount JSON is illustrative and has an empty currency (lines 870–904). Sandbox US choice is not a discovery pair.
