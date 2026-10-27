# docs-payment-methods-ach-direct-debit-ios — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-ach-direct-debit-ios]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-ach-direct-debit-ios]] is a 2026-09-15 ACH iOS integration chooser, pointing to Drop-in and `ACHDirectDebitComponent` child guides (raw lines 15–27). It gives no method-specific request fields, SDK version, bank-verification procedure, mandate collection, outcome flow or payment-success evidence. The related [[source-adyen-docs-payment-methods-ach-direct-debit|ACH overview]] states the method-level US-entity, consumer validation, SEC/mandate and asynchronous reversal conditions, which this chooser does not implement (overview raw lines 23–29, 35–74). Directory links and this historical snapshot do not establish current eligibility or a successful debit (this raw lines 2, 11, 19–36).

## Q2 — What central capability, prerequisites, and warnings are stated?

The chooser offers all-in-one iOS Drop-in or an iOS Components route using `ACHDirectDebitComponent` (raw lines 19–27). It instructs readers to build the main integration before adding ACH and links separate iOS Drop-in/Components guides for both Sessions and Advanced flows (raw lines 29–36). Select the matching base and child guide for actual setup and outcomes; this page cannot be used alone to infer bank authorization, valid mandate, settlement or merchant account activation (raw lines 15–36; overview raw lines 25–29, 35–74).
