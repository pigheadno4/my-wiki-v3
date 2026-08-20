---
title: "Metronome Currencies and Custom Pricing Units"
type: concept
category: technology
tags: [metronome, currencies, custom-pricing-units, rate-cards, credits, commits, invoicing]
---

## Definition

Metronome rate cards use one fiat currency and can price products in that currency or a named custom pricing unit. A custom-unit rate defines a conversion from the rate card's underlying fiat currency, supports balances denominated in the same custom unit, and converts residual unbalanced usage to fiat on an invoice.

## Fiat currencies and API denomination

The documented supported set is USD, AUD, BRL, CAD, CHF, CZK, EUR, GBP, INR, MXN, NGN, NOK, PLN, SEK, TRY, ZAR, NZD, and SGD. USD API values use cents, so $1.00 is `100`; every other listed fiat currency uses whole units, so EUR 10.00 is `10`, not `1000`. The API reflects this through `USD (cents)` versus an unqualified code such as `EUR`. Do not apply a universal divide-by-100 rule.

> [!warning] Denomination wording
> The source calls all monetary values the currency's smallest denomination, but then explicitly defines non-USD values as whole currency units. Preserve the concrete Metronome encoding instead of inferring conventional ISO minor-unit scaling for non-USD currencies. The page does not define general precision, integer-only storage, or rounding.

> [!warning] Hierarchy-guide amount contradiction
> The hierarchical-customer guide calls a shared parent commitment $10M while its access and invoice schedules both use `amount: 10000000`; it later labels a parent commit $200K with `amount: 200000` and a child commit $500K with `amount: 500000`. Under the documented USD-cent convention, those payloads represent $100,000, $2,000, and $5,000 rather than the labeled amounts. The payloads do not identify another currency or pricing unit that resolves the mismatches, so verify the intended denomination and amounts before adapting them. This contradiction does not extend to later unlabeled `5000000` and `2000000` examples.

## Rate-card setup and immutability

Custom units are created and named in the Metronome app for invoice presentation. A rate card selects one fiat currency, and each product rate uses either that fiat currency or a custom pricing unit with a conversion from the underlying fiat currency. Once a product's rate is saved in one pricing unit, that rate's pricing unit cannot be changed. The source does not define the required replacement or migration path or its effects on contracts and invoices.

## Credits, commits, and invoice conversion

Customer- or contract-level credits and prepaid commits can have access schedules in custom units or selected currencies. Usage priced in a custom unit first burns down applicable balances with schedules in that same unit. If none remains, Metronome adds a conversion line item and calculates the residual cost in the rate card's fiat currency. A CHF-paid commit granting Cloud Compute Tokens illustrates that payment currency and access unit can differ; it does not prove arbitrary cross-currency balance conversion.

## Boundaries and unknowns

The guide does not define custom-unit creation APIs, precision, conversion formula direction, rounding, exchange-rate sourcing or timing, rate-card currency mutation, mixed-rate resolution, balance priority, tax, invoice lifecycle, collection, refund, or revaluation behavior. Its supported-currency list and denomination behavior are dated documentation evidence, not an evergreen capability guarantee.

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-credits-and-commits]]
- [[metronome-invoicing]]

## Sources

- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — $10M, $200K, and $500K hierarchy commitment labels whose paired numeric amounts conflict with the USD-cent convention

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — supported currencies, Metronome-specific denomination, rate-card custom units, matching-balance drawdown, and residual fiat conversion
