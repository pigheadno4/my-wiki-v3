---
title: "Adyen Account API v6: update account-holder payout or processing state"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolderState"
raw_files:
  - "adyen/api-explorer/Account/latest/post/updateAccountHolderState/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holder, payout-state, processing-state]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /updateAccountHolderState` on the TEST Account API v6 server (`https://cal-test.adyen.com/cal/services/Account/v6`). It enables or disables an account holder's `Processing` or `Payout` state. The request does not set the holder's overall `Active`, `Inactive`, `Suspended`, or `Closed` status directly.

## Key takeaways

- The request requires `accountHolderCode`, `disable` (true to disable, false to enable), and `stateType` (`Processing` or `Payout`). `reason` is listed as optional in the table but is required when disabling the selected state. The example disables `Payout`; it does not limit the operation to payout state.
- In the response schema, `accountHolderStatus.payoutState.disabled` is the platform-controlled payout disable flag across all of the holder's accounts. If true, `allowPayout` is false; if false, `allowPayout` can still be false due to other conditions, including KYC or Adyen restrictions. `allowPayout` is the aggregate payout status. `notAllowedReason` describes an Adyen-side payout restriction, and `payoutLimit` applies only when payouts are allowed but limited. Enabling the platform flag alone is therefore not a guarantee that payouts become allowed.
- `accountHolderStatus.processingState` has separate disable/reason and tier-bound fields. The response also has optional scheduled `InactivateAccount` or `RefundNotPaidOutTransfers` events and a nested `status` enum; those response fields do not turn this endpoint into a full status-change operation.
- A 200 says the request succeeded. A 202 says the request was accepted for processing but is not yet complete. The page lists 400, 401, 403, 422, and 500 errors. It gives no named credential role, success response example, final-state notification, propagation timing, or LIVE execution evidence.

## Detail locators

- Operation and TEST server: raw lines 5–10.
- Required and conditionally required request fields; disabling example: raw lines 14–32.
- 200/202 response schemas, aggregate payout conditions, limits, processing fields, status and events: raw lines 33–108.
- Error responses and examples: raw lines 111–199.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — older account-holder and account model; separate from newer balance-platform resources.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/updateAccountHolderState/2026-09-15|Account API v6 POST /updateAccountHolderState (captured 2026-09-15)]]
