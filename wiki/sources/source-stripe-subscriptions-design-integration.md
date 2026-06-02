---
title: "Stripe — Design a Subscriptions Integration"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-design-integration-2026.md"
tags: [stripe, subscriptions, billing, pricing-models, checkout, usage-based, freemium, trial]
---

## Summary

Design guide for choosing among pricing models, checkout interfaces, and billing timing for a subscriptions integration. Includes an integration matrix linking combinations to the right implementation guide.

**Note**: 9 CDN images referenced in source (pricing model screenshots, checkout interface previews) — could not be downloaded due to network restrictions.

## 4 Pricing Models

| Model | Subtypes |
| --- | --- |
| **Flat rate** | Fixed price per service tier (monthly/yearly) |
| **Per-seat** | Price per user/seat |
| **Tiered** | Volume-based (applies tier of final quantity) OR Graduated (sums across tiers used) |
| **Usage-based** | Fixed fee + overage; Pay-as-you-go (per unit/package/volume/graduated); Credit burndown (prepaid credits) |

## 7 Checkout Interfaces

| Interface | Notes |
| --- | --- |
| Stripe-hosted page | Redirect to Stripe; 20 fonts, 3 border radiuses, custom colors + logo |
| Embedded payment page | Stripe-hosted but embedded in site; same customization |
| Custom payment form | Elements + Appearance API; full layout control |
| Pricing table | Embeddable; shows multiple pricing tiers; redirects to hosted checkout |
| One-click payment buttons | Express Checkout Element; Link/Apple Pay/Google Pay/PayPal/Klarna/Amazon Pay |
| Payment link | Share URL; not supported for usage-based billing |
| Mobile app | Payment Sheet (prebuilt) or custom; iOS/Android/React Native |

## 3 Billing Models

| Model | When charged |
| --- | --- |
| **Pay up front** | Before access; payment collected at sign-up |
| **Free trial** | PM collected but not charged; billing starts when trial ends |
| **Freemium** | No PM collected initially; PM collected before trial ends; billing starts when trial ends |

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with design decision framework)
- [[source-stripe-subscriptions-overview]] — lifecycle/status guide

## Raw Sources

- [[stripe-subscriptions-design-integration-2026]] — verbatim design guide (167 lines, 9 CDN images not downloaded)
