# Fixed queries — docs-platforms-reports-and-fees-payout-report

## Q1 — purpose, scope, and non-inference

**Query:** What does the Balance Platform Payout Report cover, at what grain, and does it prove bank receipt?

**Answer:** The page describes a daily report for platforms with scheduled daily, weekly or monthly sweeps, covering payouts processed midnight-to-midnight CEST and transactions contributing debit/credit amounts; no payout day produces an empty report (raw lines 15–29). Filter by Account Holder, Balance Account and Currency. Although prose says one record per account/currency, the sample has multiple transaction rows and a payout row for the same account/currency, so do not collapse those grains (lines 31, 49–68). The report is platform ledger/reconciliation evidence, not a beneficiary-bank receipt, legal ownership proof or live payout-success guarantee. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees-payout-report]] → [[raw/adyen/docs/platforms/reports-and-fees/payout-report/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** Which identifiers, signs, rolling balance and date fields matter when reconciling a scheduled payout?

**Answer:** Standard columns distinguish Transfer Id for a pending debit/credit from Transaction Id for a completed one; Category/Type/Status identify rows, `Balance (PC)` is debit/credit amount in payment currency, and Rolling Balance (PC) accumulates those amounts (raw lines 80–117). The sample has positive capture rows and negative booked `bankTransfer` rows, with rolling balance zero after full payout; these are illustrative signs, not a bank-credit confirmation (lines 49–68, 104–105). Pending refunds/chargebacks can be withheld, carrying a non-zero rolling balance into the next report; the page directs readers to Accounting Report transfers booked before but valued after the payout date (lines 33–37). Booking Date, Value Date, and Payout Date have distinct meanings, with separate booking/value time-zone fields. The page uses CEST for report window/availability and CET for Payout Date initiation, so keep those labels qualified (lines 21–25, 89–92, 117). Customer Area report settings may add columns; sample data is not exhaustive (lines 43–45, 119–133). Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees-payout-report]] → [[raw/adyen/docs/platforms/reports-and-fees/payout-report/2026-09-15|pinned raw]].
