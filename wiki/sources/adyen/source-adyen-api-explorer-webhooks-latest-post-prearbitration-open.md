---
title: "Adyen Webhooks: PREARBITRATION_OPEN notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN/2026-09-15.md"
tags: [adyen, webhooks, disputes, prearbitration]
---

## Overview

This 2026-09-15 capture of the Adyen API Explorer `Webhooks/latest` `POST /PREARBITRATION_OPEN` reference describes an incoming disputes notification that the cardholder's bank opened a pre-arbitration case. The heading names a webhook event received by an endpoint, not a merchant operation to open a case. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The notification-item schema requires `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success`. `eventCode` is the notification event type; `success` describes execution of that event code. This page does not provide an example payload or spell out a particular `success` value for this event.
- `originalReference` is optional and described for modifications as the payment request assigned to the original payment. `pspReference` is Adyen's reference associated with the transaction or request. `reason` is optional, with a refusal explanation described only for `success=false`. The enclosing `live`, `notificationItems`, and `NotificationRequestItem` rows are marked optional in the table.
- The page identifies case opening by the cardholder's bank but gives no defense deadline, required merchant action, resolution state, or financial reversal rule. It lists `200 Success` and says webhook acceptance is based on HTTP status code; that receiver acceptance does not decide the case. No delivery-order, retry, deduplication, or signature procedure is specified here.

## Detail locators

- Event identity and bank action: raw lines 5–7.
- Request schema and field requiredness: raw lines 9–27.
- HTTP response acceptance: raw lines 29–32.

## Related

- [[adyen-webhooks]] — incoming webhook context.
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — separate dispute-flow guide for broader lifecycle context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN/2026-09-15|Adyen API Explorer PREARBITRATION_OPEN reference, captured 2026-09-15]]
