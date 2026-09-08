---
title: "Metronome API: Fetch Billing Provider Configurations for a Customer"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/fetch-billing-provider-configurations-for-a-customer"
raw_files:
  - "metronome/api-reference/customers/fetch-billing-provider-configurations-for-a-customer-2026-08-28.md"
tags: [metronome, api-reference, customers, billing-providers, contract-provisioning]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/getCustomerBillingProviderConfigurations`, which retrieves billing-provider configurations previously set for one Metronome customer. Its central provisioning use is to obtain the configuration `id` that can be supplied as `billing_provider_configuration_id` when creating a contract.

## Retrieval boundary

A supplied JSON object requires UUID `customer_id` and may set `include_archived`; the OpenAPI `requestBody` itself is not marked required, and no default is documented for `include_archived`. A successful `200` response places an array of `CustomerBillingProviderConfiguration` objects directly under required top-level `data`. Each returned object requires its configuration ID, provider, customer ID, provider-specific configuration, delivery method and delivery configuration, nullable `archived_at`, and delivery-method ID.

> [!warning] Do not treat every returned configuration as a currently usable route
> Inspect `archived_at` and choose the intended configuration before contract provisioning; this page does not define the default archived-record scope or prove that any contract currently selects the configuration. A returned configuration can also carry Beta, Stripe-only `unbillable_invoices_configuration` rules that stop matching invoices from being sent; when that field is omitted, the page says every invoice is sent to the billing provider.

## Raw detail locators

- Method, path, operation ID, bearer authentication, request media type, required `customer_id`, optional `include_archived`, and the request example: OpenAPI `security` and `paths./v1/getCustomerBillingProviderConfigurations.post`.
- Success envelope, complete example, and generic `400` error: `paths./v1/getCustomerBillingProviderConfigurations.post.responses`.
- Returned configuration identity, provider-specific open configuration, delivery routing, archive timestamp, and all required response fields: `components.schemas.CustomerBillingProviderConfiguration`.
- Provider and delivery-method values: `components.schemas.BillingProviderType` and `components.schemas.BillingProviderDeliveryMethodType`.
- Beta Stripe-only invoice-suppression behavior, precedence, specificity failure, invoice types, currency selector, and amount threshold: `components.schemas.CustomerBillingProviderConfiguration.properties.unbillable_invoices_configuration` and `components.schemas.UnbillableInvoiceRule`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/customers/fetch-billing-provider-configurations-for-a-customer-2026-08-28|2026-08-28 snapshot - customer billing-provider configuration lookup, contract selector identity, response schema, and Stripe suppression-rule details]]
