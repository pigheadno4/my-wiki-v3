---
title: "Adyen Webhooks: PAYOUT_DECLINE notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PAYOUT_DECLINE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PAYOUT_DECLINE/2026-09-15.md"
tags: [adyen, webhooks, payouts, deprecated]
---

## Overview

This 2026-09-15 capture of Adyen API Explorer `Webhooks/latest` `POST /PAYOUT_DECLINE` describes an incoming notification that a payout was declined. The webhook is deprecated and does not support new integrations: Adyen directs new integrations to Transfer Webhooks and existing Payout API users to their Adyen contact for Transfers API migration. This legacy payout event should not be conflated with a Transfer webhook state. See [[adyen]], [[adyen-webhooks]], and [[adyen-payouts]].

## Key takeaways

- The request example sets `eventCode` to `PAYOUT_DECLINE` and `success` to `true`. The schema defines `success` as the outcome of the named event; `true` here is compatible with a successfully executed decline event, not a successful payout. The page does not state a payout-completion or recipient-credit transition.
- The item schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. `originalReference` is optional and described for modifications as the original payment-request reference. The top-level `live` and `notificationItems` and the nested `NotificationRequestItem` rows are marked optional in this table.
- `reason` is optional and described as a short refusal explanation if `success=false`; the illustrative declined-payout payload has an empty `reason` with `success=true`. Do not treat `reason` as the payout-decline cause on the basis of this page. `hmacSignature` and `paymentMethodVariant` appear only in the example's generic `additionalData`.
- The response section lists `200 Success` and says webhook acceptance is based on HTTP status code. Acceptance concerns the receiver's HTTP response, separate from the declined payout event. This endpoint page does not specify delivery order, retry/deduplication, signature-validation procedure, or later payout/transfer outcome.

## Detail locators

- Deprecation, migration direction, and event meaning: raw lines 5–23.
- Request-body schema, requiredness, identities, and conditional `reason`: raw lines 25–43.
- Illustrative test payload: raw lines 45–75.
- HTTP response acceptance: raw lines 76–79.

## Related

- [[adyen-payouts]] — legacy Payout API and Transfers API distinction.
- [[adyen-webhooks]] — webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_DECLINE/2026-09-15|Adyen API Explorer PAYOUT_DECLINE reference, captured 2026-09-15]]
