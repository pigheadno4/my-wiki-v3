---
title: "Metronome List Invoices API"
type: source
date_ingested: 2026-08-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/list-invoices"
raw_files:
  - "metronome/api-reference/invoices/list-invoices-2026-08-28.md"
  - "metronome/api-reference/invoices/list-invoices-2026-07-13.md"
tags: [metronome, api, invoices, pagination, reporting]
---

## Overview

This OpenAPI page documents bearer-authenticated `GET /v1/customers/{customer_id}/invoices`, a cursor-paginated List operation for one customer's billing history and current charges. It supports billing portals, support, reconciliation, and reporting, but its List response and endpoint-local narrative do not replace the separate Get Invoice or invoice-mutation contracts.

## Query-critical facts

- At the GET operation's parameter list, `customer_id` is a required UUID-formatted path parameter. Principal optional query parameters are integer `limit` from `1` through `100`, string cursor `next_page`, open-string `status`, enumerated invoice `type`, boolean `skip_zero_qty_line_items`, `sort`, `credit_type_id`, UUID `contract_id`, and the billing-period bounds `starting_on` and `ending_before`. The full parameter catalog, including the feature-annotated webhook-notification field, remains in raw.
- The operation-level `starting_on` query parameter is an inclusive RFC 3339 lower bound on billing-period start, while `ending_before` is an exclusive RFC 3339 upper bound on billing-period end; neither is an issue-date filter. The operation's `sort` parameter orders by `issued_at` and says omission defaults to `date_asc`.
- HTTP `200` has a response-envelope object requiring `data` and `next_page`; `data` is an array whose items reference the `Invoice` schema, and `next_page` is a nullable string. Continue with the cursor until the separate API-wide pagination convention returns `null`; this page defines no cursor lifetime, result-snapshot, or concurrent-update guarantee.
- At the operation-query level, `type` permits `USAGE`, `USAGE_CONSOLIDATED`, and `SCHEDULED`; `status` is only an open string with examples `DRAFT`, `FINALIZED`, and `VOID`. The narrative says void invoices are included unless status-filtered and draft invoices update as usage arrives, but it defines no freshness SLA or stable read snapshot.
- Within the top-level `Invoice` item, optional `billable_status` is described as indicating whether the invoice has been or will be sent to the configured customer billing provider and defaults to `billable`. Its property combines a `$ref` to `BillableStatus` with sibling `type: object`, so the referenced-versus-object shape is internally unresolved on this page. It is separate from nullable `Invoice.external_invoice` and that nested object's optional `external_status`; none proves delivery, payment, settlement, tax, accounting, or reconciliation completion.
- Within the response component `AppliedCommitOrCredit`, `id` and `type` are required and optional feature-annotated `access_type` says `SPEND` deducts the dollar cost of usage while `QUANTITY` deducts the number of units used. This List response gives no `access_type` default and does not establish access-schedule configuration, balance or ledger mutation, denomination, precision, rounding, or mutation behavior; use raw for its exact `InvoiceLineItem.applied_commit_or_credit` placement.

## Material boundaries and contradictions

> [!warning] Conflicting default-order authorities
> The narrative says results default to creation-date descending (newest first), but the operation's `sort` parameter says it orders by `issued_at` and defaults to `date_asc`. The page does not reconcile creation time with issue time or identify which default governs, so callers that require deterministic ordering should pass `sort` explicitly.

> [!warning] Summary versus List schema
> The narrative calls the results invoice summaries and directs detailed-line-item queries to Get Invoice, yet the List success envelope references `Invoice`, whose required properties include `line_items`, and its example contains a line item. The page supplies no projection or truncation contract, so do not infer either line-item omission or Get-equivalent completeness.

The narrative names due date, subtotal, and amount due, but the List `Invoice` schema does not define separate `due_date`, `subtotal`, or `amount_due` properties. Most response objects omit `additionalProperties: false`, so their documented property sets are not proven closed. Only HTTP `404` is specified, with a generic required message; authentication, authorization, invalid-filter, throttling, timeout, retry, cache, and other failure behavior remain undocumented here.

## Raw-detail coverage map

- **Operation and traversal:** production server, bearer security, complete path and query parameter catalog, formats, enums, feature annotations, success envelope, example, and generic `404` are in the current raw page.
- **Invoice identity and lifecycle:** complete required and optional `Invoice` properties, status and type vocabularies, billing-period and correction timestamps, consolidation, payer, regeneration, and correction lineage are in raw.
- **Line items and financial attribution:** the full `InvoiceLineItem` catalog, exact quantity and amount wording, product and service-period attribution, applied credit or commit identity, quantity-consumption field, postpaid-total treatment, custom-pricing-unit conversion, rates, tiers, discounts, and origin records are in raw.
- **External and metadata surfaces:** billing-provider and revenue-system records, provider/status enums, tax and invoice-total fields, errors, custom fields, client-configuration gates, reseller data, and NetSuite fields are in raw; their presence remains response observation rather than external outcome proof.
- **Schema history:** the retained 2026-07-13 snapshot preserves the prior configuration-dependent description of `Invoice.billable_status` and predates the current quantity-consumption and nested access-type additions. List, Get, and mutation pages retain separate versioned authority.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-reporting-and-analytics]]
- Additional affected concept: [[metronome-credits-and-commits]]
- API-wide navigation: [[source-metronome-api-reference-pagination]]
- Separate Get contract: [[source-metronome-api-reference-invoices-get-an-invoice]]
- Legacy shared surface: [[source-metronome-plans-shared-endpoints-invoices]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/list-invoices-2026-08-28|2026-08-28 snapshot - customer invoice listing, filters, pagination, delivery-intent status, nested applied-balance access type, and current List schema]]
- [[raw/metronome/api-reference/invoices/list-invoices-2026-07-13|2026-07-13 snapshot - prior List schema and immutable description history]]
