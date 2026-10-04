---
title: "Braintree AU Accepted Payment Methods"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/transactions/accepted-payment-methods"
raw_files:
  - "braintree/articles/au/transactions/accepted-payment-methods-2026-09-16.md"
tags: [braintree, australia, payment-methods, cards, american-express, digital-wallets]
---

## Overview

This collected Braintree AU-path article is an account-scoped retrieval route for the payment methods described for the page's Australian context: default Visa and Mastercard acceptance, separately arranged American Express processing, and qualified PayPal, Apple Pay and Google Pay availability. The page body was last updated on 2025-04-01 and was collected on 2026-09-16; it is snapshot evidence, not proof of current support, an individual merchant's configuration or eligibility, pricing, approval, or successful payment execution.

## Key takeaways

- The article says the account accepts Visa and Mastercard by default. American Express is not configured by default and requires the merchant to apply directly to Amex; Amex manages funding, descriptors, chargebacks and technical support for that route.
- American Express carries separate account, currency and commercial prerequisites. Braintree charges a per-transaction fee in addition to Amex-assessed processing fees. Setup requires Service Establishment Numbers and the currencies corresponding to them, and gateway enablement depends on Amex pricing having been included in the original pricing agreement or completion and signature of a separate pricing form. These statements do not prove approval, actual fees or terms for an individual merchant.
- The alternative-method statements are modal and conditional. The article says most merchants can link PayPal Business Account credentials through the Braintree Control Panel, most merchants with an iOS mobile app can enable Apple Pay for eligible customers using iOS devices, and most merchants can enable Google Pay for eligible customers using Android devices.
- The AU article's mobile-only wording is narrower than the separately collected dedicated guides: the Apple Pay guide describes mobile and web acceptance, and the Google Pay guide describes Android apps and web checkout. This cross-page channel-scope difference is unresolved here; do not use the AU article to deny web support, and do not use the broader guides to prove that a particular AU account, merchant, buyer, device or transaction is currently supported.

> [!warning] AU account, time and eligibility scope are material
> Keep default-card acceptance, Amex setup and pricing prerequisites, and alternative-method availability scoped to this collected AU-path account article. "Most merchants," "eligible customers," device conditions and account configuration are qualifications, not guarantees. Collection, application, credential entry or enablement is not proof of present support, approval, authorization, capture, settlement, funding, dispute handling or refund success.

> [!warning] Apple Pay and Google Pay channel scope differs across collected pages
> This AU article describes Apple Pay through an iOS mobile app and Google Pay for purchases using Android devices, while the dedicated Braintree guides collected on the same date describe web routes as well. Preserve the difference and confirm current account, region, platform, processor-setting and production-approval eligibility before implementation.

## Detail locators

- Payment-method purpose and account framing: `# Accepted Payment Methods`, raw lines 14-16.
- Default Visa and Mastercard acceptance: `## Card types`, raw lines 19-25.
- Non-default Amex configuration, direct-account application and Amex-owned funding, descriptors, chargebacks and support: `### American Express`, raw lines 28-32.
- Separate Braintree and Amex fees: `#### Fees`, raw lines 35-37.
- Service Establishment Number and corresponding-currency setup: `#### Setup`, raw lines 40-42.
- Original-pricing-agreement prerequisite or separate signed pricing form: `#### Setup > **NOTE**`, raw lines 45-46.
- Modal PayPal Business Account credential route: `## Alternative payment methods > ### PayPal`, raw lines 51-56.
- Qualified Apple Pay iOS-app and eligible-customer wording: `### Apple Pay`, raw lines 59-61.
- Qualified Google Pay and eligible-customer Android-device wording: `### Google Pay`, raw lines 64-66.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Dedicated Apple Pay route: [[source-braintree-payment-methods-apple-pay]]
- Dedicated Google Pay route: [[source-braintree-payment-methods-google-pay]]

## Raw Sources

- [[raw/braintree/articles/au/transactions/accepted-payment-methods-2026-09-16|Braintree AU Accepted Payment Methods article]] - complete collected snapshot covering default cards, separately arranged American Express and qualified PayPal, Apple Pay and Google Pay availability
