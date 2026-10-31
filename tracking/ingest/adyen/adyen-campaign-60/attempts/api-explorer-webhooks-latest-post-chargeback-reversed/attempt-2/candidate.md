---
title: "Adyen Webhooks latest: CHARGEBACK_REVERSED"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CHARGEBACK_REVERSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CHARGEBACK_REVERSED/2026-09-15.md"
tags: [adyen, webhooks, disputes, chargebacks]
---

## Overview

This 2026-09-15 snapshot of Adyen's Webhooks `latest` `POST /CHARGEBACK_REVERSED` reference describes an incoming dispute notification, not a merchant operation. It says the chargeback was successfully defended toward the issuing bank, but this stage is **not final**: a second chargeback from the issuing bank can still cause the case to be lost. [[adyen]] [[adyen-webhooks]]

## Key takeaways

- The example item uses `eventCode: CHARGEBACK_REVERSED` and `success: "true"`. The `success` field reports execution of the event named by `eventCode`; it does not establish final dispute resolution.
- The request-body table marks the outer `live` and `notificationItems` fields and the nested `NotificationRequestItem` wrapper optional, while marking `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required within the item. `originalReference` is optional and is described for modifications as the reference of the original payment request.
- The `200 Success` response section says webhook events are accepted based on HTTP status code. Acceptance is separate from the dispute stage described by the event. This page specifies no delivery order, retry, or deduplication rule; it explicitly says this dispute stage is not final.

## Detail locators

- Request-body field meanings and requiredness: pinned raw, lines 9–27. In particular, `reason` is optional; the table describes its refusal explanation when `success` is `false`. The example at lines 29–57 has `success: "true"` and a `reason`, so do not treat that sample as a conditional requirement.
- Example payload and identifiers: pinned raw, lines 29–57. The sample is in the test environment (`live: "false"`), with EUR amount, merchant reference, and a PSP reference. Its `additionalData.hmacSignature` is an example value, not a signature-validation rule.
- Acceptance wording: pinned raw, lines 58–61.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CHARGEBACK_REVERSED/2026-09-15|Adyen Webhooks latest CHARGEBACK_REVERSED reference (2026-09-15)]]
