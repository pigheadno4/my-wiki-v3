---
title: "Metronome Custom Fields"
type: concept
category: technology
tags: [metronome, custom-fields, metadata, integrations]
---

## Definition

Metronome custom fields attach metadata such as foreign keys and other descriptors to platform objects. They preserve relationships between Metronome entities and records in external systems so those systems can contextualize Metronome data and support connected business processes.

## Entity scope and persistence

The overview lists customers, products, contracts, commits, credits, scheduled charges, rate cards, and alerts as supported entities. Values persist with an object and are returned wherever that object appears in the Metronome app, API calls, and data exports.

The customer-credit create schema accepts `custom_fields` for the `contract_credit` entity. The referenced `CustomField` is a typed object with `additionalProperties: {type: string}`. Under OpenAPI 3.0.1, neither schema sets `nullable: true`, so a supplied `custom_fields` value must be a non-null object and each supplied arbitrary property value must be a non-null string at the schema boundary. The endpoint does not define configured-key validation, uniqueness, limits, endpoint-specific runtime error mapping for invalid nulls, deletion-by-null semantics, overwrite behavior, persistence, API or export visibility, invoice propagation, or archived-credit handling; those behaviors must come from the dedicated custom-fields authority rather than this create operation.

The `listBalances` Commit and Credit response schemas can each expose optional `custom_fields` through an arbitrary-key object whose additional-property values are strings. The Commit field is annotated as entity `commit`; the Credit field is annotated `contract_credit`. This endpoint does not define key format, value length, field count, visibility, redaction, permissions, availability, or unset-value behavior.

## Uniqueness

Uniqueness is intended for foreign entities that have a one-to-one relationship with a Metronome object. Enforcement continues for archived objects; resolving a duplicate involving an archived object requires resetting that object's field value.

## Invoice propagation

A Product custom field can propagate to the associated invoice line item. The overview's `stripe_product_id` example uses this propagation to link an invoice line item to a Stripe product when creating invoices in Stripe.

## Billable-metric response shape

The `GET /v1/billable-metrics` response schema can expose `custom_fields` on each returned billable metric as an object with arbitrary property names and string values. The field is optional because only metric `id` and `name` are required. This endpoint does not document custom-field key, value, or entry-count limits, visibility rules, redaction behavior, or whether every field configured elsewhere is returned through this listing. [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]]

## Customer retrieval surface

`GET /v1/customers/{customer_id}` returns the required customer `custom_fields` property as an open object with string-valued properties inside the customer detail. The endpoint does not define configured map-key ordering or endpoint-specific freshness, and its separate `customer_config` object must not be conflated with custom fields. [[source-metronome-api-reference-customers-get-a-customer]]

## Limits of the overview

The overview establishes the purpose, supported object examples, persistence, uniqueness, and invoice-line propagation of custom fields. It does not establish endpoint methods, request or response schemas, or endpoint-specific behavior; those details require complete reads of the relevant API references.

## Sources

- [[source-metronome-api-reference-custom-fields]] — overview, supported entity scope, persistence, uniqueness, and product-to-invoice-line propagation

- [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]] - billable-metric response custom fields as an arbitrary-key, string-valued object and undocumented limits

- [[source-metronome-api-reference-customers-get-a-customer]] — customer-detail retrieval of the string-valued custom-field map and endpoint-specific read boundaries

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - contract-credit custom-field input shape and endpoint-specific validation and propagation limits

- [[source-metronome-api-reference-credits-and-commits-list-balances]] - optional commit and contract-credit custom-field response maps, string-valued additional properties, and endpoint-level limits and visibility unknowns

## Related

- [[metronome-integrations]]
- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-reporting-and-analytics]]
