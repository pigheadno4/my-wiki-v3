---
title: "GitHub changelog: paypal/paypal-js"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json"
tags: [paypal, javascript-sdk, react, npm, changelog, github-repository]
---

## Overview

Chronological release synthesis for the independently versioned packages in `paypal/paypal-js`. Detailed implementation knowledge belongs in [[source-github-paypal-js]] and the linked immutable snapshots.

## Repository change set: `77487d6` (2025-10-02)

### `@paypal/react-paypal-js` timeline

| From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| Initial retained baseline | `@paypal/react-paypal-js@8.9.2` | 2025-10-02 | `77487d6cea80c2df694166e5d8f5c420cca41e7e` | Full |

**Important change:** Added proxy props to Card Fields to prevent stale React closures. Also upgraded the package-lock format, corrected a Rollup dependency, and moved the package dependency to `@paypal/paypal-js@9.0.0`.

**Developer or merchant impact:** Card Fields provider callbacks and individual-field input events can observe current React state without recreating the underlying SDK components. The dependency range now requires `@paypal/paypal-js ^9.0.0`.

**Migration action:** No application API migration is stated. Upgrade the paired core dependency and rerun package installation and type checking. Applications whose Card Fields callbacks close over changing state should upgrade for the callback-freshness fix.

**Updated source sections:** `@paypal/react-paypal-js` responsibility and version 8; [[paypal-expanded-checkout]] React callback freshness.

**Evidence:**

- Release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/manifest.json`
- Release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json`
- Proxy implementation: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/hooks/useProxyProps.ts`
- Provider integration: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/components/cardFields/PayPalCardFieldsProvider.tsx`
- Individual field integration: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/components/cardFields/PayPalCardField.tsx`
- Dynamic provider story: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/stories/payPalCardFields/payPalCardFieldsProvider.stories.tsx`
- Dynamic individual-fields story: `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/stories/payPalCardFields/payPalCardFieldsIndividual.stories.tsx`
- Comparison: not applicable for the initial retained package baseline

### Collateral package context

The same SHA contains `@paypal/paypal-js@9.0.0`, matching React 8.9.2's declared dependency. That core package is not part of this approved work item and is not independently ingested by this entry.

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

- `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json` — exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/manifest.json` — `@paypal/react-paypal-js@8.9.2` release record
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json` — exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json` — `@paypal/paypal-js@8.4.2` release record
