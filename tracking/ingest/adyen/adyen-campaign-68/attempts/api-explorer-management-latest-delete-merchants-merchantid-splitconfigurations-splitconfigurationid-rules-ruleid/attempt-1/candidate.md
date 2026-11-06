---
title: "Delete one merchant split-configuration rule (Adyen Management API)"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configuration, split-rule]
---

## Overview

This captured Management API `latest` reference documents `DELETE /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}`. It deletes the specified rule within the identified split configuration for the identified merchant account. The listed server is Test `/v3`, and the API credential needs `Management API - SplitConfiguration read and write`.

## Key takeaways

- All three path values are required: the merchant-account ID, unique split-configuration ID, and rule ID. The reference documents no request body, query parameters, idempotency key, or conditional input for this operation. It does not say that the split configuration itself is deleted.
- `200` success has a split-configuration response schema with required `description` and `rules` array; individual rules have condition fields and `splitLogic`. The parent `splitConfigurationId` and nested `ruleId` are response-optional. `204` success has no additional content. Consult the raw for condition values, nested required fields, fee-allocation choices and defaults; these response fields are not new DELETE inputs.
- Removing a configuration rule is distinct from a transaction-specific split, payment, capture, refund, booking, settlement or payout. The response cannot establish which rule a later transaction will match or any financial outcome. The reference lists `400`, `401`, `403`, `422` and `500` errors.

## Detail locators

- Raw lines 5–23: operation purpose, role, Test server and required merchant/configuration/rule path values.
- Raw lines 25–61: `200` split-configuration response fields, rule conditions and split-logic locators. The `dcc` field is marked pilot and unavailable to some platforms (line 51); fee-allocation default text is at line 53.
- Raw lines 64–165: `204` no-content success and documented error responses.

## Related

- [[adyen]]
- [[adyen-automatic-split-configuration]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07|DELETE merchant split-configuration rule, 2026-11-07 capture]]
