---
title: "Adyen Webhooks: INFORMATION_SUPPLIED dispute defense notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/INFORMATION_SUPPLIED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/INFORMATION_SUPPLIED/2026-09-15.md"
tags: [adyen, webhooks, disputes, information-supplied]
---

## Overview

This captured Adyen API Explorer `Webhooks/latest` POST reference describes an incoming `INFORMATION_SUPPLIED` notification after dispute defense documents have been uploaded or Adyen has auto-defended a dispute. The POST heading identifies a webhook event, not a merchant upload operation. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The displayed request-body table marks `live`, `notificationItems`, and the nested `NotificationRequestItem` wrapper optional. Within the item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. `eventCode` identifies the event type; the example uses `INFORMATION_SUPPLIED`.
- `merchantReference` identifies the merchant's payment reference, `pspReference` is Adyen's transaction or request reference, and optional `originalReference` is described for modifications as corresponding to the original payment request. The example shows all three; its fields do not expand schema requiredness.
- `success` is defined as the outcome of the specified event, with `true` for successfully executed and `false` for not successfully executed. The schema says `reason` contains a short refusal explanation if `success=false`, yet the example has a nonempty dispute reason alongside `success="true"`. Do not infer refusal from the presence of `reason` alone.
- The example's `additionalData.disputeStatus` is `Pending`, with chargeback reason and scheme codes, and is illustrative. The notification confirms defense-document supply or auto-defense, not that the dispute has been won, finally resolved, or financially settled.
- The response section lists `200 Success` and says webhook events are accepted based on HTTP status. Receiver acceptance is separate from the event's `success` value. This page does not establish delivery order, retry, deduplication, signature verification, or a later dispute or funds outcome.

## Detail locators

- Raw lines 5–7: event title and uploaded-documents or auto-defense purpose.
- Raw lines 11–27: request-body table, required versus optional nested fields, environment flag, references, event-scoped `success`, and conditional `reason` description. `amount` is described as the payment amount; the table says currency and value are URL parameters for HTTP POST notifications.
- Raw lines 29–60: illustrative live-origin USD 10000 payload, `INFORMATION_SUPPLIED` event code, `Pending` dispute status, chargeback codes, and the nonempty-`reason`/`success="true"` mismatch.
- Raw lines 61–64: `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen-webhooks]] — Adyen webhook concepts and other event families.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/INFORMATION_SUPPLIED/2026-09-15|Captured INFORMATION_SUPPLIED webhook reference]]
