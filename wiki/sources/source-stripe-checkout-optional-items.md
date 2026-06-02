---
title: "Stripe Checkout: Configure Optional Items"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-optional-items-2025.md"
tags: [stripe, checkout, optional-items, cross-sells, add-ons, checkout-sessions]
---

## Summary

Guide for configuring optional items in Stripe Checkout — complementary products customers can add to their order during checkout. Covers `optional_items` API, adjustable quantities, cross-sells (product catalog-based auto-items), and a comprehensive limitations list.

## Key Takeaways

- **`optional_items`**: array on session create, same structure as `line_items` (`price`, `quantity`); up to 10 items
- **`adjustable_quantity`**: supported on optional items (same params as line items); customers can always remove even if `minimum > 0`
- **Cross-sells**: product catalog-based; configure on Product details → Cross-sells; auto-appear on eligible sessions; **do not appear if `optional_items` is explicitly set on session**

## API

```js
stripe.checkout.sessions.create({
  line_items: [{ price: '...', quantity: 1 }],
  optional_items: [
    { price: '...', quantity: 1 },
    {
      price: '...', quantity: 1,
      adjustable_quantity: { enabled: true, minimum: 0, maximum: 10 }
    },
  ],
})
```

## Cross-Sells

Configure on Product catalog → Product details → Cross-sells. Auto-appear as optional items on eligible sessions containing that product. Two limitations:
- Cross-sell items won't appear if `optional_items` is explicitly specified on the session
- Cross-sells won't appear if additional `optional_items` are set on a payment link

## Limitations

| Limitation | Notes |
| --- | --- |
| Max items | 10 |
| Recurring + upsells | Incompatible — recurring optional items not supported when line item has subscription upsell |
| Custom amounts | Incompatible in both directions |
| `setup` mode | Not supported |
| Recurring in `payment` mode | Not supported |
| Billing interval | Recurring optional items must match line item billing interval |
| Cross-sell + optional_items | Cross-sells won't appear when `optional_items` is set on session |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page

## Raw Sources

- [[stripe-checkout-optional-items-2025]] — Optional items: optional_items API, adjustable_quantity, cross-sells, full limitations table (2 video assets)
