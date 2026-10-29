---
title: "Manage split configuration profiles through the Management API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api"
raw_files:
  - "adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/api/2026-09-15.md"
tags: [adyen, platforms, automatic-splits, management-api]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes Management API operations for viewing, editing, and deleting merchant-account split configuration profiles. A profile has a `splitConfigurationId`, contains rules identified by `ruleId`, and each rule's instructions can be addressed by `splitLogicId`. The page covers list/get, adding and removing rules, editing rule conditions or split logic, changing a profile description, and deleting a profile. [[adyen]] [[adyen-automatic-split-configuration]]

## Key takeaways

- The guide requires an Adyen for Platforms platform-model integration, a Management API credential with **Management API—SplitConfiguration read and write**, and the relevant profile, rule, or split-logic IDs for updates. Its card-region condition is a pilot, not available to every platform. See raw lines 26–35.
- Profile list and detail retrieval use `GET /merchants/{merchantId}/splitConfigurations` and `GET /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}`. Adding a rule uses `POST` on the profile path; the response returns the updated profile and the new `ruleId`. See raw lines 37–39, 292–294, 509–540, 2642–2710.
- A rule selects by currency, payment method, card usage type, card region, funding source, and shopper interaction; its split logic addresses commission and, where configured, fee booking, refund/chargeback allocation, remainder, in-person DCC markup, tips, and surcharges. The fee types have mutually exclusive groupings; `refundCostAllocation` requires `refund`, and `chargebackCostAllocation` requires `chargeback`. A store with multiple partial captures must not use `deductAccordingToSplitRatio` for refund logic. DCC allocation is an in-person pilot; surcharges are limited to Australia/New Zealand, with pilots elsewhere. See raw lines 515–575, 966–977, 1776–1788, 1853–1862.
- Condition updates use `PATCH /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}`. Send all conditions: omitted conditions reset to defaults. Split-logic updates use `PATCH` on that rule's `/splitLogic/{splitLogicId}`; send all existing instructions because undefined split types book to the platform liable balance account. These changes and added rules affect transactions authorized before the update but captured afterward because the profile is re-evaluated at capture. See raw lines 2712–2722, 2749, 2980–3013.
- The profile description has its own `PATCH` operation. A profile must retain at least one rule, so the only rule cannot be deleted; deleting the whole profile is a separate `DELETE` operation. See raw lines 3275–3279, 3515–3519, 3665–3669.

> [!warning] Source example inconsistencies
> The fee table names the API field `acquiringFees` but spells it `aquiringFees` in prose/list entries (raw lines 563–575). The add-rule curl request includes `cardUsageType: commercial`, `cardRegion: domestic`, `dcc`, and `remainder: addToLiableAccount`; several SDK examples omit these and the response's first rule says `cardUsageType: consumer` (raw lines 2257–2287, 2313–2639, 2646–2709). The condition-update curl request uses USD/card fields while several SDK examples use EUR and omit card fields (raw lines 2755–2769, 2842–2893). The split-logic update prose says all existing instructions must be sent, yet the curl includes `dcc` and the JavaScript/Python examples omit it; its response also retains a `variablePercentage` omitted from the request (raw lines 3011–3040, 3113–3183, 3230–3273). Treat these examples as illustrative, not equivalent payloads or proof of exact update behavior.

## Detail locators

- List and profile-detail endpoints, with test-environment examples and responses: raw lines 37–507.
- Add-rule required-field table, optional split instructions, fee groupings, and create-profile illustrations: raw lines 509–2250. The DCC illustration omits `commission` although the add-rule field table marks `splitLogic.commission` required; compare raw lines 539–540 with 1795–1849.
- Add-rule request and returned IDs/profile: raw lines 2251–2714.
- Condition, split-logic, and description PATCH requests/responses: raw lines 2716–3513.
- Rule and profile deletion endpoints/examples: raw lines 3515–3854.

## Related

- [[adyen-automatic-split-configuration]] — automatic split selection and capture-time behavior.
- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations]] — management overview.
- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — creation and store association.

## Raw Sources

- [[raw/adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/api/2026-09-15|Full pinned Management API guide]]
