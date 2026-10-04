---
title: "Braintree AIB AF Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/aib-af/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, aib-af, settlement, funding, disbursement, credit-cards]
---

## Overview

This collected [[braintree]] article under the AIB AF path describes credit-card transactions being divided into settlement batches and sent to the processing bank to confirm settlement; once a transaction has successfully settled, AIB disburses the funds toward the merchant's bank account. It documents an account cutoff, first-deposit delay, card-brand schedules, weekday and bank-holiday handling, optional weekly or monthly cadence, wallet alignment, and a separate PayPal funding route.

This is a Braintree-hosted AIB AF snapshot, not AIB BF coverage, independent or current bank authority, a merchant-specific agreement, or evidence that any transaction settled or any deposit arrived.

## Key takeaways

- Before the first deposit, the article states an additional delay of 10 business days. It says the regular funding schedule applies after that first deposit.
- Credit-card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The stated cutoff for the account is 6:00 p.m. Central Time (US) and cannot be changed; transactions submitted after it move to the next settlement batch.
- After successful settlement, the article says AIB disburses funds and presents an expected bank-deposit schedule of 2–3 business days for Visa, Mastercard, Discover and Maestro, and 2–8 business days for American Express. The Amex timing is explicitly experiential; Amex sets its own cutoff and handles disbursement directly, so the article routes details to Amex.
- By default, funds are disbursed on weekdays excluding bank holidays. Weekend and bank-holiday funds are sent the next business day, and the article says it typically takes another business day before funds are visible in the account. Weekly or monthly disbursement is offered as a custom schedule through the linked contact route.
- Apple Pay and Google Pay transactions are described as processed and disbursed alongside credit-card transactions. PayPal instead manages funding separately from the Braintree-managed account; the linked PayPal funding page is navigation only here and does not establish its options or agreement with this snapshot.

> [!warning] Schedule is not deposit-arrival proof
> These are snapshot schedule statements with first-deposit, successful-settlement, card-brand, cutoff, weekday and bank-holiday qualifications. A schedule or absence of a documented failure does not prove that an individual transaction settled, that funds were sent, or that a deposit reached the merchant's bank account.

> [!warning] Captured AIB AF scope
> Keep the cutoff, timing and cadence within this captured AIB AF article. Do not transfer them to AIB BF, another processor/account arrangement, a current merchant agreement, or current independent bank policy. Linked contact, accepted-payment-method and PayPal-funding pages are navigation, not evidence that their target content agrees.

## Detail locators

- Post-settlement merchant-account-to-bank-account framing: raw line 16.
- Additional 10-business-day delay before the first deposit: `## Credit cards`, raw lines 22-23.
- Credit-card settlement batching, fixed account cutoff and next-batch effect: `## Credit cards`, raw line 27.
- Successful-settlement prerequisite, card-brand schedules and Amex-owned timing/disbursement qualification: `## Credit cards`, raw lines 29-35.
- Default weekday cadence, bank-holiday/weekend handling, additional visibility delay and optional weekly/monthly schedule: `## Credit cards`, raw lines 37-39.
- Apple Pay and Google Pay alignment with credit-card processing and disbursement: `## Apple Pay and Google Pay`, raw lines 42-44.
- PayPal's separately managed disbursement and linked funding-options route: `## PayPal`, raw lines 47-49.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/aib-af/transactions/accepted-payment-methods-2026-09-16|Braintree AIB AF accepted payment methods]] - unread navigation-only destination linked for Apple Pay and Google Pay; not used as factual evidence here
- [[raw/braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16|Braintree PayPal funding and reconciliation]] - unread navigation-only destination linked for separate PayPal funding options; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/aib-af/transactions/settlement-funding-timeline-2026-09-16|Braintree AIB AF Settlement and Funding Timeline]] - fully read collected article covering post-settlement batching, first-deposit and card-brand timing, disbursement cadence, wallet alignment and separate PayPal funding
