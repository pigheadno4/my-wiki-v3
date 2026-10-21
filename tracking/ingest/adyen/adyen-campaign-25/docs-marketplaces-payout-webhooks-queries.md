# Q1 — purpose and prerequisites

**Question:** Which payout events does this Marketplace guide route, and what setup and identifiers apply?

**Answer:** It documents `balancePlatform.transfer.created` for an initiated outgoing user-balance-account bank payout and `balancePlatform.transfer.updated` for status changes. It lists a payout service integration, webhook-receiving/accepting server, and Customer Area subscriptions to Transfer and Transaction webhooks. Payout Transfer events use `category=bank`, `direction=outgoing`, and `type=bankTransfer` (raw lines 19–44, 60–69). The EUR 100 sample is illustrative (line 58). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payout-webhooks]] → [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15]].

# Q2 — lifecycle and blocked retry boundary

**Question:** Does a booked payout prove bank receipt, and what do insufficient balance, returns and tracing imply?

**Answer:** No. `authorised` reserves source funds; insufficient balance gives `refused/notEnoughBalance`, requires funding then a **new** request (raw lines 138–140, 223–230). `booked` debits the balance account but is explicitly nonfinal; instant bank rejection can fail and regular/wire bank return can follow (lines 325–334). An ETA is only an estimate, and tracing IDs aid investigation; the snapshot limits ETA to local payouts and UK/US network examples for tracing (lines 830–836, 950–974). `tracking.status=credited` is the instant-priority bank-credit confirmation described by the page (lines 1111–1115). A permanent-return reason can block later attempts with HTTP 422 even though the reason table also includes some retry suggestions; there is no blanket retry rule (lines 1349–1355, 1532–1547). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payout-webhooks]] → [[raw/adyen/docs/marketplaces/payout-webhooks/2026-09-15]].
