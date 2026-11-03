---
title: "Adyen Balance Platform API v2: DELETE an account managed payout schedule"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md"
tags: [adyen, balance-platform, managed-payouts, payout-schedules, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `DELETE /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}`, deleting a managed payout schedule applied to a balance account. Both string path parameters are required: `balanceAccountId` identifies the account, while `id` identifies the schedule applied to that account. The only displayed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation route is not evidence of current live availability or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The documented success is HTTP 204 with no response-body schema. It establishes successful removal of the account-level schedule, not deletion of the platform-level schedule definition, reversal of past executions, or any transfer or bank-receipt result. The page gives no query parameters, request body, idempotency header or propagation timing.
- The reference lists 401 authentication required, 404 resource not found, 422 validation error and 500 server error. Their response tables contain optional problem-detail fields and conditionally required `invalidFields` children. No credential role, retry rule or response examples are supplied here.
- This is a configuration deletion. Whether a schedule was previously executed, whether a resulting transfer later failed or returned, and whether another schedule can be applied are separate questions requiring their own evidence.

## Detail locators

- Endpoint, TEST server, path identity and requiredness: pinned raw lines 5–18.
- 204 success without response schema: `## Responses > ### 204 Success`, lines 20–24.
- Error statuses and body fields: `## Responses`, lines 26–99.

## Related

- [[adyen-platforms]] — managed payout context and source routes.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate application and account-level lifecycle guide.
- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separate execution-result guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02|Account managed payout schedule DELETE snapshot]]