---
title: "Adyen Management API v3: update a company API credential"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/apiCredentials/(apiCredentialId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, access-control, company-accounts]
---

## Overview

This 2026-11-03 [[adyen]] Management API reference describes `PATCH /companies/{companyId}/apiCredentials/{apiCredentialId}` for changing selected settings of an API credential under a company account. The request supplies new values for fields being changed; the response is described as the full updated credential. The calling API credential needs `Management API—API credentials read and write`. The captured server is `https://management-test.adyen.com/v3`; no live server URL is given here. This credential-configuration operation does not generate an API key or prove successful authentication to another endpoint. [[adyen-api-access]]

## Key takeaways

- Required path strings identify the company account (`companyId`) and the API credential (`apiCredentialId`). The request-body table lists optional `active`, `allowedOrigins`, `associatedMerchantAccounts`, `description`, `roles` and `subjectDN`; no required body property, default or idempotency rule is stated. The request can change enabled state, allowed origins, merchant access and roles; role delegation is limited to roles assigned to `ws@Company.<CompanyName>`. The page does not specify omission semantics or whether a submitted array is merged or replaced.
- The `200` response requires `active`, `allowedIpAddresses`, `clientKey`, credential `id`, `roles` and `username`; it can also return optional origins, explicit associated merchant accounts, description, `subjectDN` and resource links. `active` must be true for use in an integration. An empty returned `allowedIpAddresses` list permits requests from any IP; a nonempty list rejects requests from outside it. `allowedIpAddresses` is a response field here, not a documented PATCH input.
- `associatedMerchantAccounts` in the response lists **explicit** merchant access. Company access implies all company merchants, and their IDs are omitted from that list; an empty example list therefore does not prove the credential has no merchant access. Optional `_links` includes `self` (required within `_links`) and links for origins, related account and separate API/client-key generation actions. A returned `clientKey` or generation link is not evidence that this PATCH rotated either key.
- The page lists `400`, `401`, `403`, `422` and `500` errors. It gives no key-rotation request in this operation, propagation time, cross-endpoint authorization result, revocation/deletion behavior or payment outcome.

> [!warning] Contradiction
> The captured test server is `/v3`, while the `200` example's resource links use `/v1`. The snapshot does not reconcile the version difference; the example links should not determine the endpoint base path.

## Detail locators

- **Purpose, caller role and captured test server:** raw lines 5–14.
- **Company/credential path IDs and optional PATCH fields:** raw lines 16–33.
- **Single active-state request example:** raw lines 35–42.
- **Updated response, scope, active/IP rules and related links:** raw lines 43–77.
- **Error response schemas:** raw lines 80–177.
- **Illustrative response and v1 links:** raw lines 179–225.

## Related

- [[adyen-api-access]] — credential roles, account scope and lifecycle.
- [[adyen-account-structure]] — company and merchant account identities.
- [[source-adyen-api-explorer-management-latest-get-me]] — readback for the calling API credential.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03|Management API v3 company-credential PATCH — collected 2026-11-03]]