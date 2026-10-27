# docs-payment-methods-pad-web — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pad-web]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-pad-web]] is a 2026-09-15 PAD Canada Web integration chooser for Drop-in or `PreAuthorizedDebitCanada` Components, not a full method or base-flow guide (raw lines 15–36). It gives no request fields, component options, mandate procedure, delayed-outcome handling or live activation proof. The related [[source-adyen-docs-payment-methods-pad|PAD overview]] requires merchant-held mandate consent before any debit and describes non-real-time authorization and chargeback risk (overview raw lines 23–60); those are separate method-level facts, not implementation steps on this chooser. A link does not prove current merchant enablement or successful payment (this raw lines 2, 11, 19–36).

## Q2 — What central capability, prerequisites, and warnings are stated?

The page routes to Web Drop-in as the all-in-one UI or Web Components using `PreAuthorizedDebitCanada` (raw lines 19–27). It says to build the main integration first and links four paths: Drop-in/Components under Sessions and Advanced server-side flows (raw lines 29–36). Select the matching child and base guide for configuration, mandate and outcome requirements; the overview separately states the Canadian-account eligibility and merchant agreement responsibilities (overview raw lines 23–31, 33–51). This chooser alone cannot establish final bank authorization or funds receipt (this raw lines 15–36; overview raw lines 53–60).
