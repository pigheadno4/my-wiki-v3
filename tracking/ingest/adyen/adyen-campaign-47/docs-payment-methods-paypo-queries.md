# Fixed queries — PayPo overview

## Q1 — purpose, scope, and limits

**Query:** What does the captured Adyen PayPo overview document establish, and what should a reader avoid inferring?

**Expected answer:** The 2026-09-15-captured overview at `https://docs.adyen.com/payment-methods/paypo` describes PayPo as a Polish buy now, pay later payment method, gives a capability matrix, and routes readers to platform-specific integrations. It states a 30-day payment option or up to 6 installments (full pinned `raw/adyen/docs/payment-methods/paypo/2026-09-15.md`, `# PayPo`, lines 15–27). Its popularity and active-user figures are dated source assertions. The snapshot, capability marks, and navigation do not establish current availability, merchant-account enablement, shopper approval, successful execution, or a PayPo-specific 3D Secure feature merely because a general “See also” link appears at line 70. Retrieval route: root `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo.md`.

## Q2 — central capability and integration routes

**Query:** In the captured PayPo overview, which geography, currency, flow, lifecycle marks, and integration routes are stated?

**Expected answer:** The capability row identifies Buy Now Pay Later, **redirect**, **PL**, and **PLN**. It marks recurring and chargebacks unavailable; refunds, partial refunds, multiple partial refunds, and separate captures available; partial captures and multiple partial captures unavailable. Separate captures must not be read as partial-capture support. These are overview marks rather than current account entitlements or guarantees of a successful operation (`raw/adyen/docs/payment-methods/paypo/2026-09-15.md`, capability table lines 25–27). The chooser links pre-built Web, iOS, Android, React Native, and Flutter UI solutions and an API-only build-your-own UI route for website/iOS/Android (`## How do you want to integrate?`, lines 29–65). The page does not present a complete implementation procedure. Retrieval route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo.md`.
