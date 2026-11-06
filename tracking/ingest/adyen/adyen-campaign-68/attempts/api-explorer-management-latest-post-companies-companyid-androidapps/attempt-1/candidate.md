---
title: "Adyen Management API: Upload an Android app"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/androidApps"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/androidApps/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, android-terminals, app-upload]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `POST /companies/{companyId}/androidApps` for uploading an Android APK to Adyen under the company account identified by required `companyId`. The listed server is TEST `https://management-test.adyen.com/v3`. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- The APK size limit is 200 MB. The API credential must have Management API—Android files read and write. Live requests are subject to rate limits.
- Adyen states that choosing to upload, install or run third-party applications on a payment terminal carries full responsibility and liability for the consequences.
- A `200` means the request succeeded; the uploaded app's unique `id` is an optional response field. The captured page gives no request-body schema or file encoding instructions. A successful upload response does not establish app processing, approval, installation, on-device operation or payment execution.

## Detail locators

- Upload purpose, size, role, Live rate limit, liability, TEST server and company ID: raw lines 5–25.
- `200` response with optional `id`: raw lines 27–35. Error response definitions for 400, 401, 403, 422 and 500: raw lines 38–135.

## Related

- [[adyen-android-terminals]] — Android terminal app deployment context.
- [[adyen-terminal-management]] — Management API terminal fleet administration.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/androidApps/2026-11-07|Pinned Management API Android APK upload reference (2026-11-07)]]
