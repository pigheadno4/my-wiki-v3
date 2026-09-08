---
title: "Metronome API: Upsert Avalara Credentials"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/settings/upsert-avalara-credentials"
raw_files:
  - "metronome/api-reference/settings/upsert-avalara-credentials-2026-07-13.md"
tags: [metronome, avalara, plg-invoicing, billing-integrations]
---

## Overview

This Metronome Settings API reference documents the bearer-authenticated `POST /v1/upsertAvalaraCredentials` operation. It maps Avalara account credentials to billing-provider delivery methods and limits their documented use to PLG Invoicing.

## Key takeaways

- Supply `delivery_method_ids` obtained from `/listConfiguredBillingProviders`; Metronome uses the selected delivery methods to map the credentials to the appropriate billing entity.
- The JSON object schema requires `delivery_method_ids`, `avalara_environment`, `avalara_username`, and `avalara_password`. `avalara_environment` accepts `PRODUCTION` or `SANDBOX`.
- `commit_transactions` is an optional boolean in this endpoint schema; its description routes readers to whether Metronome tax calculations are committed for reporting and tax filings.
- The endpoint is documented only for PLG Invoicing at this snapshot. This page does not establish that the credential flow is the same as the separate Stripe-hosted Avalara tax-app workflow.

## API navigation

- Operation and authentication: `## OpenAPI` → document-level `security` → `bearerAuth`, then `paths` → `/v1/upsertAvalaraCredentials` → `post`.
- Required payload properties and environment values: `requestBody` → `content` → `application/json` → `schema` → `required` and `properties`. The enclosing `requestBody` is not marked `required`; that is distinct from the four required properties inside the JSON object schema.
- Delivery-method mapping detail: `properties` → `delivery_method_ids`; the description points back to `/listConfiguredBillingProviders`.
- Reporting and filing option: `properties` → `commit_transactions`.
- Result and errors: `responses` documents an empty-object `200`; the `400` response uses `$ref: '#/components/schemas/Error'`, whose body schema is defined at `components` → `schemas` → `Error`; and `404` uses the `NotFound` response reference.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-integrations]]
- Supporting route: [[metronome-invoicing]]

## Raw Sources

- [[raw/metronome/api-reference/settings/upsert-avalara-credentials-2026-07-13|Upsert Avalara credentials]] — complete API reference and embedded OpenAPI operation
