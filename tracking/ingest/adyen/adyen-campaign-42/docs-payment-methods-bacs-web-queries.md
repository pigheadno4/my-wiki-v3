# docs-payment-methods-bacs-web — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bacs-web]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-bacs-web]] is the 2026-09-15 BACS Web chooser for Drop-in or `BacsDirectDebit` Components, not a full integration or DDI/mandate guide (raw lines 15–36). It contains no request fields, version floor, notice timing or payment-outcome steps. The [[source-adyen-docs-payment-methods-bacs|BACS overview]] gives the shopper DDI and four-to-six-day clearing/settlement context plus undefendable chargeback risk (overview raw lines 23–27, 60–74); these are distinct from this chooser's links. A directory link cannot establish a valid DDI, current activation or successful funds receipt (this raw lines 2, 11, 19–36).

## Q2 — What central capability, prerequisites, and warnings are stated?

The page offers Web Drop-in as an all-in-one UI or the `BacsDirectDebit` Web Components route (raw lines 19–27). It instructs readers to create their main integration first, and links Web Drop-in and Web Components under both Sessions and Advanced flows (raw lines 29–36). Select the matching child and base guide for version, fields, tokenization and outcomes; the BACS overview separately describes shopper agreement/DDI, notice/chargeback risk and delayed settlement (overview raw lines 23–27, 35–74). This chooser alone is not evidence of a completed debit (this raw lines 15–36).
