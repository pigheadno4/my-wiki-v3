---
title: "Adyen Platforms: track balance updates"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/balance-updates"
raw_files:
  - "adyen/docs/platforms/balance-updates/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, balance-webhooks, notifications]
---

## Overview

This 2026-09-15 Adyen for Platforms overview describes a limited-availability Balance webhook pilot for notifications when a configured balance-change rule matches. A rule may cover all balance accounts in a balance platform, all accounts of one account holder, or one balance account. The page explains subscription, settings creation and inheritance; it is not evidence that an account currently has the pilot, that a notification was delivered, or that a payment, payout or top-up completed. See [[adyen]], [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- **Pilot and purpose:** The page says Balance webhooks are in pilot and the process/documentation may change. Balance changes can arise from payment lifecycle or financial products; it gives incoming payments, payouts, refunds and chargebacks as examples of events affecting Available. These are examples of possible changes, not a universal timing or amount rule for each operation.
- **Configure notification scope:** Subscribe to the **Balance webhook** in Customer Area and obtain its webhook ID. Configure settings with `POST /balancePlatforms/{id}/webhooks/{id}/settings`, naming that ID and trigger criteria. A setting may target the entire balance platform, one account holder's balance accounts, or a single balance account. The overview does not specify detailed request fields, roles, quotas or security setup; use [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] for those details.
- **Inheritance and override:** Platform-level settings apply broadly, account-holder settings inherit and override platform rules for that user's accounts, and balance-account settings inherit and override higher-level rules for that account. A more specific configuration can therefore change which account changes prompt an alert. The page says Adyen sends an event when all configured conditions are met, but the related configuration guide's `status=active` row says any condition can trigger; the captured sources leave compound-condition logic unresolved. Verify current behavior before relying on it for automatic control decisions.
- **Action boundary:** An alert reports a matching balance change according to the configured rule. It does not itself cause or prove a transfer, top-up, refund, chargeback or beneficiary-bank receipt. Manage existing settings through the separate [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] route; disabling, deleting and clearing conditions have different implications there.

## Detail locators

- Pilot notice, example balance-change causes and target scopes: raw lines 15–32. Subscribe, obtain webhook ID, settings POST and matching event: lines 34–47. Platform/account-holder/balance-account inheritance and override table: lines 49–57. Links to configuration and management guides: lines 59–67.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — balance-platform, account-holder and balance-account context.
- [[adyen-webhooks]] — general webhook handling context.
- [[source-adyen-docs-platforms-balance-types]] — definitions of the per-currency balance types being monitored.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — detailed pilot setup, roles, security, limits and unresolved all-versus-any condition wording.
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — reading, changing, deactivating or deleting settings.

## Related raw API references

- The raw page links to Configuration API balance-webhook settings and the linked configuration/management procedures. Consult them separately for current schema and availability.

## Raw Sources

- [[raw/adyen/docs/platforms/balance-updates/2026-09-15|Adyen Docs: Track balance updates (2026-09-15 snapshot; pilot)]]
