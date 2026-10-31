---
title: "Adyen Webhooks: CHARGEBACK notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CHARGEBACK"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CHARGEBACK/2026-09-15.md"
tags: [adyen, webhooks, disputes, chargebacks]
---

## Overview

This 2026-09-15 capture of the Adyen API Explorer `Webhooks/latest` `POST /CHARGEBACK` reference describes an incoming payment chargeback notification: the payment was charged back and funds were deducted from the merchant account. The POST heading names the webhook event received by a merchant endpoint, not a merchant chargeback operation. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- In the request item, `eventCode` identifies the event type; the example sets it to `CHARGEBACK`. `success` is the outcome of that event code, not a separate statement that a dispute has been defended or reversed.
- The item schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. The enclosing `live`, `notificationItems`, and `NotificationRequestItem` rows are marked optional in this captured table. `originalReference` is optional and, for modifications, corresponds to the original payment request; `pspReference` identifies the transaction or request.
- The example includes `chargebackReasonCode`, `defensePeriodEndsAt`, `defendable`, `capturePspReference`, and `hmacSignature` in generic `additionalData`. The table does not make those sample fields required or define a defense workflow, signature-verification procedure, or deadline rule.
- The response section says webhook events are accepted on the basis of HTTP status code and lists `200 Success`. Receiver acceptance is separate from the chargeback and deducted-funds event described by the notification. This page does not specify delivery order, retries, deduplication, or financial reversal.

## Detail locators

- Event meaning: raw lines 5–7.
- Request-body requiredness, identifiers, event outcome, and conditional refusal `reason`: raw lines 11–27.
- Illustrative `CHARGEBACK` payload and additional data: raw lines 29–70.
- Response acceptance: raw lines 71–74.

## Related

- [[adyen-webhooks]] — webhook-family context.
- [[source-adyen-docs-risk-management-disputes-api-dispute-notifications]] — separate dispute-notification guide; consult its own evidence for broader lifecycle rules.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CHARGEBACK/2026-09-15|Adyen API Explorer CHARGEBACK reference, captured 2026-09-15]]
