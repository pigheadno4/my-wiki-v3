---
title: "Braintree Moneris Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/moneris/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, moneris, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected Braintree Moneris-path article is an account-scoped retrieval route for default Visa and Mastercard acceptance, separately arranged American Express processing, qualified PayPal and wallet availability, and USD/CAD currency handling. The page body records an update time of 2025-04-01 and was collected on 2026-09-16. It is Braintree-hosted snapshot evidence, not independent Moneris or American Express authority and not proof of current support, an individual merchant's configuration, pricing, approval, buyer eligibility or successful payment execution.

## Key takeaways

- The article says the account accepts Visa and Mastercard by default. American Express is not configured by default and requires the merchant to apply directly to Amex; Amex manages funding, descriptors, chargebacks and technical support for those transactions.
- American Express has separate account, currency and commercial prerequisites. Braintree charges a per-transaction fee in addition to Amex-assessed processing fees. Setup requires the merchant's Service Establishment Numbers and their corresponding currencies. Gateway enablement also depends on Amex pricing having been specified in the original pricing agreement; otherwise, the page says Braintree will provide an Amex pricing agreement form to complete and sign. These statements do not establish approval, actual fees or contract terms for an individual merchant.
- Alternative-method availability is modal and conditional. The article says most merchants can accept PayPal by entering PayPal Business Account credentials in the Braintree Control Panel; most merchants can enable Google Pay for eligible customers using Android devices; and most merchants with an iOS mobile app can enable Apple Pay for eligible customers using iOS devices.
- The article calls Secure Remote Commerce (SRC) currently available in limited release for eligible merchants. A separately collected Braintree SRC guide, however, says Visa Click to Pay (SRC) would no longer be supported effective 2026-01-20 while also retaining current-tense limited-release language. The 2026-09-16 snapshots do not resolve that support-status conflict; consult [[source-braintree-payment-methods-secure-remote-commerce]] rather than treating this article as current availability proof.
- Transactions use the currency associated with the merchant account, and the customer's bank converts when its account currency differs. The page offers USD or CAD presentment and settlement but requires the selected presentment and settlement currencies to match. This account-scoped statement does not establish current currency coverage for another processor, region or merchant.

> [!warning] Moneris-path account, time and eligibility scope are material
> Keep the card defaults, Amex setup and pricing prerequisites, alternative-method statements, and USD/CAD behavior scoped to this collected Moneris-path account article. "Most merchants," "eligible customers," device conditions, limited-release wording and account configuration are qualifications, not guarantees. Do not use this Braintree-hosted page as independent processor or card-network authority.

> [!warning] Setup documentation is not execution evidence
> Account configuration, credential entry, application, pricing-form completion, card listings and enablement language do not prove present support, approval, authorization, capture, settlement, funding, dispute handling, refund success or any individual transaction outcome.

## Detail locators

- Default Visa and Mastercard acceptance: `## Card types`, raw lines 17-23.
- Non-default Amex configuration, direct-account application and Amex-owned funding, descriptors, chargebacks and support: `### American Express`, raw lines 26-30.
- Separate Braintree and Amex fees: `#### Fees`, raw lines 33-35.
- Service Establishment Number and corresponding-currency setup: `#### Setup`, raw lines 38-40.
- Original-pricing-agreement prerequisite or separate signed pricing form: `#### Setup > **NOTE**`, raw lines 43-44.
- Modal PayPal Business Account credential route: `## Alternative payment methods > ### PayPal`, raw lines 49-54.
- Qualified Google Pay eligible-customer and Android-device wording: `### Google Pay`, raw lines 57-59.
- Qualified Apple Pay iOS-app, eligible-customer and iOS-device wording: `### Apple Pay`, raw lines 62-64.
- SRC limited-release and eligible-merchant wording: `### Secure Remote Commerce`, raw lines 67-69.
- Merchant-account currency processing, customer-bank conversion, USD/CAD options and same-currency presentment/settlement requirement: `## Currencies`, raw lines 72-74.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency context: [[braintree-currencies]]
- SRC support-status conflict: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]

## Raw Sources

- [[raw/braintree/articles/moneris/transactions/accepted-payment-methods-2026-09-16|Braintree Moneris Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering account-default cards, separately arranged American Express, qualified alternative methods and USD/CAD currency handling
