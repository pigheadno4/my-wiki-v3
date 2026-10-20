---
title: "Adyen Issuing balance webhook use cases"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/balance-updates/use-cases"
raw_files:
  - "adyen/docs/issuing/balance-updates/use-cases/2026-09-15.md"
tags: [adyen, issuing, balance-platform, webhooks, balance-updates]
---

## Overview

This 2026-09-15-captured Issuing-path page gives Configuration API examples for balance-webhook settings at balance-platform, account-holder and individual balance-account scope, with example `balancePlatform.balanceAccount.balance.updated` events. The page marks balance webhooks **limited availability** and in pilot, with processes and documentation subject to change. These are test-environment examples, not a live event-delivery result. [[adyen]] [[adyen-issuing]]

## Key takeaways

- A platform-wide example targets `balancePlatform` and the current `balance` below USD 5,000 using `lessThan` and sample value `500000` (raw lines 26–70). A user-scoped example targets `accountHolder` and uses `lessThanOrEqual` for current balance at or below USD 5,000 (raw lines 97–141). The distinction matters at the exact threshold.
- The individual-account example targets `balanceAccount`, using `available` and `lessThan`; its prose requests notifications below JPY 1,000 for six accounts and says to create a setting for each account (raw lines 169–213). Its sample request instead uses numeric `value: 100000` and the example event `available: 95000`, without explaining the amount scale for JPY. Preserve the mismatch; do not silently interpret those figures as JPY 1,000 and JPY 950.
- The sample events use `balancePlatform.balanceAccount.balance.updated` in `environment: test` and include currency plus balance-type fields (raw lines 72–95, 143–167, 215–239). The balance-account-targeted sample includes `accountHolderId` but no `balanceAccountId` in its shown payload, so the example alone does not demonstrate identification of which of six accounts changed; `settingIds` appears, but no mapping procedure is supplied here (raw lines 222–238).

## Detail locators

- Pilot warning: raw lines 15–24. Platform-scope request table and test-host payload: raw lines 26–70; example event: raw lines 72–95.
- Account-holder scope, inclusive threshold and event: raw lines 97–167. Individual balance-account scope, per-account settings, JPY amount discrepancy and event fields: raw lines 169–239.

## Related

- [[adyen-issuing]] — Issuing and balance-account context.
- [[source-adyen-docs-issuing-balance-types]] — definitions of current and available balance.

## Raw Sources

- [[raw/adyen/docs/issuing/balance-updates/use-cases/2026-09-15|Balance webhook use cases, captured 2026-09-15]]
