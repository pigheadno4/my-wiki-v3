# docs-payment-methods-pay-by-bank-us — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pay-by-bank-us]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-pay-by-bank-us]] is the Pay by Bank (US) payment-method overview: it describes a US/USD online-banking redirect method, Plaid and bank permissions, ACH Direct Debit routing, a capability table, tokenization advice, ACH return exposure, and separate Web/iOS/Android/API-only routes (raw lines 22–32, 34–48, 50–74). It does not define an endpoint request, SDK version, exact merchant enablement, or successful authorization/capture/settlement for a particular payment (full raw, lines 1–74). The 2026-09-15 snapshot is historical evidence, not a live eligibility check (raw lines 2, 11).

## Q2 — What central capability, prerequisites, and warnings are stated?

[[source-adyen-docs-payment-methods-pay-by-bank-us]] says the shopper grants Plaid account-connection permission, selects a bank, grants bank-side data-collection permission, and returns to the merchant site/app; the transactions use ACH Direct Debit (raw lines 24–28). Its US/USD matrix supports recurring, refunds including multiple partial refunds, separate/partial captures and chargebacks, but marks multiple partial captures unsupported (raw lines 30–32). Tokenization on the first transaction is recommended for lower-friction later payments, not stated as a prerequisite (raw lines 34–38). ACH returns remain possible despite validation and checks; the source warns about B2B company-ID allowlisting, long dispute windows, a debit report line and `CHARGEBACK` webhook, nondefensible chargebacks, and reason-code-dependent retry (raw lines 40–48). The linked platform/API guides must establish implementation details (raw lines 50–74).
