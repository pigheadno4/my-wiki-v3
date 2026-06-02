---
title: "Stripe Checkout: Customize Card Brands"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-card-brands-2025.md"
tags: [stripe, checkout, card-brands, brands-blocked, link, apple-pay, google-pay, co-badged-cards]
---

## Summary

How to block specific card brands from Stripe Checkout using the `brands_blocked` parameter. Applies to both hosted and embedded Checkout modes.

## Key Takeaways

- **`payment_method_options.card.restrictions.brands_blocked`**: array of brand values to block
- **4 blockable brands**: `visa`, `mastercard`, `american_express`, `discover_global_network`
- **`discover_global_network`** covers Discover, Diners, JCB, UnionPay, and Elo
- **Filtering scope**: card entry form, Link saved cards (disabled if blocked), Apple Pay / Google Pay wallets, customer saved payment methods, co-badged card networks

## API

```javascript
payment_method_options: {
  card: {
    restrictions: {
      brands_blocked: ['american_express'],
    },
  },
},
```

Hosted: use with `success_url`. Embedded: use with `return_url` + `ui_mode: 'embedded_page'`. Logic is identical across both modes.

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-appearance]] — Checkout branding and appearance customization

## Raw Sources

- [[stripe-checkout-card-brands-2025]] — Card brand blocking: 4 blockable brands, brands_blocked param, filtering scope (Link/Apple Pay/Google Pay/saved PMs/co-badged), 2 PNG screenshots
