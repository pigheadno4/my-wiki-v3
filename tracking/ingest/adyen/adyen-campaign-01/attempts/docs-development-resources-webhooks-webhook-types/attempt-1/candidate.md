---
title: "Adyen Webhook Structure and Types"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/webhook-types"
raw_files:
  - "adyen/docs/development-resources/webhooks/webhook-types/2026-09-15.md"
tags: [adyen, webhooks, payments, platforms, event-types]
---

## Overview

This [[adyen]] documentation page is a catalog of webhook structures, selectable webhook types, and their event scopes. It separates Payments webhooks from Platforms webhooks and routes detailed event-code, security-method, and product-specific webhook questions to the tables in the complete raw snapshot.

## Key takeaways

- Every webhook message has an event type that merchant or platform server logic can use to identify the information received. Payments webhooks typically expose it in `eventCode`; Platforms webhooks typically expose it in `type`.
- For most payment integrations, the page directs merchants to Standard webhooks. Standard webhooks combine default event types that cannot be disabled with non-default event types enabled through the Standard webhook, Webhooks settings, or Risk settings surfaces described on the page.
- Adyen warns that it can add webhook and event types. Receivers should accept more webhook types and event values than the captured list, while adding explicit business logic before using newly introduced events.
- Other Payments webhook types use separate endpoints, and each configured endpoint can receive only one such webhook type. Their purposes and listed authentication methods vary; use the raw table rather than assuming Standard-webhook structure or security applies to every type.
- Platforms webhooks use an event-specific `data` object plus `environment`, `timestamp`, and `type`, then divide events by product purpose such as authentication, balances, Capital, card orders, configuration, disputes, managed risk, network tokens, reporting, transactions, and transfers.

> [!warning] Event coverage is configuration-dependent
> The webhook types and event values received depend on webhook configuration. The captured Standard catalog is not exhaustive over time, and the page explicitly says no webhook event is sent when a payment is settled. Do not infer settlement confirmation, current product eligibility, or successful processing from this catalog alone.

## Detail locators

- Page purpose and the Payments/Platforms split: `# Webhook structure and types`, lines 17-24.
- Event identity and the `eventCode` versus `type` distinction: `## Event types`, lines 28-35.
- Payments payload envelope and event-dependent fields: `### Payments webhook structure`, lines 41-128.
- Standard default transaction, dispute, and payout event catalogs: `### Default event types`, lines 134-203; the settlement warning is at line 170.
- Non-default enablement surfaces and their event tables: `### Non-default event codes`, lines 205-262.
- Separate endpoint constraint and other Payments webhook-type catalog: `### Other webhooks`, lines 266-295.
- Platforms payload envelope and event-field definitions: `### Platforms webhook structure`, lines 299-320.
- Product-specific Platforms webhook purposes and event tables: `## Platforms webhooks`, lines 322-504.

The tables are snapshot evidence, not proof that every listed webhook is currently available to a particular account, region, integration, or environment. Linked pages and API Explorer entries are navigation unless separately retained and read.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/webhook-types/2026-09-15|Adyen webhook structure and types]] - complete collected catalog of Payments and Platforms webhook structures, types, event scopes, and warnings
