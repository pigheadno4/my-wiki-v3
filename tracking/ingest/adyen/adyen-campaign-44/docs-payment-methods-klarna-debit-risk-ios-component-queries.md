# C44 Klarna Debit Risk iOS Component retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-debit-risk-ios-component`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna-debit-risk/ios-component/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-debit-risk-ios-component]]` → `[[raw/adyen/docs/payment-methods/klarna-debit-risk/ios-component/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does this iOS page add, and what must not be inferred from its snippets?

**Answer path:** The source entry points to the Klarna Debit Risk add-on for existing iOS Components, not consumer Klarna financing. Raw `## Sessions flow Component` lines 25–73 and `## Advanced flow Component` lines 1084–1131 define separate prerequisites and redirect handling. Sessions states Checkout API v68+; the Advanced table does not. Both initialization snippets use `None` and undefined `directEbankingConfiguration`, so they do not establish a working Component API. The page gives no merchant enablement, deployment or payment-outcome proof.

## Q2 — central capability, prerequisites and warnings

**Query:** How does Klarna Debit Risk recurring work on iOS, and which caveats affect token creation and reuse?

**Answer path:** Read `## Recurring payments` at raw lines 75–108 and 1132–1165 for SEPA Direct Debit tokenization, explicit-permission recommendation and `/payments` field table. `recurring.token.created` provides the stored ID at lines 456–457 and 1513–1514. `### Make a payment with a token` at lines 458–462 and 1515–1519 restricts reuse to shopper-absent Subscription or UnscheduledCardOnFile; the corresponding examples use `sepadirectdebit`, `storedPaymentMethodId` and `ContAuth`. The table's `Ecommerce` description conflicts with token-creation sample `ContAuth`; the source entry flags it. TEST and live setup are at lines 1076–1082 and 2133–2139. Do not infer a token or settled payment from a request example.
