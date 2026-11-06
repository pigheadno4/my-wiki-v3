---
title: "Adyen Management API: upload Android certificate"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/androidCertificates"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/androidCertificates/2026-11-07.md"
tags: [adyen, management-api, android-certificates, terminal-management]
---

## Overview

This captured Management API `POST /companies/{companyId}/androidCertificates` reference describes uploading an Android certificate file to Adyen for a company account. The required `companyId` is the unique company-account identifier. Its listed server is TEST `/v3`; live requests are subject to rate limits. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- The API credential needs `Management API—Android files read and write`.
- This captured page specifies no request-body schema, file encoding, content type, size limit, or example. Do not infer an upload format from the endpoint name.
- `200` says the request succeeded. The response schema lists an optional `id` for the uploaded Android certificate. The response does not itself establish application approval, distribution, installation, or payment readiness.
- Documented failures are 400, 401, 403, 422, and 500.

## Detail locators

- Raw lines 5–23: purpose, credential role, live rate-limit note, TEST server, and company path identity.
- Raw lines 25–33: 200 response and optional certificate `id`; lines 36–133: error schemas.

## Related

- [[adyen]]
- [[adyen-android-terminals]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/androidCertificates/2026-11-07|Captured Management API Android certificate upload reference]]
