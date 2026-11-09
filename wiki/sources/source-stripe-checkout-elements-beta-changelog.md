---
title: "Elements with Checkout Sessions API Beta Changelog"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/checkout/elements-with-checkout-sessions-api/changelog"
raw_files:
  - "stripe-checkout-elements-with-checkout-sessions-api-changelog-2026-11-07.md"
  - "stripe-checkout-elements-beta-changelog-2025.md"
tags: [stripe, checkout-sessions, elements, migration, clover, basil, beta-changelog, breaking-changes]
---

## Overview

Dated migration history for the Elements with Checkout Sessions API beta, covering `custom_checkout_beta_*` through Basil and Clover. The November 7, 2026 capture explicitly says this changelog does not apply to integrations on Clover or later and directs those readers to the general Stripe changelog. The April 22 capture excluded Clover alone. This page remains useful for the beta-to-Basil-to-Clover path, not as a current integration guide for Clover or later. See [[stripe-checkout]] and [[stripe-elements]].

> [!warning] Contradiction
> The April source summary called Clover “latest.” That label was relative to its historical capture. The retained `@stripe/stripe-js@9.12.1` source targets `dahlia`, removes `initCheckout()`, and uses `initCheckoutElementsSdk()` for the Elements path. Keep this page as version-scoped Clover migration evidence; use [[source-github-stripe-js]] and [[changelog-github-stripe-js]] for package-qualified later behavior. The November changelog's illustrative pre-Basil API header changes from `2026-03-25.dahlia; custom_checkout_beta=v1` to `2026-10-28.endive; custom_checkout_beta=v1`; neither sample proves a supported Endive beta path or current runtime compatibility.

## Clover migration history — key breaking changes

For the documented migration, first update to Basil, then use `@stripe/stripe-js >= 8.0.0`, `@stripe/react-stripe-js >= 5.0.0`, and backend API version at least `2025-09-30.clover`. Script-tag integrations are directed to the versioned `clover` Stripe.js URL. These are migration requirements in this beta history, not a universal package recommendation.

- `stripe.initCheckout` becomes synchronous. Remove its `await`/`.then()`; pass a client-secret string or Promise instead of `fetchClientSecret`. Call asynchronous `checkout.loadActions()` once to get actions including `getSession()` or `confirm()`, and check its resolved `type` for errors.
- React imports move to `@stripe/react-stripe-js/checkout`; `useCheckout()` returns a loading/success/error disjoint union rather than throwing; `CheckoutProvider` renders children before initialization succeeds and uses `clientSecret` in place of `fetchClientSecret`.
- Saved payment methods configured on the Checkout Session become enabled in Payment Element without extra client configuration. Postal codes stop being automatically collected for card payments in Canada, the UK, and Puerto Rico.

The captured Clover HTML/JS example demonstrates `const checkout = stripe.initCheckout({ clientSecret })` followed by `await checkout.loadActions()`; it is version-scoped example code, not evidence that the same entrypoint exists in later package declarations.

## Basil migration history

The guide says to update to `custom_checkout_beta_6` before Basil. It specifies `@stripe/stripe-js >= 7.0.0`, `@stripe/react-stripe-js >= 3.6.0`, and backend API version at least `2025-03-31.basil`, with beta headers removed. For script-tag integrations still on `v3` or `acacia`, it directs a versioned `basil` Stripe.js URL.

- Async methods such as `confirm` and `applyPromotionCode` return successful updated session state under `session`, not the earlier beta `success` key.
- `confirm({ returnUrl })` throws when the Checkout Session already has `return_url`; successful redirect URLs contain only the supplied return URL parameters.
- In subscription-mode Sessions, `checkout_session.invoice` and `.subscription` stay null until Checkout Session completion because the subscription is created after the user completes payment. For code relying on deprecated `payment_intent.invoice`, the changelog recommends the `checkout_session.completed` webhook and `checkout_session.invoice` or Invoice Payment list to find the invoice.
- `discountAmounts.percentOff` is added for display.

The April capture's illustrative “Before” backend header is `2026-03-25.dahlia; custom_checkout_beta=v1`; the November capture uses `2026-10-28.endive; custom_checkout_beta=v1`. Both show `2025-03-31.basil` in “After.” This sample change is not a new required upgrade step or proof of Endive beta compatibility.

## Beta version history

The changelog distinguishes a Stripe.js front-end beta header (for example, `custom_checkout_beta_6`) from an API-version back-end beta header (for example, `custom_checkout_beta=v1`).

### `custom_checkout_beta_6`

The dated beta_6 section specifies `@stripe/stripe-js >= 6.1.0` and `@stripe/react-stripe-js >= 3.5.0`. It flips the sign convention of `total.appliedBalance`, replaces a static `clientSecret` with async `fetchClientSecret`, renames HTML/JS element create/get methods, revises `canConfirm` and removes `confirmationRequirements`, makes `updateEmail` throw if `customer_email` was set at Session creation, requires an absolute `returnUrl`, and nests pricing values under formatted `amount` and integer `minorUnitsAmount`. The price display rule and full method mapping are in the raw beta_6 section.

| Earlier HTML/JS method | beta_6 name |
| --- | --- |
| `createElement('payment')` | `createPaymentElement()` |
| `createElement('address', {mode: 'billing'})` | `createBillingAddressElement()` |
| `createElement('address', {mode: 'shipping'})` | `createShippingAddressElement()` |
| `createElement('expressCheckout')` | `createExpressCheckoutElement()` |
| `getElement(...)` | `getPaymentElement()` / `getBillingAddressElement()` / corresponding address and Express Checkout getters |

### `custom_checkout_beta_5` and earlier

Beta_5 renames `initCustomCheckout` to `initCheckout`, `CustomCheckoutProvider` to `CheckoutProvider`, and `useCustomCheckout` to `useCheckout`; it changes Express Checkout confirmation to `confirm({ expressCheckoutConfirmEvent })`, standardizes error handling, and adds a success/error discriminator to async results. For beta_5, success is under `success`; Basil later moves it to `session`. Beta_4 through beta_1 changes and the unchanged back-end beta-version note remain in the raw locator.

## Detail locators

- [[raw/stripe-checkout-elements-with-checkout-sessions-api-changelog-2026-11-07|November 7, 2026 changelog]]: scope lines 5–11; Clover lines 13–121; Basil lines 123–198; beta_6 lines 200–239; beta_5 and earlier lines 241–300.
- [[raw/stripe-checkout-elements-beta-changelog-2025|April 22, 2026 changelog]]: former Clover exclusion lines 8–10; corresponding migration and beta history lines 12–290; former “Before” API header line 172.

## Related

- [[stripe]]; [[stripe-checkout]]; [[stripe-elements]]; [[source-stripe-checkout-elements-quickstart]]

## Raw Sources

- [[raw/stripe-checkout-elements-with-checkout-sessions-api-changelog-2026-11-07|November 7, 2026 beta changelog capture]]
- [[raw/stripe-checkout-elements-beta-changelog-2025|April 22, 2026 beta changelog capture]]
