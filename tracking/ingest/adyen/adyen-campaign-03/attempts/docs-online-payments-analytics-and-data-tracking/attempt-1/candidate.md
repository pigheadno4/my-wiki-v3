---
title: "Adyen Drop-in and Components analytics and data tracking"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/analytics-and-data-tracking"
raw_files:
  - "adyen/docs/online-payments/analytics-and-data-tracking/2026-09-15.md"
tags: [adyen, online-payments, analytics, telemetry, checkout, drop-in, components]
---

## Overview

This [[adyen]] documentation page describes usage data collected by Drop-in and Components for [[adyen-online-payments]] integrations. It distinguishes telemetry, a checkout attempt identifier that links telemetry with payment data, and Drop-in/Components analytics events. Adyen says it uses the data to improve product performance and stores it for two years. This is a documentation snapshot, not evidence of a particular merchant's configuration, live data flow, or legal position.

## Key takeaways

- Telemetry can include integration type and version, platform, device system version for mobile, locale, mounted page URL, rendered or used payment methods/components, user agent, amount and currency, and Web build type where supported. Drop-in/Components analytics includes front-end errors and shopper events. The checkout attempt identifier links telemetry with payment data; Adyen says it does not use cookies to collect analytics data.
- Data collection is on by default in supported versions, but the version table separates telemetry plus checkout attempt identifier from Drop-in/Components analytics. The latter begins later for Web, iOS, and Android, and the table does not list a Drop-in/Components analytics version for React Native or Flutter. Consult the platform/version matrix before applying a collection or configuration claim.
- For `/sessions`, the checkout attempt identifier is sent automatically with the payment request. For `/payments`, newer listed SDK versions include `checkoutAttemptId` in `sdkData`, which the server passes in the request; earlier versions require forwarding `checkoutAttemptId` from the front end in the server request. The document associates the identifier with the Checkout dashboard and, for Web, Adyen Uplift Personalize.
- The per-platform analytics settings default to enabled. On Web from v5.69.0 or v6.2.0, iOS from v5.12.0, and Android from v5.7.0, the documented setting affects Drop-in/Components analytics while telemetry and the checkout attempt identifier are always sent. Do not treat setting analytics to false as a blanket stop to all three data categories. React Native and Flutter have separate `enabled` settings; the page does not state the same always-sent configuration qualification for those tabs.
- Adyen directs merchants to check with legal counsel whether collection needs mention in a privacy or cookie policy in their country or region. Separately, for Web Drop-in/Components, the page describes an optional fraud detection script for collecting activity beyond checkout pages; Drop-in or the Component sends data collected by that script when the shopper checks out. This optional fraud path is distinct from the analytics settings and is not evidence of legal compliance or an account's risk-product availability.

## Detail locators

- `# Analytics and data tracking` and `## Benefits of data collection`, raw lines 15–27 — purpose, two-year storage statement, and examples of intended use.
- `## Data we are collecting`, raw lines 29–55 — telemetry fields, checkout attempt identifier, analytics events, cookies statement, and privacy-policy counsel note.
- `## Versions with data collection features`, raw lines 57–69 — platform-specific start versions for telemetry/identifier and Drop-in/Components analytics, including the Web build-type exception.
- `### Checkout attempt identifier`, raw lines 71–87 — dashboard and Web Personalize purpose, `/sessions` automatic sending, and `/payments` `sdkData` versus earlier-version forwarding.
- `## Configure data collection`, raw lines 89–188 — Web, iOS, Android, React Native, and Flutter defaults, setting names, version qualifications, and examples.
- `## Collect additional data to detect fraud`, raw lines 190–202 — optional Web script, beyond-checkout-page collection, and checkout-time sending.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — online-payments concept and integration routes.
- [[adyen-risk-management]] — related fraud and risk-management documentation; the optional script here has its own scope.

## Raw Sources

- [[raw/adyen/docs/online-payments/analytics-and-data-tracking/2026-09-15|Analytics and data tracking (2026-09-15 snapshot)]]
