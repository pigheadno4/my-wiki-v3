---
title: "Adyen Management Notification: terminalSettings.modified"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalSettings.modified"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/terminalSettings.modified/2026-09-15.md"
tags: [adyen, management, webhooks, terminals]
---

## Overview

Captured API Explorer `ManagementNotification/latest` `POST terminalSettings.modified` reference for an incoming notification that a request to update terminal settings was completed. The `POST` heading is webhook delivery, not a merchant settings-update endpoint. The page describes completion of the update request, but does not show the changed settings or establish when a physical terminal applies them. The `latest` label gives no numbered version. See [[adyen]], [[adyen-terminal-management]], and [[adyen-webhooks]].

## Key takeaways

- The request-body table marks `createdAt`, `data`, `data.updateSource`, `data.user`, `environment`, and `type` required. Company, merchant, store, and terminal identifiers within `data` are each optional; the page does not state which are present for a particular event. No request example is provided.
- `updateSource` identifies whether the settings were updated through Customer Area or the Management API. `user` identifies the updater and can be Adyen or the API credential username. `createdAt` is webhook-creation time, and `environment` is `test` or `live`. The table labels `type` as notification type; the heading identifies this event as `terminalSettings.modified`.
- The response section labels `200` Success and says the request succeeded. The optional `notificationResponse` field's description says any HTTP `2xx` accepts the webhook. Receiver acceptance is separate from the completed settings-update request and any later physical-terminal configuration state. This page gives no delivery, ordering, retry, deduplication, signature, changed-settings payload, or payment-readiness guarantee.

## Detail locators

- Event purpose and update-request completion: raw lines 5–7.
- Body requiredness, optional resource IDs, updater and environment: raw lines 11–23.
- Response and receiver acceptance: raw lines 25–33.

## Related

- [[adyen]]
- [[adyen-terminal-management]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/terminalSettings.modified/2026-09-15|Captured terminalSettings.modified Management notification]]
