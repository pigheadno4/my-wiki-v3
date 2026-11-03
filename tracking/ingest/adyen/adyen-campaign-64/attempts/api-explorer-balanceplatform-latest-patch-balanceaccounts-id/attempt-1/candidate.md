---
title: "Adyen Balance Platform API v2 PATCH /balanceAccounts/{id}"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(id)/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, platforms, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API v2 TEST reference describes `PATCH /balanceAccounts/{id}`, updating the balance account selected by required path `id`. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` URL does not establish a later current version, live access or account eligibility. See [[adyen-platforms]] for the account-holder and balance-account context.

## Key takeaways

- The path `id` identifies the balance account. The request-body table marks every listed property **No**: `accountHolderId`, `description`, `metadata`, `platformPaymentConfiguration` with nested `salesDayClosingTime` and `settlementDelayDays`, `reference`, `status` and `timeZone`. The page does not separately state whole-body requiredness or show a query parameter (raw lines 12–31). Its example updates only `timeZone` (raw lines 33–40).
- Updating `metadata` deletes existing key-value pairs omitted from the supplied metadata object. The `status` enum is `active`, `closed` or `suspended`; linked payment instruments can be used only while the balance account is `active`. If no account time zone is set, it defaults to the account holder's time zone (raw lines 23–31). The separate [[source-adyen-docs-platforms-manage-balance-accounts|Platforms balance-account guide]] says closure is permanent and requires an empty balance account; its raw lines 473–482 supply that prerequisite, which this endpoint table does not state.
- `platformPaymentConfiguration.salesDayClosingTime` accepts HH:MM at whole hours 00 through 07 and defaults to 00:00. `settlementDelayDays` accepts 1–20 business days or null, defaults to null and requires Custom Sales Day Payout enablement for that balance account through an account or implementation manager (raw lines 26–28). This is a conditional configuration requirement, not a universal prerequisite for a balance-account update.
- HTTP 200 says the request succeeded and returns the account-holder ID and balance-account ID as required fields; optional fields include status, configuration, metadata, reference, description, time zone, default currency and a balances array. If the array is present, its balance objects mark `available`, settled `balance`, `currency` and `reserved` required, while `pending` and `pendingAvailable` are optional. The response description says default currency is EUR and immutable after creation; it lists a 300-character description maximum and 150-character reference maximum (raw lines 41–67). The zero balances and active status in the example are illustrative, not funded-state or payout proof (raw lines 169–190).
- Errors are listed as 400, 401, 403, 422 and 500 (raw lines 70–167). The generic 422 and 500 JSON examples refer to payment-instrument operations, so they do not define this PATCH's specific failure conditions (raw lines 231–256). The page specifies no idempotency, propagation timing, asynchronous outcome or reversal contract. A successful balance-account update does not prove payment authorization, settlement, payout execution or bank receipt.

## Detail locators

- Endpoint, TEST v2 server, path and request properties: raw lines 5–31.
- Time-zone request example and success response schema: raw lines 33–67.
- Error schemas and generic examples: raw lines 70–167, 192–256.
- Balance-account closure prerequisite: separate [[source-adyen-docs-platforms-manage-balance-accounts|Platforms guide]], raw lines 473–482; not part of this endpoint schema.

## Related

- [[adyen-platforms]] — balance-account resource context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts]] — separate creation contract.
- [[source-adyen-docs-platforms-manage-balance-accounts]] — separate management and permanent-closure guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(id)/2026-11-02|PATCH balance account reference, captured 2026-11-02]]