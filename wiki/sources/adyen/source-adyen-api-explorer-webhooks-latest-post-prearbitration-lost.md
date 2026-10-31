---
title: "Adyen Webhooks latest PREARBITRATION_LOST notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST/2026-09-15.md"
tags: [adyen, webhooks, disputes, prearbitration]
---

## Overview

This 2026-09-15 snapshot of Adyen Webhooks `latest` POST `/PREARBITRATION_LOST` describes an incoming notification that the cardholder's bank declined a pre-arbitration case. The POST heading denotes delivery to a webhook receiver, not a merchant dispute action.

## Key takeaways

- The item schema requires `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` within `NotificationRequestItem`. `originalReference` is optional and is described for modifications as the original payment request reference. The outer `live`, `notificationItems`, and wrapper item are marked optional.
- The example uses `eventCode: "PREARBITRATION_LOST"`, `success: "true"`, EUR 1000, `pspReference`, payment method `visa`, and a reason string; it omits `originalReference`. The schema says `success` reports execution of the named event, not payment authorization or a new dispute resolution guarantee. The generic `reason` description associates explanatory refusal text with `success=false`, although the example has a reason and `success=true`; preserve this example/table tension.
- The response section labels `200 Success` and says webhook events are accepted on the basis of HTTP status code. Receiver acceptance is distinct from the reported pre-arbitration outcome. This page does not establish delivery order, retry/deduplication, signature verification, funds movement, or subsequent dispute stages.

## Detail locators

- Event identity and bank decision: raw lines 5–7. Field requiredness and reference/outcome descriptions: raw lines 11–27. Full sample payload and example tension: raw lines 29–60. HTTP acceptance: raw lines 61–64.

## Related

- [[adyen]] — provider overview.
- [[adyen-webhooks]] — incoming-event context.
- [[disputes]] — cross-provider dispute context; this event's exact outcome remains in the source.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST/2026-09-15|PREARBITRATION_LOST webhook reference (2026-09-15)]]
