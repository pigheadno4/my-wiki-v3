---
title: "Manage Adyen Payout Service balance webhook settings"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/balance-updates/manage-balance-webhook"
raw_files:
  - "adyen/docs/payouts/payout-service/balance-updates/manage-balance-webhook/2026-09-15.md"
tags: [adyen, payout-service, balance-webhooks, configuration-api]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service-path guide explains how to view, PATCH, deactivate and DELETE pilot Balance webhook settings through the Configuration API. It routes under [[adyen-payouts]] and concerns notification coverage, not a payout or balance movement. The pilot notice says processes and documentation may change.

## Key takeaways

- GET `/balancePlatforms/{id}/webhooks/{id}/settings` lists settings for a balance platform and webhook; GET the same path plus `/{settingId}` reads one setting and its conditions. The examples return `type: balance`, target resource, currency, `status` and `conditions`. See raw lines 26–119.
- PATCH `/balancePlatforms/{id}/webhooks/{id}/settings/{id}` to update a setting. The guide marks `type: balance` required and describes optional target scopes `balancePlatform`, `accountHolder`, `balanceAccount`, currency, status and threshold conditions. Its active-status row says any condition can trigger; the page itself does not define how to reconcile compound conditions beyond that row. See raw lines 121–147.
- **Preserve wanted conditions in PATCH:** Adding a set means sending both existing and new condition sets; removing one means excluding it while resending each condition to keep. Removing the **only** existing condition broadens the setting to updates for **all** balance changes in the target balance account(s), rather than silencing it. See raw lines 155–195 and 243–245.
- To stop delivery for a setting temporarily, PATCH `status: inactive`; to permanently stop notifications for the specified conditions, DELETE the setting by platform, webhook and setting IDs. Neither action is a transfer or payout reversal. See raw lines 224–263.
- **Example scope warning:** The GET detail example uses setting `BWHS...01` with a `balancePlatform` target (raw lines 102–118), while the PATCH “add conditions” sample reuses that setting ID but supplies a `balanceAccount` target (raw lines 161–185). The guide does not explain whether changing target is intended; do not treat this as evidence that adding a condition leaves scope unchanged. The sample curl lines also end in a bare `-d` for GET/DELETE (raw lines 33–38, 92–97, 258–263), so they are not copy-ready shell commands.

## Evidence boundary

Setting status or deletion concerns which Balance webhooks are emitted. A configuration read or accepted PATCH/DELETE does not prove that any particular underlying balance change, booking, settlement, payout or bank credit occurred. This guide is a pilot snapshot, not a current availability assertion.

## Detail locators

- Pilot and GET list/detail routes: raw lines 19–119.
- PATCH fields and retain-condition behavior: raw lines 121–220.
- Inactive, no-condition broadening and DELETE: raw lines 224–263.

## Related

- [[adyen-payouts]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/balance-updates/manage-balance-webhook/2026-09-15|Payout Service balance-webhook management guide, 2026-09-15]]
