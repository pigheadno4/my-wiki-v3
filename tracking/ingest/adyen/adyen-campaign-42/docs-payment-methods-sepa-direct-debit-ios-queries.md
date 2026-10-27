# Fixed-query evidence — SEPA Direct Debit iOS

Canonical source stem: `source-adyen-docs-payment-methods-sepa-direct-debit-ios`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-sepa-direct-debit-ios]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 page is an **iOS route selector** for SEPA Direct Debit: it links Drop-in and `SEPADirectDebitComponent` child guides (raw lines 15–27). It supplies no request fields, SDK/API minimum, mandate procedure, transaction outcome, capture or settlement evidence, and does not prove merchant eligibility or a successful debit (raw lines 15–36). Method-level duties and payment lifecycle require the separate SEPA overview and selected child guide.

## Q2 — Central capability, prerequisites, and warnings

The chooser describes Drop-in as the all-in-one UI route and Components as the `SEPADirectDebitComponent` route (raw lines 19–27). It explicitly says to build the **main integration first**, linking all four iOS combinations of Sessions/Advanced with Drop-in/Components (raw lines 29–36). Those links are navigation, not proof that either child guide has identical configuration, request requirements or outcomes.
