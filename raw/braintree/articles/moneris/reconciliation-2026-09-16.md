<!-- Source URL: https://developer.paypal.com/braintree/articles/moneris/reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation
slug: /articles/moneris/reconciliation/
createTime: '2025-04-01T22:16:51.073Z'
updateTime: '2025-04-01T22:16:51.094Z'
---



# Reconciliation

The best way to reconcile your debits and deposits is to compare the [Settlement Batch Summary Report](/braintree/articles/control-panel/reporting/settlement-batch-summary) – which is generated daily – with your [monthly statements](/braintree/articles/moneris/statements).


## Gross sales

If you’re looking to reconcile your gross sales, you can use the Settlement Batch Summary daily gross sales for reference. These daily sales should match the daily gross sales listed in the [Daily Activity Summary](/braintree/articles/moneris/statements#daily-activity-summary) on your Moneris statement.


## Deposits

If you’re interested in reconciling your daily transaction net sales with the deposits in your account, you can do so by comparing the Totals for each day in the Daily Activity Summary on your statement with the deposits in your account. You can also cross-reference the Totals in the Settlement Batch Summary with the deposits in your account.


## Refunds and voids

When you issue a refund, the refunded amount will be pulled from that day's [settlement batch](/braintree/articles/moneris/transactions/settlement-funding-timeline#settlement) prior to funding. If you do not have enough funds in your settlement batch to cover the refunded transaction, the remaining balance will be debited from your bank account.

The transaction fees associated with any voids issued within the month will be returned to you as a single small deposit on your account at the beginning of the following month. This deposit amount is calculated by Moneris using the count of voids, gateway rejections, and transactions with a $0 amount from the previous month.


## Reconciliation terminology

There are a few slight differences between the terms used on your Moneris statement vs. the Settlement Batch Summary. On your statement:


- Gross Sales are equal to Sales in the Settlement Batch Summary
- Returns are equal to Credits in the Settlement Batch Summary
- Net Sales are equal to Totals in the Settlement Batch Summary

