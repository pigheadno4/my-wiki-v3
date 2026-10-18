# Worker retrieval checks

Q1. What does this PIISP guide provide, and what setup does it name?

A1. A third-party PIISP uses `POST /funds-confirmations` to check available funds for an account and instructed amount on behalf of a consenting account holder (raw lines 15–23, 33–44). The page calls for Adyen onboarding and an access token for the Adyen business account; the test request carries a Bearer token and request/address headers (raw lines 25–31, 46–63). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-piisp]] → [[raw/adyen/docs/business-accounts/piisp/2026-09-15]].

Q2. Does `fundsAvailable: true` reserve or transfer EUR 10.50?

A2. No. The example checks a sample account/amount and returns `fundsAvailable: true`; the stated response meaning is availability for the instructed amount, while `false` means insufficient funds for it (raw lines 39–73). This guide contains no hold, payment-initiation, debit or settlement step; its PISP link is only a separate route (raw lines 75–78). The answer is limited to the guide's informational check and cannot establish later availability or a live operation. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-piisp]] → [[raw/adyen/docs/business-accounts/piisp/2026-09-15]].
