# docs-payment-methods-gcash-flutter-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It gives GCash-specific additions for **existing Flutter Components** integrations in Sessions and Advanced flows, not a complete base implementation or proof of current merchant eligibility and successful payment (source-adyen-docs-payment-methods-gcash-flutter-component; raw lines 15–25, 27–34, 296–306). Both Integration type links point to Drop-in, and the Sessions one also points to Advanced flow, so those URLs cannot be assumed to supply the matching Components base procedure (raw lines 31, 304). TEST snippets, Customer Area checks and use of a real GCash-registered number do not establish live enablement, authorization or settlement (raw lines 87–108, 286–294, 558–566).

Q2. What are its central capability, prerequisites and warnings?

Sessions calls for Checkout API v68+, redirect handling (`action.type: redirect`) and GCash added in Customer Area, but no GCash-specific `/sessions` or Component configuration additions (raw lines 27–46). Advanced separately calls for an existing Components flow, redirect handling and Customer Area addition, with no extra ordinary `/payments` or configuration additions (raw lines 296–318). Recurring is a separate `/payments` token route: `storePaymentMethod: true`, a shopper reference of at least three characters, **settlement-gated** `recurring.token.created` webhook carrying `storedPaymentMethodId`, and later token payments with `ContAuth` and the fixed/nonfixed recurring model (raw lines 48–85, 320–357). The phrase “test successful GCash live payments” sits in a test/live section; preserve its wording and the separate live Customer Area request rather than claiming a test result or live approval (raw lines 286–294, 558–566).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash-flutter-component]] → [[raw/adyen/docs/payment-methods/gcash/flutter-component/2026-09-15]].
