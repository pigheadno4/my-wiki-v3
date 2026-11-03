---
title: "Adyen Balance Platform API v2: Get a sweep"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md"
tags: [adyen, platforms, balance-platform, sweeps, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST `GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}` reference. It reads a sweep configuration identified by required balance-account and sweep path IDs for [[adyen]] [[adyen-platforms]]. Reading configuration is distinct from observing a sweep execution or financial result.

## Key takeaways

- A 200 reports the sweep `id`, `counterparty`, `currency`, and `schedule` as required response fields. `counterparty` is a source or destination depending on pull/push direction; one of balance-account ID, transfer-instrument ID, or merchant account is required by prose. Merchant account is limited to pull sweeps when processing payments with Adyen. Transfer-instrument top-up pull sweeps require a merchant account in the described setup and Adyen Support enablement.
- The response can describe bank or internal `category`, bank-transfer `priorities`, `status`, `type`, and amounts. `sweepAmount` and `targetAmount` are mutually exclusive configurations. Nested amount currency and minor-unit value are required when their object is present. `triggerAmount` defaults to zero; direction defaults to push and status defaults to active according to response descriptions. These are documented configuration defaults, not evidence of a particular execution.
- `schedule` is required and its nested `type` is required: cron, daily, weekly, monthly, or balance. Cron requires a five-part expression and uses the balance account time zone; daily, weekly and monthly descriptions give 07:00 CET timing; balance evaluates immediately upon the threshold. A pull threshold uses balance less than or equal to `triggerAmount`, while push uses greater than or equal.
- Bank-transfer priorities are ordered preferences, with fallback when an earlier one is unsupported or unavailable; the response description says acceptance requires at least one supported and activated priority. This GET snapshot does not establish that a priority is currently enabled for a given platform or that a bank transfer occurred. Optional `reason` and `reasonDetail` describe disabled sweeps.
- The 200 sample is an active daily push to another balance account with zero target and trigger values. It illustrates a returned configuration, not an execution. Generic 422 and 500 error examples mention payment instruments and should not be treated as sweep-specific failure behavior.

## Detail locators

- Operation, TEST server and path IDs: pinned raw lines 5–18. Full 200 field table, defaults and conditional fields: lines 20–54. Success example: lines 156–182.
- Error classes 400/401/403/422/500: lines 57–154; generic error examples: lines 184–248.

## Related

- [[adyen-platforms]] — platform balance-account and sweep context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02|Pinned 2026-11-02 API reference]]
