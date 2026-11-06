---
title: "Adyen Management API: Delete a merchant split configuration profile"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configuration]
---

## Overview

Captured Management API v3 reference for deleting the split-configuration profile selected by `splitConfigurationId` under merchant account `merchantId`. This is a profile deletion operation, not a transaction-level split request. See [[adyen]] and [[adyen-automatic-split-configuration]].

## Key takeaways

- Both the merchant account ID and split-configuration ID are required path identifiers. The captured reference lists no query parameters or request body. The API credential must have **Management API - SplitConfiguration read and write**.
- Documented success is `200` with a split-configuration response schema, or `204` without additional content. The `200` schema requires `description` and `rules`, and lists optional `splitConfigurationId`; within each rule, required condition and split-logic fields are documented. These are **response** fields, not deletion request inputs.
- The reference says the specified profile is deleted. It does not state a prerequisite, rollback mechanism, store-association behavior, propagation timing or effect on an individual payment, capture, booking or settlement. Consult the separate automatic-split guidance for transaction behavior.

## Detail locators

- Purpose, permission, TEST server and required path identifiers: raw lines 5–22.
- `200` response schema, including rule conditions and split logic: raw lines 24–60. `204` success: lines 63–64.
- Documented 400, 401, 403, 422 and 500 errors and field schemas: raw lines 67–164.

## Related

- [[adyen-automatic-split-configuration]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07|Management API v3 split-configuration deletion reference]]
