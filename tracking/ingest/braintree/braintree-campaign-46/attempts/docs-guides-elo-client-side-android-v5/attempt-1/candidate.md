---
title: "Braintree Elo Client-Side Availability (Android v5 Route)"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/elo/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/elo/client-side/android/v5-2026-09-16.md"
tags: [braintree, elo, android-v5, limited-release]
---

## Overview

This 2026-09-16 snapshot is a [[braintree|Braintree]] Elo client-side page at the Android v5 route. Its retained body contains no Android implementation procedure or exact Android SDK behavior: it only states that Elo was in limited release for select merchants using what the page calls the latest JavaScript v3 and server SDKs, and directs merchants to request access.

## Key takeaways

- The captured availability notice conditions Elo on select-merchant limited-release access and directs merchants to contact Braintree to request access.
- Despite the Android v5 route, the retained body names JavaScript v3 and server SDKs rather than an Android SDK and supplies no Android code, setup steps, or client behavior.

> [!warning] Route, version, and availability boundary
> The Android v5 route is navigation metadata, not evidence of Android SDK implementation or support. The page-relative word "latest" identifies no exact JavaScript or server SDK package version, and this snapshot does not establish current Elo availability, merchant or environment enablement, or payment execution.

## Detail locators

- Android v5 route metadata — frontmatter `slug`, raw line 7.
- Limited-release, select-merchant, JavaScript v3/server-SDK, and access-request conditions — `AVAILABILITY`, raw lines 17-18.
- Server-side navigation target — `Next Page: Server-side`, raw line 22.

## Related

- [[braintree]] — provider context
- [[braintree-payment-methods]] — provider payment-method eligibility and Elo retrieval route
- [[source-braintree-docs-guides-elo-client-side-javascript-v3]] — captured JavaScript v3 Elo client-side guide
- [[source-braintree-docs-guides-elo-server-side-node]] — captured Elo server-side Node.js route

## Raw Sources

- [[raw/braintree/docs/guides/elo/client-side/android/v5-2026-09-16|Braintree Elo client-side Android v5 route (2026-09-16 snapshot)]]
