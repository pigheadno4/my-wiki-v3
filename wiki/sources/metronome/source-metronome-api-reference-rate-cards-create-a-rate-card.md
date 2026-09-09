---
title: "Metronome API: Create a Rate Card"
type: source
date_ingested: 2026-09-09
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/create-a-rate-card"
original_format: webpage
raw_files:
  - "metronome/api-reference/rate-cards/create-a-rate-card-2026-07-13.md"
tags: [metronome, api-reference, rate-cards, pricing, aliases]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contract-pricing/rate-cards/create` operation for creating a Metronome rate card. A rate card is the central pricing configuration that can carry one fiat currency, conversions to custom pricing units, and aliases used when provisioning customer contracts.

## Key takeaways

- The payload schema requires `name`. The rate card has one underlying fiat currency; when `fiat_credit_type_id` is omitted, the schema says it defaults to USD cents. Custom pricing-unit conversions can be supplied so later product rates can use those units.
- Aliases are human-readable substitutes for the rate-card ID during contract provisioning. An alias can belong to only one rate card at a time, and the documentation says it resolves to the card to which it was most recently assigned.
- Creating the card does not add product prices through this operation. The documented next step is to use `addRate` or `addRates` to add products and their prices.
- HTTP `200` places the created rate-card identifier at `data.id`.

## Material warnings and boundaries

> [!warning] Alias reassignment changes the original schedule
> Reusing an alias already assigned to another rate card updates the original card's alias schedule, and the alias then references the most recently assigned card. Treat alias reassignment as a consequential routing change when provisioning contracts.

> [!info] Propagation wording is broader than this create operation
> The page describes rate-card pricing changes as automatically propagating across customer cohorts, but this create endpoint does not itself define the timing or scope of later rate changes. Use the dedicated rate-addition and pricing-change authorities for those behaviors.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contract-pricing/rate-cards/create` -> `post`.
- **Payload detail:** `components.schemas.CreateRateCardPayload` contains the required name and routes optional description, fiat currency, conversion, alias, and custom-field detail. `components.schemas.CreditTypeConversionInput` and `components.schemas.RateCardAlias` contain the nested conversion and effective-dated alias shapes.
- **Response placement:** `paths` -> `/v1/contract-pricing/rate-cards/create` -> `post` -> `responses` -> `200` -> `application/json` -> `schema` requires `data`, which references `components.schemas.Id`; the example places the UUID at `data.id`.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-products-and-rate-cards]]
- Supporting concept: [[metronome-currencies-and-custom-pricing-units]]
- Rate-card guide: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/create-a-rate-card-2026-07-13|Create a rate card]] — complete collected documentation and embedded OpenAPI operation
