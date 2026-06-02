---
title: "Stripe Tax ID Element"
type: concept
category: technology
tags: [stripe, elements, tax-id, vat, invoicing, address-element, checkout-sessions, payment-intents, beta]
---

## Definition

The Tax ID Element is a Stripe UI component for collecting customer business tax IDs. It's used to calculate sales tax accurately and to display tax IDs on invoices. It supports 100+ countries across 6 regions and works with both the Checkout Sessions API and Payment Intents API.

> **Beta**: Both integration paths require a beta flag in the Stripe constructor.

## API Paths

### Checkout Sessions

```js
const stripe = Stripe('PK', { betas: ['custom_checkout_tax_id_1'] });
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const taxIdElement = checkout.createTaxIdElement({ visibility: 'always' });
taxIdElement.mount('#tax-id-element');
```

### Payment Intents

```js
const stripe = Stripe('PK', { betas: ['elements_tax_id_1'] });
const elements = stripe.elements({ clientSecret });
const taxIdElement = elements.create('taxId', { visibility: 'always' });
taxIdElement.mount('#tax-id-element');
```

Payment Intents path requires a `CustomerSession` to save and redisplay a previously entered tax ID.

## Visibility Modes

| Mode | Behavior |
| --- | --- |
| `auto` (default) | Shows only in countries where tax ID collection is common |
| `always` | Always shown regardless of customer location |

**Auto mode detection order**:
1. Country from [[stripe-address-element]] (shipping or billing mode)
2. Customer's IP address (fallback if no Address Element)

When used with the Address Element, Stripe automatically adapts the tax ID type and format to the customer's address.

## Business Name Collection

Optional option — enables a business name field. The collected name appears as the customer name on invoices.

## Supported Regions

100+ countries across 6 regions:

| Region | Countries (count) |
| --- | --- |
| North America | 6 (AW, BB, BS, CA, CR, MX) |
| South America | 5 (CL, EC, PE, SR, UY) |
| Europe | 44 (all EU + UK, CH, NO, RU, UA, and others) |
| Asia | 19 (AE, IN, KR, SA, SG, TH, TR, TW, and others) |
| Oceania | 2 (AU, NZ) |
| Africa | 19 (EG, KE, MA, NG, ZA, ZM, ZW, and others) |

Full list in [[source-stripe-tax-id-element]].

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-tax-id-element]] — primary reference: beta flags, both API paths, visibility logic, supported regions, CustomerSession requirement
