---
title: "GitHub changelog: paypal/paypal-sdk-release"
type: source
date_ingested: 2026-08-21
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json"
tags: [paypal, javascript-sdk, release-automation, changelog, github-repository]
---

## Overview

Package-qualified release history for `paypal/paypal-sdk-release`. Durable assembly and release behavior belongs in [[source-github-paypal-sdk-release]]; this page records version transitions and their evidence.

## `@paypal/sdk-release@5.0.569` (2026-08-18)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/sdk-release` | Initial baseline | `5.0.569` | `71e5116c56355a60bc8af337720116047d4d6ab8` | Full |

**Important findings:** Established the first policy-controlled release-assembly baseline. The package pins twelve direct PayPal browser components, delegates setup to `@paypal/sdk-client@4.0.204`, and records Checkout Components `5.0.428`, Messaging Components `1.94.0`, Apple Pay Components `1.8.2`, and Google Pay Components `1.3.5` among the assembled versions.

**Developer or merchant impact:** Use this release as a component bill of materials, not as proof of product eligibility or component behavior. The manifest can identify which independently versioned repository needs inspection for a detailed implementation question.

**Migration action:** None for the initial baseline. For a later release, compare the direct dependency table and recollect any changed checkout-focused component repository before attributing behavior to the assembly update.

**Updated source sections:** release assembly; wrapper entry point; upgrade, publish, and deployment flow; evidence boundary; PayPal Checkout concept and company summary.

**Evidence boundary:** GitHub release notes were unavailable. The retained capsule excludes the transitive lockfile and CDN tarballs, so exact transitive versions and packaged artifacts require a SHA-pinned supplement. The README documents `npm run activate`, but the retained package manifest defines no `activate` script; treat activation as unresolved operational documentation rather than a verified command.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/manifest.json`
- Release-note record: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json`
- Package manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/package.json`
- README: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/README.md`
- Deployment workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/deploy.yml`
- Publication workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/publish.yml`
