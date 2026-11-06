---
title: "Adyen Management API: list merchant split configuration profiles"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/2026-11-07.md"
tags: [adyen, management-api, platforms, split-configurations]
---

## Overview

This 2026-11-07 Management API `latest` reference describes `GET /merchants/{merchantId}/splitConfigurations` on the listed TEST `/v3` server. It lists split-configuration profiles for a merchant account. The response describes rules and their split logic; it is a configuration read, not a payment, capture, booking, settlement, or payout result. See [[adyen]] and [[adyen-automatic-split-configuration]].

## Key takeaways

- The required path `merchantId` uniquely identifies the merchant account. No query parameter or request body is listed. The API credential needs `Management API - SplitConfiguration read and write`.
- `200` has optional `data`, described as split configurations applied to stores under the merchant account. Within a returned configuration object, `description` and `rules` are required, while `splitConfigurationId` is optional in the table. Each returned rule requires `currency`, `fundingSource`, `paymentMethod`, `shopperInteraction`, and `splitLogic`; `cardRegion`, `cardUsageType` (default `ANY`), and `ruleId` are optional. The response gives no store ID or per-store association field, so this list alone cannot identify which store uses which profile.
- `204` is processed successfully with no content. Errors documented are `400`, `401`, `403`, `422`, and `500`. The `200` example illustrates nested commission, fee, remainder, tip and balance-account values inside `splitLogic`, but the response table does not define that object's child schema here; example values do not prove actual applied rules or transaction outcomes.

> [!warning] Contradiction
> The response table says rule `currency` must be a three-character ISO currency code (line 36), while the `200` example includes `"currency": "ANY"` (line 189). This snapshot does not resolve whether `ANY` is accepted for that field; do not infer validation from the example.

## Detail locators

- Purpose, role, TEST server and path ID: pinned raw lines 5–21.
- `200` optional parent and nested rule schema, conditions, IDs and status: pinned raw lines 23–42.
- `204` and error response shapes: pinned raw lines 45–146. The illustrative `200` split-logic payload and conflicting `currency` value are at lines 148–238.

## Related

- [[adyen-automatic-split-configuration]] — platform split configuration and booking context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/splitConfigurations/2026-11-07|2026-11-07 pinned merchant split configurations list reference]]