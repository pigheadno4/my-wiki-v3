---
title: "Get a merchant API credential | Adyen Management API v3"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, merchant-accounts, access-control]
---

## Overview

This [[adyen]] Management API reference, captured 2026-11-03, describes `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}`, a read of a specified merchant-account API credential. The listed server is `https://management-test.adyen.com/v3`. The **calling** API credential needs **Management API—API credentials read and write**; the credential identified in the path is the returned resource and can have different roles. See [[adyen-api-access]] for credential context.

## Key takeaways

- Required string path parameters distinguish `merchantId` (merchant account) from `apiCredentialId` (the credential to retrieve). The captured operation lists no query or request body. [Raw: lines 16–22]
- The `200` response marks `active`, `allowedIpAddresses`, `clientKey`, `id`, `roles`, and `username` required, with optional description, allowed origins, certificate `subjectDN`, and resource links. `active: true` is stated as necessary to use the credential. An empty IP list allows requests from any IP; a nonempty list rejects unlisted source IPs with a security error. These are credential configuration/readback facts, not proof of successful authentication or authorization for another API. [Raw: lines 29–57]
- `clientKey` is described as a public key for client-side authentication; it is distinct from an API key. The optional `generateApiKey` and `generateClientKey` links point to separate generation actions whose descriptions say the existing respective key stays valid for 24 hours after generation. Reading these links does not generate either key. A `204` alternative has no additional content. [Raw: lines 32–61]
- The listed errors are `400` request interpretation, `401` authentication, `403` permission, `422` validation, and `500` server processing, with problem-detail fields in each error body. [Raw: lines 64–161]

> [!warning] Contradiction
> The listed TEST server uses Management API `/v3`, while all resource `href` values in the `200` example use `/v1`. Treat the example links as illustrative; they do not establish this operation's versioned route. [Raw: lines 13–14, 163–196]

## Detail locators

- Purpose, caller role and TEST v3 server: raw lines 5–14.
- Path IDs: raw lines 16–22.
- `200` credential fields, IP policy and separate key-generation links: raw lines 24–57.
- `204` and failure schemas: raw lines 60–161.
- Example credential and v1 links: raw lines 163–196.

## Related

- [[adyen-api-access]] — API credential roles, scope and lifecycle context.
- [[source-adyen-api-explorer-management-latest-get-me]] — separate request-API-key-selected credential lookup.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/2026-11-03|Management API merchant credential detail — captured 2026-11-03]]