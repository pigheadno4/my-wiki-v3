---
title: "Adyen Management API: update split configuration description"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configurations]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}` on the v3 test server. It changes the **description** of a specified split configuration profile under a merchant account. The request body contains required `description`; this endpoint does not describe a rule or split-logic update. See [[adyen-automatic-split-configuration]].

## Key takeaways

- Required path `merchantId` identifies the merchant account, and `splitConfigurationId` identifies the profile. The API credential needs `Management API - SplitConfiguration read and write`.
- `200` says the request succeeded and returns required `description` and `rules`; optional `splitConfigurationId` may appear. The returned rules describe configuration behavior, including conditional fields and split logic, but they are response fields here, not writable request fields. `204` says processing succeeded without additional content.
- A profile-description response does not establish store linkage, which rule matched a transaction, payment authorization, capture, booking, settlement, or payout. This reference states no idempotency key, version check, or propagation time.

> [!warning] Contradiction
> In the `200` response schema, `rules[].currency` is described as a three-character ISO currency code, but the `200` example includes `"currency": "ANY"`. The example does not settle the accepted or returned currency-value contract. The request here edits only `description`.

## Detail locators

- `## Parameters` → path parameters and request body: two required identifiers and required description.
- `## Request examples` → `patch-splitConfiguration-description`: illustrative description payload.
- `## Responses` → `200 Success`: profile readback with rules and split logic; inspect the raw table for required versus optional fields, conditions, pilot DCC, and fee-allocation descriptions.
- `## Responses` → `204 Success` and `400`, `401`, `403`, `422`, `500` error tables.
- `## Response examples` → `200 Success`: illustrative profile with two rules; its `ANY` currency values conflict with the response field description above.

## Related

- [[adyen]]
- [[adyen-automatic-split-configuration]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/2026-11-07|Management API split-configuration description PATCH, captured 2026-11-07]]
