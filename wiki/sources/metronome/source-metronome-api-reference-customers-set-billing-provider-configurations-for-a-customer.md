---
title: "Metronome API Reference: Set Billing Provider Configurations for a Customer"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/api-reference/customers/set-billing-provider-configurations-for-a-customer"
original_format: webpage
raw_files:
  - "metronome/api-reference/customers/set-billing-provider-configurations-for-a-customer-2026-08-28.md"
tags: [metronome, customers, billing-providers, invoice-routing, integrations, api-reference]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/setCustomerBillingProviderConfigurations`, which inserts one or more billing-provider configurations for existing Metronome customers and returns customer-configuration records. The created configuration is only an available destination: a contract must later associate its own provider selector with the intended customer configuration before that configuration controls where invoices are delivered or payment is collected.

## Query-critical facts

- A supplied JSON payload requires immediate-parent `data`, an array of customer-configuration inputs; each input requires `billing_provider` and UUID `customer_id`. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is undocumented. Neither the wrapper nor input object declares `additionalProperties: false`, so unknown-field behavior is also undocumented.
- The endpoint creates additional configurations rather than replacing a customer's existing configuration. A customer can have multiple configurations, including multiple configurations for the same destination, and an upgrade or downgrade can create a configuration for a new system before a separate contract association changes routing. This operation does not update a contract, retire the prior configuration, or define an in-place replacement.
- `billing_provider` enumerates AWS Marketplace, Stripe, NetSuite, custom, Azure Marketplace, QuickBooks Online, Workday, GCP Marketplace, and Metronome. The nested `configuration` object explicitly allows arbitrary properties and depends on the provider and delivery-method combination; it defaults to an empty object, which the page says is invalid for most combinations. The examples are not provider-specific required-field schemas.
- Each input can name `delivery_method` or provide UUID `delivery_method_id`; each field's description requires the other when it is absent. Named methods are `direct_to_billing_provider`, `aws_sqs`, `tackle`, and `aws_sns`. The page specifically requires `delivery_method_id` when multiple Stripe accounts are connected, but does not define provider-method compatibility or validate that an account-level destination is ready.
- The returned configuration `id` is the customer billing-provider configuration identity used for later contract association. Keep it distinct from `customer_id`, the account-level `delivery_method_id`, provider-specific external customer identifiers inside `configuration`, and the downstream contract field `billing_provider_configuration_id` documented by related contract and integration sources. HTTP `200` requires a `data` array, but the referenced output item declares no required properties even though the prose identifies `id` as the key response field.
- Optional `unbillable_invoices_configuration` is a Stripe-only array of rules that can stop matching invoices from being sent. More-specific rules take precedence, and multiple rules with the same specificity make this method fail with HTTP `400`. The rule schema requires `invoice_type`, while the rule description says omitting it applies the rule to all invoices; preserve that unresolved intra-page conflict. `fiat_credit_type_id` narrows currency and is described as required when `max_amount` is set, while `max_amount` suppresses totals at or below a positive decimal threshold.

## Routing, provider, and replacement boundaries

The named delivery methods describe four Metronome-side routes: direct provider API delivery, Tackle for AWS Marketplace attribution and commission tracking, AWS SQS for custom processing, and AWS SNS for event-driven workflows. These descriptions establish configuration intent, not external-platform acceptance or complete provider behavior. The open `configuration` examples include Stripe customer and collection settings, AWS customer/product/region values, Azure subscription identity, GCP entitlement and service identity, and NetSuite customer identity, but the page does not make those examples closed schemas or document validation, normalization, credential ownership, or synchronization.

Creating a second destination does not itself switch an existing contract. Related contract authority uses the customer configuration's identity to select or schedule routing and defines when a draft or later-period invoice changes destination. This endpoint does not define effective timing, precedence among several customer configurations, archival or deletion, rollback, propagation to existing contracts or invoices, read-after-write visibility, or what happens when a configuration later becomes invalid.

## Response, failures, idempotency, and downstream authority

The operation lists HTTP `200`, generic HTTP `400`, and generic HTTP `500`; each error body requires only string `message`. Apart from the duplicate-rule-specific `400`, it does not map provider validation, missing or invalid conditional fields, unknown customer or delivery identifiers, authorization, partial batch success, duplicate configuration, atomicity, rate limits, or provider-side effects to outcomes. It also does not say whether several `data` entries commit atomically or in order.

The separate API-wide authority applies `Idempotency-Key` to all POST endpoints. Once a request begins executing after validation and concurrent-request conflict checks, identical same-key parameters replay the original result, changed parameters return HTTP `409`, keys persist for at least 24 hours, and the cached result can be HTTP `500`. That request-result replay is separate from the returned customer-configuration resource `id`. This endpoint adds no guarantee for another or expired key, concurrent mutations, partial batch recovery, duplicate resource prevention, read-after-write visibility, or provider-side deduplication and reconciliation. After a cached or ambiguous failure, investigate state rather than assume a changed key is safe.

A successful Metronome response establishes only the documented customer-configuration result. It does not prove that a contract selects the configuration, an invoice has been sent, SQS or SNS delivery occurred, Tackle or a marketplace accepted a transaction, Stripe or NetSuite accepted an invoice, payment or settlement completed, tax was correct, or downstream state reconciled.

## Raw-detail coverage map

- **Endpoint and envelopes:** production server, bearer security, operation ID, request wrapper, batch array, HTTP `200` array response, and generic HTTP `400` and `500` schemas are in the raw page.
- **Customer-configuration schema:** complete input and output properties, immediate-parent required lists, UUID formats, open provider-specific objects, tax-provider restriction, delivery-method alternatives, and all provider and delivery enums are in the raw page.
- **Provider examples:** complete Stripe, AWS, Azure, GCP, and NetSuite request examples and their provider-specific identifier values are in the raw page; they are examples rather than closed validation authority.
- **Invoice-suppression rules:** Stripe-only scope, rule precedence, duplicate-specificity failure, invoice types, currency selector, positive threshold semantics, examples, and the `invoice_type` requiredness conflict are in the raw page.
- **Retry authority:** API-wide same-key replay, conflicts, retention, cached errors, and investigation guidance are in the linked idempotency source and its immutable raw page, not in this endpoint's raw page.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-integrations]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]], [[source-metronome-api-reference-settings-list-account-level-billing-providers]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-integrations-invoice-integrations-netsuite]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/set-billing-provider-configurations-for-a-customer-2026-08-28|2026-08-28 snapshot - customer billing-provider configuration creation, routing identifiers, provider schemas, invoice-suppression rules, responses, and failure boundaries]]
