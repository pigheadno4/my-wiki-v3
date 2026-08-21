---
title: "List account-level billing providers"
type: source
date_ingested: 2026-08-21
canonical_url: "https://docs.metronome.com/api-reference/settings/list-account-level-billing-providers.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/settings/list-account-level-billing-providers-2026-07-13.md"
tags: [metronome, billing-providers, invoice-delivery, api]
---

## Overview

Metronome exposes `POST /v1/listConfiguredBillingProviders` to enumerate the billing providers and delivery-method configurations set up for an account. The read-only Settings operation returns identifiers and provider-specific settings intended to support mapping customer contracts to billing integrations; it does not itself create, change, or schedule a customer or contract mapping.

## Key takeaways

- The OpenAPI document applies HTTP bearer authentication to the operation. Although the operation uses `POST`, its documented behavior is enumeration rather than mutation.
- The JSON request body and its `next_page` property are not marked required. When supplied, `next_page` is a nullable UUID cursor for the next result page.
- A successful response requires `data`, an array whose entries require `billing_provider`, UUID `delivery_method_id`, `delivery_method`, and `delivery_method_configuration`; the top-level nullable UUID `next_page` is not marked required.
- The provider enum covers AWS Marketplace, Stripe, NetSuite, custom, Azure Marketplace, QuickBooks Online, Workday, GCP Marketplace, and Metronome. Delivery methods are direct provider delivery, AWS SQS, Tackle, or AWS SNS.
- Delivery-method configuration is deliberately open-ended and method-specific, and security-sensitive configuration may be omitted. Consumers therefore cannot treat the returned configuration object as a complete secret-bearing integration record.

## Request contract

The operation is `POST /v1/listConfiguredBillingProviders` with document-level bearer authentication. Its optional JSON object documents one property, `next_page`: a nullable, UUID-formatted cursor. The schema does not set `additionalProperties: false`, and the page does not define whether unrecognized request properties are accepted, ignored, or rejected. The page does not define page size, ordering, initial-page cursor conventions beyond omission or nullability, cursor expiry, or invalid-cursor behavior.

The page does not state bearer-token scope or role requirements. It also does not document authentication or authorization error responses, so the bearer scheme does not establish which tokens may enumerate configurations.

## Response contract

HTTP 200 requires a top-level `data` array. Every documented array item requires all four fields:

- `billing_provider`: one of `aws_marketplace`, `stripe`, `netsuite`, `custom`, `azure_marketplace`, `quickbooks_online`, `workday`, `gcp_marketplace`, or `metronome`.
- `delivery_method_id`: a UUID described as the delivery-method identifier to use for a customer.
- `delivery_method`: one of `direct_to_billing_provider`, `aws_sqs`, `tackle`, or `aws_sns`.
- `delivery_method_configuration`: an object allowing arbitrary properties whose structure depends on the delivery method; some values may be omitted for security reasons.

The optional nullable UUID `next_page` carries a continuation cursor. The examples show a Stripe direct-delivery configuration with account-level invoice-export flags and an AWS Marketplace direct-delivery configuration with AWS identity and region values. Those are examples, not a closed configuration schema or a guarantee that security-sensitive values will be returned.

## Contract-mapping and delivery boundaries

This endpoint inventories account-level provider delivery methods and exposes IDs and settings described as needed when mapping individual customer contracts to billing integrations. The item schema separately describes `delivery_method_id` as an ID used for a customer. The page does not reconcile those levels with the distinct customer billing-provider configuration and contract selector identifiers documented elsewhere, so callers must not substitute this account-level delivery-method ID for an unverified customer-configuration or contract-configuration ID.

The operation does not document configuration creation, customer provisioning, contract mutation, schedule changes, invoice routing at runtime, provider readiness, payment collection, tax, reconciliation, or delivery success. Enumeration of a configured provider is not evidence that a particular customer or contract currently selects it or that downstream delivery will succeed.

## Errors and explicit unknowns

The only operation-specific error response shown is HTTP 400 using a generic object that requires a string `message`. The page gives no error codes, error examples, field-level validation rules, or documented 401, 403, 404, 409, 429, or 5xx responses. It also leaves rate limits, retry guidance, idempotency relevance for this read-only POST, consistency during concurrent configuration changes, duplicate entries, and response ordering unspecified.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-customers-and-contracts]], [[metronome-invoicing]]
- Contract routing context: [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]]

## Raw Sources

- [[raw/metronome/api-reference/settings/list-account-level-billing-providers-2026-07-13|2026-07-13 snapshot - account-level provider and delivery-method enumeration]]
