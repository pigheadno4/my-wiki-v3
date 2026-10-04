---
title: "Braintree Brazil Statements"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/statements"
raw_files:
  - "braintree/articles/br/reporting-reconciliation/statements-2026-09-16.md"
tags: [braintree, brazil, statements, reporting, reconciliation, fees]
---

## Overview

This 2026-09-16 snapshot of Braintree's Brazil-route Statements article describes the monthly merchant statement as a reconciliation aid and explains permission-gated access through the Braintree Control Panel. Its statement summary covers the prior month's disbursements, processing and fees; the detailed sections identify statement-period sales, refunds, chargebacks, credits and fees rather than proving that any individual bank deposit arrived. [[braintree]] [[payment-reconciliation-reporting]]

## Key takeaways

- A user needs the **View Statements** role permission to access monthly merchant statements in the Control Panel. The article routes the user through **Reports** to **Statements**.
- The Disbursement Summary combines gross sales with refunds, credits and fees and shows the net amount disbursed to the merchant's PayPal account for the statement period. Disbursement Details groups daily amounts by the date funds were disbursed to that PayPal account and says those funds are then swept to the bank; this is a documented route, not evidence of actual arrival.
- Date labels are not interchangeable: the article says the Disbursement Report date is the PayPal payout date to the bank and is at least one day later than the date shown in the statement's Braintree Disbursement Details section.
- Braintree Fee Details distinguishes fee or credit type, quantity created during the statement period and amount credited or debited during that period. The Pricing Schedule is the article's route to the selected merchant account's discount, per-transaction and chargeback rates; the snapshot does not establish a transaction or settlement currency, despite using the phrase "static dollar amount" when defining a per-transaction fee.
- The article says Braintree processing fees apply only to successful transactions and are deducted from daily disbursements; verifications, declines, gateway rejections and voids do not incur those fees. It separately says Braintree does not charge fees for PayPal transactions and that PayPal processing fees apply.
- Fee calculations round down remainders beyond the penny at transaction level, so multiplying a fee rate by a month's total settled sales can differ slightly from statement fee details. Refunds or credits add no fee, but whether previously charged Braintree processing fees are credited back for a fully refunded transaction depends on when the merchant began processing with Braintree.
- The bank managing a chargeback or pre-arbitration charges a non-refundable fee; the snapshot says retrievals do not result in a fee "at this time." Treat these as captured article statements, not current independent bank or pricing authority.

## Detail locators

- **Statement purpose and contents:** raw lines 14–29.
- **Permission and Control Panel route:** raw lines 32–40.
- **Summary, processing and fee-detail sections:** raw lines 42–79.
- **Disbursement composition and date-label warning:** raw lines 82–100.
- **Transaction-fee categories, event qualification and merchant-account Pricing Schedule route:** raw lines 103–141.
- **Rounding, refund-credit condition and chargeback/pre-arbitration fee treatment:** raw lines 144–160.

## Qualifications

This is a Braintree-hosted snapshot of the `/br/` article fetched on 2026-09-16. It does not show that sibling regional or processor-specific statement guides are equivalent, does not establish current pricing, currency or bank policy, and does not prove that a reported disbursement reached a PayPal or bank account. Account-specific rates remain tied to the Pricing Schedule for the merchant account selected in the statement workflow.

## Related

- [[braintree]]
- [[payment-reconciliation-reporting]]

## Related raw API references

The article links to separate reconciliation, Disbursement Report, Transaction-Level Fee report, role-permission and chargeback materials. Those targets were not read for this entry and are navigation only.

## Raw Sources

- [[raw/braintree/articles/br/reporting-reconciliation/statements-2026-09-16|Braintree Brazil Statements (2026-09-16 snapshot)]]
