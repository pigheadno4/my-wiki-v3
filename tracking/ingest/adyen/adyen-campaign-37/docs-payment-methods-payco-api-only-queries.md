# PAYCO API-only retrieval checks

**Q1. What is the page for, and what cannot be inferred?** It adds PayCo to an existing Web API-only Advanced redirect integration and shows KR/KRW method discovery and a `kcp_payco` example. It does not prove merchant eligibility or payment completion. Raw locators: `raw/adyen/docs/payment-methods/payco/api-only/2026-09-15.md:17-29,44-53,329-340,660-676`. Canonical stem: `https://docs.adyen.com/payment-methods/payco/api-only`.

**Q2. What capability, prerequisites, and warnings matter?** Add PayCo in Customer Area, handle `redirect`, and build a form with no extra PayCo fields. Discovery uses KR/KRW; payment examples use `kcp_payco`, KRW, reference and return URL. The “how it works” step mentions item information, but the parameter section says no additional fields and examples omit items; no unconditional item schema should be inferred. There are no specific test credentials, and the page gives no final outcome procedure. Raw locators: `raw/adyen/docs/payment-methods/payco/api-only/2026-09-15.md:23-52,329-368,660-682`. Canonical stem: `https://docs.adyen.com/payment-methods/payco/api-only`.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payco-api-only]] → [[raw/adyen/docs/payment-methods/payco/api-only/2026-09-15]].
