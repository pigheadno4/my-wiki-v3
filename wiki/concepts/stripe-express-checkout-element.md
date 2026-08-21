---
title: "Stripe Express Checkout Element"
type: concept
category: technology
tags: [stripe, elements, express-checkout, apple-pay, google-pay, paypal, link, klarna, amazon-pay, one-click-payments, wallet]
---

## Definition

The Express Checkout Element is a Stripe UI component that renders multiple one-click payment buttons in a single integration. It replaces the older Payment Request Button Element and has six built-in methods: **Link**, **Apple Pay**, **Google Pay**, **PayPal**, **Klarna**, and **Amazon Pay**. The `@stripe/stripe-js@9.14.0` declarations also add a beta embedded Custom Payment Method button surface.

## How It Works

The element mounts to a single DOM node and renders whichever wallet buttons are:
1. Active in the Stripe Dashboard
2. Supported by the customer's browser
3. Denominated in a supported currency
4. Set up by the customer (e.g., Google Pay configured on device)

Stripe automatically sorts buttons by relevance to the customer's location. When the element has determined which wallets are available, it fires a `ready` event with `availablePaymentMethods`.

## Supported Payment Methods

| Method | Notes |
| --- | --- |
| Apple Pay | Requires domain registration; desktop Chromium needs `paymentMethods.applePay: 'always'` |
| Google Pay | Firefox/Safari support requires `paymentMethods.googlePay: 'always'` |
| Link | Stripe's saved-payment network; not supported in Firefox |
| PayPal | Broad browser support; not available on Firefox iOS or Edge iOS |
| Klarna | BNPL option; not supported in Firefox |
| Amazon Pay | Single button type; broad support |

## Browser Support

Firefox does not support Apple Pay, Link, or Klarna. All payment methods have limited or no support in in-app webviews — use the iOS or Android SDK for mobile apps instead.

Full browser support matrix: [[source-stripe-express-checkout-element]].

## Customization

### Button Type (`buttonType`)
Controls the call-to-action text shown alongside each wallet's logo. Key options:
- Apple Pay: `buy`, `checkout`, `subscribe`, `donate`, `order`, `plain`, and 8 more
- Google Pay: `buy`, `checkout`, `pay`, `subscribe`, `donate`, `order`, `plain`
- PayPal: `checkout`, `buynow`, `pay`, `paypal` (logo only)
- Klarna: `continue`, `pay`

### Button Theme (`buttonTheme`)
- Apple Pay: `black`, `white`, `white-outline`
- Google Pay: `black`, `white`
- PayPal: `gold`, `blue`, `silver`, `white`, `black`
- Themes auto-selected from the Appearance API background color when not explicitly set

### Appearance Limits
Logos and brand colors are wallet-controlled and cannot be changed. Customizable: button height (`buttonHeight`), border radius (via Appearance API `variables.borderRadius`), button themes.

### Layout
Default: grid layout, with an overflow menu for low-relevance methods if space is limited. Configurable via `layout` option (max columns, max rows, overflow menu behavior).

## Controlling Which Methods Appear

- **Activate/deactivate**: via Stripe Dashboard
- **Order**: `paymentMethodOrder` option overrides Stripe's relevance-based default
- **Hide**: `paymentMethods.applePay: 'never'` or `paymentMethods.googlePay: 'never'`
- **Force show**: `paymentMethods.applePay: 'always'` or `paymentMethods.googlePay: 'always'` — still blocked on unsupported platforms

> [!info] Regulations in Finland and Sweden require debit payment methods to appear before credit methods.

## Ready Event Pattern

```js
expressCheckoutElement.on("ready", ({ availablePaymentMethods }) => {
  if (!availablePaymentMethods) {
    // No wallets available — show fallback payment UI
    showPaymentElement();
  }
});
```

React: use the `onReady` prop on `<ExpressCheckoutElement>`. Check `availablePaymentMethods` in the callback; if falsy, show a fallback (e.g., `<PaymentElement>`).

## Integration Paths

Two API paths — Checkout Sessions (recommended) and Payment Intents — share the same ECE component but differ in initialization and confirmation.

### Payment Method Type Mappings

`card` enables both Apple Pay and Google Pay automatically. Link requires `link` + `card`.

| Payment Method | type(s) |
| --- | --- |
| Apple Pay | `card` |
| Google Pay | `card` |
| Link | `link`, `card` |
| PayPal | `paypal` |
| Amazon Pay | `amazon_pay` |
| Klarna | `klarna` (Payment Intents only) |

### Checkout Sessions Path (Recommended)

Server: create session with `ui_mode: 'elements'` → client secret.

Client:

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const ece = checkout.createExpressCheckoutElement();
ece.mount('#express-checkout-element');
const { actions } = await checkout.loadActions();
ece.on('confirm', (event) => actions.confirm({ expressCheckoutConfirmEvent: event }));
```

React: `CheckoutElementsProvider` + `useCheckout()` hook + `<ExpressCheckoutElement onConfirm={...} />` from `@stripe/react-stripe-js/checkout`.

### Payment Intents Path

Client:

```js
const elements = stripe.elements({ mode: 'payment', amount: 1099, currency: 'usd' });
const ece = elements.create('expressCheckout');
ece.mount('#express-checkout-element');
ece.on('confirm', async (event) => {
  await stripe.confirmPayment({ elements, confirmParams: { return_url: '...' } });
});
```

React: `<Elements>` provider + `<ExpressCheckoutElement onConfirm={...} />` from `@stripe/react-stripe-js`.

## Customer Detail Collection (Payment Intents Path)

Options passed when creating the ECE:

- `emailRequired: true` — collect email
- `phoneNumberRequired: true` — collect phone
- `billingAddressRequired` — defaults to `true` unless shipping/payer/lineItem options are also passed
- `shippingAddressRequired: true` + `allowedShippingCountries` + `shippingRates[]`

**PayPal caveat**: does not provide billing address (except country) or phone. If these are required and unavailable, the PayPal button is hidden.

> Browsers may anonymize the shipping address (city/state/postal only) until the customer confirms. Full address appears in the `confirm` event.

## Wallet Events

| Event | Trigger | Action Required |
| --- | --- | --- |
| `confirm` | Customer confirms payment | Call `confirmPayment` or `actions.confirm()` |
| `ready` | Available methods determined | Show/hide fallback UI |
| `shippingaddresschange` | Customer selects shipping address | `resolve({lineItems})` or `reject()` |
| `shippingratechange` | Customer selects shipping rate | `resolve({lineItems})` + `elements.update({amount})` |
| `cancel` | Customer dismisses UI | Reset amount: `elements.update({amount: original})` |
| `click` | Customer clicks a button | Request Apple Pay merchant tokens for MIT |

## Custom Payment Methods in v9.14

The `@stripe/stripe-js@9.14.0` type contract allows a `cpmt_` Custom Payment Method to define an `expressCheckout` configuration with `type: 'embedded'`, a required `handleRender(container)` callback, and optional `handleDestroy()` cleanup. The `availablepaymentmethodschange` event can report dynamically keyed custom payment-method IDs alongside the six built-in method keys.

> [!warning] Versioned availability
> Earlier product documentation describes Express Checkout Element as unsupported for Custom Payment Methods. The v9.14 declarations prove a beta typed integration surface, not general runtime rollout or account eligibility. Confirm beta access and live behavior before offering this path to a merchant.

## Apple Pay Merchant Tokens (MIT)

For recurring, deferred, or auto-reload Apple Pay payments, request the relevant merchant token type in the `click` event. Aligns with Apple Pay's latest guidelines.

## Klarna Limitation

`setupFutureUsage` is not supported for Klarna when using the Express Checkout Element.

## Testing

| Method | How |
| --- | --- |
| Link | Any 6-digit OTP succeeds; 000001 = invalid, 000002 = expired, 000003 = max attempts |
| Apple Pay | Use test API keys — Stripe returns test token; live card not charged |
| Google Pay | Use test API keys; also supports Google's own test card suite |
| PayPal | Create sandbox account at developer.paypal.com (sandbox mode only) |
| Amazon Pay | Sandbox test cards: Discover 9424 / Visa 1111 = success; Visa 0701 = 3DS; Amex 0005 / JCB 0000 = decline |

> Google Pay and Apple Pay cannot be tested from Indian IP addresses, even for non-Indian Stripe accounts.

## Connect Integration

- **Checkout Sessions**: pass `Stripe-Account: CONNECTED_ACCOUNT_ID` header on session creation
- **Payment Intents**: pass `stripeAccount` option on the Stripe instance before creating Elements
- Both paths require domain registration for all domains where the ECE appears

## Migrating from Payment Request Button Element

The ECE replaces the older Payment Request Button Element. Key changes:

| Area | Payment Request Button | Express Checkout Element |
| --- | --- | --- |
| Elements init | `stripe.elements()` | `stripe.elements({ mode, amount, currency })` |
| Availability check | `paymentRequest.canMakePayment()` required | Not needed — ECE handles internally |
| Element creation | `stripe.paymentRequest({...})` + `elements.create('paymentRequestButton', ...)` | `elements.create('expressCheckout', {...})` |
| `setup_future_usage` | At confirm time | Moved to Elements instance options |
| Confirmation | `stripe.confirmCardPayment(clientSecret, { payment_method: id })` | `stripe.confirmPayment({ elements, clientSecret, confirmParams })` |
| Styling | `style.paymentRequestButton.type/theme/height` | `buttonType`, `buttonTheme`, `buttonHeight` + Appearance API |
| Apple Pay MPAN | Not supported | Supported — recommended for MIT (recurring/deferred/auto-reload) |

> If migrating from the Charges API, first migrate to Payment Intents before adopting ECE.

Full migration guide: [[source-stripe-express-checkout-element-migration]]

## Integration Notes

- Domain must be registered in Stripe in both test and live mode
- Reuses an existing Elements instance — compatible with Payment Element in the same group
- New payment methods added from Dashboard activate without frontend changes
- Supersedes the Payment Request Button Element — see migration table above
- Must serve over HTTPS in both development and production
- Elements options (captureMethod, setupFutureUsage, paymentMethodOptions) must match PaymentIntent params on confirmation — mismatches cause errors

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-express-checkout-element]] — overview reference: supported methods, browser matrix, customization options, ready event
- [[source-stripe-express-checkout-element-accept-payment]] — full integration guide: both API paths, customer detail collection, wallet events, testing, Connect
- [[source-stripe-express-checkout-element-migration]] — migration guide: Payment Request Button → ECE, before/after code, MPAN support
- [[source-github-stripe-js]] — package-qualified v9.14 beta Custom Payment Method button and dynamic availability-event typing
