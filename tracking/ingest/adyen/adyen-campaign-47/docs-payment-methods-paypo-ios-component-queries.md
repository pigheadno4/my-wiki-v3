# PayPo iOS Component retrieval checks

## Q1 — What does this guide cover, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-paypo-ios-component]]` → `[[raw/adyen/docs/payment-methods/paypo/ios-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-paypo-ios-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/paypo/ios-component/2026-09-15.md`. Raw lines 15–48 and 468–523 show PayPo additions for existing iOS Components Sessions or Advanced flows, with PL/PLN examples. The captured guide does not prove current eligibility, live enablement or final payment success.

## Q2 — Which fields, redirect/capture boundaries and warnings matter?

Use the same root/provider/concept/source/raw route. Sessions requires Checkout API v68+, name and email; Advanced requires `paymentMethod.type=paypo`, name/email and additional redirect handling, with billing/delivery addresses unmarked in both request tables (raw lines 25–48, 468–523). RedirectShopper is an intermediate action (lines 894–908). The offer lasts up to 72 hours before authorization; shopper's 30-day PayPo term starts at authorization, and merchant capture is full-only after authorization, with funding following capture (lines 391–421, 910–940). Both Component snippets literally use unexplained `None` and the Advanced Components base link selects Drop-in (lines 431–450, 476–505). Test values and live request are at lines 454–466 and 942–954.
