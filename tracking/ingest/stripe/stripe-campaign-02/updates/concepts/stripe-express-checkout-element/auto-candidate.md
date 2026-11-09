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

Stripe sorts eligible buttons by relevance to the customer's location. The November 2026 overview uses `availablepaymentmethodschange` with `paymentMethods` to check availability in the customer's current environment; its React prop is `onAvailablePaymentMethodsChange`. The April 2026 overview used `ready` with `availablePaymentMethods` for this check. The captures do not establish removal of `ready` for every purpose or actual payment completion.

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

The November browser table lists Firefox desktop Apple Pay with the non-Safari desktop `paymentMethods.applePay: 'always'` condition, while Firefox still lacks Link and Klarna. The April table marked Firefox Apple Pay unsupported and its desktop Chromium footnote said macOS-only; November omits that OS restriction without proving support on every desktop OS. In eligible iOS webviews Apple Pay can work; Google Pay can work without a popup, and Android webviews additionally need host Payment Request API support. Link, PayPal, Klarna, and Amazon Pay are marked unsupported in webviews. All browser, currency, setup, and device gates still apply; consider native iOS/Android SDKs for mobile apps.

Full browser support matrix: [[source-stripe-express-checkout-element]].

## Customization

### Button Type (`buttonType`)
Controls the call-to-action text shown alongside each wallet's logo. Key options:
- Apple Pay: `buy`, `check-out`, `subscribe`, `donate`, `order`, `plain`, and 8 more
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
- **Allow when wallet is not set up**: `paymentMethods.applePay: 'always'` or `paymentMethods.googlePay: 'always'` can allow the button to appear, subject to merchant/account and current-device eligibility. It cannot force display on an unsupported platform or for an unsupported currency.

> [!info] Regulations in Finland and Sweden require debit payment methods to appear before credit methods.

## Availability Event Pattern

The November overview uses the event below to check the methods currently available for the Element to display and to choose a fallback UI when none are available:

```js
expressCheckoutElement.on("availablepaymentmethodschange", ({ paymentMethods }) => {
  if (!paymentMethods) showPaymentElement();
});
```

React uses `onAvailablePaymentMethodsChange={({ paymentMethods }) => ...}` on `<ExpressCheckoutElement>`. The April overview used `ready`/`availablePaymentMethods` and React `onReady` for this availability example; that is dated historical guidance, not proof that `ready` itself was removed. An availability callback does not prove merchant eligibility or payment completion.

## Integration Paths

The 2026-04-21 [[source-stripe-express-checkout-element-accept-payment]] guide documents Checkout Sessions and Payment Intents paths with different initialization and confirmation. Its Payment Intents path recommends collecting details before creating an Intent; neither that guide nor the 2026-11-07 base-URL index ranks Checkout Sessions over Payment Intents.

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

### Checkout Sessions Path (2026-04-21 guide)

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
  const { error: submitError } = await elements.submit();
  if (submitError) return handleError(submitError);
  const response = await fetch('/create-intent', { method: 'POST' });
  const { client_secret: clientSecret } = await response.json();
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: { return_url: '...' },
  });
  if (error) handleError(error);
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
| `availablepaymentmethodschange` (November overview) | `paymentMethods` reports methods available to display | Show/hide fallback UI; April overview used `ready`/`availablePaymentMethods` for this check |
| `shippingaddresschange` | Customer selects shipping address | `resolve({lineItems})` or `reject()` |
| `shippingratechange` | Customer selects shipping rate | `resolve({lineItems})` + `elements.update({amount})` |
| `cancel` | Customer dismisses UI | Reset amount: `elements.update({amount: original})` |
| `click` | Customer clicks a button | Request Apple Pay merchant tokens for MIT |

## Custom Payment Methods in v9.14

The `@stripe/stripe-js@9.14.0` type contract allows a `cpmt_` Custom Payment Method to define an `expressCheckout` configuration with `type: 'embedded'`, a required `handleRender(container)` callback, and optional `handleDestroy()` cleanup. The `availablepaymentmethodschange` event can report dynamically keyed custom payment-method IDs alongside the six built-in method keys.

> [!warning] Versioned availability
> The April 2026 product overview said methods could not be specified, while the November 2026 overview describes `customPaymentMethods` buttons on `stripe.elements()` with valid Dashboard `cpmt_` IDs and a working `handleRender`. The separately captured v9.14 declarations prove a beta typed surface. These snapshots do not prove general runtime rollout, account eligibility, or successful rendering; confirm access and live behavior before offering this path.

## Apple Pay Merchant Tokens (MIT)

For recurring, deferred, or auto-reload Apple Pay payments, request the relevant merchant token type in the `click` event. Aligns with Apple Pay's latest guidelines.

## Klarna Limitation

`setupFutureUsage` is not supported for Klarna when using the Express Checkout Element.

## Testing

| Method | How |
| --- | --- |
| Link | In the 2026-04-21 guide's sandbox, any other 6-digit OTP succeeds; 000001 = invalid, 000002 = expired, 000003 = max attempts |
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

Payment Request Button → ECE migration: [[source-stripe-express-checkout-element-migration]] preserves the Payment Intents steps captured on 2026-04-21 and identifies the Checkout Sessions and Payment Intents variant routes in Stripe's 2026-11-07 index. The index does not establish either variant's current implementation details.

### React wrapper boundary at 7.0.0

`@stripe/react-stripe-js@7.0.0` removes the root `PaymentRequestButtonElement` export, its React props/component types, the React `getElement` overload, and the class/hooks demo and Storybook pairs. `ExpressCheckoutElement` remains exported. Existing v6 code importing the removed wrapper must migrate before adopting v7; this is not a drop-in name change because initialization, availability, event and confirmation contracts differ as described above. It does not prove removal of all lower-level Payment Request APIs or a new wallet rollout. The v7 wrapper requires `@stripe/stripe-js >=10.0.0 <11.0.0`; underlying declaration/runtime behavior has its own evidence boundary. See [[source-github-react-stripe-js]] and [[changelog-github-react-stripe-js]].

## Integration Notes

### Stripe.js 10.0.0 declaration boundary

The separately collected `@stripe/stripe-js@10.0.0` Endive baseline removes `StripePaymentRequestButtonElement`, its barrel export, group creation/lookup overloads and Element-union membership, while retaining `stripe.paymentRequest()` and its lower-level events. This complements the independently owned React 7.0.0 wrapper removal above. Express Checkout remains a separate integration, not a renamed Payment Request Button; no wallet availability or hosted behavior is established solely by the declaration change. See [[source-github-stripe-js]].

- Domain must be registered in Stripe in both test and live mode
- Reuses an existing Elements instance — compatible with Payment Element in the same group
- New payment methods added from Dashboard activate without frontend changes
- Supersedes the Payment Request Button Element — see migration table above
- Must serve over HTTPS in both development and production
- Elements options (captureMethod, setupFutureUsage, paymentMethodOptions) must match PaymentIntent params on confirmation — mismatches cause errors

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-github-react-stripe-js]] - version-qualified React 7.0.0 Payment Request Button removal and retained Express Checkout wrapper
- [[source-stripe-express-checkout-element]] — April and November overview captures for built-in methods, qualified Firefox/webview matrix, custom buttons, styling, and dated availability events
- [[source-stripe-express-checkout-element-accept-payment]] — full integration guide: both API paths, customer detail collection, wallet events, testing, Connect
- [[source-stripe-express-checkout-element-migration]] — migration guide: Payment Request Button → ECE, before/after code, MPAN support
- [[source-github-stripe-js]] — package-qualified v9.14 beta Custom Payment Method button and dynamic availability-event typing
