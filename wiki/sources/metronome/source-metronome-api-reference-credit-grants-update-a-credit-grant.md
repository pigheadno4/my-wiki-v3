---
title: "Metronome API: Update a Credit Grant"
type: source
date_ingested: 2026-09-11
canonical_url: "https://docs.metronome.com/api-reference/credit-grants/update-a-credit-grant"
original_format: webpage
raw_files:
  - "metronome/api-reference/credit-grants/update-a-credit-grant-2026-07-13.md"
tags: [metronome, api-reference, credit-grants, plans, deprecated]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/credits/editGrant` for editing an existing legacy Plans credit grant. The Plans endpoint is deprecated, and the page directs new clients to implement with Contracts.

## Key takeaways

- The request identifies the existing grant by UUID. Its request description says that only the grant's name and expiration timestamp can be updated.
- The embedded payload schema also lists `credit_grant_type` as an optional property, conflicting with the request description's narrower editable-field statement.

## Material boundary

> [!warning] Deprecated endpoint and editable-field conflict
> This operation belongs to the deprecated Plans surface; new clients are directed to Contracts. Do not assume `credit_grant_type` is editable without further authority: the request description limits updates to `name` and `expires_at`, while the embedded schema additionally exposes `credit_grant_type`.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/credits/editGrant` -> `post`.
- **Grant identification and editable fields:** `paths` -> `/credits/editGrant` -> `post` -> `requestBody`; `components.schemas.EditCreditGrantPayload` contains the required grant identifier and candidate editable properties. Read both locations together because they disagree on whether `credit_grant_type` is editable.
- **Success response:** `paths` -> `/credits/editGrant` -> `post` -> `responses` -> `200` -> `application/json` -> `schema`; the returned `data` references `components.schemas.Id`.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/update-a-credit-grant-2026-07-13|Update a credit grant]] — complete collected documentation and embedded OpenAPI operation
