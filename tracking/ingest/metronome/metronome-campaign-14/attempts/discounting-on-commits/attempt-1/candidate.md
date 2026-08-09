---
title: "Offer discounts on commits"
type: source
date_ingested: 2026-08-05
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits.md"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits-2026-07-13.md"
tags: [metronome, commits, discounts, pricing-overrides, rate-cards]
---

## Overview

This guide describes three ways to discount usage associated with commits in Metronome: bill less than the accessible prepaid value, apply commit-specific contract overrides, or define reusable commit rates on a rate card. The methods serve different pricing structures and have distinct visibility, applicability, precedence, and fallback behavior.

## Key takeaways

- Reducing a commit's cost basis grants more accessible prepaid value than the amount invoiced. The guide limits this approach to prepaid commits with a uniform percentage discount and says the discount is not reflected in usage-statement prices.
- Commit-specific multiplier, overwrite, or tiered overrides can target usage funded by all commits and credits or by selected balances. Product IDs, product tags, pricing group keys, and presentation group keys can scope affected line items.
- The documented precedence places commit-specific overwrite overrides first, followed by commit-specific multipliers, contract-level overwrites, and contract-level multipliers. Specificity by number of associated commits does not itself determine priority.
- A rate-card commit rate provides reusable pricing for customers who consume commitments, while a commit-specific override can further discount that rate for an individual contract or selected commits.
- Commit rates apply only to usage products, must be added alongside a list rate in the same pricing unit, and may be tiered without resetting tier quantity when consumption moves between commit and list rates.
- If a commit or credit is configured to use a commit rate but a product has no such rate, Metronome falls back to the product's list rate and list-rate-targeting overrides; commit-rate-targeting overrides are ignored.

## Cost-basis discounts

A cost-basis discount separates the accessible amount from the invoiced amount. The worked commercial description grants $10,000 of prepaid spend while billing $8,000, representing a 20% discount. This does not change the prices displayed on usage statements, and the guide says it is unsuitable for postpaid commits because their invoice and access schedule amounts must match.

This method is also bounded to a uniform percentage reduction. Distinct rates relative to list price or different discounts by product require commit-specific overrides instead.

## Commit-specific overrides

Commit-specific overrides adjust rates while qualifying usage burns down prepaid commits, postpaid commits, or credits. They can apply whenever any such balance is consumed or be limited to identified commit, recurring-commit, credit, or recurring-credit objects. The guide documents multiplier, overwrite, and tiered forms, with product and grouping selectors available for line-item scope.

The precedence sequence is commit-specific overwrite, commit-specific multiplier, contract-level overwrite, then contract-level multiplier. Multipliers within their respective levels follow the contract's configured prioritization scheme. An override that targets one commit is not automatically preferred over an otherwise comparable override that targets all commits merely because its balance scope is narrower.

The continued-discount example combines a 0.95 contract-level multiplier for on-demand audio usage with a 0.8 commit-specific multiplier while commit A is being consumed. A second example uses product-level overwrite rates whenever any commit or credit is consumed and returns to list rates after all qualifying balances are exhausted. These prices, identifiers, and dates are illustrative rather than general platform defaults.

## Rate-card commit rates

Rate-card commit rates centralize a standard committed-usage price so it need not be recreated as a contract override for every customer. They are supported only for usage products and must be created with a list rate in the same pricing unit. Both rates can be tiered, and the guide says tier quantity continues across commit-rate and list-rate consumption rather than resetting at the boundary.

A commit or credit should select commit-rate behavior only when distinct commit rates have been configured. When a product lacks a commit rate, Metronome uses its list rate plus applicable list-rate overrides and ignores commit-rate overrides. A contract may further negotiate the shared commit rate through a commit-specific override targeting `commit_rate`; omitting commit IDs makes that override apply whenever a prepaid or postpaid commit is used.

## Documentation cautions

> [!warning] Example amount mismatch
> The cost-basis prose and request introduction describe $10,000 of accessible prepaid value billed for $8,000, but the displayed USD-style request uses `amount: 100000` and `unit_price: 80000`. Under the wiki's existing Metronome USD-cent evidence, those values represent $1,000 and $800. Preserve the intended 20% pattern, but verify the example's missing order of magnitude before implementation.

The targeting prose names `any_commit_or_credit_ids`, while the displayed contract examples use `override_specifiers.commit_ids`; this page does not reconcile those request shapes. It also describes a `COMMIT_RATE` target in prose while payloads use `commit_rate`. Confirm the current endpoint schema rather than treating these spellings or placements as interchangeable. The negotiated-rate table has an unlabeled fifth column and rows whose product labels and prices do not align cleanly with its four named headers, so its numeric mapping should not be relied on without clarification.

The guide does not define validation errors, effective-date overlap behavior, retroactive recalculation, finalized-invoice handling, rounding, concurrent edits, or behavior when multiple tiered commit-specific overrides qualify. No contradiction with existing Metronome concept pages was found when the new precedence and fallback rules remain scoped to this guide; the internal example inconsistencies above still require explicit caution.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- API boundaries: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-credits-and-commits-create-a-commit]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits-2026-07-13|2026-07-13 snapshot — cost-basis discounts, commit-specific overrides, and rate-card commit rates]]
