---
title: "Braintree AIB BF Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/aib-bf/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, aib-bf, payment-methods, cards, currencies]
---

## Overview

This collected [[braintree]] article at the exact AIB BF route describes account-configured card types, conditions for additional card brands and alternative methods, and merchant-account currency handling. It is a 2026-09-16 snapshot of that Braintree-hosted document variant, not AIB AF evidence, independent current bank or card-network authority, a merchant-specific agreement, or proof that a method is enabled or a payment succeeded.

## Key takeaways

- The article says the account is configured for Visa, Mastercard, Maestro and American Express. Maestro acceptance is conditional: 3D Secure is not automatically enabled; same-country-issued Maestro cards can be accepted for one-time or recurring payments without 3D Secure, while enabling 3D Secure permits more cross-country flexibility but prevents recurring Maestro billing. It says never to enter a Maestro card number directly in the Control Panel because such transactions may appear to settle initially but will eventually be rejected.
- JCB is available in many supported presentment currencies but is not enabled by default. Discover and Diners Club are limited by this page to EUR, GBP and USD, Diners Club is processed as Discover, and neither is enabled by default. The linked support routes are navigation, not evidence of actual enablement.
- The alternative-method section says most merchants can accept PayPal after entering PayPal Business Account credentials in the Control Panel; it separately qualifies Apple Pay by merchant iOS-app and customer eligibility, Google Pay by customer eligibility and Android-device use, and Secure Remote Commerce by limited-release eligibility in certain EU locations. These snapshot statements do not establish current availability or eligibility for a particular merchant or customer.
- When a customer's bank-account currency differs, the page says the transaction is processed in the merchant account's currency and the customer's bank converts the charge. It warns that the bank may charge conversion or other fees and that refunds become harder, potentially increasing chargebacks. An additional merchant account can be requested for another supported currency; applicable presentment and settlement currencies depend on account setup, and the integration must then specify the new merchant account ID.

> [!warning] Exact route and currency boundary
> Keep these acceptance, enablement, eligibility, device, location and currency statements scoped to the captured AIB BF article. Do not transfer them to AIB AF, another account or region, or current independent bank/card-network policy. The document is not a merchant contract and provides no pricing terms. Its linked 3D Secure, payment-method, currency, support and request-reference destinations establish navigation only and were not used as agreeing authority.

## Detail locators

- Account-configured Visa, Mastercard, Maestro and American Express list: `## Card types`, raw lines 17-25.
- Maestro 3D Secure default, issuer-country and recurring-payment conditions, Control Panel prohibition and eventual rejection warning: `### Special note on Maestro`, raw lines 28-36.
- JCB presentment-currency and default-enablement qualification: `### JCB cards`, raw lines 39-41.
- Discover/Diners Club currency limitation, processing relationship and default-enablement qualification: `### Discover and Diners Club cards`, raw lines 44-46.
- PayPal, Apple Pay, Google Pay and limited-release Secure Remote Commerce qualifications: `## Alternative payment methods`, raw lines 49-69.
- Merchant-account processing currency, bank conversion and fee/refund warning, additional-currency account request and merchant-account-ID integration step: `## Currencies`, raw lines 72-78.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Administration context: [[braintree-control-panel]]
- Authentication context: [[braintree-3d-secure]]

## Related raw API references

- [[raw/braintree/docs/guides/3d-secure/overview-2026-09-16|Braintree 3D Secure overview]] - unread navigation-only destination; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]] - unread navigation-only destination; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16|Braintree Apple Pay guide]] - unread navigation-only destination; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]] - unread navigation-only destination; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]] - unread navigation-only destination; not used as factual evidence here
- [[raw/braintree/articles/get-started/currencies-2026-09-16|Braintree currencies guide]] - unread navigation-only destination; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/aib-bf/transactions/accepted-payment-methods-2026-09-16|Braintree AIB BF Accepted Payment Methods]] - fully read collected article covering account-configured cards, method-specific acceptance and enablement conditions, alternative-method qualifications, and merchant-account currency handling
