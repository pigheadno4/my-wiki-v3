---
title: "PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} — Update a sweep | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, sweeps, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}` for updating one sweep configuration under a balance account. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. A sweep's conditional push or pull configuration is distinct from an executed transfer, booked balance change or bank payout. See [[adyen-platforms]] for platform context.

## Key takeaways

- The path requires string `balanceAccountId` and `sweepId`. Every top-level request-body field is marked optional; the introduction says an omitted parameter remains unchanged. Conditional requirements still apply inside provided objects: `counterparty` requires a balance-account, transfer-instrument or merchant-account identity; `category` is required when setting `priorities`; a provided `schedule` requires its `type`, with `cronExpression` required for `cron`; provided `sweepAmount`, `targetAmount` and `triggerAmount` objects require currency and minor-unit integer value. `sweepAmount` and `targetAmount` are alternatives. [Raw: lines 7, 14–47]
- `type` is `push` or `pull`, with push named as the default; `status` is `active` or `inactive`. The trigger threshold defaults to zero and is evaluated under the specified schedule; the described push condition is balance at least the threshold, and pull is balance at most the threshold. A `balance` schedule type says execute instantly at threshold; `daily`, `weekly`, `monthly` and `cron` options have distinct timing. The currency must match a balance currency. Counterparty transitions explicitly require nulling the old `transferInstrumentId` or `balanceAccountId`; merchant-account source is restricted to pull sweeps when processing payments with Adyen. [Raw: lines 25–29, 34–47]
- Bank-transfer priorities are ordered preferences, with request acceptance when at least one priority is supported and activated for the platform; acceptance does not prove that a particular route paid out. Pull top-up sweeps from a transfer instrument start a direct-debit request and the page says to contact Adyen Support for enablement. The description is capped at 140 characters after placeholder replacement. [Raw: lines 28, 30–31]
- The 200 response is labeled request success and requires `counterparty`, uppercase `currency`, sweep `id` and `schedule`. Its other fields, including `status`, `triggerAmount`, category, direction, amount choices and reason fields, are optional in the response schema. The request example changes only `status` to `inactive`; its response example is illustrative configuration readback, not proof that a sweep fired or funds reached the destination. [Raw: lines 49–91, 193–215]

> [!warning] Contradiction
> The PATCH introduction says omitted request parameters are left unchanged [Raw: line 7], but the request and response `status` rows say an omitted status defaults to `active` [Raw: lines 37, 81]. The snapshot does not reconcile whether omission preserves an existing inactive status or activates it. Do not infer that status transition from an omitted field.

- Errors include 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server-processing. The generic 422 and 500 examples concern payment instruments, so they do not define a sweep-specific failure or transfer outcome. [Raw: lines 94–191, 217–281]

## Detail locators

- Purpose, TEST v2 server, path IDs and request schema: pinned raw lines 5–47; status-only request example: lines 49–56.
- Success response schema and optional-versus-required fields: lines 57–91; success example: lines 193–215.
- Error headings/schemas and generic examples: lines 94–191, 217–281.

## Related

- [[adyen-platforms]] — platform balance-account and sweep configuration context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02|PATCH balance-account sweep — captured 2026-11-02]]