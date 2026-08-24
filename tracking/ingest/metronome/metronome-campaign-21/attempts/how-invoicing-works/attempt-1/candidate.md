---
title: "How Metronome Invoices Work"
type: source
date_ingested: 2026-08-24
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/how-invoicing-works.md"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/how-invoicing-works-2026-07-13.md"
tags: [metronome, invoicing, usage-invoices, scheduled-invoices, invoice-lifecycle, invoice-presentation]
---

## Overview

This guide is Metronome's conceptual authority for its native invoice types, contract-driven generation, lifecycle states, line-item model, and presentation controls. It is useful for deciding whether an invoice is usage-based or scheduled and how draft, grace-period, finalized, and void states relate; exact API payloads, billing-provider delivery, payment collection, tax, and accounting outcomes require the dedicated references.

## Key takeaways

- Contracts are the primary invoice-generation mechanism. Metronome distinguishes usage invoices from scheduled invoices and creates them on contract-defined schedules.
- Usage invoices track entitlements and consumption for a billing period, update while usage arrives, can absorb effective-dated product, rate, credit, or commitment changes, and enter a configurable grace period before finalization.
- Scheduled invoices cover fixed charges such as commitment prepayments, postpaid true-ups, and upfront or recurring fees. They have no usage grace period or billing-period start and end fields, and their finalization timing depends on issue date relative to contract creation.
- Finalized invoices are immutable within Metronome. A finalized invoice created in error can be voided and regenerated from updated usage and pricing, but this guide does not define the regeneration API contract or prove downstream cancellation, delivery, collection, payment, tax, or accounting outcomes.
- Pricing group keys split usage into separately priced line items, while presentation group keys organize invoice display by a chosen property. The page's worked payload is illustrative and conflicts with some of its universal field wording.

## Contract-driven invoice types

### Usage invoices

A usage invoice represents services a customer is entitled to and consumes during a contract billing period. Its cadence comes from the contract's usage-statement schedule. The page says draft usage invoices update continuously as usage arrives, but gives no freshness, ordering, read-after-ingest, or snapshot-consistency guarantee.

Usage invoices use type `USAGE` and are associated with `billing_period_start_date` and `billing_period_end_date`. Usage may still be reported during a configurable grace period after the period end, and the invoice is issued on `issue_date` once finalized. Credits or prepaid commitments can reduce the total to zero; the page says such an invoice may remain a revenue record without being sent for payment collection.

Effective-dated product, rate, commitment, and credit changes are reflected without issuing a separate invoice. Metronome divides the invoice into the periods in which entitlements, rates, and balances applied, then applies commitments or credits and calculates overage per line item. The guide does not define recalculation latency, overlapping-change precedence, correction ordering, or how these statements interact with already finalized invoices beyond the later immutability rule.

### Scheduled invoices

A scheduled invoice is produced by adding a commitment or scheduled charge to a contract. The guide positions it for fixed charges including commitment prepayments, postpaid true-ups, and upfront or recurring fees, and says scheduled charges are automatically grouped onto the same invoice without defining the grouping key, currency boundary, or behavior for conflicting schedules.

Scheduled invoices use type `SCHEDULED`, have no grace period, and omit `billing_period_start_date` and `billing_period_end_date`. An issue date in the past or present finalizes immediately. An issue date within two hours of contract creation finalizes within two hours and 30 minutes after creation; one more than two hours away finalizes within 30 minutes of that issue date. These windows qualify the page's broader wording that scheduled invoices finalize "on" the configured issue date.

## Lifecycle and state boundaries

| State | Documented behavior | Important boundary |
| --- | --- | --- |
| Draft | Both types begin as `DRAFT`. Usage drafts update as usage arrives; scheduled drafts remain until their scheduled date. A postpaid true-up draft tracks commitment shortfall and finalizes after the contract's last usage invoice finalizes. | The page defines no draft read consistency, correction ordering, or exact update latency. |
| Grace period | After a usage billing period ends, the default 24-hour buffer accepts late usage and corrections; a Metronome representative can customize it. | No machine-readable status token, minimum, maximum, customization API, or finalization retry behavior is documented. Scheduled invoices have no grace period. |
| Finalized | `FINALIZED` invoices accept no further changes even if later usage is reported. They are ready for delivery and reporting. | Distribution and collection follow contract billing configuration, but this statement is not proof of provider acceptance, customer delivery, settlement, payment success, tax completion, or accounting posting. |
| Void | The guide says a finalized invoice created in error because of provisioning can become `VOID`, then be regenerated in the UI or through the linked endpoint using current usage and pricing. | It does not define eligibility beyond that example, identity, errors, idempotency, concurrency, downstream effects, or the regenerated invoice's state. |

The existing void-endpoint summary uses descriptive status wording `voided` and lists broader intended uses such as billing errors and disputed invoices, whereas this guide names enum-like status `VOID` and specifically describes a provisioning error. Treat these as documentation-scope and terminology differences, not proof of separate runtime states or a complete eligibility contract.

## Line items and presentation

The guide says invoice line items correspond to products or services and lists display name, decimal quantity, unit price, calculated total, and optional pricing and presentation grouping keys. Its prepaid-commit example separates covered usage, a negative commitment application, and uncovered overage, preserving attribution instead of presenting only a net total. Monetary values use the configured currency denomination; the example uses USD cents, but the dedicated currency guide remains the stronger cross-currency authority.

Pricing group keys create separate line items for each priced dimension combination, such as input versus output tokens, but the page says combinations without usage do not create line items. Presentation group keys instead group usage products under an attribute such as project or organization for customer-facing allocation. The guide does not define missing-key behavior, ordering, maximum cardinality, fallback pricing, or whether group labels remain stable after product changes.

## Documentation conflicts and evidence limits

> [!warning] Schema prose versus worked payload
> The usage-invoice schema prose names `billing_period_start_date`, `billing_period_end_date`, and `issue_date`, while the worked JSON uses `start_timestamp`, `end_timestamp`, and `issued_at`. The guide does not map or deprecate either field family. It also says each line item includes quantity and unit price, but the negative prepaid-commit adjustment in the example omits both. Use dedicated API schemas for exact response fields rather than treating this example as a complete contract.

The guide's claims that usage invoices update "in real time" and scheduled invoices finalize within stated windows do not supply a service-level guarantee, error surface, alert, replay rule, or operational recovery procedure. It links regeneration and billing material but does not replace those APIs' authentication, request, response, error, idempotency, concurrency, or downstream-system contracts.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-guides-invoices-overview]], [[source-metronome-api-reference-invoices-regenerate-an-invoice]], [[source-metronome-api-reference-invoices-void-an-invoice]], [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/how-invoicing-works-2026-07-13|2026-07-13 snapshot — Metronome invoice types, lifecycle, line items, and presentation]]