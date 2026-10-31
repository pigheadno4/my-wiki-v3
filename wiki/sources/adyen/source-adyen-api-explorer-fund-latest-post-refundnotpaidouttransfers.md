---
title: "Adyen Fund API v6: refund not-paid-out transfers"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/refundNotPaidOutTransfers"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/refundNotPaidOutTransfers/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, refunds]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /refundNotPaidOutTransfers` on the TEST Fund API v6 server (`https://cal-test.adyen.com/cal/services/Fund/v6`). It requests refunds for all transactions of one account since that account's most recent payout. It is account-based rather than payment-based: only the portion of each payment allocated to the specified account is refunded. Commissions, fees and portions sent to other accounts remain where the original split placed them.

## Key takeaways

- The request requires both `accountCode`, identifying the account from which to perform the refunds, and `accountHolderCode`, identifying its owner. There is no transaction-selection list or amount field in this request schema. The page does not specify an eligible-balance test, a count of affected transactions, or behavior if no transactions qualify.
- A 200 response says the request succeeded. A 202 response says the request was accepted for processing but processing has not completed. Both success schemas list optional `invalidFields`, `pspReference` and `resultCode`; no refund outcome or completed transfer is shown. A request receipt alone does not establish that every refund was executed.
- The page lists 400, 401, 403, 422 and 500 error classes. It does not name a specific credential role, final refund notification, propagation time, idempotency rule, or LIVE availability.

## Detail locators

- Operation, account-based split effect and TEST server: raw lines 5–10.
- Required request fields and example: raw lines 14–28.
- 200 and 202 success schemas: raw lines 29–62.
- Error schemas: raw lines 65–127.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — older account-holder/account and split-payment model; separate from newer balance-platform transfer contracts.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/refundNotPaidOutTransfers/2026-09-15|Fund API v6 POST /refundNotPaidOutTransfers (captured 2026-09-15)]]
