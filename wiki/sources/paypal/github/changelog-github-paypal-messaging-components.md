---
title: "GitHub changelog: paypal/paypal-messaging-components"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json"
tags: [paypal, pay-later, paypal-credit, messaging, changelog, github-repository]
---

## Overview

Package-qualified release history for `paypal/paypal-messaging-components`. Durable implementation behavior belongs in [[source-github-paypal-messaging-components]]; this page records version transitions and their evidence.

## `@paypal/messaging-components@1.95.1` (2026-08-25)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/messaging-components` | Initial baseline | `1.95.1` | `2bdaf940cdb0dcd29a8a3bc992eea975798d6d00` | Full |

**Important findings:** Established the first policy-controlled full baseline for the web Messaging Components runtime. The release filters qualifying offers before term sorting, validates numeric payment counts, makes country-specific sort direction explicit, preserves default APR disclaimer fallback, and guards modal event delivery when the target window is absent.

**Developer or merchant impact:** The changes make long-term offer ordering and disclaimer selection deterministic for already-returned offers and reduce a modal event failure. They do not alter or prove upstream buyer qualification, merchant enablement, or country availability.

**Migration action:** No API migration is identified. Consumers should keep package and combined-SDK versions separate: `@paypal/sdk-release@5.0.569` records Messaging Components `1.94.0`, while this independently released package baseline is `1.95.1`.

**Updated source sections:** merchant integration surface; message and modal lifecycle; rendering and style contracts; `1.95.1` offer processing; Pay Later concept and PayPal company summary.

**Evidence boundary:** This is an initial baseline with no prior managed snapshot comparison. The retained capsule excludes tests, and source-level Venmo logo rendering is not Venmo checkout or Pay Later eligibility evidence.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json`
- Package manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/package.json`
- Upstream changelog: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/CHANGELOG.md`
- Offer terms table: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/components/modal/v2/parts/TermsTable.jsx`
