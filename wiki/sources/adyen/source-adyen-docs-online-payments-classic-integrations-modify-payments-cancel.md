---
title: "Adyen Classic API: cancel an uncaptured payment"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/cancel/2026-09-15.md"
tags: [adyen, classic-api, online-payments, cancellation, authorization, webhooks]
---

## Overview

Adyen's dated Classic Payment API guide covers cancelling the authorization of an **uncaptured** payment, releasing reserved funds. If the payment was captured, the guide routes to a refund; if capture status is uncertain, it routes to `/cancelOrRefund`. The Classic cancel endpoint is marked inactive and unsupported for new integrations, with new builds directed to Checkout API and existing integrations to migration guidance. [[adyen-online-payments]] [[adyen]]

## Key takeaways

- POST `/cancel` with the merchant account and `originalReference` equal to the **original payment's** `pspReference` (from its payment response or `AUTHORISATION` webhook). An optional `reference` is the merchant's reference for the cancellation request. The immediate `[cancel-received]` response carries a **different** PSP reference for the cancellation modification; it acknowledges receipt, not the final outcome.
- The `CANCELLATION` webhook reports the asynchronous result with `originalReference`, a modification `pspReference`, and `success`. `success: false` includes a reason. The page's webhook field description points to a Checkout cancels response while the surrounding instructions describe Classic `/cancel`; preserve the original-versus-modification distinction and use the actual operation's response and webhook for reconciliation.
- If the original payment `pspReference` is unavailable, such as after a timeout, `/technicalCancel` uses `originalMerchantReference` equal to the **original payment request's merchant `reference`**. The guide limits this route to within 24 hours after authorization and to cases where payment references are unique. Its `[technical-cancel-received]` response likewise has a distinct modification PSP reference; a later `TECHNICAL_CANCEL` webhook reports success or failure. Do not confuse the optional new modification `reference` with the original merchant reference.

## Detail locators

- Opening through `Cancel a payment` — uncaptured/captured/unknown-state route selection, inactive-endpoint notice, Customer Area option, and original PSP reference requirement.
- `Cancel a payment` — request fields, `[cancel-received]` response and separate modification PSP reference.
- `CANCELLATION webhook` — asynchronous success/failure, original and modification references, and failure reason.
- `Technical cancel` — missing-original-PSP case, unique merchant reference and 24-hour limits, request and receipt fields.
- `TECHNICAL CANCEL webhook` — asynchronous processing result.

## Related

- [[adyen-online-payments]] — provider online-payment integration and Classic route.
- [[adyen-refunds]] — captured-payment refund concept.
- [[adyen]] — provider overview.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel/2026-09-15|Adyen Classic cancel guide, fetched 2026-09-15]]
