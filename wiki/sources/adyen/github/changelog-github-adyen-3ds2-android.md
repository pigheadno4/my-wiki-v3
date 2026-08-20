---
title: "GitHub changelog: Adyen/adyen-3ds2-android"
type: source
date_ingested: 2026-08-19
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/manifest.json"
tags: [adyen, android, 3d-secure, 3ds2, authentication, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-3ds2-android`. Cumulative integration knowledge belongs in [[source-github-adyen-3ds2-android]] and the linked immutable snapshots.

## `adyen-3ds2-android@2.2.27` (2026-05-27)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-3ds2-android` | Initial baseline | `2.2.27` | `de845e67488b6aecb1ff57ea7908b662f5ee2d40` | Full |

**Important findings:** The release claims a Data Safety Guide, a merchant-whitelisting compound-button text-color fix, `FLAG_ACTIVITY_NEW_TASK` for out-of-band issuer-app launch, and Bouncy Castle `1.84`.

**Developer or merchant impact:** The UI fix affects challenge branding, and the new intent flag can change issuer-app navigation behavior. The dependency update changes the SDK's cryptography dependency. The claimed guide would affect Google Play Data Safety declarations, but it is absent from the exact tag and cannot be used as retained disclosure evidence.

**Migration action:** Regression-test challenge UI and out-of-band app switching when updating. Verify privacy declarations against current authoritative Adyen guidance rather than relying on the missing guide. The README also omits a `2.2.27` compatibility row, so verify Android compatibility independently.

**Updated source sections:** Evidence boundary; distribution and version; challenge flow and outcomes; lifecycle and error model; security controls and device data; UI customization and deprecations; `2.2.27` release finding.

Broader transaction, challenge, lifecycle, security-warning, and UI behavior is the initial cumulative baseline, not change evidence introduced solely by `2.2.27`.

### Evidence gaps

- `DATA_SAFETY_GUIDE.md` is named by the release note but absent from the exact snapshot.
- The README compatibility table ends at `2.2.26`.
- The snapshot retains generated public API documentation but not implementation source, so code-level verification of release claims is unavailable.
- `ThreeDS2Service` generated documentation conflicts on whether cleanup is per transaction or once per app session.

### Evidence

- `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/manifest.json`
- `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/release-notes.md`
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/manifest.json`
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md`
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/ThreeDS2Service.html`
