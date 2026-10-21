# C24 Marketplace reserve-account retrieval checks

## Q1 — What is the reserve account for, and how is it funded?

It is a balance account linked to the platform's liable account holder and supplies collateral for transfers that create negative user balances; a current-balance payout configuration is an example use (raw lines 19–23). The guide lists internal balance-account transfer, split-payment credit to reserve, or top-up as ways to increase available reserve funds (raw lines 34–42). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-reserve-account]] → [[raw/adyen/docs/marketplaces/manage-reserve-account/2026-09-15]].

## Q2 — What fails when funds are insufficient, and what does this reserve not cover?

For a transfer that would make a user balance negative, Adyen checks reserve availability; insufficient funds fail the request. Otherwise it blocks collateral equal to the negative amount, processes the transfer, and releases the block when the user balance is replenished enough (raw lines 25–32). This reserve covers transfer-caused deficits; the separate reserved compensation account covers negative balances caused by refunds or chargebacks (raw lines 19–21). Neither a requested transfer nor blocked collateral proves a bank payout. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-reserve-account]] → [[raw/adyen/docs/marketplaces/manage-reserve-account/2026-09-15]].
