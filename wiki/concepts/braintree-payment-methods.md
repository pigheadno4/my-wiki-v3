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

- [[source-braintree-payment-methods-sepa-direct-debit]] - pilot-only SEPA Direct Debit availability, mandate and linked-PayPal setup prerequisites, customer-confirmation funding statement, post-disbursement return exposure, and supported vaulting and recurring transactions

- [[source-braintree-payment-methods-paypal-pay-later-offers]] - Braintree PayPal Pay Later route for country-dependent offer identity, merchant-versus-customer eligibility, Checkout with Vault enablement, and messaging/button and promotional-content boundaries

- [[source-braintree-payment-methods-unionpay]] - UnionPay-specific deprecation and limited-release tension; European-merchant, SDK-version and settlement-currency conditions; SMS verification and vaulted-card behavior; processing, chargeback-fee and CVV/AVS-bypass boundaries

- [[source-braintree-payment-methods-paypal-credit]] - deprecated PayPal Credit guide covering the legacy reusable credit-line identity, US/UK currency and regulatory qualifications, customer credit approval, named financing options and existing-PayPal-setup boundary, with a separate Pay Later offers redirect

- [[source-braintree-payment-methods-secure-remote-commerce]] - SRC/Click to Pay identity, limited-release merchant and SDK prerequisites, credit-card-like processing routes, and the guide's unresolved January 2026 end-of-support versus current-tense availability conflict

- [[source-braintree-payment-methods-google-pay]] - dedicated Google Pay route for Android and web setup, merchant-versus-customer availability, card-or-account distinctions, method-specific fraud-tool and vaulting boundaries, and Google production approval

- [[source-braintree-payment-methods-local-payment-methods]] - regional bank, wallet and other local-method scope; eligible-merchant and PayPal-account prerequisites; locality-based display; euro presentment and primary-currency PayPal settlement; redirect-qualified Payment Context visibility; and unsupported dispute, vaulting and recurring-transaction boundaries

- [[source-braintree-payment-methods-apple-pay]] - dedicated Braintree Apple Pay route for conditional merchant and customer availability, mobile/web platform requirements, DPAN processing, vaulting consent guidance, integration roles and certificate renewal

- [[source-braintree-payment-methods-venmo]] - Venmo checkout and vaulting route with unsupported-business-model, US-entity, SDK-version, customer-version, production-profile and 180-day refund qualifications from the collected guide

- [[source-braintree-payment-methods-ach]] - ACH Direct Debit merchant eligibility, required bank-account verification, delayed batch settlement and late-return exposure, conflicting void guidance, and bank-account vaulting versus recurring-billing boundary

- [[source-braintree-get-started-payment-methods]] - provider-wide payment-method categories, merchant and customer qualifications, card scope, and collected deprecation boundaries
