---
title: "GitHub changelog: stripe/react-stripe-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-09-01
original_format: github-repo
raw_files:
  - "github/stripe/react-stripe-js/snapshots/2026-09-01-c48d651/manifest.json"
  - "github/stripe/react-stripe-js/snapshots/2026-09-01-e814674/manifest.json"
  - "github/stripe/react-stripe-js/snapshots/2026-07-30-a742a10/manifest.json"
  - "github-react-stripe-js.md"
tags: [stripe, react, stripe-js, elements, checkout, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/react-stripe-js`. Cumulative implementation knowledge belongs in [[source-github-react-stripe-js]] and the linked immutable evidence.

## `@stripe/react-stripe-js@6.8.2` - Change Set `c48d651` (2026-08-20)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/react-stripe-js` | `6.8.1` | `6.8.2` | 2026-08-20 | `c48d6515c48da2fa5e2eefc9c8168b95e3026ef2` | Delta |

**Important change:** The Checkout Sessions README example now uses trusted server-side pricing, validates the returned client secret, checks `checkout.canConfirm`, handles loading and error states, prevents duplicate confirmation, and displays Session line items and totals.

**Developer or merchant impact:** The documented client pattern handles both `checkout.confirm()` error results and thrown exceptions, supplies the client secret as a checked fetch promise, and nests Appearance under `elementsOptions`. These are stronger integration examples, not new React Stripe.js APIs.

**Migration action:** New Checkout Elements implementations should adopt the readiness, submission, error, and server-response checks. Existing Payment Intents integrations are not deprecated by the README shortening and do not require migration solely because of `6.8.2`.

**Updated source sections:** evidence boundary; package status; version history; integration guidance; Stripe company; Stripe Checkout concept.

**Evidence boundary:** Only `README.md` and the package version changed from `6.8.1`. No retained runtime source, public export, dependency, or peer-dependency range changed.

**Evidence:**

- Release manifest: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.2/2026-09-01/manifest.json`
- Release notes: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.2/2026-09-01/release-notes.md`
- Snapshot manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-c48d651/manifest.json`
- README: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-c48d651/files/README.md`
- Package manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-c48d651/files/package.json`
- Comparison manifest: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.1--6.8.2/comparison.json`
- Comparison summary: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.1--6.8.2/comparison.md`
- Exact patch: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.1--6.8.2/diff.patch`

## `@stripe/react-stripe-js@6.8.1` - Change Set `e814674` (2026-08-10)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/react-stripe-js` | `6.8.0` | `6.8.1` | 2026-08-10 | `e8146742ffe374ff54301cbdc6fb566e3218a220` | Delta |

**Important change:** The README and demos now emphasize Checkout Sessions with `ui_mode: 'elements'`, `CheckoutElementsProvider`, and `useCheckoutElements()` as the recommended path for most new custom payment forms. The lower-level Payment Intents example remains for existing integrations and finer-grained control.

**Developer or merchant impact:** All retained demos move from JavaScript to typed TSX and receive Storybook stories. Storybook advances to v10 and the repository development environment moves to Node 24. These changes improve the maintained examples and contributor workflow but do not add or remove a public React Stripe.js API.

**Migration action:** New custom checkout implementations should evaluate the Checkout Sessions path first. Existing Payment Intents implementations do not need to migrate solely because of `6.8.1`; continue using that path when its lower-level control justifies the additional code and maintenance.

**Updated source sections:** evidence boundary; package status and compatibility; version history; integration guidance; Stripe company; Stripe Checkout concept.

**Evidence boundary:** Changes across retained `src/` files are formatting-only under the upgraded Prettier configuration. PostCSS, `fast-uri`, Storybook, Prettier, Babel, and Node changes affect repository tooling or development dependencies; the package's public entrypoints, peer ranges, and retained runtime behavior are unchanged.

**Evidence:**

- Release manifest: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.1/2026-09-01/manifest.json`
- Release notes: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.1/2026-09-01/release-notes.md`
- Snapshot manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-e814674/manifest.json`
- README: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-e814674/files/README.md`
- Package manifest: `raw/github/stripe/react-stripe-js/snapshots/2026-09-01-e814674/files/package.json`
- Comparison manifest: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.0--6.8.1/comparison.json`
- Comparison summary: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.0--6.8.1/comparison.md`
- Exact patch: `tracking/github/repos/stripe/react-stripe-js/comparisons/react-stripe-js/6.8.0--6.8.1/diff.patch`

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
