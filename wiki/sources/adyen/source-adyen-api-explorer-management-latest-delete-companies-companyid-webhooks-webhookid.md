---
title: "Adyen Management API v3: remove a company webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, configuration]
---

## Overview

This 2026-11-05-captured Adyen Management API reference describes `DELETE /companies/{companyId}/webhooks/{webhookId}`: remove the configuration identified by a webhook ID under a company account. The captured server is `https://management-test.adyen.com/v3`. The API credential must have the **Management API—Webhooks read and write** role. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- Both path parameters are required strings: `companyId` identifies the company account, and `webhookId` identifies the webhook configuration.
- The documented success response is HTTP `204`; the reference says to inspect the actual response code for request status and supplies no success response body. This is a configuration deletion contract, not proof of webhook delivery, payment outcome, or financial finality.
- The captured reference gives no request body, query parameters, idempotency behavior, propagation timing, or live server. It does not establish present availability or account eligibility.

## Detail locators

- Purpose, role, TEST server, and path identities: raw lines 5–22.
- HTTP `204` success wording: raw lines 24–27.
- Documented `400`, `401`, `403`, `422`, and `500` errors and their problem response schemas: raw lines 30–127. `401` is authentication required; `403` is insufficient permissions.

## Related

- [[adyen-webhooks]] — provider webhook concept and source routes.
- [[adyen-api-access]] — provider API access context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/webhooks/(webhookId)/2026-11-05|Adyen Management API DELETE company webhook, captured 2026-11-05]]
