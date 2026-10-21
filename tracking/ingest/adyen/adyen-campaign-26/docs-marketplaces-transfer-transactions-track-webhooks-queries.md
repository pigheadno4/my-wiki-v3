# C26 transaction webhook retrieval checks

## Q1 — Meaning and prerequisites

**Query:** When is a Marketplace transaction webhook emitted, and what setup does the guide require?

**Answer:** `balancePlatform.transaction.created` reports a debit from or credit to a balance account when transfer funds are booked, in contrast with Transfer webhooks for transfer-status changes (raw lines 19–21, 75–83, 156–164, 218–226, 274–284). The page lists Adyen for Platforms, Issuing or Payouts integrations, Standard and Transaction webhook subscriptions, optional Transfer webhooks, and a server able to receive and accept webhooks (raw lines 23–31). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transfer-transactions-track-webhooks]] → [[raw/adyen/docs/marketplaces/transfer-transactions/track-webhooks/2026-09-15]].

## Q2 — Money-flow and example boundary

**Query:** Do the webhook examples prove external bank receipt or provide canonical third-party top-up and cross-event IDs?

**Answer:** No. The negative outgoing samples refer to the source balance account; the positive incoming samples refer to the target balance account (raw lines 75–127, 156–207, 218–272, 274–327). A booked balance-account mutation is not evidence of beneficiary-bank credit. The incoming-external narrative calls the transfer third-party, but its sample has `categoryData.type: platformPayment` and PSP references (raw lines 218, 243–253). Distinct outgoing categories reuse a sample transaction ID, as do distinct incoming categories (raw lines 94–105, 175–186, 237–253, 295–306), so do not join examples by those IDs. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transfer-transactions-track-webhooks]] → [[raw/adyen/docs/marketplaces/transfer-transactions/track-webhooks/2026-09-15]].
