---
title: "PayPal Expanded Checkout: Card Fields Style Guide"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-card-field-style.md"
tags: [paypal, expanded-checkout, card-fields, css, styling, javascript-sdk]
---

## PayPal Expanded Checkout: Card Fields Style Guide

Reference for supported CSS properties and styling patterns for the CardFields component.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/>

Last updated: 2025-05-14

## Key Takeaways

### Restricted CSS — only the listed properties work

Only ~40 CSS properties are supported. Any unsupported property logs a **warning to the browser console** (not an error) — easy to miss. Key supported properties:

`appearance`, `background`, `border`, `border-radius`, `box-shadow`, `color`, `direction`, `font*`, `height`, `letter-spacing`, `line-height`, `opacity`, `outline`, `padding*`, `text-shadow`, `transition` + vendor prefixes (`-moz-*`, `-webkit-*`)

### Two style targets

Styles use CSS selector keys, not DOM class names:
- `'input'` — the input element itself
- `'.invalid'` — applied when the field fails validation

### Two scoping levels

| Level | How | Effect |
| ----- | --- | ------ |
| Parent (all fields) | Pass `style` to `paypal.CardFields({ style })` | Applied to every field |
| Individual field | Pass `style` to `cardField.NameField({ style })` | Overrides parent style for that field |

## Raw Sources

- [[paypal-expanded-checkout-card-field-style]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog
- [[source-paypal-javascript-sdk-reference]] — CardFields API reference (style property documented there)
