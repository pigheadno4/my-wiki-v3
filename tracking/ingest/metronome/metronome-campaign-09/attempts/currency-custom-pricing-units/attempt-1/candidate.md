---
title: "Metronome Set Currencies and Custom Pricing Units"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits"
raw_files:
  - "metronome/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits-2026-07-13.md"
tags: [metronome, currencies, custom-pricing-units, rate-cards, credits, commits, invoicing]
---

## Overview

This guide documents the currency representation and custom-pricing-unit workflow for Metronome rate cards, credits, prepaid commits, and invoices. Its central integration boundary is Metronome-specific: USD values use cents, while every other fiat currency listed by this page uses whole currency units; custom-unit rates draw down matching balances first and otherwise convert to the rate card's fiat currency.

## Key takeaways

- The page lists 18 supported fiat currencies: USD, AUD, BRL, CAD, CHF, CZK, EUR, GBP, INR, MXN, NGN, NOK, PLN, SEK, TRY, ZAR, NZD, and SGD. This page is a dated documentation snapshot, not a guarantee that the list is exhaustive or unchanged.
- USD is encoded in cents, so $1.00 is `100`. All other supported fiat currencies are encoded in whole units; for example, EUR 10.00 is `10`, not `1000`. An integration must not apply a universal divide-by-100 rule.
- One rate card is associated with one fiat currency. Its product rates can use that fiat currency or a custom pricing unit; a custom-unit rate requires a conversion rate from the underlying fiat currency.
- After a product's rate is saved in one pricing unit, the guide says that rate's pricing unit cannot be changed. It does not describe a migration path, so replacement or effective-dated behavior must be verified elsewhere.
- Custom-unit usage first burns down credits and prepaid commits whose access schedules use that same custom unit. If no applicable matching balance remains, Metronome adds a conversion line item and calculates the cost in the rate card's fiat currency.

## Currency denomination and API scaling

The page says API monetary fields such as `total`, `unit_price`, `amount`, and `threshold` use the currency denomination represented by the pricing unit returned from the API. USD is labeled `USD (cents)` and uses cents. Other listed currencies return their normal code, such as `EUR`, and use whole currency units.

> [!warning] Metronome-specific scaling
> Do not generalize Stripe-style or ISO-minor-unit scaling to these Metronome values. On this page, USD uses cents, but every other supported fiat currency uses whole units, even currencies that ordinarily have fractional minor denominations. Preserve decimal values where the relevant API schema permits them; this guide does not establish integer-only storage or a general rounding rule.

> [!warning] Documentation terminology tension
> The guide first calls all API monetary values the currency's "smallest denomination (minor unit)," then explicitly says every supported non-USD fiat currency uses whole units. Treat the concrete Metronome examples and returned pricing-unit labels as the documented encoding rule, not the opening phrase as evidence that non-USD values follow conventional ISO minor-unit scaling.

## Custom pricing-unit setup and immutability

Custom pricing units are created in the Metronome app under **Offering → Pricing units → Custom pricing units** and named for invoice presentation. The rate card then selects one fiat currency, assigns a product rate either that fiat currency or a custom unit, and defines a conversion from the underlying fiat currency for a custom-unit rate.

The page states that once a rate is saved in one pricing unit for a product, that rate's unit cannot be changed. It does not define whether a new rate, product, or rate card is required; whether future-effective replacement is supported; or how existing contracts, balances, draft invoices, or finalized invoices behave during such a change.

## Credits, commits, and invoice conversion

Contract-level and customer-level credits or prepaid commits can carry access schedules in custom pricing units or selected currencies. The example separates payment denomination from access value: a prepaid commit paid in CHF can grant 100 Cloud Compute Tokens. This does not establish a general foreign-exchange engine, automatic currency conversion between arbitrary balances, or multi-currency aggregation.

Usage priced in a custom unit consumes applicable credits and prepaid commits whose access schedules use that custom unit. When no applicable matching balance exists, a conversion line item calculates the residual cost in the fiat currency configured on the rate card. In the invoice example, the remaining 350 Cloud Compute Tokens are converted after prepaid commits are exhausted, and the resulting fiat amount becomes the total due. The page does not define conversion formula direction, decimal precision, rounding, exchange-rate sourcing or timing, taxes, line-item schema, or invoice lifecycle and payment status.

## Documentation boundaries and unknowns

This guide does not document an API for creating custom pricing units, the pricing-unit list schema, custom-unit precision or uniqueness, conversion-rate validation, rounding, currency-change behavior, mixed-rate resolution, rate-card migration, credit/commit priority, balance applicability beyond unit matching, invoice finalization, collection, refunds, tax, or foreign-exchange revaluation. Its 18-currency table and USD-versus-whole-unit rule should be treated as source-specific dated evidence and checked against current API references before implementation.

No contradiction was found with the existing Metronome wiki: current rate-card, customer-control, and prepaid-commit pages already preserve USD cents and non-USD whole-unit behavior. The terminology tension within this source remains explicit because "smallest denomination" and "whole currency units" should not be collapsed into a universal minor-unit rule.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits-2026-07-13|2026-07-13 snapshot — supported currencies, API denomination, custom-unit setup, balance drawdown, and invoice conversion]]
