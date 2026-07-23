---
title: "GitHub: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, github-repository, venmo]
---

## Overview

`paypal/paypal-checkout-components` contains the browser runtime that renders PayPal funding buttons and launches PayPal checkout experiences. This cumulative page preserves the package-qualified `@paypal/checkout-components@4.1.47` baseline and extends the history through `@paypal/checkout-components@5.0.425` at exact SHA `e03bffc45b7a3c7f36346a514f34ebbd168dd403`.

Repository: <https://github.com/paypal/paypal-checkout-components>

## Evidence boundary

- The v4 snapshot proves the implementation shipped in `@paypal/checkout-components@4.1.47`, released on 2019-02-07. The v5 snapshot proves the source retained at `5.0.425`, released on 2026-07-22. Neither is a substitute for current integration guidance.
- The repository owns checkout presentation and funding-button behavior. The separately collected `paypal/paypal-js` repository owns loader, wrapper, and TypeScript package evidence.
- Historical funding eligibility does not prove current product availability, merchant enablement, geographic eligibility, or account configuration.
- The exact `5.0.425` patch forwards browser back-forward-cache events via post-robot. Broader capability statements below describe the accumulated v5 source, not features introduced by that one patch.

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

> "Pass bfcache events via post-robot"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/CHANGELOG.md:1-3`

> "flows: [BUTTON_FLOW.PURCHASE, BUTTON_FLOW.VAULT_WITHOUT_PURCHASE]"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/funding/venmo/config.jsx:27`

> "export const SavedPaymentMethods"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/interface/saved-payment-methods.js:9-11`

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

## Version 5 accumulated architecture

The `5.0.425` source retains the public `Buttons` interface and adds distinct interfaces for Marks, Card Fields, Payment Fields, Hosted Buttons, Wallet, and Saved Payment Methods. Lower-level Checkout, Venmo, QR Code, and other Zoid components remain protected exports in the button interface. This demonstrates a broader runtime architecture than v4, but each integration still depends on the matching JS SDK loader and product eligibility.

The v5 Venmo funding configuration allows purchase and vault-without-purchase flows. Vault-without-purchase is gated by the `venmoVaultWithoutPurchase` experiment, and shipping callbacks are rejected when the display-only state is vaultable because native app-switch and QR flows do not support that combination. Mobile Venmo requires both native and popup capabilities; the accumulated changelog records later desktop handling and QR component work that superseded v4's mobile-only presentation.

The separate Venmo Zoid component accepts order creation or vault setup-token creation and distinguishes desktop-web from mobile-web channels. The Saved Payment Methods component carries order callbacks, app-switch preferences, shipping callbacks, funding eligibility, customer identity, and style validation. These are implementation contracts, not proof that a merchant account is enabled for every flow.

The exact `5.0.425` release entry is narrowly about forwarding bfcache events through post-robot. The major-version comparison is used as a full historical baseline because the change from `4.1.47` to `5.0.425` spans the accumulated v5 component system.

## Public and security boundary

The browser-facing `Buttons` component is public on merchant pages. Lower-level checkout controls remain PayPal-domain-only. The iframe helper is therefore not a merchant escape hatch for forcing an unsupported presentation mode.

The exact snapshot also shows that layout, platform, remembered funding, and server eligibility jointly determine button visibility. A configured funding source is not proof that its button will render for a particular buyer.

## Related

- [[changelog-github-paypal-checkout-components]] — package-qualified release ledger
- [[source-github-paypal-js]] — independent loader, wrapper, and TypeScript package history
- [[paypal-checkout]] — cumulative PayPal Checkout concept
- [[paypal-vault]] — setup-token and stored-payment-method concepts
- [[paypal-expanded-checkout]] — Card Fields and 3DS concepts
- [[source-paypal-pay-with-venmo]] — current product documentation for mobile app switch and desktop QR

## Raw sources

- Snapshot manifest (`5.0.425`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json`
- Release manifest (`5.0.425`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.425/2026-07-23/manifest.json`
- Major comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/4.1.47--5.0.425/comparison.json`
- Release history: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/CHANGELOG.md`
- v5 public interfaces: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/interface/`
- v5 Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/funding/venmo/config.jsx`
- v5 Venmo component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/zoid/venmo/component.jsx`
- v5 Saved Payment Methods component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/zoid/saved-payment-methods/component.jsx`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json`
- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/4.1.47/2026-07-23/manifest.json`
- README: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx`
- Funding eligibility: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js`
- Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/venmo/config.jsx`
- Public button interface: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/interface/button.js`
