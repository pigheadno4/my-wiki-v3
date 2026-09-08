---
title: "Upsert Anrok API token"
type: source
date_ingested: 2026-09-08
canonical_url: "https://docs.metronome.com/api-reference/settings/upsert-anrok-api-token"
original_format: webpage
raw_files:
  - "metronome/api-reference/settings/upsert-anrok-api-token-2026-07-13.md"
tags: [metronome, anrok, tax, threshold-billing, api]
---

## Overview

Bearer-authenticated `POST /v1/upsertAnrokApiToken` associates an Anrok API token with submitted billing-provider `delivery_method_ids`. The operation maps the credential to the appropriate billing entity and is documented as serving Threshold Billing workflows only at the time of this snapshot.

## Key takeaways

- The delivery-method identifiers come from `/listConfiguredBillingProviders`; this upsert page does not enumerate or create those configurations.
- Inside the JSON payload schema, both `delivery_method_ids` and `anrok_api_token` are required properties. The enclosing OpenAPI `requestBody` is not itself marked required, so this page does not establish omitted-body behavior.
- HTTP `200` requires `data.success`, a boolean describing whether the update succeeded. The page exposes no per-delivery-method result shape.
- The explicit Threshold Billing qualification is consequential: this endpoint is not evidence of a complete, general-purpose Anrok tax integration.

## Raw detail map

- Operation and authentication: OpenAPI `post /v1/upsertAnrokApiToken`, document-level `security`, and `components.securitySchemes.bearerAuth`.
- Payload fields and example: `paths./v1/upsertAnrokApiToken.post.requestBody.content.application/json.schema` and sibling `example`.
- Success and errors: `responses.200`, `responses.400`, `responses.404`, `components.schemas.Error`, and `components.responses.NotFound`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-integrations]]
- Delivery-method discovery context: [[source-metronome-api-reference-settings-list-account-level-billing-providers]]

## Raw Sources

- [[raw/metronome/api-reference/settings/upsert-anrok-api-token-2026-07-13|2026-07-13 snapshot - Anrok token upsert for Threshold Billing]]
