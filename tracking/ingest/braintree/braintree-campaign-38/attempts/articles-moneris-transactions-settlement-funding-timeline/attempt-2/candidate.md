---
title: "Braintree Moneris Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/moneris/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, moneris, settlement, funding, disbursement, credit-cards]
---

## Overview

This pinned Braintree-hosted Moneris-route article describes card settlement batching and the funding steps and timing statements that follow successful settlement for the captured account context. It is a retrieval route for the stated event anchors, method-specific handling, account-dependent cutoff language, funding ownership, bank descriptors and payout cadence. It is not independent current Moneris policy, a rule for another Braintree account or processor route, or proof that an individual transaction settled, was paid out or reached a bank account.

## Key takeaways

- Credit-card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The article says the cutoff depends on account setup and cannot be changed, then identifies an 8pm cutoff; transactions submitted after it enter the next day's settlement batch.
- Once Moneris receives confirmation that a transaction successfully settled, the article says the funds are ready for payout and that the merchant should see Visa/Mastercard funds 1–3 business days after settlement and American Express funds 2–8 business days after settlement. The American Express range is qualified as Braintree's experience; American Express sets its own cutoff times, handles those disbursements directly and owns related questions.
- The Funding section says Moneris issues funding and that bank descriptors should look similar to `VSA DEP` or `MC DEP`, subject to the merchant's bank. It separately says funds are typically reflected within 2–5 business days of the transaction settlement date. The article does not explain how that general 2–5-day bank-reflection statement relates to the preceding brand-specific 1–3- and 2–8-day deposit schedules, so keep each statement with its own wording rather than collapsing them into one deadline.
- By default, funds are paid out every weekday except bank holidays. For weekends and bank holidays, the article says funds are sent the following business day and typically take an additional business day to appear in the account.
- All Apple Pay transactions are processed and paid out alongside American Express credit-card transactions in this snapshot. PayPal manages disbursement separately from the Braintree-managed account and links to a different funding-options route.

> [!warning] Qualified schedules are not settlement or bank-arrival proof
> The 8pm cutoff is a pre-settlement batch-inclusion rule qualified by account setup. Separately, the Visa/Mastercard and American Express payout/deposit schedules follow successful settlement and retain their payment-method qualifications; the general bank-reflection statement also follows the transaction settlement date and depends on the merchant's bank, while the weekday and bank-holiday wording qualifies payout cadence and when funds appear. The schedules use "should," "typically" and "in our experience" rather than guarantees, and the two timing sections are not reconciled. Moneris funding ownership also has an explicit American Express direct-disbursement exception, while PayPal is separate. Treat this as the captured Braintree-hosted Moneris account route, not current independent processor policy or evidence of an individual settlement, payout or deposit.

## Detail locators

- Post-settlement merchant-account-to-business-bank-account path: `# Settlement and Funding Timeline`, raw line 16.
- Credit-card batching, processing-bank confirmation purpose, account-setup qualification, non-changeable cutoff and post-8pm next-day handling: `## Credit cards > ### Settlement`, raw line 24.
- Successful-settlement confirmation prerequisite and qualified payout introduction: `## Credit cards > ### Settlement`, raw line 26.
- Visa/Mastercard and American Express schedules with the after-settlement event anchor: `## Credit cards > ### Settlement`, raw lines 29–30.
- American Express experience qualification, cutoff ownership, direct-disbursement responsibility and support route: `## Credit cards > ### Settlement`, raw line 32.
- Moneris funding ownership, bank-dependent descriptor qualification and descriptor examples: `## Credit cards > ### Funding`, raw lines 37–41.
- General 2–5-business-day bank-reflection statement: `## Credit cards > ### Funding`, raw line 43.
- Weekday default, bank-holiday exclusion, following-business-day sending and additional visibility delay: `## Credit cards > ### Funding`, raw line 45.
- Apple Pay handling and American Express support ownership: `## Apple Pay`, raw line 50.
- Separate PayPal disbursement and funding-options route: `## PayPal`, raw line 55.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Linked PayPal funding route: [[source-braintree-payment-methods-paypal-funding-reconciliation]] (navigation only; not used as evidence for this page's Moneris statements)

## Raw Sources

- [[raw/braintree/articles/moneris/transactions/settlement-funding-timeline-2026-09-16|Braintree Moneris Settlement and Funding Timeline article]] - complete captured page covering the post-settlement path, card batching, Moneris and American Express funding ownership, qualified timing, bank descriptors, payout cadence and separate Apple Pay and PayPal treatment
