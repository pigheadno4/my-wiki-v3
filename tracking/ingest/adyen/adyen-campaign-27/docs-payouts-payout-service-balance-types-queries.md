# Retrieval checks — docs-payouts-payout-service-balance-types

Q1. What balance categories does this Payout Service-path page define, and how can per-currency balances be observed?

A1. For each currency of a balance-platform balance account, it defines Balance/current, Available, Pending, Pending available and Reserved; Pending can be positive or negative and Reserved includes authorized unbooked outgoing and blocked funds (raw lines 19–30). It points to `GET /balanceAccounts/{id}`, the balance-updated webhook or Customer Area balances for observation (raw lines 34–40). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-payouts-payout-service-balance-types]] → [[raw/adyen/docs/payouts/payout-service/balance-types/2026-09-15]].

Q2. Can the printed Available and Pending available formulas be implemented literally from this snapshot or used as payout proof?

A2. No. Available is printed as min(current, current − pending − reserved), but Example 1 yields EUR 50 by that formula while the table shows EUR 70, and Example 2 yields EUR 50 while the table shows EUR -20 (raw lines 24–25, 58–64, 78–86). Pending available is printed as min(pending, pending + available), but Example 2 yields EUR -90 while the table shows EUR -70 (raw lines 27–28, 78–84). These are unresolved source conflicts; the examples are not live booking, payout or bank-receipt evidence. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-payouts-payout-service-balance-types]] → [[raw/adyen/docs/payouts/payout-service/balance-types/2026-09-15]].
