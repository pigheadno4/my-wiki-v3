---
title: "Adyen Upgrade Your Integration"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/2026-09-15.md"
tags: [adyen, online-payments, upgrades, versioning]
---

## Overview

Adyen's online-payments upgrade hub explains release/version policy, the separate lifecycles of Drop-in/Components and Checkout API, migration from Classic API, and routes to version-specific upgrade guides. Its 2026-09-15 snapshot includes iOS and Android compatibility tables. Use release notes and the linked platform GitHub or API Explorer lifecycle pages to check a version's current state before making an upgrade decision.

## Key takeaways

- The guide says breaking changes are introduced in major versions. Drop-in/Components release patch, minor and major versions; Checkout API releases only major versions. Adyen recommends regular upgrades and reading release notes before a new Drop-in/Components major version to check the minimum required Checkout API version.
- Both product families have Active, Inactive, Deprecated and End-of-Life states, but their deprecated upgrade windows differ: **one year** for Drop-in/Components and **two years** for Checkout API after reaching that state. Deprecated versions no longer receive new features, bug fixes or regulation-required changes. At end of life Adyen says support ends and payment processing can be suspended at any time. These are product-family policies, not a claim that any specific version is currently deprecated or suspended.
- The guide says Adyen no longer develops Classic API and strongly recommends moving server-side integrations to Checkout API. It recommends a Checkout API upgrade in particular for Adyen 3DS2 users on v66 or earlier and when a Drop-in/Components upgrade is incompatible with the existing Checkout API version.
- Mobile upgrades require compatible combinations of Drop-in/Components and other integration parts. The iOS table pairs component ranges with Checkout API and earliest iOS versions, including some Xcode-dependent rows. The Android table pairs component ranges with Checkout API, minimum SDK and target SDK levels. These table rows are snapshot-specific, not a guarantee for later releases.

## Detail locators

- `## Our way of versioning`, `### Drop-in/Components lifecycle`, and `### Checkout API lifecycle`: version semantics, four states, consequences, and links to current platform/API lifecycle sources.
- `## Staying up-to-date` and `## Upgrade guides`: upgrade recommendations and version-specific Checkout API, Web, iOS and Android guides.
- `## Drop-in/Components version compatibility`, `### iOS compatibility table`, and `### Android compatibility table`: the exact snapshot matrix and its platform prerequisites.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/2026-09-15|Adyen upgrade-your-integration webpage snapshot (2026-09-15)]]
