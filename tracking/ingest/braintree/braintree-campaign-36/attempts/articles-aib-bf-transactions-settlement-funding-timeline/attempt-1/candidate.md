---
title: "Braintree AIB BF Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/aib-bf/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, aib-bf, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted AIB BF article describes card settlement batching and the funding schedules that follow successful settlement for the captured account route. It is retrieval guidance for timing and payout-report meaning, not evidence that a particular transaction settled or that a particular bank deposit arrived.

The body does not explain the AIB BF label or identify an independent bank, processor, region, or pricing model. Treat it as a snapshot of Braintree's AIB BF route, not AIB AF documentation or current independent bank or processor policy.

## Key takeaways

- For credit cards other than American Express, the account's settlement batch cutoff is 6pm Central Time (US) and cannot be changed; submissions after that time enter the next batch. Only after successful settlement does the article describe disbursement, with funds expected in the bank account 2–3 business days after settlement. Weekday, bank-holiday, and following-business-day qualifications apply.
- American Express uses separate batches. Under Braintree's aggregated Amex setup, the final daily batch is sent at 4PM Central Time (US), later submissions move to the next day's settlements, and the article gives a 2–8-business-day disbursement expectation. Its daylight-saving note says the fixed cutoff runs at 3PM Central Time (US) between the second Sunday in March and the first Sunday in November.
- With the merchant's own Amex account rather than Braintree's aggregated setup, Amex sets its own cutoff, funds and deposits the transactions directly, and owns related questions.
- The Control Panel's Disbursement Date is the date money was paid out to the bank account; the article says it typically takes another business day for funds to appear. Apple Pay and Google Pay follow the credit-card route, while PayPal manages disbursement separately from the Braintree-managed account.

> [!warning] Funding schedules are not settlement or deposit proof
> Every listed timing remains conditional on the article's applicable successful-settlement, account setup, payment-method, weekday and bank-holiday conditions. A Disbursement Date records payout to the bank account, not arrival there. Do not use this captured AIB BF schedule as proof that an individual transaction settled, a payout completed, or a deposit arrived.

## Detail locators

- Non-Amex scope and linked Amex exception: `## Credit cards > NOTE`, raw lines 20–21.
- Non-Amex batching, 6pm Central Time (US) account cutoff and next-batch handling: `## Credit cards`, raw line 25.
- Successful-settlement prerequisite, 2–3-business-day expectation, weekday cadence and bank-holiday adjustment: `## Credit cards`, raw lines 27–29.
- Aggregated American Express cutoff, next-day handling and 2–8-business-day expectation: `### American Express`, raw line 34.
- Daylight-saving-time qualification: `### American Express > NOTE`, raw lines 37–38.
- Merchant-owned American Express account funding and support responsibility: `### American Express`, raw line 42.
- Control Panel payout lookup fields and sent-versus-appeared meaning: `### Payout information`, raw lines 45–57.
- Apple Pay and Google Pay treatment: `## Apple Pay and Google Pay`, raw lines 60–62.
- Separate PayPal disbursement route: `## PayPal`, raw lines 65–67.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/aib-bf/transactions/settlement-funding-timeline-2026-09-16|Braintree AIB BF Settlement and Funding Timeline article]] - complete captured page covering card settlement batches, post-settlement schedules, Amex setup differences, payout reporting and separate wallet and PayPal treatment
