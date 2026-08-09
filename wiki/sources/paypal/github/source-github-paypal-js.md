---
title: "GitHub: paypal/paypal-js"
type: source
date_ingested: 2026-04-13
date_updated: 2026-08-08
original_format: github-repo
raw_files:
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
  - "github-paypal-js.md"
tags: [paypal, javascript-sdk, react, npm, typescript, github-repository, venmo]
---

## Overview

`paypal/paypal-js` is PayPal's JavaScript SDK monorepo. It contains two independently versioned packages: `@paypal/paypal-js`, the vanilla loader and TypeScript definitions, and `@paypal/react-paypal-js`, the React integration layer.

This cumulative page preserves package-qualified historical findings. The immutable pipeline contains independent v8 baselines for `@paypal/paypal-js@8.4.2` and `@paypal/react-paypal-js@8.9.2`, the shared-SHA major transition to `@paypal/paypal-js@9.8.0` and `@paypal/react-paypal-js@9.3.0`, the coordinated `10.0.0` environment-safety transition, and every collected stable v10 patch through `@paypal/paypal-js@10.1.0` and `@paypal/react-paypal-js@10.3.0`. Each package release retains its own record even when two releases point to one repository snapshot.

Repository: <https://github.com/paypal/paypal-js>

## Evidence boundary

- Package versions are not repository-wide versions. Always resolve `@paypal/paypal-js@<version>` or `@paypal/react-paypal-js@<version>`.
- A release record identifies one package release and links it to an exact-SHA repository snapshot.
- The React package delegates script loading and SDK behavior to `@paypal/paypal-js`; its component behavior remains separately versioned.
- Runtime behavior implemented by `paypal/paypal-checkout-components` is outside this repository and requires that repository's own evidence history.
- Current product guidance may be newer than an ingested historical package snapshot. Version-specific questions must use the matching release and SHA.

## Grounding excerpts

> "This is a collection of libraries intended to help developers more easily integrate with PayPal's JS SDK"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/README.md:3`

> "if (findScript(url, attributes) && existingWindowNamespace) { return PromisePonyfill.resolve(existingWindowNamespace); }"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/packages/paypal-js/src/load-script.ts:29-32`

> "clientToken: string; components: T;"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/packages/paypal-js/types/v6/index.d.ts:34-37`

> "It relies on the `<PayPalScriptProvider />` parent component for managing state related to loading the JS SDK script."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/files/packages/react-paypal-js/src/stories/venmo/VenmoButton.stories.tsx:37`

> "fix: use correct type name with v6 script load options"
>
> `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/release-notes.md:3`

> "Add optional submit options to CardFields submit() method, including billingAddress and name fields for 3DS authentication support"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/CHANGELOG.md:11`

> "The return type changes based on which components are specified in the components array."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/types/v6/index.d.ts:85-88`

> "Braintree merchants use `BraintreePayPalProvider` instead of `PayPalProvider` to integrate PayPal via Braintree's `paypalCheckoutV6` module."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/README.md:728`

> "Server-side with Braintree SDK — send the nonce to your server and process it with the Braintree server SDK (not PayPal's Orders API)"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/react-paypal-js/README.md:1165`

> "Unlike other payment methods, Google Pay does not use a start() callback pattern."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/files/packages/paypal-js/types/v6/components/googlepay-payments.d.ts:288-291`

> "**BREAKING:** The v6 `environment` option is now required on `loadCoreSdkScript`."
>
> `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/release-notes.md:3`

> "'The \"environment\" option is required and must be either \"production\" or \"sandbox\"'"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/files/packages/paypal-js/src/v6/index.ts:104-107`

> "**The `environment` prop is required.** `clientId` does not select the environment in v6"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/files/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx:59-61`

> "Augments `HTMLElementTagNameMap` so that `document.createElement()` and `document.querySelector()` return strongly-typed elements for non-React integrations"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/paypal-js/types/v6/components/web-components.d.ts:4-6`

> "Present for vault-without-purchase flows (Venmo, PayPal save-payment)."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/paypal-js/types/components/buttons.d.ts:55-56`

> "`BraintreePayPalPayLaterButton` is a prebuilt button that renders a `<paypal-pay-later-button>` web component and manages the Braintree PayPal Pay Later"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/components/Braintree/BraintreePayPalPayLaterButton.tsx:14-16`

> "**Without eligibility, the button renders with `display: none` and is invisible.**"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/components/Braintree/BraintreePayPalPayLaterButton.tsx:21-25`

> "'The \"environment\" option is required and must be either \"production\" or \"sandbox\"'"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/files/packages/react-paypal-js/src/v6/hooks/useFetchEligibleMethods.ts:99-109`

> "Add a `default` export condition to the `./sdk-v6` subpath so bundlers/tracers (e.g. @vercel/nft) resolve it correctly and don't fall back to the v5 entry."
>
> `raw/github/paypal/paypal-js/releases/paypal-js/10.0.2/2026-07-22/release-notes.md:3`

> "\"default\": \"./dist/v6/esm/paypal-js.js\""
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/files/packages/paypal-js/package.json:17-20`

> "This is a tooling/dev-dependency change only — the published package output is unchanged"
>
> `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.1/2026-07-22/release-notes.md:3`

> "\"@paypal/paypal-js\": \"^10.0.2\""
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/files/packages/react-paypal-js/package.json:61-64`

> "Adding v6 types for Venmo vault-without-payment (SavePayment)"
>
> `raw/github/paypal/paypal-js/releases/paypal-js/10.0.3/2026-07-22/release-notes.md:3`

> "Creates a Venmo save payment session for storing payment methods for future use."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/files/packages/paypal-js/types/v6/components/venmo-payments.d.ts:89-94`

> "`ApplePayOneTimePaymentButton` no longer writes a `disabled` attribute to Apple's `<apple-pay-button>`"
>
> `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.2/2026-07-22/release-notes.md:3`

> "\"logo-type\"?: \"MONOGRAM\" | \"WORDMARK\" | \"TEXT\";"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/files/packages/react-paypal-js/src/v6/types/sdkWebComponents.ts:43-50`

> "Use hasOwnProperty to avoid picking up prototype-polluted values."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/paypal-js/src/utils.ts:70-83`

> "fetchContent: (options?: FetchContentOptions) => Promise<MessageContent>;"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/paypal-js/types/v6/components/paypal-messages.d.ts:136-142`

> "Hook for creating a Braintree PayPal Messages instance to fetch promotional / BNPL messaging content for `<paypal-message>` elements."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/hooks/Braintree/useBraintreePayPalMessages.ts:27-35`

> "@deprecated Renamed to `fetchEligibleMethods`. This is a server-side async function, not a React hook"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/server/fetchEligibleMethods.ts:135-141`

> "Normalize null to undefined so a server-hydrated payload (stored as null by PayPalProvider) matches a consumer that passes no payload (undefined)."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/files/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts:115-134`

> "Fix: race condition between server-hydrated eligibility and client-side fetch"
>
> `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.1/2026-07-30/release-notes.md:3`

> "Dispatched during render (not in an effect) so children see the correct status on the same render, before their own effects run."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx:358-371`

> "Only block those on hydration; let payload-specific calls fetch immediately since hydration will never answer them."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts:108-116`

> "`eligibleMethodsResponse` must be a resolved value, not a Promise."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/files/packages/react-paypal-js/README.md:2300-2304`

> "Merchants can now pass a merchant origin to the eligibility API via the server method fetchEligibleMethods."
>
> [React 10.3.0 release notes](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/release-notes.md)

> "merchant_info?: {"
> "merchant_origin?: string;"
> "};"
>
> [React 10.3.0 server eligibility helper](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/files/packages/react-paypal-js/src/v6/server/fetchEligibleMethods.ts)

> "const body = await response.text();"
>
> [React 10.3.0 server eligibility helper](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/files/packages/react-paypal-js/src/v6/server/fetchEligibleMethods.ts)

## Package status

| Package | Latest ingested release | Evidence status |
| --- | --- | --- |
| `@paypal/paypal-js` | `10.1.0` | Approved delta ingest; v8 through 10.0.3 history retained |
| `@paypal/react-paypal-js` | `10.3.0` | Approved delta ingest; v8 through 10.2.1 history retained |

This table reports wiki ingest progress, not the latest version published upstream.

## `@paypal/paypal-js`

### Responsibility

The package describes itself as a "Loading wrapper and TypeScript types for the PayPal JS SDK." Its root export provides `loadScript()`, `loadCustomScript()`, the wrapper version, the legacy SDK namespace types, and generated Orders and Subscriptions API declarations. The `./sdk-v6` export provides `loadCoreSdkScript()` and v6 instance types.

### Legacy loader behavior

`loadScript()`:

- resolves to `null` outside a browser when `document` is unavailable;
- converts typed options into SDK query parameters and script attributes;
- defaults to the `paypal` window namespace unless `dataNamespace` is supplied;
- adds `data-js-sdk-library="paypal-js"` unless the caller supplies it;
- reuses an existing matching script only when its attributes match and the expected window namespace exists; and
- rejects after load when the configured namespace is still unavailable.

It accepts an optional Promise constructor for legacy environments. The exported `loadCustomScript()` uses the same validation and insertion path for a caller-supplied URL and attributes, returning `Promise<void>`.

The retained option surface includes:

- required `clientId` for the legacy SDK script;
- `buyerCountry`, `commit`, `components`, `currency`, `debug`, `disableFunding`, `enableFunding`, `integrationDate`, `intent`, `locale`, `merchantId`, and `vault` query options;
- client token, CSP nonce, client metadata ID, merchant ID, namespace, page type, partner attribution, integration source, UID, and user ID token data attributes;
- `crossorigin`; and
- wrapper-specific `environment` and `sdkBaseUrl` controls.

When multiple merchant IDs are passed, option processing moves the comma-separated IDs to `data-merchant-id` and uses `merchant-id=*`. Production remains the default base URL for backward compatibility; sandbox must be selected explicitly.

### Version 8

#### `@paypal/paypal-js@8.4.2`

The package exports both the legacy loader and the v6 loader subpath. Its declared v6 `createInstance()` surface requires `clientToken`, accepts a non-empty components tuple, and conditionally exposes methods for:

- `paypal-payments`;
- `venmo-payments`; and
- `paypal-legacy-billing-agreements`.

Every instance includes `findEligibleMethods()` and `updateLocale()`. The eligibility types cover PayPal, Pay Later, PayPal Credit, and Venmo. The Venmo session reuses PayPal one-time-payment callbacks but omits shipping-address and shipping-options change callbacks. Declared Venmo presentation modes are `auto`, `modal`, and `popup`.

The `8.4.2` patch corrects the v6 script-load option type name and the conditional `SdkInstance` type definitions. These are compile-time typing fixes; the release notes do not claim a new runtime checkout feature or a migration step.

The package also ships generated TypeScript declarations for Orders v2 and Billing Subscriptions v1. Those declarations are API typing context, not proof that this loader implements the server APIs.

### Version 9

#### `@paypal/paypal-js@9.8.0`

The retained v9 release is the latest selected v9 package at commit `31eb658ac885a490d38ef34e471c069b0c6e49cb`. It is a full major-version ingest from the v8.4.2 baseline, so this section records the cumulative v9 surface rather than only the four changes named in the 9.8.0 release note.

The `./sdk-v6` package surface now accepts exactly one of `clientId` or `clientToken`. Its conditional `SdkInstance` type expands from the three components evidenced in v8.4.2 to nine:

- `paypal-payments`, `venmo-payments`, and `paypal-legacy-billing-agreements`;
- `paypal-guest-payments`, `paypal-messages`, and `paypal-subscriptions`;
- `card-fields`, `applepay-payments`, and `googlepay-payments`.

Every instance exposes `findEligibleMethods()`, `updateLocale()`, and `hydrateEligibleMethods()`. The latter transforms a pre-fetched eligibility response and supports server-to-client eligibility hydration. Page typing also adds product listing and search results to the earlier checkout, product details, cart, mini-cart, and home contexts.

For Card Fields, one-time and save-payment sessions both accept an optional second `submit()` argument containing a cardholder `name` and billing address. The billing address includes address lines, administrative areas, postal code, and country code; the 9.8.0 release identifies this as support for 3DS authentication. Session `start()` presentation options are optional and default to `auto`.

Google Pay becomes a typed v6 component. Its session:

- formats eligibility configuration for Google's `PaymentsClient`;
- maps supported networks and merchant country into Google request fields;
- confirms a merchant-created PayPal order with Google payment-method data; and
- delegates native button and payment-sheet UI to Google's SDK.

The exact 9.8.0 declaration calls `initiatePayerAction()` a no-argument placeholder for future 3DS support. This package-specific limitation must not be replaced by broader current Google Pay guidance without checking the deployed SDK version.

The cumulative v9 changelog also records deterministic core-script loading, optional client-ID instance creation, eligibility hydration, Apple Pay and Google Pay component typing, and a prototype-pollution defense that accepts `sdkBaseUrl` only as an own property.

### Version 10

#### `@paypal/paypal-js@10.0.0`

The core `10.0.0` release is a focused breaking configuration change at commit `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429`. The v6 `LoadCoreSdkScriptOptions` declaration now requires `environment: "production" | "sandbox"`. `loadCoreSdkScript()` validates the options before checking server context or touching the DOM, so JavaScript callers receive a thrown `Error` when the property is missing or invalid while TypeScript callers receive a compile-time error.

After validation, the loader maps `production` to `https://www.paypal.com/web-sdk/v6/core` and `sandbox` to `https://www.sandbox.paypal.com/web-sdk/v6/core`. It no longer silently defaults an omitted value to sandbox. This prevents a live client ID from accidentally loading the sandbox SDK, but it also means every v9 direct-loader call must add an explicit environment during migration.

The release note and changed public files identify no new payment component, session, payment method, or server API behavior. The root legacy loader exports remain separate from this v6 breaking change.

#### `@paypal/paypal-js@10.0.1`

The `10.0.1` patch shares commit `59cb2ce64d158ac4f4cabecdd82f7b4191a8dff3` with React `10.1.0`. It keeps the root and `/sdk-v6` export map stable while adding public TypeScript evidence in two areas.

First, non-React integrations receive DOM element types for eight custom elements through `HTMLElementTagNameMap`: PayPal, Venmo, Pay Later, Credit, basic-card button and container, PayPal Messages, and the Apple Pay button registered by Apple's SDK. Element-specific interfaces type properties such as Pay Later country/product codes and disabled state. The v6 `PayLaterCountryCodes` union also adds Canada. These are compile-time changes; they are not evidence that this package registers or renders every element itself.

Second, the legacy Buttons `OnApproveData` type adds optional `vaultSetupToken`. Expanded `createVaultSetupToken` and `onApprove` JSDoc covers PayPal and Venmo vault-without-purchase: return a server-created `/v3/vault/setup-tokens` token, use `payment_source.venmo` for Venmo, and read the approved token from `data.vaultSetupToken` while `data.orderID` is empty. The separate v6 save-payment token type already existed at `10.0.0` and must not be attributed to this patch.

The release also migrates repository tests to Vitest 4. That is build tooling, not merchant-facing payment behavior.

#### `@paypal/paypal-js@10.0.2`

The `10.0.2` patch shares commit `3d72ac928b059cffab3c004d83656bd964ff4a1b` with React `10.1.1`. It adds a `default` condition to the `./sdk-v6` package export, pointing to the same `./dist/v6/esm/paypal-js.js` file as the existing `import` condition. The `types` condition remains `./types/v6/index.d.ts`, and the root package export is unchanged.

This is a package-resolution correction for bundlers and dependency tracers such as `@vercel/nft`. Without a matching condition, those tools could fall back to the package's v5 entry even when an integration requested `@paypal/paypal-js/sdk-v6`. The release changes how tooling resolves the existing v6 build; it does not add a payment method, session API, callback, or runtime checkout behavior.

No application API migration is stated. Consumers using the `/sdk-v6` subpath should upgrade when their bundler or deployment tracer resolves the wrong entry, then verify the emitted server or deployment bundle. The repository also upgrades `openapi-typescript`, but the retained public declaration capsule shows no release-note claim of a generated API behavior change.

#### `@paypal/paypal-js@10.0.3`

The `10.0.3` patch shares commit `3caece5256428b6b5c713decbaec10ff7d785e9f` with React `10.1.2` and adds a v6 Venmo vault-without-payment contract. When `venmo-payments` is included in the SDK instance components, `VenmoPaymentsInstance` now exposes `createVenmoSavePaymentSession()`.

The new save-session types:

- replace the one-time `onApprove` payload with optional approval data containing `vaultSetupToken`;
- allow a setup token to be supplied in the session options;
- define the deferred session input as `Promise<{ vaultSetupToken: string }>`;
- retain Venmo's `auto`, `popup`, and `modal` presentation modes; and
- return a session with `start()`, `destroy()`, and `cancel()` behavior inherited from the base session contract.

The JSDoc describes saving a buyer's Venmo account for future transactions without a purchase. Its example creates the save session, supplies a promise resolving to a vault setup token, and receives the approved token through `onApprove`.

> [!warning] Contradiction
> The 2025 Save Payment Methods and Pay with Venmo documentation says Venmo is not supported for save-for-purchase-later, while this exact package release types a Venmo save-payment session for vault setup without a purchase. The declaration proves the `10.0.3` TypeScript surface, not production eligibility or runtime implementation in `paypal/paypal-checkout-components`. Verify current product documentation, merchant enablement, and the matching runtime before offering this flow.

#### `@paypal/paypal-js@10.1.0`

The `10.1.0` release shares commit `b496f3a7ea2a547b99ea5fb9895dfaf8cd01f6a3` with React `10.2.0`. It hardens legacy script option processing by accepting both `sdkBaseUrl` and `environment` only when each is an own property of the options object. An inherited `environment="sandbox"` value can therefore no longer switch a production-default script URL to sandbox through prototype pollution.

The v6 PayPal Messages declaration also changes `PayPalMessagesSession.fetchContent()` from `Promise<MessageContent | null>` to `Promise<MessageContent>`. API failures resolve to an empty sentinel content object rather than `null`, allowing `<paypal-message>` to receive that content and collapse its presentation. Integrations should process the returned content object and must not depend on a `null` result to identify this failure path.

The release does not add a payment method or establish merchant eligibility. The option-processing protection belongs to the legacy loader path, while the Messages declaration describes the v6 package contract.

## `@paypal/react-paypal-js`

### Responsibility

The package describes itself as "React components for the PayPal JS SDK." It owns React lifecycle, context, reducer, component, and hook behavior while delegating script loading and SDK runtime calls to `@paypal/paypal-js`.

The React package:

- wraps script loading in `PayPalScriptProvider`;
- uses reducer state for initial, pending, resolved, and rejected script states;
- removes the existing SDK script before resetting options;
- exports Buttons, Marks, Messages, Braintree buttons, Hosted Fields, Card Fields, and related hooks; and
- retains historical Storybook examples as integration evidence in earlier capsules; from `10.1.1`, the v5 stories live in a separate repository workspace rather than in the published package workspace.

The retained Venmo story configures `buttons,funding-eligibility`, enables Venmo funding, and renders `PayPalButtons` with the Venmo funding source. This is an example for the React package and legacy JS SDK button flow; it is distinct from the v6 `venmo-payments` session types in `@paypal/paypal-js`.

### Version 8

#### `@paypal/react-paypal-js@8.9.2`

This release is the exact v8 React baseline at commit `77487d6cea80c2df694166e5d8f5c420cca41e7e`. Its public component and hook architecture remains consistent with the earlier focused v8 review, but Card Fields callback handling changes materially.

Grounding excerpts:

> "(fix) Proxy props added to Card Fields to prevent stale closure"
>
> `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/release-notes.md:3`

> "new copies of this function without having to re-render the SDK components to pass new callbacks."
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/hooks/useProxyProps.ts:12-14`

> "const proxyProps = useProxyProps(props);"
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/src/components/cardFields/PayPalCardFieldsProvider.tsx:39`

> "\"@paypal/paypal-js\": \"^9.0.0\""
>
> `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/files/packages/react-paypal-js/package.json:49`

`useProxyProps()` keeps one stable JavaScript `Proxy` in a React ref. On every render it assigns the newest props to that proxy. When a proxied property is a function, the proxy returns a wrapper that looks up and invokes the current function at call time. This allows an SDK component initialized once to call current React callbacks without requiring SDK re-rendering.

React 8.9.2 applies that mechanism at two Card Fields levels:

- `PayPalCardFieldsProvider` proxies the full provider props and separately proxies `inputEvents` before creating `paypal.CardFields(...)`.
- `PayPalCardField` proxies each individual field's `inputEvents` before registering and rendering the field.

The retained `WithDynamicOrderState` stories vary React state after the Card Fields objects have mounted. They observe current state in `createOrder`, `onApprove`, provider input events, and the Name, Number, Expiry, and CVV field event callbacks. These stories are integration evidence for the stale-closure fix; tests remain excluded from the capsule.

The package dependency moves from `@paypal/paypal-js ^8.4.0` in collateral React 8.9.1 context to `@paypal/paypal-js ^9.0.0` in React 8.9.2. This is a package compatibility requirement, not permission to mark `@paypal/paypal-js@9.0.0` as independently ingested. The React release notes also mention a package-lock v3 and Rollup dependency fix, which affects repository/build maintenance rather than merchant integration behavior.

No API migration is stated for application code. Merchants using dynamic Card Fields callbacks should upgrade to receive fresh React state without rebuilding the SDK component.

#### Collateral React 8.9.1 context

The earlier `@paypal/paypal-js@8.4.2` SHA contains `@paypal/react-paypal-js@8.9.1` depending on `@paypal/paypal-js ^8.4.0`. It remains useful comparison context but is not a separately ingested React release.

### Version 9

#### `@paypal/react-paypal-js@9.3.0`

React 9.3.0 is the paired v9 release at the same `31eb658ac885a490d38ef34e471c069b0c6e49cb` SHA and depends on `@paypal/paypal-js ^9.8.0`. The root export remains the legacy React integration; the v6 client and server surfaces are explicitly exported as `@paypal/react-paypal-js/sdk-v6` and `@paypal/react-paypal-js/sdk-v6/server`.

The v6 `PayPalProvider` replaces the v8 `PayPalScriptProvider` integration pattern. It:

- accepts mutually exclusive `clientId` or `clientToken` values as strings, Promises, or deferred `undefined`;
- loads the v6 core script and defaults `components` to `paypal-payments`;
- creates the component-qualified SDK instance;
- optionally hydrates a pre-fetched eligibility response; and
- holds instance, eligibility, loading, error, and hydration state in React contexts.

Eligibility is not fetched automatically by the provider. Client integrations use `useEligibleMethods()`; server rendering can use the `/sdk-v6/server` export and pass the response into `eligibleMethodsResponse`.

> [!warning] Contradiction
> [[source-github-paypal-js-v6]] previously said `PayPalProvider` calls `findEligibleMethods()` on mount. The exact v9 changelog says the default eligibility request was removed, and the 9.3.0 provider only hydrates an explicitly supplied response. The older source summary is corrected accordingly.

The v6 public export includes provider, prebuilt button, and session-hook paths for PayPal one-time and saved payments, Venmo, Pay Later, PayPal Credit, guest payments, subscriptions, Card Fields, Apple Pay, Google Pay, and PayPal Messages. Buttons wait for client hydration, while hooks expose loading and error state for custom UI.

React 9.3.0 passes the new optional Card Fields `name` and billing-address submit values through one-time and save-payment hooks. It also makes presentation mode optional for v6 buttons and hooks, with each hook supplying its own default.

Google Pay uses a native Google button rather than a PayPal web component. `useGooglePayOneTimePaymentSession()` creates Google's `PaymentsClient`, checks `isReadyToPay()`, creates the native button, creates the PayPal order during authorization, and calls `confirmOrder()`. The exact wrapper invokes the core placeholder `initiatePayerAction()` when confirmation returns `PAYER_ACTION_REQUIRED`; this is not sufficient evidence of a complete awaited 3DS flow.

#### Braintree PayPal surface

React 9.3.0 adds a separate Braintree path under the same `/sdk-v6` export:

- `BraintreePayPalProvider` validates a Braintree namespace, creates a client from a server-generated Braintree client token, creates `paypalCheckoutV6`, loads the PayPal SDK, and tears down the instance on unmount.
- One-time payment, billing-agreement, and checkout-with-vault flows each have a prebuilt `<paypal-button>` wrapper and a custom session hook.
- Billing agreements support vault-only, recurring, subscription, unscheduled, and installment plan types.
- Checkout with vault combines one-time payment and billing-agreement consent.

These are nonce-based Braintree flows. The Braintree SDK creates the payment session from amount and currency, so the merchant does not provide PayPal `createOrder`. After approval, the integration calls `tokenizePayment()` with order/payer IDs or a billing token, sends the resulting nonce to its server, and processes it with a Braintree server SDK rather than PayPal's Orders API. See [[paypal-braintree-integration]].

#### Migration from React 8

The major integration migration is package-surface specific:

| React 8 legacy integration | React 9 v6 integration |
| --- | --- |
| Root import | `@paypal/react-paypal-js/sdk-v6` |
| `PayPalScriptProvider` with `options` | `PayPalProvider` with direct `clientId` or `clientToken` |
| `PayPalButtons` | Product-specific button components or session hooks |
| `createOrder` returns an order ID string | v6 callbacks return `{ orderId }` |
| Provider-managed script state | Provider plus explicit eligibility hook or hydrated response |

The root export still exists for legacy use. A merchant must choose the integration surface deliberately rather than treating package major 9 as an automatic runtime migration.

### Version 10

#### `@paypal/react-paypal-js@10.0.0`

The coordinated React `10.0.0` release shares commit `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429` and depends on `@paypal/paypal-js ^10.0.0`. For the `/sdk-v6` surface, `PayPalProvider` inherits the required `environment` property from the core loader options and forwards it to `loadCoreSdkScript()`.

The provider documentation is explicit that `clientId` does not select the environment. A live client ID still loads the sandbox SDK when `environment="sandbox"`; applications must pass `environment="production"` for production traffic. Missing or invalid values fail through the core v10 validation path.

Migration from React v9 is additive to the existing source history:

- add `environment="production"` or `environment="sandbox"` to every v6 `PayPalProvider`;
- audit environment configuration independently from client-ID selection;
- run TypeScript checks to find missing props and exercise runtime configuration for untyped callers; and
- retain the established v9 component, eligibility, session, and Braintree behavior unless a later package-qualified release changes it.

The changed React files do not establish new payment functionality. `BraintreePayPalProvider` is a separate provider path and is not evidence that this `PayPalProvider` environment change applies to Braintree integrations.

#### `@paypal/react-paypal-js@10.1.0`

React `10.1.0` depends on `@paypal/paypal-js ^10.0.1` and adds three public Braintree exports under `/sdk-v6`: `BraintreePayPalPayLaterButton`, `useBraintreePayPalPayLaterSession()`, and `useBraintreeEligibleMethods()`.

The Pay Later hook creates a Braintree `createPayLaterSession()` with amount, currency, callbacks, shipping data, and presentation options. The prebuilt component renders `<paypal-pay-later-button>` and starts that session. Approval remains a Braintree flow: the merchant tokenizes the approval data and processes the nonce server-side.

Pay Later is eligibility-gated. `useBraintreeEligibleMethods()` calls the checkout instance's `findEligibleMethods()`, caches the result and request payload in provider context, deduplicates by checkout instance plus deep-equal options, and refetches when options change. Its typed result covers only PayPal, Pay Later, and Credit. The prebuilt button reads Pay Later country/product details from that result; integrations should wait for eligibility and avoid rendering when `paylater` is false.

Provider and eligibility errors become more actionable. Provider initialization errors are retained in context and surfaced separately from a missing checkout instance. Eligibility clears stale errors before refetch, avoids duplicate fetches, resets interrupted fetch markers, and treats payload-mismatched cached data as loading so stale buttons do not flash.

The release expands shipping types:

- one-time and Pay Later sessions add `shippingCallbackUrl`, typed `shippingAddressOverride`, and `contactPreference`;
- billing agreements replace the unstructured address override with `BraintreeShippingAddressOverride`; and
- checkout-with-vault adds `shippingCallbackUrl`.

> [!warning] Contradiction
> The release note says `shippingAddressOverride` and `contactPreference` were also added to checkout-with-vault. The exact `BraintreeCheckoutWithVaultSessionOptions` type and hook at this SHA expose only `shippingCallbackUrl`. The source declaration and implementation take precedence for this version.

Other fixes affect integration correctness:

- server-side `useFetchEligibleMethods()` now requires `environment`, validates it, and chooses the production or sandbox eligibility API explicitly;
- the basic-card JSX type uses the actual `buyer-country` attribute instead of ineffective `buyerCountry`;
- Google Pay reports a clear setup error through hook state and `onError` when `pay.js` is absent; and
- standard eligibility refetches clear stale errors and avoid a perpetual loading state after interrupted effects.

Migration from `10.0.0` is additive: provide `environment` to every server eligibility call, fetch Braintree eligibility before Pay Later rendering, change manually supplied basic-card buyer-country JSX to `buyer-country`, load Google `pay.js` before mounting Google Pay, and distinguish provider initialization errors from session errors.

#### `@paypal/react-paypal-js@10.1.1`

React `10.1.1` shares commit `3d72ac928b059cffab3c004d83656bd964ff4a1b` with core `10.0.2` and updates its runtime dependency to `@paypal/paypal-js ^10.0.2`.

The package's v5 Storybook is migrated from Storybook 6 to Storybook 10 with `@storybook/react-vite` and extracted into the separate `@paypal/react-paypal-js-storybook-v5` workspace. The root repository manifest now declares `packages/react-paypal-js-storybook/*` workspaces and dedicated v5/v6 Storybook scripts. Correspondingly, the React package removes its Storybook scripts, Storybook-only development dependencies, and in-package `src/stories` files.

The release notes state that the published package output is unchanged. The removed stories include useful Venmo, subscriptions, Card Fields, Hosted Fields, and Braintree examples, but their relocation is documentation/tooling maintenance rather than evidence that those integration behaviors were removed. Earlier immutable capsules remain the evidence authority for their historical contents; a future query about the relocated current stories requires a snapshot policy that includes the separate Storybook workspace.

No merchant application migration is required. Package maintainers use the root workspace's v5 Storybook commands, while application consumers receive the core `10.0.2` dependency range and otherwise retain the `10.1.0` public React surface.

#### `@paypal/react-paypal-js@10.1.2`

React `10.1.2` shares commit `3caece5256428b6b5c713decbaec10ff7d785e9f` with core `10.0.3` and updates its runtime dependency to `@paypal/paypal-js ^10.0.3`.

`ApplePayOneTimePaymentButton` removes its public `disabled` prop and no longer derives a disabled attribute from the Apple Pay hook's pending state. Apple's `<apple-pay-button>` ignored that attribute and manages availability through `canMakePayments()`, so the component now leaves presentation control to the merchant. It still attaches the click listener directly to the custom element because React's `onClick` does not cross the element's shadow DOM.

For PayPal Messages, the typed `<paypal-message>` `logo-type` attribute adds `TEXT` alongside `MONOGRAM` and `WORDMARK`. This is a JSX/TypeScript surface expansion; the release does not claim a broader Messages runtime or eligibility change.

Migration from `10.1.1` is narrow:

- remove `disabled` from `ApplePayOneTimePaymentButton` usage and control whether the component is presented in merchant UI;
- continue using Apple capability checks rather than treating an HTML disabled attribute as an availability gate; and
- permit `logo-type="TEXT"` where the matching v6 Messages runtime supports it.

#### `@paypal/react-paypal-js@10.2.0`

React `10.2.0` shares commit `b496f3a7ea2a547b99ea5fb9895dfaf8cd01f6a3` with core `10.1.0` and updates its runtime dependency to `@paypal/paypal-js ^10.1.0`.

The `/sdk-v6` surface adds `useBraintreePayPalMessages()`. It asynchronously creates a Messages instance through Braintree's shared `paypalCheckoutV6` object, exposes `isReady`, `isLoading`, `error`, and `handleFetchContent()`, and supports amount updates through the returned message content. Instance, provider-context, and content-fetch failures remain distinguishable. When Braintree returns an empty message sentinel, the hook sets a fetch error but still returns the content so `<paypal-message>` can collapse.

The server eligibility helper is renamed from `useFetchEligibleMethods()` to `fetchEligibleMethods()` because it is an async server function rather than a React hook. The old export remains as a deprecated alias for this release, and related client type aliases also remain deprecated rather than being removed. Consumers should migrate imports before the next major version.

Eligibility hydration now treats the provider's stored `null` payload and a consumer's omitted `undefined` payload as equivalent. A hydrated result is reused only when `useEligibleMethods()` is called without a different payload; supplying a payload still triggers the matching client-side eligibility request.

The TypeScript build cache moves outside `dist`, preventing stale incremental output after the distribution directory is removed. This is build correctness, not a payment API change. No public API incompatibility is reported for this release.

#### `@paypal/react-paypal-js@10.2.1`

React `10.2.1` is a contained patch at commit `7ff3eeec13e734f24f6e8fbf9aded68437c1398e`. It fixes a race between `PayPalProvider` hydrating server-fetched eligibility and a child `useEligibleMethods()` effect starting a client request.

The provider now tracks eligibility hydration separately from general SDK loading. When `eligibleMethodsResponse` is present, it exposes hydration as pending on the same render before child effects run, records successful hydration independently, and reports hydration errors as rejected. A no-payload `useEligibleMethods()` call waits while this hydration is pending, then reuses the hydrated result rather than issuing a competing request.

Payload-specific calls do not wait. Server-hydrated eligibility is stored without a client payload and cannot answer a different payload-specific query, so `useEligibleMethods({ payload })` still fetches immediately for that configuration.

For server rendering, await `fetchEligibleMethods()` and pass its resolved response to `eligibleMethodsResponse`; do not pass a Promise. Consume that hydrated result by calling `useEligibleMethods()` without a payload. No public API incompatibility, payment-session change, or new payment method is reported.

#### `@paypal/react-paypal-js@10.3.0`

React `10.3.0` is a contained minor release at commit `1ce6b30db4b7bcec8177a0c25aaf6408c6d523f2`. It extends the TypeScript `FindEligiblePaymentMethodsRequestPayload` with optional `merchant_info.merchant_origin`. The helper already serializes the supplied payload, so the retained implementation proves typed support for sending this field rather than a new serialization path.

The release note states that merchants can pass a merchant origin through `fetchEligibleMethods()` and that previous origin overwriting caused a bug particularly in the Google Pay payments flow. A typed server call can supply it as follows; the field remains optional, so existing calls remain valid.

```ts
await fetchEligibleMethods({
  environment: "production",
  headers,
  payload: { merchant_info: { merchant_origin: "https://checkout.example.com" } },
});
```

The helper also reads the response body for non-successful Eligibility API responses and includes that body after the HTTP status in the thrown error. This improves server diagnostics but may expose upstream error text to application logs, so merchants should continue controlling how server errors are logged or returned to clients.

This release does not update the package's `@paypal/paypal-js ^10.1.0` dependency and does not establish a new core package release, payment method, eligibility decision, or Google Pay runtime behavior. Retained code proves the React wrapper's request typing and error construction; the origin-preservation behavior is attributed to the release note.

## Historical evidence retained from the earlier ingest

The earlier repository review at commit `f59f94baefea4b2ddb38553669ed0ac4ede86167` established the legacy loader option handling above and recorded a broader v6 component set, including guest payments, card fields, messages, subscriptions, Apple Pay, and Google Pay. That snapshot did not retain an exact package-qualified release identity, so its broader surface is useful historical context but must not be attributed to `@paypal/paypal-js@8.4.2`.

Additional focused findings remain available through:

- [[source-github-react-paypal-js-v8]] — focused React v8 implementation evidence;
- [[source-github-paypal-js-v6]] — later SDK v6 and React v9 source evidence; and
- [[source-npm-react-paypal-js-v9]] — package documentation for React v9.

These pages must not be used as substitutes for an exact package release when answering version-specific questions.

## Release history

See [[changelog-github-paypal-js]] for the chronological package release ledger and path-qualified release evidence.

## Related

- Company: [[paypal]]
- Concepts: [[paypal-checkout]], [[paypal-vault]]
- Sources: [[source-paypal-javascript-sdk-reference]], [[source-paypal-js-sdk-v6-setup]]

## Raw Sources

- [React 10.3.0 snapshot](../../../../raw/github/paypal/paypal-js/snapshots/2026-08-08-1ce6b30/manifest.json) — exact-SHA source capsule
- [React 10.3.0 release record](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/manifest.json) — package-qualified release identity
- [React 10.3.0 release notes](../../../../raw/github/paypal/paypal-js/releases/react-paypal-js/10.3.0/2026-08-08/release-notes.md) — merchant-origin eligibility notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-30-7ff3eee/manifest.json` — exact-SHA source capsule for React `10.2.1`
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.1/2026-07-30/manifest.json` — package-qualified React `10.2.1` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.1/2026-07-30/release-notes.md` — SSR eligibility hydration race patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-30-b496f3a/manifest.json` — shared exact-SHA source capsule for core `10.1.0` and React `10.2.0`
- `raw/github/paypal/paypal-js/releases/paypal-js/10.1.0/2026-07-30/manifest.json` — package-qualified core `10.1.0` release record
- `raw/github/paypal/paypal-js/releases/paypal-js/10.1.0/2026-07-30/release-notes.md` — loader and Messages patch notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.0/2026-07-30/manifest.json` — package-qualified React `10.2.0` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.2.0/2026-07-30/release-notes.md` — Braintree Messages and eligibility patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-3caece5/manifest.json` — shared exact-SHA source capsule for core `10.0.3` and React `10.1.2`
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.3/2026-07-22/manifest.json` — package-qualified core `10.0.3` release record
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.3/2026-07-22/release-notes.md` — Venmo save-payment patch notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.2/2026-07-22/manifest.json` — package-qualified React `10.1.2` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.2/2026-07-22/release-notes.md` — Apple Pay and Messages patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-3d72ac9/manifest.json` — shared exact-SHA source capsule for core `10.0.2` and React `10.1.1`
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.2/2026-07-22/manifest.json` — package-qualified core `10.0.2` release record
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.2/2026-07-22/release-notes.md` — core package-resolution patch notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.1/2026-07-22/manifest.json` — package-qualified React `10.1.1` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.1/2026-07-22/release-notes.md` — React Storybook-tooling patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-59cb2ce/manifest.json` — shared exact-SHA source capsule for core `10.0.1` and React `10.1.0`
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.1/2026-07-22/manifest.json` — package-qualified core `10.0.1` release record
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.1/2026-07-22/release-notes.md` — core patch notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.0/2026-07-22/manifest.json` — package-qualified React `10.1.0` release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.1.0/2026-07-22/release-notes.md` — React minor-release notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json` — shared exact-SHA source capsule for the coordinated `10.0.0` releases
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/manifest.json` — package-qualified core v10 release record
- `raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-22/release-notes.md` — core v10 breaking-change notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.0.0/2026-07-22/manifest.json` — package-qualified React v10 release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/10.0.0/2026-07-22/release-notes.md` — React v10 breaking-change notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json` — shared exact-SHA source capsule for the selected v9 releases
- `raw/github/paypal/paypal-js/releases/paypal-js/9.8.0/2026-07-22/manifest.json` — package-qualified core v9 release record
- `raw/github/paypal/paypal-js/releases/paypal-js/9.8.0/2026-07-22/release-notes.md` — core 9.8.0 release notes
- `raw/github/paypal/paypal-js/releases/react-paypal-js/9.3.0/2026-07-22/manifest.json` — package-qualified React v9 release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/9.3.0/2026-07-22/release-notes.md` — React 9.3.0 release notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json` — exact-SHA source capsule for `@paypal/react-paypal-js@8.9.2`
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/manifest.json` — package-qualified React release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/release-notes.md` — React patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json` — exact-SHA source capsule for `@paypal/paypal-js@8.4.2`
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json` — package-qualified release record
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/release-notes.md` — upstream patch notes
- [[github-paypal-js]] — legacy repository snapshot retained for historical links
