---
title: "Stripe Payment Element"
type: source
date_ingested: 2026-04-21
original_format: notes
raw_files:
  - "stripe-payment-element-2025.md"
tags: [stripe, payment-element, elements, dynamic-payment-methods, appearance-api, link, express-checkout, layout]
---

## Summary

Reference page for the Stripe Payment Element — the primary UI component for accepting 100+ payment methods. Covers layout options, Appearance API, all 8 options, combining with other elements, dynamic payment methods, and auto-handled error codes.

## Key Takeaways

- **100+ payment methods** with auto-validation and error handling
- **3 layout options**: `tabs`, `accordion` (with/without radio buttons) — set via `layout.type`
- **Appearance API**: themes (`stripe`, `night`, `flat`, `none`) + CSS-level variables
- **8 options**: `layout`, `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `wallets`
- **Dynamic payment methods**: Dashboard-managed; auto-selects by location/currency/amount; auto-hides methods unsupported for the current transaction (wrong currency or payment type)
- **Finland/Sweden regulation**: debit methods must appear before credit methods at checkout
- **Combines with**: Link Authentication Element (contact info) + Address Element (shipping); or Express Checkout Element (wallets only there to avoid duplication)
- **Link legal agreement cannot be removed** — required for compliance
- **17 auto-handled error codes**: card_declined, insufficient_funds, expired_card, etc.

## Layout Options

```javascript
const options = {
  layout: {
    type: 'tabs',       // 'tabs' | 'accordion'
    defaultCollapsed: false,
  }
};
```

| Layout | Description |
| --- | --- |
| `tabs` | Payment methods displayed horizontally as tabs |
| `accordion` (with radio) | Vertically listed with radio buttons |
| `accordion` (no radio) | Vertically listed, no radio buttons |

## Appearance API

```javascript
const appearance = {
  theme: 'flat',   // 'stripe' | 'night' | 'flat' | 'none'
  variables: { colorPrimaryText: '#262626' }
};
```

## All 8 Options

| Option | Description |
| --- | --- |
| `layout` | Layout type (tabs or accordion); accordion default shows 5 methods, rest behind "More"; `visibleAccordionItemsCount: 0` shows all |
| `defaultValues` | Initial customer info to prefill |
| `business` | Business info (e.g., `{ name: "RocketRides" }`) |
| `paymentMethodOrder` | Custom order; `apple_pay` and `google_pay` are valid values; specified methods shown first, rest get dynamic ordering; ignored if method unavailable |
| `fields` | Control billing details collection: `fields.billingDetails.address` (and `name`, `email`) accepts `'auto'` (default), `'never'` (hide + must pass manually at confirm), `'if_required'` (PM-specific; may increase network fees) |
| `readOnly` | Whether payment details can be changed |
| `terms` | Mandate/legal agreement display (default: only when necessary) |
| `wallets` | Show Apple Pay / Google Pay (default: when possible) |

## Combining Elements

```text
Link Authentication Element → contact info (email) + Link autofill
Address Element             → shipping address + Link saved addresses
Payment Element             → payment method selection + details
```

When combined with **Express Checkout Element**: wallets (Apple Pay, Google Pay) appear only in Express Checkout to avoid duplication.

## Auto-Handled Error Codes (17)

`card_declined`, `card_velocity_exceeded`, `expired_card`, `fraudulent`, `generic_decline`, `incorrect_cvc`, `incorrect_number`, `incorrect_zip`, `insufficient_funds`, `invalid_cvc`, `invalid_expiry_month`, `invalid_expiry_year`, `live_mode_test_card`, `lost_card`, `processing_error`, `stolen_card`, `test_mode_live_card`

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page (all 7 elements)
- [[source-stripe-web-elements-overview]] — Elements overview + API comparison

## Raw Sources

- [[stripe-payment-element-2025]] — Payment Element: layout (3 options), Appearance API, 8 options, element combining, dynamic payment methods, 17 auto-handled error codes (4 CDN images)
- [[stripe-payment-element-billing-details-2025]] — Billing details control: auto/never/if_required modes, never requires manual confirm injection, if_required trade-offs
- [[stripe-payment-element-saved-payment-methods-2025]] — Saved PMs: allow_redisplay, CVC re-collection, subscription removal warning, unspecified legacy PMs, consent override
