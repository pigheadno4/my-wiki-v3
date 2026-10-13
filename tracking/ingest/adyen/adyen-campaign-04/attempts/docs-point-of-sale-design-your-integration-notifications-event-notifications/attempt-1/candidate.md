---
title: "Adyen POS event notifications"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/notifications/event-notifications"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/notifications/event-notifications/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, event-notifications, asynchronous-responses]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, explains how a merchant POS app receives **terminal-generated `EventNotification`** messages about terminal state and availability. It belongs to [[adyen-terminal-api]]. The same configured event endpoint also receives asynchronous Terminal API `SaleToPOIResponse` messages when the integration uses the asynchronous cloud endpoint. A terminal state event is distinct from a payment response, a transaction-progress `DisplayRequest`, and a platform-generated payment webhook; the event alone is not proof of payment outcome.

## Key takeaways

- The merchant configures a JSON-capable HTTP callback endpoint under Terminal API **Event URLs** in Customer Area, or `nexo.eventUrls` through Management API `/terminalSettings`. Customer Area distinguishes public from local URLs and offers optional basic authentication and message encryption. The Management API route requires the **Management API—Terminal Advanced settings read and write** role and uses `eventPublicUrls` or `eventLocalUrls` at company, merchant, store, or terminal level. Inspect higher-level inheritance before removing a setting.
- The snapshot specifies test receiver ports 80/8080/8888 for HTTP or 443/8443/8843 for HTTPS with TLSv1.2; live uses HTTPS ports 443/8443/8843 with TLSv1.2. The receiver must accept JSON. These documented ports and setup choices are snapshot evidence, not proof that a particular account or endpoint is configured.
- Store the notification, return a successful HTTP status (202 is an example), **then** apply business logic. Adyen says acknowledgement prevents repeated sends and warns that business-logic failure before acknowledgement can block later important notifications. Do not treat receipt or acknowledgement as payment success.
- `EventToNotify` identifies terminal events such as shutdown, maintenance, network connection/disconnection, out-of-order state, `Reject`, `SaleWakeUp`, and `UseAnotherCardForPreauth`; the page's table gives their meanings. Its examples wrap `EventNotification` in `SaleToPOIRequest` with a `MessageHeader` containing `MessageClass: Event`, `MessageCategory: Event`, `MessageType: Notification`, terminal `POIID`, and `DeviceID`.
- For **asynchronous cloud communications**, event notifications must be set up: Adyen sends the Terminal API request's `SaleToPOIResponse` to this endpoint. The guide says that response is the same as for local or synchronous cloud communication; the payment-response example has `MessageCategory: Payment`, `MessageClass: Service`, and `MessageType: Response`. It must be interpreted as a payment response, not as an `EventToNotify` terminal-state event.

## Detail locators

- Purpose and asynchronous-cloud requirement: raw lines 15-23.
- Customer Area endpoint, environment ports, URL/public-local/auth/encryption configuration: raw `## Set up event notifications in the Customer Area`, lines 25-56.
- Management API role, setting scope, inheritance, `nexo.eventUrls` local/public arrays, and illustrative request/response: raw `## Set up event notifications using API calls`, lines 58-220. The opening sentence of this section calls them “display notifications,” but the section's role, `eventUrls` fields and following examples address event URLs.
- Persist → acknowledge → business logic and retry-avoidance warning: raw `## Accept event notifications`, lines 223-232.
- Event table and JSON examples including `Reject`, `SaleWakeUp` and `UseAnotherCardForPreauth`: raw `## Event notification types`, lines 234-249, and `## Event notification examples`, lines 251-502.
- Asynchronous `SaleToPOIResponse` endpoint delivery and payment response example: raw `## Asynchronous Terminal API responses`, lines 504-578.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-terminal-api]]
- Transaction progress: [[source-adyen-docs-point-of-sale-design-your-integration-notifications-display-notifications]]
- Platform-generated webhooks: `## Next steps` in the raw links to the separate standard-notifications guide; this source does not establish its payload or delivery rules.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/event-notifications/2026-09-15|Adyen POS event notifications]] — full captured event and asynchronous-response guide
