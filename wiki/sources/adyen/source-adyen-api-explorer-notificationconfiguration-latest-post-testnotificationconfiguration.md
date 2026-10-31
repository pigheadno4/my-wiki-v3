---
title: "Adyen Notification API v6: POST /testNotificationConfiguration"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, webhooks, testing]
---

## Overview

This captured Notification API page describes `POST /testNotificationConfiguration`, which tests an **existing notification subscription configuration**. For each specified event type it generates a test notification and sends it to that subscription's configured URL. The listed server is Notification v6 TEST, `https://cal-test.adyen.com/cal/services/Notification/v6`. The request requires the integer `notificationId` of the subscription configuration. Optional `eventTypes` narrows the test; omitting it tests all event types configured for that subscription.

## Key takeaways

- The request and 200-response tables list permitted Classic notification event types, including account-holder verification, payout, transfer and store-status events. The basic request example selects `ACCOUNT_HOLDER_VERIFICATION` with `notificationId` 25032. The ID identifies a **subscription configuration**, not a notification delivery or an account holder.
- A 200 says the API request succeeded. Its response has a required `notificationId` and optional `errorMessages`, tested `eventTypes`, `exchangeMessages`, `invalidFields`, `okMessages`, request `pspReference`, and `resultCode`. Inspect these diagnostics for delivery outcome: the captured **200 example** contains “The server did not respond with HTTP 2XX” and `ResponseCode: 404`. Thus HTTP 200 on the test API is not proof that the endpoint acknowledged the test notification.
- The page lists 400, 401 (authentication required), 403 (insufficient permissions), 422, and 500 responses. A TEST configuration probe and its generated messages do not prove production subscription activation, real-event webhook delivery, downstream processing, or a payment/payout result. The captured page does not specify retry timing or persistent delivery state.

## Detail locators

- Test purpose, v6 TEST server, request selectors, permitted event types, and example: pinned raw lines 5–30.
- 200 response diagnostic schema and required configuration ID: pinned raw lines 31–54.
- Error response descriptions and fields: pinned raw lines 57–119.
- 200 example showing a non-2XX test-recipient response and HTTP 404: pinned raw lines 121–152.

## Related

- [[adyen-classic-platforms]] — Classic notification and account-holder context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration/2026-09-15|Notification API v6 POST /testNotificationConfiguration capture (2026-09-15)]]
