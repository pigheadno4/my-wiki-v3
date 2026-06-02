---
title: "Stripe FX Quotes API"
type: concept
category: technology
tags: [stripe, fx-quotes, currency-conversion, localization, payment-intents, exchange-rate, preview]
---

## Definition

The FX Quotes API is a Stripe preview feature that gives merchants access to current or time-locked exchange rates for currency pairs. Unlike Adaptive Pricing (which auto-converts with 0% merchant fee), FX Quotes lets merchants control which currencies to localize, whether to pass the FX fee to customers, and how long a rate is locked.

## When to Use vs Adaptive Pricing

| | FX Quotes API | Adaptive Pricing |
| --- | --- | --- |
| Rate control | Merchant sets prices using API rates | Stripe auto-converts |
| Merchant fee | 0% (pay duration premium only) | 0% |
| Customer fee | Optional — can absorb or pass on | 2–4% always |
| Integration | Manual (PaymentIntent + fx_quote param) | Declarative (Dashboard + adaptivePricing flag) |
| API | Payment Intents | Checkout Sessions |
| Status | Preview (gated) | GA |

## Price Calculation

```
# Pass FX fee to customer
localized_price = your_price / exchange_rate   # includes Stripe fee

# Absorb FX fee
localized_price = your_price / base_rate       # excludes Stripe fee
```

## Lock Durations

| Duration | Cost (Group 1) | Cost (Group 2) |
| --- | --- | --- |
| `none` | Free (live rate) | Free |
| `five_minutes` | 0.07% | 0.12% |
| `hour` | 0.10% | 0.15% |
| `day` | 0.20% | 0.30% |

- **Group 1**: Major currencies (USD, EUR, GBP, JPY, AUD, CAD, CHF, SGD, etc.)
- **Group 2**: Emerging market currencies (BRL, CNY, INR, KRW, MXN, PLN, etc.)
- If one currency is Group 2, the Group 2 rate applies

## Integration Pattern

```bash
# 1. Get quote
POST /v1/fx_quotes
  to_currency=gbp
  from_currencies[]=usd
  lock_duration=hour

# 2. Set localized price using exchange_rate or base_rate

# 3. Attach to PaymentIntent
POST /v1/payment_intents
  amount=125
  currency=usd
  fx_quote=fxq_...
```

## Expired Quotes

When a quote expires due to market drift, `lock_status` becomes `expired`. Using an expired quote on a PaymentIntent returns `payment_intent_fx_quote_invalid`. Subscribe to `fx_quote.expired` webhook to create a new quote and update prices.

Mid-market rate fallback: applies to non-card PMs taking >24h to process when extended quote expires.

## Key Restrictions

- Disputes/refunds use **current** rate, not original locked rate
- Cannot selectively use locked rates only when favorable (terms of use)
- Available in 33 countries: all EU + CH, GB, CA, NO, US
- Certain MCCs not supported
- Preview: requires API version `2025-03-31.preview` or `2025-07-30.preview`

## Key Players

- [[stripe]] — the sole provider of this API

## Sources

- [[source-stripe-fx-quotes-api]] — primary reference: rate fields, lock durations, pricing tiers, integration, webhooks, restrictions
