# Scalapay API-only retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the captured Scalapay API-only guide cover and what does its presence prove?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay-api-only]] → [[raw/adyen/docs/payment-methods/scalapay/api-only/2026-09-15]]. It adds Scalapay to an existing merchant-built API-only integration, with FR/IT/PT/ES and EUR discovery, redirect, result and capture guidance (raw lines 15–37, 39–535). It does not prove current merchant enablement or completed payment. [[source-adyen-docs-payment-methods-scalapay]] supplies the BNPL overview and snapshot recurring/chargeback marks; the generic tokenization See also link here does not establish Scalapay recurring support.

## Q2 — Central capability, prerequisites, and warnings

**Question:** What request, outcome, capture and refund conditions must an implementer preserve?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay-api-only]] → [[raw/adyen/docs/payment-methods/scalapay/api-only/2026-09-15]]. Existing API-only setup and test Customer Area addition are prerequisites; activation has standard-pricing default and account-manager eligibility check for Enterprise pricing (raw lines 21–28). The `/payments` table marks `scalapay_3x`, country, returnUrl, email and name required, but the examples omit email (raw lines 39–80). Follow returned redirect action and `/payments/details`; Pending/Received and non-return need AUTHORISATION webhook (raw lines 415–505). Manual or delayed automatic capture expires after seven days; confirm successful capture before shipping and cancel an unused balance. Multiple partial capture requires Support, and related refunds need `capturePspReference` (raw lines 507–527). Test and live Customer Area steps are separate (raw lines 529–535).
