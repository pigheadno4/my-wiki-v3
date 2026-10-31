---
title: "Adyen Webhooks latest PAIDOUT_REVERSED notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PAIDOUT_REVERSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PAIDOUT_REVERSED/2026-09-15.md"
tags: [adyen, webhooks, payouts, reversal, deprecated]
---

## Overview

This 2026-09-15 snapshot of Adyen Webhooks `latest` POST `/PAIDOUT_REVERSED` documents an incoming notification that a financial institution rejected a payout. The page says Adyen will return the funds to the account; it does not show that return as already booked. The webhook is deprecated and does not support new integrations. New integrations are directed to Transfer Webhooks, while existing Payout API users are directed to their Adyen contact for Transfers API migration. The POST heading describes a notification received by a merchant endpoint, not a merchant payout command.

## Key takeaways

- The item schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required within `NotificationRequestItem`. `originalReference`, `reason`, `paymentMethod`, and `additionalData` are optional; the outer `live`, `notificationItems`, and wrapper item are also marked optional. The table describes `pspReference` as the PSP reference for the Capture's PSP reference, a wording to retain as written rather than silently interpreting it as a transfer ID.
- `success` reports the outcome of the named event, not successful payout to the recipient. The example uses `eventCode: "PAIDOUT_REVERSED"`, `success: "true"`, `EUR` amount `1000`, and separate `originalReference` and `pspReference`. The `reason` description says it contains the bank statement description if present, otherwise `PaidOutReversed`; the example instead has an empty string. Treat the example as a conflicting fixture, not a general empty-reason rule.
- The response section labels `200 Success` and says webhook events are accepted by HTTP status code. This is receiver acceptance, distinct from the institution's rejection and any subsequent funds return. This reference does not establish delivery order, retry/deduplication rules, signature verification procedure, bank receipt, or a completed reversal booking.

## Detail locators

- Deprecation, migration routing and payout-rejection/return wording: raw lines 5–24. Request-body requiredness and identity fields: raw lines 28–44. Example payload and reason discrepancy: raw lines 46–71. HTTP acceptance: raw lines 72–75.

## Related

- [[adyen]] — provider overview.
- [[adyen-payouts]] — legacy payout context and distinct Transfers API route.
- [[adyen-webhooks]] — incoming webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PAIDOUT_REVERSED/2026-09-15|PAIDOUT_REVERSED webhook reference (2026-09-15)]]
