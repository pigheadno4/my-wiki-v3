---
title: "PayPal Expanded Checkout: Card Field Properties"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-card-field-properties.md"
tags: [paypal, expanded-checkout, card-fields, properties, inputevents, placeholder, javascript-sdk]
---

## PayPal Expanded Checkout: Card Field Properties

Reference for the four CardFields components (v2), their required/optional status, and the three options available on each field.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/card-field-properties/>

Last updated: 2025-02-28

## Key Takeaways

### Four field components

| Component | Required | Notes |
| --------- | -------- | ----- |
| `NumberField` | Yes | Card number |
| `CVVField` | Yes | 3 or 4-digit CVV/CID |
| `ExpiryField` | Yes | Expiration date |
| `NameField` | No | Cardholder name |

### Three options per field

| Option | Type | Purpose |
| ------ | ---- | ------- |
| `inputEvents` | Object | Event callbacks (`onChange`, etc.) — returns a `stateObject` |
| `style` | Object | CSS styling (see [[source-paypal-expanded-checkout-card-field-style]]) |
| `placeholder` | String | Override default placeholder text |

### `inputEvents.onChange` returns `stateObject`

```javascript
inputEvents: {
    onChange: (event) => {
        console.log("returns a stateObject", event);
    }
}
```

The event parameter is a `stateObject` — contains field validation state and other metadata.

### Pattern: render to DOM element reference

Fields are rendered by passing a DOM element (not a CSS selector string):

```javascript
const cardNameContainer = document.getElementById("card-name-field-container");
nameField.render(cardNameContainer);  // DOM element, not "#card-name-field-container"
```

## Raw Sources

- [[paypal-expanded-checkout-card-field-properties]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-expanded-checkout-card-field-style]] — CSS style options for card fields
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
- [[source-paypal-javascript-sdk-reference]] — full CardFields API reference
