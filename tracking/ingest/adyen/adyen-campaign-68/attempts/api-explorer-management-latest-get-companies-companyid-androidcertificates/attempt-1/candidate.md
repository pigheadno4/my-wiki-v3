---
title: "Adyen Management API: List company Android certificates"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/androidCertificates"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/androidCertificates/2026-11-07.md"
tags: [adyen, management-api, android-terminals, certificates]
---

## Overview

This 2026-11-07 capture of the Management API `latest` reference documents `GET /companies/{companyId}/androidCertificates` on the shown TEST v3 server (`https://management-test.adyen.com/v3`). It lists Android certificates available for the company account identified by required path `companyId`. These uploaded certificates typically enable apps on Android payment terminals; installation or removal is a separate terminal-action operation. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- The API credential needs **one of** four roles: Management API—Android files read, Android files read and write, Terminal actions read, or Terminal actions read and write. Live requests are subject to rate limits; this reference gives no numeric limit.
- Optional query filters are `certificateName`, `pageSize` (default 20, maximum 100), and `pageNumber`. The `200` response schema marks `data` optional. Within an included certificate object, `id` is required; `description`, `extension`, `name`, `notBefore`, `notAfter`, and `status` are optional.
- A returned certificate identifies an uploaded company-available file in this snapshot. The example's `ready` statuses and dates are illustrative; they do not establish installation, valid use on a particular terminal, successful app deployment, or payment execution. This GET does not upload, install, uninstall, activate, or delete a certificate.
- The captured error responses are `400` problem reading/understanding the request, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` server failure. The reference states no idempotency, conflict/version, approval, reversal, or asynchronous completion rule for this read.

## Detail locators

- Purpose, separate terminal-action boundary, roles, Live rate-limit notice and TEST v3 server: raw lines 5–23.
- Required path and optional query parameters: raw lines 25–38. `200` optional collection and item fields: raw lines 40–55.
- Error schemas and status descriptions: raw lines 58–155. Illustrative two-item `200` response, including `ready` examples: raw lines 157–184.

## Related

- [[adyen]] · [[adyen-android-terminals]] · [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/androidCertificates/2026-11-07|2026-11-07 captured company Android certificates GET reference]]
