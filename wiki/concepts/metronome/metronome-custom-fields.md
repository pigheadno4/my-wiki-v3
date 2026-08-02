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

## Uniqueness

Uniqueness is intended for foreign entities that have a one-to-one relationship with a Metronome object. Enforcement continues for archived objects; resolving a duplicate involving an archived object requires resetting that object's field value.

## Invoice propagation

A Product custom field can propagate to the associated invoice line item. The overview's `stripe_product_id` example uses this propagation to link an invoice line item to a Stripe product when creating invoices in Stripe.

## Limits of the overview

The overview establishes the purpose, supported object examples, persistence, uniqueness, and invoice-line propagation of custom fields. It does not establish endpoint methods, request or response schemas, or endpoint-specific behavior; those details require complete reads of the relevant API references.

## Sources

- [[source-metronome-api-reference-custom-fields]] — overview, supported entity scope, persistence, uniqueness, and product-to-invoice-line propagation

## Related

- [[metronome-integrations]]
- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-reporting-and-analytics]]
