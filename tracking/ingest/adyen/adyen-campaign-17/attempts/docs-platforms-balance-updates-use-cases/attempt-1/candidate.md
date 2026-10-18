---
title: "Adyen Platforms balance webhook use cases"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/balance-updates/use-cases"
raw_files:
  - "adyen/docs/platforms/balance-updates/use-cases/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, webhooks, examples]
---

## Overview

This 2026-09-15-captured Adyen for Platforms page provides **TEST examples** of Balance webhook settings and matching balance-update event payloads for three alert scopes. Balance webhooks are marked **limited availability / pilot**, with processes and documentation subject to change. The page illustrates configuration and event shape, not a live account balance, completed transfer, payout, or bank receipt. [[adyen]] · [[adyen-platforms]] · [[adyen-webhooks]]

## Key takeaways

- **Three target scopes:** To alert when any balance account's **current balance** drops below USD 5,000, the first example targets `balancePlatform`, sets `conditions.balanceType: balance`, and uses `lessThan`. To alert when any of a particular user's balance accounts reaches or drops below USD 5,000, the second targets that `accountHolder` and uses `lessThanOrEqual`. To monitor **available balance** for six separate users' foreign-currency balance accounts, the third instructs one `balanceAccount` setting per account, each with its own currency and threshold. These are alternative example scopes; the platform, account holder, and balance account are distinct resource identities.
- **Event shape and evidence limit:** Each example's `balancePlatform.balanceAccount.balance.updated` event is marked `environment: test` and shows `settingIds`, platform, currency, and `balances` including `available`, `pending`, `reserved`, and `balance`. The user-target and individual-account examples include `accountHolderId`; the shown event data does **not** include a `balanceAccountId`, even for the individually targeted example. A sample `settingIds` value or account-holder ID is not by itself proof of which balance account changed in a real event. Use the actual payload and setting lookup rather than assuming identifiers not shown here.
- **Threshold units need verification:** The first two examples label USD 5,000 and send `value: 500000`. The third labels a JPY 1,000 threshold but sends `value: 100000`, while its test event reports `available: 95000`. This page does not explain that scaling. The separate Adyen currency-code guide says JPY has no decimal minor units, so the JPY narrative/value pairing conflicts with that general convention if used as a minor-unit amount. Do not copy the JPY numeric value as a validated JPY 1,000 setting without checking the current Balance webhook API contract.
- **Related configuration caveat:** The examples each use **one** condition and therefore do not resolve the related configuration guide's conflict between its active-status row (“any” condition) and its conditions row (“all” conditions). The configuration guide owns subscription, roles, 20-setting/20-condition limits, and setup; this page is an example catalog only.

## Detail locators

- Pilot notice, scope and example intent: pinned raw lines 15–24.
- Platform-wide current-balance example: pinned raw lines 26–95.
- Account-holder current-balance example: pinned raw lines 97–167.
- Separate balance-account available-balance settings, JPY value and event payload: pinned raw lines 169–239.
- Related all-versus-any configuration conflict: [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]], pinned raw lines 88–90 there.
- JPY no-decimal general convention: [[source-adyen-docs-development-resources-currency-codes]], pinned raw lines 164–172 there.

## Related

- [[adyen-platforms]] — main Platforms source route.
- [[adyen-webhooks]] — general webhook handling and event scope.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — initial subscription, settings fields, roles, and limits.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — later setting updates and deletion.
- [[source-adyen-docs-development-resources-currency-codes]] — JPY minor-unit comparison.

## Raw Sources

- [[raw/adyen/docs/platforms/balance-updates/use-cases/2026-09-15|Adyen Balance webhook example use cases, captured 2026-09-15]]
