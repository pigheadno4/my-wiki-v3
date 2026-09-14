---
title: "Metronome API: Update a Rate Card"
type: source
date_ingested: 2026-09-10
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/update-a-rate-card"
original_format: webpage
raw_files:
  - "metronome/api-reference/rate-cards/update-a-rate-card-2026-08-28.md"
tags: [metronome, api-reference, rate-cards, pricing, aliases]
---

## Overview

This API reference documents `POST /v1/contract-pricing/rate-cards/update`, which updates rate-card configuration without changing underlying pricing rates or schedules. Its alias behavior distinguishes already-created contracts, which retain their originally assigned rate cards, from new alias-based contracts, which resolve the alias when they are provisioned.

## Key takeaways

- The operation updates a rate card's name, description, aliases, and credit-type conversions; it does not update the card's underlying pricing rates or schedules.
- Already-created contracts continue using their originally assigned rate cards after alias changes. A scheduled alias transition instead changes which card new contracts resolve when provisioned at or after the transition.
- The page states that other changes made through this endpoint affect only the Metronome UI.
- Credit-type conversions can be added for custom pricing units, but existing conversions cannot be modified through this operation.

## Material boundary

> [!warning] Configuration update is not a price update
> Do not use this operation to change existing product prices or rate schedules. Alias reassignment or scheduling changes the card selected for newly provisioned alias-based contracts; it does not move already-created contracts off their originally assigned cards.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contract-pricing/rate-cards/update` -> `post`.
- **Payload detail:** `paths` -> `/v1/contract-pricing/rate-cards/update` -> `post` -> `requestBody` states that at least one supported update must be supplied; `components.schemas.UpdateRateCardPayload` contains the rate-card identifier and optional update categories. `components.schemas.RateCardAlias` and `components.schemas.CreditTypeConversionInput` contain the effective-date and conversion details.
- **Response placement:** `paths` -> `/v1/contract-pricing/rate-cards/update` -> `post` -> `responses` -> `200` -> `application/json` -> `schema` requires `data`, which references `components.schemas.Id`; the example places the UUID at `data.id`.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-products-and-rate-cards]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/update-a-rate-card-2026-08-28|Update a rate card]] — complete collected documentation and embedded OpenAPI operation
