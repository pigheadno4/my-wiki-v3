---
title: "Adyen Issuing: manage balance webhook settings"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/balance-updates/manage-balance-webhook"
raw_files:
  - "adyen/docs/issuing/balance-updates/manage-balance-webhook/2026-09-15.md"
tags: [adyen, issuing, balance-webhooks, balance-platform, pilot]
---

## Overview

This Adyen Issuing guide, captured 2026-09-15, describes Configuration API operations to view, update and delete **balance webhook settings** for a balance platform. The feature is marked **limited availability / pilot**, with processes and documentation subject to change. A setting determines which balance changes trigger notifications; this page describes configuration, not an observed webhook delivery or a transfer of funds. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Use `GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings` for the list, or append `/{settingId}` for one setting. The sample response separates the webhook ID from each setting ID and shows `type: balance`, target, currency, status and conditions.
- PATCH the individual setting route to change it. The guide marks `type: balance` as required in the PATCH body. Optional target scopes in its table are the entire `balancePlatform`, one `accountHolder`, or one `balanceAccount`; the target ID names that resource. Conditions select `available`, `balance`, `pending` or `reserved` balance and a threshold comparison (`greaterThan`, `greaterThanOrEqual`, `lessThan`, `lessThanOrEqual`) in the specified currency.
- **Preserve conditions when updating:** to add a condition, send both old and new condition sets; to remove one, omit it but send every condition to keep. If the only existing condition is removed, the guide says the setting will notify for **all balance changes in the specified balance account(s)**. Treat that as a material widening of the trigger.
- `status: active` permits a webhook if any condition in the setting is met. `inactive` suppresses delivery for the specified conditions and is the guide's temporary stop. DELETE of the individual setting is its permanent stop for those configured conditions. The all-changes statement above concerns removal of the last condition, not reactivation of an inactive setting.
- The curl commands use a test Balance Platform endpoint and illustrative resource IDs/thresholds. They show configuration request shapes, not current pilot eligibility, actual balance changes or successful webhook receipt.

## Detail locators

- Pilot and list/detail GET routes: raw lines 19–28 and 81–87; response shapes: 40–79 and 99–119.
- PATCH path/body fields, target types, status and condition vocabulary: raw lines 121–147.
- Add/remove conditions and temporary deactivation: raw lines 155–157, 191–195 and 224–238.
- Removing the last condition versus deleting a setting: raw lines 243–253.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing-balance-types]] — balance-type reference.

## Raw Sources

- [[raw/adyen/docs/issuing/balance-updates/manage-balance-webhook/2026-09-15|Adyen balance webhook setting guide, captured 2026-09-15]]
