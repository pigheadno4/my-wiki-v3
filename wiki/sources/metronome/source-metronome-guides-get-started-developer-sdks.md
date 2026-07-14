---
title: "Metronome SDK Usage-Billing Walkthrough"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/guides/get-started/developer-sdks"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/developer-sdks-2026-07-13.md"
tags: [metronome, developer-sdks, usage-events, billable-metrics, contracts]
---

## Overview

This guide uses the Python, Node.js, Ruby, and Go SDKs to demonstrate one end-to-end usage-billing path: configure a client, ingest events, define a billable metric, create and match a customer, build a product and rate card, then create a contract whose draft invoice responds to usage. It is a practical introductory walkthrough, not an exhaustive API or lifecycle reference.

## Key takeaways

- The four SDKs provide typed endpoints and objects, pagination support, and configurable automatic retries; the documented default is up to three retries after request failures.
- An ingestion request can contain up to 100 events. `transaction_id` provides event-level deduplication, and timestamps may be up to 34 days in the past.
- A billable metric filters events and aggregates a property per customer using `SUM`, `COUNT`, or `MAX`; the guide says it matches only events sent after the metric is created.
- Ingest aliases let an application send usage before creating the corresponding Metronome customer, then associate the identifier during customer provisioning.
- Products control billable-metric presentation and quantity conversion, rate cards define prices and effective periods, and contracts apply those terms to customers for invoicing.

## Details

### SDK setup

| SDK | Installation command from the guide |
| --- | --- |
| Python | `pip install --pre metronome-sdk` |
| Node.js | `npm install @metronome/sdk` |
| Ruby | `gem install metronome-sdk` |
| Go | `go get -u 'github.com/Metronome-Industries/metronome-go'` |

Each client accepts an API-key bearer token and otherwise looks for `METRONOME_BEARER_TOKEN`. The linked SDK repositories are the deeper source for language-specific behavior and current examples.

### Event ingestion

The `/ingest` examples include `transaction_id`, `timestamp`, `customer_id`, `event_type`, and arbitrary `properties`. The guide permits 100 events per request, treats the transaction ID as the deduplication key, and permits timestamps up to 34 days old. An accepted event still needs both a matching metric and a matched customer before it affects billing.

### Billable metric

The example filters on event type and required properties, aggregates the `tokens` property with `SUM`, and groups by `user_id`. The guide also lists `COUNT` and `MAX`. A required property that is absent prevents the event from matching, and metric creation is not retroactive: the guide sends a new event after creating the metric.

### Customer association

The customer example registers `team@example.com` as an ingest alias. An alias can instead be an internal customer-table ID, allowing usage to flow before the Metronome customer record is provisioned. Once associated, the example's earlier customer event can contribute after invoicing is configured.

### Product and rate card

The example connects a usage product to the metric, groups invoice presentation by `user_id`, and divides token quantities by one million. The guide lists usage, fixed, composite, and subscription product types.

The rate card adds a flat, entitled rate with an effective start. `entitled=false` requires a contract-level override for invoice inclusion. The guide also lists tiered pricing, uses cents for USD prices, and describes `starting_at`/`ending_before` as the effective-period controls.

### Contract and draft invoice

A contract applies the rate card to the customer. It can use list prices directly or layer negotiated discounts and commitments over them. The guide says invoices are generated for billing periods after the contract start, current usage is visible on a draft invoice, and draft line items update seconds after ingestion.

### Example caveats

- The Ruby client is initialized as `metronome`, while later Ruby snippets call `client`; readers should normalize the client variable or consult the linked SDK repository.
- Python, Node.js, and Ruby create the sample contract at `2024-08-01`, while the Go snippet uses `2024-09-01`. Treat these as illustrative timestamps rather than language-specific contract behavior.
- The Node.js rate-card example creates through `client.V1.contracts` but adds a rate through `client.contracts` without `V1`; confirm the current namespace in the linked SDK repository.
- Python, Node.js, and Ruby pass `group_keys` when creating the example metric, while the Go snippet omits it even though the prose describes grouping by `user_id`.
- The page demonstrates one happy-path object chain. It does not establish complete SDK parity, error semantics, contract amendments, invoice-state transitions, or every field accepted by the referenced APIs.

## Change history

- 2026-07-14: Initial ingest from the 2026-07-13 collection snapshot; Sol added lifecycle boundaries and pricing details, then the independent pilot review added two more cross-language example caveats.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- Billing context: [[metronome-usage-based-billing]]
- Invoicing context: [[metronome-invoicing]]

## Raw Sources

- [[raw/metronome/guides/get-started/developer-sdks-2026-07-13|2026-07-13 snapshot - full SDK walkthrough and language examples]]
