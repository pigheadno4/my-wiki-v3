---
title: "GET /grantAccounts/{id} — Get a grant account | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/grantAccounts/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/grantAccounts/(id)/2026-11-03.md"
tags: [adyen, balance-platform-api, capital, grant-account, api-reference]
---

## Overview

This captured Balance Platform API `/bcl/v2` reference documents `GET /grantAccounts/{id}`, a lookup of one Capital grant account by its grant-account identifier. The page lists the TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`. It does not list a live server or state account-specific availability. [[adyen]] [[adyen-capital]]

## Key takeaways

- The required string path parameter `id` is the unique grant-account identifier. The captured operation specifies no query parameters or request body; it does not name a caller role, idempotency key, or endpoint-specific default.
- A `200 Success` says the request succeeded and may return `balances`, `fundingBalanceAccountId`, grant-account `id`, and `limits`. These top-level response fields are marked optional in the captured schema. Within a returned `balances` item, `currency`, `fee`, `principal`, and `total` are marked required, and `total` is described as principal plus fee. Within a returned limit `amount`, `currency` and integer `value` are marked required; `value` is in minor units. Nested requiredness does not make the optional parent array or object mandatory.
- The response is grant-account detail, not a grant request, accepted offer, disbursement confirmation, repayment completion, payment authorization, settlement, or bank receipt. This reference does not provide a grant status, lifecycle transition, propagation timing, or financial outcome guarantee.
- The page lists `400` malformed-request, `401` authentication, `403` permission, `422` validation, and `500` server errors with a problem-detail body. The generic `422` and `500` examples describe payment-instrument operations; they are not grant-account-specific behavior or constraints.

## Detail locators

- Endpoint purpose, TEST server and path parameter: raw lines 5–17.
- `200` response and optional versus nested-required fields: raw lines 19–37.
- Error schemas: raw lines 40–137. Generic examples and their unrelated payment-instrument wording: raw lines 139–205.

## Related

- [[adyen-capital]] — Capital product and grant lifecycle context.
- [[source-adyen-docs-capital-get-grant-balances]] — separate Capital guide for grant and grant-account balance lookup.
- [[source-adyen-api-explorer-capital-latest-get-grants]] — separate Capital API grant-list response; a grant ID is distinct from this endpoint's grant-account ID.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/grantAccounts/(id)/2026-11-03|GET /grantAccounts/{id} captured 2026-11-03]]
