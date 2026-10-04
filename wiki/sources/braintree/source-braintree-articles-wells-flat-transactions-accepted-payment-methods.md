---
title: "Braintree Wells Flat Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/wells-flat/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, wells-flat, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected Braintree Wells Flat article is an account-scoped retrieval route for accepted card types, qualified alternative payment methods and merchant-account currency behavior. The page was collected on 2026-09-16; it is Braintree-hosted snapshot evidence, not a current Wells Fargo, provider-wide or Wells IC support guarantee and not proof of merchant enablement, buyer eligibility, pricing or successful payment execution.

## Key takeaways

- The article says the account is configured for Visa, Mastercard, American Express, Discover/Diners Club and JCB when the card does not require a PIN or password; Diners Club cards are processed as Discover cards. Keep this list scoped to the captured Wells Flat account article rather than treating it as universal Braintree or bank support.
- For merchants processing less than $1 million in annual American Express volume, the article presents Braintree aggregated Amex as the default-enabled route but warns that descriptor flexibility is reduced. A merchant may instead apply directly to Amex, in which case Amex manages funding, descriptors and chargebacks and provides support for those issues. The captured threshold and account configuration are not current eligibility or pricing guarantees.
- Alternative-method availability is conditional: the page says most merchants can accept several listed methods, directs Braintree Marketplace merchants to contact Braintree, limits ACH Direct Debit to eligible US merchants, qualifies Apple Pay and Google Pay by app/device and customer eligibility, limits Venmo to select US merchants and personal-account users on iOS or Android, and describes Secure Remote Commerce as a limited release for eligible US merchants.
- The page marks Samsung Pay as deprecated. A nearby warning also says "this guide" is deprecated and redirects readers to the Pay Later offers guide without clearly identifying the guide to which that warning applies. Preserve that ambiguity; do not infer a current replacement or support status from the snapshot.
- Transactions use the currency associated with the merchant account, with the customer's bank converting when its account currency differs. The page warns of possible customer bank fees and more difficult refunds that may increase chargebacks. Charging directly in another supported currency requires an additional merchant account, guidance on applicable presentment and settlement currencies, and an integration update to select the new merchant account ID.

> [!warning] Wells Flat, account and regional qualifications are material
> Do not transfer the listed card brands, aggregated Amex posture, alternative-method availability, account configuration or currency behavior to Wells IC, another processor, another region or another merchant account. Terms such as "most," "select," "eligible" and "limited release" are conditions, not guarantees.

> [!warning] Setup documentation is not transaction evidence
> Account configuration and setup routes do not establish authorization, capture, settlement, funding, conversion, refund outcome or successful processing of an individual transaction.

## Detail locators

- Account card list, PIN/password exclusion and Diners Club processing identity: `## Card types`, raw lines 17-28.
- Aggregated Amex volume threshold, default-enabled posture and descriptor limitation: `### Special note on American Express`, raw lines 31-33.
- Direct Amex account alternative and Amex-owned funding, descriptors, chargebacks and support: `### Special note on American Express`, raw line 35.
- Marketplace qualification and method-specific applicability: `## Alternative payment methods`, raw lines 38-65 and 79-81.
- Samsung Pay deprecation and ambiguous nearby Pay Later redirect: `### Samsung Pay`, raw lines 68-74.
- Merchant-account currency, customer-bank conversion, possible fees and refund/chargeback warning: `## Currencies`, raw line 86.
- Additional-currency merchant account, presentment/settlement guidance and merchant-account-ID integration step: `## Currencies`, raw lines 88-90.
- Billing-address collection recommendation and authorization-likelihood rationale: `### Billing address`, raw lines 93-95.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/ach-2026-09-16|Braintree ACH Direct Debit guide]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/venmo-2026-09-16|Braintree Venmo guide]]
- [[raw/braintree/articles/guides/payment-methods/paypal-pay-later-offers-2026-09-16|Braintree Pay Later offers guide]]
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/transactions/accepted-payment-methods-2026-09-16|Braintree Wells Flat Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering account-scoped cards, qualified alternative methods, deprecation wording and merchant-account currency behavior
