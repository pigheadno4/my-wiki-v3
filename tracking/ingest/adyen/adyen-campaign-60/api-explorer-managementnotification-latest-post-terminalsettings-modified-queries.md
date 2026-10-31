# Fixed queries — api-explorer-managementnotification-latest-post-terminalsettings-modified

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-managementnotification-latest-post-terminalsettings-modified.md` — https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalSettings.modified
Pinned evidence: `raw/adyen/api-explorer/ManagementNotification/latest/post/terminalSettings.modified/2026-09-15.md`, SHA-256 `d6ac1d824861fdeebe78ee6eb4a7f1991e28607dcd537bffb129f61f63c0608c`.

## Q1

The captured `ManagementNotification/latest` `POST terminalSettings.modified` page describes an incoming notification that a terminal-settings update request was completed; the `POST` heading is webhook delivery, not the update operation (raw lines 5–7). The `latest` label supplies no numbered version. The table requires `createdAt`, `data`, `data.updateSource`, `data.user`, `environment`, and `type`; it marks company, merchant, store, and terminal IDs optional (raw lines 11–23). `updateSource` distinguishes Customer Area from Management API, while `user` can be Adyen or an API credential username; `environment` is test or live (raw lines 20–23). There is no request example or changed-settings object in this page.

## Q2

The page describes completion of the settings-update request but gives no evidence that the changed settings were applied on a physical terminal or that the terminal can process payments (raw lines 5–7, 11–23). The response section labels `200` Success and says the request succeeded; the optional `notificationResponse` row directs any `2xx` to accept the webhook, separating receiver acknowledgement from settings state (raw lines 25–33). The page gives no response-body value requirement, delivery/order/retry/deduplication/signature rule, deprecation statement, or terminal-readiness guarantee. Consult the canonical source route and raw locators for this bounded contract.
