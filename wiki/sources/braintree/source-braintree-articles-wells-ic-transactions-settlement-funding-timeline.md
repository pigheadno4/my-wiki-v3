---
title: "Braintree Wells IC Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/wells-ic/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, wells-ic, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted Wells IC article describes the path after a transaction has settled for the captured Braintree Direct account context: funds pass through the merchant account to the bank account, with Braintree managing funding. It is a retrieval route for card settlement batches, qualified post-settlement disbursement timing, account-specific exceptions and separate wallet/PayPal handling. It does not establish Wells Flat terms, current universal bank policy or proof that an individual deposit reached a bank account.

## Key takeaways

- For credit cards other than American Express, transactions are divided into settlement batches and sent to the processor several times daily for confirmation. Transactions submitted for settlement after 5pm CT (US) move to the next day's settlements.
- After processor confirmation of successful settlement, the article says Braintree disburses the funds and that they should appear in the bank account 2 business days after the associated transactions settled. Disbursements occur on weekdays except bank holidays, when they are sent the next business day.
- Under Braintree's aggregated American Express setup, the final batch is sent at 4PM CT (US); later submissions move to the next day's settlements, and the article gives a 2–5-business-day disbursement window. The fixed cutoff is not adjusted for daylight saving time, so the article says it runs at 3PM CT between the first Sunday in November and the second Sunday in March.
- With the merchant's own American Express account rather than Braintree's aggregated setup, American Express sets the cutoff and funds and deposits the transactions directly. Gateway-only accounts through another merchant-account provider instead have one daily settlement batch with a 6am CDT/CST cutoff.
- The Control Panel's disbursement date records when money was sent to the bank account; it may not match when funds appear. Apple Pay and Google Pay follow the credit-card disbursement route, while PayPal manages disbursement separately from the Braintree-managed account.

> [!warning] Funding timing is not individual deposit proof
> Every listed bank timing starts from the article's applicable settlement or disbursement condition and retains the card-brand, account-setup, weekday and bank-holiday qualifications. A disbursement date shows when money was sent, not when or whether a particular deposit appeared. This captured Wells IC route must not be generalized to Wells Flat or current universal bank policy.

## Detail locators

- Post-settlement merchant-account-to-bank-account path, Braintree Direct funding ownership and support route: `# Settlement and Funding Timeline`, line 16.
- Non-Amex credit-card batching, 5pm CT cutoff and next-day settlement handling: `## Credit cards`, lines 22–29.
- Successful-settlement prerequisite, 2-business-day bank timing and weekday/bank-holiday qualification: `## Credit cards`, lines 29–31.
- Aggregated American Express cutoff, next-day handling and 2–5-business-day timing: `### American Express`, line 36.
- Daylight-saving-time qualification for the aggregated American Express cutoff: `### American Express > NOTE`, lines 39–40.
- Merchant-owned American Express account responsibility: `### American Express`, line 44.
- Gateway-only account cutoff and uncertainty-support route: `### Special note on gateway-only accounts`, lines 47–49.
- Control Panel disbursement fields and the sent-versus-appeared distinction: `### Disbursement Information`, lines 52–64.
- Apple Pay and Google Pay treatment: `## Apple Pay and Google Pay`, lines 67–69.
- Separate PayPal disbursement route: `## PayPal`, lines 72–74.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Separate general funding route: [[source-braintree-get-started-get-paid]]
- Separate PayPal funding route: [[source-braintree-payment-methods-paypal-funding-reconciliation]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/transactions/settlement-funding-timeline-2026-09-16|Braintree Wells IC Settlement and Funding Timeline article]] - complete collected page covering Braintree Direct post-settlement funding, card batching and timing qualifications, account-specific exceptions, disbursement-date meaning and separate wallet/PayPal handling
