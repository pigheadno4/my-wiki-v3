---
title: "Metronome API Reference: Update a Customer Configuration"
type: source
date_ingested: 2026-08-31
canonical_url: "https://docs.metronome.com/api-reference/customers/update-a-customer-configuration"
original_format: webpage
raw_files:
  - "metronome/api-reference/customers/update-a-customer-configuration-2026-07-13.md"
tags: [metronome, customers, customer-configuration, salesforce, integrations, api-reference]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/customers/{customer_id}/updateConfig`, which updates configuration for one Metronome customer without changing core customer data such as the customer's name or ingest aliases. The page names external-system linkage and customer-specific billing parameters as configuration scope, but its only concrete payload property is the nullable Salesforce account ID; it is not authority for customer billing-provider configuration, invoice routing, core-data mutations, or Salesforce synchronization.

## Query-critical facts

- The production operation is `POST /v1/customers/{customer_id}/updateConfig` under top-level HTTP bearer authentication. The path `customer_id` is required and UUID-formatted. The page defines no endpoint-specific token role, permission scope, authorization-failure body, or archived-customer eligibility.
- The operation is scoped to customer configuration. Its description expressly separates configuration from core customer data such as `name` and ingest aliases, and the request schema exposes neither core field. The broader phrase "other customer-specific billing parameters" supplies no additional property names, validation rules, defaults, units, or billing effects.
- The enclosing OpenAPI `requestBody` is not marked `required: true`, and `CustomerConfigPayload` has no `required` array. In a supplied JSON object, `salesforce_account_id` is therefore the sole documented property but is not schema-required; it is a nullable string. Omitted-body, empty-object, omission of that property, and the operational meaning of null are not documented.
- `CustomerConfigPayload` declares no `additionalProperties` policy. The page therefore does not establish whether unknown fields are accepted, ignored, persisted, or rejected, and the generic phrase about billing parameters must not be treated as an open-ended runtime field contract.
- HTTP `200` has only the immediate response description `Success`; it supplies no response content schema or example and returns no documented customer/configuration representation, operation identifier, applied value, version, or propagation state. HTTP `400` uses an error object requiring string `message`, and HTTP `404` reuses that same error schema, but the page gives no error codes, examples, or field-to-error mapping.

## Material boundaries

- Current customer-read authorities separately expose `customer_config.salesforce_account_id`, while the dedicated billing-provider-configuration authority creates distinct customer configuration records selected later by contracts. This mutation page neither names nor returns a billing-provider configuration ID, so do not conflate its lightweight customer configuration with invoice-destination configuration or contract routing.
- Nullable `salesforce_account_id` is schema evidence that null is representable, not proof that null unlinks an account, that a non-null value is validated or unique, or that either value reaches Salesforce. The endpoint does not define reassignment, deletion, read-after-write visibility, synchronization cadence, propagation to reports or integrations, audit history, concurrency ordering, lost-update protection, atomicity, rollback, or recovery after partial or ambiguous failure.
- The separate API-wide [[source-metronome-api-reference-idempotency|`Idempotency-Key` authority]] applies to all POST endpoints: identical same-key parameters replay the original result, changed parameters return HTTP `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. This endpoint adds no no-key, another-key, expired-key, concurrent-mutation, cached-error-state, or recovery guarantee. Same-key replay recovers the original result; it is not a fresh read of customer configuration and does not prove Salesforce acceptance or propagation. After an ambiguous failure, investigate current state rather than assume that changing keys is safe.

## Raw-detail coverage map

- **Purpose and scope:** use the raw page for the complete configuration-versus-core-customer-data description and the page's external-system and billing-parameter examples.
- **Endpoint and identity:** use raw for the production server, bearer security declaration, Customers tag context, operation ID, exact POST path, required UUID customer path parameter, and request example.
- **Request schema:** use raw for the complete `CustomerConfigPayload`, nullable Salesforce property, absent request-body required marker, absent payload required list, and absent closed-object declaration.
- **Immediate responses and errors:** use raw for the sparse HTTP `200` description, HTTP `400` and `404` placement, shared `Error.message` schema, and the absence of a success body, error examples, or wider endpoint failure catalog.
- **Retry and adjacent authority:** use the linked idempotency source for API-wide POST replay and cached-error behavior; use customer get/list sources for the read representation, the Salesforce integration source for outbound sync, and the billing-provider-configuration source for invoice-destination records and contract selection.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-integrations]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-list-customers]], [[source-metronome-api-reference-customers-update-a-customer-name]], [[source-metronome-api-reference-customers-create-or-update-customer-ingest-aliases]], [[source-metronome-integrations-platform-integrations-sfdc-integration]], [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/update-a-customer-configuration-2026-07-13|2026-07-13 snapshot - customer configuration scope, endpoint, request schema, and immediate response boundaries]]