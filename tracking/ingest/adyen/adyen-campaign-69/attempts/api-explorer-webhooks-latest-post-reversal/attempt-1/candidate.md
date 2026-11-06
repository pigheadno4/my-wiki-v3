---
title: "Adyen Webhooks latest REVERSAL notification"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REVERSAL"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REVERSAL/2026-11-07.md"
tags: [adyen, webhooks, reversals, online-payments]
---

## Overview

This 2026-11-07-captured Adyen Webhooks `latest` API Explorer reference describes an inbound `POST /REVERSAL` notification reporting the result of a reversal request. Its heading is a notification route, not a merchant operation to initiate a reversal. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The introduction says `modification.action` indicates whether the original payment was cancelled or refunded, or an authorised refund was cancelled. The displayed request-body table does not define `modification.action` or its values, so this snapshot does not establish its placement or an exhaustive action enum.
- The table marks outer `live` and `notificationItems` optional, as well as the item wrapper. Within a notification item, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required; `additionalData`, `originalReference`, `paymentMethod`, and `reason` are optional. These are nested table markings, not a claim that the optional outer container is always present.
- `live` distinguishes Live (`true`) from Test (`false`) origin when present. `merchantAccountCode` identifies the transaction's merchant account, `merchantReference` is the merchant's payment reference, optional `originalReference` refers to the original payment request for modifications, and `pspReference` is Adyen's unique transaction or request reference. `success` describes the event outcome; optional `reason` can explain a refusal when `success` is `false`.
- The response section lists `200 Success` and says webhook events are accepted on the basis of HTTP status. Receiver acceptance does not itself establish that the reversal succeeded. This captured page specifies no authentication, idempotency, propagation timing, further lifecycle, or financial settlement guarantee.

## Detail locators

- Pinned raw, lines 5–7: result purpose and `modification.action` description.
- Pinned raw, lines 11–27: request-body envelope, field requiredness, references, `live` origin, and event outcome.
- Pinned raw, lines 29–32: HTTP response and acceptance rule.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REVERSAL/2026-11-07|REVERSAL API Explorer reference, captured 2026-11-07]]
