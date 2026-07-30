---
title: "GitHub changelog: stripe/react-stripe-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/manifest.json"
  - "github-react-stripe-js.md"
tags: [stripe, react, stripe-js, elements, checkout, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/react-stripe-js`. Cumulative implementation knowledge belongs in [[source-github-react-stripe-js]] and the linked immutable evidence.

## `@stripe/react-stripe-js@6.8.0` — Change Set `a742a10` (2026-07-15)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/react-stripe-js` | Legacy retained `6.3.0` context | `6.8.0` | 2026-07-15 | `a742a105cdf297aa28f87bac5292c27a60defad3` | Full |

**Important change:** The exact `6.8.0` release note adds Terms Element. The full baseline additionally records the current root and `/checkout` package surfaces, provider-specific Checkout hooks, beta Checkout Form support, Issuing components, SSR handling, component lifecycle, and peer-dependency boundaries.

**Developer or merchant impact:** React integrations can use typed Terms components under standard Elements or Checkout Elements, but both exports require beta access. Existing code should move from deprecated `useCheckout()` to `useCheckoutElements()` or `useCheckoutForm()` according to its provider. Consumers must pair this release with `@stripe/stripe-js >=9.5.0 <10.0.0` and React/React DOM `>=16.8.0 <20.0.0`.

**Migration action:** Verify beta access before adopting Terms Element, replace deprecated `useCheckout()` calls with the matching provider-specific hook, keep Stripe and initialization-secret props stable, and run package and TypeScript compatibility checks when upgrading React Stripe.js together with Stripe.js.

**Updated source sections:** evidence boundary; package shape and compatibility; standard Elements; Checkout Elements and Form; Embedded Checkout and SSR; version history; Stripe company; Stripe Elements and Checkout concepts.

**Evidence boundary:** Adding Terms Element is the only change attributable specifically to the `6.8.0` release note. No immutable automated comparison exists from the legacy `6.3.0` manual capsule, so broader findings describe the complete retained `6.8.0` baseline rather than an exhaustive `6.3.0--6.8.0` diff. React exports do not prove Stripe-hosted runtime rollout or merchant eligibility.

**Evidence:**

- Release manifest: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.0/2026-07-30/manifest.json`
- Release notes: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.0/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/manifest.json`
- Package manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/package.json`
- Root exports: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/index.ts`
- Checkout exports: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/index.ts`
- Checkout hook contracts: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/checkout/components/CheckoutContext.tsx`
- Standard provider: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/components/Elements.tsx`
- Shared Element lifecycle: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/files/src/components/createElementComponent.tsx`

## Legacy `@stripe/react-stripe-js@6.3.0` Context (2026-05-08 review)

The pre-collector manual capsule established the React wrapper's standard Elements, Checkout Elements, Embedded Checkout, hooks, shared Element factory, TypeScript props, and representative Payment Element integrations at commit `58e7e27bfc6560db3636791496958e5c6ccda9ee`.

This context remains useful for historical queries, but it is not represented as a package release record or immutable collector snapshot. The `6.8.0` baseline adds to this history and does not erase it.

**Evidence:**

- Legacy capsule pointer: `raw/github-react-stripe-js.md`
- Legacy README: `raw/github-react-stripe-js/README.md`
- Legacy root exports: `raw/github-react-stripe-js/src/index.ts`
- Legacy standard provider: `raw/github-react-stripe-js/src/components/Elements.tsx`
- Legacy Checkout provider: `raw/github-react-stripe-js/src/checkout/components/CheckoutElementsProvider.tsx`
