---
title: "Adyen Balance Platform API v2: Get card order items"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/cardorders/(id)/items"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/cardorders/(id)/items/2026-11-03.md"
tags: [adyen, issuing, balance-platform, card-orders, api]
---

## Overview

Captured Balance Platform API v2 TEST reference for `GET /cardorders/{id}/items`. It reads the item list for one card order identified by the required path `id`; it does not place an order or create a card. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- Optional query `limit` is the number of items per page (default 10); optional `offset` starts the returned item list at a position (default 0). No maximum or explicit ordering is stated. The offset description also calls 0 the value that returns all elements, which should not override the separately documented default limit of 10.
- A 200 response requires `data` (array of card order items), `hasNext`, and `hasPrevious`. Item fields are optional and include balance-platform, card-order-item, resource and payment-instrument IDs; creation date; card and PIN delivery objects; and shipping method. The card/PIN objects can include status, tracking number and error message. The `card` parent is described as card-delivery status with listed values `created`, `rejected`, `processing`, `produced`, `shipped`, `delivered`, `notApplicable`, `unknown`, but its nested `status` and `trackingNumber` descriptions say PIN delivery. Treat this label mismatch as unresolved rather than reassigning their meaning.
- A successful GET reports the returned snapshot and pagination flags, not subsequent production, shipping, receipt, card activation, transaction authorization, capture or settlement. The example's `shipped` card and `produced` PIN values are illustrative, not a guarantee for another order.
- The reference lists 401 authentication required, 403 insufficient permission, 422 validation error and 500 server error. Its generic 422 and 500 examples concern payment-instrument changes/creation and cannot establish card-order-item-specific failure rules. It states no named role, idempotency key, live host, eligibility rule, propagation timing or asynchronous approval semantics for this GET.

## Detail locators

- Test server, required path ID and optional pagination defaults: pinned raw, `## Servers` and `## Parameters`, lines 9–24.
- 200 fields, delivery labels, statuses and page indicators: `## Responses` → `### 200 Success`, lines 28–50.
- Authentication, permission, validation and server-error schemas: `## Responses`, lines 53–130.
- Illustrative success and generic error payloads: `## Response examples`, lines 132–209.

## Related

- [[adyen-issuing]] — card-program context.
- [[adyen-platforms]] — balance-platform context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-cardorders]] — list of card orders, separate from this order's items.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/cardorders/(id)/items/2026-11-03|Captured GET /cardorders/{id}/items API Explorer reference (2026-11-03)]]