---
title: "Adyen Management API: update split logic in a rule"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/splitLogic/(splitLogicId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/splitLogic/(splitLogicId)/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configuration]
---

## Overview

This captured Management API PATCH changes the split logic identified by `splitLogicId` within rule `ruleId` of split configuration `splitConfigurationId` under merchant account `merchantId`. All four path IDs are required and identify different resources. The listed server is TEST `/v3`. [[adyen]] [[adyen-automatic-split-configuration]]

## Key takeaways

- The API credential needs `Management API - SplitConfiguration read and write`. The request body requires `commission`; its fixed amount is in minor units and variable percentage in basis points, booked to the platform's liable balance account. Other fee, refund, chargeback, surcharge, tip, remainder, and additional-commission instructions are optional fields.
- If the `splitLogic` object does not include at least one transaction fee type, the described fallback updates the payment request with `paymentFee`, booking all transaction fees to the platform's liable balance account. DCC markup allocation is described as pilot and unavailable to some platforms.
- A `200` response describes the split configuration, its rules and conditional split logic; `204` has no additional content. A configuration response does not prove any payment was split, booked, captured, or settled. The 200 example illustrates multiple rules and IDs; its sample values are not guarantees.
- The page lists 400, 401, 403, 422, and 500 errors.

## Detail locators

- Raw lines 5–24: purpose, role, TEST server, and distinct required path IDs.
- Raw lines 27–52: request schema, amounts, fallback fee behavior, and DCC pilot; lines 54–73: illustrative request.
- Raw lines 74–110: 200 response schema and rule conditions; lines 113–215: 204 and error responses; lines 216–273: illustrative 200 response.

## Related

- [[adyen]]
- [[adyen-automatic-split-configuration]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/splitLogic/(splitLogicId)/2026-11-07|Captured Management API split-logic PATCH reference]]
