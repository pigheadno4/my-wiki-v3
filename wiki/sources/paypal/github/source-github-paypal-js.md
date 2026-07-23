---
title: "GitHub: paypal/paypal-js"
type: source
date_ingested: 2026-04-13
date_updated: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json"
  - "github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json"
  - "github-paypal-js.md"
tags: [paypal, javascript-sdk, react, npm, typescript, github-repository, venmo]
---

## Overview

`paypal/paypal-js` is PayPal's JavaScript SDK monorepo. It contains two independently versioned packages: `@paypal/paypal-js`, the vanilla loader and TypeScript definitions, and `@paypal/react-paypal-js`, the React integration layer.

This cumulative page preserves package-qualified historical findings. The immutable pipeline currently contains independent v8 baselines for `@paypal/paypal-js@8.4.2` and `@paypal/react-paypal-js@8.9.2`. Each release has its own record and exact-SHA snapshot even though both packages live in the same repository.

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

## Package status

| Package | Latest ingested release | Evidence status |
| --- | --- | --- |
| `@paypal/paypal-js` | `8.4.2` | Approved full baseline |
| `@paypal/react-paypal-js` | `8.9.2` | Approved full baseline |

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

- `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json` — exact-SHA source capsule for `@paypal/react-paypal-js@8.9.2`
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/manifest.json` — package-qualified React release record
- `raw/github/paypal/paypal-js/releases/react-paypal-js/8.9.2/2026-07-22/release-notes.md` — React patch notes
- `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json` — exact-SHA source capsule for `@paypal/paypal-js@8.4.2`
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/manifest.json` — package-qualified release record
- `raw/github/paypal/paypal-js/releases/paypal-js/8.4.2/2026-07-22/release-notes.md` — upstream patch notes
- [[github-paypal-js]] — legacy repository snapshot retained for historical links
