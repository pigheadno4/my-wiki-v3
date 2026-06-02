---
title: "PayPal JavaScript SDK Overview"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-javascript-sdk-overview.md"
tags: [paypal, javascript-sdk, buttons, marks, card-fields, funding-eligibility, configuration, reference]
---

## PayPal JavaScript SDK Overview

Official top-level overview of the PayPal JavaScript SDK — a brief index to the four SDK components and their documentation sections.

Source URL: <https://developer.paypal.com/sdk/js/>

Last updated: 2024-09-12

## Key Takeaways

### Four SDK components

| Component | Purpose |
| --------- | ------- |
| `buttons` | Render PayPal, Venmo, Pay Later, Card payment buttons |
| `marks` | Render payment method logos/icons |
| `card-fields` | Hosted credit/debit card input fields (Expanded Checkout only) |
| `funding-eligibility` | Check whether a payment method is eligible for the current buyer |

### Three documentation areas

- **Configuration** — script tag query parameters that personalise the SDK and control which funding sources appear
- **Reference** — complete API reference for SDK objects and methods
- **Performance** — optimising SDK load time and button render speed

### Key insight

The `card-fields` component is the distinguishing feature of Expanded Checkout vs Standard Checkout — Standard Checkout only uses `buttons` (and optionally `marks`). Adding `card-fields` requires the Expanded Credit and Debit Card Payments sandbox capability.

## Raw Sources

- [[paypal-javascript-sdk-overview]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout (Standard) — uses `buttons` and `marks`
- [[paypal-expanded-checkout]] — PayPal Expanded Checkout — adds `card-fields`
- [[source-paypal-checkout-display-payment-methods]] — uses `marks` component alongside radio buttons
- [[source-paypal-checkout-standalone-buttons]] — uses `funding-eligibility` component
