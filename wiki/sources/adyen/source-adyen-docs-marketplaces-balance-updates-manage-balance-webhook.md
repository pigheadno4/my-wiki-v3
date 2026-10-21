---
title: "Adyen Marketplace: Manage Balance webhook settings"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/balance-updates/manage-balance-webhook"
raw_files:
  - "adyen/docs/marketplaces/balance-updates/manage-balance-webhook/2026-09-15.md"
tags: [adyen, marketplaces, platforms, webhooks, balance-accounts, configuration]
---

## Overview

This 2026-09-15 Marketplace-path guide explains how to list, inspect, update, deactivate or delete **Balance webhook settings** using the Configuration API. Adyen labels Balance webhooks **limited availability / pilot** and warns the process and documentation may change. A setting controls notifications for balance changes in a target scope; it is distinct from the webhook subscription, an actual balance movement or a payout. See [[adyen]], [[adyen-webhooks]] and [[adyen-platforms]].

## Key takeaways

- **Read and address settings:** GET `/balancePlatforms/{id}/webhooks/{id}/settings` lists settings and conditions; append `/{settingId}` to inspect one. The path requires a balance-platform ID and Balance webhook ID, plus a setting ID for single-setting operations. The TEST examples show a platform-wide target and a specific liable balance account; the PATCH field table also lists account-holder scope. The example IDs and USD thresholds do not establish live account state (raw lines 26–119, 121–147).
- **PATCH replaces the condition set being kept:** PATCH the same single-setting path to change a setting, with `type: balance` marked required. Supported target types are `balancePlatform`, `accountHolder` and `balanceAccount`; the table also lists currency, status, four balance types (`available`, `balance`, `pending`, `reserved`), comparison operators and value. To add a condition, send both retained and new conditions. To remove one, omit it while sending every condition to keep. Removing the last condition causes notifications for **all** balance changes in the target account(s), rather than stopping notifications (raw lines 121–220, 243–245).
- **Stop and delete differ:** PATCH `status: inactive` temporarily suppresses notifications even if thresholds match. DELETE the setting path to permanently stop notifications for its conditions. This guide does not describe a restore-after-delete operation. Do not equate deleting the setting, marking it inactive, and clearing its conditions (raw lines 224–263).
- **Compound-condition ambiguity:** This page's `status: active` row says any condition may trigger, while the related Platforms configuration guide's `conditions` row says all configured conditions must match; its own active row also says any. The snapshot therefore does not settle the Boolean behavior of a multi-condition setting. A stored setting or successful PATCH is not evidence that a webhook was delivered or that funds moved (this raw lines 139–141; [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] raw lines 88–90).

## Detail locators

- Pilot warning and Configuration API scope: pinned raw lines 15–24.
- GET-all and GET-one paths, IDs and TEST response examples: pinned raw lines 26–119.
- PATCH path and field/target/condition table: pinned raw lines 121–147.
- Retain-all-desired-conditions PATCH examples: pinned raw lines 149–220.
- Inactive PATCH, last-condition all-changes effect, permanent DELETE: pinned raw lines 224–263.
- Related all-versus-any condition conflict: [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] raw lines 88–90; this raw lines 139–141.

## Related

- [[adyen-webhooks]] — main asynchronous notification concept.
- [[adyen-platforms]] — platform/account-holder/balance-account context.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — parallel Platforms-path settings guide.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — initial subscription and condition-language conflict.

## Raw Sources

- [[raw/adyen/docs/marketplaces/balance-updates/manage-balance-webhook/2026-09-15|Marketplace manage Balance webhook settings, captured 2026-09-15]]
