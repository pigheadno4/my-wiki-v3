---
title: "GitHub changelog: paypal/paypal-messages-android"
type: source
date_ingested: 2026-08-12
date_updated: 2026-08-13
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-android/snapshots/2026-08-13-0424354/manifest.json"
  - "github/paypal/paypal-messages-android/snapshots/2026-08-13-1d2238c/manifest.json"
  - "github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/manifest.json"
tags: [paypal, android, kotlin, messaging, pay-later, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `paypal/paypal-messages-android`. Durable integration and architecture guidance belongs in [[source-github-paypal-messages-android]].

## Untagged `default-branch@0424354` (`develop`) - Braintree Policy Boundary (2026-05-29)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `develop` | historical `1d2238c` tree | untagged documentation commit | `0424354a5fa0ab697275186fe101d105838ac03e` | Delta |

The only changed path is `README.md`. It adds that the component is intended for the Braintree SDK only, requires both a Braintree account and Braintree SDK integration, and does not support PPCP SDK integrations.

This ref line is not based on the separately released `paypal-messages-android@1.3.0` SHA `f1aa138`. It is documentation-policy evidence, not a semantic release, a `1.3.0` change, or proof of code-level compatibility enforcement.

Evidence: `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-0424354/manifest.json` and `tracking/github/repos/paypal/paypal-messages-android/comparisons/default-branch/1d2238c--0424354/comparison.json`.

## `paypal-messages-android@1.3.0` - Change Set `f1aa138` (2026-03-25)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `paypal-messages-android` | Managed baseline | `1.3.0` | `f1aa138cc6822cc11d68ac4bfdee3cf183aedbc2` | Full |

The exact release adds `language_rendered` analytics and bold styling for server message substrings marked with `%bold%`. Merchant impact is presentation and analytics fidelity; no checkout-payment API was added.

The source capsule also exposes version-qualified integration risks: the AppCompat modal maps Apply to the close callback, `setConfig()` omits environment, activity callback registration follows activity launch, and shared cache/analytics/API state is not keyed per view or merchant.

Evidence: `raw/github/paypal/paypal-messages-android/releases/paypal-messages-android/1.3.0/2026-08-12/manifest.json`, release notes, and the exact-SHA snapshot manifest.

## Earlier Stable History - Cumulative Context

The retained upstream changelog records the stable line through `1.1.0`, including merchant-data-provider extraction, ProGuard and Central publishing work, modal dismissal and production SSL fixes, integration attribution, accessibility, page/offer context, analytics changes, instance IDs, and XML/Jetpack demo evolution.

The GitHub `1.3.0` release notes compare against `1.2.0`, but the retained `CHANGELOG.md` does not contain dedicated `1.2.0` or `1.3.0` sections. This ledger therefore does not invent a complete `1.2.0` change set.

## Evidence Conflicts

- GitHub release identity is `1.3.0`; root Gradle metadata says `1.1.14`; checked-in POM metadata says `1.1.10`.
- Repository `LICENSE` is MIT; Gradle/POM publication metadata declares Apache License 2.0.
- README says the library is published to Maven Central while also saying it remains in development and should be used in sandbox until an official release.

These conflicts are preserved for future release comparisons. They are not resolved by choosing the highest version string.

## Evidence Boundary

- Only `1.3.0` has a managed immutable release record and source capsule.
- Earlier entries are cumulative history from `CHANGELOG.md`, not separately collected file-level comparisons.
- Release tags, artifact metadata, and source presence do not establish general availability, merchant eligibility, or buyer offer availability.

## Raw Sources

- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-0424354/manifest.json`
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-0424354/files/README.md`
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-1d2238c/manifest.json`
- `tracking/github/repos/paypal/paypal-messages-android/comparisons/default-branch/1d2238c--0424354/comparison.json`
- `tracking/github/repos/paypal/paypal-messages-android/comparisons/default-branch/1d2238c--0424354/diff.patch`
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/manifest.json`
- `raw/github/paypal/paypal-messages-android/releases/paypal-messages-android/1.3.0/2026-08-12/manifest.json`
- `raw/github/paypal/paypal-messages-android/releases/paypal-messages-android/1.3.0/2026-08-12/release-notes.md`
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/CHANGELOG.md`
