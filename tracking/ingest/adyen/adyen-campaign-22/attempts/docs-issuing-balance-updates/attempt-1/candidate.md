---
title: "Adyen Issuing: Track balance updates"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/balance-updates"
raw_files:
  - "adyen/docs/issuing/balance-updates/2026-09-15.md"
tags: [adyen, issuing, balance-platform, balance-webhooks, pilot]
---

## Overview

This 2026-09-15-captured Adyen Issuing overview explains how a platform can subscribe to Balance webhooks and configure notifications for balance-account changes. Adyen marks the feature **limited availability / pilot** and says its processes and documentation may change. The page is a configuration route, not evidence of an actual balance movement or delivered webhook. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Balance changes may arise during payment lifecycles or from other financial products; the page gives incoming payments, outgoing payouts, refunds and chargebacks as examples. A Balance webhook can scope notifications to the whole balance platform, one account holder's balance accounts, or one balance account. See raw lines 24-32.
- First subscribe to the Balance webhook in Customer Area and obtain its webhook ID. Then configure settings through POST `/balancePlatforms/{id}/webhooks/{id}/settings`, specifying that ID and trigger criteria. The overview says Adyen sends a webhook when a change in the specified scope meets all configured conditions. See raw lines 34-47.
- Higher-level settings are inherited by connected balance accounts unless overridden by a more granular setting: account-holder settings override balance-platform settings, and balance-account settings override both. See raw lines 49-57.
- The linked [[source-adyen-docs-issuing-balance-updates-configure-balance-webhook]] guide's status row says a webhook can be sent if **any** condition is met, while its conditions row and this overview say **all** conditions. The captured docs do not resolve multi-condition behavior; verify the actual contract before depending on that trigger logic. See this raw line 47 and companion raw lines 88-90.
- The page points to separate guides for configuration and later viewing, updating or deleting settings. A subscription or setting is not proof of current pilot eligibility, actual notification delivery, or a resulting payment/funds outcome. See raw lines 59-67.

## Detail locators

- Pilot label, example balance-change causes and three notification scopes: raw lines 19-32.
- Customer Area subscription, configuration API path, target scopes and triggering statement: raw lines 34-47.
- Scope inheritance and override order: raw lines 49-57. Child-guide links: raw lines 59-67.

## Related

- [[adyen-issuing]] — main Issuing concept and reciprocal source route.
- [[source-adyen-docs-issuing-balance-updates-configure-balance-webhook]] — detailed settings fields and the multi-condition wording conflict.
- [[source-adyen-docs-issuing-balance-updates-manage-balance-webhook]] — setting lifecycle, including scope-widening effects of removing the last condition.

## Raw Sources

- [[raw/adyen/docs/issuing/balance-updates/2026-09-15|Adyen Issuing balance-updates overview, captured 2026-09-15]]
