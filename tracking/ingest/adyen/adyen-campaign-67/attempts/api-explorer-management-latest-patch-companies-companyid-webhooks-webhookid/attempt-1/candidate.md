---
title: "Adyen Management API: Update a company webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, configuration]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, documents `PATCH /companies/{companyId}/webhooks/{webhookId}` for changing the configuration of one company-account webhook. The captured server is `https://management-test.adyen.com/v3`; this page does not list a live server. The response describes the full webhook configuration including the requested new values.

## Key takeaways

- The caller's API credential needs the **Management API—Webhooks read and write** role. Both `companyId` (company account) and `webhookId` (webhook configuration) are required path identifiers. Request-body fields are individually marked optional; this reference does not specify an idempotency header or a general body-required flag.
- `active` is optional in the update body, but must be `true` for Adyen to send account-event webhooks. Company merchant filtering supports `includeAccounts`, `excludeAccounts`, or `allAccounts`; `filterMerchantAccounts` is required when the filter type is include or exclude, and is not needed for all accounts.
- Configuration options include the public `url`, format (`soap`, `http`, or `json`), optional username/password, SSL certificate acceptance flags (each default `false`), `encryptionProtocol` (`TLSv1.3`, `TLSv1.2`, or Test-only `HTTP`; omitted uses TLSv1.2), Standard-webhook additional settings, SOAP-action header flag (SOAP only), and Terminal API notification `networkType` (default `public`). Consult the raw request table for exact field scope.
- A `200` means this configuration update request succeeded and returns the full configuration. Response fields include `active`, `communicationFormat`, `type`, `url`, optional `id`, `hasError`, `hasPassword`, HMAC key check value and resource/action links. `hasError=true` calls for troubleshooting via the testing endpoint; links to generate HMAC and test are actions, not evidence those actions occurred. An active response or example does not establish successful webhook delivery, payment authorization, settlement, compliance, or account eligibility.

> [!warning] Versioned sample links
> The captured server list says Management Test `/v3` (line 14), while the 200 response example's `_links` use `/v1` (lines 285-297). Treat those links as sample values; this snapshot does not resolve which versioned action URL to invoke.

## Detail locators

- Purpose, role and captured server: opening text and `## Servers`, lines 5-14.
- Required path identifiers and optional request fields, defaults, conditional merchant filtering, and Test-only HTTP: `## Parameters`, lines 16-44.
- Example `{"active": true}`: `## Request examples`, lines 46-53; example values are illustrative.
- Success meaning, response schema, links and error indicator: `### 200 Success`, lines 54-96.
- Documented failures: `### 400 Client Error` (lines 99-116), `### 401 Client Error` (119-136), `### 403 Client Error` (139-156), `### 422 Client Error` (159-176), and `### 500 Server Error` (179-196). Their error bodies expose details, code, status and optional validation fields; no endpoint-specific rollback or retry contract is stated.
- Illustrative response and versioned `_links`: `## Response examples`, lines 198-299.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]
- Separate Customer Area configuration guide: [[source-adyen-docs-development-resources-webhooks-configure-and-manage]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/webhooks/(webhookId)/2026-11-05|Adyen Management API — Update a company webhook (2026-11-05)]]
