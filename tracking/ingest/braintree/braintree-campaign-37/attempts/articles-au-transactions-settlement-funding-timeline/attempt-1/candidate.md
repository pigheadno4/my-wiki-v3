---
title: "Braintree AU Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/au/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, au, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted AU-routed article describes the captured Braintree Direct settlement and funding path: after a transaction has settled, funds pass through the merchant account to the bank account, with Braintree managing funding. It is a retrieval route for credit-card settlement batching, the successful-settlement condition for disbursement, expected card-brand timing, disbursement reporting and separate wallet and PayPal handling. It is not proof that an individual transaction settled, that funds were disbursed or that a bank deposit arrived.

## Key takeaways

- Credit-card transactions are divided into settlement batches and sent to the processor several times a day to confirm settlement. The account's final batch cutoff is 8pm AET and cannot be changed; transactions submitted after it enter the next day's settlement batch.
- Braintree says it disburses only after receiving processor confirmation that a transaction successfully settled. The article then says funds should appear in the bank account 1–3 business days after submission for settlement for Visa/Mastercard and 2–8 business days after submission for settlement for American Express. These are the page's qualified expectations with their stated submission event anchor, not guaranteed bank-arrival deadlines.
- The American Express range is described as typical in Braintree's experience. American Express sets its own settlement-batch cutoff times and handles those disbursements directly, so the article directs related questions to American Express.
- The Control Panel exposes a settled transaction's Disbursement Date and Settlement Amount. The Disbursement Date records when money was sent to the bank account and does not necessarily match when funds appear there.
- Apple Pay and Google Pay transactions are processed and disbursed alongside credit-card transactions. PayPal manages disbursement separately from other Braintree transactions and has a separate funding-options route.

> [!warning] Expected timing is not settlement, disbursement or deposit proof
> The documented card timing does not remove the prerequisite that Braintree first receive processor confirmation of successful settlement. Its bank timing is expressed as what the merchant should see, while the American Express range is additionally described as typical in Braintree's experience. A Disbursement Date records when money was sent, not when or whether it appeared in the bank account. Treat this as the captured AU-routed Braintree Direct snapshot, not a universal current regional, bank or processor guarantee, and do not transfer timing from sibling account routes.

## Detail locators

- Post-settlement merchant-account-to-bank-account path and Braintree Direct funding ownership: `# Settlement and Funding Timeline`, raw line 16.
- Credit-card batching, processor-confirmation purpose, fixed 8pm AET account cutoff and next-day batch handling: `## Credit cards`, raw line 21.
- Successful-settlement confirmation prerequisite for disbursement and qualified bank-timing introduction: `## Credit cards`, raw line 23.
- Visa/Mastercard and American Express schedules with the submission-for-settlement event anchor: `## Credit cards`, raw lines 26–27.
- American Express experience qualification, cutoff ownership, direct disbursement responsibility and support route: `## Credit cards`, raw line 29.
- Control Panel steps and Disbursement Date/Settlement Amount fields: `### Disbursement information`, raw lines 32–42.
- Sent-versus-appeared meaning of Disbursement Date: `### Disbursement information`, raw line 44.
- Apple Pay and Google Pay treatment: `## Apple Pay and Google Pay`, raw lines 47–49.
- Separate PayPal disbursement route: `## PayPal`, raw lines 52–54.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/au/transactions/settlement-funding-timeline-2026-09-16|Braintree AU Settlement and Funding Timeline article]] - complete captured page covering Braintree Direct settlement batching, processor-confirmed settlement before disbursement, card-brand expected timing, disbursement reporting and separate wallet and PayPal handling
