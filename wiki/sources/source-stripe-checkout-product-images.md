---
title: "Stripe Checkout: Add Product Images"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-product-images-2025.md"
tags: [stripe, checkout, products, images, product-data, conversion]
---

## Summary

How to add product images and descriptions to Stripe Checkout line items — via Dashboard, Product API, or inline `product_data`. Stripe recommends this to drive higher conversion.

## Key Takeaways

- **2 approaches**: pre-create Product with `images` param, or use inline `price_data.product_data.images` per Checkout Session
- **Inline `product_data`**: useful for dynamic or one-off products — no need to pre-create a Product object
- Image + description display next to each line item on the checkout page
- Same logic applies to hosted and embedded Checkout modes

## API Patterns

**Pre-created product** (reference by price ID):
```javascript
stripe.products.create({
  name, description,
  images: ['https://example.com/image.png'],
  default_price_data: { unit_amount, currency },
});
// Then reference price ID in Checkout Session
```

**Inline product data** (dynamic/one-off):
```javascript
line_items: [{
  price_data: {
    unit_amount, currency,
    product_data: { name, description, images: ['https://...'] },
  },
  quantity: 1,
}]
```

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-products-prices]] — Products & Prices API
- [[source-stripe-checkout-appearance]] — Checkout branding and appearance

## Raw Sources

- [[stripe-checkout-product-images-2025]] — Add product images: Dashboard steps, products.create images param, inline price_data.product_data, conversion recommendation
