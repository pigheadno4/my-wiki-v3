---
title: "GET /balanceAccounts/{id}/transferLimits — Filter and view transfer limits | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balanceAccounts/{id}/transferLimits`, which filters and views transfer limits configured for a balance account. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. See [[adyen-business-accounts]] for account and transfer-limit context.

## Key takeaways

- Required string path `id` identifies the balance account. Optional query filters are `status` (active, inactive, pendingSCA or scheduled), `transferType` (instant or all priorities) and `scope` (perTransaction or perDay). No request body, query default, pagination or list-size limit is specified. [Raw: lines 5–25]
- A 200 marks request success and requires a `transferLimits` array. Each returned limit requires `amount` (three-character ISO currency and numeric value in minor units), limit `id`, `limitStatus`, `scope`, `startsAt` and `transferType`. `endsAt`, platform `reference` and `scaInformation` are optional. The response schema describes per-transaction or per-day maximum amounts and date-based activation or expiry, including no specified end date until override. [Raw: lines 27–48]
- `limitStatus` distinguishes active, inactive, pendingSCA and scheduled. If `scaInformation` is present, its `status` is required and separately distinguishes notPerformed, pending and performed; notPerformed can include an SCA exemption. An active example with `initialLimit` exemption and `notPerformed` SCA status illustrates shape, not proof of a completed authentication or a transfer. [Raw: lines 41–45, 88–131]
- The page lists 404 when one of the transfer limits could not be found and 422 for a validation error; it does not list authentication or permission errors for this route. Error problem-body fields are mostly optional, while fields inside a present `invalidFields` entry are marked required. [Raw: lines 51–86]
- This GET is a read of configured limit records, not an approval, limit change, transfer execution, debit, booking, settlement or bank receipt. The response alone does not establish which limit applies after all other account or platform configuration, whether SCA is required for a later change, or current live availability and eligibility. [Raw: lines 5–48, 88–131]

## Detail locators

- Purpose, TEST v2 server, required balance-account ID and optional filters: pinned raw lines 5–25.
- 200 schema, amount units, statuses, dates and SCA fields: lines 27–48; illustrative list: lines 88–131.
- 404 and 422 error schemas: lines 51–86.

## Related

- [[adyen-business-accounts]] — Business Accounts and transfer-limit context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/2026-11-03|GET balance-account transfer limits — captured 2026-11-03]]