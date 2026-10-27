# C42 fixed retrieval queries — docs-payment-methods-bacs-ios

**Q1. What purpose/scope does this page serve, and what cannot be inferred?**
The 2026-09-15 `docs/payment-methods/bacs/ios` snapshot is an iOS integration chooser: it links Drop-in and `BACSDirectDebitComponent` children, then four general Sessions/Advanced iOS base guides (raw lines 15-36). It gives no BACS request schema, mandate implementation, token rules or payment outcome. A linked base flow does not prove account enablement or cleared funds. Route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-bacs-ios]].

**Q2. What are the central capability, prerequisites and warnings?**
Choose the child Drop-in guide for the all-in-one UI or the child Components guide for `BACSDirectDebitComponent` (raw lines 19-27). The page directs integrators to establish the main iOS Drop-in/Components Sessions or Advanced flow before adding BACS (raw lines 29-36). The child guides and method overview are the routes for method-specific fields, Direct Debit Instruction, delayed clearing, advance notice and chargeback terms; this chooser is navigation only (raw lines 15-36). Route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-bacs-ios]].
