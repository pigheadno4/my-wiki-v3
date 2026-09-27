---
title: "Braintree Payment Methods"
type: concept
category: technology
tags: [braintree, payment-methods, cards, digital-wallets, eligibility]
---

## Braintree Payment Methods

Braintree's collected getting-started page is a provider-wide route to its stated payment-method categories and eligibility qualifications. The page covers ACH Direct Debit, Apple Pay, Google Pay, cards, PayPal, Local Payment Methods, Venmo and Secure Remote Commerce, while recording Samsung Pay as deprecated and a dated end-of-support notice for Visa Click to Pay. Detailed setup belongs to the dedicated method guides rather than this overview. [[source-braintree-get-started-payment-methods]]

## Eligibility boundaries

Availability is not uniform across the listed methods. The page qualifies methods by combinations of merchant region, customer participation, processor settings, third-party approval, merchant-account card bundles, supported regional card networks, merchant category code, US merchant status and limited-release eligibility. Its collected current-tense wording is snapshot evidence, not proof of present support, merchant enablement or buyer eligibility. [[source-braintree-get-started-payment-methods]]

Card scope also varies by account and use case: the page distinguishes US from most international default card-brand bundles, treats major-brand online debit as credit because PINs cannot be accepted online, allows dual-branded routing only on a network supported in the merchant's region, and requires an appropriate MCC for special-use cards. Use the source and its raw detail locators to select the applicable qualification before following a dedicated integration route. [[source-braintree-get-started-payment-methods]]

> [!warning] Contradiction
> The page's opening note equates Visa Click to Pay with Secure Remote Commerce and gives a January 20, 2026 end-of-support date, while its final section calls Secure Remote Commerce a current limited release for eligible merchants. The snapshot does not resolve the conflict; use the source and raw locators rather than inferring current support.

## Sources

- [[source-braintree-get-started-payment-methods]] - provider-wide payment-method categories, merchant and customer qualifications, card scope, and collected deprecation boundaries
