---
title: "Metronome Shared Invoice Endpoints for Plans and Contracts"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/plans-shared-endpoints/invoices"
raw_files:
  - "metronome/plans-shared-endpoints/invoices-2026-07-13.md"
tags: [metronome, invoices, plans, contracts, api-reference]
---

## Overview

This page describes a shared Metronome invoice surface for Plans and Contracts. It catalogs customer-scoped retrieval, regeneration, and voiding operations and documents plan context, adjustments, sub-line items, and tier detail returned with associated invoices.

## Key takeaways

- The shared surface retrieves one customer invoice, lists a customer's invoices, regenerates a previously issued invoice, and voids an invoice.
- Contract invoices may include commit, credit, or usage details, while Plan invoices are generally scoped to plan-level billing events.
- Associated invoices include plan identity and generation-time plan custom fields plus invoice adjustments and sub-line-item breakdowns.
- Adjustments require a name, total, and credit type; credit-grant identity and custom fields are optional.
- Sub-line items require a name, quantity, subtotal, and custom fields. Unit price is present only for a non-tiered charge with nonzero quantity, while tiered charges can expose a tier period and per-tier quantity, price, and subtotal.

## Shared endpoint catalog

| Documented path | Purpose |
| --- | --- |
| `/customers/{customer_id}/invoices/{invoice_id}` | Retrieve one invoice for a customer. |
| `/customers/{customer_id}/invoices` | List invoices for a customer. |
| `/invoices/regenerate` | Regenerate a previously issued invoice. |
| `/invoices/void` | Void an existing invoice. |

The page gives path fragments and descriptions but does not specify HTTP methods, a versioned API prefix, authentication, pagination, request bodies, response envelopes, idempotency, or invoice-state preconditions. It also does not say whether regeneration or voiding changes an invoice already delivered to a downstream billing provider.

## Plan and contract context

The response context includes `plan_id`, `plan_name`, and `plan_custom_fields`; the custom-field map reflects the associated plan at invoice-generation time. The page also applies the shared endpoints to Contracts but does not define how these plan fields are populated or omitted for a contract-targeted invoice, or how a caller selects Plan versus Contract behavior.

The source says Contract invoices may contain commit, credit, or usage details and characterizes Plan invoices as generally scoped to plan-level billing events. It does not enumerate the differing request or response parameters beyond the plan, adjustment, and sub-line-item fields shown on the page. The page points readers to `/api-reference/invoices/get-an-invoice` as the Contracts version of the documentation, but this assigned page itself does not enumerate the differing Plan-versus-Contract request and response parameters; no methods, schemas, or behavior from that linked page are inferred here.

## Adjustment schema

Each `invoice_adjustments` entry requires `name`, numeric `total`, and `credit_type`. `credit_grant_id` and `credit_grant_custom_fields` are optional. The page gives a monthly-minimum example but does not define amount units, currency, sign conventions, allowed credit-type values, ordering, or how an adjustment affects invoice totals.

## Sub-line items and tiers

Each `sub_line_items` entry requires `name`, `quantity`, `subtotal`, and `custom_fields`. Optional identifiers can associate the entry with a charge or credit grant. `start_date` and `end_date` are documented only for seat charges, while `price` is present only when the charge is not tiered and quantity is nonzero.

For tiered charges, optional `tier_period` records a required RFC 3339 `starting_at` value and optional RFC 3339 `ending_before` value. Each object in `tiers` requires numeric `starting_at`, `quantity`, `price`, and `subtotal`. The page does not define tier ordering, boundary semantics, quantity or monetary units, rounding, empty arrays, or the relationship between tier subtotals and the parent sub-line-item subtotal.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-invoicing]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-invoices-overview]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]

## Raw Sources

- [[raw/metronome/plans-shared-endpoints/invoices-2026-07-13|2026-07-13 snapshot - shared Plan and Contract invoice endpoints and schemas]]
