---
title: "Stripe Tax ID Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-tax-id-element-2025.md"
tags: [stripe, elements, tax-id, vat, invoicing, address-element, checkout-sessions, payment-intents, beta]
---

## Summary

The Tax ID Element is a Stripe UI component for collecting customer business tax IDs (used for tax calculation and VAT display on invoices). It is currently in beta and supports 100+ countries. It works with both the Checkout Sessions API and Payment Intents API.

## Key Takeaways

- **Beta feature**: requires beta flag on both API paths
- **Visibility modes**: `auto` (default — shows only for supported countries) or `always`
- **Auto mode detection**: checks Address Element country first, falls back to IP address
- **Address Element integration**: automatically adapts tax ID type and visibility to customer's address
- **Business name collection**: optional; collected name appears as customer name on invoices
- **CustomerSession required** (Payment Intents path) to save and redisplay a previously entered tax ID

## Initialization

### Checkout Sessions API

```js
const stripe = Stripe('PK', { betas: ['custom_checkout_tax_id_1'] });
const checkout = stripe.initCheckoutElementsSdk({ clientSecret, elementsOptions });
const taxIdElement = checkout.createTaxIdElement({ visibility: 'always' });
taxIdElement.mount('#tax-id-element');
```

### Payment Intents API

```js
const stripe = Stripe('PK', { betas: ['elements_tax_id_1'] });
const elements = stripe.elements({ clientSecret, appearance });
const taxIdElement = elements.create('taxId', { visibility: 'always' });
taxIdElement.mount('#tax-id-element');
```

To save/redisplay a tax ID on the Payment Intents path, create a `CustomerSession`.

## Visibility Logic

| Visibility | Behavior |
| --- | --- |
| `auto` (default) | Shows only in countries where tax ID collection is common; checks Address Element → IP address |
| `always` | Always shown regardless of country |

## Supported Regions (summary)

- **North America**: AW, BB, BS, CA, CR, MX
- **South America**: CL, EC, PE, SR, UY
- **Europe**: 44 countries including all EU member states + UK, CH, NO, RU, UA, and others
- **Asia**: AE, BD, BH, IN, KR, SA, SG, TH, TR, TW, and others (19 total)
- **Oceania**: AU, NZ
- **Africa**: AO, EG, KE, MA, NG, ZA, ZM, ZW, and others (19 total)

Full country list in raw file.

## Options

| Option | Description |
| --- | --- |
| `visibility` | `'auto'` or `'always'` |
| Business name | Enable via option — appears as customer name on invoices |

## Related Pages

- [[stripe-tax-id-element]] — concept page
- [[stripe-address-element]] — works with Tax ID Element for automatic location detection
- [[stripe-tax]] — Stripe's automatic tax calculation
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page

## Raw Sources

- [[stripe-tax-id-element-2025]] — verbatim Stripe docs webpage
