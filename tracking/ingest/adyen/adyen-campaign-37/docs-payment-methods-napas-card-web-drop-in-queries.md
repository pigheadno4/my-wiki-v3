# Napas card Web Drop-in retrieval checks

## Q1 — Purpose, scope, and non-inferences

`source-adyen-docs-payment-methods-napas-card-web-drop-in` is the 2026-09-15 method add-on for Napas card online-banking payments in an already-built Web Drop-in integration (raw lines 15–26). It does not supply a standalone checkout, payment-method identifier, redirect/details/webhook procedure, current live eligibility or proof of successful payment; its named scenarios are TEST fixtures, and a separate live Customer Area request is required (raw lines 28–58). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card-web-drop-in]] → [[raw/adyen/docs/payment-methods/napas-card/web-drop-in/2026-09-15]].

## Q2 — Central capability, prerequisites, warnings

The merchant adds Napas card in test Customer Area to an existing Web Drop-in; no extra Napas fields or Drop-in configuration are specified (raw lines 21–37). The guide calls `/sessions` the default with Drop-in v5.0.0+ and `/payments` an additional-use-case endpoint (raw lines 28–33). Its test table covers success, blocked card, insufficient funds and amount-limit scenarios and tells merchants to check Customer Area Payment list; live acceptance needs a separate live Customer Area request (raw lines 39–52). The test fixtures and status lookup do not prove an executed live payment. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card-web-drop-in]] → [[raw/adyen/docs/payment-methods/napas-card/web-drop-in/2026-09-15]].
