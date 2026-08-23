---
title: "Metronome API Reference: Set Up Account-Level Billing Provider"
type: source
date_ingested: 2026-08-23
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/settings/set-up-account-level-billing-provider.md"
raw_files:
  - "metronome/api-reference/settings/set-up-account-level-billing-provider-2026-07-13.md"
tags: [metronome, billing-providers, settings, api-reference, marketplaces, credentials]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/setUpBillingProvider`, which inserts an account-level billing-provider delivery configuration and returns a UUID `delivery_method_id`. The documented setup surface supports AWS Marketplace, Azure Marketplace, and GCP Marketplace, while leaving customer configuration and contract selection to separate workflows.

## Key takeaways

- The OpenAPI document applies HTTP bearer authentication to the operation. It does not define the token scope or role required to create account-level provider configuration.
- The enclosing `requestBody` is not marked required, while its JSON payload schema requires `billing_provider`, `delivery_method`, and `configuration`; omitted-body behavior is therefore undocumented.
- `billing_provider` is limited here to `aws_marketplace`, `azure_marketplace`, or `gcp_marketplace`. `delivery_method` is limited to `direct_to_billing_provider`, `aws_sqs`, or `aws_sns`; the page does not define which provider-method combinations are valid beyond its direct-delivery examples.
- `configuration` explicitly allows arbitrary properties and has no provider-specific required-property schema. Examples submit AWS identity values, an Azure client ID and raw client secret, or a GCP provider ID and raw workload-identity federation configuration, but examples do not establish validation requirements.
- HTTP `200` requires `data.delivery_method_id` as a UUID. The description says contracts across customers can later be mapped to the account-level configuration with that identifier, but this operation does not identify or mutate a customer or contract.

## Endpoint and request contract

The production operation is `POST /v1/setUpBillingProvider` with operation ID `setUpBillingProvider-v1` under the OpenAPI document's HTTP bearer scheme. The operation has no path or query parameters. The `requestBody` describes JSON billing-provider, delivery-method, and configuration data, but does not declare `required: true`; inside the payload object, all three named properties are required. The top-level payload schema does not set `additionalProperties: false`, so the page does not state whether undocumented top-level properties are accepted, ignored, or rejected.

`billing_provider` enumerates only AWS Marketplace, Azure Marketplace, and GCP Marketplace. This is narrower than the separate account-level listing endpoint's broader provider enum, so this setup page is not evidence that every listed provider can be created through this operation. `delivery_method` enumerates direct provider delivery, AWS SQS, and AWS SNS. All three examples use `direct_to_billing_provider`; the source does not document compatibility rules for SQS or SNS, provider-specific validation, or whether duplicate configurations are allowed.

## Provider configuration and credential boundary

The required `configuration` property is an object with `additionalProperties: true`. Its structure depends on the billing-provider and delivery-method combination, but the page provides no closed schema, property types, required-property lists, mutual-exclusion rules, or unknown-field behavior within that object beyond permitting arbitrary properties.

The AWS example sends `aws_external_id` and `aws_iam_role_arn`. The Azure example sends `azure_client_id`, `raw_azure_client_secret`, and `azure_tenant_id`. The GCP example sends `gcp_provider_id` and `raw_gcp_workload_identity_federation_config`. These examples establish that callers may submit provider identity and secret-bearing material; they do not define who must create or rotate those credentials, how Metronome stores, encrypts, validates, redacts, or deletes them, whether a secret can be updated independently, or whether values are forwarded to an external provider during setup. The separate listing reference says security-sensitive configuration may be omitted from list responses, but this setup page does not define its own response exposure or a credential-retrieval contract.

## Account, customer, and contract boundaries

This operation creates account-level configuration and returns a delivery-method identifier. It does not accept a Metronome `customer_id`, a customer billing-provider configuration ID, or a contract ID, and it does not create a customer-level billing destination or select one on a contract. Existing customer-provisioning and Stripe-integration sources separately describe using `delivery_method_id` when creating a customer billing-provider configuration and using `billing_provider_configuration_id` when a contract selects among that customer's configurations. The setup page's statement that contracts across customers can be mapped with the returned ID does not reconcile those identifier layers, so implementations should verify the downstream customer and contract schemas instead of substituting one identifier for another.

The source does not document when the new configuration becomes usable, whether the external provider is contacted or validated synchronously, how to confirm readiness, how the record appears in account-level listing, or how changes propagate to existing customers or contracts. It also defines no update, rotation, archive, delete, rollback, or reconciliation operation. A successful setup response therefore proves issuance of a `delivery_method_id`, not that any customer or contract currently selects it or that invoice delivery, marketplace metering, payment, tax, or downstream reconciliation will succeed.

## Response, errors, idempotency, and recovery

HTTP `200` requires a top-level `data` object, which requires only UUID-formatted string `delivery_method_id`. The page does not return the normalized provider, delivery method, configuration, creation status, readiness state, timestamps, or an external-provider identifier. It also does not state whether success is durable and immediately readable or whether later reconciliation can fail.

HTTP `400` and HTTP `409` both use a generic error object requiring string `message`. No error codes or examples identify validation failures, invalid provider-method combinations, duplicate configuration, credential rejection, authorization, or which conflict condition produced `409`. The page does not document partial creation, atomicity, timeout recovery, concurrent setup ordering, rate limits, or safe cleanup after an uncertain outcome.

The separate API-wide idempotency authority applies `Idempotency-Key` to all POST endpoints: identical parameters with the same key return the original result, changed parameters conflict with HTTP `409`, keys persist for at least 24 hours, and results cached after execution can include HTTP `500`. This endpoint does not add any endpoint-specific retry, concurrency, provider-side deduplication, or recovery guarantee. After an ambiguous failure, reuse the same key and parameters within the documented window and investigate state before changing keys; do not infer that a new key is safe or that the external-provider side is reconciled.

No contradiction was found when account-level setup, customer-level configuration, contract selection, and invoice-delivery outcomes are kept as separate lifecycle stages.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]], [[metronome-security-principles]]
- Related sources: [[source-metronome-api-reference-settings-list-account-level-billing-providers]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/settings/set-up-account-level-billing-provider-2026-07-13|2026-07-13 snapshot — account-level billing-provider setup endpoint and embedded OpenAPI schema]]