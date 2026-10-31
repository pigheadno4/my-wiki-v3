---
title: "Adyen Balance Platform webhook: card order created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created/2026-09-15.md"
tags: [adyen, issuing, balance-platform, webhooks, card-orders]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.cardorder.created` event. It indicates successful creation of a card order after a physical card payment instrument is created; it is not a merchant request to create that instrument or order. The `latest` route label does not identify a numbered webhook version. See [[adyen-issuing]], [[adyen-webhooks]], and [[adyen]].

## Key takeaways

- The body requires `data`, `environment` (`test` or `live`), and `type`. The queued-event `timestamp` is optional. All listed `data` fields are marked optional: balance platform, card and PIN delivery objects, card-order item ID, event trigger date, resource ID, related payment-instrument ID, and shipping method.
- The event's successful *order creation* does not mean successful card production or delivery. The two test examples have `type: balancePlatform.cardorder.created` with card and PIN statuses of `processing` and `rejected`, respectively; the rejected example includes `Unknown value in the image field`. The table lists card-delivery status values `created`, `rejected`, `processing`, `produced`, `shipped`, `delivered`, `notApplicable`, and `unknown`.
- The raw table describes `data.card` as card delivery status, yet labels the nested `data.card.status` and `data.card.trackingNumber` as PIN delivery fields, duplicating the separate `data.pin` descriptions. Treat those labels as a documentation inconsistency; do not map card status to PIN delivery by inference.
- The optional `notificationResponse` response field accompanies a statement that any HTTP `2xx` accepts the webhook. Neither an example nor an acknowledgment proves physical delivery, card activation, payment authorization, or any financial outcome. This page does not specify event ordering, retry, deduplication, or signature rules.

## Detail locators

- Trigger and physical-card condition: pinned raw lines 5–7.
- Required envelope, optional IDs and delivery fields, and duplicated status descriptions: pinned raw lines 11–31.
- Processing and rejected test examples: pinned raw lines 33–73.
- Acknowledgment response: pinned raw lines 74–82.

## Related

- [[adyen-issuing]] — card program and payment-instrument context.
- [[adyen-webhooks]] — webhook processing context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments]] — separate physical-card payment-instrument creation reference.
- [[source-adyen-api-explorer-balanceplatform-latest-get-cardorders]] — separate card-order read reference.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created/2026-09-15|Card order created webhook reference, captured 2026-09-15]]
