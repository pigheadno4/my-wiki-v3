# Fixed queries — docs-platforms-reports-and-fees

## Q1 — purpose, scope, and non-inference

**Query:** What does this Platforms reports-and-fees page select, and does its report map complete a reconciliation?

**Answer:** It maps Adyen-account reports for processing/invoices and balance-platform reports for account-holder-linked balance events, then routes to split and fee reporting (raw lines 15–57). It says full monthly financial reconciliation needs reports from both account scopes and labels Payment accounting, Monthly invoice and Balance Platform Accounting as required, Settlement details optional (lines 30–55). It is a report-selection hub; catalog entries or report availability do not prove a complete month close, a booked payout, beneficiary-bank receipt, legal fund ownership or specific fee assessment. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees]] → [[raw/adyen/docs/platforms/reports-and-fees/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** How does the hub locate split lines and distinguish payment, processing and platform-service fees across reports?

**Answer:** It says split payment/capture credits or debits appear as separate `platformPayment` lines in Balance Platform Accounting Report, matched by `Psp Payment Psp Reference`; without instructions it describes liable-account booking, including a partial-refund example, while detailed transaction behavior belongs to split guides (raw lines 59–65). Balance Platform Accounting covers fees for captured funds booked to balances; Payment accounting includes all per-transaction payment fees and Processing fees that may have no booked funds; Monthly invoice totals assessed fees and adjustments, including platform-service examples; Settlement details holds aggregate Processing-fee and invoice-adjustment lines (lines 67–93). Fees are deducted from settlement and default to the liable balance account, but the table is not a price or charge-specific proof (lines 69–93). The page gives no field-level schema for each linked report, bank-receipt status or completed reconciliation procedure. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees]] → [[raw/adyen/docs/platforms/reports-and-fees/2026-09-15|pinned raw]].
