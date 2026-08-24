---
title: "Metronome API Reference: List Customers"
type: source
date_ingested: 2026-08-24
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/list-customers.md"
raw_files:
  - "metronome/api-reference/customers/list-customers-2026-07-13.md"
tags: [metronome, customers, api-reference, pagination, ingest-aliases]
---

## Overview

This reference documents the bearer-authenticated `GET /v1/customers` endpoint for browsing, searching, or synchronizing customers in a Metronome account. It is the authority for this list operation's query filters, cursor envelope, and returned customer-detail schema; it does not establish customer lifecycle policy or synchronization consistency.

## Key takeaways

- The endpoint returns active customers by default. Optional filters select one ingest alias, up to 100 customer IDs, only archived customers, or up to 100 Salesforce account IDs; the page does not define how combined filters interact.
- Cursor pagination uses optional `limit` and `next_page` query parameters. `limit` accepts 1 through 100, and a successful response requires both the `data` array and a nullable `next_page`.
- Every returned `CustomerDetail` requires the customer's UUID, deprecated `external_id`, ingest aliases, name, creation and update timestamps, customer configuration, and custom fields.
- `archived_at` is optional and nullable. `current_billable_status` is also optional and configuration-dependent; when present, it requires a `billable` or `unbillable` value and may include a nullable effective timestamp.
- The reference defines neither result ordering nor default page size, cursor lifetime, snapshot consistency, freshness, errors, or read-after-write behavior.

## Endpoint and filters

The production server is `https://api.metronome.com`, the operation ID is `listCustomers-v1`, and the OpenAPI document applies HTTP bearer authentication. All documented inputs are optional query parameters: `limit`, `next_page`, `ingest_alias`, `customer_ids`, `only_archived`, and `salesforce_account_ids`. No request body is defined; that absence documents no body schema but does not prove how the runtime handles a supplied body.

`limit` has a minimum of 1 and maximum of 100. `next_page` identifies where the following page should start. The page does not document a default limit, array-query serialization, cursor opacity, expiry, reuse, or behavior after the underlying customer set changes.

`ingest_alias` filters by one string alias. The `customer_ids` description limits the filter to 100 IDs, but its array schema has no `maxItems` and does not require UUID formatting. By contrast, `salesforce_account_ids` has both the same prose limit and `maxItems: 100`. These are documentation and schema boundaries, not permission to exceed the prose customer-ID limit.

`only_archived` filters the list to archived customers, while the documented default returns only active customers. The reference does not define whether an explicit false differs from omission, whether active and archived customers can be returned together, archive retention, restoration, or visibility rules.

## Response schema

HTTP `200` requires an object with `data` and `next_page`. `data` is an array of `CustomerDetail` objects; `next_page` is a nullable string. The endpoint-specific schema is consistent with the general pagination authority's terminal-null convention, but this page does not independently state whether every non-null cursor guarantees another nonempty page.

Each customer item requires `id`, `external_id`, `name`, `created_at`, `updated_at`, `customer_config`, `ingest_aliases`, and `custom_fields`. The UUID-formatted `id` is Metronome's customer ID. `external_id` remains required in this response schema but is deprecated in favor of `ingest_aliases`; those aliases can replace the Metronome customer ID in usage events. The page does not define alias ordering, uniqueness, or active-state semantics.

`customer_config` requires a `salesforce_account_id` property whose string value may be null. `custom_fields` is an open map with string-valued properties. These structures must not be conflated with customer billing-provider configurations, and the page does not define Salesforce-link freshness or custom-field ordering.

Optional `archived_at` is an RFC 3339 timestamp and is null for an active customer when present. Optional `current_billable_status` is available only for some client configurations. Its nested `value` is required and enumerated as `billable` or `unbillable`; `effective_at` is optional and nullable. The reference does not define status derivation, billing effects, transition history, or freshness.

## Documented boundaries

Only HTTP `200 Success` is documented. The page does not define authentication or authorization errors, malformed filters, rate limits, retry guidance, partial results, response ordering, cursor lifetime, snapshot isolation, concurrent-update behavior, or read-after-write consistency. It also does not specify how multiple filters combine or whether duplicate IDs affect results.

`CustomerDetail` does not set an `additionalProperties` policy, so the source does not establish unknown response-field behavior. The prose-only maximum for `customer_ids` and schema-level `maxItems` for `salesforce_account_ids` are an asymmetry, not a contradiction with the documented 100-ID limit. No contradiction was found with the existing single-customer retrieval, customer creation, pagination, event-ingestion, or custom-field authorities.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-custom-fields]]
- Related sources: [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-pagination]]

## Raw Sources

- [[raw/metronome/api-reference/customers/list-customers-2026-07-13|2026-07-13 snapshot — customer-list endpoint and embedded OpenAPI schema]]