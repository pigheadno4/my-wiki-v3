---
title: "Adyen Notification API v6: POST /deleteNotificationConfigurations"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations/2026-09-15.md"
tags: [adyen, classic-platforms, notification-api, subscriptions, deletion]
---

## Overview

This 2026-09-15-captured Classic Notification API reference documents `POST /deleteNotificationConfigurations`, which deletes existing **notification subscription configurations**. The page says that after a subscription is deleted, no further event notifications are sent to the URL defined in that subscription. That statement concerns the deleted subscription, not every subscription that might use the same URL. The listed server is **test** `https://cal-test.adyen.com/cal/services/Notification/v6`, despite `latest` in the documentation route. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request-body table marks `notificationIds` as a required array of integers: IDs of the subscription configurations to delete. Its example contains one ID. The page gives no empty-array, duplicate-ID, partial-success, or idempotency rule (raw lines 12–28).
- The only success status listed is 200, described as request succeeded. Its body schema lists optional `invalidFields`, `pspReference` and `resultCode`; the example returns only a `pspReference`. The page does not provide a per-ID deletion result or propagation timing. The stated cessation of notifications is conditioned on the subscription being deleted; a request reference alone is not evidence that any particular configuration was removed or delivery stopped (raw lines 29–45, 112–121).
- Listed errors are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 request validation and 500 server processing. No specific credential role is named, and error body fields are optional in the tables (raw lines 48–110).

## Detail locators

- Deletion purpose, delivery effect and test v6 server: raw lines 5–10. Required ID array and example: lines 12–28. Success description/schema: lines 29–45; example: lines 112–121. Error descriptions/schemas: lines 48–110.

## Related

- [[source-adyen-docs-classic-platforms-configure-notifications]] — Classic subscription configuration, notification delivery and asynchronous operation-outcome context.
- [[adyen-classic-platforms]] — Classic Platforms scope, separate from newer balance-platform webhooks.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations/2026-09-15|Notification configuration deletion reference, captured 2026-09-15]]
