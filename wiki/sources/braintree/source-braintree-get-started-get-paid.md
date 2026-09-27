---
title: "Braintree Get Paid"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/get-paid"
raw_files:
  - "braintree/articles/get-started/get-paid-2026-09-16.md"
tags: [braintree, funding, settlement, merchant-accounts, credit-cards, american-express, paypal]
---

## Overview

This collected Braintree getting-started article is a post-settlement funding guide. Its starting point is a transaction that has already settled: it describes funds passing through the merchant account to the bank account supplied during the application process, then gives account- and payment-method-qualified timing and funding-provider routes.

The page does not explain how to accept, create or submit a payment for settlement. Its general statements and typical timelines are not proof that a particular transaction settled or that funds reached a merchant's bank account.

## Key takeaways

- After a transaction is settled, the page says funds pass through the merchant account to the bank account provided during application. Funding is managed by the merchant-account provider; for Braintree Direct, the page says Braintree handles that funding.
- How and when funds are paid depends on the payment method and the type of Braintree account. The page routes readers to bank-specific articles or Braintree support for more specific timelines but does not supply those bank-specific details itself.
- Credit-card payments are described as typically reaching the bank account within 2–5 business days after settlement, with a warning that the timeline may differ for international merchants. This is a qualified typical timeline, not a guaranteed arrival time or evidence of an individual deposit.
- For most US merchants using Braintree's aggregated American Express account, Braintree manages disbursement and the page says funds can be expected within 2–5 business days of settlement. International merchants and US merchants choosing an individual Amex account instead have Amex manage funding for those transactions directly.
- PayPal disbursement is managed separately from the Braintree account. The linked PayPal funding guide is a navigation route; it was not read as evidence for this source and this page does not state its details.

> [!warning] Payment acceptance, settlement and funding proof are separate
> This page begins only after settlement and gives general funding routes and qualified timing. It does not document the payment-acceptance flow, establish that a transaction reached settlement, or prove that an individual payout arrived. The 2026-09-16 collection date also does not establish current timing or account eligibility.

## Detail locators

- Post-settlement merchant-account-to-bank route, application bank account and Braintree Direct funding responsibility: `# Get Paid`, line 16.
- Payment-method/account dependence and bank-specific/support navigation: `# Get Paid`, line 18.
- Typical credit-card deposit timing and international-merchant qualification: `## Credit cards`, line 23.
- Aggregated versus individual American Express funding responsibility and timing: `### American Express`, lines 28-30.
- PayPal's separate disbursement route: `## PayPal`, line 35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Separate lifecycle route: [[source-braintree-transaction-lifecycle]]
- Separate disbursement-notification route: [[source-braintree-webhooks-disbursement-node]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16|Braintree PayPal funding and reconciliation guide]] - unread navigation-only destination for the article's PayPal funding link; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/get-started/get-paid-2026-09-16|Braintree Get Paid article]] - complete collected page covering the post-settlement funding route, account- and payment-method-dependent timing, credit-card and American Express qualifications, and separate PayPal disbursement navigation
