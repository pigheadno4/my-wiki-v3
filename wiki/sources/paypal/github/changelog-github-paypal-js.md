---
title: "GitHub changelog: paypal/paypal-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-08-30
original_format: github-repo
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-08-30-1246244/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-3caece5/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json"
tags: [paypal, javascript-sdk, react, npm, changelog, github-repository]
---

## Overview

Chronological release synthesis for the independently versioned packages in `paypal/paypal-js`. Detailed implementation knowledge belongs in [[source-github-paypal-js]] and the linked immutable snapshots.

## Repository change set: `1246244` (2026-08-26)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `10.1.0` | `11.0.0` | 2026-08-26 | `1246244faf376b5abe3ab35335d95b82426d74f5` | Full |
| `@paypal/react-paypal-js` | `10.3.0` | `10.4.0` | 2026-08-26 | `1246244faf376b5abe3ab35335d95b82426d74f5` | Delta |

The package-qualified releases are `@paypal/paypal-js@11.0.0` and `@paypal/react-paypal-js@10.4.0`.

**Important change:** Core removes its bundled `ApplePaySession` browser-global declaration, replaces the Google Pay 3DS placeholder with a typed `{ orderId }` promise contract and liability-shift result, and adds component-narrowed TypeScript sessions for 50 v6 Local Payment Methods. React coordinates that core contract by closing Google's sheet before payer action, delaying `onApprove` until authentication completes, routing cancellation or failure to `onError`, and suppressing callbacks after unmount.

**Developer or merchant impact:** Apple Pay TypeScript consumers may need `@types/applepayjs`. Google Pay React integrations no longer approve before required 3DS completes, and `onApprove` can include `liabilityShift`; complete authentication status still belongs to the server-side order. LPM integrations gain precise compile-time session methods and field shapes, but the type catalog is not proof of merchant, regional, buyer, or runtime availability.

**Migration action:** Upgrade React with core `^11.0.0`, install community Apple Pay typings when application code references the native global, capture only after the React approval callback or an equivalent verified server decision, handle 3DS errors, and inspect the complete order authentication result server-side when needed. Request only the required LPM components and retain separate product-eligibility checks.

**Updated source sections:** core version 11 and React version 10; [[paypal-apple-pay]], [[paypal-google-pay]], and [[paypal-apm]]; PayPal company summary; provider index and logs.

**Evidence:**

- [Core release record](../../../../raw/github/paypal/paypal-js/releases/paypal-js/11.0.0/2026-08-30/manifest.json)
- [Core release notes](../../../../raw/github/paypal/paypal-js/releases/paypal-js/11.0.0/2026-08-30/release-notes.md)
- [Snapshot manifest](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/manifest.json)
- [Core comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.1.0--11.0.0/comparison.json)
- [React release record](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.4.0/2026-08-30/manifest.json)
- [React release notes](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.4.0/2026-08-30/release-notes.md)
- [React comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.3.0--10.4.0/comparison.json)
- [Apple Pay types](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/files/packages/paypal-js/types/v6/components/applepay-payments.d.ts)
- [Google Pay types](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/files/packages/paypal-js/types/v6/components/googlepay-payments.d.ts)
- [LPM types](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/files/packages/paypal-js/types/v6/components/lpm-payments.d.ts)
- [Core v6 barrel](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/files/packages/paypal-js/types/v6/index.d.ts)

### Evidence boundary

The core release proves package declarations and package-version metadata; the loader implementation is unchanged. The React release proves wrapper callback ordering and error routing, not the deployed PayPal runtime, merchant enablement, regional availability, or a universal capture policy.

## Repository change set: `1ce6b30` (2026-07-31)

### Package timeline

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/react-paypal-js` | `10.2.1` | `10.3.0` | 2026-07-31 | `1ce6b30db4b7bcec8177a0c25aaf6408c6d523f2` | Delta |

The package-qualified release is `@paypal/react-paypal-js@10.3.0`. No `@paypal/paypal-js` package release is part of this change set.

**Important change:** The TypeScript payload for server-side `fetchEligibleMethods()` now declares optional `merchant_info.merchant_origin`. The release note says merchants can pass that origin to the Eligibility API and that previous overwriting caused a bug particularly in the Google Pay payments flow. Separately, retained code shows Eligibility API errors now include the upstream response body.

**Developer or merchant impact:** Typed server-rendered React integrations can supply an explicit merchant origin and receive more detailed failure diagnostics. Existing payloads remain valid because the new field is optional. Origin preservation is a release-note claim; retained implementation proves the request type and payload serialization.

**Migration action:** No mandatory migration is stated. Pass `payload.merchant_info.merchant_origin` when the eligibility request must preserve an explicit merchant origin, and ensure server logging does not expose upstream error details to clients.

**Updated source sections:** React version 10; [[paypal-google-pay]]; PayPal company summary; provider index and logs.

**Evidence:**

- [React release record](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/manifest.json)
- [React release notes](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/release-notes.md)
- [Snapshot manifest](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/manifest.json)
- [React comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.2.1--10.3.0/comparison.json)
- [Server eligibility helper](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/files/packages/react-paypal-js/src/v6/server/fetchEligibleMethods.ts)

### Evidence boundary

This patch proves the React wrapper's server request type, existing whole-payload serialization, and error construction. The origin-overwrite fix is attributed to the release note. The patch does not prove a change to PayPal's eligibility decision, Google Pay payment-session runtime, product availability, or the independently versioned `@paypal/paypal-js` package.

## Repository change set: `7ff3eee` (2026-07-29)

### Package timeline

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/react-paypal-js` | `10.2.0` | `10.2.1` | 2026-07-29 | `7ff3eeec13e734f24f6e8fbf9aded68437c1398e` | Delta |

The package-qualified release is `@paypal/react-paypal-js@10.2.1`. No `@paypal/paypal-js` package release is part of this change set.

**Important change:** React coordinates `PayPalProvider` eligibility hydration with child `useEligibleMethods()` effects so a no-payload client hook cannot race a server-hydrated response.

**Developer or merchant impact:** Server-rendered integrations avoid a redundant or competing client eligibility request while provider hydration is pending. Explicit client payloads remain independent and continue fetching immediately.

**Migration action:** Await `fetchEligibleMethods()` before passing its resolved value as `eligibleMethodsResponse`. Call `useEligibleMethods()` without a payload when consuming that hydrated response; supply a payload only when a distinct client-side eligibility request is intended.

**Updated source sections:** React version 10; [[paypal-checkout]]; PayPal company summary; provider index and logs.

**Evidence:**

- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.1/2026-07-30/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.1/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/manifest.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.2.0--10.2.1/comparison.json`
- Provider hydration state: `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx`
- Eligibility hook: `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts`
- Server-rendering guidance: `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/README.md`

### Evidence boundary

This patch proves React provider and hook coordination. It does not change PayPal's eligibility decision, payment-session behavior, product availability, or Braintree integration.

## Repository change set: `b496f3a` (2026-07-27)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `10.0.3` | `10.1.0` | 2026-07-27 | `b496f3a7ea2a547b99ea5fb9895dfaf8cd01f6a3` | Delta |
| `@paypal/react-paypal-js` | `10.1.2` | `10.2.0` | 2026-07-27 | `b496f3a7ea2a547b99ea5fb9895dfaf8cd01f6a3` | Delta |

The package-qualified releases are `@paypal/paypal-js@10.1.0` and `@paypal/react-paypal-js@10.2.0`.

**Important change:** Core rejects inherited `environment` and `sdkBaseUrl` option values and makes PayPal Messages content non-null through an empty failure sentinel. React adds Braintree PayPal Messages, renames the server eligibility helper, and fixes reuse of server-hydrated eligibility when the consumer omits a payload.

**Developer or merchant impact:** Prototype-polluted inherited options can no longer redirect the legacy loader to sandbox. Messages integrations receive content on API failure so their element can collapse instead of processing `null`. Braintree React merchants can fetch promotional or BNPL message content through the shared checkout instance. Server-rendered React integrations avoid an unnecessary eligibility request when the hydrated and omitted payloads are equivalent.

**Migration action:** Stop treating `fetchContent() === null` as the PayPal Messages failure contract. Import `fetchEligibleMethods()` for server eligibility and migrate away from the deprecated `useFetchEligibleMethods()` alias before the next major. For Braintree Messages, wait for `isReady`, handle provider and fetch errors separately, and pass even empty returned content to `<paypal-message>`.

**Updated source sections:** core version 10; React version 10; [[paypal-checkout]]; [[paypal-pay-later]]; [[paypal-braintree-integration]]; PayPal company summary; provider index and logs.

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/10.1.0/2026-07-30/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/10.1.0/2026-07-30/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.0/2026-07-30/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.0/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.0.3--10.1.0/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.1.2--10.2.0/comparison.json`
- Core option processing: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/paypal-js/src/utils.ts`
- PayPal Messages types: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/paypal-js/types/v6/components/paypal-messages.d.ts`
- Braintree Messages hook: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/hooks/Braintree/useBraintreePayPalMessages.ts`
- Server eligibility helper: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/server/fetchEligibleMethods.ts`
- Eligibility hydration: `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts`

### Evidence boundary

This repository proves package declarations, loader option handling, and React wrapper behavior. Braintree server processing, PayPal Messages service behavior, product rollout, and merchant eligibility remain outside this source boundary.

## Repository change set: `3caece5` (2026-07-07)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `10.0.2` | `10.0.3` | 2026-07-07 | `3caece5256428b6b5c713decbaec10ff7d785e9f` | Full |
| `@paypal/react-paypal-js` | `10.1.1` | `10.1.2` | 2026-07-07 | `3caece5256428b6b5c713decbaec10ff7d785e9f` | Full |

The package-qualified releases are `@paypal/paypal-js@10.0.3` and `@paypal/react-paypal-js@10.1.2`.

**Important change:** Core adds a v6 Venmo save-payment session typed around a vault setup token. React removes the ineffective Apple Pay button `disabled` prop, stops writing that ignored attribute during pending state, and adds `TEXT` to the PayPal Messages `logo-type` union.

**Developer or merchant impact:** TypeScript integrations can model a Venmo vault-without-payment flow, but the package contract conflicts with older product documentation that excludes Venmo from purchase-later vaulting. Apple Pay merchants must control presentation themselves rather than relying on a disabled prop. React Messages JSX accepts the additional text logo type.

**Migration action:** Treat Venmo save-payment availability as unconfirmed until the matching runtime and merchant account are verified. Remove `disabled` from `ApplePayOneTimePaymentButton`, gate presentation through merchant UI and Apple capability checks, and use `logo-type="TEXT"` only with a compatible v6 Messages runtime.

**Updated source sections:** core version 10; React version 10; [[paypal-vault]], [[paypal-apple-pay]], and [[paypal-pay-later]]; PayPal company summary; provider index and logs.

> [!warning] Contradiction
> Older Save Payment Methods and Pay with Venmo documentation says no Venmo save-for-purchase-later path exists. The core `10.0.3` declaration adds exactly such a save-payment contract. The type surface does not prove production runtime availability, so the conflict remains explicit.

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.3/2026-07-22/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.3/2026-07-22/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.2/2026-07-22/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.2/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.0.2--10.0.3/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.1.1--10.1.2/comparison.json`
- Venmo save-payment types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/files/packages/paypal-js/types/v6/components/venmo-payments.d.ts`
- Apple Pay button: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/files/packages/react-paypal-js/src/v6/components/ApplePayOneTimePaymentButton.tsx`
- Messages web-component types: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/files/packages/react-paypal-js/src/v6/types/sdkWebComponents.ts`

### Evidence boundary

This repository proves wrapper declarations and React component behavior. It does not prove runtime code owned by `paypal/paypal-checkout-components`, product rollout, merchant eligibility, or whether older product documentation has been superseded.

## Repository change set: `3d72ac9` (2026-06-29)

### Package timelines

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@paypal/paypal-js` | `10.0.1` | `10.0.2` | 2026-06-29 | `3d72ac928b059cffab3c004d83656bd964ff4a1b` | Full |
| `@paypal/react-paypal-js` | `10.1.0` | `10.1.1` | 2026-06-29 | `3d72ac928b059cffab3c004d83656bd964ff4a1b` | Full |

**Important change:** Core adds a `default` export condition to `./sdk-v6`, pointing to the existing v6 ESM build so bundlers and dependency tracers do not fall back to the v5 entry. React moves its v5 Storybook from the package workspace into a separate Storybook 10 workspace and updates its core dependency to `^10.0.2`.

The package-qualified releases are `@paypal/paypal-js@10.0.2` and `@paypal/react-paypal-js@10.1.1`.

**Developer or merchant impact:** Deployments using condition-sensitive bundlers or tracers can now resolve the intended v6 entry. React's published package output and payment integration surface are unchanged; the removed in-package stories are a tooling relocation, not removal of Venmo, subscriptions, Card Fields, Hosted Fields, or Braintree support.

**Migration action:** Upgrade core when `/sdk-v6` is misresolved and verify the emitted deployment bundle. React application consumers need no API migration. Repository maintainers should use the root v5 Storybook workspace commands.

**Updated source sections:** core version 10; React responsibility and version 10; PayPal company summary; provider index and logs. No payment concept page changed because this release contains packaging and development-tooling changes only.

**Evidence:**

- Core release record: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.2/2026-07-22/manifest.json`
- Core release notes: `raw/github/paypal/paypal-js/releases/paypal-js/10.0.2/2026-07-22/release-notes.md`
- React release record: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.1/2026-07-22/manifest.json`
- React release notes: `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.1/2026-07-22/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/manifest.json`
- Core comparison: `tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.0.1--10.0.2/comparison.json`
- React comparison: `tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.1.0--10.1.1/comparison.json`
- Core package exports: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/files/packages/paypal-js/package.json`
- React package manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/files/packages/react-paypal-js/package.json`
- Root Storybook workspace manifest: `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/files/package.json`

### Evidence boundary

The core patch proves package-entry resolution, not a runtime payment-flow change. The React release says published output is unchanged. The current capsule does not retain the files inside the newly separate Storybook workspace, so current-story implementation questions require separately collected workspace evidence; earlier story contents remain available in older immutable snapshots.

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

- [Core 11.0.0 snapshot](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-30-1246244/manifest.json) — exact-SHA source capsule
- [Core 11.0.0 release record](../../../../raw/github/paypal/paypal-js/releases/paypal-js/11.0.0/2026-08-30/manifest.json) — package-qualified release identity
- [Core 10.1.0 to 11.0.0 comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/paypal-js/10.1.0--11.0.0/comparison.json)
- [React 10.4.0 release record](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.4.0/2026-08-30/manifest.json) — package-qualified release identity
- [React 10.3.0 to 10.4.0 comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.3.0--10.4.0/comparison.json)
- [React 10.3.0 snapshot](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/manifest.json) — exact-SHA source capsule
- [React 10.3.0 release record](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/manifest.json) — package-qualified release identity
- [React 10.2.1 to 10.3.0 comparison](../../../../tracking/github/repos/paypal/paypal-js/comparisons/react-paypal-js/10.2.1--10.3.0/comparison.json)
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
