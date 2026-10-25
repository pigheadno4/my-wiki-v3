# docs-payment-methods-napas-card-ios-drop-in — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Napas card add-on for an existing **iOS Drop-in** integration (source-adyen-docs-payment-methods-napas-card-ios-drop-in; raw lines 15–26). It does not establish current merchant eligibility, full card-gateway/OTP redirect and return behavior, a Checkout API minimum or final authorization/settlement (raw lines 28–64). Its “See also” iOS Components guide points to Components despite the Drop-in identity, so it is not the matching base route (raw lines 15–25, 60–62).

Q2. What are its central capability, prerequisites and warnings?

The page requires the iOS Drop-in base integration and adding Napas card in **test Customer Area**, with no extra Napas-specific fields or version-tab Drop-in configuration; `/sessions` is the default with **Drop-in v5.0.0+**, while `/payments` is listed for additional use cases (raw lines 21–43). It lists test-only card/OTP scenario fixtures and test-status navigation, while live acceptance needs a separate live Customer Area request (raw lines 45–58). The fixture labeled “Successful” and the test status link are not evidence of an executed payment, and the page does not instruct handling live card/PIN/OTP data.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card-ios-drop-in]] → [[raw/adyen/docs/payment-methods/napas-card/ios-drop-in/2026-09-15]].
