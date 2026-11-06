---
title: "Adyen for Platforms automatic split configuration"
type: concept
category: technology
tags: [adyen, platforms, automatic-splits, balance-accounts]
---

## Definition

Adyen for Platforms can apply split logic automatically to transactions processed through a user's store when a split-configuration profile is linked to that store. The profile contains one or more conditional rules specifying booking to the platform liable balance account and the user's balance account. This configuration route is distinct from supplying transaction-specific split instructions. [[source-adyen-docs-platforms-automatic-split-configuration]]

## Selection and limits

> [!warning] Contradiction
> The 2026-11-07 Management API description-PATCH response schema says `rules[].currency` must be a three-character ISO currency code, while its `200` example uses `ANY`. This response example does not settle accepted or returned currency values; the PATCH request itself changes only the profile description. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid]]


All conditions of a rule must match. When several rules match, the documented priority is currency, payment method or variant, card usage type, card region, funding source, then shopper interaction; specificity breaks ties within a priority. A catch-all ANY rule is recommended because unmatched transactions otherwise default to the platform liable balance account. Payment, capture or refund request split instructions override the automatic split for that request. At capture, Adyen reevaluates the then-current profile and recalculates when the capture amount differs from the authorization. The source labels card usage type and in-person DCC markup allocation as pilots; those features are not generally available to every platform.

## Evidence boundary

These are provider configuration and booking rules in a 2026-09-15 snapshot. They do not prove that a profile is enabled or linked on an account, that a transaction was split, or that capture, settlement or payout completed. They do not establish the legal seller or merchant of record.

## Sources

- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid-rules-ruleid-splitlogic-splitlogicid]] — 2026-11-07-captured Management API v3 TEST PATCH of one merchant split-configuration rule's split logic, including required commission, fee fallback and DCC pilot boundary.

> [!warning] Contradiction
> Its 200 response rule-currency table calls for a three-character ISO currency code (raw line 86), while the 200 example uses `ANY` (raw line 226); the capture does not settle whether `ANY` is accepted as a rule currency. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid-rules-ruleid-splitlogic-splitlogicid]]


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-splitconfigurations-splitconfigurationid-rules-ruleid]] — 2026-11-07-captured Management API v3 Test reference for deleting one merchant split-configuration rule by merchant, configuration and rule IDs, with `200` configuration-shaped or `204` no-content success; no transaction outcome is established.


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-splitconfigurations-splitconfigurationid]] — 2026-11-07-captured Management API v3 TEST reference for deletion of a merchant's split-configuration profile; 200 schema or 204 no-content success.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-splitconfigurations]] — 2026-11-07-captured Management API v3 TEST profile-creation reference for merchant-scoped automatic splits; separate store association is needed, and `200`/`204` is not payment or booking proof.

> [!warning] Contradiction
> The [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-splitconfigurations|2026-11-07 API reference]] requires a three-character ISO code in its `currency` request and response tables but uses `ANY` in both examples. The [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration|2026-09-15 creation guide]] explicitly instructs `ANY` for any currency. These dated sources do not resolve current API acceptance.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid-rules-ruleid]] — 2026-11-07-captured Management API v3 TEST PATCH for one merchant split-configuration rule's conditions; the `200` readback includes the full configuration, while a `204` has no content and neither proves a transaction was split.

> [!warning] Contradiction
> This PATCH reference's request/response currency tables require a three-character ISO code, while its illustrative `200` response includes `"currency": "ANY"`. The sample does not establish that `ANY` is accepted in the request. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid-rules-ruleid]]


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-splitconfigurations-splitconfigurationid]] — 2026-11-07-captured Management API v3 TEST description-only PATCH for a merchant split profile; 200 may return rules but does not edit them through this request.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-splitconfigurations-splitconfigurationid]] — 2026-11-07-captured Management API `latest` v3 TEST read of a merchant split-configuration profile and its rules; profile readback does not prove store association or financial execution.

> [!warning] Contradiction
> This GET response schema requires a three-character ISO `rules[].currency` value, but its illustrative `200` response uses `ANY`. The capture does not settle acceptance or meaning for that value. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-splitconfigurations-splitconfigurationid]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-splitconfigurations]] — 2026-11-07-captured Management API v3 TEST merchant profile list with optional `data`, rule conditions and split logic; it does not expose per-store association IDs or prove a financial outcome.

> [!warning] Contradiction
> The list response table requires a three-character ISO rule `currency`, but its `200` example uses `ANY`; the snapshot does not settle acceptance of that value. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-splitconfigurations]]


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-splitconfigurations-splitconfigurationid]] — 2026-11-07-captured Management API v3 TEST rule creation within a merchant's existing split configuration; condition and split-logic schema, 200/204 response boundary, and an ISO-currency-versus-`ANY` example conflict.

> [!warning] Contradiction
> This create-rule reference's currency tables require a three-character ISO currency code, while its 200 example contains `"currency": "ANY"`. The snapshot does not settle request acceptance of `ANY`. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-splitconfigurations-splitconfigurationid]]


- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-api]] — 2026-09-15 Management API guide to profile/rule retrieval, condition and split-logic edits, description updates, and deletions; records overwrite and capture-time effects.


- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations]] — 2026-09-15 management hub for Customer Area/API profile-rule edits, API-only description/card-region changes and capture-time reevaluation with request override.


- [[source-adyen-docs-platforms-automatic-split-configuration]] — 2026-09-15 automatic-split behavior, hierarchy, request precedence, fallback, rounding, commission and capture-time reevaluation.
- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — 2026-09-15 profile-creation, enablement, rule-field and store-association guide.

- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-customer-area]] — 2026-09-15 Customer Area profile/rule management guide for role-gated edits and deletion, Management API-only fields, at-least-one-rule limit, and capture-time effect on earlier authorizations.

## Related

- [[adyen-platforms]] — parent platform context.
