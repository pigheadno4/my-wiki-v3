---
title: "Braintree UnionPay"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/unionpay"
raw_files:
  - "braintree/articles/guides/payment-methods/unionpay-2026-09-16.md"
tags: [braintree, unionpay, credit-cards, china, sms-verification, vaulting]
---

## Overview

This collected Braintree guide describes UnionPay credit and debit card acceptance, including merchant geography and settlement-currency conditions, version-qualified client SDK availability, SMS verification, processing, disputes, fraud-rule handling, vaulting and setup. Its opening availability notice says the dedicated UnionPay integration has been deprecated because UnionPay can now be processed as a credit card through a Discover partnership, while the body also calls UnionPay a limited release and describes setup for the dedicated flow; treat that unresolved scope tension as snapshot evidence rather than proof of current support or merchant enablement.

## Key takeaways

- The page describes UnionPay as a major credit- and debit-card provider for customers in China. It says UnionPay transactions are not enabled on a merchant account by default and require additional setup.
- The collected availability section says most European merchants can accept UnionPay with Android v4, iOS v4+, and JavaScript v3 SDKs, but not through the JavaScript v3 Drop-in UI. It limits the described merchant settlement currencies to USD, GBP, EUR, or CHF and directs interested merchants to contact Braintree for setup and access.
- The documented checkout flow requires the customer to enter a mobile number and then an SMS verification code sent to the device before the transaction can be processed. The page says customers verify on each purchase unless the UnionPay card is vaulted; after verification, transactions process like regular credit and debit cards and typically settle within three business days.
- UnionPay processing uses a different fee from the merchant's normal rate. The page separately states a USD 25 standard chargeback fee, or settlement-currency equivalent, that is non-refundable regardless of outcome and includes pre-arbitrations. Exact pricing remains in the merchant's pricing agreement.
- The guide says some UnionPay cards lack CVV numbers and postal codes are rarely collected for these transactions, so Braintree bypasses CVV and AVS rules for certain UnionPay transactions to avoid unnecessary gateway rejections. This is a UnionPay-specific qualification, not a generic card-processing rule.
- After initial verification, the page says vaulted UnionPay cards do not require SMS verification. Its setup section calls UnionPay a limited release and directs interested merchants to contact Braintree, which must remain visible alongside the opening deprecation notice.

## Evidence boundaries

> [!warning] Deprecation and limited-release tension
> The same collected page says the dedicated UnionPay integration is deprecated because UnionPay can now be processed as a credit card through Discover, then presents the described UnionPay setup as a limited release. The snapshot does not reconcile whether every body section applies to the replacement card-processing path, the deprecated dedicated integration, or both. Confirm the current merchant route with Braintree rather than combining the statements into a current-support claim.

> [!warning] UnionPay-specific scope
> Do not generalize this page's European-merchant, SDK-version, settlement-currency, SMS, vaulting, fee, dispute, CVV or AVS statements to generic credit cards, other card networks, sibling payment methods, or unlisted merchant geographies.

## Detail locators

- Deprecation notice, Discover credit-card path, China customer-card identity and account enablement requirement: `# UnionPay` and `AVAILABILITY`, lines 14-20.
- European merchant scope, Android v4, iOS v4+, JavaScript v3, unsupported JavaScript v3 Drop-in UI, settlement currencies and setup contact: `## Availability`, lines 23-27.
- Mobile-number and device SMS verification, per-purchase versus vaulted-card behavior, card-like processing and typical settlement timing: `## Processing`, lines 30-34.
- Merchant-agreement fee route: `## Processing > ### Fees`, lines 37-39.
- Chargeback fee, non-refundability and pre-arbitration scope: `## Processing > ### Disputes`, lines 42-44.
- Fraud-tool compatibility, missing-CVV and rarely collected postal-code conditions, and certain-transaction AVS/CVV bypass: `## Processing > ### Fraud tools`, lines 47-53.
- Vaulted-card SMS behavior and limited-release setup statement: `## Processing > ### Recurring billing and vaulting` through `## Setup`, lines 56-63.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Supporting concepts: [[recurring-payments]], [[disputes]], [[braintree-fraud-tools]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/unionpay-2026-09-16|Braintree UnionPay payment-method guide]] - complete collected page covering the deprecation notice, UnionPay-specific availability, SMS verification, processing, disputes, fraud-rule handling, vaulting and setup
