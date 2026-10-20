---
title: "Adyen Issuing: Configure balance webhooks"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/balance-updates/configure-balance-webhook"
raw_files:
  - "adyen/docs/issuing/balance-updates/configure-balance-webhook/2026-09-15.md"
tags: [adyen, issuing, balance-platform, webhooks]
---

## Overview

This 2026-09-15-captured Issuing-path guide describes subscribing to Balance webhooks in Customer Area and configuring balance-change notification conditions with the Balance Platform Configuration API. Adyen labels the feature **Limited availability** and says it is in pilot, with processes and documentation subject to change. The notifications can help monitor balances; the page does not claim they prevent a negative balance. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Subscribe to the Balance webhook in Customer Area, then use the webhook ID and balance platform ID in a Configuration API settings request. The guide lists **Balance Platform BCL role** for the Configuration API credential and at least one Customer Area role, **Merchant technical integrator** or **Merchant admin**. Customer Area setup includes a public server URL and encryption protocol; its HMAC key must be copied and saved when generated because it cannot be copied later.
- A setting targets the whole `balancePlatform`, all balance accounts of one `accountHolder`, or one `balanceAccount`, with a target ID and currency. An `active` setting can trigger when its conditions are met; `inactive` suppresses notifications even when met. The status row says an `active` setting receives a webhook if *any* condition is met, while the conditions row says a balance change must meet *all* conditions; this is an unresolved contradiction. Check the linked API reference or verified behavior before relying on multi-condition triggers. With no conditions, the guide says updates are sent for all balance changes in the specified balance account(s). The documented maxima are 20 settings per Balance webhook and 20 condition sets in each setting.
- The prose specifies POST `/balancePlatforms/{id}/webhooks/{id}/settings`, but the illustrated curl posts to `/bcl/v2/balancePlatforms` without the webhook settings path. Treat the example as illustrative, not a verified endpoint. The troubleshooting sections also label resubmission as POST while linking a PATCH settings URL. Check the linked API reference for implementation.
- Keep the returned setting `id` for subsequent view, modification, deletion or matching an event to a setting, and accept received webhooks. The guide lists duplicate conditions (`1047_002`), missing target account (`1047_404`) and invalid currency (`1047_001`) as example setup errors.

## Detail locators

- Pilot status, purpose, subscription and scope choices: raw lines 15–30. Credential/Customer Area roles and maxima: lines 32–39. Customer Area creation, server/security fields and webhook ID: lines 41–71.
- Stated settings endpoint and field meanings, including target, status, conditions, balance types and comparisons: lines 73–96. The liable-account threshold example and shortened curl endpoint: lines 98–123; response `id` and event acceptance: lines 125–149.
- Troubleshooting error payloads and suggested corrections: lines 151–244. Related use-case, settings-management and funding guides: lines 246–258.

## Related

- [[adyen-issuing]] — Issuing source route.
- [[adyen-index]] — Adyen source catalog.

## Raw Sources

- [[raw/adyen/docs/issuing/balance-updates/configure-balance-webhook/2026-09-15|Configure balance webhooks, captured 2026-09-15]]
