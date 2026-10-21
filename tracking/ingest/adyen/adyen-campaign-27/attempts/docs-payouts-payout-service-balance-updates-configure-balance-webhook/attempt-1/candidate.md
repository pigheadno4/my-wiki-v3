---
title: "Payout Service path: configure balance webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/balance-updates/configure-balance-webhook"
raw_files:
  - "adyen/docs/payouts/payout-service/balance-updates/configure-balance-webhook/2026-09-15.md"
tags: [adyen, payout-service, platforms, balance-accounts, webhooks, configuration]
---

## Overview

This 2026-09-15-captured [[adyen]] page sits under the **Payout Service** documentation path but describes **balance-platform Balance webhook** subscription in Customer Area and condition settings through the Configuration API. It is marked **limited availability / pilot**. A setting may target the entire balance platform, one account holder's balance accounts, or one balance account. This configures alerts; it is not evidence of a live balance, completed payout, bank receipt or applicability to legacy Payout API webhooks. [[adyen-platforms]]

## Key takeaways

- Subscribe to and enable the Balance webhook under Customer Area's **Platforms** tab, configure the receiver URL/security and retain its webhook ID. The guide calls for Basic authentication, an HMAC key and acceptance of delivered events. The Configuration API credential needs the **Balance Platform BCL role**, while the Customer Area user needs **Merchant technical integrator** or **Merchant admin**. It states a maximum of 20 settings per Balance webhook and 20 condition sets per setting. See raw lines 19–71 and 149.
- Settings use POST `/balancePlatforms/{id}/webhooks/{id}/settings` with balance-platform and webhook IDs. The table marks `type=balance`, `target` type/id, `currency` and `status` required; `conditions` is optional. Targets are `balancePlatform`, `accountHolder`, or `balanceAccount`. No conditions means changes across all target account(s); `inactive` suppresses messages even if conditions match. Record the returned setting ID for later management or event matching. See raw lines 73–96 and 125–147.
- **Condition-wording conflict:** the `status=active` row says a webhook is sent if **any** condition matches, while the `conditions` row says **all** configured conditions must match. The page does not resolve multi-condition Boolean behavior. Condition types cover available/current/pending/reserved balances and greater/less-than comparisons. See raw lines 88–96.
- The USD 5,000 available-balance example is a TEST illustration for a liable balance account, not a default threshold or proof of its funds. The prose gives the nested settings POST route, but the cURL example points only to `/bcl/v2/balancePlatforms`, so it is not a complete settings URL. Troubleshooting illustrates duplicate condition `1047_002`, unknown account `1047_404` and invalid currency `1047_001`; later “resend POST” wording links PATCH-style settings URLs. Verify the current API route before implementation. See raw lines 75, 98–147 and 151–244.

## Detail locators

- **Pilot scope, subscription and target options:** raw lines 15–30.
- **Roles, 20-by-20 limits and Customer Area receiver setup:** raw lines 32–71.
- **Settings route, fields and all-versus-any conflict:** raw lines 73–96.
- **TEST liable-account threshold, shortened cURL path and setting ID:** raw lines 98–149.
- **Error examples and method/link inconsistencies:** raw lines 151–244.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — Payout Service documentation path, separate from legacy Payout API
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook|Parallel Platforms-path balance webhook guide]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/balance-updates/configure-balance-webhook/2026-09-15|Adyen Payout Service path balance webhook configuration — collected 2026-09-15]]
