---
title: "Update a company terminal logo | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalLogos/2026-11-05.md"
tags: [adyen, management-api, terminal-settings, terminal-logos, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `PATCH /companies/{companyId}/terminalLogos`: update the company-level logo for one payment terminal model at a time. The logo applies to terminals of that model under the company unless a merchant-account, store or individual-terminal logo overrides it. The listed server is TEST `https://management-test.adyen.com/v3`; the caller's API credential needs `Management API—Terminal settings read and write`. Live calls are rate limited, with no numeric limit stated here. See [[adyen-terminal-management]] for configuration scope and [[adyen-api-access]] for credential scope.

## Key takeaways

- Required path string `companyId` identifies the company account. Required query string `model` selects one terminal model; the raw lists its possible values. The request body table marks `data` optional, while the prose says to provide a Base64-encoded image string to change the logo or an empty logo value to restore the logo inherited from Adyen PSP level. The examples show both `{"data": ""}` and encoded image data. Do not interpret omitted `data` as removal; that behavior is not specified. [Raw: lines 5–12, 23–56]
- The `200` response marks the request successful and has an optional `data` string for image data. The remove-logo response example contains an inherited higher-level Base64 string; it is illustrative and does not establish a universal returned value. [Raw: lines 57–65, 167–182]
- Company-level update scope is qualified by lower-level overrides. A `200` configuration response does not prove that every terminal displays the logo, that device settings have propagated, or that a payment is ready or completed. The capture gives no propagation delay, per-device confirmation, idempotency or automatic rollback/reversal rule. [Raw: lines 5–12, 57–65]
- The documented failures are `400` request interpretation, `403` insufficient permission, `422` validation and `500` server processing, each with a problem-detail response schema. This page does not list a `401` response. [Raw: lines 68–165]

## Detail locators

- Purpose, inheritance/override, change/restore instructions, role, Live rate-limit notice and TEST server: pinned raw lines 5–21.
- Required path/query inputs, model list, optional body field and request examples: pinned raw lines 23–56.
- `200` response field and error categories/schemas: pinned raw lines 57–165.
- Illustrative remove/upload response examples: pinned raw lines 167–182.
- This dated `latest` capture does not establish present account eligibility, current Live endpoint/rate, on-device application, compliance or financial outcome.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalLogos/2026-11-05|Management API company terminal-logo PATCH — captured 2026-11-05]]