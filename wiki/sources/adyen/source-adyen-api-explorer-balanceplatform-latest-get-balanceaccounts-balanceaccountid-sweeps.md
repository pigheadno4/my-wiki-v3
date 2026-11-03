---
title: "Adyen Balance Platform API v2: Get sweeps for a balance account"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, sweeps, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API Explorer capture documents `GET /balanceAccounts/{balanceAccountId}/sweeps` on the listed TEST `/bcl/v2` server. It reads paginated sweep configurations associated with one balance account. Reading a configuration is separate from a triggered transfer, booked balance-account movement or bank receipt. The `latest` URL and TEST server do not establish current version, LIVE availability or account eligibility.

## Key takeaways

- `balanceAccountId` is a required string path parameter identifying the balance account. Optional integer query parameters `limit` and `offset` control page size and skipped items: default `limit` is 10 and maximum is 100. No request body or idempotency header is specified.
- The 200 schema requires `hasNext`, `hasPrevious` and a `sweeps` array. Each listed sweep requires `counterparty`, `currency`, sweep `id` and `schedule`; `schedule.type` is required within the schedule. The sweep ID is distinct from the path balance-account ID and counterparty identifiers. `counterparty` is a source or destination depending on sweep direction; the prose requires one of `balanceAccountId`, `transferInstrumentId` or `merchantAccount` within it, even though each child is marked optional in the table. `merchantAccount` is limited to pull sweeps when processing payments with Adyen; transfer-instrument pull top-ups carry a separate enablement note.
- Optional configuration fields include `category` (bank or internal, required when setting `priorities`), `priorities`, status, references, description, `sweepAmount`, `targetAmount`, `triggerAmount` and direction `type`. The page says `sweepAmount` and `targetAmount` are alternatives; amount children `currency` and integer minor-unit `value` are required within each present amount object. It describes default `status=active`, default `type=push` and default `triggerAmount=0` when those fields are omitted. Those are configuration descriptions in the returned sweep schema, not evidence that this GET mutates or triggers a sweep.
- `schedule.type` covers cron, daily, weekly, monthly and balance-triggered evaluation; `cronExpression` is required when the schedule type is cron. The raw schema gives schedule times/time zone, direction-specific threshold comparisons, and priority fallback detail; use those locators before implementing a schedule or route. `active` means enabled for potential triggering, while `inactive` cannot trigger; neither value proves an executed transfer.
- The page documents 400, 401 authentication, 403 permission, 422 validation and 500 errors. The generic 422 and 500 example payloads refer to changing or creating a payment instrument, although this endpoint lists sweeps. Treat those examples as generic error illustrations, not sweep-update/create semantics or guaranteed failure causes.

> [!warning] Contradiction
> The 422 example says a `balanceAccountId` can only be changed in an inactive or requested payment instrument, and the 500 example says payment-instrument creation failed (raw lines 240–265). This GET has no update/create request body and its 200 result lists sweeps. Those example details do not define this endpoint's lifecycle or failure conditions.

## Detail locators

- Raw lines 5–26: list purpose, pagination example, TEST v2 server and path/query parameters.
- Raw lines 28–65: 200 response and sweep-configuration schema, including identity, counterparties, schedule, status, amounts, direction and defaults.
- Raw lines 68–165: 400, 401, 403, 422 and 500 error schemas.
- Raw lines 167–266: one success example and generic error examples; payment-instrument wording is at lines 240–265.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]
- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts]]
- [[source-adyen-docs-platforms-top-up-balance-account-scheduled-top-ups]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02|Adyen Balance Platform API Explorer GET balance-account sweeps (captured 2026-11-02)]]
