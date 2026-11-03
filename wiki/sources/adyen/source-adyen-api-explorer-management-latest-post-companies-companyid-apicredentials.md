---
title: "Adyen Management API v3: create a company API credential"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/2026-11-03.md"
tags: [adyen, management-api, api-credentials, authentication]
---

## Overview

This captured Management API v3 reference describes `POST /companies/{companyId}/apiCredentials`, creating an API credential for the company account identified by required path `companyId`. The request may choose associated merchant-account access, roles and allowed origins. The listed server is `https://management-test.adyen.com/v3`; the calling credential needs **Management API—API credentials read and write**. See [[adyen-api-access]] and [[adyen]].

## Key takeaways

- All four documented request-body fields are optional: `allowedOrigins`, `associatedMerchantAccounts`, `description` and `roles`. The role list is limited to roles assigned to `ws@Company.<CompanyName>`. This endpoint capture does not state a default role or merchant scope when those fields are omitted.
- The 200 response describes the created credential's `id`, `username`, `active`, roles, associated merchant accounts, allowed IP addresses, `apiKey`, `clientKey` and Basic-auth `password` as required fields. It says `active` must be true for integration use. An empty allowed-IP list permits requests from any IP; a nonempty list rejects unlisted source IPs. `allowedOrigins`, description, subject DN and resource links are optional.
- The API key cannot be retrieved later, so the capture directs secure storage; lost or compromised keys require generating a new key. The response describes optional generate-key links and says the existing key remains valid for 24 hours when a new API or client key is generated. Those are later operations, not an effect of this creation response. A returned credential does not prove successful subsequent authentication, allowed endpoint access, payment authorization or compliance.

> [!warning] Contradiction
> This reference lists a `/v3` TEST server (raw line 26), while the 200 example's credential, allowed-origin and generate-key `href` values use `/v1/` (raw lines 221–240). The example does not establish the v3 link routes or the correct Live routes.

## Detail locators

- Purpose, authentication types, secret handling, calling role and TEST server: raw lines 5–26.
- Required company path and optional request fields: raw lines 28–42; example request: lines 44–61.
- 200 response schema, nested optional links and required credential fields: raw lines 62–98.
- Error tables: raw lines 101–198 (400, 401, 403, 422 and 500).
- Illustrative 200 response and `/v1/` links: raw lines 200–251.

## Related

- [[adyen-api-access]] — credential and authentication context.
- [[source-adyen-api-explorer-management-latest-post-me-generateclientkey]] — distinct client-key rotation route.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/2026-11-03|POST company API credential captured 2026-11-03]]