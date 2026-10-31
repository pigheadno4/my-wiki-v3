---
title: "Adyen Account API v6: Create an account"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/createAccount"
raw_files:
  - "adyen/api-explorer/Account/latest/post/createAccount/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, accounts, payouts]
---

## Overview

This 2026-09-15-captured API Explorer reference describes `POST /createAccount` on the **Classic Account API v6 test server** (`https://cal-test.adyen.com/cal/services/Account/v6`). It creates an additional account under an existing account holder identified by `accountHolderCode`; one holder can have multiple accounts. Keep the Classic `accountHolderCode`/`accountCode` model separate from newer balance-platform resources. [[adyen-classic-platforms]] [[adyen]]

## Key takeaways

- `accountHolderCode` is the only request property marked required in this table. Optional `bankAccountUUID` couples a holder-owned bank account for matching-currency scheduled payouts; other currencies use a matching holder bank account. Optional `payoutMethodCode` couples a holder-owned method for scheduled card payouts. See [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 14–24]].
- `payoutSchedule` includes `HOLD`, which prevents scheduled payouts while allowing manual initiation; `payoutScheduleReason` is required **when** `payoutSchedule` is `HOLD`. Optional `payoutSpeed` lists `STANDARD` as default and `SAME_DAY` as another value; this field list alone does not establish same-day eligibility. The optional description has a 256-character limit and specified character set. See [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 19–24]].
- The `metadata` field note says omitted existing key-value pairs are deleted **during a metadata update**. This is an update warning in a creation endpoint's field description, not a claim that this request updates an existing account. See [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw line 20]].
- The response table lists `accountCode`, `accountHolderCode`, optional payout linkage and schedule details, `pspReference`, `resultCode`, `status` (`Active`), and `invalidFields`. HTTP 200 is labeled success; HTTP 202 expressly means accepted for processing and **not completed**. The separate Classic account-creation guide says `/createAccount` is asynchronous and to wait for `ACCOUNT_CREATED` before business logic even after HTTP 200; use that guide's completion boundary, rather than treating this reference's 200 label or optional `Active` field as final creation proof. See [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 34–89]] and [[source-adyen-docs-classic-platforms-account-holders-and-accounts|Classic creation guide]] ([[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|guide raw lines 424–429]]). Account creation does not itself establish verification approval, payout eligibility, or money movement.
- The error sections list 400 malformed/unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server failure. Their response fields and illustrative 400/403 JSON are at [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 92–180]].

## Detail locators

- Request properties, conditional schedule reason and payout coupling: [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 14–24]].
- Basic request example and 200/202 response schemas: [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 26–89]].
- Error schemas and illustrative error bodies: [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|raw lines 92–180]].

## Related

- [[adyen-classic-platforms]] — Classic resource and lifecycle context.
- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — Additional-account flow and `ACCOUNT_CREATED` completion gate.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15|Create an account API reference (captured 2026-09-15)]]
