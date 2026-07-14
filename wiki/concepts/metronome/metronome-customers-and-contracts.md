---
title: "Metronome Customers and Contracts"
type: concept
category: technology
tags: [metronome, customers, contracts, invoicing]
---

## Definition

Metronome customers are the billing entities to which usage is attributed. Contracts represent the commercial terms a customer has agreed to pay, generally starting from a rate card with optional negotiated discounts or commitments layered on top.

## Customer matching

An ingest alias associates an application-defined identifier with a Metronome customer. The SDK guide recommends this pattern when usage starts before the customer exists in Metronome: send the application's customer-table ID in events, then register it as an alias when provisioning the customer.

## Contract and invoice behavior

- A basic contract can apply predefined list prices from a rate card.
- Contract-level terms can add negotiated discounts or commitments.
- The contract `starting_at` time determines the billing periods for which invoices are generated.
- Current-period usage appears on a draft invoice, and the guide says its line items update seconds after Metronome receives usage data.

This introductory source does not define the full contract schema, amendment lifecycle, or invoice-state machine; those require dedicated contract and invoicing references.

## Contract creation API

`POST /v1/contracts/create` requires only `customer_id` and `starting_at` at the top level. Optional structures can apply a rate card or package, commits and credits, overrides, scheduled charges, subscriptions, usage routing, thresholds, provider configuration, and hierarchy behavior.

Important creation constraints include:

- `starting_at` is inclusive and `ending_before` is exclusive.
- `package_id` invokes a restricted package-provisioning mode in which only the documented small field subset is accepted; `package_alias` is mutually exclusive with `package_id`.
- Subscription quantity requirements depend on `quantity_management_mode`: quantity-only needs `initial_quantity`, while seat-based needs `seat_config`.
- `uniqueness_key` can prevent duplicate creation; its schema says reuse fails with HTTP 409.
- The scheduled-charge consolidation setting cannot be changed after the contract is created.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — customer aliases, basic contract provisioning, and introductory invoice behavior
- [[source-metronome-api-reference-contracts-create-a-contract]] — create endpoint, request families, conditional requirements, and response boundary

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-invoicing]]
