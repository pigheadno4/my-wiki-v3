# docs-payment-methods-blik-api-only — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-blik-api-only]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-blik-api-only]] is the BLIK add-on for an existing API-only integration, covering a merchant-built PL/PLN code form, `/paymentMethods` discovery, `/payments`, waiting screen and webhook, plus a One Click consent/token path (raw lines 17–50, 362–404, 418–517). It says the method works with all Checkout API versions; the v68 curl and language-library versions are examples (raw lines 25, 52–360). The page does not supply a separate later code-free payment request, establish current enablement, or turn a `Pending` response into a successful payment (raw lines 362–404, 418–517). Its raw was fetched 2026-09-15 and metadata last modified 2020-07-09 (raw lines 2, 11).

## Q2 — What central capability, prerequisites, and warnings are stated?

[[source-adyen-docs-payment-methods-blik-api-only]] requires an existing API-only integration and BLIK in test Customer Area, then asks the merchant to display BLIK, collect a six-digit code, discover with PL/PLN, and submit `type: blik` and `blikCode` (raw lines 21–50). The response can be `Pending` with a wait-screen `action`; the shopper completes in their app and the `AUTHORISATION` webhook reports success/failure, while `Refused` can reflect an incorrect code (raw lines 362–404). For One Click consent, the initial code-bearing request lists a shopper reference, `storePaymentMethod: true`, and `CardOnFile`; an enabled recurring-token webhook can then report `recurring.token.created` (raw lines 432–441, 509–515). The One Click sample has a missing comma and string `storePaymentMethod`, while discovery conditionality and app-label casing disagree across prose/example (raw lines 43, 426, 450–453, 517–529). Testing uses code `999000` and BLIK guidelines; live BLIK requires live Customer Area addition, with One Click additionally calling for BLIK certification/enablement (raw lines 406–416, 532–545).
