---
title: "Braintree APAC Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/apac/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, apac, payment-methods, cards, digital-wallets, currencies, merchant-accounts]
---

## Overview

This collected Braintree APAC-path article is an account-scoped retrieval route for default card acceptance, separately arranged American Express processing, qualified alternative payment methods and merchant-account currency handling. The page was collected on 2026-09-16; it does not establish current regional support, merchant enablement, account eligibility, fixed pricing or successful payment execution.

## Key takeaways

- The article says the account accepts Visa and Mastercard by default. American Express is available only to merchants domiciled in Hong Kong and Singapore, is not configured by default, and requires the merchant to apply directly to Amex. Amex manages funding, descriptors, chargebacks and technical support for that route.
- American Express carries separate account, currency and commercial prerequisites: Braintree charges a per-transaction fee in addition to Amex-assessed processing fees; setup requires Service Establishment Numbers and their corresponding currencies; and gateway enablement depends on Amex pricing having been included in the original pricing agreement or completion of a separate pricing form. These snapshot statements do not prove approval or the terms for an individual merchant.
- The alternative-method statements are modal and conditional. The article says most merchants can link PayPal Business Account credentials through the Braintree Control Panel, most merchants with an iOS app can enable Apple Pay for eligible customers using iOS devices, and most merchants can enable Google Pay for eligible customers using Android devices. Linked integration guides remain separate authorities for implementation and current eligibility.
- Secure Remote Commerce is described here as a limited release for eligible merchants in Hong Kong, Malaysia and Singapore. Separate collected Braintree authority contains an unresolved conflict between current-tense limited-release language and a January 20, 2026 end-of-support notice for Visa Click to Pay/SRC; do not treat this page's sentence as proof of current support.
- Transactions use the currency associated with the merchant account. When the customer's bank-account currency differs, the bank converts the charge and may assess conversion or other fees; the article warns that refunds become more difficult and chargebacks may increase. Direct charging in another supported currency requires an additional merchant account, guidance on applicable presentment and settlement currencies, and an integration update to specify the new merchant account ID after setup.

> [!warning] APAC, account and snapshot scope are material
> Keep the default-card statement, Amex domicile and account requirements, alternative-method qualifications and currency setup scoped to this collected APAC-path article. "Most," "eligible," "only available" and "limited release" are conditions, not guarantees. Collection and configuration are not proof of present availability, approval, authorization, capture, settlement, funding or refund success.

> [!warning] Secure Remote Commerce support status is unresolved
> This article's limited-release statement conflicts with the collected dedicated SRC and provider-wide pages' January 20, 2026 end-of-support notice for Visa Click to Pay/SRC. Preserve both statements and verify current merchant, region, SDK and account support with Braintree before implementation.

## Detail locators

- Default Visa and Mastercard acceptance: `## Card types`, raw lines 17-24.
- American Express Hong Kong/Singapore domicile boundary, non-default configuration, direct-account requirement and Amex-owned responsibilities: `### American Express`, raw lines 26-36.
- Separate Braintree and Amex fees: `#### Fees`, raw lines 39-41.
- Service Establishment Number and corresponding-currency setup plus original-pricing-agreement prerequisite: `#### Setup`, raw lines 44-50.
- Modal PayPal, Apple Pay and Google Pay setup and customer/device conditions: `## Alternative payment methods`, raw lines 55-70.
- Secure Remote Commerce limited-release, eligible-merchant and Hong Kong/Malaysia/Singapore wording: `### Secure Remote Commerce`, raw lines 73-75.
- Merchant-account currency processing, customer-bank conversion, possible fees and refund/chargeback warning: `## Currencies`, raw line 80.
- Additional-currency merchant account, presentment/settlement guidance and merchant-account-ID integration update: `## Currencies`, raw lines 82-84.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]
- Dedicated SRC support-status route: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/apac/transactions/accepted-payment-methods-2026-09-16|Braintree APAC Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering default cards, separately arranged American Express, qualified alternative methods and merchant-account currency handling
