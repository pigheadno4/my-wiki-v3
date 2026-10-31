# Fixed queries — Notification Configuration API POST /getNotificationConfiguration

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-getnotificationconfiguration.md` — https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration

## Q1

For `NotificationConfiguration/latest/post/getNotificationConfiguration`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: The TEST Notification v6 endpoint retrieves one notification-subscription configuration by required integer `notificationId`. The 200 `configurationDetails` object contains optional activation, subscribed `apiVersion`, event include/exclude, HMAC key, notify URL/username/password and SSL protocol settings. Event-config items require event type and include mode if present. The page lists 401/403 but no named role. The API schema specifies a 32-byte HMAC key (64 hex characters); the separate Classic signing guide says “32bit hexadecimal” despite 64-character examples, so its wording is not a compatible key-length rule. [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] Credentials in this response describe endpoint access; they do not establish a successful webhook authentication. See full canonical source stem and URL above; pinned raw `raw/adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration/2026-09-15.md` lines 5–56, 72–95.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: HTTP 200 says the lookup request succeeded and requires `configurationDetails`; it is not a delivery event. The request example ID is 21259, but the response example's ID is 50054, so the sample cannot establish identity echo. `active: true`, included events, a URL and HMAC settings do not prove delivery, endpoint reachability, successful authentication, or signature verification. Errors are 400, 401, 403, 422 and 500. The captured server is TEST Notification v6, while example `apiVersion: 5` denotes a subscribed notification version; no current live status is shown. See full canonical source stem and URL above; pinned raw lines 9–56, 59–146.
