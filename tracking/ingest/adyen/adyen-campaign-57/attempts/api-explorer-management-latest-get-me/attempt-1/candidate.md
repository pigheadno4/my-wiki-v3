---
title: "GET /me — Get API credential details | Adyen Management API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/me"
raw_files:
  - "adyen/api-explorer/Management/latest/get/me/2026-09-15.md"
tags: [adyen, management-api, api-credentials, access-control, api-explorer]
---

## Overview

This [[adyen]] Management API Explorer snapshot documents `GET /me`: it returns details of the API credential associated with the API key used in the request. The page says any Management API role can call it. The captured server is TEST `https://management-test.adyen.com/v3`; the URL says `latest`, while the server path identifies `v3`. It is a credential read, not a merchant-account management action. See [[adyen-api-access]].

## Key takeaways

- The response schema requires the credential's `id`, `username`, `roles`, `active`, `allowedIpAddresses` and public `clientKey`, plus a `_links.self` link. `active` must be true to use the credential in an integration. An empty allowed-IP list means requests from any IP are allowed; a nonempty list blocks request IPs outside it with a security error. These are documented access fields, not proof that a particular operation or merchant account is authorized. [Raw: lines 19–48]
- Optional links can point to allowed origins, company or merchant resources, and API/client-key generation. The merchant link is described as present only for merchant-level API credentials; the company-link description specifically says it is present only for company-level webhooks. Preserve that page wording rather than inferring every company-level credential has the link. Merely returning a generation link does not rotate a key. [Raw: lines 22–34]
- `allowedOrigins` and `clientKey` concern client-side authentication. The page also lists optional `companyName`, description and certificate `subjectDN`; these fields do not disclose the secret API key in this response schema. [Raw: lines 37–48]
- A 200 means this read request succeeded. The page lists 400 malformed/unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server-processing failure. Error-body requiredness is separate from success-body requiredness. No page-level response examples are present. [Raw: lines 14–17, 51–148]

## Detail locators

- Purpose, role scope and TEST v3 server: pinned raw lines 5–12.
- 200 response fields, resource links, credential and client-side settings: lines 14–48.
- Error headings and schemas: lines 51–148.

## Related

- [[adyen-api-access]] — credential roles, account scope and lifecycle context.
- [[source-adyen-docs-development-resources-api-credentials]] — separate guide for credential management, account scope and test/live separation.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/me/2026-09-15|GET /me — captured 2026-09-15]]
