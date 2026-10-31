---
title: "Adyen Notification Configuration API v6 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/NotificationConfiguration/latest/overview"
raw_files:
  - "adyen/api-explorer/NotificationConfiguration/latest/overview/2026-09-15.md"
tags: [adyen, classic-platforms, notification-configuration, api-explorer]
---

## Overview

Captured API Explorer overview for the Classic Platforms Notification Configuration API v6. It catalogs endpoints to set up and test notification subscription configurations for platform events, including completed verification checks or payouts. The page directs new implementations to a separate newer integration guide. It describes configuration operations, not notification delivery or proof that a particular verification or payout completed. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The catalog lists six POST operations: create, delete, get, list, test and update notification configurations. These are subscription configuration actions; the overview does not specify each operation's request fields, response codes or delivery behavior. See raw lines 42–52.
- The captured TEST server is `https://cal-test.adyen.com/cal/services/Notification/v6`. API versions use a `vXX` endpoint suffix. This captured `latest` route displays v6; it does not establish a later/current version or live availability. See raw lines 31–40.
- Authentication uses an `X-API-Key` header with an API key supplied through an Adyen contact, or Basic authentication with username and password. Going live requires new web service user credentials for live endpoints. See raw lines 13–29.
- A configured or tested subscription is not evidence of a delivered notification, receipt/acknowledgment, approved verification, or completed payout. The overview gives examples of event purposes but no concrete delivery result. See raw lines 7–11 and 42–52.

## Detail locators

- Classic integration scope, event examples and documentation route: raw lines 5–11.
- Authentication and live credential boundary: raw lines 13–29.
- Versioning and TEST server: raw lines 31–40.
- Six endpoint catalog entries: raw lines 42–52.

## Related

- [[adyen-classic-platforms]] — Classic Platforms context and other captured notification guides.

## Raw Sources

- [[raw/adyen/api-explorer/NotificationConfiguration/latest/overview/2026-09-15|Notification Configuration API v6 overview captured 2026-09-15]]
