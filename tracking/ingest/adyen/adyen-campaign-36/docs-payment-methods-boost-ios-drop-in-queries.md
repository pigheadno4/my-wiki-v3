# docs-payment-methods-boost-ios-drop-in — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Boost Wallet add-on for existing **iOS Drop-in** Sessions and Advanced integrations, not a full base or completed payment guide (source-adyen-docs-payment-methods-boost-ios-drop-in; raw lines 15–25, 54–64). The page cannot establish current merchant eligibility, shopper return handling, webhook status, authorization or settlement (raw lines 25–82). Its live penny-test language is a warning about the lack of a test environment, not evidence that any test occurred (raw lines 50–52, 80–82).

Q2. What are its central capability, prerequisites and warnings?

Sessions requires an iOS Drop-in base integration, Checkout API v68+ and Boost Wallet added in Customer Area, with no extra Boost-specific `/sessions` fields or configuration (raw lines 29–46). Advanced requires an existing iOS Drop-in flow with `action.type: redirect` handling and Customer Area addition, and no extra Boost Wallet configuration or `/payments` fields; this section does not separately give an API minimum (raw lines 58–76). The source states that no Boost Wallet TEST environment exists and that penny testing must use LIVE, so no financial test should be inferred or conducted as part of this ingest (raw lines 48–52, 78–82).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-ios-drop-in]] → [[raw/adyen/docs/payment-methods/boost/ios-drop-in/2026-09-15]].
