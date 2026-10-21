---
title: "Configure Adyen Marketplace balance webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/balance-updates/configure-balance-webhook"
raw_files:
  - "adyen/docs/marketplaces/balance-updates/configure-balance-webhook/2026-09-15.md"
tags: [adyen, marketplaces, platforms, balance-accounts, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace-path guide describes a pilot Balance webhook setup for notifications about balance changes on a platform, a specified account holder's balance accounts, or one balance account. It belongs under [[adyen-platforms]]. An alert rule or delivered notification is balance-change monitoring, not proof of a particular transfer's booking, settlement, payout or bank receipt.

## Key takeaways

- **Limited availability:** Balance webhooks are in pilot and processes/documentation may change. Subscribe to the Balance webhook in Customer Area, configure its destination/security there, then use the Configuration API and the saved webhook ID to create settings. The guide requires a Configuration API credential with Balance Platform BCL role and a Customer Area Merchant technical integrator or Merchant admin role. See raw lines 19–39 and 41–75.
- POST `/balancePlatforms/{id}/webhooks/{id}/settings` with `type: balance`, `target.type` and `target.id`, `currency`, and `status`. Targets are `balancePlatform`, `accountHolder`, or `balanceAccount`; an account-holder target covers its balance accounts. `active` enables and `inactive` suppresses notifications for that setting. Save the returned setting ID to manage the setting or match an event. See raw lines 73–90 and 125–146.
- Each Balance webhook supports at most 20 settings, each with at most 20 condition sets. Optional conditions choose `available`, `balance`, `pending`, or `reserved` balance type, one of four greater/less comparisons, and a currency-specific threshold value. With no conditions, the guide says updates are sent for all balance changes within the specified target. See raw lines 39 and 90–96.
- **Condition conflict:** The `status` description says an active setting sends if **any** condition is met; the `conditions` description says a balance change must meet **all** set conditions. The page does not resolve the disagreement. Do not assume multi-condition AND/OR behavior from this guide alone. See raw lines 88–90.
- Customer Area setup includes webhook URL, encryption protocol, Basic authentication and HMAC key; the HMAC key must be copied when generated because the guide says it cannot be copied later. Accept each received webhook. The example sets an available-balance threshold below USD 5,000 on a liable balance account; it is a configuration example, not evidence of an actual balance change. See raw lines 45–71, 98–149.
- Troubleshooting examples cover duplicate conditions (`1047_002`), unknown target account (`1047_404`) and invalid currency (`1047_001`). The latter two “resend POST” solution links point to a PATCH endpoint and include a setting ID; treat those links as an internal documentation inconsistency and verify the intended request before implementation. See raw lines 151–244.

## Detail locators

- Pilot status, role gates, scope and 20-by-20 limits: raw lines 19–39.
- Customer Area subscription/security and Configuration API fields: raw lines 41–96.
- Liable-account threshold example and setting ID: raw lines 98–149.
- Error payloads and remedy-link discrepancy: raw lines 151–244.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]]
- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/balance-updates/configure-balance-webhook/2026-09-15|Marketplace balance-webhook configuration guide, 2026-09-15]]
