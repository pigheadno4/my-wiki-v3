---
title: "Adyen ManagementNotification: terminalAssignment.completed"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalAssignment.completed"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/terminalAssignment.completed/2026-09-15.md"
tags: [adyen, management-notification, terminal-management, terminal-assignment]
---

## Overview

This captured Adyen API Explorer `ManagementNotification/latest` POST reference describes an incoming `terminalAssignment.completed` event: a terminal reassignment request was completed. It is a terminal-management notification, separate from Standard payment webhooks and from the merchant's Management API reassignment request. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The request body requires `assignedToAccount`, `eventDate`, `pspReference`, and `uniqueTerminalId`. `assignedToAccount` identifies the merchant or company account receiving the assignment; `uniqueTerminalId` identifies the terminal; `pspReference` identifies the request from which the notification originates. `eventDate` records when the event was completed.
- `assignedToStore` (store reference/code) and `assignedToStoreId` (unique store ID) are optional. Their absence in the schema does not mean the terminal is assigned to a specific store. The event reports reassignment completion, not physical boarding, configuration application, readiness for payments, or a payment outcome.
- The `200 Success` response section says the request succeeded and lists optional `notificationResponse`; it directs the receiver to respond with any `2xx` HTTP status to accept the webhook. Receiver acceptance is distinct from the terminal reassignment described by the incoming event. The reference gives no delivery, order, retry, deduplication, or signature-verification rule.

## Detail locators

- Raw lines 5–7: event identity and completed reassignment purpose.
- Raw lines 11–19: request-body requiredness and account, store, event-time, originating-request, and terminal identifiers.
- Raw lines 21–29: `200 Success`, optional response-body field, and `2xx` receiver acceptance.

## Related

- [[adyen-terminal-management]] — assignment and boarding boundaries.
- [[adyen-webhooks]] — Adyen webhook-family distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/terminalAssignment.completed/2026-09-15|Captured terminalAssignment.completed notification reference]]
