---
title: "Payment methods for Adyen for Platforms | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payment-methods"
raw_files:
  - "adyen/docs/platforms/payment-methods/2026-09-15.md"
tags: [adyen, platforms, payment-methods, ecommerce, point-of-sale]
---

## Overview

This Adyen for Platforms page is a dated catalog of payment methods and variants that the platform documentation lists for ecommerce and/or point of sale. It says payment methods are configured per store: onboarding sets the methods users can accept, while users onboarded by invitation already have default methods and can request additional ones through Customer Area or Management API. A table entry indicates documented support for a channel, not current country/currency eligibility, merchant approval, store configuration, method activation, or a successful payment. [[adyen]] [[adyen-platforms]] [[adyen-payment-method-variants]]

## Key takeaways

- The pinned 2026-09-15 table lists method names, variants, ecommerce/POS indicators and method-specific notes. The indicators differ by variant and channel: for example, Pay Now (`paynow`) is listed for ecommerce and Pay Now POS (`paynow_pos`) for POS, both with SGD; WeChat Pay has separate `wechatpay` and `wechatpay_pos` rows. Use the exact raw row when checking a method rather than assuming a name is enabled on both channels.
- Notes qualify individual entries with additional Management API parameters, shopper-interaction settings, specified currencies, store geography, or approval through an Adyen contact. Examples include Cartes Bancaires only for a France-located store; Pay by Bank (Europe) with EUR/GBP and approval; ACH Direct Debit and SEPA Direct Debit requiring approval; and SEPA Direct Debit available only through Management API. These examples do not replace each method's own setup or regional requirements.
- A footnote on marked ecommerce methods says they do not support aggregated acquiring accounts for payment facilitators. For users who want to accept such a method, the page calls for business lines and stores in the merchant account. This is a conditional structural prerequisite, not evidence that any particular platform uses a payment-facilitator model or that the user's method is active.
- The page links onward to Management API and Customer Area request/manage guides. It does not itself state API credential roles, account-holder capability checks, request rate/quantity limits, activation timing or response status semantics; consult those operational guides and account state for a specific request.

## Detail locators

- Per-store onboarding/default/request routes: pinned raw lines 15–23 (introduction).
- Full method/variant and ecommerce/POS support table, including method-specific parameters, countries, currencies and approval: pinned raw lines 25–76 (`## Supported payment methods`).
- Payment-facilitator aggregated-acquiring restriction and business-line/store consequence for footnoted methods: pinned raw line 78.
- Management API and Customer Area management routes: pinned raw lines 80–88 (`## Next steps`).

## Related

- [[adyen-platforms]] — provider platform/store context.
- [[adyen-payment-method-variants]] — variant-code concept; a variant alone does not prove setup eligibility.
- [[source-adyen-docs-platforms-payment-methods-api]] — separate Management API request/manage guide for operational details.

## Raw Sources

- [[raw/adyen/docs/platforms/payment-methods/2026-09-15|Adyen for Platforms payment-method catalog — 2026-09-15 snapshot]]
