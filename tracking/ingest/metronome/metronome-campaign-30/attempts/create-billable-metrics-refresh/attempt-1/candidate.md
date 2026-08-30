---
title: "Metronome Create Billable Metrics"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/create-billable-metrics"
original_format: webpage
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-08-28.md"
  - "metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-07-13.md"
tags: [metronome, billable-metrics, usage-based-billing, metering]
---

## Overview

This implementation guide defines a billable metric as the query that filters and aggregates usage events into invoice-line quantities and alert inputs. It explains the operator's design and testing decisions, Metronome's metric-processing role, and the boundaries among metrics, products, rate cards, contracts, and customers; dedicated API references remain authoritative for endpoint schemas.

## Query-critical facts

- The merchant or implementer chooses the usage components to price, the calculation scale and latency, group keys, filters, and aggregation strategy. Metronome's ingestion pipeline continuously applies the resulting metric definition to incoming usage; the computed quantity can feed invoice line items and alerts.
- A billable metric supplies quantity, a product supplies invoice-line presentation, a rate card defines product list prices, and a customer contract can associate or overwrite rates and generate invoices. These are separate configuration roles, so defining a metric alone does not establish a price, contract, invoice, or collection outcome.
- Streaming metrics are for simple-filter, high-throughput and low-latency workflows and support `COUNT`, `SUM`, `MAX`, and `LATEST`; `LATEST` takes the most recent property value within the billing period. SQL metrics support calculations outside the basic-filter model, including distinct counts. The guide gives no numeric throughput, latency, or availability guarantee.
- `LATEST` metrics can use group keys but currently cannot use contract-level usage filters. This guide-level compatibility statement does not supply the contract usage-filter schema or validation behavior.
- A streaming metric must exist before incoming usage is attributed to it by default. Metronome says it retains raw events and can perform a support-requested reflow so earlier events apply to a new streaming metric, but the guide does not define reflow eligibility, timing, cost, completeness, or service guarantees.
- Group keys are metric-layer properties used downstream for invoice presentation or dimensional pricing. A product that needs both kinds must combine every property in one compound metric group key. For streaming metrics, a group-key property must first use an `Exists` or `In` property filter, and group keys cannot be edited after metric creation. Customer-level cardinality approaching one thousand values is a reason to consult Metronome because API latency can increase, not a documented hard limit.
- The operator tests a created metric by ingesting events and then searching for their `transaction_ids`; the search response can expose the matched metric and, when present, customer. This checks those test-event matches, not invoice finalization, payment collection, or complete production-event coverage.

## Material boundaries and contradictions

> [!warning] Forward attribution and assisted reflow
> The related event-design source says new metrics cannot be applied retroactively, while this guide documents a support-requested reflow for retained earlier events. Treat forward-only attribution as the default and reflow as an assisted exception whose operating guarantees are not documented. [[source-metronome-guides-events-design-usage-events]]

> [!warning] Streaming aggregation authority
> This guide lists four streaming aggregations and routes distinct counts to SQL, while the dedicated create endpoint also enumerates `UNIQUE` without defining its semantics. Preserve the conflict: the guide is metric-design authority, and the endpoint reference is request-schema authority; neither proves how the other wording is normalized at runtime. [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]]

The guide does not provide complete create-metric, ingest, or event-search request and response schemas; body requiredness, field validation, errors, retries, and consistency remain with the dedicated endpoint references. Its worked pricing and SQL examples illustrate configuration choices and are routed to raw rather than treated as universal invoice or query semantics.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Purpose, actors, and data flow | Metric definition, ingestion-pipeline processing, invoice quantity and alert roles, operator design steps, and product/rate-card/contract/customer responsibility split |
| Metric modes | Streaming selection criteria, four guide-listed aggregations, `LATEST` meaning and usage-filter restriction, SQL selection criteria, distinct-count direction, and alerting guidance |
| Attribution lifecycle | Forward-only default for new streaming metrics, retained raw events, support-portal reflow route, and undocumented reflow guarantees |
| Group-key configuration | Presentation and pricing roles, compound keys, cardinality consultation, streaming property-filter prerequisite and immutability, SQL output-column grouping, and complete worked examples |
| Editors and testing | Basic Filters versus SQL Editor classification, ingest-to-search test sequence, transaction-ID lookup, and matched metric/customer diagnostics |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-events-design-usage-events]], [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-usage-search-events]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-08-28|2026-08-28 snapshot - metric actors, design flow, streaming and SQL boundaries, group-key configuration, support-requested reflow, and matching test]]
- [[raw/metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-07-13|2026-07-13 snapshot - prior metric design, group-key, reflow, and testing guidance]]
