---
title: "Adyen Platforms balance webhook configuration"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/balance-updates/configure-balance-webhook"
raw_files:
  - "adyen/docs/platforms/balance-updates/configure-balance-webhook/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, webhooks, configuration]
---

## Overview

This 2026-09-15-captured Adyen for Platforms guide describes how to subscribe to a Balance webhook in Customer Area and configure settings through the Configuration API so Adyen can notify a platform about balance changes. It is marked **limited availability / pilot**; process and documentation can change. The target can be the entire balance platform, all balance accounts of one account holder, or one balance account. This is alert configuration, not proof of a particular balance, transfer, payout, or bank receipt. [[adyen]] · [[adyen-platforms]] · [[adyen-webhooks]]

## Key takeaways

- **Two-step setup and access:** Subscribe to and enable the Balance webhook under the Customer Area Platforms tab, configure the receiver URL/security, and record the webhook ID. The page instructs setting Basic authentication and generating/storing an HMAC key, then accepting received events. A Configuration API credential needs the **Balance Platform BCL role**; the Customer Area user needs **Merchant technical integrator** or **Merchant admin**. Use the webhook ID and balance-platform ID in the settings request. These are setup instructions; the snapshot does not prove a subscription or delivered event in any account.
- **Setting scope and limits:** The settings POST route is `/balancePlatforms/{id}/webhooks/{id}/settings`. The table marks `type=balance`, `target` and its type/id, `currency`, and `status` as required, while `conditions` is optional. Target types are `balancePlatform`, `accountHolder`, and `balanceAccount`; an account-holder target covers that user's balance accounts, whereas a balance-account target covers one account. The documented cap is 20 settings per Balance webhook and 20 condition sets per setting. Record the returned setting ID to view, modify, delete, or match an event to a setting.
- **Condition semantics and conflict:** Optional conditions specify balance type (`available`, `balance`, `pending`, `reserved`), comparison (`greaterThan`, `greaterThanOrEqual`, `lessThan`, `lessThanOrEqual`), and value. The conditions row says **all** configured conditions must match and an empty array covers all changes in the target accounts. But the `status=active` row says a webhook arrives if **any** condition matches; the page does not reconcile this all-versus-any conflict. `inactive` suppresses notifications even when its conditions match. Do not infer reliable multi-condition Boolean behavior from this snapshot alone.
- **Example and troubleshooting limits:** The USD 5,000 available-balance threshold on a liable balance account is a TEST example, not a default threshold or evidence of that account's state. The prose names the nested settings POST endpoint, but the example cURL points only to `/bcl/v2/balancePlatforms`; use the cited API route rather than treating that cURL as a complete settings request. The troubleshooting section illustrates duplicate conditions (`1047_002`), unknown target account (`1047_404`), and invalid currency (`1047_001`); its later “resend POST” text links PATCH-style settings URLs, another example-level inconsistency. These errors do not establish an actual webhook delivery outcome.

## Detail locators

- Pilot notice, notification purpose, subscription, and target scopes: pinned raw lines 15–30.
- Credential/Customer Area roles and 20-by-20 limits: pinned raw lines 32–39.
- Customer Area subscription, receiver security, and webhook ID: pinned raw lines 41–71.
- Settings endpoint, required/optional fields, target/currency/status/condition rows and all-versus-any wording: pinned raw lines 73–96.
- TEST USD 5,000 example, shortened cURL path, returned setting ID and event acceptance: pinned raw lines 98–149.
- Troubleshooting codes and inconsistent resend links: pinned raw lines 151–244.

## Related

- [[adyen-platforms]] — platform/account-holder/balance-account scope and reciprocal route.
- [[adyen-webhooks]] — general webhook receiver and event-handling context.
- [[source-adyen-docs-platforms-payout-amount]] — balance calculations for payout caps, separate from these alert rules.

## Raw Sources

- [[raw/adyen/docs/platforms/balance-updates/configure-balance-webhook/2026-09-15|Adyen Configure balance webhooks, captured 2026-09-15]]
