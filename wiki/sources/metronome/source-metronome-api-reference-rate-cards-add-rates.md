---
title: "Metronome API: Add Rates"
type: source
date_ingested: 2026-09-11
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/add-rates"
original_format: webpage
raw_files:
  - "metronome/api-reference/rate-cards/add-rates-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing]
---

## Overview

This API reference documents `POST /v1/contract-pricing/rate-cards/addRates`, the Metronome operation for adding an array of new product rates to an identified rate card. Use this bulk operation when selecting a multi-rate mutation; its payload object schema requires both the rate-card identifier and the rates array.

## Material warnings

> [!warning] Conditional subscription configuration
> `billing_frequency` is optional generally, but the schema says it is required for subscription-type products with a flat rate.

> [!warning] Percentage minimums disable commit-specific overrides
> `minimum_config` is only for `PERCENTAGE` or `TIERED_PERCENTAGE` rates. When a minimum is set on the rate or applied override, commit-specific overrides do not apply.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contract-pricing/rate-cards/addRates` -> `post`.
- **Batch request:** the operation's `requestBody` -> `application/json` -> `schema` defines the payload object. The enclosing `requestBody` is not marked required; inside the object schema, `rate_card_id` and `rates` are required, and each array item routes to `components.schemas.RatePayload`.
- **Rate configuration:** `components.schemas.RatePayload` contains product targeting, effective dates, entitlement, rate type, pricing, dimensional values, and specialized-rate configuration. Nested detail is under `Tier`, `MinimumConfig`, and `CommitRate`.
- **Success response:** `paths` -> `/v1/contract-pricing/rate-cards/addRates` -> `post` -> `responses` -> `200`; required `data` routes to `components.schemas.Id` and is described as the ID of the rate card to which the rates were added.
- **Error routes:** the same operation's `responses` section locates the documented errors without duplicating their schemas here.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/add-rates-2026-07-13|Add rates]] — complete collected documentation and embedded OpenAPI operation
