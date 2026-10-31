---
title: "Adyen transaction created webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transaction-webhooks/latest/post/balancePlatform.transaction.created"
raw_files:
  - "adyen/api-explorer/transaction-webhooks/latest/post/balancePlatform.transaction.created/2026-09-15.md"
tags: [adyen, transaction-webhooks, balance-accounts, transfers]
---

## Overview

This 2026-09-15-captured API Explorer `latest` POST reference describes Adyen's incoming `balancePlatform.transaction.created` webhook with transaction information after a transfer is booked in a balance account. It records a balance-account transaction and is distinct from a Transfer webhook's transfer-state update; booking is not proof of beneficiary-bank receipt. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The body requires `data` and `environment`, while top-level `type` and `timestamp` are marked optional in this table despite examples containing both. Within `data`, required fields include `accountHolder`, `amount` (currency and minor-unit value), `balanceAccount`, `balancePlatform`, `bookingDate`, transaction `id`, `status`, and `valueDate`. Nested holder and account IDs are individually marked optional. See raw lines 11–45.
- `data.id` is the transaction identifier. Optional `data.transfer` can carry a distinct transfer `id`; within that optional object, `reference` is marked required and is the request reference or an Adyen-generated one. `bookingDate` is the account booking date and `valueDate` is when the amount becomes available in that balance account. See raw lines 27–42.
- The status enum lists `pending` and `booked`, while the introduction says Adyen sends this event after booking. Keep that documentation tension visible; do not infer a universal status transition from this page. The examples show booked EUR -10000 outgoing bank and business-account entries, and a +10000 internal incoming entry, all in `test`. The internal incoming example's balance-account description still says "from where the amount is debited"; the positive amount and heading should not be silently rewritten into a debit claim. See raw lines 7, 37, 47–170.
- An HTTP 2xx accepts the webhook; `notificationResponse` is optional. The reference gives no delivery, ordering, retry/deduplication, signature or external-bank finality guarantee. See raw lines 171–179.

## Detail locators

- Envelope and transaction schema: raw lines 9–45.
- Outgoing payout, internal incoming and outgoing business-account examples: raw lines 47–170.
- Acknowledgment response: raw lines 171–179.

## Related

- [[adyen-webhooks]]
- [[adyen-platforms]]
- [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/api-explorer/transaction-webhooks/latest/post/balancePlatform.transaction.created/2026-09-15|Transaction created webhook reference, captured 2026-09-15]]
