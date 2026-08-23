---
title: "Metronome API Reference: Get a Customer"
type: source
date_ingested: 2026-08-23
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/get-a-customer.md"
raw_files:
  - "metronome/api-reference/customers/get-a-customer-2026-07-13.md"
tags: [metronome, customers, api-reference, ingest-aliases, custom-fields]
---

## Overview

This API reference documents the bearer-authenticated `GET /v1/customers/{customer_id}` endpoint for retrieving one customer by Metronome UUID. The response exposes the customer's identity, timestamps, usage-event aliases, configuration data, and custom fields, while directing billing-configuration searches to a separate endpoint.

## Key takeaways

- The required `customer_id` path parameter is a UUID and identifies the customer by its Metronome ID.
- HTTP `200` returns a required `data` envelope containing a `CustomerDetail`; the schema requires the customer's ID, deprecated `external_id`, ingest aliases, name, creation and update timestamps, customer configuration, and custom fields.
- `ingest_aliases` are alternate identifiers usable instead of the Metronome customer ID in usage events. The returned `external_id` remains required by this response schema but is deprecated in favor of ingest aliases.
- Customer custom fields are returned as an object whose arbitrary keys have string values. `customer_config` separately requires a nullable `salesforce_account_id`; this page does not establish that it is a customer billing-provider configuration.
- The optional nullable `archived_at` records when the customer was archived. An optional `current_billable_status` is available only for some client configurations and, when present, contains a required `billable` or `unbillable` value plus an optional nullable effective timestamp.

## Endpoint and request

The production server is `https://api.metronome.com`, the operation ID is `getCustomer-v1`, and the OpenAPI document applies HTTP bearer authentication. The operation takes one required path parameter, `customer_id`, whose schema is a UUID-formatted string. No query parameters or request body are defined on this page.

The page explicitly says billing-configuration lookups should use `/getCustomerBillingConfigurations`. It does not provide that endpoint's method, request contract, or response schema, so this customer-detail response must not be treated as the billing-configuration authority.

## Response schema

A successful response requires a top-level `data` property referencing `CustomerDetail`. Within that object, `id`, `external_id`, `ingest_aliases`, `name`, `customer_config`, `custom_fields`, `created_at`, and `updated_at` are required. `id` is a UUID; `created_at` and `updated_at` are RFC 3339 date-time strings.

`external_id` is described as the first Metronome ID or ingest alias usable in usage events, but is deprecated in favor of `ingest_aliases`. The alias array contains strings that may replace the Metronome customer ID in usage events. The page does not state alias ordering, uniqueness, or whether every returned alias is currently active.

`customer_config` references a schema that requires `salesforce_account_id`, while allowing that string field to be null. The page supplies no semantics for null or stale Salesforce mappings and does not define unknown-field behavior for this object. `custom_fields` is an open string-valued map.

`archived_at` is optional and nullable; when present it is an RFC 3339 timestamp, and null denotes an active customer. `current_billable_status` is also optional and explicitly configuration-dependent. Its nested `value` is required and enumerated as `billable` or `unbillable`; `effective_at` is optional and nullable. This page does not define the status's billing effect, derivation, freshness, transition history, or behavior for clients where the field is unavailable.

## Documented boundaries

The operation documents only HTTP `200 Success`. It does not define not-found representation, authentication or authorization errors, malformed-ID behavior, rate limits, retry guidance, cache or read-after-write consistency, or response freshness. Although the response can carry `archived_at`, the page does not say whether archived customers are always retrievable, for how long, or under what access rules.

The `CustomerDetail` schema does not set an `additionalProperties` policy, so this source does not establish how clients should handle undocumented response fields.

No contradiction was found with the existing customer-creation, customer-provisioning, custom-field, or event-ingestion summaries when the retrieval schema is kept separate from creation limits and billing-provider configuration.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-custom-fields]]
- Related sources: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-custom-fields]]

## Raw Sources

- [[raw/metronome/api-reference/customers/get-a-customer-2026-07-13|2026-07-13 snapshot — customer retrieval endpoint and embedded OpenAPI schema]]