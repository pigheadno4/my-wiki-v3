---
title: "PayPal Pay Later CA Button + Message Integration Guide (Canada Merchant)"
type: analysis
date_created: 2026-04-16
tags: [paypal, pay-later, canada, ca, messaging, button, js-sdk, enable-funding, bnpl, bilingual, french, english]
---

## Overview

Step-by-step integration guide for a **Canada-based PayPal merchant** integrating the Pay Later button and Pay Later messaging on their site.

**CA Pay Later product:**

| Product | Payments | Schedule | Range |
| --- | --- | --- | --- |
| Pay in 4 | 4 | First at checkout, then every 2 weeks (biweekly) | CAD $30–$1,500 |

**Key CA-specific requirement:** Canada requires **bilingual support** — both English (`en_CA`) and French (`fr_CA`). The `locale` parameter on the SDK URL controls the button language; `data-pp-language` controls the message language. You must serve the correct language version based on the buyer's site language.

## Prerequisites

- Canada-based PayPal Business account
- Canada-facing website transacting in CAD
- One-time payment integration (recurring/reference transactions are ineligible)
- Existing PayPal Checkout integration

## SDK Script Tag

`enable-funding=paylater` is **required** — without it the Pay Later button will not render for CA merchants. Set `locale` to match the page language:

**English site:**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=en_CA"
></script>
```

**French site:**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=fr_CA"
></script>
```

> Only one `<script>` tag per page. If your site switches language dynamically (SPA), reload the SDK with the new `locale` by dispatching `resetOptions` via `usePayPalScriptReducer` (React) or reloading the page with the updated URL parameter.

## Pay Later Messages

Add `data-pp-language` to every `data-pp-message` element to match the page language. No `data-pp-buyercountry` needed — CA merchant accounts resolve CA eligibility automatically.

**English message:**

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-language="en-CA"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

**French message:**

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-language="fr-CA"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

### Message placements

| Placement | `data-pp-placement` value |
| --- | --- |
| Product page | `product` |
| Cart page | `cart` |
| Checkout page | `payment` |
| Home page | `home` |
| Category page | `category` |

### Dynamic amount update

The SDK monitors `data-pp-amount` for changes and re-renders automatically — do **not** call `render()` again:

```javascript
document.querySelector('[data-pp-message]')
  .setAttribute('data-pp-amount', newAmount);
```

## Pay Later Button

The Pay Later button renders as **"Pay in 4"** in `en_CA` locale. Always guard with `isEligible()`.

```html
<div id="paylater-button-container"></div>
```

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: {
    color: 'gold',    // or 'blue' to distinguish from a PayPal button
    shape: 'rect',
    layout: 'vertical',
  },
  createOrder: function(data, actions) {
    return actions.order.create({
      purchase_units: [{
        amount: {
          currency_code: 'CAD',
          value: '150.00'  // Update to actual cart total
        }
      }]
    });
  },
  onApprove: function(data, actions) {
    return actions.order.capture().then(function(details) {
      console.log('Order captured:', details);
    });
  },
  onError: function(err) {
    console.error('PayPal error:', err);
  }
});

if (payLaterButton.isEligible()) {
  payLaterButton.render('#paylater-button-container');
}
```

## Radio Button Payment Wall Pattern

If showing PayPal and Pay Later as separate radio options, gate the radio row on `isEligible()` — never show a radio option for a button that won't render:

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: { color: 'blue', shape: 'rect', layout: 'vertical' },
  createOrder: createOrder,
  onApprove: onApprove,
  onError: onError
});

if (payLaterButton.isEligible()) {
  // Show the radio row and its inline message
  document.getElementById('row-paylater').style.display = 'block';
  paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER }).render('#mark-paylater');
  payLaterButton.render('#button-paylater');
} else {
  // Hide the entire radio row — buyer cannot use Pay Later this session
  document.getElementById('row-paylater').style.display = 'none';
}
```

For the full radio button payment wall pattern see [[analysis-paypal-radio-button-payment-wall]].

## React Integration (`@paypal/react-paypal-js`)

### Provider setup

Pass `locale` and `enableFunding` in the options object. Serve different `locale` values based on the page language:

```jsx
import { PayPalScriptProvider } from "@paypal/react-paypal-js";

// English site
const PAYPAL_OPTIONS_EN = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "en_CA",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",
};

// French site
const PAYPAL_OPTIONS_FR = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "fr_CA",
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",
};

export default function App({ language }) {
  const options = language === "fr" ? PAYPAL_OPTIONS_FR : PAYPAL_OPTIONS_EN;
  return (
    <PayPalScriptProvider options={options}>
      <CheckoutPage language={language} />
    </PayPalScriptProvider>
  );
}
```

### Language switching in SPA

Use `resetOptions` to reload the SDK when the user switches language:

```jsx
import { usePayPalScriptReducer } from "@paypal/react-paypal-js";

function LanguageSwitcher() {
  const [{ options }, dispatch] = usePayPalScriptReducer();

  function switchToFrench() {
    dispatch({
      type: "resetOptions",
      value: { ...options, locale: "fr_CA" },
    });
  }

  return <button onClick={switchToFrench}>Français</button>;
}
```

### Pay Later message component

Pass `language` as a prop to `<PayPalMessages>`:

```jsx
import { PayPalMessages } from "@paypal/react-paypal-js";

// language: "en-CA" | "fr-CA"
function PayLaterMessage({ amount, language }) {
  return (
    <PayPalMessages
      style={{
        layout: "text",
        logo: { type: "inline" },
        text: { color: "black", size: 12 },
      }}
      amount={amount}
      placement="product"
      language={language}
    />
  );
}
```

### Pay Later button + message (complete CA example)

```jsx
import {
  PayPalScriptProvider,
  PayPalButtons,
  PayPalMessages,
  PayPalMarks,
  FUNDING,
  usePayPalScriptReducer,
} from "@paypal/react-paypal-js";

// ── Provider — place at app root ──────────────────────────────────────────
// language: "en" | "fr" — determined by your site's active language
const PAYPAL_OPTIONS = {
  clientId: "YOUR_CLIENT_ID",
  currency: "CAD",
  locale: "en_CA",             // switch to "fr_CA" for French site
  components: "messages,buttons,funding-eligibility,marks",
  enableFunding: "paylater",   // required for CA merchants
};

export default function App() {
  return (
    <PayPalScriptProvider options={PAYPAL_OPTIONS}>
      <CheckoutSection language="en-CA" amount={150.00} />
    </PayPalScriptProvider>
  );
}

// ── Checkout section — message + mark + button ────────────────────────────
// language: "en-CA" | "fr-CA"
function CheckoutSection({ language, amount }) {
  const [{ isResolved }] = usePayPalScriptReducer();

  if (!isResolved) return <p>Loading payment options…</p>;

  return (
    <div>
      {/* Pay Later message — shown above the button */}
      <PayPalMessages
        style={{
          layout: "text",
          logo: { type: "inline" },
          text: { color: "black", size: 12 },
        }}
        amount={amount}
        placement="payment"
        language={language}
      />

      {/* Pay Later mark + button */}
      <div style={{ display: "flex", alignItems: "center", gap: 8, marginTop: 8 }}>
        <PayPalMarks fundingSource={FUNDING.PAYLATER} />
      </div>

      <PayPalButtons
        fundingSource={FUNDING.PAYLATER}
        style={{ color: "gold", shape: "rect", layout: "vertical" }}
        createOrder={(data, actions) =>
          actions.order.create({
            purchase_units: [{
              amount: { currency_code: "CAD", value: String(amount) },
            }],
          })
        }
        onApprove={(data, actions) =>
          actions.order.capture().then((details) => {
            console.log("Captured:", details);
          })
        }
        onError={(err) => console.error(err)}
      >
        {/* children renders when Pay Later is ineligible — return null to hide silently */}
        {null}
      </PayPalButtons>
    </div>
  );
}
```

## Bilingual Summary

| Element | English | French |
| --- | --- | --- |
| SDK `locale` param | `locale=en_CA` | `locale=fr_CA` |
| Message `data-pp-language` | `data-pp-language="en-CA"` | `data-pp-language="fr-CA"` |
| React `<PayPalMessages language>` | `language="en-CA"` | `language="fr-CA"` |
| React `PayPalScriptProvider locale` | `locale: "en_CA"` | `locale: "fr_CA"` |
| Button label (rendered by SDK) | "Pay in 4" | "Payez en 4 fois" |

## Key Rules

| Rule | Detail |
| --- | --- |
| CA merchant account required | Standard CA Pay Later requires a Canada-based PayPal account — no cross-border approval needed unlike FR/US scenarios |
| `enable-funding=paylater` | **Required** — Pay Later button will not render without it |
| `currency=CAD` | Required — CA Pay Later only supports Canadian dollars |
| Amount range | CAD $30–$1,500 — message auto-hides outside this range; `isEligible()` gates the button |
| Bilingual support | **Required** — serve `en_CA` and `fr_CA` based on site language |
| `locale` vs `data-pp-language` | `locale` is an SDK URL param controlling button language; `data-pp-language` is a per-message attribute controlling message language — both must be set |
| No content modification | Cannot translate, resize, recolor, or modify Pay Later message text |
| No recurring | Reference Transactions and Recurring Payment integrations are ineligible |
| One SDK load per page | All components in a single `<script>` tag |
| `message` inside `Buttons()` | **US merchants + US buyers only** — not applicable here; use standalone `data-pp-message` with `data-pp-language` |

## Test and Go Live

1. Use sandbox `client-id=test` with `buyer-country=CA` (sandbox only) to simulate a CA buyer
2. Verify Pay in 4 button renders and message displays in both `en_CA` and `fr_CA`
3. Confirm message auto-hides below CAD $30 and above CAD $1,500
4. Remove `buyer-country=CA` and swap to production `client-id` when going live

```html
<!-- Sandbox testing only -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=CA&components=messages,buttons,funding-eligibility,marks&currency=CAD&enable-funding=paylater&locale=en_CA"
></script>
```

## Relevant Wiki Pages

- [[paypal-checkout]] — Base Checkout integration
- [[paypal-pay-later]] — Pay Later product details by country
- [[analysis-paypal-radio-button-payment-wall]] — Radio button payment wall pattern with eligibility gating
- [[analysis-paypal-pay-later-fr-integration-guide]] — Cross-border Pay Later (non-CA merchant targeting FR buyers)

## Sources

- [[source-paypal-pay-later]] — CA Pay Later eligibility, biweekly schedule, CAD $30–$1,500 range, bilingual requirements, `locale` and `data-pp-language` parameters
