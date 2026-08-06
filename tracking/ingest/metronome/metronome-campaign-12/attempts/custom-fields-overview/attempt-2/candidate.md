---
title: "Metronome Custom Fields"
type: source
date_ingested: 2026-08-02
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/custom-fields"
raw_files:
  - "metronome/api-reference/custom-fields-2026-07-13.md"
tags: [metronome, api-reference, custom-fields, metadata, integrations]
---

## Overview

Metronome custom fields are properties added to platform objects to store metadata such as foreign keys and other descriptors. They provide context for Metronome data in external systems and can support business processes that depend on mapping Metronome entities to third-party entities.

## Key takeaways

- Custom fields can be added to customers, products, contracts, commits, credits, scheduled charges, rate cards, and alerts.
- The fields persist across the platform and can be fetched wherever the object appears in the Metronome app, API, and data export.
- Enforcing uniqueness is intended for one-to-one mappings and prevents reuse of the same value across objects, including archived objects.
- After a value is set on an object instance, it is returned with that object in the app, API calls, and data exports.

## Details

The overview frames custom fields as a way to preserve relationships between Metronome objects and records in external systems. Its examples attach an external customer identifier to a Metronome customer and a Stripe product identifier to a Metronome product.

Custom-field definitions and values can be managed through the Metronome app or API. The source cautions that uniqueness remains enforced for archived objects; resolving a duplicate involving an archived object requires resetting the archived object's field value.

The source also illustrates propagation in invoice data: a custom field on a product appears in the associated invoice line item, allowing the external product identifier to remain available in the invoice context.

## Scope and unknowns

This source is the Custom Fields overview. The five related endpoint raw pages below are navigation-only references: they were not read or summarized for this candidate, and they support no endpoint-specific claim here.

## Related

- Company: [[metronome]]
- Concept: [[metronome-custom-fields]]

## Related raw API references

- [[raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13|raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13.md]] — raw reference; not summarized
- [[raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13|raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md]] — raw reference; not summarized
- [[raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13|raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md]] — raw reference; not summarized
- [[raw/metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13|raw/metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13.md]] — raw reference; not summarized
- [[raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13|raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md]] — raw reference; not summarized

## Raw Sources

- [[raw/metronome/api-reference/custom-fields-2026-07-13|2026-07-13 snapshot — Metronome Custom Fields overview]]
