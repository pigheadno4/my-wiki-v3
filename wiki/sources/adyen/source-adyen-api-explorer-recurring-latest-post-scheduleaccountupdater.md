---
title: "Adyen Recurring API v68 POST /scheduleAccountUpdater"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/scheduleAccountUpdater"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/scheduleAccountUpdater/2026-09-15.md"
tags: [adyen, recurring, api, account-updater, cards]
---

## Overview

This 2026-09-15 [[adyen]] Recurring API Explorer capture documents `POST /scheduleAccountUpdater` on the listed TEST `Recurring/v68` server. It schedules an Account Updater run using either credit-card information or a recurring-detail reference paired with the shopper reference. The `latest` URL does not establish a newer API version or LIVE account eligibility. This is a legacy Recurring API operation within the broader [[adyen-tokenization]] area, not a Checkout payment or token-creation endpoint.

## Key takeaways

- The request table marks `merchantAccount` and the merchant's call `reference` required. It marks `card`, `shopperReference` and `selectedRecurringDetailReference` optional at the row level, while the opening rule requires either card information or both recurring-detail and shopper references. Do not treat the two alternatives as simultaneously required. The table does not separately state whole-body requiredness.
- The opening text says all `card` subfields are mandatory when card information is supplied. Yet the nested table marks every listed card field optional, and its card-data example supplies only expiry month/year, holder name and number. This unresolved internal mismatch prevents deriving an exact card-field minimum from this snapshot. The CVC row also includes a Client-Side Encryption-specific warning against posting card details to the server; apply that warning in its stated context.
- A 200 response provides a `pspReference` for this request and a `result`: `Success` means scheduling succeeded; otherwise the result contains an error message. It does not prove that Account Updater ran, changed card details, propagated a token update, or authorized/captured/settled a payment. The examples show `Success` for both request alternatives and a 422 “RecurringShopper not found” error for a token-data request, not universal outcomes.
- The page lists 400, 401, 403, 422 and 500 error categories with optional error fields. No completion timing, downstream update notification, deletion or retry contract appears in this captured endpoint reference.

## Detail locators

- Raw lines 5–14: operation, alternative-input rule and TEST Recurring/v68 server.
- Raw lines 18–34: request table and inconsistent card-field requiredness. Lines 36–60: two request examples.
- Raw lines 61–70: 200 scheduling-result contract. Lines 73–140: API error tables. Lines 142–172: success and 422 examples.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[recurring-payments]]

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/scheduleAccountUpdater/2026-09-15|Adyen Recurring API Explorer POST /scheduleAccountUpdater (captured 2026-09-15)]]
