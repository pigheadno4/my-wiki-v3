---
title: "Metronome: Target Usage with Credits and Commits"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13.md"
tags: [metronome, credits, commits, product-targeting, dimensional-pricing]
---

## Overview

This guide explains how a Metronome credit or commitment can be restricted to a subset of customer usage. Simple product selectors cover product IDs and product families, while `specifiers` support pricing dimensions, presentation dimensions, and compound boolean conditions.

## Key takeaways

- `applicable_product_ids` and `applicable_product_tags` are the simple targeting path; usage matching any listed product ID or tag is eligible to consume the credit or commit.
- A `specifiers` array expresses richer targeting. Fields inside one specifier are ANDed, while separate specifier objects are ORed.
- Specifiers can use pricing-group values, presentation-group values, or product tags. A group-value specifier does not match a product that lacks the corresponding group key.
- Subscriptions and composite products have no pricing or presentation group values, so they cannot draw down a credit or commit whose eligibility depends on such a group-value match.

## Targeting modes

Use `applicable_product_ids` or `applicable_product_tags` when eligibility depends only on product identity or family and does not require compound AND/OR logic. These direct selectors use any-match semantics across the listed IDs and tags.

Use `specifiers` when targeting pricing-group values, presentation-group values, or advanced boolean combinations. Each object in the array is one alternative eligibility branch: every populated field in that object must match, but satisfying any object in the array makes the line item eligible. This is the same boolean model the guide attributes to contract `override_specifiers`.

## Group-value eligibility boundaries

A pricing-group or presentation-group condition only matches usage from products configured with the corresponding group key and value. For example, a `pricing_group_values` condition on `region` excludes products that do not have `region` as a pricing group key. Because subscription and composite products never have pricing or presentation group values, a credit or commit targeted solely through those dimensions does not apply to them.

## Worked examples

- A `POST /v1/contracts/create` example supplies two `pricing_group_values` specifiers, one for `region: us-east-1` and one for `region: us-west-1`, so either region can consume the commitment.
- A `POST /v2/contracts/edit` example adds a prepaid credit restricted to the presentation-group value `user_id: user_123`. The scenario uses a non-pricing presentation dimension to isolate one user's usage.
- A second `POST /v2/contracts/edit` example puts `Audio` and `Basic` in the same specifier's `product_tags` list, illustrating that both tags must match. This lets newly launched products with both tags become eligible without enumerating their IDs.

## Documentation cautions

> [!warning] Contradiction
> The first example's heading and prose say the commitment applies to `us-east-1` and `us-east-2`, but its name and request payload target `us-east-1` and `us-west-1`. Treat the payload as an illustration of OR semantics, not as reliable evidence for which second region was intended.

> [!warning] Contradiction
> The product-tag scenario calls the commitment postpaid, but the request payload sets `type` to `PREPAID`. Verify the intended commitment type before adapting this example.

The page demonstrates request fragments rather than a complete API contract. It does not define selector validation errors, behavior when selectors are empty or omitted, precedence among multiple eligible balances, or mutation semantics for the edit request; use the dedicated API references for those boundaries.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13|2026-07-13 snapshot — targeted credit and commitment eligibility guide]]
