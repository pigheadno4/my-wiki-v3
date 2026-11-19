---
title: "Stripe Adaptive Pricing"
type: concept
category: technology
tags: [stripe, adaptive-pricing, local-currency, checkout, payment-links, presentment-currency, international, fx]
---

## Stripe Adaptive Pricing

ML-based feature that automatically presents prices in customers' local currencies at checkout. Covers 150+ countries. Stripe handles currency selection, conversion, exchange rate guarantees, and compliance. Zero additional cost to merchants.

## How It Works

1. Customer visits Checkout or Payment Link
2. Stripe ML selects most relevant presentment currency based on customer location
3. Price automatically converted at mid-market rate + 2–4% fee (guaranteed 24h)
4. Customer sees local price; can opt to pay in integration currency instead (avoiding Adaptive Pricing fee)
5. After payment: session/PaymentIntent objects reflect integration currency; `presentment_details` hash shows what customer actually paid

## Enablement

- **Payment Links**: always enabled, cannot be disabled
- **Checkout (hosted)**: managed in Dashboard → [Adaptive Pricing settings](https://dashboard.stripe.com/settings/adaptive-pricing)
- **Elements (Checkout Sessions API)**: Dashboard OR `adaptive_pricing.enabled` per session; **additionally requires** `adaptivePricing: { allowed: true }` in `initCheckoutElementsSdk` options to mark the integration as ready
- Disabling doesn't affect already-converted sessions or active local-currency subscriptions

## Pricing

| | Cost |
| --- | --- |
| Merchant | 0% additional |
| Customer | 2–4% embedded in exchange rate (Stripe-determined) |

Customer avoids fee by choosing integration currency (but their bank may apply exchange fees).

## Local Payment Methods Unlocked

Adaptive Pricing unlocks 20 payment methods that require local currency presentation:

iDEAL · Bancontact · BLIK · EPS · P24 · Pix · Amazon Pay · Link · South Korean cards · MB WAY · Naver Pay · Kakao Pay · PAYCO · PayPal · Revolut Pay · Samsung Pay · TWINT · WeChat Pay · Klarna (EU+UK) · UPI

> Cross-border subscriptions: only cards, Link, Apple Pay, Google Pay.

## Reporting

`presentment_details` hash added to events when customer pays in local currency:

- `checkout.session.completed` → `presentment_amount` + `presentment_currency`
- `payment_intent.succeeded` → `presentment_amount` + `presentment_currency`
- `customer.subscription.created` → `presentment_currency` (used for future off-session charges)

Session/PaymentIntent `amount_total` and `currency` always remain in integration currency.

## Testing

Pass `customer_email: 'test+location_XX@example.com'` on session create (replace `XX` with ISO country code, e.g. `FR` for France). For Payment Links, use `prefilled_email` URL parameter.

## Restrictions

Not supported for:
- Elements + Payment Intents API integrations
- Indian businesses
- `capture_method: 'manual'`
- `custom_unit_amount` (pay-what-you-want)
- When local currency already in price `currency_options` (that currency skipped, others still converted)
- Price currency must be a settlement currency

## Supported Coverage

150+ countries across 6 regions: North America (23), South America (9), Europe (44), Asia (39), Oceania (5), Africa (38).

## Refunds

Refund in integration currency → Stripe automatically refunds customer in their local currency at the original exchange rate. No extra cost to merchant or customer.

## Sources

- [[source-stripe-adaptive-pricing]] — Full reference: 150+ countries, 20 local PMs, presentment_details, testing, restrictions, pricing, refunds
- [[source-stripe-adaptive-pricing-elements]] — Elements integration guide: adaptivePricing.allowed flag, CurrencySelectorElement React component, currencyOptions guard, +location_XX testing
