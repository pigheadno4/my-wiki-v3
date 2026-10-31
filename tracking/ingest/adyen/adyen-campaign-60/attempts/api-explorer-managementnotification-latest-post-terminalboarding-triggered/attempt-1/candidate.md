---
title: "Adyen Management terminalBoarding.triggered webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered/2026-09-15.md"
tags: [adyen, management-webhooks, terminal-management, boarding]
---

## Overview

This 2026-09-15 Management Webhooks v3 API Explorer POST reference describes the incoming `terminalBoarding.triggered` notification as a result of terminal boarding. Its text specifically says boarding of a payment terminal succeeded. The POST is an Adyen-to-merchant webhook, not an operation for the merchant to trigger boarding. See [[adyen]], [[adyen-webhooks]], and [[adyen-terminal-management]].

## Key takeaways

- The request body requires `createdAt` (webhook creation time), `data`, `environment` (`test` or `live`), and `type`. Within `data`, `companyId` and `uniqueTerminalId` are required; `merchantId` and `storeId` are optional. The page does not give an example or a literal `type` value.
- The event text establishes successful boarding for the identified terminal in the event's context. It does not itself establish current assignment, configuration, payment-method availability, or successful payment execution. `createdAt` is webhook creation time, not a stated boarding-completion timestamp.
- The response section shows `200 Success`, lists optional `notificationResponse`, and says any `2xx` HTTP status accepts the webhook. Receiver acceptance is separate from the terminal boarding event.

## Detail locators

- Pinned raw, lines 5–7: event title and successful-boarding statement.
- Pinned raw, lines 11–21: request body requiredness, IDs, time, environment and type.
- Pinned raw, lines 23–31: response and `2xx` acceptance.

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/terminalBoarding.triggered/2026-09-15|terminalBoarding.triggered API Explorer reference, captured 2026-09-15]]
