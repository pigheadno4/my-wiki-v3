---
title: "GitHub changelog: paypal/paypal-messages-ios"
type: source
date_ingested: 2026-08-12
date_updated: 2026-08-13
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json"
tags: [paypal, ios, swift, messaging, pay-later, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `paypal/paypal-messages-ios`. Durable integration and architecture guidance belongs in [[source-github-paypal-messages-ios]].

## Untagged `default-branch@fdd1868` (`develop`) - Braintree Policy Boundary (2026-06-01)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `develop` | released `1.2.0` tree | untagged documentation commit | `fdd18681f486a3b2f1c60e3c47f8669f55a73a96` | Delta |

The only changed path is `README.md`. It removes the recommendation to integrate through the PayPal iOS SDK and states that the component is intended for the Braintree SDK only, requiring both a Braintree account and Braintree SDK integration; PPCP SDK integrations are unsupported.

This is a repository documentation-policy change, not a semantic release or code change. No package version can yet be identified as the first release carrying or enforcing this policy.

Evidence: `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json` and `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/comparison.json`.

## `paypal-messages-ios@1.2.0` - Change Set `432d6b8` (2026-03-25)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `paypal-messages-ios` | Managed baseline | `1.2.0` | `432d6b832714b2615106c3f2a748ac61654d8bbd` | Full |

The exact release adds `language_rendered` analytics and bold styling for server message substrings marked with `%bold%`. Merchant impact is primarily analytics fidelity and message presentation; no checkout-payment API was added.

The exact source also exposes a version-qualified configuration risk: `PayPalMessageViewModel.updateConfig()` omits `environment`, `merchantID`, and `partnerAttributionID`. A full config replacement therefore does not replace those fields through `setConfig`; see [[source-github-paypal-messages-ios]] and [[analysis-paypal-messages-ios-vs-android]].

Evidence: `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/manifest.json`, release notes, and the exact-SHA snapshot manifest.

## `paypal-messages-ios@1.1.0` - Cumulative Context (2026-02-27)

The retained upstream changelog records language/locale parameters, requested-language analytics, an authorization header for logging, and modal/dependency fixes. This is cumulative history inside the `1.2.0` snapshot, not a separately collected managed release.

## `paypal-messages-ios@1.0.0` - Cumulative Context (2024-05-14)

The first stable history includes message/modal accessibility, interaction gating until render, merchant-profile caching by client and merchant ID, richer response errors, integration identity, analytics/schema revisions, privacy-manifest work, and development-environment controls. These facts are historical context from the cumulative changelog; the current API description is grounded in the `1.2.0` source capsule.

## Evidence Boundary

- Only `1.2.0` has a managed immutable release record and source capsule.
- Earlier entries summarize the `CHANGELOG.md` retained at the `1.2.0` SHA and are not complete file-level comparisons.
- Package presence and stable tags do not establish merchant eligibility or buyer offer availability.

## Raw Sources

- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/files/README.md`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/comparison.json`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/diff.patch`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/release-notes.md`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/CHANGELOG.md`
