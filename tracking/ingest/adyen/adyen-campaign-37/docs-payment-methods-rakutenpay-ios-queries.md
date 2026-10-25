# docs-payment-methods-rakutenpay-ios — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a **Rakuten Pay iOS navigation chooser**, linking Drop-in and `InstantPaymentComponent` child pages plus four iOS Sessions/Advanced base guides (source-adyen-docs-payment-methods-rakutenpay-ios; raw lines 15–36). It does not state API/SDK minima, method-specific setup, recurring model approval or any final payment outcome (raw lines 19–36).

Q2. What is its central capability, prerequisite and warning?

The page describes Drop-in as an all-in-one UI choice and Components through `InstantPaymentComponent`, then directs the reader to build the relevant main iOS Sessions or Advanced integration before adding Rakuten Pay (raw lines 21–36). These are route labels; use the child and base guides for redirect, configuration, testing, recurring restrictions and result handling. This page alone cannot prove merchant eligibility or authorization (raw lines 19–36).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-ios]] → [[raw/adyen/docs/payment-methods/rakutenpay/ios/2026-09-15]].
