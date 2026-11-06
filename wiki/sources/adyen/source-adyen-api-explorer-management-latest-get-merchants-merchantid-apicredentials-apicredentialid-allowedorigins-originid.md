---
title: "Adyen Management API v3: get a merchant credential allowed origin"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`, a read of the allowed origin identified in the merchant-account, API-credential and origin path. The listed server is `https://management-test.adyen.com/v3`. The calling API credential needs the **Management API—API credentials read and write** role. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- All three path identifiers are required strings: `merchantId` identifies the merchant account, `apiCredentialId` the target credential, and `originId` the allowed origin. This GET reference specifies no query parameters or request body.
- A `200` response describes an allowed-origin resource: required `domain`, optional `id`, and optional `_links` whose `self` object is required if `_links` appears; `self.href` is optional. The reference also lists `204` success with no additional content. Neither status changes the origin or establishes that a browser request using a client key succeeds.
- The captured errors are `400` (request problem), `401` (authentication required), `403` (insufficient permissions), `422` (validation), and `500` (server processing). Their common problem schema and conditional `invalidFields` details are in the raw response tables.
- This read reference supplies no default, pagination, rate or size limit, idempotency contract, propagation timing, lifecycle transition, approval result, Live server, or payment outcome. Its TEST response is configuration readback at capture time, not proof of current access or compliance.

> [!warning] Contradiction
> The listed TEST server is `/v3`, but the `200` example's `_links.self.href` uses `/v1/merchants/...`. The example does not resolve the versioned self-link route or a Live route.

## Detail locators

- Raw `## Parameters > ### Path parameters`: required resource identifiers.
- Raw `## Responses > ### 200 Success` and `### 204 Success`: result shape and no-content outcome.
- Raw `## Responses > ### 400/401/403/422 Client Error` and `### 500 Server Error`: documented failure classes and problem fields.
- Raw `## Response examples > ### 200 Success`: illustrative domain, ID and version-conflicting self-link.

## Related

- [[adyen-api-access]] — credential scope, roles and related allowed-origin references.
- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]] — list origins for the merchant credential.
- [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid-allowedorigins-originid]] — separate company-path detail read.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05|GET merchant credential allowed origin, captured 2026-11-05]]