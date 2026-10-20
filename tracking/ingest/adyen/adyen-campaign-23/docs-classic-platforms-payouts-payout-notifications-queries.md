# C23 Classic Platforms payout notification retrieval checks

## Q1 — What does each `ACCOUNT_HOLDER_PAYOUT` status mean?

After initiation, the Classic event reports `Initiated`, `Confirmed` or `Failed` status updates (raw lines 16–22). `Initiated` means scheduled for bank dispatch, with an estimated arrival date; `Confirmed` (Notification v5+) means funds left Adyen and are in transit to the holder's bank; `Failed` reports a reason such as invalid/closed bank details, returned funds or payout validation error (raw lines 24–34, 47–56). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] → [[raw/adyen/docs/classic-platforms/payouts/payout-notifications/2026-09-15]].

## Q2 — Does `Confirmed` prove bank credit, and how does a returned scheduled payout recover?

No. The receiving bank can still return a payout after `Confirmed`, which only says funds left Adyen (raw lines 32–45). A failed payout has a new `pspReference`; for a returned scheduled payout, payout state is automatically disabled, and the guide calls for updating holder bank details and then re-enabling payout state with separate update calls (raw lines 58–64). The MarketPay accounting report can link returned and original payouts (raw line 64). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] → [[raw/adyen/docs/classic-platforms/payouts/payout-notifications/2026-09-15]].
