---
title: "Adyen Management API: Create terminal theme metadata"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `POST /companies/{companyId}/terminalThemes` on the listed TEST `https://management-test.adyen.com/v3` server. It creates basic Android-terminal theme metadata for the company account identified by required `companyId`: a name and dark or light display mode. Model-specific image or video assets and application/activation are later steps. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- The credential needs Management API - Terminal themes read and write. Request body `mode` and `name` are required; `mode` is `dark` or `light`. The name is unique within the company account and has a maximum of 255 characters; another account may use the same name.
- `201 Created` returns required Adyen-generated theme `id`, `name` and `mode`. Creation does not add model-specific assets, activate/apply the theme, or prove that an Android terminal displays it.
- Errors listed are 400, 401, 403, 404, 422 and 500. The `422` examples include a blank name and a duplicate name within the account; they illustrate validation outcomes, not every possible failure.

## Detail locators

- Creation scope, later asset/application steps, uniqueness, role and TEST server: raw lines 5–18.
- Required company ID, request fields and example: raw lines 20–42. `201` response fields and error status descriptions: lines 43–77.
- Illustrative success and error bodies, including duplicate-name `422`: raw lines 79–192.

## Related

- [[adyen-android-terminals]] — Android terminal customization context.
- [[adyen-terminal-management]] — terminal administration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/2026-11-07|Pinned terminal theme creation reference (2026-11-07)]]
