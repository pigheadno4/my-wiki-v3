---
title: "GitHub: stripe/react-stripe-js"
type: source
date_ingested: 2026-05-08
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/manifest.json"
  - "github-react-stripe-js.md"
tags: [stripe, react, stripe-js, elements, checkout, typescript, github-repository]
---

## Overview

`stripe/react-stripe-js` publishes `@stripe/react-stripe-js`, the official React component and hook layer for Stripe.js and Elements. This cumulative page preserves the legacy `6.3.0` manual capsule and adds the approved `@stripe/react-stripe-js@6.8.0` baseline at commit `a742a105cdf297aa28f87bac5292c27a60defad3`.

Repository: <https://github.com/stripe/react-stripe-js>

## Evidence Boundary

- This repository owns React providers, hooks, component lifecycle, and TypeScript props. Runtime payment behavior is delegated to `@stripe/stripe-js` and the Stripe-hosted Stripe.js runtime.
- An exported component or declaration does not prove account eligibility, runtime rollout, payment-method availability, or recurring-payment support.
- The current immutable collector first retained `6.8.0`. The older `6.3.0` evidence is a legacy manual capsule, so this page preserves it as historical context without presenting an automated exact diff.
- Generated `dist/` targets are declared public package outputs but are not tracked in the upstream repository. The retained source capsule covers their source inputs rather than generated bundles.
- Tests were excluded by the approved capsule policy. Examples and the complete retained public source were included.

> [!warning] Contradiction
> The 2025 summary in [[source-stripe-react-stripejs]] describes the entire `Elements.options` prop as immutable. The retained `6.8.0` implementation blocks updates only for `clientSecret` and `fonts`, then forwards other changed options through `elements.update()`. Treat the older statement as dated documentation context.

## Grounding Excerpts

> "React components for
> [Stripe.js and Elements](https://stripe.com/docs/stripe-js)."
>
> `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/README.md:1-4`

> "The minimum supported version of React is v16.8."
>
> `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/README.md:8-13`

> `"@stripe/stripe-js": ">=9.5.0 <10.0.0",`
>
> `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/package.json:134-137`

> "`useCheckout()` will keep working under both providers and returns the Elements-shaped result for backward compatibility."
>
> `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/components/CheckoutContext.tsx:161-171`

> "Requires beta access:
> Contact [Stripe support](https://support.stripe.com/) for more information."
>
> `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/index.ts:79-85`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `@stripe/react-stripe-js` | `6.8.0` | `a742a105cdf297aa28f87bac5292c27a60defad3` | Approved full baseline; legacy v6.3.0 retained |

This table reports wiki ingest progress, not the latest version published upstream.

## Package Shape and Compatibility

Version `6.8.0` publishes two explicit entrypoints:

- `@stripe/react-stripe-js` for standard Elements, Embedded Checkout, disclosure components, hooks, and the root Element component set.
- `@stripe/react-stripe-js/checkout` for Checkout Elements and beta Checkout Form providers, hooks, and components.

Both entrypoints declare separate CommonJS, ES module, and TypeScript outputs under generated `dist/`. The package requires:

- `@stripe/stripe-js >=9.5.0 <10.0.0`;
- React `>=16.8.0 <20.0.0`; and
- React DOM `>=16.8.0 <20.0.0`.

The README directs consumers to install both React Stripe.js and Stripe.js. Type declarations imported from `@stripe/stripe-js` are part of the public contract, so compatible versions must be resolved together.

## Standard Elements Surface

`Elements` accepts a Stripe object, a promise resolving to one, or `null` for initial server rendering. It creates and publishes Stripe and Elements context once the Stripe object is available. Replacing a non-null `stripe` prop is unsupported.

The provider treats `clientSecret` and `fonts` as immutable. Other changed options are compared recursively and forwarded to `elements.update()`. The `useStripe()` and `useElements()` hooks expose the current context; `ElementsConsumer` provides the same values to class components.

The root entrypoint exports:

- Card, split-card, IBAN, Payment, Address, Link Authentication, Express Checkout, Payment Request Button, Payment Method Messaging, Contact Details, Tax ID, and Currency Selector components;
- five Issuing components for card number, CVC, expiry, PIN, and copy-button rendering;
- beta-gated `TermsElement`;
- `EmbeddedCheckoutProvider` and `EmbeddedCheckout`; and
- Financial Account and Issuing disclosure components.

`createElementComponent()` owns the shared lifecycle. It creates the appropriate underlying Element, attaches only requested event callbacks, updates mutable options, mounts once, and destroys the Element during cleanup. On the server it renders only the wrapper element after validating provider context.

## Checkout Surfaces

### Checkout Elements

`CheckoutElementsProvider` calls `stripe.initCheckoutElementsSdk(options)`. After `loadActions()` succeeds, it combines the SDK methods, Checkout actions, and current session into the success value returned by `useCheckoutElements()`. Session changes update that value.

The provider can apply later `elementsOptions.appearance` and `elementsOptions.fonts` changes through the Checkout SDK. Its `clientSecret` remains part of the one-time initialization contract.

### Checkout Form

`CheckoutFormProvider` calls the beta `stripe.initCheckoutFormSdk(options)`. `useCheckoutForm()` returns the narrower Form action surface, reflecting fields and actions owned by the form UI. Appearance and fonts are top-level options for this provider.

`useCheckout()` is retained as an Elements-shaped backward-compatibility alias, but it has been deprecated since `6.3.0` and is scheduled for removal in v7. Provider-specific code should use `useCheckoutElements()` or `useCheckoutForm()`. The runtime rejects calling a provider-specific hook under the wrong provider.

An application cannot wrap the same consumer in both standard `Elements` and a Checkout provider.

### Checkout Components

The `/checkout` entrypoint maps:

- `PaymentElement` to `createPaymentElement()`;
- `CheckoutForm` to the Form SDK's `createForm()`;
- Express Checkout, Tax ID, Contact Details, billing address, and shipping address to their Checkout SDK factories;
- Currency Selector to the shared Checkout SDK; and
- beta `TermsElement` to `createTermsElement()`.

Billing and shipping wrappers inject their fixed address mode. Unsupported Element types inside a Checkout provider throw instead of silently falling back to standard Elements.

## Embedded Checkout and SSR

`EmbeddedCheckoutProvider` accepts `clientSecret` or `fetchClientSecret`, initializes `createEmbeddedCheckoutPage()` once, and destroys the instance when the provider unmounts. `EmbeddedCheckout` mounts and unmounts that instance in the browser; on the server it returns a context-validated wrapper `div`.

Standard and Checkout providers also allow a `null` Stripe value for server rendering. This is an initialization allowance, not permission to swap between populated Stripe instances later.

## Version History

### `@stripe/react-stripe-js@6.8.0`

The exact release note is limited to adding Terms Element. The retained full baseline also establishes the current package shape, compatibility window, provider-specific Checkout hooks, Checkout Form surface, Issuing components, SSR behavior, and component lifecycle. Those broader findings describe the complete `6.8.0` capsule and must not be attributed solely to the patch note.

Both root and `/checkout` Terms components carry explicit beta-access notices. Merchants must verify access separately.

### Legacy `@stripe/react-stripe-js@6.3.0`

The prior manual capsule established the standard `Elements`, `useStripe()`, `useElements()`, and `ElementsConsumer` path; Checkout Elements through `CheckoutElementsProvider` and `useCheckoutElements()`; Embedded Checkout; the shared Element factory; and Payment Element examples.

The `6.8.0` baseline preserves these responsibilities while adding later public surfaces. Because the old capsule predates the immutable collector and no automated `6.3.0--6.8.0` comparison exists, this page does not claim an exhaustive transition.

## Integration Guidance

- Call `loadStripe()` outside React render so the Stripe object is not recreated.
- Disable submission until the required Stripe, Elements, or Checkout state is ready.
- For Payment Element flows, call `elements.submit()` before server-side Intent creation when using the deferred client-secret pattern, then confirm with the same Elements instance.
- Use provider-specific Checkout hooks; do not start new code on deprecated `useCheckout()`.
- Treat Stripe objects and initialization secrets as immutable provider inputs. Remount a new provider for a genuinely new instance.
- Re-run TypeScript checks whenever either React Stripe.js or `@stripe/stripe-js` changes because the React package imports its runtime-facing types from Stripe.js.
- Verify beta access and runtime feature availability independently of the React export surface.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-elements]], [[stripe-checkout]], [[stripe-express-checkout-element]], [[stripe-address-element]]
- Runtime and declaration dependency: [[source-github-stripe-js]]
- Documentation reference: [[source-stripe-react-stripejs]]
- History: [[changelog-github-react-stripe-js]]

## Raw Sources

- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/manifest.json` — exact-SHA `6.8.0` source capsule
- `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.0/2026-07-30/manifest.json` — package-qualified release record
- `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.0/2026-07-30/release-notes.md` — exact upstream release note
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/README.md` — purpose, installation, React requirement, and usage
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/package.json` — entrypoints and peer compatibility
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/index.ts` — root public exports
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/components/Elements.tsx` — standard provider and hooks
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/components/createElementComponent.tsx` — shared component lifecycle
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/components/EmbeddedCheckoutProvider.tsx` — Embedded Checkout initialization
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/index.ts` — Checkout entrypoint components
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/components/CheckoutContext.tsx` — provider-specific hook contracts
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/components/CheckoutElementsProvider.tsx` — Checkout Elements provider
- `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/components/CheckoutFormProvider.tsx` — Checkout Form provider
- `raw/github-react-stripe-js.md` — legacy `6.3.0` manual capsule pointer
