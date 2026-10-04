---
title: "Braintree Brazil Settlement and Funding Timeline"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/transactions/settlement-funding-timeline"
raw_files:
  - "braintree/articles/br/transactions/settlement-funding-timeline-2026-09-16.md"
tags: [braintree, brazil, settlement, funding, disbursement, credit-cards, debit-cards, installments]
---

## Overview

This captured [[braintree]] BR/Brazil-routed article describes a Braintree Direct settlement-and-funding path for credit-card and debit-card transactions. It says that, after settlement, funds pass through the merchant's linked PayPal Business Account before being swept to the bank account, and it separately documents card batching, payment-method-specific timing, installment disbursements, refund adjustments and Control Panel disbursement information.

Treat this as a 2026-09-16 account-facing snapshot, not current independent bank, scheme, processor or PayPal policy, a merchant-specific agreement, a guarantee, or proof that an individual transaction settled, was disbursed or arrived. The page names no currency or card brands, so do not infer BRL, a currency-conversion rule or brand-specific timing, and do not transfer the schedule to another account, region or sibling article.

## Key takeaways

- Credit-card transactions are grouped into settlement batches and sent to the schemes to confirm settlement. The article states that the account's final cutoff is 10:45pm CT and cannot be changed; transactions submitted for settlement after that time enter the next day's settlement batch. This is an account-qualified batch-submission rule, not a settlement-completion or bank-arrival timestamp.
- Braintree says it disburses only after receiving processor confirmation that funds successfully settled. Funds are first disbursed to the linked PayPal account and swept from there to the bank account once per day. The page then says the merchant should see funds in the bank account 30–32 calendar days after the transaction settled. Settlement confirmation, PayPal-account disbursement, the daily sweep and bank visibility are distinct events.
- For a credit-card transaction paid in installments, the article says the merchant can expect an evenly divided portion every 30 days across the transaction's installment count, beginning 30–32 calendar days after settlement. A non-divisible remainder is expected in the final installment disbursement. These are qualified expectations anchored to settlement, not a promise that each bank deposit arrives on those dates.
- For debit cards, the article says payments can be expected in the PayPal account within two days and expressly excludes debit-card transactions from installments. It does not state the event from which the two days are counted. Bank-account disbursements occur every weekday, with a bank-holiday disbursement moved to the next business day.
- A settled transaction's Control Panel record exposes Disbursement Date and Settlement Amount. The article defines Disbursement Date as the date money was sent to the bank account and warns that it need not match the date funds appear there.
- PayPal payment disbursements are managed separately from the Braintree account. The linked PayPal funding page is navigation only here and was not used to infer its behavior.
- For an already-disbursed transaction, the article says the refunded amount can be expected to be applied within the next two business days once it has settled; for a transaction not yet disbursed, the amount is applied to the transaction pending disbursement. Installment refunds are divided across the sale's installment count: full refunds zero future installments, partial refunds adjust each installment, and already-disbursed installments can produce debits. Exact before-, during- and after-disbursement effects remain in the raw locators.

## Evidence boundaries

> [!warning] Event anchors and modal timing
> The page anchors credit-card bank visibility and the first installment disbursement to transaction settlement, but gives no starting event for the debit-card two-day PayPal-account expectation. It uses qualified phrases such as `should see` and `can expect`; do not turn the 30–32-calendar-day, every-30-day, two-day or two-business-day statements into guarantees or combine them into one service level.

> [!warning] Settlement, disbursement and arrival are different
> Processor confirmation of successful settlement precedes disbursement. Disbursement first reaches the linked PayPal account, the article describes a later sweep to the bank, and a Disbursement Date records when money was sent rather than when it appeared. None of these records alone proves bank arrival.

> [!warning] Captured Brazil route and unspecified currency
> Keep the cutoff, account path, payment-method handling, installment schedule, refund effects and timing within this captured BR/Brazil route and the applicable account. The page does not identify a currency, card brand, bank or scheme, and it does not establish current Brazil-wide policy or agreement with sibling account and regional articles.

## Detail locators

- Post-settlement prerequisite, linked PayPal Business Account, bank sweep, Braintree Direct funding ownership and support route: `# Settlement and Funding Timeline`, raw line 16.
- Credit-card batch purpose, fixed 10:45pm CT account cutoff and next-day treatment after the cutoff: `## Credit cards`, raw line 21.
- Processor-confirmed successful-settlement prerequisite, first disbursement to the linked PayPal account and once-daily bank sweep: `## Credit cards`, raw line 23.
- Settlement-anchored 30–32-calendar-day bank-visibility expectation: `## Credit cards`, raw line 25.
- Installment division, every-30-day cadence, settlement-anchored first disbursement and final-remainder handling: `## Installment Transaction disbursements`, raw line 30.
- Debit-card two-day PayPal-account expectation and installment exclusion: `## Debit cards`, raw line 35.
- Weekday bank disbursement and bank-holiday handling: `## Debit cards`, raw line 37.
- Control Panel route to Disbursement Date and Settlement Amount: `## Disbursement information`, raw lines 42–50.
- Disbursement Date sent-versus-appeared distinction: `## Disbursement information`, raw line 52.
- Separate PayPal payment disbursement route: `## PayPal`, raw line 57.
- Already-disbursed versus pending-disbursement refund treatment and qualified two-business-day timing: `## Refunds`, raw lines 62–64.
- Installment-refund division and full/partial effects before funds start disbursing: `### Installment Transaction Refunds > #### Refunds before funds have started disbursing`, raw lines 69–78.
- Already-disbursed debits, future-installment adjustments and partial-refund effects after disbursement begins: `#### Refunds after funds have started disbursing`, raw lines 81–87.
- Treatment after all installment funds have disbursed: `#### Refunds after all funds have been disbursed`, raw lines 90–92.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/br/reporting-reconciliation/reconciliation-2026-09-16|Braintree Brazil reconciliation]] - unread navigation-only destination linked for deposit reconciliation; not used as behavioral evidence here
- [[raw/braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16|Braintree PayPal funding and reconciliation]] - unread navigation-only destination linked for separately managed PayPal funding; not used as behavioral evidence here

## Raw Sources

- [[raw/braintree/articles/br/transactions/settlement-funding-timeline-2026-09-16|Braintree Brazil Settlement and Funding Timeline]] - fully read 2026-09-16 snapshot covering Braintree Direct card settlement batching, post-settlement disbursement, linked-PayPal-account and bank timing, installments, disbursement reporting, separate PayPal handling and refund adjustments
