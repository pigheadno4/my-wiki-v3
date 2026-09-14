---
title: "Metronome API: Add a Rate"
type: source
date_ingested: 2026-09-10
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/add-a-rate"
original_format: webpage
raw_files:
  - "metronome/api-reference/rate-cards/add-a-rate-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contract-pricing/rate-cards/addRate` operation for adding one new product rate to an identified Metronome rate card. Use this singular operation when selecting the single-rate mutation; the page directs multi-rate additions to a different endpoint.

## Material warnings

> [!warning] Use the bulk operation for multiple rates
> Metronome describes this endpoint as heavily rate limited and strongly encourages `addRates` when adding multiple rates. Keep the singular `addRate` and bulk `addRates` operations distinct when choosing an integration route.

> [!warning] Percentage minimums disable commit-specific overrides
> `minimum_config` is only for `PERCENTAGE` or `TIERED_PERCENTAGE` rates. When a minimum is set on the rate or applied override, commit-specific overrides do not apply.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contract-pricing/rate-cards/addRate` -> `post`.
- **Payload detail:** `components.schemas.AddRatePayload` contains the rate-card and product targets, effective period, entitlement, rate configuration, pricing, and optional specialized-rate detail. The consequential percentage-minimum behavior is defined at `components.schemas.MinimumConfig`.
- **Success response:** `paths` -> `/v1/contract-pricing/rate-cards/addRate` -> `post` -> `responses` -> `200`; its `data` schema routes to `components.schemas.RateWithCommitRate`.
- **Error routes:** the same operation's `responses` section locates the documented error responses without duplicating their schemas here.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/add-a-rate-2026-07-13|Add a rate]] — complete collected documentation and embedded OpenAPI operation
