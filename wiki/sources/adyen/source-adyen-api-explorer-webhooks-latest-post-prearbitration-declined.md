---
title: "Adyen Webhooks POST /PREARBITRATION_DECLINED — declined pre-arbitration case"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED/2026-09-15.md"
tags: [adyen, webhooks, disputes, prearbitration]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` POST /PREARBITRATION_DECLINED reference describes an incoming notification that a pre-arbitration case was declined. The POST label identifies a webhook event, not a merchant dispute API operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-risk-management]].

## Key takeaways

- The page states the case was declined. It provides no request example, case identifier, decline reason specific to pre-arbitration, next dispute stage, or financial outcome. Do not interpret the generic `success` field as a claim that the merchant won or lost the underlying payment dispute.
- The displayed nested `NotificationRequestItem` table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. `success` is a string indicating whether the event identified by `eventCode` executed; optional `reason` is described as a short refusal explanation when `success` is `false`. Optional `originalReference` is described generically for modifications as the original payment request. The page does not map `pspReference` specifically to a pre-arbitration case ID.
- The response section shows `200 Success` and says webhook acceptance is based on HTTP status code. Receipt acceptance is distinct from the case-declined event and from the event's `success` value.

## Detail locators

- Request body table, including optional outer `live` and `notificationItems`, nested field requirements, references, and refusal-field wording: raw lines 9–27. Outer optionality must not be collapsed into the nested field requirements.
- HTTP response acceptance wording: raw lines 29–32. The page has no example payload or delivery/order/retry/deduplication/signature/finality rule.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — incoming webhook context.
- [[adyen-risk-management]] — dispute documentation route.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED/2026-09-15|Adyen Webhooks latest POST /PREARBITRATION_DECLINED, captured 2026-09-15]]
