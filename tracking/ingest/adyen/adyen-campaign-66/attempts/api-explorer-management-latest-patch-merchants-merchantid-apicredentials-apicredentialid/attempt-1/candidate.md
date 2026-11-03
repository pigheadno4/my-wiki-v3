---
title: "PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId} — update an API credential | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/apiCredentials/(apiCredentialId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, roles, allowed-origins, security]
---

## Overview

This 2026-11-03-captured [[adyen]] Management API reference describes `PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId}` on the listed TEST `https://management-test.adyen.com/v3` server. The required path IDs identify a merchant account and its API credential; the calling API credential separately needs **Management API—API credentials read and write**. The operation changes specified credential values and says its `200` response contains the full updated credential. See [[adyen-api-access]]. [Raw: lines 5–22, 42–75]

## Key takeaways

- The request-body table marks `active`, `allowedOrigins`, `description`, `roles` and `subjectDN` optional; it does not separately declare whole-body requiredness. `allowedOrigins` is a new list of strings for this credential. The role assignment rule limits assignable roles to those assigned to `ws@Company.<CompanyName>`. The page does not state list-merging behavior, deletion semantics for omitted fields or propagation timing. [Raw: lines 25–32]
- `active` indicates whether the credential is enabled. The `200` schema says it must be `true` to use the credential in an integration. It also returns required credential `id`, `username`, `clientKey`, `roles` and `allowedIpAddresses`; an empty allowed-IP list permits requests from any IP, while an unlisted source IP in a nonempty list gets a security error. The allowed-IP list is a response field here, not a PATCH input. [Raw: lines 28, 63–75]
- The response's optional `allowedOrigins` array contains domain objects, distinct from the request's string array. Optional `_links` may point to self, allowed origins and separate API/client-key generation operations. The link descriptions say a previous key remains valid for 24 hours when a new key is generated; this PATCH does not itself generate or return an API-key secret. The returned `clientKey` is described as a public client-side key, not the server API key. [Raw: lines 50–75]
- A `200` means the update request succeeded with a credential response; `204` means processed without additional content. Neither is proof of a successful later authentication, endpoint authorization, origin acceptance, certificate use or payment. The only request example sets `active: true`; it is not a universal outcome. [Raw: lines 34–79]
- Errors listed are `400` request, `401` authentication, `403` permission, `422` validation and `500` server failure, with structured problem bodies. The page provides no idempotency, retry, live endpoint or version-conflict rule. [Raw: lines 82–179]

> [!warning] Contradiction
> The listed TEST server and operation path are `/v3/merchants/{merchantId}/apiCredentials/{apiCredentialId}`, but the `200` example's self and related links use `/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/...` for the same credential ID. The example also has a separate merchant link. The snapshot does not reconcile the route and version difference; do not infer that the company-path example is the PATCH route. [Raw: lines 5, 13–22, 181–225]

## Detail locators

- Operation, caller role, TEST v3 server and two path IDs: raw lines 5–22.
- Optional PATCH fields and company-credential role ceiling: raw lines 25–32.
- Active-only request example: raw lines 34–41.
- `200` schema, nested links and `204`: raw lines 42–79.
- Error statuses and problem fields: raw lines 82–179.
- `200` example and v1 company-path links: raw lines 181–225.

## Related

- [[adyen-api-access]] — web-service credential identity, roles and access context
- [[source-adyen-api-explorer-management-latest-post-me-allowedorigins]] — separate allowed-origin creation route

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03|Management API merchant-credential PATCH — captured 2026-11-03]]