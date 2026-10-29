# Online banking Finland React Native Component retrieval checks

## Q1 — Which server-side flow is supported, and what are the Advanced prerequisites?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking-react-native-component.md` → `raw/adyen/docs/payment-methods/finland-online-banking/react-native-component/2026-09-15.md`.
Expected answer: React Native Components do not support Sessions here. Advanced requires an existing React Native Components integration, redirect handling, Customer Area method setup, and no extra method-specific configuration. Its `/payments` table requires `paymentMethod.type=ebanking_FI` and shopperEmail; issuer is required only for Issuer redirect flow, and returnUrl row states a 1024-character maximum without a required mark. The Advanced integration-type URL incorrectly targets Drop-in, while other links name Components; the prose remains the guide's scope. Raw locators: lines 25–60. Approved `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking.md` supplies Paytrail/FI/EUR overview context separately.

## Q2 — What can be inferred from the samples, redirect response, and testing note?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: every Advanced request sample omits the required paymentMethod object and uses malformed `s.hopper@@example.com`; curl lacks continuation before `-d`. Therefore snippets are incomplete. The shown RedirectShopper/GET redirect action is intermediate, not a completed payment; this child lacks return/details/final-webhook steps. The source advises Paytrail test environment/sample data before live acceptance and says multiple partial refund testing is unavailable; that test limitation is separate from the approved overview's checked capability matrix and unresolved “See note.” Raw locators: lines 66–80, 99–109, 193–221, 347–367. No actual payment, refund test, or merchant eligibility is shown.

Canonical source URL: `https://docs.adyen.com/payment-methods/finland-online-banking/react-native-component`.
