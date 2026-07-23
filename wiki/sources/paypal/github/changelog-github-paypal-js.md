---
title: "GitHub changelog: paypal/paypal-js"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json"
tags: [paypal, javascript-sdk, react, npm, changelog, github-repository]
---

## Overview

Chronological release synthesis for the independently versioned packages in `paypal/paypal-js`. Detailed implementation knowledge belongs in [[source-github-paypal-js]] and the linked immutable snapshots.

## Repository change set: `702863f` (2025-09-04)

### `@paypal/paypal-js` timeline

| From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| Initial retained baseline | `@paypal/paypal-js@8.4.2` | 2025-09-04 | `702863f91b79d405c571cf75c3d742a82174b46e` | Full |

**Important change:** Corrected the v6 script-load option type name and the conditional `SdkInstance` TypeScript definitions.

**Developer or merchant impact:** TypeScript consumers receive more accurate compile-time v6 options and component-dependent instance methods. The release notes identify no runtime payment-flow change.

**Migration action:** No migration action is stated. Consumers affected by the incorrect v6 typings should upgrade and rerun type checking.

**Updated source sections:** `@paypal/paypal-js` responsibility, legacy loader behavior, and version 8.

**Evidence:**

- Release record: `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json`
- Release notes: `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json`
- Corrected v6 types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/packages/paypal-js/types/v6/index.d.ts`
- V6 loader: `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/packages/paypal-js/src/v6/index.ts`
- Comparison: not applicable for the initial retained package baseline

### Collateral package context

The same SHA contains `@paypal/react-paypal-js@8.9.1`, but no React release is recorded in this change set because the approved work item contains only `@paypal/paypal-js@8.4.2`. A future React release ingest will add its own package-qualified timeline entry.

## Raw Sources

- `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json` — exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json` — `@paypal/paypal-js@8.4.2` release record
