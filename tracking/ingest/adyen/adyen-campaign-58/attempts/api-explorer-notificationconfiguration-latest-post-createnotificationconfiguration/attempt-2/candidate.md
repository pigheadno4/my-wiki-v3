---
title: "Adyen NotificationConfiguration API v6 POST /createNotificationConfiguration"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/createNotificationConfiguration"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/createNotificationConfiguration/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, webhooks, api-reference]
---

## Overview

This captured Classic NotificationConfiguration API `POST /createNotificationConfiguration` reference creates a subscription for platform event notifications sent to configured URL endpoint(s). Subscriptions are **per event type**, not per account holder: a marketplace's notifications of a subscribed type go to the configured endpoint(s). The listed server is `https://cal-test.adyen.com/cal/services/Notification/v6`. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request requires `configurationDetails`. Inside it, `active`, `apiVersion`, `description`, `eventConfigs`, `hmacSignatureKey`, `notificationId`, `notifyURL`, `notifyUsername`, `notifyPassword` and `sslProtocol` are table-optional. Each supplied `eventConfigs` entry requires `eventType` and `includeMode`; `INCLUDE` sends the specified type and `EXCLUDE` sends all except excluded types. The page states no default for omitted `active`, `apiVersion`, `eventConfigs`, URL, credentials or SSL protocol. See raw lines 14–29.
- `apiVersion` is the subscribed notification version; the page advises matching the API version your integration processes. `sslProtocol` permits `TLSv12` or `TLSv13`. `notifyURL` is the delivery URL; `notifyUsername` and `notifyPassword` are credentials for access to it. The sample credentials and URL are examples, not values to reuse or evidence of a reachable endpoint. See raw lines 19, 26–29 and 31–51.
- Optional `hmacSignatureKey` is described here as a **32-byte, 64-hex-character** secret. If supplied, notifications include `HmacSignature` and `Protocol` headers; if omitted, those headers are not supplied. The separate [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] uses conflicting “32bit” wording while showing a 64-hex-character example; retain this page's explicit byte/character statement and flag the source discrepancy. The reference does not itself prove receiver-side signature validation. See raw line 24.
- `notificationId` is Adyen-generated on create and is required when updating an existing configuration. The 200 example shows an ID and an active event subscription, but its values are illustrative. The response table requires `configurationDetails` and marks its nested fields, `invalidFields`, `pspReference` and `resultCode` optional. This create response does not establish actual delivery, acknowledgment, retry behavior or successful webhook validation. See raw lines 25, 52–81 and 148–170.
- Errors listed are 400, 401, 403, 422 and 500; 401 means authentication required and 403 insufficient permissions. The companion [[source-adyen-docs-classic-platforms-configure-notifications]] covers receiver acknowledgment/retry and has conflicting older sample API-version/protocol values; those samples do not redefine this endpoint table. See raw lines 84–146 and the companion source.

## Detail locators

- Subscription scope and TEST v6 server: raw lines 5–10.
- Request schema, event modes, endpoint credentials, HMAC and SSL: raw lines 14–29.
- Illustrative create request: raw lines 31–51.
- 200 schema, error classes and illustrative 200 response: raw lines 52–170.

## Related

- [[adyen-classic-platforms]] — Classic platform and notification context.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — separate subscription setup, acknowledgment, retry and test guide.
- [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] — separate receiver-side HMAC verification and key-rotation guide, with key-size wording discrepancy.
- [[adyen-platforms]] — separate newer platform webhook model.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/createNotificationConfiguration/2026-09-15|POST /createNotificationConfiguration, captured 2026-09-15]]
