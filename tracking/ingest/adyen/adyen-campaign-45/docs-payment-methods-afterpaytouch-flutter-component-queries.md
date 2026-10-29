# Afterpay Flutter Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-afterpaytouch-flutter-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/afterpaytouch/flutter-component/2026-09-15.md`
**Verified locators:** `# Afterpay Flutter Component`, lines 15–23; `## Sessions flow Component`, line 25; `## Advanced flow Component`, later in raw; `## Capture the payment`, lines 1552–1571.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-flutter-component.md` → pinned raw.
**Answer boundary:** This is a method add-on for an existing Flutter Components integration, not a standalone payment flow. AU/AUD TEST examples and sandbox choices do not establish production country coverage, merchant enablement or a completed redirect/authorization.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions requirements lines 27–34 and request table 42–51; Advanced requirements and `/payments` table in the second flow section; redirect response lines 1536–1550; capture lines 1552–1571; test/live lines 1573–1592.
**Answer boundary:** Sessions requires Checkout API v68+, existing Flutter Components, redirect handling and Customer Area setup. Both flow tables require shopper, country, billing/delivery and line-item data; Advanced adds `afterpaytouch` paymentMethod. Both say no extra method configuration. Capture within 13 days (one day in TEST); delayed shipping needs capture delay or manual capture, and partial capture needs manual capture. Unclaimed amount after one partial capture is cancelled unless multiple partial captures are enabled through Support. The Components Requirements rows link to a Drop-in Advanced-flow URL, so verify the base guide route before using it.
