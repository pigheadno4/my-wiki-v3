# Q1 — purpose and viewing route

**Question:** Which per-currency balance categories does the Marketplace guide define, and how can they be viewed?

**Answer:** It defines Balance/current as already settled transactions, Pending as future-settlement transactions that may be positive or negative, Reserved as authorised unbooked outgoing-transfer funds and other blocked funds, plus Available and Pending available (raw lines 19–30). A balance account may hold multiple currencies; the page routes to GET `/balanceAccounts/{id}`, `balancePlatform.balanceAccount.balance.updated`, and Customer Area **Balance accounts > Balances** (lines 34–40). These are account-balance reads, not payment or payout confirmation. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-types]] → [[raw/adyen/docs/marketplaces/balance-types/2026-09-15]].

# Q2 — formula/example boundary

**Question:** Can the printed Available and Pending available formulas be used directly for payout controls?

**Answer:** Not from this snapshot without resolving its internal conflict. The page prints Available as the lower of current and current minus pending-plus-reserved (raw lines 23–25). Example 1's EUR 100 current, EUR 20 pending and EUR 30 reserved would yield EUR 50, yet its table says EUR 70 (lines 58–64). Example 2's EUR 50 current, EUR -70 pending and zero reserved would yield EUR 50 but its table says EUR -20 (lines 72–86). Printed Pending available is lower of pending and pending plus available (lines 27–28); Example 2's -70 pending and -20 available would yield -90, while its table says -70 (lines 78–84). The examples illustrate future refunds and negative availability, not an executable reconciled formula. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-types]] → [[raw/adyen/docs/marketplaces/balance-types/2026-09-15]].
