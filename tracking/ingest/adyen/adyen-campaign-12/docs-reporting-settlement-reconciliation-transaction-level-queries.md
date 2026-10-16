# Fixed queries — Adyen transaction-level settlement reconciliation

## Q1 — purpose, scope, and what must not be inferred

**Query:** What is the reconciliation grain, and does a `MerchantPayout` report entry prove receipt in the merchant's bank account?

**Answer:** The guide reconciles transaction costs and payout amount within a single payout batch. Each report line is an entry and one transaction may have more than one entry. Sum Net Credit and subtract Net Debit to compare with the batch's `MerchantPayout` entry, whose payout amount appears under Net Debit and whose Modification Reference can serve as an accounting reference. The page provides no bank statement or receipt confirmation, so report matching does not prove bank arrival. Raw: `raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/2026-09-15.md:23-30,43-50,97-112`. Canonical route: `[[source-adyen-docs-reporting-settlement-reconciliation-transaction-level]]` → `[[adyen-reporting]]`.

## Q2 — central method, prerequisites, and exceptions

**Query:** Which reports and fields support the match, and how should external acquisition, costs and unsettled items be handled?

**Answer:** Start with the merchant-account Settlement details report. Under an external-acquirer arrangement, merge company-account External settlement entries selected for the merchant account, or reconcile the acquirer's own report separately. Match PSP and Merchant References; read Gross/Net Credit and Debit, fee columns, Type, Modification Reference, Gross Currency and Net Currency. Brazil credit-card installments require separate instructions. Weekend sales may fall in the next week's batch; other gaps include funds not yet settled, failed capture and uncancelled payments. Investigate open balances, aggregate settled amounts against sales, received-payment/accounting reports, and payment status logs. The guide's debit prose conflicts with its chargeback example on whether extra markup is subtracted or added, so do not apply a single unchecked debit formula. Raw: `raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/2026-09-15.md:19-41,52-95,114-134`. Canonical route: `[[source-adyen-docs-reporting-settlement-reconciliation-transaction-level]]` → `[[adyen-reporting]]`.
