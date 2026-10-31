---
title: "Adyen Webhooks latest POST /AUTHORISATION"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTHORISATION"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/AUTHORISATION/2026-09-15.md"
tags: [adyen, webhooks, authorisation, payments]
---

## Overview

This 2026-09-15 snapshot of the API Explorer Webhooks `latest` POST /AUTHORISATION reference describes an incoming notification for the result of an authorisation request linked to the Classic Payment API `/authorise` reference. It is a webhook event contract, not a merchant call to authorise a payment. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The documented request body has optional top-level `live` and `notificationItems` fields. `live` identifies live versus test origin. Within a `NotificationRequestItem`, the table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` as required; this does not make the optional parent container required. The `AUTHORISATION` event code and the wrapper structure are shown in the example.
- `merchantReference` is the merchant's payment reference; `pspReference` is Adyen's reference for the transaction or request. The page does not list an `originalReference` field. `success` is a string flag for whether the payment request succeeded or failed; on failure, `reason` carries failure information. For successful Visa, Mastercard (`mc`) or Amex notifications, the stated conditional `reason` content includes authorisation code and card details.
- `operations` is optional and explicitly experimental; the reference warns against basing code on it. The example includes tokenization `additionalData`, `ach`, follow-up operations, and a successful flag, but those values are example data, not universal event contents.
- The response section lists `200 Success` and says webhook events are accepted on the basis of HTTP status code. That receiver acceptance is separate from the notification's `success` flag and does not establish capture, settlement, or funds receipt. This page gives no delivery, ordering, retry, deduplication, or signature contract.

## Detail locators

- Purpose and linked authorisation request: raw lines 5–7.
- Request-body field requiredness, reference identities, conditional `reason`, and experimental `operations`: raw lines 11–27. The table says HTTP POST notification currency and value are returned as URL parameters; it does not resolve that wording against the JSON amount object shown in the example.
- Example wrapper, `eventCode`, amount, optional values, and string `success`: raw lines 29–64.
- HTTP response acceptance statement: raw lines 65–68.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/AUTHORISATION/2026-09-15|API Explorer AUTHORISATION webhook reference (2026-09-15)]]
