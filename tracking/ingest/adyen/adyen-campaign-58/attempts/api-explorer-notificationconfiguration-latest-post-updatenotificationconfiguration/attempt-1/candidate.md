---
title: "Adyen Notification API v6: Update a subscription configuration"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, webhooks, configuration]
---

## Overview

This 2026-09-15-captured Classic Notification API v6 reference describes `POST /updateNotificationConfiguration` at the listed test server (`https://cal-test.adyen.com/cal/services/Notification/v6`). It updates an **existing notification subscription**, identified by Adyen-generated `notificationId` within required `configurationDetails`. It configures event selection and delivery settings; a successful configuration response is not proof that a notification was delivered or acknowledged. [[adyen-classic-platforms]] [[adyen]]

## Key takeaways

- The opening warning says that when changing event types, supply **all** desired event types or the previous event-type configuration is overwritten. `eventConfigs` is optional as a request property, but each supplied entry requires `eventType` and `includeMode`; `INCLUDE` selects the specified type, while `EXCLUDE` sends all types except excluded entries. This does not state that omission of other configuration fields clears them. See [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 5–23]].
- `configurationDetails` is required. `notificationId` is marked No in the table yet its description expressly says it is **required when updating an existing configuration**; the example supplies it. Optional `active` indicates subscription activation and `apiVersion` names the subscribed notification version, with guidance to match the API version used by the integration. See [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 17–25 and 31–56]].
- Optional `notifyURL`, `notifyUsername` and `notifyPassword` set the endpoint and access credentials; optional `sslProtocol` permits `TLSv12` or `TLSv13`. The optional `hmacSignatureKey` description requires a 32-byte hex-encoded value if supplied and says omission precludes `HmacSignature` and `Protocol` headers. This is the captured API Explorer field rule, not proof of current security configuration. See [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 24–29]].
- HTTP 200 is labeled succeeded and returns required `configurationDetails`, plus optional validation `invalidFields`, request-identifying `pspReference` and `resultCode`. The response example has `active: false` and `INCLUDE`/`EXCLUDE` entries; it is an illustration, not evidence of active delivery. The page lists no 202 response, propagation interval or delivery confirmation. See [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 57–86 and 153–179]].
- Errors list 400 unreadable request, 401 authentication, 403 insufficient permissions, 422 validation and 500 server failure. The page does not name a specific role or prove a live endpoint, successful webhook delivery, retry/acknowledgment behavior or a payment outcome. See [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 89–151]].

## Detail locators

- Overwrite warning, request field requiredness and event/endpoint/security options: [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 5–29]].
- Request example and 200 response schema: [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 31–86]].
- Error schemas and 200 example: [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|raw lines 89–179]].

## Related

- [[adyen-classic-platforms]] — Classic platform notification context.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — separate setup, delivery, retry and test guide with versioned examples.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15|Update notification configuration API reference (captured 2026-09-15)]]
