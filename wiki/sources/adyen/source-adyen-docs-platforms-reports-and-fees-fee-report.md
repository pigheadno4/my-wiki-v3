---
title: "Adyen Balance Platform Fee Report"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees/fee-report"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/fee-report/2026-09-15.md"
tags: [adyen, platforms, reporting, fees, reconciliation]
---

## Overview

This 2026-09-15 Adyen guide defines the monthly Balance Platform Fee Report for payment and processing fees incurred by balance-platform users. Its row grain in the documented sample is billing month, balance platform, account holder/balance account, fee type/name, currency and fee amount; the listed standard columns contain no transaction ID. The report helps compare user-level fees with invoice deductions and margins, but it reports where a fee was incurred rather than where it was billed or which account was debited. See [[adyen]], [[adyen-platforms]] and [[adyen-reporting]].

## Key takeaways

- **Scope and timing:** The report is available monthly on the first day of the month. It covers transactional costs such as processing, scheme, interchange, chargeback and refund fees. It can be generated on a Customer Area schedule or manually for a specific month, and the page gives a balanceplatform_fee_report_YYYY_MM.csv naming pattern. The guide's report description does not establish that a particular month's file was generated, delivered or complete.
- **Incurred versus billed:** Fees that cannot be tied to a platform user are reported on the liable account. This identifies where the fee was incurred for reporting; the page explicitly says it does not identify where fees were billed. Do not read a row's AccountHolder or BalanceAccount as the actual fee-debit account, seller/payee identity, or a settled money movement.
- **Reconciliation grain:** Use API responses and webhooks for the latest individual assessed-fee status and ledgers, then compare monthly fee totals against the report and monthly invoice. The report's sample is grouped by account and fee type/name, with positive and negative Fee Amount examples, but gives no transaction ID or universal sign interpretation. A report row or invoice comparison alone does not prove an actual balance debit, bank payout or accounting sign-off.
- **Schema boundary:** Standard columns are Billing Month, BalancePlatform, AccountHolder, BalanceAccount, Fee Type, Fee Name, Currency Code and Fee Amount. Optional account-holder and balance-account descriptions/references can be added from Customer Area. The sample table labels its currency column Currency whereas the standard-column table says Currency Code; the page also says generated reports may have extra data/columns depending on platform settings. Use the actual report header for ingestion and reconciliation.

## Detail locators

- Monthly fee purpose, incurred-versus-billed boundary, generation and filename: pinned raw lines 15-31.
- Reconciliation guidance and sample-file qualification: pinned raw lines 33-45.
- Illustrative rows, including positive and negative fee amounts: pinned raw lines 47-73.
- Standard and optional column definitions: pinned raw lines 75-105.

## Related

- [[adyen-reporting]] — main reporting concept and reciprocal source route.
- [[adyen-platforms]] — platform/user and liable-account context.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — related balance-change report at a different grain.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — related payout reporting at a different grain.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/fee-report/2026-09-15|Adyen Balance Platform Fee report, captured 2026-09-15]]
