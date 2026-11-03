---
title: "POST /merchants/{merchantId}/apiCredentials — Create an API credential | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/2026-11-03.md"
tags: [adyen, management-api, api-credentials, authentication, access-control]
---

## Overview

This 2026-11-03 Management API reference describes `POST /merchants/{merchantId}/apiCredentials` on the listed `https://management-test.adyen.com/v3` server. Its required path `merchantId` identifies a merchant account. It creates an API credential with optional requested roles and allowed origins; the calling credential needs `Management API—API credentials read and write`. The response schema describes an API key for server API authentication, a public client key for client-side authentication, and username/password for Basic authentication. These are credential identities and secrets, not payment or account-approval outcomes. See [[adyen]] and [[adyen-api-access]].

> [!warning] Contradiction
> The introduction says the endpoint creates a credential for the “company account identified in the path,” but the path table defines required `merchantId` as a merchant-account ID. The `200` example also shows company-scoped `/v1/companies/.../apiCredentials` links alongside a merchant link, while the listed server is `/v3`. This snapshot does not reconcile the account-scope wording or establish which versioned resource route applies to later calls.

## Key takeaways

- The request-body table lists only optional `allowedOrigins`, `description` and `roles`; it does not separately state whole-body requiredness or defaults. Only roles assigned to `ws@Company.<CompanyName>` can be assigned to other API credentials. The request example supplies a role and allowed origin, but does not establish actual permission or origin validation for a live account.
- The `200` schema marks `active`, `allowedIpAddresses`, `apiKey`, `clientKey`, `id`, `password`, `roles` and `username` required as response properties. `active` must be true for integration use. An empty allowed-IP list allows requests from any IP; a nonempty list rejects a request from an unlisted IP with a security error. The response also has optional allowed origins and resource links. A separate `204` success has no additional content.
- The page instructs secure storage of the API key because it cannot be retrieved later; a lost or compromised key needs generation of a new key. The `generateApiKey` and `generateClientKey` link descriptions say an existing key remains valid for 24 hours when a new one is generated. Those descriptions concern later rotation, not a guarantee that this creation request authenticated successfully.
- Listed errors are `400`, `401` authentication required, `403` insufficient permissions, `422` validation and `500`. The reference gives no idempotency contract, propagation timing, or activation/approval workflow for the newly created credential. The TEST example uses placeholder secrets and does not show live credential use.

## Detail locators

- Purpose, secret handling, role and TEST v3 server: raw lines 5–26.
- Required path ID, optional request fields and illustrative request: raw lines 28–55.
- `200` credential/link fields, key/IP semantics and `204`: raw lines 56–95.
- Error statuses and repeated response schemas: raw lines 98–195.
- Illustrative `200` payload, company/merchant links, v1 paths and placeholder keys: raw lines 197–242.

## Related

- [[source-adyen-docs-development-resources-api-credentials]] — General credential/account-scope guidance.
- [[source-adyen-docs-development-resources-api-authentication]] — API authentication guidance.
- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-generateapikey]] — Separate key-generation reference.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/2026-11-03|Pinned Adyen merchant API-credential creation reference (2026-11-03)]]
