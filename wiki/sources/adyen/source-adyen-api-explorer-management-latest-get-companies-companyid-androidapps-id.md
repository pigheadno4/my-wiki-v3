---
title: "Adyen Management API: get a company Android app"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidApps/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/(id)/2026-11-07.md"
tags: [adyen, management-api, android-terminals, android-apps]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `GET /companies/{companyId}/androidApps/{id}` on the v3 test server. It returns details of an Android app previously uploaded to Adyen, identified by its app ID under a company account. Installation or uninstallation on Android payment terminals is a separate terminal action. See [[adyen-android-terminals]].

## Key takeaways

- Both path values are required: `companyId` identifies the company account, and `id` identifies the app. The API credential needs either `Management API—Android files read` or `Management API—Android files read and write`. Live requests are subject to rate limits.
- A successful `200` response requires `id` and `status`; description, label, package name, version fields, and error details are optional. Status values are `processing` (signing/conversion underway), `error`, `invalid` (APK problem), `ready` (signed and converted), and `archived` (no longer available).
- `ready` describes app preparation, not installation on a terminal. Error details may be present for `error` or `invalid`; model-specific errors may appear in `errors[].terminalModels`. This GET does not schedule deployment, change app state, or establish a device's installed version or payment readiness.

## Detail locators

- `## Parameters` → `### Path parameters`: required company and app IDs; no query or request body is listed.
- `## Responses` → `200 Success`: optional metadata, status meanings, error fields, and model-scoped errors.
- `## Responses` → `400`, `401`, `403`, `422`, and `500` error tables.

## Related

- [[adyen]]
- [[adyen-android-terminals]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/(id)/2026-11-07|Management API company Android-app GET, captured 2026-11-07]]
