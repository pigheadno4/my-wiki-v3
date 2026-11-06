---
title: "Transfers API v4: get grant reference details"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/grants/(id)"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/grants/(id)/2026-11-07.md"
tags: [adyen, transfers-api, capital, grants, api-reference]
---

## Overview

This captured Transfers API v4 TEST `GET /grants/{id}` reference returns grant-reference details for the required grant ID in the path. The 200 schema includes the grant reference ID, grant account ID, selected grant offer ID, balances, and current grant status. This is grant readback, not proof of disbursement, bank receipt, or completed repayment. See [[adyen]] and [[adyen-capital]].

> [!warning] Contradiction
> The endpoint title and path identify grant-reference lookup, and the path table calls `id` a grant ID, but the introductory sentence says it returns a "capital account" and the 404 description says "The payment was not found." Those statements conflict with the grant-specific 200 schema; this capture does not resolve the mismatched wording.

## Key takeaways

- The sole input is required path `id`; the page lists `https://balanceplatform-api-test.adyen.com/btl/v4` and no live server.
- The 200 schema marks `balances`, `grantAccountId`, `grantOfferId`, `id`, and `status` required. The status enum is `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, or `Revoked`. It does not define transition timing or state-specific payout evidence.
- `amount`, `counterparty`, `fee`, and `repayment` are optional parent objects; nested fields marked required apply within their present parent. `amount` and `fee` values are in minor units, and `repayment.basisPoints` describes a daily deduction from incoming net volume. The optional repayment term's `maximumDays` applies only for a loan contract type.
- The listed errors are 400, 401, 403, 404, 422, and 500.

## Detail locators

- Endpoint identity, server, and path input: raw lines 5–17.
- Success schema, optional objects, and status values: raw lines 19–53.
- Error definitions and response schemas: raw lines 56–173.

## Related

- [[adyen-capital]] — Capital offer, grant, and repayment context.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/grants/(id)/2026-11-07|Transfers API v4 GET grant reference (2026-11-07)]]
