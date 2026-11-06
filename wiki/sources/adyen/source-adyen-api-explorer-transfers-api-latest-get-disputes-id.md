---
title: "Adyen Raise disputes API v4: get an Issuing dispute by ID"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(id)"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07.md"
tags: [adyen, issuing, disputes, raise-disputes-api, api-explorer]
---

## Overview

This 2026-11-07 `GET /disputes/{id}` reference reads a raised dispute by its required dispute ID. Although its URL contains `transfers-api`, the companion overview identifies this `/btl/api/v4` family as **Raise disputes API v4** for Adyen-issued-card transaction disputes and fraud reporting, separate from funds-movement Transfers API and merchant acquiring dispute defense. [[adyen]] [[adyen-issuing]] [[source-adyen-api-explorer-transfers-api-latest-overview]]

## Key takeaways

- The operation lists TEST and Live `/btl/api/v4` servers and one required path `id`, the unique raised-dispute identifier. It states no request body, query parameter, default, pagination, or idempotency rule. The companion overview describes Adyen-provided API credentials with `X-API-Key` or basic authentication and an additional role set up by Adyen; this operation does not name a finer-grained role. [[source-adyen-api-explorer-transfers-api-latest-overview]]
- `200` means the read succeeded. The response schema requires `transactionId` and dispute `type` but marks `id`, `status`, ARN, description, disputed amount, and reason-specific detail objects optional. Its status enum is `draft`, `submitted`, `closed`, `won`, `chargeback`, or `secondPresentment`; creation may set only `draft`, while update may set `submitted` or `closed`. A returned status describes the dispute record at lookup time, not an initiated or completed new action by this GET.
- Reason-specific objects are top-level optional in the response table but prose says each is required for its matching `type`; nested required and conditional fields vary by reason. The raw table is the locator for cancelled, duplicate, fraud, not-as-described, and not-delivered detail. `fraudInfo.reportOnly=true` is described as fraud reporting without further chargeback or fee-reversal action, with `false` as the stated default. Do not infer that a report-only record achieved a chargeback or reversal.
- This capture lists `cancelled`, `duplicate`, `fraud`, `notAsDescribed`, `notDelivered`, and `other` as types, but explicitly says `other` is deprecated and must not be created or submitted. It lists `401` authentication-required, `403` insufficient-permissions, and `422` validation responses with optional error-envelope fields. No success or error JSON examples appear in this pinned page.

> [!warning] Contradiction
> This November 2026 detail reference calls `other` deprecated and lists `cancelled` and `notAsDescribed`. The separately captured September 2026 `POST /disputes` reference calls `other` beta and omits those two types from its type enum. Both warn against creating or submitting `other`; the snapshots do not establish current creation support for every type. [[source-adyen-api-explorer-transfers-api-latest-post-disputes]]

## Detail locators

- Purpose, TEST/Live bases, required dispute ID and success meaning: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07#L5|raw lines 5–27]].
- Optional response fields, reason-specific conditional detail, status/type enums and deprecation: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07#L29|raw lines 29–107]].
- `401`, `403`, `422` error schemas: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07#L110|raw lines 110–164]].
- Companion API identity/authentication: [[raw/adyen/api-explorer/transfers-api/latest/overview/2026-09-15#L5|overview raw lines 5–47]]. Earlier POST type wording: [[raw/adyen/api-explorer/transfers-api/latest/post/disputes/2026-09-15#L49|POST raw lines 49–55]].

## Related

- [[adyen-issuing]] — issued-card dispute context.
- [[source-adyen-api-explorer-transfers-api-latest-overview]] — Raise disputes API v4 family identity and authentication.
- [[source-adyen-api-explorer-transfers-api-latest-post-disputes]] — older dispute creation contract and type-wording conflict.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07|Captured Raise disputes API v4 GET dispute detail reference]]
