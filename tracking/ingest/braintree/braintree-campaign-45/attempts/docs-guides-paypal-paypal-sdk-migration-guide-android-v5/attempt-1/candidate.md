---
title: "Braintree PayPal SDK Migration Route - Android v5 (JavaScript v3-only notice)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/paypal-sdk-migration-guide/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/paypal-sdk-migration-guide/android/v5-2026-09-16.md"
tags: [braintree, paypal, android-v5, javascript-v3, migration, scope-warning]
---

## Overview

This collected [[braintree]] website snapshot sits at an Android v5 URL, but its retained title and availability notice identify a `checkout.js`-to-PayPal-JS-SDK migration page for JavaScript v3 custom PayPal integrations. The page explicitly says it is not relevant to Android or iOS SDK users. Treat it as historical evidence of a route/body scope mismatch, not as an Android migration guide.

The retained body contains only the applicability notice and a Braintree JavaScript SDK reference link; it does not preserve migration steps. It therefore does not establish native Android v5 migration actions, current Android or browser SDK support, hosted PayPal behavior, merchant eligibility, or payment execution.

## Key takeaways

- The central action for a reader of this snapshot is scope triage: do not use this Android-labeled route to migrate an Android integration. The separate [[source-braintree-client-sdk-migration-android-v5]] covers the historical Braintree Android SDK v4-to-v5 migration.
- The retained notice applies only to JavaScript v3 custom PayPal integrations and excludes JavaScript v2, Android, iOS, Drop-in UI and new PayPal web integrations.
- The page title names migration from `checkout.js` to the PayPal JS SDK, but this Android-routed snapshot omits the actual old/new migration procedure. The separately collected [[source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3]] is the JavaScript v3 migration route; this source must not be used to reconstruct its steps.

> [!warning] Android route does not establish Android migration behavior
> The URL ends in `/android/v5`, while the body says the guide is only for JavaScript v3 custom integrations and explicitly excludes Android. Do not infer a PayPal Android SDK migration, an Android v5 upgrade path, or compatibility with any retained `braintree-android` package release.

> [!warning] Preserve historical evidence boundaries
> This 2026-09-16 website snapshot is neither current-support evidence nor a substitute for exact-version GitHub implementation evidence. Its title also does not establish a migration to PayPal Web SDK v6.

## Detail locators

- Canonical Android v5 source URL and capture metadata: raw lines 1-3.
- Retained title, slug and page heading: raw lines 5-14.
- JavaScript v3 custom-integration-only availability statement: raw lines 17-18.
- Explicit exclusions for JavaScript v2, Android, iOS, Drop-in UI and new PayPal web integrations: raw lines 20-26.
- Sole retained destination beyond the scope notice, the Braintree JavaScript SDK reference link: `## See also`, raw lines 31-34.

## Related

- Company: [[braintree]]
- Main native concept and version boundary: [[braintree-android-sdk]]
- Actual historical Android v4-to-v5 client SDK migration: [[source-braintree-client-sdk-migration-android-v5]]
- Separate JavaScript v3 `checkout.js` migration source: [[source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/android/v5-2026-09-16|Braintree Android v5-routed PayPal SDK migration page (JavaScript v3-only notice)]]
