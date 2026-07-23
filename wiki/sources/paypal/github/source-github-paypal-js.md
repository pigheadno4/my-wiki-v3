---
title: "GitHub: paypal/paypal-js"
type: source
date_ingested: 2026-04-13
date_updated: 2026-07-23
original_format: github-repo
raw_files:
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

This cumulative page preserves package-qualified historical findings. The immutable pipeline contains independent v8 baselines for `@paypal/paypal-js@8.4.2` and `@paypal/react-paypal-js@8.9.2`, the shared-SHA major transition to `@paypal/paypal-js@9.8.0` and `@paypal/react-paypal-js@9.3.0`, the coordinated `10.0.0` environment-safety transition, and the shared-SHA `@paypal/paypal-js@10.0.1` plus `@paypal/react-paypal-js@10.1.0` feature release. Each package release retains its own record even when two releases point to one repository snapshot.

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

## Package status

| Package | Latest ingested release | Evidence status |
| --- | --- | --- |
| `@paypal/paypal-js` | `10.0.1` | Approved full patch ingest; v8, v9, and 10.0.0 history retained |
| `@paypal/react-paypal-js` | `10.1.0` | Approved full minor ingest; v8, v9, and 10.0.0 history retained |

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

## `@paypal/react-paypal-js`

### Responsibility

The package describes itself as "React components for the PayPal JS SDK." It owns React lifecycle, context, reducer, component, and hook behavior while delegating script loading and SDK runtime calls to `@paypal/paypal-js`.

The React package:

- wraps script loading in `PayPalScriptProvider`;
- uses reducer state for initial, pending, resolved, and rejected script states;
- removes the existing SDK script before resetting options;
- exports Buttons, Marks, Messages, Braintree buttons, Hosted Fields, Card Fields, and related hooks; and
- retains Storybook examples as integration evidence.

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
