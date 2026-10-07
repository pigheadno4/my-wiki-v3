---
title: "Braintree PINless Debit Optimized Debit Routing Eligibility"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/eligibility"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/eligibility-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, eligibility, debit-cards]
---

## Overview

This unversioned [[braintree|Braintree]] website eligibility checklist states the merchant, currency, payment-method, card-BIN and network conditions for PINless debit optimized routing and directs merchants to contact an account representative or Business Development for enablement. [[braintree-payment-methods]]

## Key takeaways

- The stated merchant scope is US-domiciled merchants, and the transaction currency must be US dollars.
- Supported payment-method inputs are vaulted and keyed debit/prepaid cards plus eligible card types from Apple Pay and Google Pay. Only eligible Visa and Mastercard BINs are routed to PINless debit networks; the wallet labels do not make every Apple Pay or Google Pay card eligible.
- The listed eligible PINless card networks are STAR, NYCE, PULSE, ACCEL and MAESTRO. The page separately says Apple Pay and Google Pay payment methods are now eligible on the PINless Debit Network, subject to the page's card-type and BIN qualifications.
- Onboarding requires contacting the merchant's Technical account manager or submitting an inquiry to the Business Development team. That contact route is not proof that a merchant is currently eligible or enabled.

## Detail locators

- Merchant domicile and transaction-currency conditions: `## Eligibility` → `Merchants supported`, raw lines 16-18.
- Payment-method, wallet-card and Visa/Mastercard BIN conditions: `## Eligibility` → `Payment methods supported`, raw lines 20-23.
- Eligible PINless networks: `## Eligibility` → `Eligible PINless card networks`, raw lines 25-30.
- Apple Pay and Google Pay note: `## Eligibility` → `NOTE`, raw lines 33-34.
- Enablement contact route: `### Onboarding`, raw lines 37-39.

## Evidence boundary

> [!warning] Eligibility snapshot only
> This 2026-09-16 website snapshot is not proof of current product support, merchant or card eligibility, account enablement, network routing, authorization, payment execution, settlement or funding. It does not define pricing or savings, an SDK/version, client/server integration behavior, or GitHub implementation/history.

## Related

- [[braintree]]
- [[braintree-payment-methods]] - provider concept route for payment-method eligibility and PINless debit optimized-routing documentation

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/eligibility-2026-09-16|Braintree PINless Debit optimized routing eligibility (2026-09-16 snapshot)]]
