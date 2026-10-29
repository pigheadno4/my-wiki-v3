---
title: "Adyen for Platforms automatic split configuration"
type: concept
category: technology
tags: [adyen, platforms, automatic-splits, balance-accounts]
---

## Definition

Adyen for Platforms can apply split logic automatically to transactions processed through a user's store when a split-configuration profile is linked to that store. The profile contains one or more conditional rules specifying booking to the platform liable balance account and the user's balance account. This configuration route is distinct from supplying transaction-specific split instructions. [[source-adyen-docs-platforms-automatic-split-configuration]]

## Selection and limits

All conditions of a rule must match. When several rules match, the documented priority is currency, payment method or variant, card usage type, card region, funding source, then shopper interaction; specificity breaks ties within a priority. A catch-all ANY rule is recommended because unmatched transactions otherwise default to the platform liable balance account. Payment, capture or refund request split instructions override the automatic split for that request. At capture, Adyen reevaluates the then-current profile and recalculates when the capture amount differs from the authorization. The source labels card usage type and in-person DCC markup allocation as pilots; those features are not generally available to every platform.

## Evidence boundary

These are provider configuration and booking rules in a 2026-09-15 snapshot. They do not prove that a profile is enabled or linked on an account, that a transaction was split, or that capture, settlement or payout completed. They do not establish the legal seller or merchant of record.

## Sources

- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-api]] — 2026-09-15 Management API guide to profile/rule retrieval, condition and split-logic edits, description updates, and deletions; records overwrite and capture-time effects.


- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations]] — 2026-09-15 management hub for Customer Area/API profile-rule edits, API-only description/card-region changes and capture-time reevaluation with request override.


- [[source-adyen-docs-platforms-automatic-split-configuration]] — 2026-09-15 automatic-split behavior, hierarchy, request precedence, fallback, rounding, commission and capture-time reevaluation.
- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — 2026-09-15 profile-creation, enablement, rule-field and store-association guide.

- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-customer-area]] — 2026-09-15 Customer Area profile/rule management guide for role-gated edits and deletion, Management API-only fields, at-least-one-rule limit, and capture-time effect on earlier authorizations.

## Related

- [[adyen-platforms]] — parent platform context.
