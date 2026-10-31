---
title: "Adyen Webhooks POST /REFUND_FAILED — refund failure event"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND_FAILED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REFUND_FAILED/2026-09-15.md"
tags: [adyen, webhooks, refunds, online-payments]
---

## Overview

This 2026-09-15 snapshot of Adyen Webhooks `latest` POST /REFUND_FAILED describes an incoming refund-failure event. Its heading describes failure due to card-scheme rejection, while its only example names BLIK; this page alone does not resolve payment-method coverage or establish either BLIK eligibility generally or a card-only limit. The POST label is a webhook event, not a merchant refund API operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-refunds]].

## Key takeaways

- The example has `eventCode: "REFUND_FAILED"` and `success: "true"`: execution of this failure event is separate from refund success. The page's card-scheme wording and BLIK example should be read as that page's description and illustration, not an exhaustive method rule.
- The table says optional `reason` explains refusal when event `success` is `false`. Yet the example includes `reason: "Refund Failed"` with `success: "true"`; retain this table/example tension.
- Nested item fields marked required include `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success`. This API Explorer table describes optional `originalReference` generically for modifications as the original payment request. The separate [[source-adyen-docs-online-payments-refund|refund guide]] maps `originalReference` specifically to the original payment PSP reference and `pspReference` to the refund request PSP reference for REFUND_FAILED (guide raw lines 673–681).
- The response section says webhook events are accepted on the basis of HTTP status code and shows `200 Success`. Receiver acceptance is separate from the failed-refund event and does not establish money movement.

## Detail locators

- API Explorer request body table, including optional outer `live` and `notificationItems`, nested field requirements, reference descriptions, and `reason` wording: raw lines 9–27. Outer optionality differs from nested field requiredness.
- JSON example with EUR 1000, optional HMAC sample field, BLIK method, original reference, `Refund Failed` reason, and `success: "true"`: raw lines 29–59. The sample does not establish a signature requirement.
- HTTP acceptance wording: raw lines 60–63. This page gives no delivery/order/retry/deduplication or settlement-finality rule.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — incoming webhook context.
- [[adyen-refunds]] — refund lifecycle and later failure boundary.
- [[source-adyen-docs-online-payments-refund]] — separate refund guide for refund-specific reference correlation and subsequent failure context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REFUND_FAILED/2026-09-15|Adyen Webhooks latest POST /REFUND_FAILED, captured 2026-09-15]]
