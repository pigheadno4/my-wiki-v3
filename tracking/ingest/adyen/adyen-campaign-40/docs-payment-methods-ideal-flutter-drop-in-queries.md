# docs-payment-methods-ideal-flutter-drop-in retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-ideal-flutter-drop-in]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 snapshot is an Adyen add-on for an existing Flutter Drop-in iDEAL | Wero integration, divided by Sessions and Advanced server-side flows (pinned raw lines 15–25, 322–344). Its initial path requires redirect handling, while the recurring route is through SEPA Direct Debit (lines 33–36, 54–69, 330–332, 350–365). It does not prove current merchant enablement, successful token issuance or payment execution; `Received` on the token-payment example is followed by webhook status tracking (lines 277–282, 573–578). The canonical source stem is `source-adyen-docs-payment-methods-ideal-flutter-drop-in`.

## Q2 — What are the central prerequisites, capability and warnings?

Sessions requires existing Flutter Drop-in, Checkout API v68+, redirect handling and contacting Support for Customer Area addition; no extra `/sessions` parameters or configuration are specified (pinned raw lines 29–48). Its integration-type link points to an Advanced URL, so the named Sessions route should be checked against the main guide (line 33). Advanced separately requires existing Advanced Flutter Drop-in, redirect handling and Customer Area addition, with no additional `/payments` parameters or configuration (lines 326–344). For shopper-absent `Subscription` or `UnscheduledCardOnFile` payments, the guide uses SEPA Direct Debit tokenization and a `recurring.token.created` webhook carrying `storedPaymentMethodId` (lines 54–77, 350–373); the examples show a `sepadirectdebit` stored method and `ContAuth` (lines 81–99, 377–395). The source warns TEST is unreliable, recommends LIVE penny tests, and makes TEST simulations conditional on the test environment being available (lines 284–320, 580–616). `Received` and `pspReference` mean the token-payment request was received, with success tracked through webhooks (lines 277–282, 573–578). The canonical source stem is `source-adyen-docs-payment-methods-ideal-flutter-drop-in`.
