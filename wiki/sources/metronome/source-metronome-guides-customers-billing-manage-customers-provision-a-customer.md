---
title: "Metronome Provision a Customer and Contract"
type: source
date_ingested: 2026-09-07
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/provision-a-customer"
raw_files:
  - "metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-08-28.md"
tags: [metronome, customers, contracts, ingest-aliases, billing-providers, usage-filters]
---

## Overview

This guide is an end-to-end entry point for provisioning a Metronome customer and the contracts that govern rating and billing. It helps locate the customer identity and ingest-alias workflow, billing-destination setup, contract terms, invoice consolidation, discounts, usage filters, and custom-field examples.

## Provisioning flow

A Metronome customer is an invoice recipient and may represent a user, enterprise, API key, or another organization-defined entity. Provisioning consists of creating that customer and configuring at least one contract before metering and rating begin; multiple contracts can be attached when the commercial model requires them.

Ingest aliases preserve an application's customer identifiers while routing usage to the matching Metronome customer. The guide also uses aliases to model enterprise sub-organizations and says that adding an alias later retroactively associates earlier usage carrying that alias.

A customer may hold multiple `customer_billing_provider_configurations`, while each contract selects the configuration for its billing destination. Creating an AWS configuration on the customer does not itself route billing to AWS: a contract must select it.

> [!warning] Beta billing-configuration archival
> The guide labels this behavior **BETA**. Archiving a billing configuration that is attached to an active contract immediately archives it on that contract and stops billing to the associated destination. The guide says a new billing-provider configuration cannot then be provisioned on that contract.

## Contract and invoice choices

Contracts build on rate cards and can include commits, scheduled charges, discounts, overrides, invoice schedules, and usage filters. Scheduled charges consolidate onto usage invoices only under the timing and invoice-finalization conditions documented in the raw section **Consolidate usage and scheduled invoices**.

Usage filters route selected usage among a customer's contracts and can be changed on a schedule.

> [!warning] Usage-filter compatibility
> Contract-level usage filters are not compatible with `LATEST` billable metrics; the guide warns that combining them can cause invoice computation errors.

## Raw detail map

Use the immutable raw snapshot for implementation detail and worked payloads; this guide is not a substitute for the dedicated API schema authorities.

- **Create a customer** — prerequisites, ingest-alias hierarchy and retroactive association, app steps, customer-creation API example, and custom fields.
- **Add a billing configuration to a customer** — connected-system prerequisite, AWS Marketplace example, later configuration, and archival behavior.
- **Provision a customer contract** — rate-card relationship, app flow, and the contract-create example with a prepaid commit, scheduled fee, and usage statement schedule.
- **Consolidate usage and scheduled invoices** — consolidation conditions and invoice-timing example.
- **Add contract discounts and overrides** — edit flow and multiplier-override example.
- **Create a usage filter** — multi-contract routing, scheduled filter update, streaming/SQL metric requirements, and the `LATEST` limitation.
- **Add custom fields** — downstream metadata example for CRM and revenue-recognition workflows.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-customers-and-contracts]]
- Navigation: [[metronome-event-ingestion]], [[metronome-integrations]], [[metronome-invoicing]], [[metronome-billable-metrics]]
- Dedicated authorities: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-08-28|2026-08-28 snapshot — customer and contract provisioning guide]]
