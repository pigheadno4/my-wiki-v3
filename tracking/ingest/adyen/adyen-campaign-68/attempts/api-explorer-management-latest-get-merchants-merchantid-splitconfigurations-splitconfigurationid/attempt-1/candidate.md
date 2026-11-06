---
title: "Adyen Management API: Get a merchant split configuration profile"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configurations]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}` on the shown TEST v3 server (`https://management-test.adyen.com/v3`). It reads a specified split-configuration profile under the merchant account identified in the path. The API credential needs **Management API - SplitConfiguration read and write**. [[adyen]] · [[adyen-automatic-split-configuration]]

## Key takeaways

- Both path identifiers are required: `merchantId` is the merchant account and `splitConfigurationId` is the profile. The reference shows no query parameters or request body.
- A `200` profile representation requires `description` and `rules`; its top-level `splitConfigurationId` is optional. Each returned rule requires `currency`, `fundingSource`, `paymentMethod`, `shopperInteraction`, and `splitLogic`. Within `splitLogic`, `commission` is marked required; `ruleId`, `splitLogicId`, conditions such as `cardRegion` and `cardUsageType`, and the other allocation fields are marked optional. `cardUsageType` describes `ANY` as its default. Commission fixed amounts are in minor units and percentages in basis points.
- Rule conditions describe when split logic applies. The `dcc` allocation field is labeled pilot and unavailable to some platforms. The `paymentFee` description says that if no transaction-fee type is included in `splitLogic`, Adyen updates a **payment request** with `paymentFee`, booking all transaction fees to the platform's liable balance account; this is documented behavior of the configuration, not an effect of this GET.
- `204` means successful processing with no additional content. A `200` readback or example does not prove that the profile is enabled or linked to a store, that any rule matched, or that a payment, capture, booking, settlement, or payout occurred. The reference lists `400`, `401`, `403`, `422`, and `500` errors but gives no idempotency, mutation, deletion, reversal, review, activation, version/conflict, or asynchronous completion contract for this read.

> [!warning] Contradiction
> The `rules[].currency` response schema says its value must be a three-character ISO currency code (raw line 36), while the illustrative `200` response uses `"currency": "ANY"` in one rule (line 176). This capture does not resolve whether `ANY` is accepted or what it means for this field. Do not treat the example as a validation guarantee.

## Detail locators

- Endpoint purpose, required role, TEST server and path IDs: raw lines 5–22.
- `200` response schema and condition/allocation fields: raw lines 24–60. The pilot `dcc` qualifier is at line 50; the transaction-fee fallback description is at line 52.
- `204` and error responses: raw lines 63–164. Illustrative two-rule `200` response: raw lines 166–223.

## Related

- [[adyen]] · [[adyen-automatic-split-configuration]] · [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07|2026-11-07 captured merchant split-configuration profile GET reference]]
