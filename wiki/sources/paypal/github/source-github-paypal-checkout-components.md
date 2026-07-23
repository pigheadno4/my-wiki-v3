---
title: "GitHub: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, github-repository, venmo]
---

## Overview

`paypal/paypal-checkout-components` contains the historical browser runtime that rendered PayPal funding buttons and launched the PayPal Checkout experience. This cumulative page begins with the package-qualified `@paypal/checkout-components@4.1.47` baseline at exact SHA `289055a52c55911417d25082681ac626c4c9d160`.

Repository: <https://github.com/paypal/paypal-checkout-components>

## Evidence boundary

- This snapshot proves the implementation shipped in `@paypal/checkout-components@4.1.47`, released on 2019-02-07. It is not current integration guidance.
- The repository owns checkout presentation and funding-button behavior. The separately collected `paypal/paypal-js` repository owns loader, wrapper, and TypeScript package evidence.
- Historical funding eligibility does not prove current product availability, merchant enablement, geographic eligibility, or account configuration.
- In particular, the mobile-only Venmo implementation below predates current PayPal documentation describing both mobile app switch and desktop QR checkout.

## Grounding excerpts

> "A set of components allowing easy integration of PayPal Buttons and PayPal Checkout into your site"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md:6-7`

> "Expected a promise for a string order id to be passed to createOrder"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx:150-169`

> "Do not pass both createOrder and createBillingAgreement"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx:193-205`

> "eligibleFunding = eligibleFunding.slice(0, 2)"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js:38-50`

## Repository responsibility and architecture

The README identifies this repository as the implementation of PayPal Buttons and PayPal Checkout, powered by Zoid. The v4 runtime defines separate `paypal-buttons` and `paypal-checkout` components. Buttons collect merchant callbacks and funding configuration; Checkout manages the buyer-facing PayPal window.

Checkout prefers a pop-up when the browser supports one and falls back to an iframe. The public interface always exports `Buttons`, but it exposes the lower-level `Checkout`, `PopupOpenError`, and `allowIframe` members only when executing on a PayPal domain.

## Merchant callback contract

The decorated `createOrder` callback receives an `actions.order.create()` helper and must resolve to a nonempty string order ID. The component rejects a missing or non-string result before checkout continues.

`createOrder` and `createBillingAgreement` are mutually exclusive. The billing-agreement path also requires the SDK to be loaded with `vault=true`. These are historical client-runtime guards; merchants still need matching server-side order or billing-agreement handling.

The v4 source contains a USD 0.01 fallback order when no merchant callback is supplied. That fallback is implementation behavior, not a production integration recommendation. Merchant integrations should create and validate their own order on the server.

For approval handling, the historical default captures automatically only when the intent is `CAPTURE` and `commit` is true. Other flows require the merchant's `onApprove` implementation.

## Funding eligibility and presentation

Funding sources pass through several gates before rendering:

1. The server-provided funding record must exist, be eligible, and not set `branded` to false.
2. The source must support the selected button layout and detected platform.
3. A remembered-only source must appear in the buyer's remembered funding list.
4. Eligible sources are ordered by the repository's funding priority.

Horizontal layouts retain at most two eligible funding sources. The historical priority starts with PayPal, Venmo, and Credit, followed by local methods and cards. Most alternative payment methods are constrained to vertical layouts and cannot be the primary button.

## Historical Venmo behavior

In `4.1.47`, the Venmo funding configuration:

- supports only the mobile platform;
- uses the shared PayPal Checkout URL;
- supports blue and silver button colors; and
- sets `allowPrimary: false`, making Venmo a secondary funding choice.

This is a version-qualified implementation fact. It must not be used to deny current desktop Venmo QR support, which was added in later product/runtime generations.

## Public and security boundary

The browser-facing `Buttons` component is public on merchant pages. Lower-level checkout controls remain PayPal-domain-only. The iframe helper is therefore not a merchant escape hatch for forcing an unsupported presentation mode.

The exact snapshot also shows that layout, platform, remembered funding, and server eligibility jointly determine button visibility. A configured funding source is not proof that its button will render for a particular buyer.

## Related

- [[changelog-github-paypal-checkout-components]] — package-qualified release ledger
- [[source-github-paypal-js]] — independent loader, wrapper, and TypeScript package history
- [[paypal-checkout]] — cumulative PayPal Checkout concept
- [[source-paypal-pay-with-venmo]] — current product documentation for mobile app switch and desktop QR

## Raw sources

- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json`
- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/4.1.47/2026-07-23/manifest.json`
- README: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx`
- Funding eligibility: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js`
- Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/venmo/config.jsx`
- Public button interface: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/interface/button.js`
