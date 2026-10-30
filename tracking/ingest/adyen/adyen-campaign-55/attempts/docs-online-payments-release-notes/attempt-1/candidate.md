---
title: "Adyen online payments release notes (2018–2026 snapshot)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/release-notes"
raw_files:
  - "adyen/docs/online-payments/release-notes/2026-09-15.md"
tags: [adyen, online-payments, release-notes, checkout-api, web, ios, android]
---

## Overview

This 2026-09-15 capture of Adyen's [[adyen-online-payments]] release history has dated entries for Checkout API, Pay by Link, Hosted Checkout, Customer Area and Web, iOS, Android, React Native and Flutter Drop-in/Components. It records version-specific features, compatibility, breaking changes, removals, fixes and known issues. The visible entries span Checkout API v37 (2018) through Web v6.45.0 (2026-09-10); they do not establish the current latest release, a merchant's installed version, account enablement or payment outcome. The page's `last_modified` metadata says 2023-01-12 despite its 2026 entries, so use the dated headings and pinned capture for chronology. See [[adyen]].

## Key takeaways

- **Read by product and version.** The 2026-09-10 Web v6.45.0 entry requires Checkout API v69 or later and adds a Sessions review step with `onReview`, `processPayment` and `onAction`. Several mobile entries *recommend* Checkout API v72 or later; that wording is distinct from the Web requirement. The release list also has environment-specific Web CDN URLs and SRI hashes, whose exact values belong to the selected version's raw entry.
- **API migration changes are version-bound.** Checkout API v72 (2026-04-15) adds validation to specified request parameter values, so nonconforming requests fail; its Advanced-flow `/payments` entry gives `sdkData` precedence over duplicate SDK-related fields. It also records deprecated/removed parameters and corrected HTTP 422/429 errors. The linked v72 upgrade guide provides the parameter-level constraints. Checkout API v70 (2023-01-30) requires `recurringProcessingModel` for its `/payments` or `/sessions` token storage/use cases, an `amount` for gift-card balance requests, and `action.qrCodeData` instead of `action.url` for Pix. These are not universal rules for every historical API version.
- **Web v6 is a breaking upgrade.** The 2024-07-24 v6.0.0 entry requires Checkout API v69+, changes imports/creation and callback continuation, moves failures to `onPaymentFailed`, requires `countryCode` in checkout configuration or `/sessions`, and removes IE11 support. Method-specific changes and the migration guide need separate review. Web v4 entries in this capture state an August 1, 2026 end-of-life date; v3 entries state end of life since October 1, 2025.
- **Mobile versions have their own compatibility boundaries.** Flutter v1.12.0 (2026-08-04) raises its iOS minimum from 12 to 13 and Android minimum API from 21 to 23. Android v5.0.0 and iOS v5.0.0 have separate migration changes and Sessions support. Do not apply one platform's minimum, dependency or action-handling change to another.
- **Issues and outcomes need their dates.** The log pairs known issues with later fixes, including Web v6.24.0's Card `onAdditionalDetails` regression fixed in v6.25.1 and the historical Web v3.22.0/v3.22.1 native 3DS2 problem fixed in v3.22.2. Checkout API v67 changed when redirect 3DS authentication authorizes, while `/payments/details` verifies the returned result and an AUTHORISATION webhook covers a shopper who does not return. A release-note fix or synchronous response is not evidence of a particular payment's capture, settlement or payout.

## Detail locators

- Page scope, filters, capture metadata and newest visible Web v6.45.0 entry: raw lines 1–87.
- Flutter v1.12.0 platform minimums and dependency table; Web v6.41.0 Sessions installment change: lines 227–248 and 317–378.
- Checkout API v72 validation, Advanced `sdkData` precedence, removals and fixes: lines 1131–1177.
- Hosted Checkout and Pay by Link iframe restriction from 2026-01-16: lines 1740–1751.
- Web v6.0.0 breaking changes, method changes and migration routes: lines 5590–5669.
- Android v5.0.0 and Checkout API v71 changes: lines 7195–7345 and 7097–7118.
- Checkout API v70 tokenization, gift-card, Pix and storage changes: lines 9022–9086.
- Checkout API v69, Web v5.0.0 and Checkout API v68 transitions: lines 10395–10430, 11759–11800 and 11827–11889.
- Checkout API v67 redirect/native 3DS changes; Android/iOS/Web v4.0 migration entries: lines 13384–13456, 12404–12480, 12493–12589 and 13464–13529.
- Earlier Checkout API v65/v64 and 2018–2020 historical entries, including tables and versioned asset examples: lines 14463–14505, 14921–14998 and 15001–16346.

## Related

- [[adyen-online-payments]] — product and integration overview.
- [[adyen-review-page-checkout]] — separate implementation evidence for the Web v6.45.0 review flow.
- [[adyen-tokenization]] — tokenization concepts; apply API-version conditions.
- [[adyen-3d-secure]] — 3DS flows and outcome handling.
- [[adyen-payment-capture]] — authorization versus capture boundary.

## Raw Sources

- [[raw/adyen/docs/online-payments/release-notes/2026-09-15|Adyen online payments release notes, captured 2026-09-15]]
