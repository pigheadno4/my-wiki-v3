---
title: "Braintree Wells Flat Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/wells-flat/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, wells-flat, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted article documents the post-settlement funding timeline for the captured Wells Flat account route. It starts only after a transaction has settled and describes Braintree Direct-managed movement through the merchant account to the bank account; it does not establish that a particular transaction settled or that a particular bank deposit arrived.

## Key takeaways

- For credit cards other than American Express, transactions are batched for processor settlement confirmation. After successful settlement confirmation, the article says Braintree disburses the funds and that they should appear in the bank account 2 business days after settlement; weekday and bank-holiday qualifications apply.
- American Express uses separate batches. The article distinguishes Braintree aggregated Amex, for which it gives a 2–5-business-day disbursement expectation, from a merchant's own Amex account, where Amex funds and deposits directly and owns the cutoff and disbursement questions.
- A merchant account held with another provider while Braintree is used only as the gateway follows the article's separate gateway-only batching rule, not the Braintree Direct route.
- The Control Panel disbursement date records when money was sent to the bank account, not necessarily when it appeared there. Apple Pay and Google Pay follow the credit-card route, while PayPal disbursement is managed separately.

> [!warning] Captured route and schedule are not deposit proof
> This snapshot belongs to Braintree's captured Wells Flat documentation route. Do not transfer it to Wells IC, another account or pricing configuration, another region, or current independent Wells Fargo bank policy. All stated timing remains conditional on the documented settlement confirmation, account setup, payment method, weekday and bank-holiday context and is not proof of a specific deposit.

## Detail locators

- Post-settlement Braintree Direct funding scope and support route: `# Settlement and Funding Timeline`, line 16.
- Non-Amex batching, 5pm CT (US) cutoff, successful-settlement prerequisite, 2-business-day expectation and weekday/bank-holiday qualification: `## Credit cards`, lines 22–31.
- Aggregated American Express batching, 4PM CT (US) cutoff, 2–5-business-day expectation and daylight-savings qualification: `### American Express`, lines 34–40.
- Merchant-owned American Express account funding and support responsibility: `### American Express`, line 44.
- Gateway-only merchant-account scope and daily 6am CDT/CST (US) cutoff: `### Special note on gateway-only accounts`, lines 47–49.
- Control Panel disbursement lookup and sent-versus-appeared meaning: `### Disbursement Information`, lines 52–64.
- Apple Pay and Google Pay card-route treatment: `## Apple Pay and Google Pay`, lines 67–69.
- Separate PayPal disbursement route: `## PayPal`, lines 72–74.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- General Braintree funding route: [[source-braintree-get-started-get-paid]]
- Separate PayPal funding route: [[source-braintree-payment-methods-paypal-funding-reconciliation]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/transactions/settlement-funding-timeline-2026-09-16|Braintree Wells Flat Settlement and Funding Timeline article]] - complete collected page covering Braintree Direct funding, card and Amex schedules, gateway-only batching, disbursement reporting and separate wallet and PayPal treatment
