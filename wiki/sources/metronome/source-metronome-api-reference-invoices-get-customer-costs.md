---
title: "Metronome Get Customer Costs API"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/invoices/get-customer-costs"
raw_files:
  - "metronome/api-reference/invoices/get-customer-costs-2026-07-13.md"
tags: [metronome, api, invoices, costs, plans, contracts, pagination]
---

## Overview

This OpenAPI page documents bearer-authenticated `GET /v1/customers/{customer_id}/costs`, a deprecated Plans read for one customer's daily pending costs. It returns cost intervals grouped first by credit type and then, when present, by line item; it is not an invoice-object read, a finalized billing record, or evidence of downstream billing or payment. Metronome directs new clients to Contracts without identifying a replacement operation or migration mapping on this page.

## Query-critical facts

- Required UUID path `customer_id` selects one customer. Required RFC 3339 query parameters `starting_on` and `ending_before` define an inclusive lower bound and exclusive upper bound. The narrative calls the results daily, but the schema does not define timezone, midnight alignment, exact 24-hour bucket construction, ordering, or treatment of partial boundary days.
- Optional integer `limit` is constrained to `1` through `100`, and optional string `next_page` resumes traversal. HTTP `200` requires sibling `data` and nullable `next_page` at the response-envelope level. Complete retrieval therefore requires following a non-null cursor, but the page supplies no default page size, ordering, total count, cursor lifetime, snapshot consistency, duplicate-or-skip behavior under change, or freshness guarantee.
- Each `data` item requires `start_timestamp`, `end_timestamp`, and `credit_types`. `credit_types` is an arbitrary-key object: each key is a credit-type identifier and each value may contain `name`, numeric `cost`, and `line_item_breakdown`. Those three value properties are not required by the schema, so their absence must not be converted into zero cost, an empty breakdown, or a runtime failure by inference.
- `line_item_breakdown` is nested inside one credit-type value, not beside `credit_types` or at the response envelope. When the array is present, every item requires string `name` and numeric `cost`; optional `group_key` is a string and optional `group_value` is a nullable string. The example's `USD (cents)` key, `123.45` cost, and `CPU hours` line are illustrative, not a denomination, precision, rounding, reconciliation, or universal line-item guarantee. Use [[source-metronome-api-reference-settings-list-pricing-units]] for pricing-unit taxonomy and the documented USD-cents identifier.
- The operation is expressly unsupported when the customer's Plan includes a `UNIQUE`-type billable metric. The page does not define detection timing, whether one such metric blocks every requested interval, the error status or body, partial-data behavior, or a Contracts equivalent. Existing billable-metric authorities separately preserve a documentation tension between case-varied `UNIQUE` enum values and guide-level direction to use SQL for distinct counts; do not equate this exclusion with every SQL metric or silently choose one interpretation.
- This is a Plans (deprecated) endpoint. [[source-metronome-api-reference-plans-list-plans]] is consistent that new clients are directed to Contracts without a replacement route, Plan-to-Contract identity or field mapping, migration procedure, compatibility period, or removal date. [[source-metronome-api-reference-invoices-list-invoice-breakdowns]], [[source-metronome-api-reference-invoices-list-invoices]], and [[source-metronome-api-reference-invoices-get-an-invoice]] are separate current invoice authorities; none is documented here as the replacement for `/customers/{customer_id}/costs`.

## Material boundaries and documentation tensions

> [!warning] UNIQUE authority boundary
> The endpoint's unsupported-`UNIQUE` statement is operation-specific. The broader metric documentation retains conflicting `UNIQUE` enum and SQL-distinct guidance, and this page supplies neither the metric-classification rule nor an unsupported-request error contract. Do not infer that all SQL metrics are unsupported, that every `UNIQUE` spelling is accepted, or that a missing error schema implies success, rejection, or partial results.

> [!warning] Plans-to-Contracts migration gap
> “New clients should implement using Contracts” establishes direction, not a replacement API contract. The page does not name a Contracts route, map customer, Plan, cost-window, credit-type, or line-item fields, define historical continuity, or state when the legacy endpoint becomes unavailable. The shared Plan-and-Contract invoice catalog and current invoice List, Get, and Breakdowns pages remain separate authorities, not inferred substitutes.

“Pending costs” does not define an invoice ID, contract or Plan identifier, invoice type or status, issue or finalization time, revision, as-of timestamp, or persistence rule. The page does not say when new usage becomes visible, whether earlier results can change, how cursor traversal behaves during change, or how the returned cost intervals reconcile to a draft, finalized, voided, regenerated, or exported invoice. It also establishes no invoice creation or mutation, credit or commit balance or ledger mutation, tax result, billing-provider delivery, customer delivery, collection, payment, settlement, revenue posting, accounting conclusion, or downstream reconciliation.

Only generic HTTP `400` and `404` responses with a required string `message` are documented; the page does not assign failures to invalid windows, unsupported `UNIQUE` metrics, missing customers, authorization, cursor errors, throttling, or other causes. This GET operation has no request body, and absent closed-object declarations or omitted schema properties must not be used to infer unknown-field acceptance, response-field exhaustiveness, or runtime behavior.

## Raw-detail coverage map

- **Operation and scope:** production server, bearer security, GET path, operation ID, customer scope, daily-pending-cost description, deprecated Plans label, Contracts direction, and unsupported-`UNIQUE` boundary are in raw.
- **Window and traversal:** required inclusive `starting_on`, required exclusive `ending_before`, optional `1`-to-`100` `limit`, optional request cursor, required nullable response cursor, examples, and generic `400`/`404` responses are in raw; ordering, cursor stability, total count, freshness, and snapshot behavior are not documented.
- **Response placement:** required envelope `data` and `next_page`; required cost-item interval and `credit_types` map; optional per-credit-type `name`, `cost`, and nested breakdown; and required line-item `name`/`cost` plus optional group fields are in raw.
- **Example and schema limits:** the exact USD-cents identifier, daily interval, numeric example, CPU-hours line, arbitrary credit-type keys, nullable group value, and objects without closed-schema declarations are in raw; no runtime behavior should be inferred from missing required lists or properties.
- **Authority boundary:** use the assigned page for this legacy pending-cost read, pricing-unit authority for credit-type taxonomy, billable-metric authorities for metric semantics, and dedicated invoice List, Get, and Breakdowns sources for their own invoice contracts. None supplies an undocumented Contracts replacement or downstream outcome guarantee for this endpoint.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-reporting-and-analytics]], [[metronome-customers-and-contracts]], [[metronome-billable-metrics]], [[metronome-currencies-and-custom-pricing-units]]
- Related sources: [[source-metronome-api-reference-invoices-list-invoice-breakdowns]], [[source-metronome-api-reference-invoices-list-invoices]], [[source-metronome-api-reference-invoices-get-an-invoice]], [[source-metronome-plans-shared-endpoints-invoices]], [[source-metronome-api-reference-plans-list-plans]], [[source-metronome-api-reference-settings-list-pricing-units]]

## Raw Sources

- [[raw/metronome/api-reference/invoices/get-customer-costs-2026-07-13|2026-07-13 snapshot - complete deprecated Plans customer daily pending-cost read, pagination, credit-type map, line-item breakdown, unsupported-metric boundary, and OpenAPI responses]]
