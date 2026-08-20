---
title: "Understand Metronome Prioritization Rules"
type: source
date_ingested: 2026-08-19
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules.md"
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules-2026-07-13.md"
tags: [metronome, credits, commits, prioritization, invoice-line-items]
---

## Overview

This guide defines two related ordering systems in Metronome: which applicable credit or commit balance burns down first, and which eligible invoice line item receives that balance first. Balance type is the outer ordering rule, while priority and increasingly specific applicability and schedule attributes break ties within a type.

## Key takeaways

- Metronome's overall balance order is rollover commits and credits first, then prepaid commits and credits, then postpaid commits. Within the rollover tier, postpaid rollover commits precede prepaid rollover commits and credits.
- Commit type takes precedence over the `priority` field. Priority orders balances only within the same type and cannot move an ordinary postpaid commit ahead of a prepaid balance.
- Rollover balances of the same type are ordered by priority, then narrower product applicability, narrower usage applicability, and earlier `ending_before`.
- Prepaid balances use priority, zero-dollar before paid cost basis, narrower product applicability, narrower usage applicability, earlier end and start times, and finally fewer applicable contracts. The page says postpaid commits follow the same logic, but its abbreviated postpaid list omits usage applicability.
- Eligible invoice lines are ordered independently: usage products before subscription products before composite products, then earlier start date, higher unit price, and finally line-item name from A to Z.

## Balance burn-down order

Metronome first separates balances by type. Rollover balances are consumed before the ordinary prepaid and postpaid tiers; among rollover balances, postpaid rollover commits come before prepaid rollover commits and credits. After rollover, prepaid commits and credits burn down before postpaid commits regardless of their priority values. A priority therefore cannot override the type sequence.

For rollover balances of the same type, the tie-breakers are priority, product applicability, usage applicability, and `ending_before`. Fewer applicable products or usage group-value specifiers consume first, and an earlier end time wins the final documented tie. The guide defines usage applicability here as the number of group value specifiers containing only `presentation_group_value` or `pricing_group_value`; direct `applicable_product_ids` or `applicable_product_tags` do not count as usage applicability.

For prepaid commits and credits, priority is followed by cost basis, with a zero-dollar basis before paid value. Remaining ties use fewer applicable products, fewer applicable usage values, earlier `ending_before`, earlier `starting_on`, and fewer applicable contracts. The worked request illustrates priority by assigning commit A priority `50` and commits B through F priority `100`, then consuming A first; the prose does not separately state a universal numeric-direction rule.

The postpaid section says it follows the same ordering logic as prepaid balances, then abbreviates that sequence as priority, cost basis, product applicability, `ending_before`, `starting_on`, and applicable-contract count. Because that abbreviated list omits usage applicability even though the page says the logic is the same, this source alone does not resolve whether the omission is intentional.

## Invoice line-item prioritization

When more than one invoice line can receive a credit or commit, Metronome applies the balance to usage products before subscription products and then composite products. Ties within a product type go to the earlier line-item start date, then the higher unit price, then alphabetical line-item name. The worked example therefore applies a balance to Data Reads at $2.60 before Data Storage at $1 when both usage lines span the same dates.

## Documentation boundaries

> [!warning] Contradiction
> The existing broad summary that credits and prepaid commits always draw down before postpaid commits needs a rollover exception: this guide explicitly places postpaid rollover commits ahead of prepaid rollover commits and credits. The ordinary non-rollover rule still places prepaid balances before postpaid commits regardless of priority.

The page provides ordering behavior and one contract-creation example, not a complete contract API reference. Its staging request, identifiers, dates, and amounts are illustrative, and it does not document response schemas, validation failures, idempotency, concurrent balance consumption, or atomicity. The postpaid tie-breaker omission above should be verified before relying on usage applicability as a postpaid tie-breaker.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules-2026-07-13|2026-07-13 snapshot - credit, commit, and invoice-line prioritization rules]]
