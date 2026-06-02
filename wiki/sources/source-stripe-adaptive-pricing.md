---
title: "Stripe Adaptive Pricing"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-local-currency-2025.md"
  - "stripe-checkout-adaptive-pricing-2025.md"
tags: [stripe, adaptive-pricing, local-currency, checkout, payment-links, presentment-currency, international]
---

## Summary

Comprehensive reference for Stripe Adaptive Pricing — the ML-based feature that automatically presents prices in customers' local currencies across 150+ countries. Covers enablement, local payment methods unlocked, presentment_details reporting, testing, restrictions, pricing model, and refunds.

## Key Takeaways

- **150+ countries** supported; machine learning selects presentment currency; exchange rate guaranteed 24 hours from session creation
- **Merchant pays 0%**; customers pay 2–4% conversion fee (Stripe-determined, varies to optimize conversion)
- **Always enabled for Payment Links**; for Checkout managed in Dashboard (dashboard.stripe.com/settings/adaptive-pricing)
- **20 local PMs unlocked**: iDEAL, Bancontact, EPS, P24, Pix, BLIK, Klarna (EU+UK), Amazon Pay, PayPal, Revolut Pay, Samsung/Naver/Kakao/PAYCO Pay, TWINT, WeChat Pay, MB WAY, UPI
- **Cross-border subscriptions**: only cards, Link, Apple Pay, Google Pay supported
- **Objects still reflect integration currency** — `amount_total` + `currency` on session/PaymentIntent remain in your settlement currency
- **`presentment_details`** hash added to `checkout.session.completed` + `payment_intent.succeeded`: `presentment_amount` + `presentment_currency`
- **Refunds**: refund in integration currency → Stripe refunds customer in local currency at original exchange rate, no extra cost

## Local Payment Methods Requiring Local Currency

iDEAL, Bancontact, BLIK, EPS, P24, Pix, Amazon Pay, Link, South Korean cards, MB WAY, Naver Pay, Kakao Pay, PAYCO, PayPal, Revolut Pay, Samsung Pay, TWINT, WeChat Pay, Klarna (EU+UK only), UPI

> Cross-border subscriptions: cards + Link + Apple Pay + Google Pay only.

## Reporting

`presentment_details` appears in:
- `checkout.session.completed` (one-time + subscription first payment)
- `payment_intent.succeeded` (each payment including recurring)
- `customer.subscription.created` (contains `presentment_currency` for future off-session charges)

```json
"presentment_details": {
  "presentment_amount": 1370,
  "presentment_currency": "cad"
}
```

## Testing

Pass `customer_email: 'test+location_XX@example.com'` when creating a Checkout Session (replace `XX` with ISO country code). For Payment Links, use `prefilled_email` URL parameter.

Example: `test+location_FR@example.com` → French customer experience.

## Restrictions

Not available for:
- Elements + Payment Intents API integrations
- Indian businesses
- Sessions with `capture_method: 'manual'`
- Custom amounts (`custom_unit_amount`)
- When local currency already in price's `currency_options` (Adaptive Pricing skips that currency but still converts to others)
- Price currency must be a settlement currency; for platforms, integration currency must be merchant of record's settlement currency

## Supported Countries (150+)

North America (23), South America (9), Europe (44), Asia (39), Oceania (5), Africa (38). Full list in raw file.

## Pricing Model

- Merchant: 0% additional fee
- Customer: 2–4% conversion fee embedded in exchange rate (Stripe determines exact %)
- Customer can avoid fee by choosing integration currency (but their bank may apply exchange fees)
- Exchange rate: mid-market + fee, guaranteed 24 hours through settlement

## Related Pages

- [[stripe-adaptive-pricing]] — Stripe Adaptive Pricing concept page
- [[stripe-checkout]] — Stripe Checkout (Adaptive Pricing is a built-in feature)
- [[stripe-payment-links]] — Payment Links (Adaptive Pricing always enabled)

## Raw Sources

- [[stripe-checkout-local-currency-2025]] — Navigation index: Adaptive Pricing, FX Quotes API, Manual currency prices
- [[stripe-checkout-adaptive-pricing-2025]] — Full Adaptive Pricing reference: 150+ countries, 20 local PMs, presentment_details, testing, restrictions, pricing, refunds
