---
title: "Metronome Provision a Customer"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/provision-customer"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/provision-customer-2026-07-13.md"
tags: [metronome, customers, contracts, ingest-aliases, billing-integrations, marketplaces]
---

## Overview

This guide provisions a customer as an invoice recipient, including ingest aliases and optional billing-provider configurations. A customer needs at least one contract before rating starts; customer creation is distinct from the contract that selects the billing destination.

## Identity and aliases

An ingest alias maps an internal identifier to a Metronome customer ID, allowing producers to retain their own customer keys. Aliases can also represent enterprise sub-organizations under one Metronome customer, with group keys controlling invoice presentation.

Aliases can be supplied at customer creation or later. The page says a late alias assignment retroactively associates usage already sent with that alias, allowing customer creation to leave the signup hot path.

The app flow collects name, alias, and optional custom fields. The API example stores an SFDC account identifier; sales-led and product-led flows can trigger creation from opportunity close or website signup.

## Billing configuration and contract assignment

A `customer_billing_provider_configuration` is a customer-level billing-destination record. A customer can have several, while each contract selects one configuration and therefore one configured system. The external billing system must be connected before its customer configuration is set up.

The AWS example supplies marketplace customer ID, product code, region, and direct-provider delivery. Creating this configuration on the customer does not begin AWS billing; a contract must select it as `billing_provider_configuration`. The `/setCustomerBillingProviderConfigurations` endpoint can add a configuration later.

Metronome recommends setting customer billing-provider configurations during customer creation, although the documented set endpoint can add one later.

> [!warning] Beta archival boundary
> A configuration can be archived with its customer or directly. It then becomes reusable on another customer. If attached to an active contract, archival immediately removes it from that contract and stops billing to the destination. The page says a replacement configuration cannot then be provisioned on that contract.

## Documentation boundaries

This guide does not define the full customer request or response schema, required fields, alias limits, authentication, idempotency, validation errors, non-AWS provider schemas, contract request shape, or invoice lifecycle. Dedicated API and integration references remain authoritative.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-integrations]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/provision-customer-2026-07-13|2026-07-13 snapshot — customer provisioning, aliases, and billing configuration]]
