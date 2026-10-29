# C44 Klarna retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna]]` → `[[raw/adyen/docs/payment-methods/klarna/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does Adyen's Klarna overview cover, and what cannot be inferred from it?

**Answer path:** The source entry identifies a 2026-09-15 payment-method overview, its three consumer choices and separate Billie B2B row, country/currency/product matrix, portal and integration routes. Raw lines 15–29, 31–40, `## Supported countries/regions` (49–74), `## Klarna Merchant Portal` (76–87), and `## How do you want to integrate?` (93–123) verify scope. The dated snapshot and chooser do not prove present merchant eligibility, approval, a deployed flow, or payment execution; child guides supply implementation requirements.

## Q2 — capability, prerequisites and warnings

**Query:** Which Klarna options, recurring/capture capabilities and operational warnings matter before selecting an integration?

**Answer path:** From the source entry, read the raw product/feature matrix and its numbered notes at lines 23–40, then the exact country/currency/product row in `## Supported countries/regions` (49–74). The shopper chooses Pay later, Pay over time or Pay now; Klarna risk checks precede approval. Recurring varies by product and country, Support contact is specified, Pay over time is limited to long-term subscriptions and multiple partial captures need Support enablement. Raw `## Authorization adjustment` (42–47), `## Klarna Merchant Portal` (76–87) and `## Chargebacks` (89–91) locate adjustment, immutable dispute-email credential and the portal's dispute-management exclusion. The Orders App views order information and edits shipping and billing details (line 83); the page does not say other order fields are editable. Use the related chargeback and adjustment sources for their detailed flows; the overview's matrix alone does not establish capture or dispute outcome.
