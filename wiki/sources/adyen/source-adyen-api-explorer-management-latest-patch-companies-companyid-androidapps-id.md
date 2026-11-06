---
title: "Adyen Management API: Reprocess a company Android app"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/androidApps/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/androidApps/(id)/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-apps]
---

## Overview

Captured Management API v3 reference for reuploading an existing Android app identified by app `id` under a company account `companyId`. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- Both `companyId` and app `id` are required path identifiers. This reference lists no query or request-body parameters.
- The API credential needs the **Management API—Android files read and write** role. Live requests are subject to rate limits; the captured server is `https://management-test.adyen.com/v3`.
- Adyen states that choosing to upload, install or run third-party applications on its payment terminals carries full responsibility and liability for the consequences.
- A `200` says the request succeeded and its response body may contain optional `Message`, described as the result of the reprocess. This reference does not specify app installation, terminal deployment or payment execution as a consequence of that response.

## Detail locators

- Purpose, permission, Live rate-limit notice and third-party responsibility: raw lines 5–17.
- Required path identifiers and optional response field: raw lines 19–35.
- Documented 400, 401, 403, 422 and 500 errors and their schemas: raw lines 38–135.

## Related

- [[adyen-android-terminals]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/androidApps/(id)/2026-11-07|Management API v3 Android app reprocess reference]]
