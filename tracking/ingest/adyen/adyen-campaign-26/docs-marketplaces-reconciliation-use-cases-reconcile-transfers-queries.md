# docs-marketplaces-reconciliation-use-cases-reconcile-transfers retrieval probes

## Q1 — How does the Marketplace guide reconcile internal transfers versus payouts?

Answer: Use the **Balance Platform Accounting Report**: payouts from a holder balance account to an external bank/instrument use `Category: bank` and `Type: bankTransfer`; balance-account-to-balance-account movement uses `Category: internal` and `Type: internalTransfer` (raw lines 15–33). A **Transfer Id** links pending events; a populated **Transaction Id** on a `booked` row marks the booked balance movement. **Balance (PC)** is the signed amount (lines 24–33). Reference fields, webhooks and Customer Area help locate a particular transfer; the Statement Report is a daily changed-account alternative for payouts (lines 35–42, 57–59).

Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reconciliation-use-cases-reconcile-transfers]] → [[raw/adyen/docs/marketplaces/reconciliation-use-cases/reconcile-transfers/2026-09-15]].

## Q2 — How should the two-sided example be joined, and does booked payout mean bank receipt?

Answer: The EUR 15.00 internal-transfer table has a sender `-15.00` booked row and recipient `+15.00` booked row, **different Transfer Ids**, and the same illustrative booked **Transaction Id** (raw lines 44–55). Preserve balance-account identity, sign, status and CEST booking/value dates when reconciling. The guide's `booked` plus Transaction Id is balance-platform movement evidence (lines 28–33), including bankTransfer payout accounting; it does not independently prove that the external beneficiary bank credited funds or rule out a later return. Optional descriptors are recommended for matching (lines 35–42).

Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reconciliation-use-cases-reconcile-transfers]] → [[raw/adyen/docs/marketplaces/reconciliation-use-cases/reconcile-transfers/2026-09-15]].
