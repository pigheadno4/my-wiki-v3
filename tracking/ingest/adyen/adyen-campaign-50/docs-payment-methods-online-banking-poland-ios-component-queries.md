# docs-payment-methods-online-banking-poland-ios-component retrieval checks

## Q1 — Purpose and route

Query: What does Adyen's Online banking Poland iOS Component guide cover, and what does it not prove?

Expected: This is the 2026-09-15-captured iOS Components add-on for existing Sessions and Advanced integrations, covering Online banking Poland setup, request additions, Component presentation, redirect and test/live instructions. It does not establish current account eligibility, an executable SDK recipe from its placeholder snippet, or final payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15]]. Evidence: full pinned raw `raw/adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15.md`, heading `# Online banking Poland iOS Component` lines 15–23; flow headings lines 25 and 307; raw lines 270–299, 692–712.

## Q2 — Central details and warnings

Query: Which request fields and redirect requirements appear in the Sessions and Advanced iOS Components paths, and what sample caveats matter?

Expected: Sessions requires an existing iOS Components Sessions integration, Checkout API v68+, redirect handling and method setup; shopperEmail is marked required, at most 50 characters, in /sessions (raw lines 25–46). The PL/PLN app returnUrl is a sample (lines 48–69). Advanced requires existing iOS Components with action.type redirect handling (raw line 316), marks shopperEmail required (50 characters maximum) and lists paymentMethod.issuer without a required mark; its example onlineBanking_PL/141/PLN 1000 and web returnUrl are examples (lines 307–383). The illustrated Advanced response has RedirectShopper and redirect action (lines 692–706), not final success. Warn that Advanced Components prerequisite links to `integration=Drop-in` (line 315), and both Swift initialization sections name `None` and a configuration object while the prose says no added configuration (lines 270–299, 320–346). Test status and live method request are Customer Area steps (lines 301–305, 708–712). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15.md`.
