---
title: "Braintree Wells IC Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/wells-ic/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, wells-ic, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected Braintree Wells IC article is an account-scoped retrieval route for accepted card types, qualified alternative payment methods, American Express account choices, merchant-account currency behavior and billing-address guidance. The page was collected on 2026-09-16; it is Braintree-hosted Wells IC documentation, not current independent bank policy, not a Wells Flat source and not proof of merchant enablement, buyer eligibility, pricing for an individual account or successful payment execution.

## Key takeaways

- The article says the account is configured for Visa, Mastercard, American Express, Discover/Diners Club and JCB when the card does not require a PIN or password; Diners Club cards are processed as Discover. Keep that list and its condition scoped to this Wells IC article and account context.
- For merchants processing less than $1 million in annual American Express volume, the page presents Braintree's aggregated Amex as enabled by default but warns of less descriptor flexibility. As an alternative, a merchant can apply directly to Amex; under that option, Amex manages funding, descriptors and chargebacks and is the support contact for those issues. The snapshot does not establish eligibility, approval or current pricing for an individual merchant.
- The alternative-method section is conditional: it says most merchants can accept the listed methods and directs Braintree Marketplace merchants to contact Braintree about their available methods. PayPal requires PayPal Business Account credentials in the Control Panel; ACH Direct Debit is for eligible US merchants; Apple Pay requires an iOS app and eligible customers; Google Pay is for eligible customers using Android devices; and Venmo is limited to select US merchants and customers using a personal Venmo account on iOS or Android.
- Samsung Pay is stated as deprecated. A separate adjacent notice says "This guide has been deprecated" and redirects to the Pay Later offers guide, but the captured text does not identify the notice's antecedent; do not infer that the entire accepted-payment-methods article or another named method is deprecated from that sentence alone. Secure Remote Commerce is separately described as a limited release for eligible US merchants.
- Transactions are processed in the merchant-account currency, with the customer's bank converting when its account currency differs. The bank may charge conversion or other fees, and the article warns of more difficult refunds and potentially more chargebacks. Direct charging in another supported currency requires an additional merchant account, Customer Success guidance on applicable presentment and settlement currencies, and an integration update to specify the new merchant account ID.
- The page recommends passing billing-address information when storing payment methods or creating transactions, with postal code at minimum. It says this can help authorization likelihood and avoid interchange downgrades or additional fees; it does not guarantee authorization or a particular price.

> [!warning] Wells IC, account and support scope are material
> Do not transfer the card list, aggregated-Amex threshold/default, direct-Amex responsibility split, wallet availability, currency setup or billing-address effects to Wells Flat, another processor, another region or an individual merchant account. "Most," "eligible" and "select" are conditions, not availability guarantees; the captured support ownership is specific to the direct-Amex option described by this page.

> [!warning] Setup and snapshot evidence are not execution proof
> Account configuration, credentials, method listings and integration instructions do not establish authorization, capture, settlement, funding, refund success or present-day availability for any transaction. Bank conversion fees, interchange effects and chargeback risk are qualified possibilities, not fixed pricing outcomes.

## Detail locators

- Account card list, PIN/password condition and Diners Club processing identity: `## Card types`, raw lines 17-28.
- Aggregated Amex annual-volume threshold, default enablement and descriptor limitation: `### Special note on American Express`, raw line 33.
- Direct Amex account alternative and Amex-owned funding, descriptors, chargebacks and support: `### Special note on American Express`, raw line 35.
- General alternative-method and Marketplace qualifications: `## Alternative payment methods`, raw line 40.
- PayPal Business Account credential requirement: `### PayPal`, raw lines 43-45.
- ACH, Apple Pay, Google Pay and Venmo merchant, region, app/device and customer qualifications: raw lines 48-65.
- Samsung Pay deprecation and the adjacent ambiguous guide-deprecation redirect: raw lines 68-74.
- Secure Remote Commerce limited-release, eligible-merchant and US conditions: raw lines 79-81.
- Merchant-account currency, bank conversion, possible fees and refund/chargeback warning: `## Currencies`, raw line 86.
- Additional-currency merchant account, presentment/settlement guidance and merchant-account-ID integration update: `## Currencies`, raw lines 88-90.
- Billing-address recommendation, postal-code minimum and qualified authorization/interchange effects: `### Billing address`, raw lines 93-95.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/wells-ic/transactions/descriptors-2026-09-16|Braintree Wells IC transaction descriptors article]]
- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/ach-2026-09-16|Braintree ACH Direct Debit guide]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/venmo-2026-09-16|Braintree Venmo guide]]
- [[raw/braintree/articles/guides/payment-methods/paypal-pay-later-offers-2026-09-16|Braintree Pay Later offers guide]]
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/transactions/accepted-payment-methods-2026-09-16|Braintree Wells IC Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering account-scoped cards, qualified alternative methods, American Express account choices, currency setup and billing-address guidance
