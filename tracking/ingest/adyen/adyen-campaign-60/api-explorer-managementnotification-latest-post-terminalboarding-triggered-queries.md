# C60 terminalBoarding.triggered fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-managementnotification-latest-post-terminalboarding-triggered.md` — https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered. Pinned raw: `raw/adyen/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered/2026-09-15.md`.

## Q1

This ManagementNotification incoming POST reference names `terminalBoarding.triggered` as a terminal-boarding result and says boarding of a payment terminal succeeded (raw lines 5–7). The request body requires `createdAt`, `data`, `environment` and `type`; `data.companyId` and `data.uniqueTerminalId` are required, while `data.merchantId` and `data.storeId` are optional (lines 11–21). `createdAt` is when the webhook was created, and `environment` is `test` or `live` (lines 14, 20). The page has no request example and does not supply a literal `type` value, payment reference, amount or currency. The identifier in this event is `uniqueTerminalId` (line 19), rather than a payment `pspReference`.

## Q2

The event description establishes successful terminal boarding for the terminal described by the event (raw lines 5–7). The response shows `200 Success` and lists optional `notificationResponse`; any `2xx` HTTP status accepts the webhook (lines 23–31). Receiver acceptance is distinct from the boarding event and does not prove configuration, payment-method availability or payment readiness. This reference states no delivery, ordering, retry, deduplication, signature or later-state guarantee. Its `latest` path is a snapshot label; the related overview names the family Management Webhooks v3.
