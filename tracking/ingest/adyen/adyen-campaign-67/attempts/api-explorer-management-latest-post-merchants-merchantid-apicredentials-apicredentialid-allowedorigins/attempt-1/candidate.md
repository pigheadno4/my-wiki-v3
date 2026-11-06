---
title: "POST merchant API credential allowed origin | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-05.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This 2026-11-05-captured Management API reference adds a domain to the allowed origins of an API credential identified under a merchant account: `POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins`. The listed TEST server is `https://management-test.adyen.com/v3`. The caller's API credential needs the **Management API—API credentials read and write** role. `merchantId` identifies the merchant account and `apiCredentialId` the target credential; both path parameters are required. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The request-body property table marks `domain` required, `id` and `_links` optional, and `self` required inside `_links` if that optional parent is supplied. It does not separately state whole-body requiredness, a default, an origin-count limit, domain-validation details or idempotency behavior. The domain-only request example illustrates a shape, not general acceptance.
- `200` says the request succeeded and lists `domain` as required in the response body, with `id` and `_links` optional; `self` is required only within a supplied `_links`. `204` means successfully processed with no additional content. The example self link is illustrative, not proof of client-side acceptance, client-key generation, payment authorization or a Live configuration.
- Documented errors are `400` malformed request, `401` authentication, `403` insufficient permissions, `422` validation and `500` server processing. Their common error schema can include `requestId` described as essentially the same as `pspReference`; that field does not make configuration creation a payment result. The capture does not document propagation timing, subsequent activation, deletion/reversal or asynchronous review.

> [!warning] Contradiction
> The listed TEST server uses `/v3`, but the `200` response example's allowed-origin self link uses `/v1`. The example does not reconcile the route versions or establish a Live URL.

## Detail locators

- Raw lines 5–32: purpose, caller role, TEST server, path identities and body-property requiredness.
- Raw lines 34–58: request example, `200` body schema and `204` response.
- Raw lines 61–158: `400`, `401`, `403`, `422` and `500` error descriptions and schemas.
- Raw lines 160–174: illustrative `200` response and `/v1` self link.

## Related

- [[adyen-api-access]] — credential and client-side access context.
- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]] — separate merchant credential allowed-origin list.
- [[source-adyen-docs-development-resources-client-side-authentication]] — separate client-side authentication guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-05|2026-11-05 allowed-origin creation reference]]