---
title: "Adyen Management API: Update split rule conditions"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07.md"
tags: [adyen, management-api, platforms, automatic-split, split-configuration]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}` on the listed TEST `https://management-test.adyen.com/v3` server. It changes the conditions of one rule in a merchant-account split configuration. The required path IDs identify the merchant account, split configuration and rule separately. See [[adyen]] and [[adyen-automatic-split-configuration]].

## Key takeaways

- The API credential requires Management API - SplitConfiguration read and write.
- The request table marks `currency`, `fundingSource`, `paymentMethod` and `shopperInteraction` required; optional `cardUsageType` defaults to `ANY`. These are rule conditions. The documented request does not include `splitLogic`, so this endpoint's condition update should not be mistaken for an edit of booking instructions.
- A `200` returns a split-configuration representation with required `description` and `rules`, and optional `splitConfigurationId`; nested rule responses include conditions and `splitLogic`. A `204` has no additional content. Success is configuration response evidence, not proof that a store uses the profile or that a payment was split, captured, settled or paid out.
- The response schema describes a DCC split-logic field as pilot-only. It also says that when no transaction fee type is included in `splitLogic`, Adyen updates the payment request with `paymentFee` to book all transaction fees to the platform's liable balance account. Those response descriptions are not additional request fields for this PATCH.

> [!warning] Contradiction
> The request and response tables describe `currency` as a three-character ISO currency code, but the illustrative `200` response includes a rule with `"currency": "ANY"`. The capture does not establish whether `ANY` is accepted as a request value for this endpoint.

## Detail locators

- Purpose, role, TEST server, three required path IDs and request conditions: raw lines 5–33. Illustrative request: lines 35–45.
- `200` configuration response, rule and split-logic fields, including DCC pilot and fee fallback descriptions: raw lines 46–82. `204` and error definitions: lines 85–186. Illustrative `200` response: lines 188–246.

## Related

- [[adyen-automatic-split-configuration]] — profile selection and booking context.
- [[adyen-platforms]] — platform account context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/splitConfigurations/(splitConfigurationId)/rules/(ruleId)/2026-11-07|Pinned split rule condition PATCH reference (2026-11-07)]]
