---
title: "PayPal Pay Later FR Messaging + Button Integration Guide (US Merchant Account)"
type: analysis
date_created: 2026-04-14
tags: [paypal, pay-later, france, cross-border, messaging, button, js-sdk, enable-funding, bnpl]
---

## Overview

Step-by-step integration guide for a merchant with a **US PayPal account** who wants to display Pay Later messaging and a standalone Pay Later button targeting **French buyers** ("4X PayPal").

**Key constraint**: Standard FR Pay Later eligibility requires a France-based PayPal merchant account. A US account must use the **cross-border messaging** feature instead, which is a **limited release** requiring PayPal approval.

## Prerequisites

- US PayPal Business account with Checkout integration already in place
- PayPal approval for [cross-border messaging](https://developer.paypal.com/limited-release/sdk-pay-later-messaging-cross-border/) (limited release)
- Orders REST API integration (required for the Pay Later button)

## FR Pay Later Product

| Product | Payments | Range | Schedule |
|---|---|---|---|
| Pay in 4 ("4X PayPal") | 4 | €30–€2,000 | First at checkout, then monthly over 90 days |

## Step 1 — Single SDK Script Tag

One `<script>` tag per page covers both Pay Later messaging and the Pay Later button. Two parameters are critical:

- `enable-funding=paylater` — **required** for the Pay Later button to render; without it, the button will not appear for a non-FR merchant account
- `currency=EUR` — required since FR Pay Later transacts in EUR only

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility&currency=EUR&enable-funding=paylater"
></script>
```

> **Note:** The PayPal JS SDK can only be loaded once per page. Do not add a second `<script>` tag — merge all required `components` into this single tag.

## Step 2 — Pay Later Message Components

Add `data-pp-buyercountry="FR"` on every message element. The SDK auto-hides messages outside the €30–€2,000 range and displays legal disclosure that only FR customers are eligible.

### Text layout (product, cart, checkout pages)

```html
<!-- Product page -->
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-buyercountry="FR"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>

<!-- Cart page -->
<div
  data-pp-message
  data-pp-placement="cart"
  data-pp-amount="150.00"
  data-pp-buyercountry="FR"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
></div>

<!-- Checkout page -->
<div
  data-pp-message
  data-pp-placement="payment"
  data-pp-amount="150.00"
  data-pp-buyercountry="FR"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
></div>
```

### Flex banner layout (home/category pages)

```html
<div
  data-pp-message
  data-pp-placement="home"
  data-pp-buyercountry="FR"
  data-pp-style-layout="flex"
  data-pp-style-color="white-no-border"
  data-pp-style-ratio="8x1"
></div>
```

### JavaScript API alternative

```javascript
paypal.Messages({
  amount: 150.00,
  placement: 'product',
  buyerCountry: 'FR',
  style: {
    layout: 'text',
    logo: { type: 'inline' },
  },
}).render('.pp-message');
```

### Dynamic amount update (no re-render needed)

The SDK monitors `data-pp-*` attributes for changes and re-renders automatically. Do **not** call `render()` again for amount changes:

```javascript
// Update amount when cart changes — SDK auto-detects and re-renders
document.querySelector('[data-pp-message]')
  .setAttribute('data-pp-amount', newAmount);
```

For SPA/React: do not reload the SDK on state changes. Call `paypal.Messages.render()` again only when new DOM elements are injected.

## Step 3 — Funding Eligibility Check

Before rendering any Pay Later UI (button **or** its associated radio button / container), check eligibility using `paypal.Buttons({ fundingSource: paypal.FUNDING.PAYLATER }).isEligible()`. Eligibility is determined per session by the SDK based on buyer country, currency, cart amount, and account status.

**Rule: if the Pay Later button is not eligible, hide the radio button too.** Never show a radio option that leads to a button that won't render.

```javascript
// Check eligibility once, use the result to gate both the radio row and the button
const payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  // ... createOrder, onApprove, onError (see below)
});

if (payLaterButton.isEligible()) {
  // Show the radio button row
  document.getElementById('paylater-radio-row').style.display = 'block';
  // Render the button inside the radio-controlled panel
  payLaterButton.render('#paylater-button-container');
} else {
  // Hide the entire radio row — buyer cannot use Pay Later this session
  document.getElementById('paylater-radio-row').style.display = 'none';
}
```

**Corresponding HTML structure:**

```html
<!-- Radio row — hidden by default, shown only when eligible -->
<div id="paylater-radio-row" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paylater" />
    Pay in 4 installments (4X PayPal)
  </label>

  <!-- Collapsed panel revealed when radio is selected -->
  <div id="paylater-panel" style="display: none;">
    <div id="paylater-button-container"></div>
  </div>
</div>
```

**Wire the radio toggle to show/hide the button panel:**

```javascript
document.querySelector('input[value="paylater"]')
  .addEventListener('change', function() {
    document.getElementById('paylater-panel').style.display =
      this.checked ? 'block' : 'none';
  });
```

> **Why `isEligible()` instead of just `enable-funding=paylater`?**
> `enable-funding=paylater` tells the SDK to *attempt* to load Pay Later funding — it does not guarantee the button renders. Eligibility is still resolved per session (buyer location, account, cart amount). `isEligible()` is the runtime gate that reflects the actual outcome for this specific buyer session.

## Step 4 — Standalone Pay Later Button (full implementation)

Renders as **"4X PayPal"** in French locale. The `isEligible()` check from Step 3 already gates rendering — do not call `render()` without it.

```html
<div id="paylater-button-container"></div>
```

> **Important:** The `message` option inside `paypal.Buttons()` is **US merchants + US buyers only**. Do not use it for the FR cross-border scenario — use a standalone `paypal.Messages()` component instead (see Step 2).

```javascript
const payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,

  createOrder: function(data, actions) {
    return actions.order.create({
      purchase_units: [{
        amount: {
          currency_code: 'EUR',
          value: '150.00'  // Update to actual cart total
        }
      }]
    });
  },

  onApprove: function(data, actions) {
    return actions.order.capture().then(function(details) {
      console.log('Order captured:', details);
      // Redirect to confirmation page
    });
  },

  onError: function(err) {
    console.error('PayPal error:', err);
  }
});

// Gate on eligibility — also controls the radio row visibility (see Step 3)
if (payLaterButton.isEligible()) {
  document.getElementById('paylater-radio-row').style.display = 'block';
  payLaterButton.render('#paylater-button-container');
} else {
  document.getElementById('paylater-radio-row').style.display = 'none';
}
```

### Pair with a standalone message using `contextualComponents`

Use a separate `paypal.Messages()` with `contextualComponents: 'PAY_LATER_BUTTON'` to show a coordinated message adjacent to the button. This is the correct approach for cross-border — unlike the `message` option inside `Buttons()`, standalone `paypal.Messages()` supports `buyerCountry`:

```html
<div
  data-pp-message
  data-pp-amount="150.00"
  data-pp-buyercountry="FR"
  data-pp-contextualcomponents="PAY_LATER_BUTTON"
></div>
<div id="paylater-button-container"></div>
```

> `PAY_LATER_BUTTON` — message features Pay Later only, uses the PayPal monogram logo. Designed to sit adjacent to a Pay Later button.

## Step 5 — Test and Go Live

1. Use your **sandbox Client ID** during testing — verify messages render at all placements and the "4X PayPal" button appears
2. Confirm message auto-hides below €30 and above €2,000
3. Swap to **production Client ID** when ready to go live
4. Verify cross-border messaging approval is active on the production account before launch

## Rules and Restrictions

| Rule | Detail |
|---|---|
| PayPal approval required | Cross-border messaging is **limited release** — must be approved before going live |
| `enable-funding=paylater` | **Required** in SDK URL — Pay Later button will not render for non-FR accounts without it |
| One SDK load per page | Only one `<script>` tag allowed — merge all `components` into one tag |
| Currency | EUR only — `currency=EUR` in SDK and `currency_code: 'EUR'` in order creation |
| Amount range | €30–€2,000 — message auto-hides outside this range; `isEligible()` gates button AND radio row |
| Radio button gate | If `isEligible()` is false, hide the Pay Later radio row — never show a radio option for a button that won't render |
| No content modification | Cannot translate, resize, recolor, or modify message text in any way |
| No social media | Cannot post Pay Later content on social media without PayPal written authorization |
| No recurring | Reference Transactions and Recurring Payment integrations are ineligible |
| FR button label | `paypal.FUNDING.PAYLATER` renders as **"4X PayPal"** in French locale |
| Hosted content only | Cannot create, display, or host your own Pay Later content — use official PayPal-provided code only |
| `message` inside `Buttons()` | **US merchants + US buyers only** — do not use for FR cross-border; use standalone `paypal.Messages()` with `buyerCountry: 'FR'` instead |

## Relevant Wiki Pages

- [[paypal-pay-later]] — Pay Later product overview across all countries
- [[paypal-checkout]] — Base Checkout integration required for the Pay Later button
- [[paypal-apm]] — Other PayPal alternative payment methods

## Sources

- [[source-paypal-pay-later]] — FR Pay Later eligibility, cross-border messaging (`buyerCountry`), integration guide, JS API reference, standalone buttons, funding eligibility patterns
- [[source-paypal-checkout-standalone-buttons]] — Standalone button pattern: `paypal.FUNDING.PAYLATER`, `isEligible()`, radio button + Marks component pattern, `enable-funding` usage
- [[source-paypal-checkout-messaging-with-buttons]] — `message` option inside `paypal.Buttons()`: **US merchants + US buyers only** — not applicable for FR cross-border
- [[source-paypal-checkout-display-funding-source]] — `paypal.FUNDING.PAYLATER` localisation table ("4X PayPal" for France)
