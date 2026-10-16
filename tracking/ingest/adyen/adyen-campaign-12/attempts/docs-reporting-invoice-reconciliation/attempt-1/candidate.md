---
title: "Adyen invoice reconciliation guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/invoice-reconciliation"
raw_files:
  - "adyen/docs/reporting/invoice-reconciliation/2026-09-15.md"
tags: [adyen, reporting, invoice-reconciliation, payment-processing-fees]
---

## Overview

Adyen's invoice reconciliation guide explains how to match transaction costs in the [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report|Payment accounting report]] to items on the monthly Payment processing invoice. It is a reconciliation workflow using two separate artifacts, not the Payment accounting report's field specification or proof that a payout reached a bank. [[adyen]] [[adyen-reporting]]

## Key takeaways

- The guide requires the Payment accounting report and invoice for the relevant month. For a full month, it directs an Interactive payment accounting report from the first day of that month at `00:00:00` through the first day of the next month at `00:00:00`, using Central European Time. The linked report reference owns account access, column definitions, and generation behavior; this guide states no user-role prerequisite.
- For a settled transaction, the guide says to identify `Received`, `Authorised`, `SentForSettle`, and `Settled` report entries. To total Adyen processing fees, select `Received` and `SentForRefund` entries and add their `Processing Fee` amounts in the stated `Processing Fee Currency`. Compare that total with the invoice's **Specification of amounts already deducted from settlement → Processing Fees → Subtotal**.
- If that amount differs from the invoice Summary's **Processing Fees** line, consult **Specification of final calculation including discounts**. The guide also says extra lines may cover externally acquired transactions or transactions refused by the risk engine; do not assume a single report subtotal explains every invoice line.
- Acquiring and payment-method fees are charged at `Settled` status in this guide. For those entries, total `Markup`, `Scheme Fees`, and `Interchange`, then compare with the invoice's calculated amounts and itemized fees. Differences between payment-method fee sections may arise from transaction-level versus aggregate rounding; the sample amounts illustrate that mechanism, not a merchant-specific fee outcome.
- The invoice's **Amount due** is month-end calculated costs minus amounts already deducted. The guide says it is added to or deducted from the next payout and appears as an `Invoice deduction` entry in the corresponding Settlement details report. That is an invoice and future payout booking relationship, not proof of final bank receipt, complete reconciliation, or correct accounting treatment. Do not collapse processing fee, acquiring fee, invoice amount due, and payment gross/net into one figure.

## Detail locators

- Opening and prerequisites, lines 19–24: two required artifacts and the exact Interactive report month window/time zone.
- `## Step 1`, lines 26–35: the four `Record Type` entries for a settled transaction.
- `## Step 2` and `## Step 3`, lines 37–62: processing-fee record types/currency/amount, invoice subtotal versus Summary, and additional-fee lines.
- `## Step 4`, lines 64–86: `Settled` acquiring/payment-method fee fields, invoice comparison, and rounding illustration.
- `## Step 5`, lines 88–90: `Amount due` and next-payout `Invoice deduction` relationship.

## Related

- [[adyen-reporting]] — Adyen reporting and reconciliation routes.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — report grain, fields, generation, and access qualifications.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — later payout-batch invoice-deduction entry.

## Raw Sources

- [[raw/adyen/docs/reporting/invoice-reconciliation/2026-09-15|Adyen invoice reconciliation guide, fetched 2026-09-15]]
