---
title: "Braintree Chase Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/chase/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, chase, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted Chase processor article describes what happens after a transaction has settled: Chase passes funds through the merchant account to the merchant's bank account. It is a retrieval route for account-dependent card settlement batches, card-brand-specific funding schedules, disbursement timing qualifications and separate wallet/PayPal handling; it is not proof that an individual deposit reached a bank account.

## Key takeaways

- Credit-card transactions are divided into settlement batches and sent to the processor for settlement confirmation. The batch cutoff depends on the merchant's account setup and cannot be changed; transactions submitted after a cutoff move to the next batch.
- After Chase receives processor confirmation that a transaction successfully settled, the article says Chase disburses funds to the merchant's account. It lists 2–3 business days after settlement for Visa, Mastercard, Discover and Diners Club, and 2–5 business days for American Express.
- The American Express schedule is explicitly described as Braintree's experience. American Express sets its own settlement-batch cutoff times and handles those disbursements directly, so the article directs merchants to American Express for details.
- Chase Paymentech reporting can show the disbursement date for a transaction, but that date is when money was sent to the bank account and may not match when funds appear there. Funds are disbursed on weekdays except bank holidays, when they are sent on the next business day.
- Apple Pay and Google Pay transactions are processed and disbursed alongside credit-card transactions. PayPal manages disbursement separately from the Braintree-managed account and follows a different funding route.

> [!warning] Schedule and reporting records are not deposit proof
> The listed timing begins only after successful settlement confirmation and retains the article's card-brand, merchant-account, weekday and bank-holiday qualifications. A Chase Paymentech disbursement date records when money was sent; it does not prove when, or whether, an individual deposit appeared in the merchant's bank account.

## Detail locators

- Post-settlement Chase merchant-account-to-bank-account route and funding-support navigation: `# Settlement and Funding Timeline`, line 16.
- Settlement batching, account-setup-dependent immutable cutoff and next-batch handling: `## Credit cards`, line 21.
- Chase disbursement condition and card-brand schedules, including the American Express cutoff/disbursement responsibility qualification: `## Credit cards`, lines 23–29.
- Chase Paymentech disbursement-date meaning and bank-appearance distinction: `## Credit cards`, line 31.
- Weekday and bank-holiday disbursement qualification: `## Credit cards > NOTE`, lines 34–35.
- Apple Pay and Google Pay treatment: `## Apple Pay and Google Pay`, lines 40–42.
- Separate PayPal disbursement route: `## PayPal`, lines 45–47.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Separate general funding route: [[source-braintree-get-started-get-paid]]
- Separate PayPal funding route: [[source-braintree-payment-methods-paypal-funding-reconciliation]]

## Raw Sources

- [[raw/braintree/articles/chase/transactions/settlement-funding-timeline-2026-09-16|Braintree Chase Settlement and Funding Timeline article]] - complete collected page covering post-settlement Chase funding, account-dependent settlement batching, card-brand schedules, disbursement-date qualifications and separate wallet/PayPal handling
