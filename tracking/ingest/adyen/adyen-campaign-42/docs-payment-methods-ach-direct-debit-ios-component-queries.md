# Fixed-query evidence — ACH Direct Debit iOS Component

Canonical source stem: `source-adyen-docs-payment-methods-ach-direct-debit-ios-component`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-ach-direct-debit-ios-component]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 page is a method-specific ACH Direct Debit add-on for **existing iOS Components** Sessions and Advanced integrations (raw lines 15–25, 92–104). It provides component initialization and test cases and states no additional ACH-specific `/sessions` or `/payments` parameters are needed (raw lines 44, 137); it is not a full base guide, iOS SDK version or payment-outcome lifecycle (raw lines 52–90, 112–161). It cannot establish current merchant/bank eligibility, a signed mandate, account validation, authorized debit or settled funds; the ACH overview is the related authority for those conditions. The change-notice webhook concerns outdated bank details, not payment success (raw lines 37, 103).

## Q2 — Central capability, prerequisites, and warnings

Sessions requires Checkout API v68+, ACH Customer Area setup and change-notice webhook subscription, but adds no method-specific `/sessions` parameters or configuration (raw lines 29–50). Advanced repeats setup/webhook and says no extra ACH configuration or `/payments` fields, without stating the Sessions v68 minimum (raw lines 96–137). Refund roles are stated only for issuing a refund by API or Customer Area (raw lines 34–35, 101–102). Both flows use `ACHDirectDebitComponent` but their Swift snippets leave `configuration:` without a value (raw lines 56–72, 116–131). The Advanced Components prerequisite links to a Drop-in URL despite its label (raw line 100). Test inputs permit correctly formatted account/routing data and `ownerName: chargeback:R01` for a return scenario; that is TEST guidance, not live proof (raw lines 74–90, 139–155).
