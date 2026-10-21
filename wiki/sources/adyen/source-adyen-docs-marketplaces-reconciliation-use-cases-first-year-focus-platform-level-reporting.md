---
title: "Adyen Marketplace-level reporting use cases"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/first-year-focus/platform-level-reporting"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/first-year-focus/platform-level-reporting/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, reconciliation, profitability]
---

## Overview

This 2026-09-15 Marketplace first-year reporting guide offers **four proposed analyses** for product and finance teams: monthly profitability, transaction-level profitability, user-level profitability, and monthly invoice reconciliation. Each uses different report grains and account scopes. These are build recommendations and illustrative templates, not completed reconciliation or current account financial results. [[adyen]] [[adyen-reporting]]

## Key takeaways

- **Monthly indicator:** commission and costs affect the marketplace **liable balance account**; include other adjustments such as internal transfers and invoice deductions when reconciling cash. For scheduled liable-account payouts, filter the Payout Report to that account and sum payouts **initiated** during the period; alternatively filter the Balance Platform Accounting Report to the liable account and **value date**. The guide calls payout sum less Adyen-invoice costs only an **initial indication** of embedded-payments profitability. Month-end payout arrival may lag initiation/costs by a day, so initiation, balance debit and bank receipt are distinct (raw lines 28–48).
- **Transaction-level method applies only to blended pricing** in this guide; it explicitly separates IC++ markup economics. Join Payment Accounting `Psp Reference` with Balance Platform Accounting `Payment Psp Reference`. On the liable account, filter `captured`: a negative `Payment Fee for ...` entry versus a positive commission entry for the same payment. Processing Fees are **not** in Balance Platform Accounting; use Payment Accounting `Processing Fee`. Its alternative sums Scheme, Interchange and Processing fees for a PSP reference, filtering lifecycle `Record Type` to `SentForSettle` and `Received` to avoid unrelated stages (raw lines 50–95).
- The transaction analysis excludes fees not directly linked to a payment, such as non-transactional scheme, payout and KYC fees. The guide recommends a data warehouse because Balance Platform Accounting grows large. The per-location/user cost allowance and account-manager thresholds are dated suggestions with malformed currency text (`USD/EU/GBPR`); do not treat them as validated fee rates or eligibility rules (raw lines 93–95).
- **User-level method:** group PSP Payment References by AccountHolder for a month; use `captured` payments, `booked` internal/bank transfers and fees, and `refunded` refunds. Map each PSP reference to both user and liable-account credits, count carefully at payment grain rather than counting all captured split rows as distinct payments, sum liable-account commission, and obtain per-account-holder incurred fees from the Balance Platform Fee Report. The guide says a PSP reference has three captured line items and suggests request references/prefixes to disambiguate them; its exact split count is a worked-method assumption, not a universal row count (raw lines 97–139).
- **User formula caveat:** the text defines profit as user commission less total fees, but its effective-rate sentence ends “dividing the Profit by the User's” without naming the denominator. Do not implement that denominator from this sentence alone; the sample table is illustrative. The user analysis also excludes non-transactional fees (raw lines 104–141).
- **Invoice method:** the Payment Processing Invoice covers transaction processing; KYC, external-payout service and non-transactional scheme fees need separate attention. Reconcile transaction costs through the invoice guide, KYC lines on the invoice, and payout-service fees using Balance Platform Accounting `type: bankTransfer` / `status: booked` event counts for the invoice period. A Settlement details `InvoiceDeduction` entry is given as a comparison with monthly amount due; an entry or count alone is not evidence of beneficiary-bank receipt or invoice sign-off (raw lines 143–174).
- **Template discrepancy:** grouped Visa example commission `392,30` and fee `44.65` do not yield its shown profit `348.27` by simple subtraction. Treat worked figures and other sample rates as illustration, not accounting authority (raw lines 74–80).

## Detail locators

- Four jobs, monthly liable-account/payout/value-date methods and timing: raw lines 17–48.
- Blended-price transaction joins, fees and exclusions: lines 50–95. User-level joins, statuses, fee report and incomplete formula: lines 97–141. Invoice categories and report filters: lines 143–174.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — reporting and reconciliation concept.
- [[adyen-platforms]] — modern Marketplace/platform account context.
- [[source-adyen-docs-platforms-reconciliation-use-cases-first-year-focus-platform-level-reporting]] — separate Platforms-path use-case guide.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — payment accounting report route.
- [[source-adyen-docs-platforms-reports-and-fees-fee-report]] — balance-platform fee report route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/first-year-focus/platform-level-reporting/2026-09-15|Marketplace-level reporting — 2026-09-15 snapshot]]
