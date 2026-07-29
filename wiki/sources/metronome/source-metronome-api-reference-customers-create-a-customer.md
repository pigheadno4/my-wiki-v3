---
title: "Metronome API Reference: Create a Customer"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/create-a-customer"
raw_files:
  - "metronome/api-reference/customers/create-a-customer-2026-07-13.md"
tags: [metronome, customers, contracts, event-ingestion, billing-integrations]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/customers`, which creates a Metronome customer and can attach billing-provider or revenue-system configuration during provisioning. It connects customer identity used for usage-event matching with the downstream systems that receive invoices or collect payment.

## Key takeaways

- Metronome recommends creating the customer first in the downstream payment or ERP system when collecting a payment method, then using that system's customer identifier when creating the Metronome customer.
- `name` is the only unconditionally required top-level request field; names longer than 160 characters are truncated.
- `ingest_aliases` map usage events to the customer. The schema allows up to 2,000 aliases, each from 1 to 128 characters, and deprecates `external_id` in favor of aliases.
- Billing-provider configuration is optional at customer creation and can be added later, but each supplied configuration requires `billing_provider`; its provider-specific `configuration` object cannot generally be assumed valid when empty.
- After customer creation, a contract must use the intended customer billing configuration because one customer can have multiple configurations.

## Provisioning flow

The endpoint supports customers originating in either a product-led application workflow or a sales-led system. The guide recommends provisioning the downstream payment or ERP customer first when payment details are collected, creating the Metronome customer with the downstream response, setting an ingest alias so usage maps correctly, and then creating a contract. Billing configuration can be supplied during customer creation or added later.

## Request schema

`LegacyCreateCustomerPayload` requires `name`. It also accepts `ingest_aliases`, `customer_billing_provider_configurations`, `customer_revenue_system_configurations`, and customer `custom_fields`. The legacy `external_id` field is deprecated in favor of `ingest_aliases`.

The documented alias limits are 2,000 items, with each alias containing 1 to 128 characters. The customer name is truncated to 160 characters when longer. Custom fields are an object whose values are strings.

The OpenAPI `requestBody` object does not declare `required: true`. The page therefore does not explicitly document behavior when the body is omitted, even though `name` is required inside the payload schema.

## Billing and revenue-system configuration

A customer billing-provider configuration requires `billing_provider`. Enumerated billing providers are AWS Marketplace, Azure Marketplace, GCP Marketplace, Stripe, and NetSuite. The configuration may identify a delivery method directly or by UUID; the field descriptions say that when one is absent the other must be provided. Supported delivery-method values are `direct_to_billing_provider`, `aws_sqs`, `tackle`, and `aws_sns`.

The optional tax provider is enumerated as Anrok, Avalara, or Stripe. Its description limits tax calculation through Stripe to configurations using `auto_charge_payment_intent` or `manual_charge_payment_intent` collection methods. The provider-specific `configuration` object is open-ended, and the reference warns that its empty-object default is invalid for most billing-provider and delivery-method combinations.

The revenue-system configuration is marked with a revenue-recognition feature flag in the schema. It enumerates NetSuite as the provider, expects `netsuite_customer_id` in the provider-specific configuration, and supports direct delivery or a delivery-method UUID.

## Response and documented boundaries

A successful request returns HTTP `200` with a `Customer` object under `data`, including the Metronome UUID in `data.id`, aliases, name, and the deprecated `external_id`. The narrative calls the created identifier `customer_id`, whereas the OpenAPI schema and example expose it as `data.id`; implementations should follow the actual response contract and verify this naming boundary.

The reference also documents HTTP 409 when a customer with the requested ID already exists, but the request schema has no dedicated customer-ID field. It does not identify whether the conflict is keyed by an ingest alias or deprecated `external_id`, nor does it document retry behavior for this endpoint.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-integrations]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-integrations-invoice-integrations-stripe]]

## Raw Sources

- [[raw/metronome/api-reference/customers/create-a-customer-2026-07-13|2026-07-13 snapshot — customer provisioning and embedded OpenAPI schema]]
