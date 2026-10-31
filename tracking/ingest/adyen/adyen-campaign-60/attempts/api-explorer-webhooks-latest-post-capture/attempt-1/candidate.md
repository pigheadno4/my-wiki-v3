---
title: "Adyen Webhooks POST /CAPTURE — result of capture request"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CAPTURE/2026-09-15.md"
tags: [adyen, webhooks, capture, online-payments]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` POST /CAPTURE reference describes an incoming notification for the result of a payment capture request. The POST label identifies the webhook event, not a merchant capture API operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-payment-capture]].

## Key takeaways

- A notification item identifies its event with `eventCode`; the example uses `CAPTURE`. Its required `success` string reports whether that event executed successfully, while optional `reason` gives a short refusal explanation when `success` is `false`. The example's `success: "true"` illustrates one outcome, not a guarantee for every capture.
- The item has required `merchantAccountCode`, `merchantReference`, `pspReference`, `eventDate`, `eventCode`, `amount`, and `success` fields in the displayed table. `originalReference` is optional and, for modifications, corresponds to the original payment request. `pspReference` identifies the transaction or request; keep it distinct from the merchant reference and original reference.
- The response section says webhook events are accepted on the basis of HTTP status code and shows `200 Success`. This is receiver acceptance of the webhook, separate from the event's `success` outcome or any later capture failure or settlement.

## Detail locators

- Request body table, including optional outer `live` and `notificationItems`, nested required fields, reference identities, amount, environment and refusal reason: raw lines 9–27. The table labels both outer fields and the nested wrapper `No`; do not recast item-field requiredness as outer-body requiredness.
- One JSON capture notification example with EUR 1000 and `success: "true"`: raw lines 29–55.
- Response status/acceptance wording: raw lines 56–59. The snapshot does not specify delivery ordering, retry, deduplication, signature validation, or financial finality.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — webhook families and acknowledgement context.
- [[adyen-payment-capture]] — capture request and outcome boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CAPTURE/2026-09-15|Adyen Webhooks latest POST /CAPTURE, captured 2026-09-15]]
