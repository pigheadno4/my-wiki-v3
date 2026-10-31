---
title: "Adyen Webhooks latest POST /EXPIRE"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/EXPIRE"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/EXPIRE/2026-09-15.md"
tags: [adyen, webhooks, authorisation, expiry]
---

## Overview

This 2026-09-15 snapshot of the API Explorer Webhooks `latest` POST /EXPIRE reference describes an incoming notification that the remaining uncaptured amount of an authorisation expired. The POST heading identifies the webhook event, not a merchant operation. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The table marks top-level `live` and `notificationItems` optional; the latter contains an optional `NotificationRequestItem` wrapper. Within the item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and string `success` are marked required. The example uses `eventCode: "EXPIRE"`; `live` distinguishes live versus test origin.
- The page defines `amount` as the amount **originally authorised**, while the event description says the **remaining uncaptured amount** expired. Do not interpret the amount object as a measured remainder. `merchantReference` identifies the merchant's payment reference, `pspReference` Adyen's transaction or request reference, and optional `originalReference` is described for modifications as corresponding to the original payment request. The example omits `originalReference`.
- The EXPIRE item's string `success` is defined as always `true`: it is the event's success flag, not a claim that the authorisation remains usable, the payment was captured, or funds settled. The optional `reason` description addresses `success = false`, although the EXPIRE description says `success` is always true; the example shows an empty reason.
- The response section lists `200 Success` and HTTP-status-based webhook acceptance. This receiving endpoint acceptance is separate from the expired-authorisation event state. This page states no delivery, order, retry, deduplication, signature, reversal, or funds-receipt contract.

## Detail locators

- Event identity and remaining-uncaptured-amount description: raw lines 5–7.
- Request-body requiredness, originally authorised amount, reference identities, conditional reason, and always-true success: raw lines 11–27.
- EXPIRE example with EUR amount, no `originalReference`, empty `reason`, and string `success`: raw lines 29–53.
- HTTP response acceptance: raw lines 54–57.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/EXPIRE/2026-09-15|API Explorer EXPIRE webhook reference (2026-09-15)]]
