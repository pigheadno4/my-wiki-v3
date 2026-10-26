# docs-payment-methods-twint-flutter-drop-in retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-twint-flutter-drop-in]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 page adds TWINT to existing Flutter Drop-in, separating Sessions and Advanced prerequisites and repeating a recurring-token route (pinned raw lines 15–48, 50–89, 97–160). It does not specify a concrete redirect response, shopper return, capture rule or final payment outcome. It cannot establish current merchant enablement, a created token or successful payment. Canonical source stem: `source-adyen-docs-payment-methods-twint-flutter-drop-in`.

## Q2 — What are central prerequisites, recurring capability and warnings?

Sessions requires existing Flutter Drop-in, Checkout API v68+, redirect handling and Support contact to add TWINT, with no extra `/sessions` fields or Drop-in configuration (pinned raw lines 25–48). Its integration-type URL points to Advanced despite the Sessions label and Sessions links (lines 33–42). Advanced separately requires its corresponding integration, redirect handling and Customer Area addition, with no extra normal `/payments` fields or configuration; no Advanced API minimum is stated (lines 97–119). Both sections describe initial `storePaymentMethod` plus shopper reference, `recurring.token.created` stored ID, then `ContAuth` Subscription or UnscheduledCardOnFile reuse (lines 50–89, 121–160). TEST status checks and a separate live Customer Area request are stated, but no test/live outcome is proved (lines 91–95, 162–166). Canonical source stem: `source-adyen-docs-payment-methods-twint-flutter-drop-in`.
