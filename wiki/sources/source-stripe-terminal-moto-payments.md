---
title: "Stripe Terminal: Process MOTO Payments (All SDK Platforms)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-moto-payments-2025.md"
tags: [stripe, terminal, in-person, moto, card, paymentintents, ios, android, javascript, react-native, server-driven]
---

## Stripe Terminal: Process MOTO Payments (All SDK Platforms)

Integration guide for MOTO payment collection across all 5 Terminal SDK platforms.

## Key Takeaways

### PaymentIntent: `card` not `card_present`

```javascript
payment_method_types: ['card']  // MOTO uses 'card', NOT 'card_present'
```

### SDK-specific MOTO enablement

| SDK | How to enable MOTO |
| --- | --- |
| Server-driven | `process_config.moto: true` on `processPaymentIntent` |
| iOS | `MotoConfiguration` on `CollectPaymentIntentConfiguration` |
| Android | `MotoConfiguration` on `CollectPaymentIntentConfiguration` |
| JavaScript | `config_override.moto: true` in `collectPaymentMethod` |
| React Native | `motoConfiguration` on `collectPaymentMethod` |

### CVC requirement

CVC is **mandatory** for MOTO. Skipping CVC is private preview (mail orders only) — contact Stripe support.

### Cart display conflict

If using `setReaderDisplay` (cart line items), must reset display to splash screen **before** collecting a MOTO payment.

### Rest of flow

After collection, standard confirm + capture flow applies (same as regular Terminal payments).

### Testing

Simulated reader + simulated test cards work for MOTO testing.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-moto-payments-2025]] — verbatim MOTO payment processing guide (all 5 platforms)
