---
title: "Adyen payment processing invoice"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice"
raw_files:
  - "adyen/docs/reporting/invoice-reconciliation/payment-processing-invoice/2026-09-15.md"
tags: [adyen, reporting, invoice, invoice-reconciliation, processing-fees]
---

## Overview

This Adyen guide explains the monthly **Payment processing invoice** as an itemized statement of Adyen payment-service costs and how its billed amounts relate to deductions from settlement batches. The invoice period is **CET-based**. It is described for a company account and merchant accounts linked to the same legal entity; a merchant account tied to a different legal entity receives a separate invoice. This page was last modified in 2022 and captured 2026-09-15. Invoice figures and settlement deductions are distinct evidence; neither alone proves final bank payout or correct accounting treatment. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Scope, period and access:** Adyen says it provides a monthly company-account invoice covering payment-processing costs of linked merchant accounts with the same legal entity; a different-legal-entity merchant account gets a separate invoice. The invoice is always based on CET. Viewing/downloading in Customer Area under **Reconciliation > Invoices** requires either **Merchant financial** or **Manage key financial tasks** role. These are the page's dated access and grouping claims, not proof of current grants or merchant-of-record identity.
- **Costs and exceptions:** The summary itemizes transaction fees and commissions; the details page gives a final fee calculation **including discounts** and a table of amounts already deducted from settlement. Optional additional pages break details down by merchant account. Ordered payment terminals are invoiced separately. Sales tax/VAT is **not** deducted from settlement batches; the page gives historical US and French examples where applicable taxes appear on invoices. Do not infer a universal tax charge or a tax payment outcome from those examples.
- **Two different amounts:** **Already deducted from settlement** totals fees and commissions taken from payout batches, with report routes to Interactive payment accounting and Settlement details. **Amount due** is the amount owed that has not been deducted from settlement; it can be positive or negative. The invoice can differ from settlement-batch deductions during the month, with a credit/debit difference described for the next corresponding merchant-account settlement batch. Reasons named include tiered pricing, month-end commission timing and midmonth price changes. The invoice's Payment instructions explain next-batch treatment; an invoice figure is not proof that a future deduction or credit was executed.
- **Reconciliation boundary:** Match the invoice's CET period, legal-entity/merchant-account scope, fee/discount calculation, tax treatment and already-deducted lines against the appropriate payment-accounting and Settlement details entries. This page gives no universal invoice currency or standalone bank-arrival evidence; use the actual invoice and report amount/currency fields before reconciling figures.

## Detail locators

- Lines 15–23: invoice purpose, CET period, company/merchant-account and legal-entity grouping.
- `## Common discrepancies and exceptions`, lines 25–36: separate terminal invoices, next-batch differences and tax treatment/examples.
- `## Get your invoice`, lines 38–47: Customer Area role and access route.
- `## Structure`, lines 49–70: summary, details, optional merchant breakdown, discounts, already-deducted and Amount due definitions.
- `## Amount due`, lines 72–80: positive/negative amount, timing/pricing causes and next-batch Payment instructions.

## Related

- [[adyen-reporting]] — reciprocal reporting route.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — separate payment-entry and CET invoice-window evidence.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — separate settlement-entry and deduction evidence.
- [[adyen-account-structure]] — account hierarchy versus legal or payment ownership.

## Raw Sources

- [[raw/adyen/docs/reporting/invoice-reconciliation/payment-processing-invoice/2026-09-15|Payment processing invoice, captured 2026-09-15]]
