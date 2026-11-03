---
title: "Balance Platform API: Create a balance account sweep"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/sweeps"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02.md"
tags: [adyen, balance-platform, sweeps, api]
---

## Overview

This captured Balance Platform API v2 `POST /balanceAccounts/{balanceAccountId}/sweeps` reference creates a sweep configuration to pull funds into or push funds out of a balance account according to a schedule, threshold, currency and counterparty. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. Creation is distinct from an actual transfer or bank receipt. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Path `balanceAccountId` is required. The request body has required `counterparty`, `currency` and `schedule`. Within `counterparty`, one of balance-account ID, transfer-instrument ID or merchant account is required, though each child is individually marked optional. The uppercase three-character sweep currency must match a balance currency. A merchant-account source is allowed only for a `pull` sweep when processing payments with Adyen. For automated direct-debit top-up from a transfer instrument, the reference says to combine transfer instrument and merchant account with `pull` and contact Adyen Support to enable the feature. See **Parameters**, lines 16–30.
- `schedule.type` is required: `cron`, `daily`, `weekly`, `monthly` or `balance`. `cronExpression` is required for `cron` and uses the balance account time zone; daily/weekly/monthly fixed times are stated as 07:00 CET, and `balance` triggers instantly at the threshold. Optional `type` defaults to `push`; optional `status` defaults to `active`, while `inactive` cannot be triggered. Optional `triggerAmount` defaults to zero. A `pull` triggers at balance less than or equal to threshold, a `push` at balance greater than or equal to it. See **Parameters**, lines 35–48.
- Choose at most one of optional `sweepAmount` (amount to move) and `targetAmount` (desired post-sweep balance). When an amount object is present, its currency and integer value in minor units are required. Optional `priorities` rank bank-transfer routes; `category` becomes required when they are set, and the request is accepted if at least one supplied priority is supported and activated for the platform. This acceptance does not guarantee the first priority or transfer completion. A description over 140 characters after placeholder replacement is cut off. See **Parameters**, lines 25–47.
- A 200 response marks request success and includes required sweep `id`, counterparty, currency and schedule; it may include `reason` and `reasonDetail` for a disabled sweep and other configured fields. The examples show `active` pull/push configurations, not executed transfers. The page lists 400, 401, 403, 422 and 500 errors; its generic 422/500 examples concern payment instruments and do not establish sweep-specific failure behavior. See **Responses** and **Response examples**.
- This 2026-11-02 snapshot gives a TEST server. The `latest` URL does not establish current live access, caller roles beyond the described permission errors, or account eligibility. The endpoint does not specify idempotency, deletion, propagation timing, reversal or version-conflict behavior.

## Detail locators

- **Parameters**, lines 14–48: required fields, nested conditions, defaults, units, threshold and priority behavior.
- **Request examples**, lines 50–112: illustrative pull, push and prioritized push bodies.
- **Responses**, lines 113–247: returned fields and error schema.
- **Response examples**, lines 249–382: illustrative configurations and generic errors.

## Related

- [[adyen-platforms]] — platform balance-account and sweep context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/sweeps/2026-11-02|Captured sweep creation API reference (2026-11-02)]]
