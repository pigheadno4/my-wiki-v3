# Fixed retrieval checks — Adyen batch-level reconciliation

## Q1 — Purpose, scope, and non-inference

**Question:** What does this page help reconcile, and why is a report row not proof of bank receipt or a single transaction?

**Expected answer:** It uses the Aggregate Settlement Details Report to find payout batches for a date range and compare report amounts with a bank statement. A Batch Number can span multiple rows by creation date, payment method, journal type, and currency. A `Settled` entry is an aggregate for a group of transactions. The page supplies no particular bank-statement entry or receipt confirmation, so its report row or `Net Credit` description cannot alone prove that a specific payout reached the bank.

**Raw locators:** Introduction lines 17–21; `Step 1` lines 23–34; `Step 2` lines 60–68.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-batch-level]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** How does the guide identify batches and calculate settled-entry totals, and which currency/journal distinctions matter?

**Expected answer:** Use `Batch Number` to locate a batch in the Aggregate Settlement Details Report. For `Settled` entries, `Gross Credit` is the total for a transaction group, `Bank/Card Commission` and `DCC Markup` are deductions, `Num Txs` is its count, and `Net Credit` is gross minus those two deduction columns. This is a `Settled`-entry formula, not a blanket formula for `Balancetransfer` or other journals. Batch 604's example includes multiple currencies and both `Settled` and `Balancetransfer` rows; batch 608's EUR-only example sums net credits, commission, and counts. Do not sum unlike currencies or treat debit and credit columns as an undocumented universal sign convention.

**Raw locators:** `Step 1` lines 25–58; `Step 2` lines 60–82.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-batch-level]] → [[raw/adyen/docs/reporting/settlement-reconciliation/batch-level/2026-09-15|pinned raw snapshot]].
