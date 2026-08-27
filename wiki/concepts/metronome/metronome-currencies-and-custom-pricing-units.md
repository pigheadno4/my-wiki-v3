---
title: "Metronome Currencies and Custom Pricing Units"
type: concept
category: technology
tags: [metronome, currencies, custom-pricing-units, rate-cards, credits, commits, invoicing]
---

## Definition

Metronome rate cards use one fiat currency and can price products in that currency or a named custom pricing unit. A custom-unit rate defines a conversion from the rate card's underlying fiat currency, supports balances denominated in the same custom unit, and converts residual unbalanced usage to fiat on an invoice.

## Fiat currencies and API denomination

Metronome exposes `GET /v1/credit-types/list` as a bearer-authenticated, cursor-paginated listing of fiat currency pricing units and configured custom pricing units. A successful JSON object requires `data` and nullable `next_page`; the array-item schema exposes `name`, UUID `id`, and `is_currency`, although those item properties are not marked required. The endpoint identifies `USD (cents)` as `2714e483-4ff1-48e4-9e25-ac732e8f24f2`. This page does not enumerate the complete fiat set or define non-USD denomination, custom-unit precision, conversion, rounding, identifier stability, error responses, ordering, or propagation after configuration changes.

The documented supported set is USD, AUD, BRL, CAD, CHF, CZK, EUR, GBP, INR, MXN, NGN, NOK, PLN, SEK, TRY, ZAR, NZD, and SGD. USD API values use cents, so $1.00 is `100`; every other listed fiat currency uses whole units, so EUR 10.00 is `10`, not `1000`. The API reflects this through `USD (cents)` versus an unqualified code such as `EUR`. Do not apply a universal divide-by-100 rule.

> [!warning] Denomination wording
> The source calls all monetary values the currency's smallest denomination, but then explicitly defines non-USD values as whole currency units. Preserve the concrete Metronome encoding instead of inferring conventional ISO minor-unit scaling for non-USD currencies. The page does not define general precision, integer-only storage, or rounding.

> [!warning] Hierarchy-guide amount contradiction
> The hierarchical-customer guide calls a shared parent commitment $10M while its access and invoice schedules both use `amount: 10000000`; it later labels a parent commit $200K with `amount: 200000` and a child commit $500K with `amount: 500000`. Under the documented USD-cent convention, those payloads represent $100,000, $2,000, and $5,000 rather than the labeled amounts. The payloads do not identify another currency or pricing unit that resolves the mismatches, so verify the intended denomination and amounts before adapting them. This contradiction does not extend to later unlabeled `5000000` and `2000000` examples.

The `listBalances` response models access- and invoice-schedule `amount`, `unit_price`, and `quantity` as numbers. Both schedule schemas make `credit_type` optional; on this page the referenced type requires only UUID `id` and string `name` and does not expose `is_currency`. The example uses `USD (cents)`, but this endpoint independently defines no USD, non-USD, or custom-unit denomination, precision, conversion, or rounding rule. Apply the dedicated currency and custom-unit authorities rather than inferring a universal scale from this response example.

The daily Salesforce sync includes a credit-type object with credit-type ID, name, and Metronome environment; its invoice and invoice-line objects each reference a credit type. The combined commit-or-credit object has no documented credit-type lookup even though its total-amount description uses dollar wording. This Salesforce schema does not establish denomination or USD-cent, non-USD, custom-pricing-unit, conversion, precision, or rounding semantics for those replicas.


## Rate-card setup and immutability

Custom units are created and named in the Metronome app for invoice presentation. A rate card selects one fiat currency, and each product rate uses either that fiat currency or a custom pricing unit with a conversion from the underlying fiat currency. Once a product's rate is saved in one pricing unit, that rate's pricing unit cannot be changed. The source does not define the required replacement or migration path or its effects on contracts and invoices.

## Credits, commits, and invoice conversion

Customer- or contract-level credits and prepaid commits can have access schedules in custom units or selected currencies. Usage priced in a custom unit first burns down applicable balances with schedules in that same unit. If none remains, Metronome adds a conversion line item and calculates the residual cost in the rate card's fiat currency. A CHF-paid commit granting Cloud Compute Tokens illustrates that payment currency and access unit can differ; it does not prove arbitrary cross-currency balance conversion.

For customer-credit creation, `access_schedule.credit_type_id` is optional and defaults to USD cents. Every schedule item requires numeric `amount`, but the endpoint schema supplies no integer, positivity, zero, precision, maximum, or rounding constraint and no non-USD denomination rule. The schedule array is required without `minItems`; its items require inclusive RFC 3339 start and exclusive end, while ordering, overlap, chronology, gaps, and time-zone behavior beyond RFC 3339 remain unspecified.


The invoice-read schema exposes `cpu_conversion` as a distinct line-item type when products are priced in a custom pricing unit and matching prepaid commit or credit is insufficient to cover the spend. Its description says outstanding custom-unit spend is converted to fiat using the rate-card conversion. This read surface does not define conversion direction, precision, rounding, rate snapshot, tax treatment, or whether the line alone is sufficient to reproduce the calculation.


### AWS Marketplace currency boundary

The AWS Marketplace integration accepts only invoices in USD fiat currency and expresses each metering-record quantity as the accrued dollar amount in USD cents. Metronome errors when a contract selects AWS while its rate card uses non-USD fiat; when a contract has additional non-USD invoices, only its USD invoices are sent to AWS. The guide does not define conversion, mixed-currency aggregation, tax, or rounding beyond the stated USD-cent quantity. [[source-metronome-integrations-marketplace-integrations-aws]]

### Azure Marketplace currency boundary

Azure Marketplace delivery supports only USD-fiat invoices and encodes metering quantity in USD cents. Selecting Azure with a non-USD rate card causes contract creation to error; if other invoices associated with the contract are non-USD, only USD invoices are sent. The guide does not define conversion, mixed-currency reconciliation, precision, rounding, or tax. [[source-metronome-integrations-marketplace-integrations-azure]]

### GCP Marketplace currency boundary

GCP Marketplace delivery supports only USD-fiat invoices and encodes metering quantity in USD cents. Selecting GCP with a non-USD rate card causes contract creation to error; if other invoices associated with the contract are non-USD, only USD invoices are sent. The guide does not define conversion, mixed-currency reconciliation, precision, rounding, or tax. [[source-metronome-integrations-marketplace-integrations-gcp]]

## Boundaries and unknowns

The guide does not define custom-unit creation APIs, precision, conversion formula direction, rounding, exchange-rate sourcing or timing, rate-card currency mutation, mixed-rate resolution, balance priority, tax, invoice lifecycle, collection, refund, or revaluation behavior. Its supported-currency list and denomination behavior are dated documentation evidence, not an evergreen capability guarantee.

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-credits-and-commits]]
- [[metronome-invoicing]]

## Sources

- [[source-metronome-api-reference-settings-list-pricing-units]] — bearer-authenticated pricing-unit enumeration, USD (cents) identifier, cursor pagination, and successful response schema

- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — $10M, $200K, and $500K hierarchy commitment labels whose paired numeric amounts conflict with the USD-cent convention

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — supported currencies, Metronome-specific denomination, rate-card custom units, matching-balance drawdown, and residual fiat conversion

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - access-schedule credit-type default, numeric amount schema, inclusive and exclusive time bounds, and denomination constraints left open

- [[source-metronome-api-reference-credits-and-commits-list-balances]] - optional schedule credit-type references, numeric amount fields, USD-cents example, and endpoint-level denomination and precision boundaries

- [[source-metronome-api-reference-invoices-get-an-invoice]] - `cpu_conversion` invoice-line representation, insufficient matching-balance trigger, and calculation boundaries

- [[source-metronome-integrations-marketplace-integrations-aws]] — AWS Marketplace USD-only contract and invoice-delivery boundary plus USD-cent metering quantity

- [[source-metronome-integrations-platform-integrations-sfdc-integration]] - Salesforce credit-type, invoice, and invoice-line references plus the commit-or-credit denomination and missing-lookup boundary
