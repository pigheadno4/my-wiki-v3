---
title: "Adyen Balance Platform webhook: recurring top-up created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, recurring-top-ups]
---

## Overview

Captured API Explorer `latest` POST reference for the incoming `balancePlatform.balanceAccount.recurringTopUp.created` webhook. Adyen says it sends the event when a recurring top-up configuration is successfully created for a balance account. This is a configuration event, not evidence that a top-up transfer was triggered or funds were credited. See [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- The request-body table marks `data`, `data.accountId`, `data.webhookTopUpConfiguration`, `environment`, and `type` required. Within the configuration it marks `counterparty`, `description`, `id`, `status`, `topUpAmount`, and `trigger` required. `data.id`, `data.balancePlatform`, `data.creationDate`, `timestamp`, `mandate`, and `referenceForBeneficiary` are optional in this table.
- `data.accountId` identifies the balance account; `data.webhookTopUpConfiguration.id` identifies the recurring top-up configuration. The separate optional `data.id` is described only as the resource ID.
- The configuration status values are `active` (enabled and funds are pulled in) and `inactive` (disabled and cannot be triggered). `topUpAmount` can be fixed or target; `trigger` can be a schedule or minimum-balance threshold. The example's EUR amounts, weekly schedule, threshold, transfer-instrument ID, and mandate are illustrative, not stated required subfields or evidence of a transfer.
- The table distinguishes optional event `creationDate` (when triggered) from optional `timestamp` (when queued). `environment` is `test` or `live`. The captured `latest` route does not itself establish a numbered API version or current availability.
- The response section says any HTTP `2xx` accepts the webhook. Its `200` example with `notificationResponse` `[accepted]` documents receiver acknowledgement, not configuration verification, top-up execution, booking, or external bank receipt.

## Detail locators

- Event purpose and type: raw lines 5–7 and 68–70.
- Required versus optional request-body fields, resource IDs, statuses, amount and trigger descriptions: raw lines 9–30.
- Illustrative request payload: raw lines 32–72.
- Receiver acknowledgement and response example: raw lines 73–92.

## Related

- [[adyen-platforms]]
- [[adyen-webhooks]]
- [[adyen-issuing]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created/2026-09-15|Captured recurring top-up created webhook reference]]
