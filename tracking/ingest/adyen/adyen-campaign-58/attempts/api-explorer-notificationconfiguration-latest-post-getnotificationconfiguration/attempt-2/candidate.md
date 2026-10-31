---
title: "Adyen Notification Configuration API: POST /getNotificationConfiguration"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration/2026-09-15.md"
tags: [adyen, classic-platforms, notification-configuration, webhooks]
---

## Overview

This 2026-09-15 API Explorer capture documents `POST /getNotificationConfiguration` on the listed TEST Notification v6 server. It retrieves the configuration of a notification subscription by its required integer `notificationId`; it is a configuration lookup, not a webhook delivery record. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The 200 schema requires `configurationDetails`, with optional `active`, `apiVersion`, description, `eventConfigs`, HMAC key, notification ID, notify URL/username/password and SSL protocol fields inside it. `eventConfigs`, when present, has required event type and include mode within each item. `INCLUDE` selects that event; `EXCLUDE` selects all except excluded event types. `apiVersion` is the subscribed notification version, distinct from the listed v6 server version.
- The schema describes optional `hmacSignatureKey` as a 32-byte hex-encoded key (64 hexadecimal characters) for `HmacSignature` and `Protocol` headers; omitting it precludes those headers. The separate Classic signing guide calls the key “32bit hexadecimal” (its raw line 29), while its own examples contain 64 hex characters (raw lines 54 and 115). That wording conflicts with the API schema's byte count; do not treat “32bit” as a compatible length rule. [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] Optional `notifyUsername`/`notifyPassword` are endpoint-access credentials, and `sslProtocol` permits `TLSv12` or `TLSv13`. These settings describe a subscription; their appearance does not prove a webhook was delivered, reached the URL, authenticated successfully, or passed signature verification.
- The request example uses `notificationId: 21259`, while the 200 response example shows `configurationDetails.notificationId: 50054`. This mismatch prevents using the sample as proof that a response echoes the queried ID. The response example's `active: true`, `apiVersion: 5`, included event and URL are illustrative, not live runtime evidence.
- Errors listed are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. The page does not name a required role, describe a delivery attempt, or establish current production availability.

## Detail locators

- Operation, TEST v6 server, required ID and request example: raw lines 5–26.
- 200 configuration schema, event modes, credential/HMAC/SSL options: raw lines 27–56.
- Error response classes and schemas: raw lines 59–121.
- Illustrative 200 response and ID mismatch: raw lines 123–146.

## Related

- [[adyen-classic-platforms]] — Classic notification configuration and outcome sources.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration/2026-09-15|Notification Configuration API Explorer lookup capture]]
