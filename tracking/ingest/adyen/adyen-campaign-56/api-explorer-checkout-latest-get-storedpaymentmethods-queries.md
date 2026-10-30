# C56 fixed query answers — Checkout GET /storedPaymentMethods

Source: `source-adyen-api-explorer-checkout-latest-get-storedpaymentmethods` — https://docs.adyen.com/api-explorer/Checkout/latest/get/storedPaymentMethods
Pinned raw: `raw/adyen/api-explorer/Checkout/latest/get/storedPaymentMethods/2026-09-15.md` (fully read lines 1–60 and 61–112; SHA-256 `1f313c4681277858d0db1cb2c98e58fae24f77e0148c127ccfc2b227ef5c65a2`).

## Q1: For `get/storedPaymentMethods`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?

The captured `GET /storedPaymentMethods` lists any available tokens for a shopper's stored payment details, returning summaries and token IDs usable with later payment requests for that shopper (raw lines 5–7). The captured server is Checkout v72 **test** (`https://checkout-test.adyen.com/v72`, line 10). The table identifies `merchantAccount` and `shopperReference` as query parameters, both marked **No** under Required; `shopperReference` has a minimum length of three characters and must exclude PII such as name/email (lines 12–18). Its opening prose instead says the shopper is identified “in the path” (line 7), while the displayed route has no path shopper placeholder (line 5). The page itself does not reconcile that conflict or state authentication prerequisites.

## Q2: For `get/storedPaymentMethods`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

`200 Success` establishes request success, with optional top-level merchant/shopper fields and optional `storedPaymentMethods` array (lines 20–30). Stored objects may include an `id` and `supportedRecurringProcessingModels`; the latter describes `Subscription`, `CardOnFile`, and `UnscheduledCardOnFile` (lines 50, 79). Nested Yes markers in billing-address and mandate fields are conditional on those optional objects appearing (lines 30–39, 53–73). The sample is one Visa card supporting all three models, not a guarantee for all tokens (lines 82–112). This page has no documented error response or live server; token listing is not evidence of creation, deletion, payment authorization, capture, settlement, or current behavior of the `latest` route beyond the v72 test snapshot (lines 5–10, 20–112).
