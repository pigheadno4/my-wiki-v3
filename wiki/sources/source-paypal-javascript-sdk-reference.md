---
title: "PayPal JavaScript SDK Reference"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-javascript-sdk-reference.md"
tags: [paypal, javascript-sdk, buttons, marks, card-fields, funding-eligibility, messages, onapprove, oncreateorder, onshipping, cardfields, react, typescript]
---

## PayPal JavaScript SDK Reference

The complete JS SDK v5 API reference — objects, methods, callbacks, and options for all SDK components. Covers Vanilla JS, React (JS + TS), and ES Module patterns for every method.

Source URL: <https://developer.paypal.com/sdk/js/reference/>

Last updated: 2026-02-04

## SDK Components Covered

| Component | Top-level object |
| --------- | ---------------- |
| `buttons` | `paypal.Buttons(options)` |
| `marks` | `paypal.Marks(options)` |
| `card-fields` | `paypal.CardFields(options)` |
| `funding-eligibility` | `paypal.getFundingSources()`, `paypal.isFundingEligible()` |
| `messages` | `paypal.Messages(options)` |

---

## `paypal.Buttons(options)` — Full Callback Reference

### Callbacks

| Callback | Trigger | Key data |
| -------- | ------- | -------- |
| `createOrder` | Buyer clicks button | Must return order ID |
| `createSubscription` | Buyer clicks (subscription flow) | Uses `actions.subscription.create({ plan_id })` |
| `onApprove` | Buyer approves on PayPal | `data.orderID`, `data.subscriptionID` |
| `onCancel` | Buyer cancels | `data.orderID` |
| `onError` | Unrecoverable SDK error | `err` (catch-all) |
| `onInit` | Button first renders | `actions.enable()` / `actions.disable()` |
| `onClick` | Button clicked | `data.fundingSource` |
| `onShippingChange` | **Deprecated** — use `onShippingAddressChange` | |
| `onShippingAddressChange` | Buyer changes shipping address | `data.shippingAddress`, `actions.reject(COUNTRY_ERROR)` etc. |
| `onShippingOptionsChange` | Buyer selects a shipping option | `data.selectedShippingOption`, `actions.reject()` |

### `style` options

| Option | Values | Notes |
| ------ | ------ | ----- |
| `layout` | `vertical` (default), `horizontal` | Vertical: max 6 buttons; Horizontal: max 2 |
| `color` | `gold` (recommended), `blue`, `silver`, `white`, `black` | |
| `shape` | `rect` (default), `pill`, `sharp` | |
| `borderRadius` | number ≥ 0 | Takes priority over `shape` |
| `label` | `paypal` (default), `checkout`, `buynow`, `pay`, `installment` | `installment` only in MX and BR |
| `tagline` | `true`/`false` | Requires `layout: horizontal`; replaced by `message` option |
| `height` | 25–55 | Default max 55px |
| `disableMaxHeight` | `true` | Removes 55px max; can't combine with `height` |
| `disableMaxWidth` | `true` | Removes 750px max width |

### `message` options (Pay Later messaging inline with buttons)

- `amount` — current cart/product total; drives offer shown
- `align` — `center` (default), `left`, `right`
- `color` — `black` (default), `white`
- `position` — `top` or `bottom` (default); when card button present, forced to `top`
- US merchants/customers only; requires Pay Later eligibility

### `displayOnly`

| Value | Effect |
| ----- | ------ |
| `vaultable` | Show only payment methods that support saving |

### Other Buttons methods

- `paypal.Buttons().isEligible()` — returns `true/false` whether the button should render for the current buyer
- `paypal.Buttons().render(container)` — renders into the specified CSS selector or DOM element

### `createSubscription` setup

Requires `vault=true&intent=subscription` in the script tag. Uses `actions.subscription.create({ plan_id })` and `actions.subscription.revise()` for upgrades/downgrades.

---

## `paypal.Marks(options)`

Renders payment method logos for use with radio button layouts. `fundingSource` determines which mark to render. Use `mark.isEligible()` before rendering.

---

## `paypal.CardFields(options)` — Expanded Checkout

### Initialize

```javascript
const cardFields = paypal.CardFields({
    createOrder,
    onApprove,
    onError,
    inputEvents: { onChange, onFocus, onBlur, onInputSubmitRequest }
});
```

### Individual field components

| Method | Field rendered |
| ------ | -------------- |
| `cardFields.NameField(options).render(container)` | Cardholder name |
| `cardFields.NumberField(options).render(container)` | Card number |
| `cardFields.ExpiryField(options).render(container)` | Expiry date |
| `cardFields.CVVField(options).render(container)` | CVV |

### Style card fields

Via `style` object on individual field: `input`, `.invalid`, `.focused` CSS selectors. Via `style` on parent: styles applied across all fields.

### Card field `inputEvents`

| Event | Trigger |
| ----- | ------- |
| `onChange` | Field value changes |
| `onFocus` | Field receives focus |
| `onBlur` | Field loses focus |
| `onInputSubmitRequest` | Buyer submits form (e.g. presses Enter) |

### Methods on parent `cardFields`

| Method | Description |
| ------ | ----------- |
| `cardFields.isEligible()` | Whether card fields can render |
| `cardFields.submit(options)` | Submit the card form; triggers `createOrder` |
| `cardFields.getState()` | Returns current form state |

### Methods on individual field instances

| Method | Description |
| ------ | ----------- |
| `field.render(container)` | Render the field into a container |
| `field.clear()` | Clear the field value |
| `field.focus()` | Focus the field |
| `field.setAttribute(attr, val)` | Set an HTML attribute |
| `field.removeAttribute(attr)` | Remove an attribute |
| `field.addClass(className)` | Add a CSS class |
| `field.removeClass(className)` | Remove a CSS class |

### Validate entire card form

`cardFields.getState()` — returns field validation state before calling `submit()`.

---

## Funding helpers

| Method | Description |
| ------ | ----------- |
| `paypal.getFundingSources()` | Returns array of eligible funding sources for the current buyer |
| `paypal.isFundingEligible(fundingSource)` | Returns boolean for a specific funding source |
| `paypal.rememberFunding(fundingSources)` | Persists funding source preferences across sessions |

---

## `onShippingAddressChange` vs `onShippingOptionsChange`

```javascript
paypal.Buttons({
    onShippingAddressChange: async (data, actions) => {
        if (data.shippingAddress.countryCode !== 'US') {
            return actions.reject(PAYPAL_ERRORS.COUNTRY_ERROR);
        }
        // update order with new shipping costs
        await actions.resolve();
    },
    onShippingOptionsChange: async (data, actions) => {
        // data.selectedShippingOption
        await actions.resolve();
    }
});
```

Available `PAYPAL_ERRORS` for rejection: `ADDRESS_ERROR`, `COUNTRY_ERROR`, `STATE_ERROR`, `ZIP_ERROR`, `METHOD_UNAVAILABLE`, `STORE_UNAVAILABLE`.

---

## React patterns

All callbacks available as `PayPalButtons` props. TypeScript types available via `@paypal/react-paypal-js`:

- `ReactPayPalScriptOptions` — options for `PayPalScriptProvider`
- `PayPalButtonsComponentProps["createOrder"]` — typed callback
- `PayPalButtonsComponentProps["onApprove"]` — typed callback
- etc.

---

## Raw Sources

- [[paypal-javascript-sdk-reference]] — full verbatim content (3,727 lines) with Vanilla JS, React JS, React TS, and ES Module examples for every method

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[paypal-expanded-checkout]] — CardFields component
- [[source-paypal-javascript-sdk-configuration]] — script tag query parameters reference
- [[source-paypal-javascript-sdk-overview]] — SDK component overview
- [[source-paypal-checkout-standalone-buttons]] — `getFundingSources()` + `isEligible()` usage
- [[source-paypal-checkout-validate-user-input]] — `onInit`/`onClick` callbacks in practice
