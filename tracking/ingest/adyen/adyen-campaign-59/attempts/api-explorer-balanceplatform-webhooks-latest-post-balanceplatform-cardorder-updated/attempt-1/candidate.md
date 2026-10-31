---
title: "Card order updated webhook | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.updated/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, issuing, card-orders]
---

## Overview

This captured Adyen Balance Platform webhook POST reference describes the incoming `balancePlatform.cardorder.updated` event sent when a card order status changes. It can report card or PIN delivery information for a card order item. The `latest` route does not resolve a numbered webhook API version in this capture. [[adyen]] [[adyen-issuing]] [[adyen-webhooks]]

## Key takeaways

- The request-body table requires outer `data`, `environment`, and `type`; `timestamp` is optional. All listed `data` fields are marked optional, including `balancePlatform`, `card`, `cardOrderItemId`, `creationDate`, resource `id`, `paymentInstrumentId`, `pin`, and `shippingMethod`. The table thus does not guarantee that a particular card-order or payment-instrument identifier appears in every event. [Raw: Request body, lines 11–31]
- `cardOrderItemId` identifies the order item; `paymentInstrumentId` identifies the related payment instrument. Optional `card` and `pin` objects have status, error-message and tracking-number rows. The table lists card-delivery values `created`, `rejected`, `processing`, `produced`, `shipped`, `delivered`, `notApplicable`, and `unknown` on the `card` object row, but its nested `card.status` description says “status of the PIN delivery.” Preserve that field-description conflict instead of treating the list as a verified enum for both status fields. [Raw: lines 16–28]
- The three test examples show a produced card and PIN together, a shipped card with its tracking number, and a separately shipped PIN with its own tracking number. A produced or shipped example is not proof of delivery to a cardholder, card activation, or payment readiness. `environment` may be `test` or `live`; any `2xx` response accepts the webhook. [Raw: lines 29–95]

## Detail locators

- Event purpose: opening statement, lines 5–7.
- Payload identities, optional fields, state-list wording and card/PIN schema conflict: Request body, lines 11–31.
- Produced-card/PIN and separately shipped card/PIN examples: Request examples, lines 33–86.
- Receiver `2xx` acknowledgement: Responses, lines 87–95.

## Related

- [[adyen-issuing]] — physical-card and payment-instrument context.
- [[adyen-webhooks]] — incoming event and acknowledgement context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.updated/2026-09-15|Adyen Balance Platform card order updated webhook — captured 2026-09-15]]
