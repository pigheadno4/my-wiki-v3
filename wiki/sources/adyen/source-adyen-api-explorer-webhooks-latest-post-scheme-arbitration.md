---
title: "Adyen Webhooks: SCHEME_ARBITRATION notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION/2026-09-15.md"
tags: [adyen, webhooks, disputes, arbitration]
---

## Overview

This 2026-09-15 capture of the Adyen API Explorer `Webhooks/latest` `POST /SCHEME_ARBITRATION` reference describes an incoming disputes notification: the issuer escalated a pre-arbitration case to scheme arbitration. The POST heading names the notification received at an endpoint, not a merchant request to escalate a case. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The notification-item schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. `eventCode` identifies the event type, and `success` describes execution of that event code. This page provides no example payload or event-specific `success` value.
- `originalReference` is optional and, for modifications, corresponds to the original payment request. `pspReference` identifies the transaction or request. `reason` is optional and described as a refusal explanation when `success=false`. The enclosing `live`, `notificationItems`, and `NotificationRequestItem` rows are marked optional in the captured table.
- Escalation to scheme arbitration is the only case transition stated here. The page supplies no arbitration decision, defense deadline, merchant action, or financial outcome. It lists `200 Success` and says webhook events are accepted by HTTP status code; that receiver response does not resolve the case. No delivery order, retry, deduplication, or signature procedure is specified in this page.

## Detail locators

- Event identity and issuer escalation: raw lines 5–7.
- Request-body schema and field requiredness: raw lines 9–27.
- HTTP response acceptance: raw lines 29–32.

## Related

- [[adyen-webhooks]] — incoming webhook context.
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — separate dispute-flow guide for broader lifecycle context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION/2026-09-15|Adyen API Explorer SCHEME_ARBITRATION reference, captured 2026-09-15]]
