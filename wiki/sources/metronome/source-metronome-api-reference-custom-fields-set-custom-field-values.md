---
title: "Metronome API Reference: Set Custom Field Values"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/custom-fields/set-custom-field-values"
raw_files:
  - "metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md"
tags: [metronome, api, custom-fields, metadata]
---

## Overview

This Metronome API reference documents the bearer-authenticated `POST /v1/customFields/setValues` operation for setting custom-field values on one entity instance. It is a value-mutation operation, not an operation for defining or removing custom-field keys.

## Key takeaways

- Values supplied for matching keys overwrite their existing values, while other custom fields on the entity are preserved.
- The update is transactional: either all submitted values are set or none are.
- Each custom-field value is limited to 200 characters.

## Operation and detail routes

The exact JSON payload requirements, managed-entity choices, example body, arbitrary-key string map shape, and bearer security definition are in the raw OpenAPI block under `paths./v1/customFields/setValues.post`, `components.schemas.ManagedEntity`, `components.schemas.CustomField`, and `components.securitySchemes.bearerAuth`. The payload schema identifies required properties within a supplied object, but the enclosing OpenAPI `requestBody` is not marked required; do not infer omitted-body behavior. The response section documents HTTP `200` as `Success` without a response content schema, so it does not establish a returned entity or value inventory.

## Related

- Company: [[metronome]]
- Concept: [[metronome-custom-fields]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13|Set custom field values]] — complete endpoint reference and OpenAPI schema
