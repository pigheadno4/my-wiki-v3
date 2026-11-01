# Fixed-query check: A2A Issuer /payments/details

## Q1

The captured A2A Issuer API v1 operation `POST /payments/details` uses separate test/live balance-platform hosts to retrieve an open payment's details and an Adyen-generated token. The body requires `method`, payment-method-generated `payload`, and `source` (`qr`, `redirect`, or `pushNotification`). HTTP 200 requires displayable `details` with amount, counterparty, description, expiry, plus `token` for later confirm/cancel. Its iDEAL redirect payload and IBAN recipient are examples. See [[source-adyen-api-explorer-a2aissuer-api-latest-post-payments-details]], [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 5–53 and 112–138]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/details).

## Q2

HTTP 200 confirms detail retrieval, not user approval, SCA, confirmation, cancellation, or settled funds. The response table lists 400 malformed request, 422 validation error, and 500 server error; 422 examples include expired/unavailable (`1069_004`) and final-state (`1069_005`) payments, while nested `invalidFields` properties are required only when an entry is present. The pinned operation gives no retry safety, delivery, signature, or financial finality guarantee. See [[source-adyen-api-explorer-a2aissuer-api-latest-post-payments-details]], [[raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/details/2026-09-15|raw lines 56–110 and 140–229]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/details).
