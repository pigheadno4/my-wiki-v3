---
title: "PayPal Expanded Checkout: Card Field Events & Methods"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-card-fields-events.md"
tags: [paypal, expanded-checkout, card-fields, events, methods, inputevents, stateobject, javascript-sdk, accessibility]
---

## PayPal Expanded Checkout: Card Field Events & Methods

The most comprehensive CardFields reference page — covers all 4 input events, 3 parent methods, 9 individual field methods, and all type definitions (`stateObject`, `cardType`, `cardFieldData`, `cardSecurityCode`).

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/card-fields-events/>

Last updated: 2025-05-14

## Key Takeaways

### 4 input events

| Event | Trigger |
| ----- | ------- |
| `onChange` | Any field value changes |
| `onFocus` | Any field gains focus |
| `onBlur` | Any field loses focus |
| `onInputSubmitRequest` | Payer submits while focused (e.g. Enter key) — use `data.isFormValid` |

### 3 parent card field methods

| Method | Return | Key use |
| ------ | ------ | ------- |
| `getState()` | Promise → stateObject | Check form validity before submit; note: `emittedBy` absent |
| `isEligible()` | Boolean | Gate before rendering any fields |
| `submit()` | Promise/void | Programmatic form submission |

### 9 individual field methods

| Method | Return | Description |
| ------ | ------ | ----------- |
| `render(el)` | Promise/void | Accepts DOM element OR CSS selector string |
| `clear()` | void | Clear field value |
| `focus()` | void | Focus the field |
| `addClass(cls)` | Promise/void | Add CSS class |
| `removeClass(cls)` | Promise/void | Remove CSS class |
| `setAttribute(attr, val)` | Promise/void | Set attribute |
| `removeAttribute(attr)` | Promise/void | Remove attribute (`aria-invalid`, `aria-required`, `disabled`, `placeholder`) |
| `setMessage(msg)` | void | Screen reader message |
| `close()` | Promise/void | Dispose/tear down field |

### `stateObject` — key fields

- `isFormValid` — top-level form validity
- `errors` — array of invalid field codes: `INVALID_NAME`, `INVALID_NUMBER`, `INVALID_EXPIRY`, `INVALID_CVV`, `INELIGIBLE_CARD_VENDOR`
- `emittedBy` — which field triggered event (`"name"`, `"number"`, `"cvv"`, `"expiry"`) — **absent from `getState()` response**
- `fields.cardNumberField.isPotentiallyValid` — true if input could become valid (e.g. `41` could become a full Visa number)
- `cards` — array of matching card types (single item once type is determined)

### `render()` accepts both formats

```javascript
// DOM element
cardField.NumberField().render(cardNumberContainer);
// CSS selector
cardField.NumberField().render("#card-number-field-container");
```

Unlike the parent `paypal.Buttons().render()` which accepts only strings, CardFields `render()` accepts both.

### `isPotentiallyValid` vs `isValid`

- `isPotentiallyValid: true` — input could still complete to a valid value (partial input)
- `isValid: true` — input is complete and valid (ready to submit)

Use `isPotentiallyValid` for real-time UI hints; use `isValid` (or `isFormValid`) for submit gating.

### `close()` for SPA cleanup

When routing away from checkout in a SPA, call `nameField.close()` etc. to properly dispose components and avoid memory leaks.

### Supported `removeAttribute` values

Only: `aria-invalid`, `aria-required`, `disabled`, `placeholder` — not arbitrary HTML attributes.

## Raw Sources

- [[paypal-expanded-checkout-card-fields-events]] — verbatim webpage content with full type definitions and complete HTML integration example

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-card-field-properties]] — card field properties overview
- [[source-paypal-expanded-checkout-card-field-style]] — CSS styling reference
- [[source-paypal-javascript-sdk-reference]] — JS SDK CardFields API reference (overlapping content)
