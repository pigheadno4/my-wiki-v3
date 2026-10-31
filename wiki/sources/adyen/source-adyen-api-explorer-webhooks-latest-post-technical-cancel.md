---
title: "Adyen Webhooks: TECHNICAL_CANCEL result notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/TECHNICAL_CANCEL"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/TECHNICAL_CANCEL/2026-09-15.md"
tags: [adyen, webhooks, technical-cancel, online-payments]
---

## Overview

This captured Adyen API Explorer `Webhooks/latest` POST reference describes an incoming `TECHNICAL_CANCEL` notification reporting the result of a technical cancel request. The POST heading is a webhook delivery route, not the merchant cancellation request endpoint. See [[adyen]], [[adyen-online-payments]], and [[adyen-webhooks]].

## Key takeaways

- The displayed request-body table marks `live`, `notificationItems`, and the nested `NotificationRequestItem` wrapper optional. Within an item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. `eventCode` identifies the event type; the example sets it to `TECHNICAL_CANCEL`.
- `merchantReference` is the merchant payment reference, while `pspReference` is Adyen's transaction or request reference. Optional `originalReference` is described for modifications as corresponding to the original payment request. The example includes distinct original and PSP references, without changing requiredness.
- `success` reports whether the specified event executed successfully; if `false`, `reason` is described as a short refusal explanation. This notification is the technical-cancel result. The page does not state technical-cancel request eligibility, timing limits, or any broader refund or settlement result.
- The response section lists `200 Success` and says webhook events are accepted based on HTTP status. Receiver acceptance is separate from the cancellation event's `success` value. The reference does not establish delivery order, retries, deduplication, signature verification, or later financial finality.

## Detail locators

- Raw lines 5–7: technical-cancel result purpose.
- Raw lines 11–27: request-body schema, required versus optional fields, `live` environment flag, payment and modification reference identities, conditional `reason`, and event-scoped `success`. `amount` is described as payment amount; the table notes currency and value as URL parameters for HTTP POST notifications.
- Raw lines 29–58: illustrative test-origin EUR 1000 `TECHNICAL_CANCEL` payload with separate original and PSP references and `success="true"`.
- Raw lines 59–62: `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen-online-payments]] — payment cancellation and request context.
- [[adyen-webhooks]] — Adyen webhook families and receiver context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/TECHNICAL_CANCEL/2026-09-15|Captured TECHNICAL_CANCEL webhook reference]]
