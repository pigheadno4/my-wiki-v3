---
title: "Braintree Chase Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/chase/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, chase, payment-methods, cards, digital-wallets, currencies]
---

## Overview

This collected Braintree article is a Chase-scoped retrieval route for the account's default card types, separately configured American Express acceptance, qualified PayPal and wallet availability, and currency-account setup. The page was collected on 2026-09-16; it is Braintree-hosted documentation, not independent Chase authority and not proof of current merchant enablement, buyer eligibility or successful payment execution.

## Key takeaways

- The page says the account is set up by default for Visa, Mastercard and Discover/Diners Club, with Discover/Diners Club qualified as US-only and Diners Club processed as Discover. These statements describe the collected Chase article's account scope, not universal payment-method availability.
- American Express is not configured by default. The article requires the merchant to apply for its own Amex account, assigns Amex funding, descriptors, chargebacks and technical support to Amex, and says Braintree charges a per-transaction fee in addition to Amex-assessed processing fees. Setup requires the relevant Service Establishment Numbers and currencies; Braintree must also confirm that Amex pricing was in the original pricing agreement or provide a form to complete and sign.
- PayPal is qualified to most merchants and requires PayPal Business Account credentials in the Braintree Control Panel. Apple Pay is qualified to most Chase merchants with an iOS app and customers in compatible countries; Google Pay is qualified to most merchants and eligible customers using Android devices. The snapshot says Chase supports Visa, Mastercard, Discover and American Express credit cards for both wallets, but it does not establish current or universal merchant, customer, country or device eligibility.
- Transactions use the currency associated with the merchant account, with the customer's bank converting when its account currency differs. The page warns that the bank may charge conversion or other fees and that refunds can become more difficult, increasing chargeback risk. An additional currency requires another merchant account, applicable presentment and settlement guidance, and an integration update to specify the new merchant account ID.
- The article says merchants domiciled in Canada can present and settle only in CAD and cannot use multi-currency setups. This is a qualification from the collected snapshot, not proof of current Canada-wide policy or of eligibility for any individual account.

> [!warning] Chase and account qualifications are material
> Do not transfer the default card list, wallet card support, Amex setup, currency behavior or Canada restriction to another processor, region or merchant account. The page's "most merchants" and "compatible" or "eligible" wording is conditional, not a guarantee of availability.

> [!warning] Setup documentation is not execution evidence
> Account configuration, listed card types and integration instructions do not establish authorization, capture, settlement, funding or successful processing of an individual transaction.

## Detail locators

- Default card types, the US-only Discover/Diners Club qualification and Diners Club processing identity: `## Card types`, raw lines 17-26.
- Non-default Amex account requirement and Amex-owned operational responsibilities: `### American Express`, raw lines 29-33.
- Braintree and Amex fee split: `#### Fees`, raw lines 36-38.
- Service Establishment Number, currency and pricing-agreement prerequisites: `#### Setup`, raw lines 41-47.
- PayPal Business Account credential qualification: `### PayPal`, raw lines 55-57.
- Chase merchant, iOS app, compatible-country and wallet card-brand qualifications: `### Apple Pay`, raw lines 60-62.
- Merchant, eligible-customer, Android-device and wallet card-brand qualifications: `### Google Pay`, raw lines 65-67.
- Merchant-account currency processing, bank conversion and fee/refund/chargeback warning: `## Currencies`, raw line 72.
- Additional-currency merchant account, presentment/settlement guidance and merchant-account-ID integration step: `## Currencies`, raw lines 74-76.
- Canada CAD-only presentment/settlement and unavailable multi-currency setups: final `**NOTE**`, raw lines 79-80.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Currency and merchant-account context: [[braintree-currencies]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]]
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]]
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]]
- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree currencies reference]]

## Raw Sources

- [[raw/braintree/articles/chase/transactions/accepted-payment-methods-2026-09-16|Braintree Chase Accepted Payment Methods article]] - fully read 2026-09-16 snapshot covering default cards, Amex onboarding and responsibilities, qualified PayPal and wallet availability, and currency-account setup
