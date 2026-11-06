---
title: "Create a merchant split configuration profile"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/2026-11-07.md"
tags: [adyen, management-api, platforms, automatic-splits]
---

## Overview

This 2026-11-07 snapshot of the [[adyen]] Management API `latest` POST reference lists the v3 TEST server for creating a split configuration profile under the merchant account identified by required path `merchantId`. An API credential with **Management API - SplitConfiguration read and write** is required. The profile is intended for automatic payment splits only after it is associated with a store in that merchant account; the described split is between the platform's liable balance account and the user's balance account.

## Key takeaways

- The request body requires `description` and a `rules` array. Each rule requires `currency`, `fundingSource`, `paymentMethod`, `shopperInteraction`, and a `splitLogic` object; within that object, `commission` is marked required. `cardRegion` and `cardUsageType` are optional conditions; `cardUsageType` defaults to `ANY`. See the pinned table for allowed values and fee, refund, chargeback, tip, remainder, and commission details.
- If no transaction fee type is included in `splitLogic`, the reference says Adyen updates the payment request with `paymentFee`, booking all transaction fees to the platform liable balance account. The `dcc` field is described as a pilot, unavailable to some platforms.
- A `200` response describes the profile with `description` and `rules`, while `splitConfigurationId`, rule `ruleId`, and `splitLogicId` are marked optional in the response schema. `204` is successful processing with no content. Neither response proves store association, a matched payment, booking, settlement, or payout.

> [!warning] Contradiction
> The request and response `currency` tables say a three-character ISO currency code is required (raw lines 31, 97), but both JSON examples set `currency` to `ANY` (lines 65, 237). The example does not establish that `ANY` is accepted for this field.

## Detail locators

- Purpose, store-association condition, role, TEST server, merchant path: raw lines 5–21.
- Request schema and optional/default conditions, split logic, pilot and fee fallback: lines 24–52; request example: 54–84.
- `200` response schema, including optional generated identifiers: lines 85–121; `204` no content: 124–125; illustrative `200` response: 227–262.
- Error descriptions and schemas: `400` lines 128–145, `401` 148–165, `403` 168–185, `422` 188–205, `500` 208–225.

## Related

- [[adyen-automatic-split-configuration]] — automatic split rules and store association.
- [[adyen-platforms]] — platform and balance-account context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/2026-11-07|Create split configuration reference (2026-11-07)]]
