---
title: "Guarantee zero overages"
type: source
date_ingested: 2026-08-31
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages"
original_format: webpage
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages-2026-07-13.md"
tags: [metronome, zero-overages, credits-and-commits, rate-cards, access-control]
---

## Overview

This guide presents a billing-safety pattern for customers who must not incur a nonzero usage charge after a commit is depleted. The merchant gives the product a zero list rate and makes the real usage price applicable only while Metronome is consuming an eligible commit balance; post-exhaustion product access remains a separate merchant-application responsibility.

## Query-critical facts

- The documented actors are the merchant configuring Metronome pricing and commits, Metronome rating submitted usage and producing billing records, and the merchant application deciding whether a customer may continue consuming the product. The named use cases are capped trials, fraud-sensitive accounts, and strict customer budgets.
- The invariant in both worked options is a `0` list rate. While an eligible commit has balance, usage draws down that balance at the real price; after exhaustion, the commit-only price stops applying and the list-rate fallback prices later usage at zero instead of ordinary nonzero overage pricing. This is a configured usage-based-billing pattern, not a universal platform default.
- Option A stores a default `commit_rate` next to the zero list rate on the rate card and creates the commit with `rate_type: commit_rate`. Customers using that rate card inherit the commit price, making the option suitable for mostly uniform pricing.
- Option B leaves only the zero list rate on the rate card and places an `overwrite` rate on each contract, scoped to the relevant commit through `override_specifiers.commit_ids`. It supports customer-specific commit pricing. A contract commit-specific override takes precedence over a default rate-card commit rate when the two patterns are combined.
- The guide distinguishes this no-overage-charge pattern from prepaid-balance auto-recharge and spend-threshold billing, which are alternatives when overages remain allowed but the merchant wants payment or exposure controls.

## Billing and access boundary

The assigned guide's documented outcome is that post-exhaustion usage reaching Metronome resolves at the zero list rate rather than generating a nonzero overage charge. It does not establish that a zero-dollar usage invoice or line item is suppressed, that no billing record is generated, or that any downstream invoice is withheld. The separate [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]] authority says credits or prepaid commitments can reduce a usage invoice to zero and that such an invoice may remain a revenue record without being sent for payment collection; that cross-source invoice fact qualifies possible record handling without extending this assigned pricing guide into invoice suppression, downstream delivery, payment, tax, accounting, or reconciliation authority.

The pattern does not reject submitted usage or enforce the merchant product's authorization decision. The guide expressly requires application-side gating, using balance thresholds or webhooks as signals after depletion. Merchant systems own the access check, cutoff, restoration, and tolerance for usage processed before a signal is evaluated and delivered; this page defines no alert or webhook latency, ordering, freshness, exactly-once delivery, or maximum-overshoot guarantee.

## Material boundaries and documentation cautions

- The result depends on the documented zero list rate, applicable commit, real commit-only rate, product and credit-type relationships, schedule, and contract or rate-card scope all being configured as intended. The page does not define behavior for missing or mismatched rates, several eligible balances, priority, partial exhaustion within a unit or event, concurrent usage near zero, quantity-based drawdown, retroactive changes, precision, rounding, or recovery after a configuration or rating failure. Do not convert the worked setup into a guarantee for every product, contract, event, or access path.
- Both examples use literal prices of `100`, then call the result `100 USD/unit`. The separate [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] authority says USD API monetary values use cents, where `100` represents $1.00. The assigned guide does not reconcile this denomination conflict; preserve its payload and prose literally and verify the intended amount and current API schema rather than silently changing either the number or label. The separate currency source supplies denomination semantics, not a correction to this worked example.
- The cURL examples are implementation illustrations, not complete endpoint contracts. They use casing such as `FLAT` and `flat`, show identifiers and dates tied to one scenario, and omit request/response schemas, validation, errors, concurrency, and recovery behavior. The separate API-wide authority applies `Idempotency-Key` to all POST requests: identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and cached errors require state investigation. This guide adds no endpoint-specific retry or ambiguous-failure guarantee.

## Raw-detail coverage map

Use the raw page for the full use-case rationale; comparison with prepaid-balance and spend thresholds; the Option A rate-card and customer-commit cURL payloads; the Option B rate-card, contract, commit, schedule, temporary-ID, and commit-scoped override payload; all example UUIDs, timestamps, amounts, casing, and inheritance wording; and the closing application-gating note. Use dedicated rate-card, contract, commit, invoice, balance, notification, webhook, currency, and idempotency sources for complete schemas, precedence outside this example, denominations, lifecycle behavior, delivery guarantees, and operational recovery.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]], [[metronome-invoicing]]
- Supporting concepts: [[metronome-customers-and-contracts]], [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]], [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]], [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/guarantee-zero-overages-2026-07-13|2026-07-13 snapshot - zero-list-rate and commit-only pricing patterns, worked configurations, and merchant access-gating boundary]]
