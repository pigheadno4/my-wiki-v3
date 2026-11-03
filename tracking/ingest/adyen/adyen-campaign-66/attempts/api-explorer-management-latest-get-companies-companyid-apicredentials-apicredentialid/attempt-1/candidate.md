---
title: "Adyen Management API v3: Get a company API credential"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, company-account]
---

## Overview

The captured [[adyen]] Management API v3 TEST `GET /companies/{companyId}/apiCredentials/{apiCredentialId}` returns the identified API credential under a company-account path. The company account ID, target credential ID, and caller's API credential are distinct. The caller needs the `Management API—API credentials read and write` role. This is credential configuration readback, not key generation, role assignment, authentication proof, or payment execution. See [[adyen-api-access]].

## Key takeaways

- Both `companyId` and `apiCredentialId` are required string path parameters. No query or request body is documented. The captured server is `https://management-test.adyen.com/v3`.
- The 200 schema requires `active`, `allowedIpAddresses`, `clientKey`, `id`, `roles`, and `username`. `active: true` is required to use the credential in an integration; it does not alone prove an API call will authenticate or be authorized. An empty `allowedIpAddresses` list allows requests from any IP according to this response-field description; a nonempty list excludes unlisted IPs with a security error.
- `associatedMerchantAccounts` optionally lists explicit merchant access. The schema says company access implies all its merchants and omits those merchant IDs from this list, so an empty list is not proof of no merchant access. Optional `allowedOrigins`, `subjectDN`, and `_links` describe configuration and related resources. Within optional `_links`, `self` is marked required; the generation links describe separate key-generation operations, not effects of this GET.
- The sample shows `/v1` resource-link URLs even though the captured server is `/v3`. The sample does not resolve which link version should be used for a current integration.

> [!warning] Contradiction
> This page lists the Management API TEST server as `https://management-test.adyen.com/v3` but its 200 example's credential, allowed-origin, company, and key-generation `href` values use `/v1`. Treat those example links as conflicting sample data, not proof of the v3 route or current link behavior.

## Detail locators

- Purpose, required caller role, TEST server and path IDs: pinned raw lines 5–22.
- 200 response schema, account scope, IP rules and related links: pinned raw lines 24–58. The `company` link description says it is present only for company-level webhooks; this wording is recorded here without resolving its applicability to this credential GET.
- 400, 401, 403, 422, and 500 error schemas: pinned raw lines 61–158.
- 200 example and conflicting `/v1` links: pinned raw lines 160–215. Example role and origin values are illustrative, not universal grants.
- This capture states no idempotency, deletion/reversal, propagation, asynchronous approval/activation, or financial outcome. Its `latest` URL and 2026-11-03 snapshot do not prove present account eligibility or API availability.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/2026-11-03|2026-11-03 pinned API Explorer snapshot]]
