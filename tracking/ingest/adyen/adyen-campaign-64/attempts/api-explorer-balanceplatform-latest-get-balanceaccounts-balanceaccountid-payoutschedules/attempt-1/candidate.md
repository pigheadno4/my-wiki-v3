---
title: "Adyen Balance Platform API v2: GET managed payout schedules on a balance account"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, managed-payouts, api]
---

## Overview

This 2026-11-02 Balance Platform API reference lists managed payout schedules configured on one balance account, with optional pagination and currency filtering. Its captured server is the TEST `/bcl/v2` endpoint; `latest` is a documentation route, not proof of current live availability. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required string path `balanceAccountId` identifies the balance account. Optional query inputs are `limit` (default 10, maximum 100 items per page), prior-response `cursor`, and a three-character ISO `currency` filter. No request body is listed.
- A 200 returns a required `balanceAccountPayoutSchedules` array and required `link` pagination object. Each returned schedule marks `balanceAccountId`, `balancePlatformPayoutScheduleId`, `createdAt`, and `transferInstrumentId` required. The balance-account schedule's own `id` is optional in this table; it is distinct from the platform schedule ID and payout destination transfer-instrument ID.
- Optional schedule fields describe currency, enabled state, frequency (`daily`, `weekdays`, `weekly`, `monthly`), timing, amount bounds, retained funds, description, and references. `frequencyValue` is allowed only for monthly (1–31, with documented weekend/month-end adjustments) or weekly (1–5). Description can be truncated beyond 140 characters; beneficiary reference supports alphanumeric characters. `description`, `frequency`, `frequencyValue`, and beneficiary reference default from the applied platform schedule; minimum/maximum payout and retained amounts each default to 0. If funds are below the retained amount, an execution is not initiated. The raw schema owns exact limits and time-zone detail.
- This is a configuration read. Even `enabled: true` or a returned transfer-instrument ID does not show that an execution was initiated, a transfer succeeded, funds were booked, or a recipient bank received a payout. The listed 401, 404, 422 and 500 responses concern authentication, missing resource, validation and server failure. The reference does not specify a caller role, GET idempotency key, schedule deletion/propagation behavior, version conflict, or payout outcome.

## Detail locators

- Purpose, TEST server, path and query inputs: pinned raw lines 5–25.
- 200 array, schedule identities, defaults/limits/timing and pagination links: pinned raw lines 27–63.
- Error schemas: pinned raw lines 66–139; illustrative 200 JSON: lines 141–172.

## Related

- [[adyen-platforms]] — platform balance-account and managed-payout context.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate dated schedule lifecycle guide.
- [[source-adyen-docs-platforms-managed-payouts]] — separate dated managed-payout overview.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02|Balance Platform GET balance-account payout schedules snapshot]]