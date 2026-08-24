---
title: "Metronome Get an Invoice API"
type: source
date_ingested: 2026-08-24
canonical_url: "https://docs.metronome.com/api-reference/invoices/get-an-invoice.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/invoices/get-an-invoice-2026-07-13.md"
tags: [metronome, api, invoices, line-items, billing-providers]
---

## Overview

This reference documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices/{invoice_id}` on `https://api.metronome.com`. It retrieves one customer-scoped invoice under a required `data` envelope and exposes invoice state, totals, line items, credit and commit applications, hierarchy attribution, and optional downstream-system records. The surface is useful for billing-portal and support queries, but it does not establish invoice finality, collection, payment, tax, accounting, delivery, or synchronization completion.

## Key takeaways

- `customer_id` and `invoice_id` are required UUID-formatted path parameters. Optional boolean `skip_zero_qty_line_items` filters all zero-quantity line items from the response; the page does not define effects on totals, line ordering, or item identity.
- HTTP `200` requires top-level `data`. Within the invoice object, only `id`, `customer_id`, `credit_type`, `line_items`, `status`, `total`, and `type` are schema-required; billing-period timestamps, contract identity, correction metadata, hierarchy fields, custom fields, and downstream records are optional or conditionally described.
- The prose names `DRAFT`, `FINALIZED`, and `VOID`, says drafts update in real time and may change, and says voided invoices retain original line-item details. The status schema is a plain string with an example rather than an enum, and the page gives no freshness SLA, read-after-write guarantee, lifecycle transitions, retention period, or immutability contract.
- Each line item requires `name`, `total`, `credit_type`, and `type`. Documented types cover scheduled charges, prepaid-commit purchases, usage, subscriptions, applied commits or credits, and custom-pricing-unit conversion; most quantities, prices, product identifiers, service periods, and attribution fields remain optional.
- Applied commits and credits have separate negative-total line items. The page specifically says a postpaid-commit application line is not included in the invoice total because it is paid in arrears; it does not define total reconciliation, precision, rounding, or balance and ledger effects.
- Nullable `external_invoice` and `revenue_system_invoices` can report provider, status or sync state, external identifiers, errors, and selected totals. Their presence does not prove downstream acceptance, delivery, payment, settlement, tax completion, revenue posting, or reconciliation.

## Request, identity, and filtering

Call `GET /v1/customers/{customer_id}/invoices/{invoice_id}` against the documented production server. The OpenAPI document applies a global HTTP bearer scheme. It defines no request body. Both path identifiers are required and UUID-formatted, while `skip_zero_qty_line_items` is an optional boolean query parameter that removes all zero-quantity line items from the returned representation when set.

The page does not define whether invoice IDs are globally unique, whether the customer path component is an authorization boundary, or how a customer-invoice mismatch differs from another missing resource. It also does not document token scope, field-level permissions, or whether client-configuration-gated fields are omitted, redacted, or rejected for an ineligible caller.

> [!warning] Undocumented list-price query parameter
> The `InvoiceLineItem.list_price` description says the field appears for eligible contract usage and subscription lines when `include_list_prices=true`, but the operation parameter list defines only the two path identifiers and `skip_zero_qty_line_items`. This page therefore does not document how to request list prices, whether the parameter is currently supported, or how omission behaves.

## Success envelope and invoice state

HTTP `200` returns JSON whose top-level object requires `data`. The referenced invoice object requires UUID `id`, UUID `customer_id`, `credit_type`, a `line_items` array, string-backed `status` and `type`, and numeric `total`. `credit_type` in turn requires UUID `id` and string `name`. The schema does not require a contract ID, billing-period timestamps, issue time, created time, external record, or separate amount-due field.

Optional UTC timestamps describe the usage-period start and end and invoice issue time. `created_at` is described as present for correction invoices only. Optional correction lineage can expose a `correction_record`, whose object requires `reason`, `memo`, and `corrected_invoice_id` when present, and a separate `regenerated_from_invoice_id`. The page does not define whether those lineage forms are mutually exclusive, exhaustive, immutable, or available for every correction.

The prose says draft invoices update in real time as usage arrives and may change before finalization. It also says a void invoice retains all original line-item details. Those statements do not define refresh latency, snapshot consistency, ordering, cache behavior, visibility of concurrent usage, retention duration, or whether every nested field remains byte-for-byte unchanged after voiding.

> [!warning] Amount-due description versus schema
> The narrative lists both total amount and amount due after credits as key response information, but the invoice schema defines numeric `total` and no separate `amount_due` property. Do not infer that `total` always means amount due, or synthesize an amount-due field, without another authority.

The status schema is a string with the example `DRAFT, VOID, or FINALIZED`; it is not an enum. Likewise, the invoice-type schema is a string whose example says `SCHEDULED or USAGE`, while conditional fields refer to `USAGE_CONSOLIDATED`. Treat these as documented vocabulary and examples, not exhaustive runtime enums.

## Line items and amount attribution

Each invoice line item requires `name`, numeric `total`, `credit_type`, and string `type`. Optional fields can report quantity, unit price, product identity and current tags, inclusive `starting_at`, exclusive `ending_before`, proration, scheduled-charge, subscription, discount, commit, professional-service, tier, grouping, presentation, and custom-field context. Optionality matters: the schema does not promise quantity, unit price, product ID, or a service period on every line.

The line-item description distinguishes these cases:

- `scheduled` points to a scheduled charge.
- `commit_purchase` represents payment for a prepaid commit.
- `usage` represents a usage or composite product.
- `subscription` represents a subscription charge.
- `applied_commit_or_credit` is a separate negative-total application line. Its nested object requires an ID and a type from `PREPAID`, `POSTPAID`, or `CREDIT`. A postpaid application line is expressly excluded from the invoice total.
- `cpu_conversion` converts uncovered spend from a custom pricing unit to fiat using the rate-card conversion when matching prepaid commit or credit is insufficient. The page does not specify formula direction, precision, rounding, tax, or conversion-time snapshot semantics.

For `USAGE`, `SUBSCRIPTION`, or `COMPOSITE` products, `commit_id` is described as the applied credit or commit ID; for `FIXED`, it identifies the prepaid or postpaid commit being paid for. The page does not define whether that overloaded identifier and `applied_commit_or_credit.id` must agree, how partial applications are split, or how line totals reconcile to ledger entries.

## Consolidation, payer, and correction context

The invoice schema includes optional `constituent_invoices`, described as required on `USAGE_CONSOLIDATED` invoices; each constituent requires contract, invoice, and customer UUIDs. Optional line-item `origin`, present on consolidated invoices, requires original line-item, invoice, customer, and contract UUIDs. An optional `payer` object is described as required for account-hierarchy usage invoices and requires the paying contract and customer UUIDs.

These prose-level conditional requirements are not represented in the invoice object's top-level `required` array. The page does not define consolidation ordering, duplicate origins, missing constituent behavior, parent-child authorization, whether standalone invoices remain retrievable, or how payer and source-customer totals reconcile.

## External billing and revenue-system records

`external_invoice` is optional and nullable. If present, its object requires `billing_provider_type`; optional fields can expose an external invoice ID, issued timestamp, external status, provider PDF URL, beta tax details, beta invoiced total and subtotal, provider error, and external payment ID. The provider enum covers Metronome, Stripe, marketplaces, ERP and accounting systems, and custom delivery. The external-status enum includes draft, finalized, paid, partially paid, uncollectible, void, deleted, payment-failed, invalid-request, skipped, sent, and queued states, but `external_status` itself is optional.

`revenue_system_invoices` is also optional and nullable. Each returned item requires provider, sync status, and external entity type; external entity ID and error message are optional. The page does not define the vocabulary or transition model for `sync_status`, polling freshness, provider precedence, multiplicity, retries, terminal states, or consistency between external billing and revenue-system records.

These nested records are observations available from the Metronome invoice read. A returned payment ID or paid-like external status is not, by itself, proof of settlement finality, refund state, tax correctness, accounting posting, or reconciliation. Likewise, absence of an error is not a delivery or sync guarantee.

## Custom fields and schema boundaries

The invoice can expose customer, contract, invoice, product, commit, professional-service, scheduled-charge, subscription, and discount custom-field context. Referenced `CustomField` objects allow arbitrary property names with string values. The invoice-level `custom_fields` property separately declares unrestricted additional properties without a value schema. The page does not define key and value limits, redaction, permissions, freshness, configured-field absence, or whether client-group annotations describe public availability.

Most response objects do not declare `additionalProperties`; under this OpenAPI 3.0.1 page, that omission does not prove that undocumented response fields are rejected or cannot appear. The `billable_status` property also combines a reference to the string enum `billable | unbillable` with a sibling `type: object`, leaving that field's documented shape internally unresolved.

## Errors and operational unknowns

The only documented failure is HTTP `404`, a generic JSON error whose object requires string `message` and whose description says only that the specified resource was not found. It does not distinguish a missing customer, invoice, or customer-invoice relationship. No `400`, `401`, `403`, `429`, or `5xx` response contract is listed; their omission is not proof that those failures cannot occur.

The page defines no rate limit, timeout, retry, cache, ordering, read-after-write, snapshot-consistency, historical-visibility, archive, or authorization-scope contract. Because this is GET, the separate API-wide POST idempotency authority does not establish endpoint-specific read guarantees. The Contracts invoice schema remains distinct from the legacy shared Plans surface, but invoice status casing conflicts across current wiki authorities.

> [!warning] Invoice status casing across sources
> This read page defines `InvoiceStatus` only as a string and gives uppercase `VOID` in its example; its prose also says a voided invoice response indicates `VOID`. The separate [[source-metronome-api-reference-invoices-void-an-invoice|void-operation source]] and [[metronome-invoicing|invoicing concept]] preserve operation prose that says the status is set to lowercase `voided`, while that POST success schema does not return a status field. Preserve both source-scoped statements: enum exhaustiveness, casing normalization, and whether the lowercase operation wording is a literal value returned by this GET endpoint remain unresolved. The internal list-price, amount-due, invoice-type, and billable-status gaps above also remain unresolved.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-integrations]], [[metronome-custom-fields]]
- Related sources: [[source-metronome-api-reference-invoices-get-an-invoice-pdf]], [[source-metronome-plans-shared-endpoints-invoices]], [[source-metronome-api-reference-invoices-void-an-invoice]], [[source-metronome-api-reference-invoices-regenerate-an-invoice]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/get-an-invoice-2026-07-13|2026-07-13 snapshot - single-invoice retrieval, required envelope, line-item attribution, hierarchy context, and downstream records]]
