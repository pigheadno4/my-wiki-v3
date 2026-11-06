---
title: "Adyen Management API: list company Android apps"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidApps"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/2026-11-07.md"
tags: [adyen, management-api, android-terminals, android-apps]
---

## Overview

This 2026-11-07 Management API `latest` reference lists `GET /companies/{companyId}/androidApps` on the TEST `/v3` server. It reads Android apps uploaded to Adyen for the company account. Installation and removal on Android payment terminals use separate terminal actions; listing an app, including one marked `ready`, does not establish installation. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- `companyId` is the required path ID of the company account. Optional filters are `versionCode` and `packageName`; optional `pageSize` defaults to 20 and has a maximum of 100, with optional `pageNumber`. No request body is listed. The caller needs one of four roles: Android files read/read and write or Terminal actions read/read and write. Live requests have a rate-limit notice but no numerical limit here.
- `200` has optional `data` listing uploaded apps. Within each returned app object, `id` and `status` are required; description, label, package name, version fields and error details are optional. The status values are `processing` (signing/conversion), `error` (a problem; check app requirements), `invalid` (APK problem), `ready` (signed/converted), and `archived` (no longer available). `ready` is a preparation state, not proof of deployment to a device.
- The reference documents `400`, `401`, `403`, `422`, and `500` errors. The two `ready` items in the `200` example are illustrative, not evidence of a company account's current apps or installed versions. This read does not upload, sign, install, uninstall, or execute a payment.

## Detail locators

- Purpose, caller roles, Live rate-limit notice, TEST server, path and optional query parameters: pinned raw lines 5–39.
- `200` optional `data`, item identity, status meanings and optional error/model fields: pinned raw lines 41–60.
- Error response shapes: pinned raw lines 63–160. Illustrative two-app `200` JSON: lines 162–189.

## Related

- [[adyen-android-terminals]] — app deployment context and separate installation routes.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidApps/2026-11-07|2026-11-07 pinned company Android apps list reference]]