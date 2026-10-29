# Klarna iOS Drop-in retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-klarna-ios-drop-in`
**Full pinned raw:** `raw/adyen/docs/payment-methods/klarna/ios-drop-in/2026-09-15.md`
**Verified locators:** `# Klarna Drop-in integration`, lines 15–19; `## Requirements`, lines 21–37; `## API reference`, lines 39–45 and 757–759; `## Test and go live`, lines 2199–2226.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-klarna-ios-drop-in.md` → pinned raw.
**Answer boundary:** This is an add-on to existing iOS Drop-in Sessions or Advanced flow. Snapshot guidance and test examples do not prove current merchant eligibility, live approval, authorization, capture or settlement.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions/Advanced requirements lines 25–37; `/sessions` and `/payments` tables lines 43–60, 757–774; `## Drop-in configuration` lines 1498–1506; `## Capture the payment` lines 1508–1510 and 1970–2003; legacy capture/partial lines 2005–2083; `## Recurring payments` lines 2085–2197; live gates lines 2205–2226.
**Answer boundary:** Add Klarna in Customer Area, send matching line items and shopper/country data, observe capture gate and 90-day expiry, await CAPTURE webhook, and use settled-token webhook for `/payments` recurring. The SE/SEK examples use `en_US` despite the matching-locale prose; new and legacy capture examples have different shapes. Do not generalize the Pay Now recurring sample to every Klarna product.
