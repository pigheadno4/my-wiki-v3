---
title: "Braintree NAB Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/nab/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, nab, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected Braintree NAB-path article is an account- and processor-scoped retrieval route for default Visa and Mastercard acceptance, separately arranged American Express processing, qualified PayPal and wallet availability, and merchant-account currency handling. The page body records an update time of 2025-04-02 and was collected on 2026-09-16. It is Braintree-hosted snapshot evidence, not independent NAB or American Express authority and not proof of present support, an individual merchant's configuration, pricing, approval, buyer eligibility or successful payment execution.

## Key takeaways

- The article says the account accepts Visa and Mastercard by default. American Express is not configured by default and requires the merchant to apply directly to Amex; Amex manages funding, descriptors, chargebacks and technical support for those transactions.
- American Express has separate commercial and setup conditions: Braintree states that it charges a per-transaction fee in addition to Amex-assessed processing fees; setup requires Service Establishment Numbers and their corresponding currencies; and gateway enablement depends on Amex pricing having been included in the original pricing agreement or completion and signature of a separate pricing form. These statements do not establish an individual merchant's approval, actual fees or contract terms.
- Alternative-method availability remains qualified. The article says most merchants can accept PayPal by entering PayPal Business Account credentials in the Braintree Control Panel; most merchants with an iOS mobile app can enable Apple Pay for eligible customers using iOS devices; and most merchants can enable Google Pay for eligible customers using Android devices. It describes Secure Remote Commerce as a limited release for eligible merchants located in Australia and New Zealand.
- Transactions are processed in the currency associated with the merchant account, with the customer's bank converting when its account currency differs. The page warns that the customer may incur conversion or other bank fees and that refunds may become more difficult, which can increase chargebacks. Reducing that friction requires requesting an additional merchant account, determining applicable presentment and settlement currencies with Customer Success, and updating the integration to specify the additional merchant account ID. The article does not enumerate currencies or establish current account eligibility.

> [!warning] Secure Remote Commerce support status is unresolved across collected pages
> This article uses current-tense limited-release language for eligible merchants in Australia and New Zealand. The separately collected Braintree SRC guide says Visa Click to Pay (SRC) would no longer be supported effective 2026-01-20 while also retaining current-tense limited-release language. The snapshots do not resolve the conflict; consult [[source-braintree-payment-methods-secure-remote-commerce]] rather than treating this article as present availability proof.

## Detail locators

- Default Visa and Mastercard acceptance: `## Card types`, raw lines 17-23.
- Non-default Amex configuration, direct application, and Amex-managed funding, descriptors, chargebacks and technical support: `### American Express`, raw lines 26-30.
- Separate Braintree and Amex fees: `#### Fees`, raw lines 33-35.
- Service Establishment Numbers and corresponding-currency setup: `#### Setup`, raw line 40.
- Original-pricing-agreement prerequisite or separate signed pricing form: `#### Setup > **NOTE**`, raw lines 43-44.
- Qualified PayPal, Apple Pay and Google Pay availability: `## Alternative payment methods`, raw lines 49-64.
- SRC limited-release, eligible-merchant and Australia/New Zealand wording: `### Secure Remote Commerce`, raw lines 67-69.
- Merchant-account currency processing, customer-bank conversion, fee/refund/chargeback warnings, additional-account request and merchant-account-ID integration step: `## Currencies`, raw lines 72-78.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency context: [[braintree-currencies]]
- SRC support-status conflict: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/nab/transactions/accepted-payment-methods-2026-09-16|Braintree NAB Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering account-default cards, separately arranged American Express, qualified alternative methods and merchant-account currency handling
