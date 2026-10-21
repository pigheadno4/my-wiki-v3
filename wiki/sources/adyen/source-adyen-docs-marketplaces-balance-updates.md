---
title: "Adyen Marketplace: Track balance updates"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/balance-updates"
raw_files:
  - "adyen/docs/marketplaces/balance-updates/2026-09-15.md"
tags: [adyen, marketplaces, platforms, balance-accounts, balance-webhooks]
---

## Overview

This 2026-09-15 Marketplace overview describes Adyen's **limited-availability / pilot** Balance webhook for configured notifications about balance changes. It routes from subscription in Customer Area to scoped settings creation and explains platform, account-holder and balance-account setting inheritance. The snapshot is a notification overview, not evidence that this pilot is currently available to an account, an event was delivered, or a payment, refund, payout or bank receipt occurred. See [[adyen]], [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- **Scope and purpose:** The page gives payments, payouts, refunds and chargebacks as examples of activity that can change a user's available balance; they are examples, not a universal posting schedule or amount rule. Notifications can target all balance accounts of a platform, all accounts of a particular account holder, or one balance account. The platform defines trigger criteria. Balance webhooks remain labeled pilot and the processes/documentation may change (raw lines 19–32).
- **Two setup steps:** Subscribe to **Balance webhook** in Customer Area and obtain its webhook ID, then create settings with `POST /balancePlatforms/{id}/webhooks/{id}/settings` using that ID and criteria. A platform target covers its accounts, an account-holder target covers a specific user's accounts, and an account target covers one. Detailed roles, security fields and limits belong to the linked configuration guide, not this overview (raw lines 34–45, 59–67).
- **Inheritance and condition conflict:** The page states higher-resource settings are inherited by connected balance accounts and more-granular settings override higher-level settings: account holder over platform, balance account over holder/platform. It says a balance webhook is sent when **all** configured conditions match. The related [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] captures a `status: active` row saying **any** condition can trigger alongside its own all-condition row. The snapshot therefore leaves compound-condition Boolean behavior unresolved; do not infer an automatic control decision from one interpretation alone (this raw lines 47–57; related source raw lines 88–90).
- **Event boundary:** A configured rule or matching notification concerns a balance-change alert. It neither causes nor independently proves a particular underlying transfer, refund, payout, settlement or bank credit. The linked management guide distinguishes modifying, deactivating and deleting a setting; this overview itself gives no event-delivery guarantee (raw lines 24–26, 59–67).

## Detail locators

- Pilot status, example balance-change causes and three target scopes: pinned raw lines 19–32.
- Customer Area subscription, webhook ID and settings POST: pinned raw lines 34–45.
- All-condition wording and platform/holder/account inheritance-override table: pinned raw lines 47–57.
- Configuration and management next-step routes: pinned raw lines 59–67.
- Cross-page all-versus-any warning: [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] raw lines 88–90.

## Related

- [[adyen-platforms]] — main platform and Marketplace balance-account context.
- [[adyen-webhooks]] — asynchronous notification handling.
- [[source-adyen-docs-platforms-balance-updates]] — parallel Platforms-path overview.
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — detailed setup and unresolved condition wording.
- [[source-adyen-docs-marketplaces-balance-updates-manage-balance-webhook]] — Marketplace-path settings lifecycle, including condition removal.

## Raw Sources

- [[raw/adyen/docs/marketplaces/balance-updates/2026-09-15|Marketplace Track balance updates, captured 2026-09-15]]
