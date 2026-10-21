# docs-marketplaces-reports-and-fees retrieval probes

## Q1 — Which reports does the Marketplace hub require for full monthly reconciliation, and how do scopes differ?

Answer: Full monthly reconciliation combines **Adyen account** and **balance platform** reports (raw line 32). On the account side, Payment accounting and Monthly invoice are marked required, while Settlement details is optional (lines 38–47). On the platform side, Balance Platform Accounting is marked required for balance changes across user and liable accounts; Balance and Statement reports cover daily opening/closing snapshots and changed-account events respectively (lines 49–57). Payment accounting omits platform charges for payouts, fund transfers and KYC (line 45); fee totals and details occur in different reports (lines 67–93).

Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reports-and-fees]] → [[raw/adyen/docs/marketplaces/reports-and-fees/2026-09-15]].

## Q2 — How are split payments and missing splits represented, and does a report row prove payout or bank receipt?

Answer: Split instructions at payment or capture direct balance-account debits and credits; each split appears as a separate `platformPayment` line in Balance Platform Accounting, matched by `Psp Payment Psp Reference` (raw lines 59–63). With no split instructions, the platform **liable account** is credited or debited, including the partial-refund example (line 65). Reports and fee tables describe accounting scope and rows; this hub does not establish a specific merchant's completed reconciliation, payout execution, or beneficiary-bank receipt (lines 30–78). Use report-specific field and date guides for those claims.

Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reports-and-fees]] → [[raw/adyen/docs/marketplaces/reports-and-fees/2026-09-15]].
