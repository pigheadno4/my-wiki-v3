# C44 Klarna Web Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-web-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/web-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-web-drop-in]]` → `[[raw/adyen/docs/payment-methods/klarna/web-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What is the Klarna Web Drop-in guide for, and what does it not prove?

**Answer path:** The source entry routes to the 2026-09-15 pinned guide, raw lines 19–25 for widget/redirect purpose, `## Requirements` lines 27–43 for an existing Sessions or Advanced Web Drop-in integration and Customer Area method setup, and `## API reference` lines 53–59 and 771–789 for endpoint tabs. It is a documented integration procedure and TEST/live checklist, not evidence of a merchant's current enablement, checkout deployment or successful payment.

## Q2 — central capability, prerequisites and warnings

**Query:** What data and lifecycle checks govern a Klarna Web Drop-in payment, capture and token reuse?

**Answer path:** Start at `## API reference` field tables, raw lines 61–74 and 773–788: line-item total must match `amount.value` and each item needs `description`; shopper email and country are marked required, with country/billing and optional locale/currency alignment. `## Drop-in configuration` lines 1512–1548 distinguishes optional widget and redirect. `## Capture the payment` lines 1550–1554 and 2012–2043 gives the immediate-plus-24-hour-shipping automatic capture exception, otherwise 90-day manual capture and `received` response versus later `CAPTURE` webhook. `### Partial captures` lines 2118–2125 and mixed endpoint examples require API-specific reading. `## Recurring payments` lines 2133–2178 supplies settled-initial-payment and token-webhook mechanics. The related `[[source-adyen-docs-payment-methods-klarna]]` overview, raw line 38, directs merchants to contact Adyen Support before offering recurring payments and limits Pay over time to long-term subscriptions, excluding monthly subscriptions and one-off/on-demand tokenized purchases; product/country conditions also apply. `## Test and go live` lines 2247–2274 contains live-only rejection conditions and readiness checks. The request examples' `en_US`/SE/SEK locale combination conflicts with locale-matching prose; do not use it as a validated locale recipe.
