---
title: "Braintree AIB AF Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/aib-af/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, aib-af, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected [[braintree]] article under the AIB AF path is an account-scoped retrieval route for default and separately enabled card types, qualified alternative payment methods, and merchant-account currency behavior. It was collected on 2026-09-16 and is Braintree-hosted snapshot evidence, not independent current bank authority, an AIB BF source, or proof of present merchant enablement, buyer eligibility, pricing, or successful payment execution.

## Key takeaways

- The article says the account is set up by default to accept Visa, Mastercard, and Maestro. Keep that list within this captured AIB AF account article rather than treating it as universal Braintree or bank support.
- American Express is not configured by default. A merchant seeking Amex acceptance must apply for its own account directly through Amex; the article assigns Amex funding, descriptors, chargebacks, and technical support to Amex. It says Braintree charges a per-transaction fee in addition to Amex-assessed processing fees and that Amex provides a separate statement for its fees. Setup requires the merchant's Service Establishment Numbers and corresponding currencies, plus confirmation that Amex pricing was in the original pricing agreement or completion and signature of a separate Amex pricing form.
- Maestro acceptance is conditional. The article says 3D Secure is not enabled automatically; a same-country-issued Maestro card can be used for one-time or recurring payments without 3D Secure, while enabling 3D Secure gives more flexibility for cards from other countries but prevents recurring billing with Maestro. Regardless of 3D Secure status, it says never to create a Maestro transaction by entering the card number directly in the Control Panel because such a transaction may initially appear to settle but will eventually be rejected.
- JCB is not enabled by default and is described as available in many supported presentment currencies. Discover and Diners Club are limited to EUR, GBP, and USD, are not enabled by default, and Diners Club is processed as Discover. These are article-scoped availability statements, not current eligibility guarantees.
- Alternative-method availability remains qualified: PayPal is described for most merchants using PayPal Business Account credentials in the Control Panel; Apple Pay for most merchants with an iOS app and eligible customers; Google Pay for most merchants and eligible customers using Android devices; and Secure Remote Commerce as a limited release for eligible merchants in certain EU locations. Linked method guides were not read for this entry and are navigation only.
- Transactions use the currency associated with the merchant account, with the customer's bank converting when its account currency differs. The article warns of possible conversion or other bank fees and more difficult refunds that can increase chargebacks. Charging directly in another supported currency requires an additional merchant account, guidance on applicable presentment and settlement currencies, and an integration update to select the new merchant account ID.

> [!warning] AIB AF and account qualifications are material
> Do not transfer the listed card brands, Amex setup and pricing prerequisites, Maestro behavior, alternative-method availability, or currency behavior to AIB BF, another processor, region, or merchant account. Terms such as `most`, `eligible`, `many`, and `limited release` are conditions, not guarantees.

> [!warning] Maestro Control Panel and recurring constraints
> The captured article says Maestro recurring billing cannot be used when 3D Secure is enabled and that a Maestro transaction created by direct card-number entry in the Control Panel will eventually be rejected even if it initially appears to settle.

> [!warning] Setup documentation is not execution evidence
> Account configuration, supported-method wording, and integration instructions do not establish authorization, capture, settlement, funding, conversion, refund outcome, or successful processing of an individual transaction.

## Detail locators

- Default Visa, Mastercard, and Maestro card list: `## Card types`, raw lines 17-24.
- Non-default Amex account requirement and Amex-owned operational responsibilities: `### American Express`, raw lines 27-31.
- Braintree and Amex fee split: `#### Fees`, raw lines 34-36.
- Service Establishment Number, corresponding-currency, and original-pricing-agreement prerequisites: `#### Setup`, raw lines 39-45.
- 3D Secure enablement, same-country card, cross-country flexibility, recurring-billing, and Control Panel rejection qualifications for Maestro: `### Special note on Maestro`, raw lines 50-58.
- JCB presentment-currency and non-default-enable conditions: `### JCB cards`, raw lines 61-63.
- Discover and Diners Club currency limits, processing identity, and non-default-enable conditions: `### Discover and Diners Club cards`, raw lines 66-68.
- PayPal Business Account credential route and qualified Apple Pay and Google Pay availability: `## Alternative payment methods`, raw lines 71-86.
- Secure Remote Commerce limited-release, merchant-eligibility, and EU-location qualifications: `### Secure Remote Commerce`, raw lines 89-91.
- Merchant-account currency, customer-bank conversion, possible fees, and refund/chargeback warning: `## Currencies`, raw lines 94-96.
- Additional-currency merchant account, presentment/settlement guidance, and merchant-account-ID integration step: `## Currencies`, raw lines 98-100.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/guides/3d-secure/overview-2026-09-16|Braintree 3D Secure overview]]
- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/aib-af/transactions/accepted-payment-methods-2026-09-16|Braintree AIB AF Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering default and separately enabled cards, Maestro 3D Secure constraints, qualified alternative methods, and merchant-account currency behavior
