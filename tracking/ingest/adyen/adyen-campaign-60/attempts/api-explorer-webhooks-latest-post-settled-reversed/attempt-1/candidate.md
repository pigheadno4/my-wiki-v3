---
title: "Adyen Webhooks latest POST /SETTLED_REVERSED"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/SETTLED_REVERSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/SETTLED_REVERSED/2026-09-15.md"
tags: [adyen, webhooks, settlement, reversal]
---

## Overview

This 2026-09-15 API Explorer Webhooks `latest` POST /SETTLED_REVERSED snapshot describes an incoming event for a debit reversing a settled capture when Adyen has not received funds from the card scheme or payment method within 30 days of capture. The page says the webhook is available for all payment methods for merchants on Sales Day Payout and must be enabled in Customer Area. See [[adyen]], [[adyen-webhooks]], and [[adyen-sales-day-payout]].

## Key takeaways

- The event is a reversal of an earlier `settled` transaction, with the 30-day condition tied to Adyen's nonreceipt of scheme or payment-method funds. The POST heading names a webhook event, not a merchant operation. The stated Sales Day Payout and enablement qualifications matter; the page does not establish availability for another payout model.
- The table marks top-level `live` and `notificationItems` optional. Inside a `NotificationRequestItem`, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `originalReference`, `pspReference`, and string `success` are required. Here `originalReference` is required and points to the original payment request reference for modifications; `pspReference` identifies Adyen's transaction or request reference. The example uses `eventCode: "SETTLED_REVERSED"` and includes `settlementReference` and `expectedValueDate` only as optional `additionalData` example values.
- String `success` reports execution outcome of this event; optional `reason` describes refusal when false. The example's true value is not proof of the original scheme funding, a later re-settlement, or bank receipt. The generic `amount` row calls it payment amount and says HTTP POST currency/value are URL parameters, while the JSON example nests them in an amount object; the page does not reconcile these representations.
- The response lists `200 Success` and HTTP-status-based webhook acceptance. Receiver acceptance is separate from the reversal state and event `success`. No delivery, order, retry, deduplication, signature, or post-reversal recovery rule is stated here.

## Detail locators

- Reversal, 30-day nonreceipt condition, Sales Day Payout scope and Customer Area enablement: raw lines 5–7.
- Body fields, required `originalReference`, reference identities, amount wording and success scope: raw lines 11–27.
- Example event, amount and optional additionalData: raw lines 29–59.
- HTTP response acceptance: raw lines 60–63.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-sales-day-payout]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/SETTLED_REVERSED/2026-09-15|API Explorer SETTLED_REVERSED webhook reference (2026-09-15)]]
