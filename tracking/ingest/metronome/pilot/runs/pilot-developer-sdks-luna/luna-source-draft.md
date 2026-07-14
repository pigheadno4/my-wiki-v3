---
title: "Build with the Metronome SDKs"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/guides/get-started/developer-sdks"
original_format: webpage
raw_files:
  - "metronome/guides/get-started/developer-sdks-2026-07-13.md"
tags: [metronome, developer-sdks, usage-based-billing, api-integration, python, go, ruby, nodejs]
---

## Overview

This guide introduces Metronome SDKs for Python, Go, Ruby, and Node.js and walks through a usage-based billing setup. The workflow covers SDK installation and configuration, usage-event ingestion, billable-metric creation, customer association, pricing and packaging, and contract creation. It also describes strong typing, pagination, and automatic retries, including a default of up to three retries per failed request.

## Key takeaways

- Metronome provides SDKs for Python, Go, Ruby, and Node.js.
- The guide presents a six-step flow from SDK setup through contract creation for usage-based billing.
- SDK repositories include documentation, examples, and resources; listed core features are strong typing, pagination support, and automatic retry support.
- By default, the SDK looks for the bearer token in the `METRONOME_BEARER_TOKEN` environment variable, although the examples pass a token to the constructor.
- Usage requests can contain up to 100 events, and `transaction_id` is used for event deduplication.

## Details

### SDK installation and configuration

- The Python installation command is `pip install --pre metronome-sdk`.
- The Node.js installation command is `npm install @metronome/sdk`.
- The Ruby installation command is `gem install metronome-sdk`.
- The Go installation command is `go get -u 'github.com/Metronome-Industries/metronome-go'`.
- The guide says the SDK uses `METRONOME_BEARER_TOKEN` by default for the API key bearer token.

### SDK features

- The page links to Python, Go, Ruby, and Node.js SDK repositories.
- The listed core features are strong typing of endpoints and objects, pagination support, and automatic retry support.
- Automatic retry support retries each request upon failure up to three times by default and can be configured to any number of retries.

### Usage-based billing workflow

- The guide covers sending usage events, creating a billable metric, creating a customer, setting up pricing and packaging, and creating a customer contract.
- Metronome accepts usage payloads of all formats through the `/ingest` endpoint.
- A billable metric describes a per-customer aggregation over a subset of usage events.
- Supported billable-metric aggregation operations include `SUM`, `COUNT`, and `MAX`.
- Ingest aliases can match a Metronome customer against a usage event and can use an application customer-table ID before the customer is created in Metronome.
- Products, rate cards, and contracts are used in the guide's pricing and invoicing setup.
- Line items on draft invoices update seconds after Metronome receives usage data.

## Change history

- 2026-07-14: Luna pilot draft from the assigned raw snapshot.

## Related

- Company: [[metronome]]
- Concepts: coordinator concept audit required before promotion.

## Raw Sources

- [[raw/metronome/guides/get-started/developer-sdks-2026-07-13|2026-07-13 snapshot]]
