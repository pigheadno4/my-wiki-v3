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
import { CheckoutElementsProvider, PaymentElement, useCheckout } from "@stripe/react-stripe-js/checkout";
// confirm: checkout.confirm()
```

### With Payment Intents API

```jsx
// Package: @stripe/react-stripe-js
import { Elements, PaymentElement, useStripe, useElements } from "@stripe/react-stripe-js";
// confirm: stripe.confirmPayment({ elements, confirmParams: { return_url } })
```

## Stripe.js Loader Boundary

The `@stripe/stripe-js` npm package is a loader and TypeScript declaration package, not a bundled copy of the Stripe.js runtime. The retained history now covers `@stripe/stripe-js@8.11.0` and the full transition to `@stripe/stripe-js@9.12.1`:

- Stripe.js must load from `https://js.stripe.com`; the runtime cannot be bundled or self-hosted.
- The v8 package targets `clover`; v9 targets `dahlia`. Package versions pin declaration trains but do not prove runtime feature availability.
- Importing `@stripe/stripe-js` schedules script loading as a side effect. Importing `@stripe/stripe-js/pure` defers loading until `loadStripe()` is called.
- `loadStripe()` resolves to `null` in a server environment, caches a browser load attempt, and clears the cached promise after a load failure so a later call can retry.
- Only the pure entrypoint exposes `loadStripe.setLoadParameters({advancedFraudSignals})`, and parameters cannot change after the first `loadStripe()` call.
- In v9, `elements.update()` returns `Promise<void>`. Contact Details and beta Terms Element entrypoints are added, Payment Element can emit `availablepaymentmethodschange`, and Tax ID Element can expose verification status.

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
- **Appearance API**: themes (`stripe`, `night`, `flat`, `none`) + CSS variables
- **8 options**: `layout`, `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `wallets`
- **Combining**: Link Authentication (contact/autofill) + Address (shipping) + Payment Element work together; when combined with Express Checkout, wallets only appear in Express Checkout
- **Link legal agreement**: cannot be removed (compliance requirement)
- **17 auto-handled error codes**: card_declined, insufficient_funds, expired_card, etc.

## React Stripe.js API

**Install**: `npm install --save @stripe/react-stripe-js @stripe/stripe-js`

**Two integration paths**:

### Checkout Sessions path (from `@stripe/react-stripe-js/checkout`)

- `CheckoutElementsProvider` → wraps app; `clientSecret` from Checkout Session; `stripe` prop immutable
- `useCheckoutElements()` → returns `{ type: 'loading'|'error'|'success', checkout }` object; `checkout.confirm()` submits
- Note: `useCheckoutElements` replaces old `useCheckout` (pre-v6)
- Elements: BillingAddressElement, CurrencySelectorElement, ExpressCheckoutElement, PaymentElement, PaymentMethodMessagingElement, ShippingAddressElement, TaxIdElement

### Advanced path (from `@stripe/react-stripe-js`)

- `<Elements stripe={stripePromise} options={{ clientSecret }}>` → wraps app; `options` immutable (use `elements.update()` for appearance)
- `useStripe()` → Stripe object (null until Promise resolves)
- `useElements()` → Elements object; `elements.getElement(PaymentElement)` for imperative focus
- `ElementsConsumer` → for class components; render props pattern `({ stripe, elements }) => ...`
- Elements: AddressElement, ExpressCheckoutElement, LinkAuthenticationElement, PaymentElement, PaymentMethodMessagingElement, TaxIdElement

**PCI compliance**: always load Stripe.js from js.stripe.com — never bundle or self-host.

## Sources

- [[source-stripe-web-elements-overview]] — Elements overview: 7 elements, API comparison table + diagram, features
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart (Checkout Sessions + Elements)
- [[source-stripe-payment-intents-quickstart]] — Payment Intents quickstart (Payment Intents + Elements)
- [[source-stripe-react-stripejs]] — React Stripe.js reference: CheckoutElementsProvider, useCheckoutElements, Elements provider, useStripe/useElements, ElementsConsumer
- [[source-github-react-stripe-js]] — react-stripe-js repo v6.3.0: Elements.tsx, createElementComponent factory, EmbeddedCheckoutProvider, CheckoutElementsProvider impl, examples
- [[source-github-stripe-js]] — package-qualified `@stripe/stripe-js@8.11.0` and `9.12.1` loader, runtime boundary, public type surface, and Elements history
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents feature matrix
- [[source-stripe-payment-element]] — Payment Element reference: layout, Appearance API, 8 options, combining elements, 17 error codes
- [[source-stripe-payment-element-best-practices]] — Best practices: LLM instruction, HTML confirm pattern, 7-item checklist, 5-item features checklist
- [[source-stripe-payment-element-vs-card-element]] — Payment Element vs Card Element: 7 comparison tables, Card Element is legacy, migration guide
- [[source-stripe-payment-element-migration]] — Migration guide: CardElement → PaymentElement (PaymentIntent + SetupIntent paths), 11 Elements options, elements.submit() pattern
- [[source-stripe-payment-element-migration-ewcs]] — Migration to Checkout Sessions (recommended): one-time + future payment paths, email collection, save PM, 12 session options
