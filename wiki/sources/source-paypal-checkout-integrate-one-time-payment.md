---
title: "PayPal Checkout: Integrate One-time Payment"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-integrate-one-time-payment.md"
  - "paypal-checkout-integrate-server-side-shipping.md"
tags: [paypal, checkout, javascript-sdk, orders-api, integration, node-js, app-switch, sandbox, refund, shipping-callbacks]
---

## PayPal Checkout: Integrate One-time Payment

Official PayPal developer integration guide with full frontend and backend code samples for a standard one-time checkout using the JS SDK and Node.js server.

Source URL: <https://developer.paypal.com/studio/checkout/standard/integrate>

## Key Takeaways

### Frontend (Client)

- **Script tag**: Load `https://www.paypal.com/sdk/js` with params: `client-id`, `buyer-country` (sandbox only), `currency`, `components=buttons`, `enable-funding` (e.g. `venmo,paylater,card`).
- **File structure**: `/src/index.html` + `/src/app.js`
- **Button init**: `window.paypal.Buttons({ style, message, createOrder, onApprove, onError, onCancel })` — renders into `#paypal-button-container`
- **`createOrder`**: POSTs to `/api/orders` with cart data → returns `orderData.id`
- **`onApprove`**: POSTs to `/api/orders/{orderID}/capture` → handles 3 cases:
  1. `INSTRUMENT_DECLINED` → call `actions.restart()` (recoverable)
  2. Other error → show failure message
  3. Success → show confirmation with `transaction.status` and `transaction.id`
- **`onError`**: catch-all; redirect to error page
- **`onCancel`**: redirect to cancel/cart page
- **Button style options**: shape (rect/pill), layout (vertical/horizontal), color (gold/etc), label, message amount

### Backend (Server, Node.js)

- **SDK**: `@paypal/paypal-server-sdk` — two controllers used: `OrdersController`, `PaymentsController`
- **Auth**: OAuth 2.0 Client Credentials via `PAYPAL_CLIENT_ID` + `PAYPAL_CLIENT_SECRET`; SDK auto-fetches token
- **Port**: 8080
- **`createOrder`**: calls `ordersController.createOrder()` with intent `CAPTURE`, purchase units (amount, items, shipping), and optional `paymentSource.paypal.experienceContext`
- **`captureOrder`**: calls `ordersController.captureOrder({ id: orderID })`
- **`refundCapturedPayment`**: calls `paymentsController.refundCapturedPayment({ captureId })`
- **Routes**:
  - `POST /api/orders` → createOrder
  - `POST /api/orders/:orderID/capture` → captureOrder
  - `POST /api/payments/refund` → refund

### App Switch (Mobile deep-link to PayPal app)

- **Client**: add `appSwitchWhenAvailable: true` to Buttons config; call `buttons.resume()` if `buttons.hasReturned()` is true (buyer returning from app switch)
- **Server**: include `appSwitchPreference.launchPaypalApp: true` + `returnUrl` + `cancelUrl` in `experienceContext`
- `return_url` and `cancel_url` must be identical, match the button page URL, include a session identifier, and have no hash fragment

### Contact Module (`experience_context.contactPreference`)

| Value | Behavior |
| ----- | -------- |
| `NO_CONTACT_INFO` (default) | Contact module hidden |
| `UPDATE_CONTACT_INFO` | Buyer can view and edit email/phone |
| `RETAIN_CONTACT_INFO` | Buyer sees but cannot edit; merchant pre-fills via `shipping.email_address` / `shipping.phone_number` |

### Shipping Callbacks

Two modes available — client-side and server-side:

**Client-side** (from `paypal-checkout-integrate-one-time-payment.md`):

- `onShippingAddressChange`: buyer selects new address → update eligibility + shipping costs + line items
- `onShippingOptionsChange`: buyer selects new shipping method → update costs + line items

**Server-side** (from `paypal-checkout-integrate-server-side-shipping.md`):

- Configured via `payment_source.paypal.experience_context.orderUpdateCallbackConfig` in Create Order
- `callbackUrl`: your server endpoint that receives PayPal's callbacks
- `callbackEvents`: array of events to subscribe to:
  - `SHIPPING_ADDRESS` — fires on review page load + address change. **Recommended** as the sole subscription; merchant returns all options upfront so `SHIPPING_OPTION` callback is not needed.
  - `SHIPPING_OPTION` — fires when buyer changes shipping option. Subscribe only if dynamic recalculation on option change is needed.
- Also requires `shippingPreference: ShippingPreference.GetFromFile` in `experienceContext`

**Merchant Decline Response** (server-side only): Return HTTP 422 with `UNPROCESSABLE_ENTITY` to reject a shipping address. Supported `issue` error codes:

| Code | Description |
| ---- | ----------- |
| `ADDRESS_ERROR` | Can't ship to this address |
| `COUNTRY_ERROR` | Can't ship to this country |
| `STATE_ERROR` | Can't ship to this state |
| `ZIP_ERROR` | Can't ship to this zip |
| `METHOD_UNAVAILABLE` | Selected shipping method unavailable |
| `STORE_UNAVAILABLE` | Part of order unavailable at this store |

```json
{ "name": "UNPROCESSABLE_ENTITY", "details": [{ "issue": "COUNTRY_ERROR" }] }
```

### Additional `experienceContext` fields (server-side shipping variant)

- `landingPage: PaypalExperienceLandingPage.Login` — send buyer directly to login page
- `shippingPreference: ShippingPreference.GetFromFile` — required for server-side shipping callbacks

### Sandbox Testing Checklist

- PayPal payment: button → personal sandbox login → Pay Now → verify business sandbox account received funds (minus fees)
- Card payment: use credit card generator → enter details → confirm in merchant sandbox activity log

### Go Live Steps

1. Log into Developer Dashboard with business account
2. Obtain live credentials
3. Swap sandbox credentials → live credentials
4. Update endpoint (remove sandbox environment flag)

## Notable Code Patterns

### INSTRUMENT_DECLINED recovery

```javascript
if (errorDetail?.issue === "INSTRUMENT_DECLINED") {
    return actions.restart(); // lets buyer pick a different funding source
}
```

### App Switch resume

```javascript
if (paypalButtons.hasReturned()) {
    paypalButtons.resume();
} else {
    paypalButtons.render("#paypal-button-container");
}
```

### Server SDK client init

```javascript
const client = new Client({
    clientCredentialsAuthCredentials: {
        oAuthClientId: PAYPAL_CLIENT_ID,
        oAuthClientSecret: PAYPAL_CLIENT_SECRET,
    },
    environment: Environment.Sandbox,
});
```

## Raw Sources

- [[paypal-checkout-integrate-one-time-payment]] — verbatim webpage content, client-side shipping callback tab, full code samples
- [[paypal-checkout-integrate-server-side-shipping]] — same page, server-side shipping callback tab; adds `orderUpdateCallbackConfig`, merchant decline error codes, updated `server.js`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-getting-started]] — getting started guide (prerequisite to this page)
