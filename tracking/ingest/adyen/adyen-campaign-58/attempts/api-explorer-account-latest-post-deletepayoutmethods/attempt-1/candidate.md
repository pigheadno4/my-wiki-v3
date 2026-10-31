---
title: "Adyen Account API v6: delete payout methods"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/deletePayoutMethods"
raw_files:
  - "adyen/api-explorer/Account/latest/post/deletePayoutMethods/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, payout-methods]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /deletePayoutMethods` on the TEST Account API v6 server (`https://cal-test.adyen.com/cal/services/Account/v6`). It deletes payout methods associated with a Classic Platforms account holder; the request identifies the holder by `accountHolderCode` and the methods by `payoutMethodCodes`. This is an account-holder payout-method operation, not a payout initiation or proof that a transfer reached a beneficiary.

## Key takeaways

- The request schema marks both `accountHolderCode` (string) and `payoutMethodCodes` (array of strings) required. The example supplies one code; the page does not state a minimum array length, idempotency rule, or what happens to an in-flight payout.
- A 200 response says the request succeeded. A 202 response says it was accepted for processing but processing has not completed. Both response schemas list optional `invalidFields`, `pspReference`, and `resultCode`; the page gives no success example or follow-up event that proves deletion completed. Treat an accepted request as a receipt, not a confirmed final state.
- The page lists 400 (unreadable request), 401 (authentication required), 403 (insufficient permissions), 422 (validation), and 500 (server processing) responses. It does not name a specific credential role or establish LIVE availability.

## Detail locators

- Operation and TEST server: raw lines 5–10.
- Required request fields and example: raw lines 14–30.
- Success and accepted-for-processing response schemas: raw lines 31–64.
- Client/server errors and generic error examples: raw lines 67–155.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — the older account-holder/account model. Keep this Account API operation separate from newer balance-platform resource contracts.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/deletePayoutMethods/2026-09-15|Account API v6 POST /deletePayoutMethods (captured 2026-09-15)]]
