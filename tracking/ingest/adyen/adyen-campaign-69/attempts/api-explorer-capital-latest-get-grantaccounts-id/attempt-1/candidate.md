---
title: "Adyen Capital API v1: get a grant account"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grantAccounts/(id)"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07.md"
tags: [adyen, capital, grant-account, api-explorer]
---

## Overview

This November 2026 Capital API v1 `GET /grantAccounts/{id}` reference returns details of one grant account, which tracks existing grants in a marketplace or platform. It is a grant-account read, distinct from an individual grant, offer, disbursement, transfer or payment outcome. [[adyen]] [[adyen-capital]]

## Key takeaways

- The required path `id` is the grant-account ID. The operation lists TEST and Live `/capital/v1` servers and specifies no query parameter, request body, default, pagination, idempotency or operation-specific role. The separate Capital API v1 overview requires `X-API-Key`, both Capital configuration and grant-initiation credential roles, and a Live key for Live calls. [[source-adyen-api-explorer-capital-latest-overview]]
- `200` means the lookup succeeded. Its `balances`, `fundingBalanceAccountId`, grant-account `id`, and `limits` fields are all optional in the response schema. `balances` summarizes grants tracked by this account by currency; if a balance item appears, its currency, fee, principal, and total are required, and total is described as principal plus fee. The table describes principal as a grant amount paid out to the user; readback alone does not verify a particular disbursement or repayment.
- `fundingBalanceAccountId` identifies the balance account used to fund the grant. `limits` describes maximum grant-disbursement funds; if a limit's optional `amount` appears, currency and minor-unit integer value are required within it. A limit is not an approved offer or evidence of funds actually disbursed.
- The reference lists `404` entity not found and `422` validation error, with optional problem-detail fields. It gives no success/error JSON examples, status lifecycle, timing or bank-receipt guarantee. A separate Balance Platform API v2 TEST reference also has a `/grantAccounts/{id}` route; its API family and server are different, so route names must not be interchanged. [[source-adyen-api-explorer-balanceplatform-latest-get-grantaccounts-id]]

## Detail locators

- Purpose, Capital `/v1` TEST/Live servers and required ID: [[raw/adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07#L5|raw lines 5–22]].
- Optional `200` parent fields and nested balance/limit fields: [[raw/adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07#L24|raw lines 24–42]].
- `404` and `422` error descriptions and envelope schemas: [[raw/adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07#L45|raw lines 45–80]].
- Companion family authentication/roles and Live key: [[raw/adyen/api-explorer/capital/latest/overview/2026-09-15#L17|overview raw lines 17–48]].

## Related

- [[adyen-capital]] — Capital resource and financing lifecycle context.
- [[source-adyen-api-explorer-capital-latest-overview]] — Capital API v1 family, roles and routes.
- [[source-adyen-api-explorer-balanceplatform-latest-get-grantaccounts-id]] — separate Balance Platform API v2 grant-account lookup.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07|Captured Capital API v1 GET grant-account reference]]
