---
title: "Metronome List Custom Field Keys API"
type: source
date_ingested: 2026-09-01
canonical_url: "https://docs.metronome.com/api-reference/custom-fields/list-custom-field-keys"
original_format: webpage
raw_files:
  - "metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13.md"
tags: [metronome, api-reference, custom-fields, pagination, idempotency, reporting]
---

## Overview

This reference documents bearer-authenticated `POST /v1/customFields/listKeys`, which retrieves active custom-field key definitions across the organization and can filter them by managed entity type. It is the dedicated discovery and configuration-audit authority for available keys; creating or removing definitions and setting or deleting entity values remain separate operations.

## Query-critical facts

- The operation uses the production API server and bearer authentication. Its only endpoint-local pagination input is optional query parameter `next_page`; it defines no `limit` parameter or page-size default.
- A supplied JSON object may contain optional `entities`, an array of `ManagedEntity` values used to restrict which entity types' keys are returned. The enclosing `requestBody` is not marked required, the object has no required-property list, and it does not declare `additionalProperties: false`; omitted-body and unknown-field runtime behavior are therefore undocumented.
- HTTP `200` requires top-level sibling fields `data` and nullable `next_page`. Each `data` item requires `entity`, string `key`, and boolean `enforce_uniqueness`. The response is a key-definition inventory: it contains no entity instance, assigned value, duplicate-value count, activation timestamp, mutation result, or downstream propagation status.
- `ManagedEntity` is a 19-value enum shared by the request filter and each result item; the complete catalog and the client-specific `professional_service` annotation remain in the raw snapshot. The separate custom-fields overview names a narrower set of eight supported entity examples, and these authorities do not explain whether the prose list is illustrative or how labels such as `product` versus `contract_product` and `credit` versus `contract_credit` relate.
- The separate API-wide `Idempotency-Key` authority applies to all POST endpoints. After execution admission, identical same-key parameters replay the persisted original result, while changed parameters return HTTP `409`; advancing `next_page` or changing the entity filter changes parameters. Replay is not proof of a fresh active-key inventory or a new stable pagination snapshot, and this endpoint adds no local key, cursor, cache, retry, concurrency, or recovery policy.

## Material boundaries and contradictions

- The narrative says the endpoint retrieves all active keys and supports configuration audits, but it does not define active-state timing, ordering, total count, page size, cursor lifetime, filter binding, snapshot consistency, duplicate-or-skip behavior while definitions change, or read-after-create/remove visibility. Complete traversal therefore requires the separate pagination convention and still does not prove an immutable point-in-time inventory.
- `enforce_uniqueness` reports how the key is configured; this page does not define the comparison scope or prove that current entity values are unique. Use the dedicated custom-fields overview and create-key authority for documented uniqueness meaning, and the value-mutation authorities for assignment behavior.
- Listing definitions is not mutation authority. A returned key does not show that a value has been set, exported, copied to an invoice, evaluated by an alert, or reconciled with an external system; absence from a filtered or replayed page is not by itself proof that the key was removed.

## Raw-detail coverage map

Use the exact raw snapshot for the production server and bearer declaration; `POST /v1/customFields/listKeys` identity and operation ID; active-key and audit narrative; optional `entities` body example; complete 19-value `ManagedEntity` enum and `professional_service` annotation; required response-envelope and item fields; nullable sibling `next_page`; response example; and the absent body-required marker, required payload properties, closed-object declaration, `limit`, ordering, totals, error responses, freshness, and consistency guarantees. Use the dedicated pagination source for repeat-until-null traversal, the idempotency source for API-wide POST replay, and dedicated create, remove, set-value, and delete-value authorities for mutations and lifecycle behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-custom-fields]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]], [[source-metronome-api-reference-custom-fields-delete-a-custom-field-key]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13|2026-07-13 snapshot - active-key scope, entity filtering, response placement, managed-entity catalog, pagination, and discovery boundaries]]