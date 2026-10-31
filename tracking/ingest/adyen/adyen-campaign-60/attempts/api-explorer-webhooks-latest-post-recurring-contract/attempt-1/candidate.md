---
title: "Adyen Webhooks: RECURRING_CONTRACT created notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/RECURRING_CONTRACT"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/RECURRING_CONTRACT/2026-09-15.md"
tags: [adyen, webhooks, recurring, tokenization]
---

## Overview

This captured Adyen API Explorer `Webhooks/latest` POST reference describes an incoming `RECURRING_CONTRACT` notification when a recurring contract has been created. The page directs merchants to enable this non-default webhook in Customer Area. The POST heading is the notification route, not a merchant token-creation operation. See [[adyen]], [[adyen-tokenization]], and [[adyen-webhooks]].

## Key takeaways

- The displayed request-body table marks `live`, `notificationItems`, and the nested `NotificationRequestItem` wrapper optional. Within an item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `originalPsp`, `pspReference`, and `success` are marked required. The example uses `eventCode: "RECURRING_CONTRACT"`; its USD zero-value payment and `ideal` method are illustrative.
- For this event, `originalPsp` is the initial payment's `pspReference`, while the notification item's `pspReference` is the stored-payment-details token for recurring payments and is the same as `recurringDetailReference`. Do not read this event's `pspReference` as the initial payment reference. `merchantReference` is the merchant payment reference; optional `originalReference` is separately described for modifications.
- `success` reports execution of the specified event; `reason` is described as a short refusal explanation if `success=false`. A created-contract notification and a successful event value do not establish any later recurring payment authorisation, capture, settlement, or token scope beyond this contract.
- The example's `additionalData` includes shopper, recurring-detail, HMAC-signature, and checkout-session fields. These are example values in an optional generic container, not separately required fields or a signature-verification procedure in this reference.
- The response section lists `200 Success` and says webhook events are accepted based on HTTP status. Receiver acceptance is separate from contract creation and any later payment. This page does not establish delivery order, retries, deduplication, or subsequent financial outcome.

## Detail locators

- Raw lines 5–7: contract-created event and Customer Area enablement.
- Raw lines 11–28: request-body table, field requiredness, `originalPsp` initial-payment identity, `pspReference` token identity, `live` origin, conditional `reason`, and event-scoped `success`.
- Raw lines 30–64: illustrative test payload, zero USD amount, `ideal` method, extra `additionalData` fields, distinct original-payment and token references, and `success="true"`.
- Raw lines 65–68: `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen-tokenization]] — stored-payment token and recurring use context.
- [[adyen-webhooks]] — webhook families and receiver context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/RECURRING_CONTRACT/2026-09-15|Captured RECURRING_CONTRACT webhook reference]]
