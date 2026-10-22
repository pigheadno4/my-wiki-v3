---
title: "Adyen Payout Service fee reconciliation routes"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reconciliation-use-cases/reconcile-fees"
raw_files:
  - "adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-fees/2026-09-15.md"
tags: [adyen, payout-service, fees, invoice-reconciliation, reporting]
---

## Overview

This 2026-09-15-captured [[adyen]] Payout Service page routes invoice-fee reconciliation by money movement: payment/pay-in fees on the payment-processing PSP side, bank-payout fees on Balance Platform, and card payouts initiated from Balance Platform. Each route uses different report grain and account scope. It describes how to compare records, not proof that a particular invoice has been reconciled. See [[adyen-reporting]].

## Key takeaways

- **Payment/pay-in fees:** For fees arising on the payment-processing PSP side, use the Settlement Details Report or Payment Accounting Report. The latter covers payment-lifecycle status changes, events and modifications for transactions, allowing costs by status to be compared for invoice reconciliation. This is separate from the Balance Platform payout-fee route. See pinned raw lines 19–21.
- **Bank-payout fees:** Compare payout fees on the Balance Platform invoice with the Balance Platform Accounting Report or Statement Report. Filter **Booking date** to the invoice month in **CET**, then filter `Category=bank`, `Type=bankTransfer`, and `Status=booked`. For priority, the Accounting Report's Brand variant field has an illustrated `payment_banktransfer_instantBanktransfer` instant-priority value; it is an example label, not a universal fee amount. See pinned raw lines 23–33.
- **Balance Platform card payouts:** Use the Settlement Details Report for the merchant account(s) used for card payouts together with the Balance Platform Accounting Report for the instructing balance account(s). An SDR `BPPaidOut` line carries Adyen Markup, Scheme fees and Interchange. Its `Net Debit (NC)` is **fees only**, not payout amount plus fees. The capture/card-payout amount is on Balance Platform reports; match SDR `Merchant Reference` ID to Accounting Report `Transfer Id` on a `booked` row. See pinned raw lines 35–46.
- **Amount and evidence boundary:** Keep the SDR `(NC)` fee columns distinct from the balance-platform card-payout/capture amount. The page supplies no numerical fee or currency conversion example, and a booked report row or matching IDs does not establish recipient receipt or completed invoice sign-off. See pinned raw lines 39–46.

## Detail locators

- PSP-side payment/pay-in fee reports: pinned raw lines 19–21.
- Balance Platform invoice and bank-transfer fee filters, month and priority: pinned raw lines 23–33.
- Card-payout account scope, `BPPaidOut` fee fields and Transfer Id match: pinned raw lines 35–46.

## Related

- [[adyen-reporting]] — reciprocal report/reconciliation route.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — Balance Platform Accounting Report field definitions.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-fees/2026-09-15|Payout Service reconcile fees, captured 2026-09-15]]
