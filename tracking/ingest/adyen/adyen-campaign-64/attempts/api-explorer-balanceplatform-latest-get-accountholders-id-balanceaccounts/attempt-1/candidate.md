---
title: "GET /accountHolders/{id}/balanceAccounts — List an account holder's balance accounts | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/balanceAccounts"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/balanceAccounts/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, account-holders, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /accountHolders/{id}/balanceAccounts`, a paginated read of balance accounts associated with one account holder. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest`, while the server path identifies v2. See [[adyen-platforms]] for the platform resource context.

## Key takeaways

- The required path `id` is the account-holder identifier, distinct from each returned balance-account `id`. Optional query `limit` defaults to 10 and has a maximum of 100 items per page; optional `offset` skips items. The response requires a `balanceAccounts` array and `hasNext`/`hasPrevious` booleans. Each listed account has required `accountHolderId` and balance-account `id`. [Raw: lines 5–9, 14–26, 30–50]
- Optional account fields include default currency, description, metadata, migrated classic account code, platform payment configuration, reference, status and time zone. The table describes default currency as EUR and unchangeable after creation; the status is active by default. If metadata is updated, omission of existing pairs deletes them. The optional settlement-delay field requires Custom Sales Day Payout enablement and allows 1–20 business days or null; this is configuration detail, not a required GET input. [Raw: lines 36–48]
- The page lists 400, 401, 403, 422 and 500 errors. Its generic 422 and 500 examples concern payment-instrument changes or creation, so they do not establish this GET route's specific validation or lifecycle behavior. [Raw: lines 53–150, 232–257]
- A 200 response reports associated balance-account records and pagination state at read time. It does not itself create or activate an account, establish capability eligibility, authorize a payment, book funds, execute settlement or prove bank receipt. The example with three active accounts is illustrative. [Raw: lines 5–7, 30–50, 152–191]

## Detail locators

- Purpose, captured TEST v2 server and path/query inputs: pinned raw lines 5–26.
- Success schema and field descriptions: lines 28–50; error schemas: lines 53–150.
- Success and generic error examples: lines 152–258.

## Related

- [[adyen-platforms]] — platform account-holder and balance-account context.
- [[source-adyen-docs-platforms-account-structure-resources]] — separate platform resources.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts]] — separate balance-account creation route.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/balanceAccounts/2026-11-02|Captured API Explorer page (2026-11-02)]]
