---
title: "PayPal Checkout: Display Other Payment Methods"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-display-payment-methods.md"
tags: [paypal, checkout, marks, radio-buttons, payment-methods, javascript-sdk, ui]
---

## PayPal Checkout: Display Other Payment Methods

Official PayPal guide for presenting PayPal alongside other payment methods using radio buttons and the JS SDK `Marks` component.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/display-payment-methods/>

Last updated: 2025-05-13

## Key Takeaways

### Two UI components involved

- **Buttons** (`paypal.Buttons()`) — the standard PayPal checkout button
- **Marks** (`paypal.Marks()`) — auto-renders payment method logos (PayPal, Venmo, Pay Later, cards) without writing custom image markup

Both must be included in the script tag: `&components=buttons,marks`

### Pattern: radio button toggle

The standard approach is a radio group where selecting PayPal shows the PayPal button and hides other payment buttons, and vice versa:

```javascript
// Script tag
<script src="https://www.paypal.com/sdk/js?client-id=test&components=buttons,marks">

// Render
paypal.Marks().render('#paypal-marks-container');
paypal.Buttons().render('#paypal-button-container');

// Toggle visibility on radio change
el.addEventListener('change', (event) => {
    if (event.target.value === 'paypal') {
        // show #paypal-button-container, hide #alternate-button-container
    } else {
        // show #alternate-button-container, hide #paypal-button-container
    }
});

// Default: hide alternate button
document.querySelector('#alternate-button-container').style.display = 'none';
```

### Compliance note (implicit)

Per PayPal's User Agreement (covered in best practices docs), PayPal must be presented equally or earlier than other payment methods — this pattern satisfies that by defaulting to PayPal selected.

## Raw Sources

- [[paypal-checkout-display-payment-methods]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-display-funding-source]] — related: detecting which funding source the buyer chose
