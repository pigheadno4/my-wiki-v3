---
title: "GitHub changelog: braintree/braintree-web"
type: source
date_ingested: 2026-07-28
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json"
tags: [braintree, javascript-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-web`. Cumulative implementation knowledge belongs in [[source-github-braintree-web]] and the linked immutable snapshots.

## `braintree-web@3.143.0` (2026-06-11)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web` | Initial baseline | `3.143.0` | `bae582d791026c143abb91c3bdcada92b8c060f6` | Full |

**Important findings:** The release updates `credit-card-type` to `10.2.0` and replaces `@paypal/accelerated-checkout-loader` with `@paypal/fastlane-sdk-loader`.

**Developer or merchant impact:** The package now loads Fastlane through the renamed loader dependency. The release notes do not identify a checkout-flow or public-API behavior change.

**Migration action:** No application migration is documented for this release. Integrations that directly inspect or constrain dependency package names should account for the loader rename.

**Updated source sections:** Package and client architecture; Fastlane dependency; exact release findings; Braintree company baseline.

**Evidence boundary:** This is the first retained Braintree Web baseline, so no prior exact-SHA comparison exists. Patch findings come from the release notes and package manifest; broader source-page findings describe accumulated `3.143.0` behavior.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json`
- Package manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/package.json`
- Repository changelog: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/CHANGELOG.md`
