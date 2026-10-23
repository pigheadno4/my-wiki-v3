# C31 retrieval checks: Apple Pay errors

Q1. What does this page troubleshoot and what path-specific prerequisites does it name?

It maps selected Apple Pay API/payment-sheet/integration errors to checks (raw lines 15–23). For `/applePay/sessions` 422, it names SDK 3.18.0+ and API v65+, `merchantId` in `/paymentMethods` configuration, full `/paymentMethods` response plus registered domains for Drop-in/Components, or required request parameters for API-only (raw lines 114–141). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]] → [[raw/adyen/docs/payment-methods/apple-pay/handle-apple-pay-errors/2026-09-15]].

Q2. Which certificate/key distinction and error boundaries prevent the wrong repair?

`5_004` is an Adyen API-credential/payment-processing-certificate and merchant-identifier mapping check, including activation and test/live conditions (raw lines 46–71). The RSA(2048) CSR error is instead for a **web merchant identity certificate**; the page explicitly says not to use the Adyen CSR for that identity (raw lines 73–81). `5_002` token stringification/base64 is presented as a `/payments` custom-integration example, not a universal Drop-in rule (raw lines 35–44). The web “Payment Not Processed” and Adobe Commerce/PEM checks are separate (raw lines 83–112). None proves a repaired payment or authorization. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]] → [[raw/adyen/docs/payment-methods/apple-pay/handle-apple-pay-errors/2026-09-15]].
