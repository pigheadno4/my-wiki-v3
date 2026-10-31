# Fixed-query audit: api-explorer-notificationconfiguration-latest-post-testnotificationconfiguration

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-testnotificationconfiguration.md` — https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration
Pinned evidence: `raw/adyen/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration/2026-09-15.md` (SHA-256 `5f79ce0e6c27bf317ddf9af3a1be2dbdb8c000f750fd107ae788b91f441e0b46`).

## Q1

For `NotificationConfiguration/latest/post/testNotificationConfiguration`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** This Notification API v6 TEST endpoint probes an existing notification subscription configuration: it generates a test notification for each selected event type and sends it to the subscription's configured URL (raw lines 5–10). The request requires integer `notificationId`, the subscription configuration ID; optional `eventTypes` narrows the test, while omission tests all configured event types (lines 14–18). The event-type list is at line 17; the example tests `ACCOUNT_HOLDER_VERIFICATION` for ID 25032 (lines 20–30). 401 and 403 describe authentication and permissions failures (lines 70–84). Retrieve `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-testnotificationconfiguration.md` at https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 means the test API request succeeded; its response requires `notificationId` and optionally reports error/OK messages, event types, exchange messages, validation errors, request reference and result code (raw lines 31–54). The captured **200 example** has `errorMessages` saying the server did not respond with HTTP 2XX and an `okMessages` entry `ResponseCode: 404` (lines 121–152). So a 200 alone cannot prove recipient acknowledgment or a successful webhook delivery. Errors 400, 401, 403, 422, 500 are listed (lines 57–119). This TEST endpoint and example do not establish live subscription activation, actual business-event delivery, retry/lifecycle behavior, verification approval, or a financial outcome. The only server shown is Notification v6 TEST (lines 9–10), captured 2026-09-15 (line 2). Retrieve `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-testnotificationconfiguration.md` at https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration.
