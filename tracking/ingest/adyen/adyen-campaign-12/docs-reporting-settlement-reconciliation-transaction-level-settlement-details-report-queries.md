# Fixed queries — docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report

## Q1 — purpose, scope, and what not to infer

**Question:** What does the Settlement details report cover, at what grain, and does a report row prove final bank receipt?

**Expected answer:** It is a merchant-account settlement and transaction-cost reconciliation report; it can combine selected merchant accounts, defaults to per-merchant-account per-batch generation, and each line below the header is a separate entry that may be a transaction or another booking type. A MerchantPayout row describes a payout from the batch and provides a bank-statement reference; the snapshot alone does not prove final bank receipt for a particular payout. Route through [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] → [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/settlement-details-report/2026-09-15]]. Raw locators: opening paragraph line 19; `Generate and download reports` lines 31–37; `Report structure > Entries` lines 130–199; `Journal types` lines 322–365.

## Q2 — central capability, prerequisites, and warnings

**Question:** How is the report generated and interpreted for automated reconciliation, including access and field warnings?

**Expected answer:** Generate manually or on a daily, weekly, monthly, or batch-close schedule; downloading and generation require Merchant Report or Generate key financial reports for every included merchant account. Interpret Gross Currency and gross debit/credit as transaction amounts and Net Currency and net debit/credit as payable-batch settlement amounts. Fee breakdown depends on whether the acquirer provides interchange-level data; externally settled refund commission can be negative, and externally settled payment Exchange Rate is only Adyen's reference rate. Account time-zone settings and date-column variants matter. Additional columns or changed order can affect automated consumers. Route through [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] → [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/settlement-details-report/2026-09-15]]. Raw locators: lines 25, 31–103, 204–245, 246–319.
