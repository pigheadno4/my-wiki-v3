# Fixed retrieval checks — docs-payment-methods-online-banking-czech-republic-ios

## Q1 — Identify the iOS chooser and its scope

- Query: What is the purpose of Adyen's Online banking Czech Republic iOS page, and does it define payment fields or outcomes?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-ios.md` → `raw/adyen/docs/payment-methods/online-banking-czech-republic/ios/2026-09-15.md`.
- Expected: It adds the method to an iOS app by routing to Drop-in and Components method guides (raw lines 15–27); no method-specific request schema, SDK version or outcome is given in this 36-line chooser. `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` carries separate CZ/CZK method context.
- Scope: The route is a dated 2026-09-15 documentation snapshot and does not prove current availability or successful payment execution.

## Q2 — Recover the exact base-guide choices

- Query: Which iOS integration routes does the chooser name, and what must be built first?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-ios.md` → pinned raw.
- Expected: Drop-in is labeled all-in-one UI (raw lines 21–23); Components routes to `OnlineBankingComponent` (25–27). It says to create the main integration before adding this method, then lists iOS Drop-in and Components for both Sessions and Advanced flows (29–36).
- Scope: Child links are navigation, not child-guide behavior imported into this page. Use the selected child guide for request, redirect and final-status details.
