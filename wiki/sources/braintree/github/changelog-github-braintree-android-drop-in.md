---
title: "GitHub changelog: braintree/braintree-android-drop-in"
type: source
date_ingested: 2026-08-13
original_format: github-repo
raw_files:
  - "github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json"
tags: [braintree, android, mobile-sdk, drop-in, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-android-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-android-drop-in]] and the linked immutable snapshots.

## `drop-in@6.17.0` (2025-04-21)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `drop-in` | Initial baseline | `6.17.0` | `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7` | Full |

**Exact release change:** All pinned `braintree_android` modules move to `4.50.0`. No new payment method or public Drop-in flow is documented for `6.17.0`.

**Developer or merchant impact:** This release remains on the Braintree Android v4 dependency line, requires API 21+, and should be used instead of pre-`6.16.0` builds affected by the repository's 2025 certificate warning. Do not infer behavior from the independently retained `braintree-android@5.30.0` modular source.

**Migration action:** Treat `6.17.0` as the first exact-SHA Android Drop-in baseline. Before moving the underlying modular SDK or adopting v5 behavior, verify a compatible Drop-in release or replace the prebuilt UI with a modular integration.

**Updated source sections:** Version and dependency boundary; launch and server handoff; payment methods and eligibility; vaulting; 3D Secure and risk data; redirect handling; release findings.

**Evidence boundary:** No prior exact-SHA Android Drop-in snapshot exists in the wiki. Historical repository changelog entries provide context but are not retained source comparisons.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json`
- Repository changelog: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/CHANGELOG.md`
- Root build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/build.gradle`
- Library build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Drop-In/build.gradle`
