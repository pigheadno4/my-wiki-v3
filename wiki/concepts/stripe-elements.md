---
title: "Stripe Elements"
type: concept
category: technology
tags: [stripe, elements, payment-element, express-checkout, link, address-element, stripe-js, ui-components, appearance-api]
---

## Stripe Elements

Stripe's prebuilt UI component library for building custom checkout flows. Built on top of Stripe.js — tokenizes sensitive payment details within each Element without ever hitting your server. Works with both Checkout Sessions API and Payment Intents API.

## The 7 Elements

| Element | Purpose | API compatibility |
| --- | --- | --- |
| **Payment Element** | Accept 100+ payment methods including cards | Both APIs |
| **Express Checkout Element** | One-click wallet buttons: Link, Apple Pay, Google Pay, PayPal, Klarna, Amazon Pay | Both APIs |
| **Link Authentication Element** | Single email field for email collection + Link auth; autofills saved payment/shipping for returning users — see [[stripe-link-authentication-element]] | Both APIs |
| **Address Element** | Collect billing/shipping + display Link saved addresses; 236 regional formats, autocomplete (26 countries) — see [[stripe-address-element]] | Both APIs |
| **Payment Method Messaging Element** | Show BNPL options (Affirm/Afterpay/Klarna); no clientSecret needed; works on product/cart/payment pages — see [[stripe-payment-method-messaging-element]] | Both APIs |
| **Currency Selector Element** | Local currency choice with Adaptive Pricing; legally required when using Adaptive Pricing — see [[stripe-currency-selector-element]] | Checkout Sessions only |
| **Tax ID Element** | Collect business tax IDs for invoices/VAT refunds; 100+ countries, auto/always visibility, beta — see [[stripe-tax-id-element]] | Both APIs |

## Compatible APIs

Elements works with two Stripe payment APIs:

| | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Recommendation | ✓ **Recommended for most** | Only for deep custom flows |
| Customer | Built-in | Build yourself |
| Shipping | Built-in | Build yourself |
| Taxes | Built-in (`automatic_tax`) | Build yourself (Tax API) |
| Discounts/coupons | Built-in | Build yourself |
| Payment | Built-in | Core feature |
| Adaptive Pricing | ✓ Available | ✗ Not available |
| Effort | Low coding | Most coding |

> **Mental model** (from Stripe diagram): Checkout Sessions API has 5 branches (Customer → Shipping → Taxes → Discounts → Payment). Payment Intents API has 1 branch (Payment only, dashed line).

## Key Features

- **100+ payment methods**: cards, wallets (Apple Pay, Google Pay), bank transfers, BNPL, and more
- **Link**: auto-fills returning customers' payment and shipping details
- **Saved payment methods**: built-in save/reuse/manage flow
- **Compliance**: globally compliant; Stripe handles mandates and consent notices automatically
- **Localization**: forms auto-localize; Stripe maintains each payment method's requirements
- **Appearance API**: full CSS-level customization (colors, fonts, border radius, etc.)
- **Address collection**: full or partial billing/shipping addresses with any payment method
- **CVC recollection + card brand control**: additional security features

## React Integration Patterns

### With Checkout Sessions API (Recommended)

```jsx
// Package: @stripe/react-stripe-js/checkout
import { CheckoutElementsProvider, PaymentElement, useCheckoutElements } from "@stripe/react-stripe-js/checkout";
// confirm: checkoutState.checkout.confirm()
```

### With Payment Intents API

```jsx
// Package: @stripe/react-stripe-js
import { Elements, PaymentElement, useStripe, useElements } from "@stripe/react-stripe-js";
// confirm: stripe.confirmPayment({ elements, confirmParams: { return_url } })
```

## Stripe.js Loader Boundary

The `@stripe/stripe-js` npm package is a loader and TypeScript declaration package, not a bundled copy of the Stripe.js runtime. The retained history now covers `@stripe/stripe-js@8.11.0`, the full transition to `@stripe/stripe-js@9.12.1`, and approved deltas through `9.15.0`:

- Stripe.js must load from `https://js.stripe.com`; the runtime cannot be bundled or self-hosted.
- The v8 package targets `clover`; v9 targets `dahlia`. Package versions pin declaration trains but do not prove runtime feature availability.
- Importing `@stripe/stripe-js` schedules script loading as a side effect. Importing `@stripe/stripe-js/pure` defers loading until `loadStripe()` is called.
- `loadStripe()` resolves to `null` in a server environment, caches a browser load attempt, and clears the cached promise after a load failure so a later call can retry.
- Only the pure entrypoint exposes `loadStripe.setLoadParameters({advancedFraudSignals})`, and parameters cannot change after the first `loadStripe()` call.
- In v9, `elements.update()` returns `Promise<void>`. Contact Details and beta Terms Element entrypoints are added, Payment Element can emit `availablepaymentmethodschange`, and Tax ID Element can expose verification status.
- In v9.13.0, `paymentElement.update()` is limited to `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `layout`, and `applePay`. The `wallets` creation option is excluded from the typed update surface, so wallet visibility must be set when creating the Element.
- In v9.14.0, `walletOptions` can require wallet-provided email and phone values at Payment Element creation and can be changed through `paymentElement.update()`. This is separate from the creation-only `wallets` visibility option.
- In v9.15.0, the Elements `Appearance.variables` contract adds `buttonBoxShadow?: string`. This establishes a typed styling variable, not independent proof that every Stripe-hosted runtime or account already supports it.

See [[source-github-stripe-js]] for package-qualified v8 and v9 implementation evidence.

## Card Element (Legacy)

> **Card Element is legacy** — maintenance only, no new features. Stripe strongly recommends migrating to Payment Element. Same integration effort; adds wallets, bank debits, BNPL, 100+ local PMs. See [[source-stripe-payment-element-vs-card-element]] for full comparison.

## HTML Vanilla Confirm Pattern (Checkout Sessions)

For non-React integrations with `ui_mode: 'elements'`:

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret: promise });
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");

// Confirm payment:
const loadActionsResult = await checkout.loadActions();
const actions = loadActionsResult.actions;
const error = await actions.confirm();
```

## Best Practices Highlights

- **Accordion layout** recommended when 4+ payment methods
- **Address Element billing mode**: hides billing fields within Payment Element — prevents duplicate entry
- **No iframe nesting**: Payment Element is already an iframe; nesting breaks redirect-based methods
- **Dynamic payment methods** → enables **payment method rules** (custom criteria)
- Always send **metadata** for Dashboard searchability

## Payment Element — Details

- **Layout**: `layout.type: 'tabs'` or `'accordion'`; accordion can show/hide radio buttons
- **Appearance API**: themes (`stripe`, `night`, `flat`, `none`) + CSS variables; `@stripe/stripe-js@9.15.0` adds the typed `buttonBoxShadow` variable
- **Creation options**: `layout`, `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `wallets`, `walletOptions`, and `applePay` in the retained v9.14 contract
- **Post-creation update boundary in `@stripe/stripe-js@9.14.0`**: `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `layout`, `applePay`, and `walletOptions` are accepted by the typed `update()` call; `wallets` remains creation-only
- **Combining**: Link Authentication (contact/autofill) + Address (shipping) + Payment Element work together; when combined with Express Checkout, wallets only appear in Express Checkout
- **Link legal agreement**: cannot be removed (compliance requirement)
- **17 auto-handled error codes**: card_declined, insufficient_funds, expired_card, etc.

## React Stripe.js API

**Install**: `npm install --save @stripe/react-stripe-js @stripe/stripe-js`

**Two integration paths**:

### Checkout Sessions path (from `@stripe/react-stripe-js/checkout`)

- `CheckoutElementsProvider` → wraps app; `clientSecret` from Checkout Session; `stripe` prop immutable
- `useCheckoutElements()` → returns `{ type: 'loading'|'error'|'success', checkout }` object; `checkout.confirm()` submits
- `useCheckout()` has been deprecated since v6.3.0 and is scheduled for removal in v7; use the provider-specific hook
- `CheckoutFormProvider` + `useCheckoutForm()` expose the narrower beta Checkout Form SDK, while `CheckoutElementsProvider` + `useCheckoutElements()` expose the Elements SDK
- Checkout exports include Billing Address, Shipping Address, Currency Selector, Payment, Express Checkout, Tax ID, Contact Details, Checkout Form, and beta-gated Terms components

### Advanced path (from `@stripe/react-stripe-js`)

- `<Elements stripe={stripePromise} options={{ clientSecret }}>` → wraps app; `clientSecret` and `fonts` are immutable, while other changed options are forwarded to `elements.update()`
- `useStripe()` → Stripe object (null until Promise resolves)
- `useElements()` → Elements object; `elements.getElement(PaymentElement)` for imperative focus
- `ElementsConsumer` → for class components; render props pattern `({ stripe, elements }) => ...`
- Root exports include Address, Express Checkout, Link Authentication, Payment, Payment Method Messaging, Tax ID, five Issuing display/copy components, and beta-gated Terms components

### Retained React package baseline

The cumulative repository baseline is `@stripe/react-stripe-js@6.8.0` at exact commit `a742a10`. It requires React and React DOM `>=16.8.0 <20.0.0` and `@stripe/stripe-js >=9.5.0 <10.0.0`. The root and `/checkout` entrypoints publish separate CommonJS, ESM, and declaration targets.

Provider behavior is intentionally strict:

- the `stripe` prop can start as `null` for server rendering, but cannot be replaced after initialization;
- standard `Elements` treats `clientSecret` and `fonts` as immutable while forwarding other changed options through `elements.update()`;
- Checkout providers initialize their SDK once, publish loading/success/error state, and apply later appearance or font changes through the SDK;
- an app cannot nest standard `Elements` and a Checkout provider around the same consumer; and
- Element wrappers attach and detach event callbacks, mount once, and destroy the underlying Element during cleanup.

The v6.8.0 release note adds `TermsElement`. Both the root and `/checkout` implementations explicitly require beta access, so the export proves a typed integration surface, not account eligibility or general availability. See [[source-github-react-stripe-js]] and [[changelog-github-react-stripe-js]].

**PCI compliance**: always load Stripe.js from js.stripe.com — never bundle or self-host.

## Sources

- [[source-stripe-web-elements-overview]] — Elements overview: 7 elements, API comparison table + diagram, features
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart (Checkout Sessions + Elements)
- [[source-stripe-payment-intents-quickstart]] — Payment Intents quickstart (Payment Intents + Elements)
- [[source-stripe-react-stripejs]] — React Stripe.js reference: CheckoutElementsProvider, useCheckoutElements, Elements provider, useStripe/useElements, ElementsConsumer
- [[source-github-react-stripe-js]] — cumulative React Stripe.js repository history: legacy v6.3.0 context plus package-qualified `@stripe/react-stripe-js@6.8.0`
- [[changelog-github-react-stripe-js]] — package-qualified React Stripe.js release ledger
- [[source-github-stripe-js]] — package-qualified `@stripe/stripe-js@8.11.0` through `9.15.0` loader, runtime boundary, public type surface, and Elements history
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents feature matrix
- [[source-stripe-payment-element]] — Payment Element reference: layout, Appearance API, 8 options, combining elements, 17 error codes
- [[source-stripe-payment-element-best-practices]] — Best practices: LLM instruction, HTML confirm pattern, 7-item checklist, 5-item features checklist
- [[source-stripe-payment-element-vs-card-element]] — Payment Element vs Card Element: 7 comparison tables, Card Element is legacy, migration guide
- [[source-stripe-payment-element-migration]] — Migration guide: CardElement → PaymentElement (PaymentIntent + SetupIntent paths), 11 Elements options, elements.submit() pattern
- [[source-stripe-payment-element-migration-ewcs]] — Migration to Checkout Sessions (recommended): one-time + future payment paths, email collection, save PM, 12 session options
