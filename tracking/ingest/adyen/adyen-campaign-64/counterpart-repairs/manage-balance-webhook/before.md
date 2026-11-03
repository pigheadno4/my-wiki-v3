---
title: "Adyen Platforms manage balance webhook settings"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/balance-updates/manage-balance-webhook"
raw_files:
  - "adyen/docs/platforms/balance-updates/manage-balance-webhook/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, webhooks, configuration]
---

## Overview

This 2026-09-15-captured Adyen for Platforms guide explains how to list, inspect, update, deactivate, or delete **Balance webhook settings** with the Configuration API. It is marked **limited availability / pilot**; the process and documentation may change. It concerns a balance-change notification rule under a particular balance platform and webhook, not the creation of the webhook subscription itself, a balance movement, or a payout outcome. [[adyen]] · [[adyen-platforms]] · [[adyen-webhooks]]

## Key takeaways

- **Read versus update identities:** GET `/balancePlatforms/{id}/webhooks/{id}/settings` lists settings and their conditions; GET the same route with `/{settingId}` inspects one setting. These routes use the balance-platform ID and Balance webhook ID, plus the setting ID for one-setting operations. PATCH `/balancePlatforms/{id}/webhooks/{id}/settings/{id}` changes a setting. The guide's response examples show `target` (`balancePlatform` or `balanceAccount`), `currency`, `status`, and `conditions`; its update table also lists `accountHolder` as a target type. The examples are TEST payloads, not evidence that those IDs or balances exist in a live platform.
- **PATCH conditions can broaden alerts:** The page instructs sending **both existing and new** condition sets when adding one, and sending **all condition sets to keep** when removing one. Excluding a condition removes it from the updated array. Removing the only existing condition set causes updates for **all balance changes** in the specified target account(s), so an empty conditions array is not equivalent to stopping alerts. The update table lists balance types `available`, `balance`, `pending`, and `reserved`, plus comparison operators and value; the full field inventory and request examples are in the raw.
- **Stop temporarily or permanently:** PATCH `status: inactive` temporarily stops notifications for that setting's conditions. DELETE `/balancePlatforms/{id}/webhooks/{id}/settings/{id}` permanently stops notifications for the specified setting/conditions. The guide does not describe a restore operation after deletion; do not infer that disabling the parent webhook, deleting the setting, and clearing conditions have the same effect.
- **Condition logic remains qualified:** This page's `status=active` row says any condition may trigger. The related configuration guide's `conditions` row says all configured conditions must match. The two captured guides leave multi-condition Boolean behavior unresolved; a platform should verify the current API behavior before relying on a compound threshold. A read response, successful configuration change, or active setting is not proof that any notification was delivered or that the reported balance changed.

## Detail locators

- Pilot notice and Configuration API management scope: pinned raw lines 15–24.
- GET all and GET one setting, required IDs, and response examples: pinned raw lines 26–119.
- PATCH endpoint, update field table, and condition options: pinned raw lines 121–147.
- Add/remove examples requiring retained conditions in the updated array: pinned raw lines 149–220.
- Temporary inactive status, all-changes effect of removing last condition, and DELETE: pinned raw lines 224–263.
- Related configuration guide all-versus-any conflict: [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]], pinned raw lines 88–90 there; this page's active-status row is at pinned raw lines 139–140.

## Related

- [[adyen-platforms]] — main platform account and balance scope.
- [[adyen-webhooks]] — event receiver and handling context.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — prerequisite subscription, pilot limits, initial setting creation, and condition-language conflict.

## Raw Sources

- [[raw/adyen/docs/platforms/balance-updates/manage-balance-webhook/2026-09-15|Adyen Manage your balance webhook settings, captured 2026-09-15]]
