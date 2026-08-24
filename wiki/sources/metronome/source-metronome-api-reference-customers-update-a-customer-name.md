---
title: "Metronome API Reference: Update a Customer Name"
type: source
date_ingested: 2026-08-24
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/update-a-customer-name.md"
raw_files:
  - "metronome/api-reference/customers/update-a-customer-name-2026-07-13.md"
tags: [metronome, customers, api-reference, customer-names, invoicing]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/customers/{customer_id}/setName` mutation for changing one Metronome customer's display name. It is the endpoint authority for request requiredness, name truncation, and the immediate propagation claim; separate customer, invoice, authentication, and idempotency authorities are still needed for broader lifecycle, downstream, and retry behavior.

## Key takeaways

- The required `customer_id` path parameter is a UUID-formatted Metronome customer ID.
- The enclosing OpenAPI `requestBody` is not marked `required: true`, while `SetCustomerNamePayload` requires the string property `name`; omitted-body behavior is therefore undocumented.
- A supplied name longer than 160 characters is truncated to 160 characters. The page gives no minimum length, normalization, character-counting, or empty-string rule.
- HTTP `200` requires a top-level `data` envelope containing a `Customer`; that object requires `id`, deprecated `external_id`, `ingest_aliases`, and `name`, and may include customer `custom_fields`.
- Metronome states that the updated name is applied immediately across all billing documents and interfaces, but the page does not define the scope of "all" across historical, draft, finalized, rendered, exported, webhook, or downstream-provider copies.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/customers/{customer_id}/setName` |
| Operation ID | `setCustomerName-v1` |
| Authentication | Top-level HTTP bearer authentication through `bearerAuth` |
| Required path input | UUID-formatted `customer_id` |
| Request media type | `application/json` |
| Required payload property | String `name` |
| Success | HTTP `200` with required `data` referencing `Customer` |
| Listed endpoint errors | None |

The endpoint identifies the customer only through the path UUID. It defines no query parameters and no request field for an ingest alias or deprecated external ID, so this page does not establish name updates by either alternate identifier. Bearer authentication is explicit, but endpoint-specific token scope, role, permission, and authorization-failure behavior are not documented.

## Request schema and validation boundaries

`SetCustomerNamePayload` is an object whose required list contains `name`. The property is a string and is truncated when longer than 160 characters. The schema sets no `minLength`, pattern, enum, or nullable marker, and the page does not define whitespace handling, Unicode counting, normalization, duplicate-name constraints, or whether an unchanged name has any distinct behavior.

The operation's `requestBody` has a description, JSON content, schema reference, and example, but it lacks `required: true`. Requiredness of the payload property must therefore remain separate from operation-level body requiredness. The payload object also has no `additionalProperties` policy, so the page does not establish whether unknown request properties are accepted, ignored, stored, or rejected.

## Success response and customer identity

The `200` response object requires `data`, which references `Customer`. That customer object requires UUID `id`, `external_id`, `ingest_aliases`, and `name`. `external_id` is deprecated in favor of `ingest_aliases`; the alias array is described as identifiers usable instead of the Metronome customer ID in usage events. Their presence in the returned representation does not prove that this name-only mutation changes, reorders, or revalidates either identity field.

The response may include `custom_fields`, which references an arbitrary-key object with string values, but `custom_fields` is not required in this `Customer` schema. The endpoint does not mutate custom fields or define their freshness, ordering, visibility, or propagation. The enclosing response and `Customer` objects do not set an `additionalProperties` policy, so this source does not establish whether other response fields can appear or how clients should treat them.

## Propagation and lifecycle boundary

The page says the new name is applied immediately across all billing documents and interfaces. Preserve that documented product claim, but do not extend it into undocumented mechanics: the page does not distinguish already-finalized from draft or future documents; define whether PDFs, exports, audit logs, webhooks, data exports, or downstream Stripe, ERP, or marketplace records are included; specify cache invalidation or measurable propagation latency; or establish payment, tax, accounting, delivery, settlement, or reconciliation effects.

The returned customer object confirms the successful mutation result and new name, but the page defines no version, `updated_at`, change-event identity, audit entry, rollback, scheduled update, archive-state restriction, or read-after-write procedure. It also does not say whether archived customers can be renamed.

## Idempotency, errors, concurrency, and recovery

This endpoint page lists only HTTP `200` and supplies no `400`, `401`, `403`, `404`, `409`, `429`, or `5xx` response contract. It does not define malformed or missing body behavior, missing or inaccessible customer representation, validation errors, truncation signaling, rate limits, partial failure, concurrent rename ordering, repeated-call behavior, timeout recovery, or whether success is atomic with the claimed document/interface propagation.

The separate [[source-metronome-api-reference-idempotency|Metronome API-wide idempotency authority]] applies `Idempotency-Key` to all POST endpoints: the same key with identical parameters returns the original result, changed parameters return HTTP `409 Conflict`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. This endpoint neither repeats nor narrows that contract and exposes no resource `uniqueness_key`. A same-key replay recovers the original result rather than proving a fresh read of the customer's current name; after an ambiguous failure, the endpoint page does not define current customer or document state, safe changed-key behavior, or reconciliation steps.

## Contradiction check

No direct contradiction was found when the authorities are kept source-scoped. The create-customer authority independently documents the same longer-than-160-character truncation behavior and returns a `Customer` representation with UUID `id`, deprecated `external_id`, `ingest_aliases`, and `name`. The get-customer authority documents retrieval by a required UUID and a richer `CustomerDetail` response whose required fields include UUID `id`, deprecated `external_id`, `ingest_aliases`, `name`, `customer_config`, `custom_fields`, `created_at`, and `updated_at`; it does not document a name-length or truncation rule. Across all three pages, `external_id` is deprecated in favor of `ingest_aliases`, and ingest aliases are described as identifiers usable instead of the Metronome customer ID in usage events. The create/update `Customer` schemas and get-customer `CustomerDetail` schema have different required-field sets and should not be flattened. The broad "immediately across all billing documents and interfaces" statement is an unresolved scope boundary rather than proof that external copies, finalized artifacts, or downstream financial outcomes are synchronously changed.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]], [[metronome-custom-fields]], [[metronome-security-principles]]
- Customer context: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-customers-get-a-customer]]
- API context: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/update-a-customer-name-2026-07-13|2026-07-13 snapshot — customer-name mutation, response schema, and propagation claim]]
