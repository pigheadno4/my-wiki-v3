---
title: "Braintree Wells Flat Pricing and Fees"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/pricing-fees"
raw_files:
  - "braintree/articles/wells-flat/pricing-fees-2026-09-16.md"
  - "braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16.md"
tags: [braintree, wells-flat, pricing, transaction-fees, refunds, chargebacks]
---

## Overview

This collected Braintree Wells Flat article describes Braintree transaction-fee treatment, where a merchant account's processing rates are listed, percentage-fee rounding, and refund and dispute-related fee treatment. It is a snapshot of Braintree's account- and region-scoped documentation, not a merchant-specific contract, a current universal rate schedule, or independent bank policy.

## Key takeaways

- Braintree processing and cross-border fees apply only to successful transactions and are deducted from daily disbursements; the article excludes verifications, declines, gateway rejections, and voids. A merchant using its own American Express account is charged a Braintree per-transaction fee in addition to fees paid directly to Amex.
- The article says Braintree does not charge fees for PayPal transactions, while PayPal processing fees still apply. This is the collected page's product-specific treatment, not a statement that PayPal transactions are fee-free.
- Processing rates are not displayed in the Control Panel. The article routes merchants to the Pricing Schedule on each merchant account's statement for discount, cross-border, per-transaction, and chargeback rates, and to the Transaction-Level Fee report for assessed transaction fees.
- Percentage-based fees are rounded to the nearest unit at transaction level using the third decimal digit, so multiplying a monthly settled-sales total by a rate may differ slightly from statement fee details.
- Full and partial refunds do not incur an additional refund fee, but the original Braintree processing fees are not returned.
- In this snapshot, the bank managing a chargeback or pre-arbitration charges a non-refundable $15 fee regardless of outcome, while retrievals do not incur that fee "at this time." Treat the amount and retrieval treatment as snapshot-scoped rather than current, universal, or independent bank policy.

> [!warning] Contradiction
> The fully read [[source-braintree-articles-wells-flat-braintree-marketplace-statements-reconciliation|Wells Flat Marketplace statements and reconciliation source]] and its [[raw/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16|raw line 156]] instruct merchants to round down and link to a missing `#rounding-down` target. This pricing page instead specifies 0–4 down and 5–9 up. The collected pages conflict and do not establish current account rounding policy.

## Detail locators

- PayPal fee carveout: `## Transaction fees > NOTE`, lines 20-21.
- Fee-category inventory, successful-transaction application, daily-disbursement deduction, excluded outcomes, and own-Amex-account treatment: `## Transaction fees`, lines 25-36.
- Statement Pricing Schedule and Transaction-Level Fee report routes: `### Braintree processing fee rates` and `### Transaction-level fees`, lines 39-55.
- Transaction-level percentage-fee rounding method and examples: `## Standard rounding`, lines 58-67.
- Refund treatment: `## Refunds`, lines 70-72.
- Chargeback, pre-arbitration, and retrieval fee treatment: `## Chargebacks, retrievals, and pre-arbitrations`, lines 75-77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Reporting context: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16|Braintree Transaction-Level Fee report]] - unread navigation-only destination linked for transaction-level fee reporting; not used as factual evidence here
- [[raw/braintree/articles/wells-flat/statements-reconciliation-2026-09-16|Braintree Wells Flat statements and reconciliation]] - unread navigation-only destination linked for reconciliation context; not used as factual evidence here
- [[raw/braintree/articles/wells-flat/chargebacks-retrievals-prearbs-2026-09-16|Braintree Wells Flat chargebacks, retrievals, and pre-arbitrations]] - unread navigation-only destination linked for dispute context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/wells-flat/pricing-fees-2026-09-16|Braintree Wells Flat Pricing and Fees]] - fully read collected article covering successful-transaction fee treatment, statement-based rates, transaction-level reports, rounding, refunds, and dispute-related fees
- [[raw/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation-2026-09-16|Braintree Marketplace Statements and Reconciliation]] - fully read cross-page conflict evidence whose line 156 says to round down and links a missing pricing-page `#rounding-down` target
