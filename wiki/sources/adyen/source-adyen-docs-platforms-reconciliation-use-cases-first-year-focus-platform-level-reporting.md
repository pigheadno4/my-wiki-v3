---
title: "Adyen Platforms platform-level reporting use cases"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/first-year-focus/platform-level-reporting"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/first-year-focus/platform-level-reporting/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, profitability, invoices]
---

## Overview

This 2026-09-15 Adyen for Platforms guide proposes four reporting use cases for a platform's product and finance teams: monthly embedded-payments profitability, transaction-level profitability, user-level profitability, and monthly invoice reconciliation. It gives report selection and join/filter guidance, with illustrative tables. These are planning and reconciliation methods, not proof that a particular platform completed a cash reconciliation, received a bank payout, or signed off its accounts.

## Key takeaways

- For monthly profitability, the liable balance account receives commission and costs. Cash reconciliation also considers other liable-account adjustments, including internal transfers and invoice deductions. The guide calls payouts from that account to a third-party bank less invoice costs an **initial indication** of profitability. With scheduled payouts, it recommends filtering the Payout Report by liable account and initiated-period payouts; alternatively, filter Balance Platform Accounting Report liable-account events by value date. Payout initiation, costs, and bank arrival can fall on different days around a month boundary.
- Transaction-level profitability in this section applies **only to blended pricing**; the guide distinguishes IC++ markup pricing. It joins Payment Accounting Report `Psp Reference` to Balance Platform Accounting Report `Payment Psp Reference`. On the liable account, `captured` rows distinguish a negative `Payment Fee for ...` fee entry from a positive commission entry. Processing Fees are absent from Balance Platform Accounting Report, so Payment Accounting Report must supply them; an alternative sums Scheme, Interchange, and Processing Fees after filtering lifecycle records to `SentForSettle` and `Received`. Multiple records per PSP reference and signed amounts make a naive one-row or unfiltered join misleading.
- Monthly user profitability groups PSP payment references by account holder and combines user-account and liable-account credits, captured payments, refunded entries, and booked transfer/fee entries at their respective grains. The guide suggests a platform-created unique reference/prefix in the accounting description to identify user versus liable transfers. User costs come from Balance Platform Fee Report's Fee Amount by account holder, with optional fee-type exclusions; profit is collected commission less selected costs. Its sample user table is illustrative, and its effective-rate sentence is incomplete in the raw, so the page does not establish a precise rate denominator.
- The transaction and user analyses expressly exclude costs not directly related to a transaction, such as nontransactional scheme, payout, and KYC fees. The raw also gives rough location/user cost recommendations with malformed currency abbreviations; treat them as dated illustrative planning guidance, not a tariff. It says the Balance Platform Accounting Report grows too large for scale without data warehousing.
- Monthly invoice reconciliation starts with the Payment Processing Invoice for transaction costs, then includes KYC service, payout service, and nontransactional scheme fees separately. The guide points to invoice lines for KYC, `bankTransfer`/`booked` event counts in Balance Platform Accounting Report for payout-service costs, and an `InvoiceDeduction` Settlement details report row matching the monthly amount due. These report entries are reconciliation checks, not independent evidence of bank receipt or finalized accounting treatment; invoice period, report grain, and amount basis must be aligned.

## Detail locators

- `## Monthly profitability`: liable-account adjustments, payout timing, Payout Report versus Balance Platform Accounting Report period filters.
- `## Transaction-level profitability`: blended-pricing scope, sample tables, PSP-reference join, signed fee/commission entries, fee-source and lifecycle filters.
- `## User-level profitability`: account-holder grouping, captured/refunded/booked status, created reference prefixes, fee aggregation and incomplete effective-rate sentence.
- `## Monthly invoice reconciliation`: Payment Processing Invoice, separate service/network fees, bankTransfer/booked count and InvoiceDeduction comparison.

## Related

- [[adyen-reporting]] — main provider reporting and reconciliation concept.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/first-year-focus/platform-level-reporting/2026-09-15|Adyen platform-level reporting use cases (fetched 2026-09-15)]]
