---
title: "Adyen Account API v6: Suspend an account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/suspendAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holders, suspension]
---

## Overview

This 2026-09-15-captured Classic Account API v6 reference describes `POST /suspendAccountHolder` on the test server `https://cal-test.adyen.com/cal/services/Account/v6`. Its stated purpose is to change the identified account holder's status to `Suspended`. The request body table marks only `accountHolderCode` required. It addresses the Classic account holder, not a newer balance-platform legal entity or balance account. [[adyen-classic-platforms]] [[adyen]]

## Key takeaways

- The endpoint's required `accountHolderCode` names the holder to suspend. No pre-suspension status, verification-check condition, reason field or idempotency key is specified in this page's request table. See [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 5–25]].
- The optional response `accountHolderStatus` includes a required **nested** `status` property when that object is present, with values `Active`, `Inactive`, `Suspended`, `Closed`. Its optional `events` can name scheduled `InactivateAccount` or `RefundNotPaidOutTransfers` events with dates and reasons. These event fields do not prove an event ran or a refund completed. See [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 29–63 and 66–100]].
- `payoutState.allowPayout` aggregates conditions across all holder accounts. If false, payouts are not permitted; platform `disabled: true` forces it false, while `disabled: false` alone does not ensure payouts are allowed. The response also separates platform `disableReason` from Adyen `notAllowedReason`, and exposes a limited-payout amount and tier when applicable. `processingState` includes disabled/reason and tier fields. See [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 40–54]].
- HTTP 200 is labeled succeeded; HTTP 202 expressly means accepted for processing **without completion**. `pspReference` identifies the request, not final propagation or a financial outcome. The response also has `resultCode` and `invalidFields`; optional top-level `accountHolderStatus` and its nested required `status` must not be conflated with a required response body. See [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 27–100]].
- The separate Classic verification guide says `Suspended` disallows data updates, payment processing and payouts; it advises hiding or removing the holder from the platform. It says unsuspension is restricted to holders with no failed verification checks, and an unsuspended holder returns to `Inactive`. These are guide-level lifecycle rules, not additional fields or prerequisites stated by this endpoint. See [[source-adyen-docs-classic-platforms-verification-process|verification guide]] and [[raw/adyen/docs/classic-platforms/verification-process/2026-09-15|guide raw lines 104–145]].
- Errors cover 400 request parsing, 401 authentication, 403 insufficient permission, 422 validation and 500 server processing. The 400/403 JSON bodies are examples, not a complete error-code guarantee. See [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 103–191]].

## Detail locators

- Purpose, v6 test server, sole required request property and example: [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 5–26]].
- Both success schemas, nested status, payout/processing states, scheduled events and result fields: [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 27–100]].
- Error schemas and examples: [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|raw lines 103–191]].

## Related

- [[adyen-classic-platforms]] — Classic holder lifecycle context.
- [[source-adyen-docs-classic-platforms-verification-process]] — status effects and conditional unsuspension.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15|Suspend an account holder API reference (captured 2026-09-15)]]
