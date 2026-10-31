---
title: "Adyen balance-platform mandate updated webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, business-accounts, direct-debit]
---

## Overview

Captured incoming `balancePlatform.mandate.updated` webhook reference. Adyen says it sends the event when a direct debit mandate is updated, and links the mandate term to its UK direct-debit guide. The `POST` heading describes a webhook sent to the receiver, not a merchant operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-business-accounts]].

## Key takeaways

- The request-body table requires top-level `data`, `environment` (`test` or `live`), and `type`; `timestamp` is optional. `data.mandate` and all its listed children are optional in this schema. The children identify a linked balance account and payment instrument, counterparty, mandate ID, creation/update times, status, and type. The listed mandate statuses are `pending`, `approved`, and `cancelled`; the listed mandate type is `bacs`. An update event alone does not identify which status applies when the optional status is absent.
- The response section says any `2xx` HTTP status accepts the webhook, with optional `notificationResponse` in the `200 Success` response-body table. Receiver acceptance and a mandate update are distinct from a direct-debit request, authorization, funds booking or bank receipt. This reference does not define the cause of an update or the effect of each status on a particular debit.
- The captured `latest` URL does not establish the currently served version; this endpoint page itself does not state one. It provides no delivery-order, retry, deduplication, authentication or signature rule.

## Detail locators

- Event identity and direct-debit-mandate trigger: pinned raw lines 5–7.
- `## Parameters` → `### Request body`: top-level requiredness, linked identities, optional mandate status/type and environment, lines 9–27.
- `## Responses` → `### 200 Success`: `2xx` acceptance and optional response field, lines 29–37.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated/2026-09-15|Captured mandate updated webhook reference (2026-09-15)]]
