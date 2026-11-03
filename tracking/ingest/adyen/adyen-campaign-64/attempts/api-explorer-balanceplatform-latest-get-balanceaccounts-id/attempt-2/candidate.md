---
title: "GET /balanceAccounts/{id} — Get a balance account | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balanceAccounts/{id}`, a read of a balance-account resource and its balances for the default currency and other currencies with a non-zero balance. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the reference URL says `latest`, while the server path identifies `v2`. The balance-account ID and associated account-holder ID are distinct. See [[adyen-platforms]] for the platform resource context.

## Key takeaways

- `id` is the only documented request parameter: a required string path ID for the balance account. This GET reference lists no request body, query parameter, input default or limit. The 200 response is labeled request success and requires the associated `accountHolderId` and balance-account `id`. [Raw: lines 9–27, 37]
- The `balances` array is optional in the response schema, although the purpose line describes balances for the default currency and other currencies with non-zero balances. Within a returned balance object, `available` (for use), `balance` (settled transaction sum), `currency` and `reserved` are required; `pending` and `pendingAvailable` are optional. The `pendingAvailable` field description says it becomes available after pending settlement and prints a lower-of(`pending`, `pending + available`) formula. These fields represent different balance states; the example's EUR zeros are illustrative and do not prove later available funds or a completed payout. [Raw: lines 7, 28–34, 149–170]

> [!warning] Contradiction
> The GET response field prints the `pendingAvailable` lower-of formula [Raw: line 33], but Example 2 in [[source-adyen-docs-platforms-balance-types]] shows Pending EUR -70, Available EUR -20 and Pending available EUR -70 [that guide's raw: lines 72–84]; the literal formula yields EUR -90. These dated snapshots do not establish a reliable executable calculation from that formula alone.

- Optional response fields include `defaultCurrencyCode` (EUR default, immutable after creation), `description` (maximum 300 characters), `metadata`, `migratedAccountCode`, `platformPaymentConfiguration`, `reference` (maximum 150 characters), `status` (active by default) and `timeZone` (account-holder time zone default). The metadata-omission deletion note concerns an update, not this GET. The optional configuration fields have a 00:00 closing-time default and a nullable 1–20-business-day settlement delay requiring Custom Sales Day Payout enablement; their presence in a read does not grant that capability. [Raw: lines 35–45]
- The page lists 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 server-processing errors with a common error-body schema. Its generic 422 and 500 examples discuss payment-instrument update/creation, so they do not establish a balance-account GET mutation or failure condition. A returned balance account or reported status is readback, not resource creation, verification, authorization, booking, payout or bank-receipt proof. [Raw: lines 48–145, 172–236]

## Detail locators

- Purpose, TEST v2 server and required path parameter: pinned raw lines 5–17.
- 200 response fields, balance meanings and optional configuration: lines 19–45; success example: lines 147–170.
- Error headings and body schemas: lines 48–145; generic error examples: lines 172–236.

## Related

- [[adyen-platforms]] — platform account-holder and balance-account resource context.
- [[source-adyen-docs-platforms-balance-types]] — worked balance examples and the `pendingAvailable` formula conflict.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/2026-11-02|GET /balanceAccounts/{id} — captured 2026-11-02]]