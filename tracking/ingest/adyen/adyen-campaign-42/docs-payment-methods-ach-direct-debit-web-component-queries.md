# Fixed-query evidence — ACH Direct Debit Web Component

Canonical source stem: `source-adyen-docs-payment-methods-ach-direct-debit-web-component`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-ach-direct-debit-web-component]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 source is a method-specific ACH Direct Debit add-on for **existing Web Components** Sessions and Advanced integrations (raw lines 15–25, 121–131). It does not establish present US-entity/merchant eligibility, consumer validation, B2B bank allowlisting, mandate validity, token creation or funded payment. Its no-extra-request-field statements do not waive method-level authorization/SEC duties (raw lines 44, 186; ACH overview source). An accepted request can precede the bank's decision by up to five business days (raw lines 97–101, 190–194).

## Q2 — Central capability, prerequisites, and warnings

Sessions needs Checkout API v68+, change-of-bank-details webhook subscription and Customer Area method setup; Advanced repeats the webhook/setup but does not state the same API minimum (raw lines 29–38, 123–131). The `Merchant allow bank-refund` role is conditional on **issuing a refund**, not taking payments (raw lines 34–35, 128–129). Both flows import `Ach` and list optional UI flags, including `enableStoreDetails` on Web v5.24.0+ for a save-details checkbox, default false; neither flow adds ACH-specific request fields (raw lines 40–93, 133–186). Example initialization/configuration snippets are visibly incomplete or mislabeled (raw lines 70–93, 157–179). The guide says the bank's authorization decision may take up to five business days after request receipt; it points to settlement reporting if authorized and a `CHARGEBACK` webhook if bank authorization fails (raw lines 99–101, 192–194). Test account/routing data and `chargeback:R01` owner-name trigger are test-only (raw lines 103–119, 196–212).
