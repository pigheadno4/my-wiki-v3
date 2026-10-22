# C28 Payout Service balance reconciliation retrieval checks

## Q1 — Purpose and report route

**Query:** How does the Payout Service guide match merchant-account settlements to balance-platform movements each day and month?

**Answer:** It treats each settled payable batch as one balance-platform incoming internal transfer (raw lines 17–19, 62–66, 148). Daily, match BPSR `InternalTransfer`/`settlementBatch` entries to SDR `MerchantPayout` entries by batch, amount/description and BPSR Value Date versus SDR Creation Date or `Booking Date (AMS)` (raw lines 144–164). Monthly, compare booked BPIAR internal transfers with target-month Value Date to ASDR MerchantPayout totals across the relevant merchant accounts (raw lines 176–194). SDR/ASDR use merchant-account booking dates, BPSR transfer value date, and BPIAR transfer booking date, with CE(S)T and merchant-time-zone qualifications (raw lines 131–143). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-payouts-payout-service-reconcile-balances]] → [[raw/adyen/docs/payouts/payout-service/reconcile-balances/2026-09-15]].

## Q2 — Qualification and example conflict

**Query:** Can every balance platform use the dashboard instead of reports, and do the examples establish a booked payout or bank receipt?

**Answer:** No. The Liable account summary dashboard route is specified only for a balance platform with one account holder; multiple holders use reports (raw lines 205–207). That route first calls for ASDR, then names SDR in its count and total checks, so the report label/grain is unresolved in the example (raw lines 217–222). The daily worked example says to generate SDRs for both 16 and 17 July when the sales day crosses CET dates but links only a 17 July sample (raw lines 168–174). The sample transfer-created webhook is `received`, not booked (raw lines 97–127), and report matching does not prove third-party bank credit. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-payouts-payout-service-reconcile-balances]] → [[raw/adyen/docs/payouts/payout-service/reconcile-balances/2026-09-15]].
