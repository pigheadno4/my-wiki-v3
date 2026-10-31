---
title: "Adyen Webhooks POST /REFUND_FAILED — scheme-rejected refund"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND_FAILED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REFUND_FAILED/2026-09-15.md"
tags: [adyen, webhooks, refunds, online-payments]
---

## Overview

This 2026-09-15 snapshot of Adyen Webhooks `latest` POST /REFUND_FAILED describes an incoming event for a refund that failed because the card scheme rejected it. The POST label is a webhook event, not a merchant refund API operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-refunds]].

## Key takeaways

- The event heading and description identify card-scheme rejection of the refund. The example has `eventCode: "REFUND_FAILED"` and `success: "true"`: successful execution of the failure event must not be read as a successful refund.
- The displayed table defines `success` as the outcome of the named event and says optional `reason` explains refusal when `success` is `false`. Yet the example includes `reason: "Refund Failed"` with `success: "true"`. Preserve this table/example tension rather than making the conditional description an invariant.
- Nested item fields marked required include `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success`. Optional `originalReference` corresponds to the original payment request for modifications and appears in the example; keep it distinct from the request/transaction `pspReference`.
- The response section says webhook events are accepted on the basis of HTTP status code and shows `200 Success`. Receiver acceptance is separate from the failed-refund event and does not establish money movement.

## Detail locators

- Request body table, including optional outer `live` and `notificationItems`, nested field requirements, reference descriptions, and `reason` wording: raw lines 9–27. Outer optionality is not the same as nested field requiredness.
- JSON example with EUR 1000, optional HMAC sample field, BLIK method, original reference, `Refund Failed` reason, and `success: "true"`: raw lines 29–59. The example does not itself establish a signature requirement.
- HTTP acceptance wording: raw lines 60–63. The snapshot gives no delivery/order/retry/deduplication or settlement-finality rule.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — incoming webhook context.
- [[adyen-refunds]] — refund lifecycle and later failure boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REFUND_FAILED/2026-09-15|Adyen Webhooks latest POST /REFUND_FAILED, captured 2026-09-15]]
