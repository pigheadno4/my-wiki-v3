# Fixed retrieval audit — api-explorer-notificationconfiguration-latest-post-deletenotificationconfigurations

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-notificationconfiguration-latest-post-deletenotificationconfigurations.md` — https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations
Pinned raw: `raw/adyen/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations/2026-09-15.md`

## Q1

**Prompt:** For `NotificationConfiguration/latest/post/deleteNotificationConfigurations`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It deletes existing Classic notification subscription configurations, selected by required `notificationIds` array of integers. The example supplies one ID; the page does not define empty-array or duplicate behavior. Once a selected subscription is deleted, no further event notifications are sent to the URL **defined in that subscription**; it does not state that every subscription sharing a URL is deleted. The listed server is test Notification API v6. A 403 means insufficient permissions, but no specific credential role is named. See canonical source Overview and Key takeaways; raw lines 5–28 and 74–84.

## Q2

**Prompt:** What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** The only listed success response is 200, with optional `invalidFields`, `pspReference`, and `resultCode`; its example gives just a request reference. The page does not show a per-ID deletion outcome or delivery cutoff timestamp, so that reference alone does not prove deletion or stopped delivery. Errors listed are 400, 401, 403, 422 and 500, with optional body fields. The snapshot lists test Notification API `/v6`; `latest` is in the documentation URL, with no live delivery evidence. This subscription operation says nothing about payment or payout results, and should not be treated as a newer webhook-management contract. See canonical source Key takeaways and Detail locators; raw lines 7–10, 29–45, 48–121.
