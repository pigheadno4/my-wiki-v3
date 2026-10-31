---
title: "Adyen Notification API v6: List subscription configurations"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/getNotificationConfigurationList"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfigurationList/2026-09-15.md"
tags: [adyen, classic-platforms, notification-api, subscriptions, configuration]
---

## Overview

This 2026-09-15 API Explorer snapshot documents POST `/getNotificationConfigurationList` on the displayed Notification v6 test server. It returns details of notification subscription configurations in the platform of the executing user. This is a configuration lookup, not a notification-delivery log. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request example is an empty JSON object; the captured page has no request-parameter table or pagination parameters (raw lines 5–17). Its stated scope is all notification subscriptions in the executing user's platform, not a single account holder or merchant account.
- The optional `configurations` array can describe active state, subscribed API version, event type/include mode, notification ID, endpoint URL, SSL protocol, and optional notification credentials/HMAC key. Inside an `eventConfigs` item, `eventType` and `includeMode` are marked required; the parent array and configuration fields are optional (raw lines 23–47). The raw table gives the event-type enumeration and `INCLUDE`/`EXCLUDE` meanings; a listed configuration does not prove an event was delivered or acknowledged.
- The schema says omitted `hmacSignatureKey` precludes `HmacSignature` and `Protocol` headers in notifications. This is a configuration-field description, not evidence of a delivered or verified webhook (raw line 33).
- HTTP 200 describes a succeeded request. The example has two active entries and a request `pspReference`; it is illustrative, not a current inventory. Errors listed are 400, 401, 403, 422 and 500, with no named permission role (raw lines 20–21, 50–151).

## Detail locators

- Operation purpose, test server and empty-object request example: raw lines 5–17.
- Optional response schema, event enum/include semantics, credential/HMAC fields, notification ID and endpoint fields: raw lines 18–47. Full two-entry example: raw lines 114–151.
- Error categories and body schema: raw lines 50–112.

## Related

- [[adyen-classic-platforms]] — Classic notification context and reciprocal route.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — separate subscription setup, acknowledgement and retry guide.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfigurationList/2026-09-15|Notification API Explorer configuration list, captured 2026-09-15]]
