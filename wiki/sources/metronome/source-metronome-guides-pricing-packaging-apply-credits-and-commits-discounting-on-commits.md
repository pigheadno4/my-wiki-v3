---
title: "Offer discounts on commits"
type: source
date_ingested: 2026-09-08
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits-2026-07-13.md"
tags: [metronome, credits-and-commits, discounts, rate-cards, contract-overrides]
---

## Overview

This guide helps choose among three ways to discount committed usage in Metronome: reducing a prepaid commit's cost basis, applying commit-specific contract overrides, or defining commit rates on a rate card. It distinguishes the scope and limitations of each approach and provides worked API examples for locating their configuration details.

## Key takeaways

- Reducing cost basis separates accessible committed spend from the amount invoiced. The guide limits this approach to prepaid commits with a uniform percentage discount and notes that the discount is not visible in usage-statement prices.
- Commit-specific multiplier, overwrite, or tiered overrides can apply while consuming all commits and credits or selected balances. Commit-specific overwrites rank ahead of commit-specific multipliers, followed by the corresponding non-commit-specific override classes.
- Rate-card commit rates support reusable committed-usage pricing across customers. The guide limits them to usage products, requires a list rate in the same pricing unit, and permits tiered list and commit rates without resetting tier quantity when switching between them.

> [!warning] Commit-rate fallback
> If a commit or credit is configured to use a commit rate but a product has no commit rate, Metronome applies the product's list rate and list-rate-targeting overrides; commit-rate-targeting overrides are ignored.

## Raw-detail guide

- `## Reduce the commit cost basis` contains the narrated $10,000-access/$8,000-invoice example, its `POST /v1/contracts/customerCommits/create` payload, and the method's usage-statement, uniform-discount, and prepaid-only limitations.
- `## Create commit-specific overrides` contains override types, selectors, priority order, and worked contract-create and contract-edit examples for a selected commit or any consumed commit or credit.
- `## Encoding commit rates on the rate card` contains rate-card setup constraints, fallback behavior, optional contract-level discounting of a commit rate, and the worked add-rate, commit-create, and contract-edit payloads. Treat those examples as navigation to the captured evidence rather than complete endpoint schemas.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]
- Supporting concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits-2026-07-13|2026-07-13 snapshot - commit discount methods, selection limits, fallback behavior, and worked examples]]
