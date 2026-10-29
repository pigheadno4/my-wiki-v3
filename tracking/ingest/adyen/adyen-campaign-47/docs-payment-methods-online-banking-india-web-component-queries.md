# Online Banking India Web Component retrieval checks

## Q1 — Scope and proof boundary

Query: What is the Online Banking India Web Component page for, and does it establish a complete payment flow or current live enablement?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2610 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india-web-component.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/online-banking-india/web-component/2026-09-15.md` `# Web Component` lines 15–21, `## Sessions flow Component` lines 23–40, `## Advanced flow Component` lines 84–93, and `## Test and go live` lines 564–568. Expected answer: 2026-09-15-captured method-specific add-on for existing Web Components Sessions/Advanced integrations; no complete redirect finality or live execution proof.

## Q2 — Flow prerequisites, fields and warnings

Query: What differs between Sessions and Advanced Web Components for Online Banking India, and which version/snippet caveats must be kept?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india-web-component.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/online-banking-india/web-component/2026-09-15.md` lines 27–76, 86–140 and 144–173, plus `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/online-banking-india/2026-09-15.md` line 25. Expected answer: Sessions requires existing Web Components, Checkout API v68+, redirect handling and Customer Area setup but no extra /sessions fields. Advanced also requires redirect handling and setup; /payments marks paymentMethod.issuer and browserInfo required. The separate method overview says India regulatory compliance, a local entity and a local integration in India are prerequisites and directs merchants to account manager or Support for details; this is overview evidence, not a child-page claim or current eligibility proof. Both import OnlineBankingIN and need no method-specific configuration. Warnings: Advanced API row omits the version number ('v or later'); both initializer snippets say newOnlineBankingIN although import/prose say OnlineBankingIN, so do not copy them unverified or infer an Advanced minimum.
