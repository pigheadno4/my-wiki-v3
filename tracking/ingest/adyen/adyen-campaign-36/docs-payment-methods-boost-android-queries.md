# docs-payment-methods-boost-android retrieval queries

Canonical source: [[source-adyen-docs-payment-methods-boost-android]] (`wiki/sources/adyen/source-adyen-docs-payment-methods-boost-android.md`).
Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-android]] → [[raw/adyen/docs/payment-methods/boost/android/2026-09-15|pinned raw]].

## Q1 — What is the purpose and scope, and what cannot be inferred?

This is an Android integration chooser for Boost Wallet, linking Drop-in and Components child guides and four main Sessions/Advanced Android guides (raw lines 15–36). It does not provide a checkout payload, SDK/API minimum, merchant eligibility or an observed payment outcome. Those details belong to the child/main guides and method overview. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-android]] → pinned raw above.

## Q2 — What central capability, prerequisites and warnings matter?

The chooser describes Drop-in as an all-in-one UI solution and the Components route as using `InstantPaymentComponent` to handle the Boost Wallet redirect (raw lines 19–27). It tells the merchant to create the main Android integration before adding Boost, then points to Sessions and Advanced guides for both UI approaches (raw lines 29–36). Redirect navigation is not proof of a shopper return or final authorization, capture, settlement or refund. The chooser does not state country/currency, TEST/LIVE rules or version requirements (raw lines 15–36). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boost-android]] → pinned raw above.
