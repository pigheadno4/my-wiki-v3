---
title: "Braintree iOS v7 PayPal Migration Route with JavaScript v3 Body"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/paypal-sdk-migration-guide/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/paypal-sdk-migration-guide/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios-v7, javascript-v3, migration, route-mismatch]
---

## Overview

This collected [[braintree]] website snapshot sits at an `/ios/v7` PayPal SDK migration URL, but its title and body identify a `checkout.js` to PayPal JS SDK migration for JavaScript v3 custom PayPal integrations. The body explicitly says the guide is not relevant to iOS SDK users. The sparse snapshot contains no migration procedure, iOS API, or iOS v7 behavior.

## Key takeaways

- The page's stated action is migration from `checkout.js` to the PayPal JS SDK, conditioned on a JavaScript v3 custom PayPal integration rather than Drop-in UI.
- The exclusion list also names JavaScript v2, Android and iOS SDKs, Drop-in UI, and new PayPal web integrations. These are page-scope exclusions, not support or deprecation findings for any excluded SDK.
- The `/ios/v7` route conflicts with the body and with its navigation link to an iOS v5 overview. Neither route label establishes iOS SDK version behavior or migration history. Use the actual [[braintree-ios-sdk]] evidence for native iOS integration and version boundaries, and [[braintree-web-sdk]] for browser SDK context.

> [!warning] Route/body mismatch
> Do not use this snapshot as an iOS v7 migration guide. Its captured body expressly excludes iOS SDK users, and it provides no native migration steps.

> [!warning] Website and GitHub evidence remain separate
> The lone Braintree JavaScript SDK reference link is navigation only. It was not read as evidence here and does not establish current hosted behavior, exact package behavior, SDK support status, or PayPal Web SDK v6 migration behavior.

## Detail locators

- Canonical source URL and fetched date: raw lines 1-2.
- Page title and migration identity: raw lines 6 and 14.
- JavaScript v3 custom-integration condition and Drop-in exclusion: raw lines 17-18.
- Full exclusion list, including JavaScript v2, Android, iOS, Drop-in UI, and new PayPal web integrations: raw lines 20-26.
- Unread Braintree JavaScript SDK reference navigation: `## See also`, raw lines 31-34.

## Related

- Company: [[braintree]]
- Native SDK concept: [[braintree-ios-sdk]]
- Browser SDK concept: [[braintree-web-sdk]]
- Full JavaScript v3 migration source: [[source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/ios/v7-2026-09-16|Braintree iOS v7-routed PayPal SDK migration snapshot]] - complete collected route/body-mismatch evidence
