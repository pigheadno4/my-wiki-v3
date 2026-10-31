# Fixed query answers — api-explorer-balance-webhooks-latest-post-balanceplatform-balanceaccount-balance-updated

Canonical route: [[source-adyen-api-explorer-balance-webhooks-latest-post-balanceplatform-balanceaccount-balance-updated]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated). Pinned raw: `raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated/2026-09-15.md`.

## Q1

The captured incoming `balancePlatform.balanceAccount.balance.updated` reference says Adyen sends the event when a specified balance type reaches or falls below a configured threshold (raw lines 5–7, 50–52). Top-level `data`, `environment`, and `type` are required. Within `data`, the balance-account ID, `balances` object, three-character ISO `currency`, and balance-webhook `settingIds` are required; `balancePlatform` and `creationDate` are optional (raw lines 14–27). The `balances` object's four listed integer fields are individually optional: available for use, `balance` as already-settled transaction sum, `pending` as future-settled transaction sum, and `reserved` as currently held in reserve (raw lines 17–21). The example shows two setting IDs and USD values, but no threshold or identified crossed balance type (raw lines 29–53).

## Q2

This is a configured balance-threshold alert with reported balance values; it does not identify a transfer or booked transaction, establish payout or bank receipt, or give a formula equating available, `balance`, pending and reserved (raw lines 7, 17–24, 33–52). The source distinguishes optional event-trigger `creationDate` from optional queued `timestamp`; the example omits `timestamp` (raw lines 22, 26, 33–53). The receiver accepts the webhook with any `2xx`, which is acknowledgement rather than a financial outcome (raw lines 54–73). This reference does not define delivery order, retry/deduplication, signatures, failure/reversal, or a numbered/current version beyond the captured `latest` route (raw lines 1–7, 9–73).
