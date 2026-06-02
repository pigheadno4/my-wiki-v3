---
title: "Stripe Terminal: Save a Card with MOTO for Future Payments"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-moto-save-card-2025.md"
tags: [stripe, terminal, in-person, moto, card, setup-intent, save-card, allow-redisplay, compliance, ios, android, javascript, react-native, server-driven]
---

## Stripe Terminal: Save a Card with MOTO for Future Payments

Integration guide for saving MOTO card details for future use via SetupIntent, across all 5 SDK platforms.

## Key Takeaways

### Flow

1. Create/retrieve Customer
2. Create SetupIntent with `payment_method_types: ['card']`
3. Process SetupIntent with MOTO flag + `allow_redisplay`
4. Charge saved PaymentMethod via standard PaymentIntent

### `allow_redisplay` required

Must pass `allow_redisplay: 'always'` or `'limited'` when processing — controls whether the saved PM can appear in the customer's checkout flow.

### SDK-specific enablement (SetupIntent)

| SDK | How to enable MOTO save |
| --- | --- |
| Server-driven | `process_config.moto: true` on `process_setup_intent` |
| iOS | `MotoConfiguration` on `CollectSetupIntentConfiguration` + `setAllowRedisplay` |
| Android | `MotoConfiguration` on `CollectSetupIntentConfiguration` + `setAllowRedisplay` |
| JavaScript | `config.moto: true` in `collectSetupIntentPaymentMethod` |
| React Native | `motoConfiguration` + `allowRedisplay` on `collectSetupIntentPaymentMethod` |

### Compliance requirements

- Must obtain written customer consent before saving
- Must disclose: purpose of saving, timing/frequency of charges, how amount is determined, cancellation policy
- Must keep records of customer agreement
- Card can only be used for the specific disclosed purpose
- If also showing as saved PM in future checkout: must explicitly collect separate consent (e.g. "Save my payment method" checkbox)

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-moto-save-card-2025]] — verbatim MOTO save-card guide (all 5 platforms)
