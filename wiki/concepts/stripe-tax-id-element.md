---
title: "Stripe Tax ID Element"
type: concept
category: technology
tags: [stripe, elements, tax-id, vat, invoicing, address-element, checkout-sessions, payment-intents, beta]
---

## Definition

The Tax ID Element is a Stripe UI component for collecting customer business tax IDs for tax calculation and invoice display. The April 21, 2026 guide covers Checkout Sessions and Payment Intents and lists 95 country or region codes across six regions; this count is dated, not verified current coverage.

> [!warning] Contradiction: the prior 100+ country and current beta claims exceed the captured evidence. The April 21, 2026 examples show path-specific beta flags, while the November 7 index contains only variant links. Current beta status and flag requirements need the separately linked variant bodies.

## API Paths

The following are **April 21, 2026 captured examples**, not verified current initialization requirements. Checkout Sessions uses `custom_checkout_tax_id_1`; Payment Intents uses `elements_tax_id_1` in that dated code.

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

For the Payment Intents path, the April guide says a `CustomerSession` is required **to save and redisplay** a previously entered tax ID. It does not state that a CustomerSession is required for every Tax ID Element use.

## Visibility Modes

The following visibility, Address Element, and business-name descriptions come from the April 21, 2026 guide; the November index does not verify present-day behavior.

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

95 country or region codes enumerated across six sections in the April 21, 2026 capture (6 + 5 + 44 + 19 + 2 + 19), not a current coverage guarantee:

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

- [[source-stripe-tax-id-element]] — April 21 captured examples for both API paths, listed regions, visibility, and conditional Payment Intents save/redisplay; November 7 variant index linked for navigation
