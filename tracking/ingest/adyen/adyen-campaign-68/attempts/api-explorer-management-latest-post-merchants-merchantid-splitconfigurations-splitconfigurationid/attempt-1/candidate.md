---
title: "Adyen Management API: Create a split configuration rule"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md"
tags: [adyen, management-api, platforms, automatic-splits, split-configuration]
---

## Overview

This 2026-11-07 capture of Adyen's Management API `latest` reference lists a TEST `/v3` server. `POST /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}` creates a **rule within the existing split configuration profile** identified in the path; it does not create the profile itself. The API credential needs **Management API - SplitConfiguration read and write**. [[adyen]] [[adyen-automatic-split-configuration]]

## Key takeaways

- Both path IDs are required: `merchantId` identifies the merchant account and `splitConfigurationId` the profile. The request table requires `currency`, `fundingSource`, `paymentMethod`, `shopperInteraction`, and a `splitLogic` object. Within `splitLogic`, `commission` is marked required; its fixed amount and variable percentage fields are individually optional and use minor units and basis points, respectively.
- Rule conditions determine when split logic applies. `cardUsageType` is optional and defaults to `ANY`; `cardRegion` is optional. Optional `additionalCommission` may use a balance-account ID, fixed amount, and/or percentage. The `dcc` split-logic field is in pilot and is not available to all platforms.
- The `paymentFee` field describes a fee-allocation fallback: if no transaction fee type is included in `splitLogic`, Adyen updates the payment request with `paymentFee`, booking all transaction fees to the platform liable balance account. Consult the raw table for the fee types and allocation options; this is configuration behavior, not proof of a completed booking.
- A `200` response describes the split configuration with required `description` and `rules` array; rule and split-logic IDs and top-level `splitConfigurationId` are optional in the response schema. `204` is success with no content. Neither response proves the profile is linked to a store or that any payment, fee, capture, settlement, or payout occurred.

> [!warning] Contradiction
> The request and response tables require `currency` to be a three-character ISO currency code, but the `200` example uses `"currency": "ANY"` for one rule. This capture does not establish whether `ANY` is accepted in requests.

## Detail locators

- Role, server, path IDs and request schema: raw lines 5–57.
- Request example: raw lines 59–84.
- Success/error schemas: raw lines 85–225 (200, 204, 400, 401, 403, 422, 500).
- Response example, including currency conflict: raw lines 227–284.

## Related

- [[adyen-automatic-split-configuration]] — profile selection and transaction-level evidence boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07|Management API create-rule reference (2026-11-07)]]
