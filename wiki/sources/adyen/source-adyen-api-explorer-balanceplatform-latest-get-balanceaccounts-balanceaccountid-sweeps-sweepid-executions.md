---
title: "Adyen Balance Platform API v2: GET custom payout sweep executions"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/executions"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/executions/2026-11-02.md"
tags: [adyen, balance-platform, custom-payouts, sweeps, executions, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}/executions` as a paginated read of custom payout schedule executions on a balance account. The required path IDs identify the balance account and sweep configuration, not a transfer. The only displayed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation URL does not establish current live version, access or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Optional query `cursor` comes from a prior next/previous pagination link; optional `limit` defaults to 10 items per page. Optional comma-separated `results` filters for `succeeded`, `failed` or `skipped`. The 200 response requires `link` and `sweepExecutions`; individual pagination links and execution fields are optional.
- Each execution may have its own `id`, `triggeredAt`, `result` and `resultDetails`. The details may include a human-readable `reason`, `reasonCode`, `sweepConfigurationDisabled`, and `transferId` for a transfer created by the execution, if applicable. Do not confuse the sweep-configuration path `sweepId`, execution `id`, and optional resulting `transferId`.
- The API labels `succeeded` a completed sweep payout, `failed` a payout not completed due to error, and `skipped` a payout not triggered as expected. These are execution results. The companion custom-payout execution guide says to follow a resulting transfer ID through separate Transfer webhooks, including possible return; neither the list nor its illustrative `succeeded` item proves beneficiary bank receipt. [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts-view-custom-payout-executions]]
- The page documents 401, 404, 422 and 500 errors. It does not state a credential role, request body, idempotency behavior, retry policy or execution-propagation timing. Its one 200 JSON sample is illustrative, not a guarantee that every execution has a transfer ID or next page.

## Detail locators

- Endpoint, TEST server, required path IDs and query filters/default: pinned raw lines 5–26.
- 200 pagination and execution/result-detail fields: `## Responses > ### 200 Success`, lines 28–55.
- Error schemas: `## Responses`, lines 58–131. Illustrative one-item success and next-link JSON: `## Response examples`, lines 133–155.

## Related

- [[adyen-platforms]] — custom payout and sweep context.
- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts-view-custom-payout-executions]] — separate execution and transfer-lifecycle guidance.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts-balanceaccountid-sweeps]] — separate sweep configuration creation.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/executions/2026-11-02|Custom payout sweep execution GET snapshot]]