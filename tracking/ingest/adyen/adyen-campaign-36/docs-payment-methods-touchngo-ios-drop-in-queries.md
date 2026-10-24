# docs-payment-methods-touchngo-ios-drop-in — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a short Touch'n Go add-on for an existing **iOS Drop-in** integration, with Sessions/Advanced prerequisites and method field/configuration statements (source-adyen-docs-payment-methods-touchngo-ios-drop-in; raw lines 15–54). It does not itself explain shopper redirect/return, webhook result semantics, current merchant eligibility or any final payment outcome (raw lines 21–66). The `/sessions` statement's v5.0.0 is a **Drop-in** version, not a Checkout API minimum (raw line 43).

Q2. What are its central capability, prerequisites and warnings?

Both Sessions and Advanced require the corresponding prebuilt iOS Drop-in flow and a Support request to add Touch'n Go in Customer Area (raw lines 21–37). No additional Touch'n Go API fields or version-tab Drop-in integration are required; the page calls `/sessions` the default with Drop-in v5.0.0+ and points to `/payments` for additional use cases (raw lines 39–54). Test status is checked in test Customer Area, while live acceptance needs separate Support addition in live Customer Area; neither step proves authorization or settlement (raw lines 56–60).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-touchngo-ios-drop-in]] → [[raw/adyen/docs/payment-methods/touchngo/ios-drop-in/2026-09-15]].
