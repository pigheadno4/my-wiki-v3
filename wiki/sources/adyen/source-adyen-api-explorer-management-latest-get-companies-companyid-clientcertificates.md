---
title: "Adyen Management API: list valid company client certificates"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/clientCertificates"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/clientCertificates/2026-11-07.md"
tags: [adyen, management-api, client-certificates, mtls]
---

## Overview

This 2026-11-07 Management API `latest` reference describes `GET /companies/{companyId}/clientCertificates` on the listed TEST `/v3` server. It retrieves previously issued client certificates under the company account that are still valid, meaning neither expired nor revoked. It is a certificate inventory read, not enrollment, credential linking, or a successful mutual-TLS request. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- `companyId` is the required company-path parameter; its table provides no additional description. The caller's API credential must have `Management API - Client certificates read`. No query parameter or request body is listed.
- `200` means all valid client certificates were returned successfully. Its `data` array is marked required, and each listed item requires `caChain` (intermediates and Management Certificate Authority Root, excluding the leaf), unique `id`, Base64-encoded DER `leaf`, `serialNumber`, and server-generated `subjectDN` derived from `companyId` and `apiCredential`. The example certificate bytes and identity are illustrative.
- Errors documented here are `401` for an invalid API credential, `403` for insufficient permission, `429` for rate-limit exceedance, and `500` for an unrecoverable server error. Listing a valid certificate does not show its private key, credential linkage, successful mTLS authentication, Live support, payment access, or current validity beyond the captured reference's semantics.

## Detail locators

- Purpose, read role, TEST server, path parameter: pinned raw lines 5–22.
- `200` response and required certificate fields: pinned raw lines 24–37.
- Error shapes: pinned raw lines 40–113. Illustrative `200` certificate payload: lines 115–134.

## Related

- [[adyen-api-access]] — credential and mTLS access context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/clientCertificates/2026-11-07|2026-11-07 pinned company client certificates list reference]]