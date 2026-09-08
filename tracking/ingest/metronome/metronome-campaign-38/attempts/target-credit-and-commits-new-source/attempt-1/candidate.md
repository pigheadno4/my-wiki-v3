---
title: "Metronome: Target usage with credits and commits"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits"
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13.md"
tags: [metronome, credits, commits, usage-targeting]
---

## Overview

This guide explains how to restrict a Metronome credit or commit to selected customer usage. It distinguishes simple product-based selectors from `specifiers`, which support pricing or presentation dimensions and more complex boolean matching.

## Key takeaways

- Use `applicable_product_ids` or `applicable_product_tags` when filtering only by product ID or product family without complex AND/OR logic. Usage matching any listed product ID or tag is eligible to consume the credit or commit.
- Use `specifiers` for pricing-group values, presentation-group values, or advanced boolean logic. Fields within one specifier are ANDed; separate specifier objects are ORed because a line item is eligible when any specifier matches.
- When a specifier tests pricing or presentation group values, a product without the corresponding group key cannot match. Subscriptions and composite products do not have those group values and therefore do not draw down the credit or commit under such a specifier.

## Raw-detail navigation

- Selector choice and direct product-selector matching: see `Target with applicable_product_ids and applicable_product_tags` (raw lines 13-22).
- Specifier structure, boolean matching, and the missing-group-key boundary: see `Target with specifiers` (raw lines 24-30).
- Worked contract-create and contract-edit payloads for pricing-group, presentation-group, and product-tag examples remain in the raw under the three `Example` headings (raw lines 32-176); consult the current dedicated API references before treating those example payloads as complete request contracts.

## Related

- Company: [[metronome]]
- Concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13|Target usage with credits and commits]] — complete collected guide with matching rules and worked payloads
