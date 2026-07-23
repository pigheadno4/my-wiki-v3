---
title: "GitHub changelog: paypal/paypal-js"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json"
tags: [paypal, javascript-sdk, react, npm, changelog, github-repository]
---

## Overview

Chronological release synthesis for the independently versioned packages in `paypal/paypal-js`. Detailed implementation knowledge belongs in [[source-github-paypal-js]] and the linked immutable snapshots.

## Repository change set: `59cb2ce` (2026-06-25)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `10.0.0` | `10.0.1` | 2026-06-25 | `59cb2ce64d158ac4f4cabecdd82f7b4191a8dff3` | Full |
| `@paypal/react-paypal-js` | `10.0.0` | `10.1.0` | 2026-06-25 | `59cb2ce64d158ac4f4cabecdd82f7b4191a8dff3` | Full |

**Important change:** Core adds typed v6 DOM custom elements, Canada to the v6 Pay Later country type, and legacy Buttons setup-token approval data/JSDoc for Venmo vault-without-purchase. React adds Braintree Pay Later, provider-cached eligibility, stronger Braintree shipping types, explicit server-eligibility environment selection, and integration error fixes.

**Developer or merchant impact:** Non-React TypeScript integrations gain typed custom elements. Braintree merchants can add Pay Later but must fetch eligibility first and still tokenize approval into a Braintree nonce. Server-rendered eligibility can no longer silently use sandbox. Missing Google `pay.js` and provider initialization failures become visible errors.

**Migration action:** Pass `environment` to `useFetchEligibleMethods()`; call `useBraintreeEligibleMethods()` before rendering Braintree Pay Later; use `buyer-country` for manually supplied basic-card JSX; ensure Google `pay.js` loads before Google Pay mounts; and handle provider, eligibility, and session errors separately.

**Updated source sections:** core version 10; React version 10; [[paypal-checkout]], [[paypal-vault]], [[paypal-braintree-integration]], and [[paypal-google-pay]].

> [!warning] Contradiction
> The React release note attributes `shippingAddressOverride` and `contactPreference` to checkout-with-vault, but the exact public type and hook expose only `shippingCallbackUrl` for that flow. The other two fields are evidenced for one-time and Pay Later.

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.1/2026-07-22/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.1/2026-07-22/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.0/2026-07-22/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.0/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.0.0--10.0.1/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.0.0--10.1.0/comparison.json`
- Core web-component types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/paypal-js/types/v6/components/web-components.d.ts`
- Legacy Buttons setup-token types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/paypal-js/types/components/buttons.d.ts`
- V6 Pay Later country type: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/paypal-js/types/v6/components/paypal-payments.d.ts`
- Braintree Pay Later component: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/components/Braintree/BraintreePayPalPayLaterButton.tsx`
- Braintree Pay Later hook: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/hooks/Braintree/useBraintreePayPalPayLaterSession.ts`
- Braintree eligibility hook: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/hooks/Braintree/useBraintreeEligibleMethods.ts`
- Braintree types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/types/braintree.ts`
- Server eligibility helper: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/hooks/useFetchEligibleMethods.ts`
- Google Pay hook: `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/hooks/useGooglePayOneTimePaymentSession.ts`

### Evidence boundary

The package source establishes React integration behavior and public types, not Braintree server processing internals or PayPal runtime behavior owned by `paypal-checkout-components`. The DOM declarations type custom elements but do not prove that `@paypal/paypal-js` registers every element.

## Repository change set: `4bd05ab` (2026-06-04)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `9.8.0` | `10.0.0` | 2026-06-04 | `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429` | Full |
| `@paypal/react-paypal-js` | `9.3.0` | `10.0.0` | 2026-06-04 | `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429` | Full |

**Important change:** Both v6 integration surfaces now require an explicit `production` or `sandbox` environment. The core loader validates the value and maps it to the corresponding PayPal host; the React provider forwards its required prop to that loader.

**Developer or merchant impact:** Omitting the value no longer silently loads sandbox. TypeScript integrations fail compilation and untyped runtime callers receive a thrown `Error`. A client ID does not select the environment, so production configuration must be audited independently.

**Migration action:** Add `environment: "production" | "sandbox"` to every v6 `loadCoreSdkScript()` call and `environment="production" | "sandbox"` to every v6 `PayPalProvider`. Use production explicitly for live traffic and verify untyped runtime configuration before deployment.

**Updated source sections:** core version 10; React version 10; [[paypal-checkout]]; PayPal company summary.

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.0.0/2026-07-22/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.0.0/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/9.8.0--10.0.0/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/9.3.0--10.0.0/comparison.json`
- Core loader implementation: `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/files/packages/paypal-js/src/v6/index.ts`
- Core required option type: `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/files/packages/paypal-js/types/v6/index.d.ts`
- React provider: `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/files/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx`

### Evidence boundary

The release notes and changed public files establish an environment-selection safety break, not a new payment method, session, or server API. The unchanged historical sections remain available for v8 and v9 questions. `BraintreePayPalProvider` is a separate integration path and is not included in the changed React files.

## Repository change set: `31eb658` (2026-06-03)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `8.4.2` | `9.8.0` | 2026-06-03 | `31eb658ac885a490d38ef34e471c069b0c6e49cb` | Full |
| `@paypal/react-paypal-js` | `8.9.2` | `9.3.0` | 2026-06-03 | `31eb658ac885a490d38ef34e471c069b0c6e49cb` | Full |

**Important change:** The core v6 type surface expands to nine conditional components, accepts client ID or client token, supports eligibility hydration, adds optional Card Fields name/billing-address submit data, and types Google Pay. The React v9 surface introduces `PayPalProvider`, explicit `/sdk-v6` and `/sdk-v6/server` exports, v6 buttons/hooks, native Google Pay UI, and Braintree one-time, billing-agreement, and checkout-with-vault flows.

**Developer or merchant impact:** React v8 legacy integrations remain available from the root export, but v6 integrations use a new provider, import path, callback shape, and explicit eligibility flow. Card Fields can pass richer 3DS data. Braintree merchants receive nonce-based React flows that must be completed with Braintree server tooling rather than PayPal Orders APIs.

**Migration action:** Choose the v6 subpath deliberately; replace `PayPalScriptProvider` with `PayPalProvider`; move credentials out of the legacy `options` object; return `{ orderId }` from v6 order callbacks; add explicit eligibility fetching or hydration; and test the relevant component-qualified SDK instance. Braintree integrations must provision a server-generated Braintree client token, load the Braintree Web scripts, tokenize approval data, and process the nonce server-side.

**Updated source sections:** core version 9; React version 9 and migration; Braintree PayPal surface; [[paypal-checkout]], [[paypal-expanded-checkout]], [[paypal-google-pay]], [[paypal-vault]], and [[paypal-braintree-integration]].

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/9.8.0/2026-07-22/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/9.8.0/2026-07-22/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/9.3.0/2026-07-22/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/9.3.0/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/8.4.2--9.8.0/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/8.9.2--9.3.0/comparison.json`
- Core v6 public surface: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/types/v6/index.d.ts`
- Card Fields submit types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/types/v6/components/card-fields.d.ts`
- Google Pay session types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/types/v6/components/googlepay-payments.d.ts`
- React v6 exports: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/src/v6/index.ts`
- React provider: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx`
- Braintree provider: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/src/v6/components/Braintree/BraintreePayPalProvider.tsx`
- Braintree integration guide: `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/README.md`

### Evidence boundary

The release notes and snapshot identify the selected latest stable v9 releases, not every v9 tag as a separately ingested release. Intermediate v9 changelog entries are cumulative implementation context within this full major-version ingest.

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

- `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json` — shared exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.1/2026-07-22/manifest.json` — `@paypal/paypal-js@10.0.1` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.0/2026-07-22/manifest.json` — `@paypal/react-paypal-js@10.1.0` release record
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json` — shared exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/manifest.json` — `@paypal/paypal-js@10.0.0` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.0.0/2026-07-22/manifest.json` — `@paypal/react-paypal-js@10.0.0` release record
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json` — shared exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/9.8.0/2026-07-22/manifest.json` — `@paypal/paypal-js@9.8.0` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/9.3.0/2026-07-22/manifest.json` — `@paypal/react-paypal-js@9.3.0` release record
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json` — exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/manifest.json` — `@paypal/react-paypal-js@8.9.2` release record
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json` — exact-SHA source capsule
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json` — `@paypal/paypal-js@8.4.2` release record
