---
title: "PayPal Pay Later Button + Message Integration Guide (US, FR, GB, IT, ES)"
type: analysis
date_created: 2026-04-17
tags: [paypal, pay-later, multi-country, us, fr, gb, it, es, messaging, button, js-sdk, enable-funding, bnpl, cross-border, funding-eligibility]
---

## Overview

Multi-country integration guide for adding the **Pay Later button** and **Pay Later messaging** across five markets: US, FR, GB, IT, and ES. Each country has distinct Pay Later products, currency requirements, and eligibility rules.

This guide covers two merchant scenarios:

1. **Native merchant** — your PayPal account is based in the same country as the buyer (e.g., US merchant → US buyers). Standard integration; no cross-border approval needed.
2. **Cross-border merchant** — your PayPal account is in a different country than the buyer (e.g., US merchant → FR buyers). Requires **PayPal approval** for cross-border messaging (limited release) and the `buyerCountry` parameter on every message element.

## Pay Later Products by Country

| Country | Product | Payments | Schedule | Amount Range | Currency |
| --- | --- | --- | --- | --- | --- |
| US | Pay in 4 | 4 | Biweekly (every 2 weeks) | $30–$1,500 | USD |
| US | Pay Monthly | 3, 6, 12, or 24 | Monthly | $49–$10,000 | USD |
| FR | Pay in 4 ("4X PayPal") | 4 | Monthly (over 90 days) | 30€–2,000€ | EUR |
| GB | Pay in 3 | 3 | Monthly | £20–£3,000 | GBP |
| IT | Pay in 3 | 3 | Monthly | 30€–2,000€ | EUR |
| IT | Pay in installments | 6, 12, or 24 | Monthly | 120€–5,000€ | EUR |
| ES | Pay in 3 | 3 | Monthly | 30€–2,000€ | EUR |
| ES | Pay in installments | 6, 12, or 24 | Monthly | 120€–5,000€ | EUR |

## Prerequisites

### Native merchant (same-country)

- PayPal Business account based in the target country
- Website facing that country's consumers
- Transactions in the country's supported currency
- One-time payment integration (recurring/reference transactions ineligible)
- Existing PayPal Checkout integration

### Cross-border merchant (different country)

All of the above, plus:

- PayPal approval for [cross-border messaging](https://developer.paypal.com/limited-release/sdk-pay-later-messaging-cross-border/) (limited release)
- `buyerCountry` / `data-pp-buyercountry` on every message element

## SDK Script Tag

One `<script>` tag per page. Key parameters:

- `enable-funding=paylater` — **required for non-US merchant accounts**; without it the Pay Later button will not render. US merchants get Pay Later enabled by default but including it explicitly is harmless.
- `currency` — must match the target country's currency
- `components` — include `messages,buttons,funding-eligibility` at minimum; add `marks` if using radio button payment wall

### Per-country SDK URLs

**US (native merchant):**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=USD&enable-funding=paylater"
></script>
```

**FR (native merchant):**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=EUR&enable-funding=paylater"
></script>
```

**GB (native merchant):**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=GBP&enable-funding=paylater"
></script>
```

**IT / ES (native merchant — both use EUR):**

```html
<script
  src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages,buttons,funding-eligibility,marks&currency=EUR&enable-funding=paylater"
></script>
```

> Only one `<script>` tag per page. If you serve multiple countries from one site, determine the buyer's country server-side and render the appropriate SDK URL with the correct `currency`.

## Pay Later Messages

### Native merchant messages

For native merchants (account country matches buyer country), no `buyerCountry` parameter is needed — the SDK resolves eligibility automatically from the merchant account.

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

### Cross-border merchant messages

For cross-border merchants, add `data-pp-buyercountry` on **every** message element. Valid values: `US`, `FR`, `GB`, `IT`, `ES`.

**Example — US merchant targeting FR buyers:**

```html
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
```

**Example — US merchant targeting GB buyers:**

```html
<div
  data-pp-message
  data-pp-placement="product"
  data-pp-amount="150.00"
  data-pp-buyercountry="GB"
  data-pp-style-layout="text"
  data-pp-style-logo-type="inline"
  data-pp-style-text-color="black"
  data-pp-style-text-size="12"
></div>
```

### JavaScript API alternative

```javascript
paypal.Messages({
  amount: 150.00,
  placement: 'product',
  buyerCountry: 'FR',  // omit for native merchants
  style: {
    layout: 'text',
    logo: { type: 'inline' },
    text: { color: 'black', size: 12 },
  },
}).render('.pp-message');
```

### Message placements

| Page | `data-pp-placement` value | Recommended layout |
| --- | --- | --- |
| Product page | `product` | `text` |
| Cart page | `cart` | `text` |
| Checkout page | `payment` | `text` |
| Home page | `home` | `flex` (banner) |
| Category page | `category` | `flex` (banner) |

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

### Dynamic amount update

The SDK monitors `data-pp-amount` for changes and re-renders automatically — do **not** call `render()` again:

```javascript
document.querySelector('[data-pp-message]')
  .setAttribute('data-pp-amount', newAmount);
```

## Pay Later Button

The Pay Later button label is localized by the SDK based on the merchant account locale:

| Country | Button label |
| --- | --- |
| US | "Pay Later" (covers Pay in 4 + Pay Monthly) |
| FR | "4X PayPal" |
| GB | "Pay in 3" |
| IT | "Paga in 3 rate" |
| ES | "Paga en 3 plazos" |

### Standalone Pay Later button

```html
<div id="paylater-button-container"></div>
```

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: {
    color: 'blue',     // blue to distinguish from gold PayPal button
    shape: 'rect',
    layout: 'vertical',
  },
  createOrder: function(data, actions) {
    return actions.order.create({
      purchase_units: [{
        amount: {
          currency_code: 'EUR',  // match target country currency
          value: '150.00'
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

> **Currency codes by country:** US → `USD`, FR/IT/ES → `EUR`, GB → `GBP`

## Funding Eligibility Verification

`isEligible()` is the **runtime per-session gate**. It reflects whether the Pay Later button can render for this specific buyer session based on buyer country, currency, cart amount, and account status.

- `enable-funding=paylater` tells the SDK to *attempt* to load Pay Later — it does not guarantee eligibility
- `isEligible()` is the definitive check — always call it before rendering

### Eligibility flow

```text
SDK loads with enable-funding=paylater
        │
        ▼
paypal.Buttons({ fundingSource: FUNDING.PAYLATER })
        │
        ▼
   isEligible()?
     /       \
   YES        NO
    │          │
    ▼          ▼
 render()   hide UI
```

### Basic eligibility gate

```javascript
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: { color: 'blue', shape: 'rect', layout: 'vertical' },
  createOrder: createOrder,
  onApprove: onApprove,
  onError: onError
});

if (payLaterButton.isEligible()) {
  payLaterButton.render('#paylater-button-container');
} else {
  document.getElementById('paylater-button-container').style.display = 'none';
}
```

### Radio button payment wall with eligibility

When showing PayPal and Pay Later as separate radio options, gate the radio row on `isEligible()` — never show a radio option for a button that won't render.

**HTML structure (rows hidden by default):**

```html
<!-- PayPal radio row -->
<div id="row-paypal" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paypal" />
    <span id="mark-paypal"></span>
    PayPal
  </label>
  <div id="panel-paypal" style="display: none;">
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-style-layout="text"
      data-pp-style-logo-type="inline"
    ></div>
    <div id="button-paypal"></div>
  </div>
</div>

<!-- Pay Later radio row -->
<div id="row-paylater" style="display: none;">
  <label>
    <input type="radio" name="payment-method" value="paylater" />
    <span id="mark-paylater"></span>
    Pay Later
  </label>
  <div id="panel-paylater" style="display: none;">
    <div
      data-pp-message
      data-pp-placement="payment"
      data-pp-amount="150.00"
      data-pp-style-layout="text"
      data-pp-style-logo-type="inline"
    ></div>
    <div id="button-paylater"></div>
  </div>
</div>
```

> **Cross-border merchants**: add `data-pp-buyercountry="XX"` to both `data-pp-message` elements above (replace `XX` with the target country code).

**JavaScript — eligibility gating + rendering:**

```javascript
// ── Shared order callbacks ────────────────────────────────
function createOrder(data, actions) {
  return actions.order.create({
    purchase_units: [{
      amount: { currency_code: 'EUR', value: '150.00' }
    }]
  });
}

function onApprove(data, actions) {
  return actions.order.capture().then(function(details) {
    console.log('Order captured:', details);
  });
}

function onError(err) {
  console.error('PayPal error:', err);
}

// ── PayPal button ─────────────────────────────────────────
var paypalButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYPAL,
  style: { color: 'gold', shape: 'rect', layout: 'vertical' },
  createOrder: createOrder,
  onApprove: onApprove,
  onError: onError
});

if (paypalButton.isEligible()) {
  document.getElementById('row-paypal').style.display = 'block';
  paypal.Marks({ fundingSource: paypal.FUNDING.PAYPAL }).render('#mark-paypal');
  paypalButton.render('#button-paypal');
}

// ── Pay Later button ──────────────────────────────────────
var payLaterButton = paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  style: { color: 'blue', shape: 'rect', layout: 'vertical' },
  createOrder: createOrder,
  onApprove: onApprove,
  onError: onError
});

if (payLaterButton.isEligible()) {
  document.getElementById('row-paylater').style.display = 'block';
  paypal.Marks({ fundingSource: paypal.FUNDING.PAYLATER }).render('#mark-paylater');
  payLaterButton.render('#button-paylater');
} else {
  document.getElementById('row-paylater').style.display = 'none';
}

// ── Radio toggle logic ───────────────────────────────────
document.querySelectorAll('input[name="payment-method"]').forEach(function(radio) {
  radio.addEventListener('change', function() {
    document.getElementById('panel-paypal').style.display = 'none';
    document.getElementById('panel-paylater').style.display = 'none';
    document.getElementById('panel-' + this.value).style.display = 'block';
  });
});
```

### Paired message with `contextualComponents`

Place a standalone message adjacent to the Pay Later button using `contextualComponents: 'PAY_LATER_BUTTON'` for coordinated styling:

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

## Country-Specific Notes

### US

- **Native eligibility** — US merchants get Pay Later enabled by default; `enable-funding=paylater` is not strictly required but including it is harmless
- **`message` inside `Buttons()`** — the `message` option inside `paypal.Buttons()` is supported **only for US merchants + US buyers**. For all other country scenarios, use standalone `data-pp-message` or `paypal.Messages()`
- **Two products** — Pay in 4 (biweekly, $30–$1,500) and Pay Monthly (monthly, $49–$10,000). The SDK automatically determines which product the buyer sees based on cart amount and credit approval

### FR

- **Native eligibility** — requires a France-based PayPal merchant account
- **Cross-border** — US/other merchant accounts must use `buyerCountry: 'FR'` on messages and have PayPal cross-border approval
- **Button label** — renders as "4X PayPal" in French locale
- **Content restriction** — cannot create, display, or host your own Pay Later content; stricter than other countries
- **No social media** — cannot post Pay Later content on social media without PayPal written authorization

### GB

- **Limited availability** — Pay Later offers are available to UK merchants on a **limited basis**
- **PayPal Credit** — in addition to Pay in 3, UK also offers PayPal Credit (revolving credit line, 0% for 4 months on purchases over £99)
- **Currency** — GBP only; SDK must load with `currency=GBP`
- **Cross-border** — non-UK merchant accounts must use `buyerCountry: 'GB'` on messages

### IT

- **Two products** — Pay in 3 (3 monthly, 30€–2,000€) and Pay in installments (6/12/24 monthly, 120€–5,000€)
- **Currency** — EUR only
- **Cross-border** — non-IT merchant accounts must use `buyerCountry: 'IT'` on messages

### ES

- **Two products** — Pay in 3 (3 monthly, 30€–2,000€) and Pay in installments (6/12/24 monthly, 120€–5,000€)
- **Currency** — EUR only
- **Same products as IT** — identical structure and amount ranges
- **Cross-border** — non-ES merchant accounts must use `buyerCountry: 'ES'` on messages

## Cross-Border Quick Reference

| Your merchant account | Target buyers | `currency` | `buyerCountry` needed? | Cross-border approval? |
| --- | --- | --- | --- | --- |
| US | US | USD | No | No |
| US | FR | EUR | Yes (`FR`) | Yes |
| US | GB | GBP | Yes (`GB`) | Yes |
| US | IT | EUR | Yes (`IT`) | Yes |
| US | ES | EUR | Yes (`ES`) | Yes |
| FR | FR | EUR | No | No |
| FR | US | USD | Yes (`US`) | Yes |
| GB | GB | GBP | No | No |
| IT | IT | EUR | No | No |
| ES | ES | EUR | No | No |

> **Rule**: if your PayPal account country differs from the buyer's country, you need `buyerCountry` on messages **and** PayPal cross-border approval.

## Test and Go Live

### Sandbox testing

Use `client-id=test` with `buyer-country=XX` (sandbox only) to simulate buyers from each country:

```html
<!-- US buyer simulation -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=US&components=messages,buttons,funding-eligibility,marks&currency=USD&enable-funding=paylater"
></script>

<!-- FR buyer simulation -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=FR&components=messages,buttons,funding-eligibility,marks&currency=EUR&enable-funding=paylater"
></script>

<!-- GB buyer simulation -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=GB&components=messages,buttons,funding-eligibility,marks&currency=GBP&enable-funding=paylater"
></script>

<!-- IT buyer simulation -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=IT&components=messages,buttons,funding-eligibility,marks&currency=EUR&enable-funding=paylater"
></script>

<!-- ES buyer simulation -->
<script
  src="https://www.paypal.com/sdk/js?client-id=test&buyer-country=ES&components=messages,buttons,funding-eligibility,marks&currency=EUR&enable-funding=paylater"
></script>
```

### Testing checklist

1. Verify Pay Later button renders for each country with correct localized label
2. Verify messages display at all placements (product, cart, checkout, home, category)
3. Confirm messages auto-hide when amount is outside the country's eligible range
4. Confirm `isEligible()` returns `false` and radio row hides when Pay Later is unavailable
5. Test cross-border scenarios with `buyerCountry` parameter
6. Verify currency matches target country in both SDK URL and `createOrder`

### Go live

1. Remove `buyer-country=XX` parameter — sandbox only
2. Replace `client-id=test` with production `client-id`
3. Verify cross-border messaging approval is active on the production account (if applicable)

## Key Rules

| Rule | Detail |
| --- | --- |
| `enable-funding=paylater` | **Required** for non-US merchant accounts; recommended for all |
| One SDK load per page | All components in a single `<script>` tag |
| Currency must match | `currency` in SDK URL and `currency_code` in `createOrder` must match the target country |
| `isEligible()` is the gate | Always check before rendering — controls both the button and its associated radio row |
| Cross-border requires approval | Non-native country merchants need PayPal cross-border messaging approval (limited release) |
| `buyerCountry` for cross-border | Required on every `data-pp-message` / `paypal.Messages()` for cross-border scenarios |
| `message` inside `Buttons()` | **US merchants + US buyers only** — all other scenarios use standalone messages |
| No content modification | Cannot translate, resize, recolor, or modify Pay Later message text |
| No recurring payments | Reference Transactions and Recurring Payment integrations are ineligible |
| Amount auto-hide | Messages auto-hide when amount is outside the country's eligible range |

## Relevant Wiki Pages

- [[paypal-checkout]] — Base Checkout integration
- [[paypal-pay-later]] — Pay Later product details by country
- [[analysis-paypal-pay-later-fr-integration-guide]] — Detailed FR cross-border guide (US merchant → FR buyers)
- [[analysis-paypal-pay-later-ca-integration-guide]] — CA merchant guide with bilingual support
- [[analysis-paypal-radio-button-payment-wall]] — Full radio button payment wall pattern with React integration

## Sources

- [[source-paypal-pay-later]] — US/FR/GB/IT/ES Pay Later products, eligibility, amount ranges, cross-border messaging parameters
- [[source-paypal-checkout-standalone-buttons]] — `isEligible()`, `paypal.Marks()`, radio button payment wall pattern
- [[source-paypal-checkout-messaging-with-buttons]] — `message` inside `Buttons()` is US-only; standalone `paypal.Messages()` for all other scenarios
