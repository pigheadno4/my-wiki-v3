# docs-payment-methods-online-banking-thailand-ios-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is Adyen's method-specific **Online banking Thailand iOS Component** guide for adding the method to an existing iOS Components integration using Sessions or Advanced server-side flow (source-adyen-docs-payment-methods-online-banking-thailand-ios-component; raw lines 15–25, 80–84). It does not supply the complete main integration, a currency, an iOS SDK version, an Advanced Checkout API minimum, the issuer-ID list or proof of current eligibility/payment success (raw lines 25–48, 72–78, 80–131).

Q2. What is its central capability, prerequisites and warnings?

Sessions requires the existing iOS Components flow, Checkout API v68+, redirect handling and method addition in Customer Area; no extra `/sessions` or method configuration parameters are specified (source-adyen-docs-payment-methods-online-banking-thailand-ios-component; raw lines 25–48). The Swift sample selects `molpay_ebanking_TH` and initiates an `InstantPaymentComponent` (raw lines 50–70). Advanced likewise requires redirect handling and Customer Area addition, with no extra configuration or `/payments` fields; its integration-type row says “iOS Components” while linking to `integration=Drop-in`, whereas its redirect link uses Components (raw lines 80–123). The test-payment check and separate live Customer Area request do not establish approval or final authorization/settlement (raw lines 72–78, 125–131).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-thailand-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-thailand/ios-component/2026-09-15]].
