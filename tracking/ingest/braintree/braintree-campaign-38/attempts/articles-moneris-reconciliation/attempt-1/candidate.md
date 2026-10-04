---
title: "Braintree Moneris Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/reconciliation"
raw_files:
  - "braintree/articles/moneris/reconciliation-2026-09-16.md"
tags: [braintree, moneris, reconciliation, settlement, reporting]
---

## Overview

This Braintree-hosted webpage snapshot describes reconciliation for the Moneris account route. It says the best way to reconcile debits and deposits is to compare the daily-generated Settlement Batch Summary Report with monthly Moneris statements. This is captured Braintree documentation, not evidence that sibling account or processor routes are equivalent, independent Moneris processor authority, current policy, or proof that any individual deposit arrived.

## Key takeaways

- For gross sales, the page says the Settlement Batch Summary daily gross sales should match the Daily Activity Summary daily gross sales on the Moneris statement.
- For daily transaction net sales, compare each day's Daily Activity Summary Totals with account deposits; the page also permits cross-referencing Settlement Batch Summary Totals with account deposits.
- A refund is pulled from that day's settlement batch before funding. If the batch lacks enough funds, the remaining balance is debited from the bank account.
- Transaction fees associated with voids issued during a month are returned as one small account deposit at the beginning of the following month. The page says Moneris calculates that deposit from the previous month's counts of voids, gateway rejections, and zero-amount transactions. It does not state a currency, fee rate, or account-pricing schedule.
- Statement terminology maps Gross Sales to Settlement Batch Summary Sales, Returns to Credits, and Net Sales to Totals.

## Detail locators

- `# Reconciliation` (lines 14–16): daily Settlement Batch Summary Report and monthly statement comparison.
- `## Gross sales` (lines 19–21): Daily Activity Summary gross-sales match.
- `## Deposits` (lines 24–26): daily Totals-to-account-deposit comparison.
- `## Refunds and voids` (lines 29–33): refund funding order, insufficient-batch debit, and next-month void-fee deposit calculation.
- `## Reconciliation terminology` (lines 36–43): statement-to-report term mappings.

## Related

- [[braintree]]
- [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/moneris/reconciliation-2026-09-16|Braintree Moneris Reconciliation (2026-09-16 snapshot)]]
