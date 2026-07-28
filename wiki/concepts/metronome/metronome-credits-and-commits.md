---
title: "Metronome Credits and Commits"
type: concept
category: technology
tags: [metronome, credits, commits, contracts]
---

## Definition

Metronome commitments represent contractually agreed spend and can be prepaid or postpaid. In the enterprise guide, a prepaid commitment separates when balance becomes available from when the customer is invoiced, allowing access and payment schedules to differ.

## Enterprise commitment structure

- Access schedules determine when commitment balance becomes usable.
- Invoice schedules determine when prepaid commitment charges are billed.
- `rollover_fraction` can preserve a defined portion of unused balance when transition logic is applied at renewal.
- Contract rate overrides can scope negotiated discounts to product tags.
- Scheduled charges model separately timed fixed charges; they are not interchangeable with commitment balance.

The guide's example allocates a $500,000 prepaid commitment across three annual access periods, invoices it in two $250,000 installments, and sets a 25% rollover fraction.

## Lifecycle

A contract edit adds terms without starting a new contract. A contract transition starts a new contract, retains its relationship to the original, and can apply transition logic such as rolling over unused commitments or credits.

## Customer-level create API

`POST /v1/contracts/customerCommits/create` creates a balance outside an individual contract for enterprise-wide or multi-contract use. Metronome recommends contract-level commits for standard cases.

- The request requires customer, type, priority, fixed product, and access schedule.
- Postpaid commits require matching access and invoice totals, one item in each schedule, and an invoice contract.
- A prepaid commit can omit invoicing to create a complimentary balance.
- Contract scope can be explicit or cross-contract; product scope can use IDs, tags, or specifiers.
- Lower priority numbers consume first, with contract-level balances winning ties over customer-level balances.
- `uniqueness_key` prevents duplicate creation; its description documents a `409` failure.

## Documentation cautions

The enterprise guide contains two example-level inconsistencies that should be checked against the current API schema before implementation:

- Its create-contract sample uses `product` inside a commit, while the dedicated create-contract API reference documents `product_id`.
- Its upsell prose calls the new $300,000 term a commitment, while the accompanying edit request adds a scheduled charge rather than a commit.
- The customer-commit schema exposes a generic recurring invoice schedule, while its postpaid prose requires one schedule item; confirm this combination before use.

## Sources

- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise commitment design, schedules, rollover, discounts, and lifecycle examples
- [[source-metronome-api-reference-contracts-create-a-contract]] — current create-contract request schema and conditional constraints
- [[source-metronome-api-reference-credits-and-commits-create-a-commit]] — customer-level create endpoint, conditional invoicing, scope, priority, and response boundary

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]
- [[metronome-invoicing]]
