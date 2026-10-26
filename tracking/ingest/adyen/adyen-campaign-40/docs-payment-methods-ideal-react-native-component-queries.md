# docs-payment-methods-ideal-react-native-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-ideal-react-native-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 snapshot covers adding iDEAL | Wero to React Native Components via Advanced flow, explicitly excluding Sessions Components (pinned raw lines 15–29, 31–53). Its source title says “React Component,” while its canonical path and requirements specify React Native (lines 5–10, 39–40). It cannot establish current merchant enablement, issued token or successful payment; the example `Received` status is followed by webhook tracking (lines 282–287). Canonical source stem: `source-adyen-docs-payment-methods-ideal-react-native-component`.

## Q2 — What are the central prerequisites, capability and warnings?

Advanced requires existing React Native Components, redirect handling and Customer Area addition, but says no extra Component configuration or normal `/payments` parameters (pinned raw lines 35–53). Its integration-type link points to Drop-in despite Components text and other Components links (lines 39–40, 53). For later shopper-absent `Subscription` or `UnscheduledCardOnFile` payments, the guide uses SEPA Direct Debit tokenization; `recurring.token.created` carries `storedPaymentMethodId` (lines 59–82). Examples use `sepadirectdebit` and `ContAuth`, while Java has a different amount and omits the shopper reference shown elsewhere (lines 86–135, 146–162). `Received` is only request receipt, with success tracked by webhooks (lines 282–287). TEST is described as unreliable; LIVE penny testing and TEST issuer simulations are conditional guidance, not present operational proof (lines 289–325). Canonical source stem: `source-adyen-docs-payment-methods-ideal-react-native-component`.
