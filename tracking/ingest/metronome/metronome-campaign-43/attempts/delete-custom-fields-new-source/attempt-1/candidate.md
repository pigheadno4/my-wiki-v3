---
title: "Metronome API Reference: Delete Custom Field Values"
type: source
date_ingested: 2026-09-10
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/custom-fields/delete-custom-fields"
raw_files:
  - "metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md"
tags: [metronome, api, custom-fields, metadata, deletion]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/customFields/deleteValues` operation for removing selected custom-field values from one Metronome entity instance. The caller selects the entity type, entity ID, and field keys; other custom fields on that entity are preserved.

## Scope and targeting

- This operation deletes values for the specified keys on one selected entity instance. It is not the separate operation that removes a custom-field key definition for every instance of an entity type, and it does not request deletion of all custom-field values on the selected instance.
- Within the supplied JSON object, `entity`, `entity_id`, and `keys` are required selectors. The exact managed-entity choices, UUID format, array shape, and example remain at the raw locators below.

> [!warning] Keep value deletion distinct from key-definition removal
> Use `deleteValues` when selected key values must be removed from one entity instance. The separately documented `removeKey` operation changes the key allowlist across an entity type and makes existing values under that key inaccessible; these operations have different targets and effects.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, then `paths` -> `/v1/customFields/deleteValues` -> `post`.
- **Target selectors:** the operation's `requestBody` -> `application/json` -> `schema` locates the required-property list and the `entity`, `entity_id`, and `keys` property definitions; `components.schemas.ManagedEntity` contains the exact entity choices.
- **Success boundary:** the operation's `responses` -> `200` documents `Success` without a response content schema.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-custom-fields]]
- Related operations: [[source-metronome-api-reference-custom-fields-set-custom-field-values]], [[source-metronome-api-reference-custom-fields-delete-a-custom-field-key]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13|Delete custom field values]] — complete collected documentation and embedded OpenAPI operation
