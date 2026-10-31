# Fixed retrieval audit: api-explorer-notificationconfiguration-latest-post-updatenotificationconfiguration

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-updatenotificationconfiguration.md` — https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration

## Q1

For `NotificationConfiguration/latest/post/updateNotificationConfiguration`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** Classic Notification API v6 test-host `POST /updateNotificationConfiguration` updates an existing subscription, with required `configurationDetails` and a `notificationId` whose row says No but description says required on update (raw lines 5–17, 25, 31–56). When updating event types, all desired types must be provided or prior event configuration is overwritten (line 7). Optional `eventConfigs` entries require nested `eventType` and `includeMode` and define INCLUDE versus EXCLUDE (lines 21–23). Other optional fields set active status, notification API version, endpoint URL/basic credentials, `TLSv12`/`TLSv13`, and a 32-byte hex-encoded HMAC key; omission of that key precludes the named HMAC/protocol headers (lines 18–29). Authentication and permissions appear through 401/403 errors, without specific role labels (lines 102–116). Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-updatenotificationconfiguration.md`; URL: https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** HTTP 200 returns required `configurationDetails` with optional `invalidFields`, `pspReference` and `resultCode` (raw lines 57–86). The response example shows `active: false`; it does not show active delivery (lines 153–179). The page lists no 202, propagation delay, webhook-delivery confirmation, acknowledgment or retry proof. Errors 400, 401, 403, 422 and 500 are documented (lines 89–151). Event-list overwrite is explicit, but behavior for omitted **other** fields is not stated (lines 7, 17–29). The snapshot lists a v6 test server only (lines 1–10), with no current live configuration or payment outcome evidence. Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-updatenotificationconfiguration.md`; URL: https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration.
