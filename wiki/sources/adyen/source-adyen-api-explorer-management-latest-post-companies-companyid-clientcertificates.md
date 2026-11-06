---
title: "Adyen Management API: Generate a company client certificate"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/clientCertificates"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/clientCertificates/2026-11-07.md"
tags: [adyen, management-api, mtls, client-certificates]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `POST /companies/{companyId}/clientCertificates` on the shown TEST v3 server (`https://management-test.adyen.com/v3`). It signs a certificate signing request (CSR) and returns a client certificate for mutual TLS communication with Adyen. The path `companyId` identifies the company account; the request's `apiCredential` identifies the intended credential for that certificate. [[adyen]] · [[adyen-api-access]]

## Key takeaways

- The calling API credential needs **Management API - Client certificates read and write**. The body requires `apiCredential` in `ws_*@Company.*` format and `certificateSigningRequest` as a Base64-encoded DER CSR. The CSR must be signed by its associated private key and use RSA of at least 2048 bits or ECC of at least 224 bits. Only the public key is enrolled.
- Adyen constructs the issued `subjectDN` from path `companyId` and body `apiCredential`; it does not use the CSR subject. The returned DN has the documented `UID={apiCredential}-Company.{companyId},CN={apiCredential}-Company.{companyId},O=Company.{companyId}` form. The generated DN **must be assigned** on the specified API credential through Customer Area or its credential PATCH endpoint. Generation and assignment are separate steps.
- A company account can have at most **10 valid client certificates at a time**. The `422` description includes an unmet CSR requirement, missing/invalid request fields, or reaching a limit of 10 client certificates. The reference gives no idempotency, renewal, or automatic replacement behavior.
- `201` reports successful certificate generation and requires `caChain` (intermediates and Management CA root, excluding the leaf), unique `id`, Base64 DER signed `leaf`, `serialNumber`, and `subjectDN`. This result is certificate issuance, not proof that the target credential has been assigned the DN, that a subsequent mTLS request authenticated, or that a payment succeeded. The error list also includes `400` malformed/incorrect CSR, `401` says the API credential used in the request is invalid, without distinguishing the calling credential from the body `apiCredential`, `403` insufficient permission, `429` rate limit, and `500` server error.

## Detail locators

- Purpose, key criteria, certificate limit, server-generated DN, caller role and TEST server: raw lines 5–25.
- Required path/body and credential-assignment instruction: raw lines 27–39. Illustrative request: lines 41–49.
- `201` result fields: raw lines 50–62. Error statuses and optional error-body fields: lines 65–176. Illustrative `201` certificate/chain response: lines 178–193.

## Related

- [[adyen]] · [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/clientCertificates/2026-11-07|2026-11-07 captured company client-certificate generation reference]]
