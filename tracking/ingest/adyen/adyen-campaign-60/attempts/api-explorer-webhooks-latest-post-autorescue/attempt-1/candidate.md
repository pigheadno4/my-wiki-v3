---
title: "Adyen Webhooks latest AUTORESCUE notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTORESCUE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/AUTORESCUE/2026-09-15.md"
tags: [adyen, webhooks, auto-rescue, recurring-payments]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` API Explorer POST reference describes an incoming `AUTORESCUE` notification when the Auto Rescue process ends. It is a notification contract, not an operation for the merchant to initiate a rescue. See [[adyen]], [[adyen-webhooks]], and [[adyen-card-auto-rescue]].

## Key takeaways

- The example has `eventCode: AUTORESCUE`, `success: "true"`, and `additionalData.retry.rescueReference` and `merchantOrderReference`. Those example fields and values do not establish a universal required payload beyond the parameter table. The item schema marks `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, `amount`, and `success` as required; the outer `live` and `notificationItems` and the item wrapper are marked optional.
- `success` reports whether the event named by `eventCode` executed successfully; when it is `false`, optional `reason` contains a short refusal explanation. This reference does not itself establish a successful underlying payment, capture, or settlement. `pspReference` identifies the associated transaction or request; `merchantReference` is the merchant's payment reference. `originalReference` is optional and described for modifications.
- The response section says webhook events are accepted on the basis of the HTTP status code and shows `200 Success`. This is an acceptance signal, separate from the event outcome.

## Detail locators

- [Pinned raw, Parameters / Request body](https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTORESCUE) — envelope, item fields and requiredness; `live` identifies live versus test origin, and `eventDate` is the event-generation time.
- [Pinned raw, Request examples / autorescue](https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTORESCUE) — one illustrative payload, including amount, references, and `additionalData`.
- [Pinned raw, Responses / 200 Success](https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTORESCUE) — HTTP status acceptance statement.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/AUTORESCUE/2026-09-15|AUTORESCUE API Explorer reference, captured 2026-09-15]]
