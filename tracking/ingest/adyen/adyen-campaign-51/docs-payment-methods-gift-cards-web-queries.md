# Fixed retrieval checks — docs-payment-methods-gift-cards-web

## Q1 — Identify the Web chooser's purpose and limits

- Query: What does Adyen's gift-cards Web page provide, and does it define gift-card payment or partial-payment behavior?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-web.md` → `raw/adyen/docs/payment-methods/gift-cards/web/2026-09-15.md`.
- Expected: A short Web chooser for gift-card Drop-in and Components method guides (raw lines 15–27) plus generic Web integration references (29). It contains no request fields, balance/partial-payment logic, result status or onboarding instructions. The separate overview `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md` holds cross-channel gift-card context.
- Scope: Last modified 2019-09-30 and captured 2026-09-15; links do not prove current provider or merchant eligibility or a payment.

## Q2 — Recover exact routes without inventing server flows

- Query: Which gift-card Web UI choices and further references are named, and are Sessions/Advanced flows stated?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-web.md` → pinned raw.
- Expected: Drop-in is described as all-in-one website UI (raw lines 21–23); Components as a pre-built renderer (25–27); generic Web Drop-in/Components links appear at line 29. The page does not name Sessions, Advanced or a Checkout API version.
- Scope: Follow the selected child method guide for provider, request, balance, partial-payment, outcome and test/live details; do not import them into this navigation page.
