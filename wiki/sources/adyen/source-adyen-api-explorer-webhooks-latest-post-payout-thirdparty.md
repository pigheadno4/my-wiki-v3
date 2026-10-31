---
title: "Adyen Webhooks latest POST /PAYOUT_THIRDPARTY"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PAYOUT_THIRDPARTY"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PAYOUT_THIRDPARTY/2026-09-15.md"
tags: [adyen, webhooks, payouts, deprecated]
---

## Overview

This 2026-09-15 API Explorer Webhooks `latest` POST /PAYOUT_THIRDPARTY snapshot describes an incoming notification for the result of a third-party payout request under the legacy payout route. The webhook is explicitly deprecated and no longer supports new integrations. New integrations are directed to Transfer Webhooks; existing Payout API users are directed to their Adyen contact for migration to the Transfers API. See [[adyen]], [[adyen-payouts]], and [[adyen-webhooks]].

## Key takeaways

- This POST heading names a webhook event, not a merchant operation to submit a payout. The request-body table marks top-level `live` and `notificationItems` optional; `live` distinguishes live and test origin. Within `NotificationRequestItem`, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and string `success` are marked required. The example uses `eventCode: "PAYOUT_THIRDPARTY"`.
- `merchantReference` is the merchant payment reference, while `pspReference` is Adyen's transaction or request reference. Optional `originalReference` is described for modifications as corresponding to the original payment request; it is absent from this example. The `amount` table describes a payment amount and says HTTP POST notification currency/value are URL parameters, while the JSON example nests them in an amount object; this snapshot does not reconcile the two representations.
- `success` reports whether the named event was executed successfully. Optional `reason` gives a refusal explanation when `success = false`. The successful Visa example, including card details and `hmacSignature` in `additionalData`, is example data; it does not establish universal fields or a signature-verification contract. Event execution or an approved example does not alone prove recipient credit, bank receipt, or settlement.
- The response section lists `200 Success` and says webhook events are accepted by HTTP status code. Receiver acceptance is separate from the event's `success` value and payout lifecycle. This page gives no delivery, ordering, retry, deduplication, or reversal rule.

## Detail locators

- Deprecation, new-integration Transfer Webhooks route, existing-user migration route, and payout-request purpose: raw lines 5–23.
- Body field requiredness, references, amount wording, conditional reason, and event-scoped success: raw lines 27–43.
- Example wrapper, event code, amount, optional card fields, and string success: raw lines 45–76.
- HTTP response acceptance: raw lines 77–80.

## Related

- [[adyen]]
- [[adyen-payouts]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_THIRDPARTY/2026-09-15|API Explorer PAYOUT_THIRDPARTY webhook reference (2026-09-15)]]
