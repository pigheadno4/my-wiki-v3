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
| Merchant fee | FX fee can be absorbed by merchant using `base_rate` or passed to customer using `exchange_rate`; extended locks add duration premium | 0% |
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
- **Group 2**: Currencies including BRL, CNY, KRW, MXN and PLN (INR belongs to Group 1).
- If one currency is Group 2, the Group 2 rate applies

## Integration Pattern

```bash
# 1. Get quote
POST /v1/fx_quotes
  to_currency=gbp
  from_currencies[]=usd
  lock_duration=hour

# 2. Set localized price using exchange_rate or base_rate

# 3. Attach to PaymentIntent (illustrative fields only)
POST /v1/payment_intents
  amount=<integer minor units for the USD price>
  currency=usd
  fx_quote=fxq_...
```

**Example caveat:** both captured guides say 125 USD in prose but send `amount=125`, which is 125 cents for USD. Their quote prose says `hour` while curl sends `lock_duration=day`. Compute minor units and use the intended lock duration before implementing.

## Expired Quotes

A quote can expire at `lock_expires_at` or be invalidated early by significant rate drift; `lock_status` becomes `expired` and `fx_quote.expired` can notify either case. Attaching an expired quote to a PaymentIntent or Transfer returns HTTP 400 with `payment_intent_fx_quote_invalid` or `transfers_fx_quote_invalid`, respectively. Create a new quote and update prices; a mid-market fallback is limited to some non-card methods that take more than 24 hours.

Mid-market rate fallback: the captures limit it to some non-card payment methods taking more than 24 hours when an extended quote expires or can no longer be applied.

## Key Restrictions

- Disputes/refunds use **current** rate, not original locked rate
- Cannot selectively use locked rates only when favorable (terms of use)
- Preview availability: the 2026-04-21 capture gave a flat list of 33 countries; the 2026-11-07 capture replaces it with an 18-region matrix by payment versus transfer usage and duration. BR, IN, JP, MY and TH have payment locks but no transfer support; day appears for payment in CA, EU, GI, NO, CH, GB and US, and nowhere for transfer. `none` informational quotes follow supported usage types. The EU aggregate row does not establish withdrawal of earlier individually listed EU countries or any merchant's access.
- Certain MCCs not supported
- Preview access and versioned examples: Ruby beta SDK shows `2025-07-30.preview`; direct secret-key curl sends `Stripe-Version: 2025-03-31.preview`. These are distinct integration examples, not proof of cross-surface version interchangeability or beta SDK requirement for direct curl.

## Key Players

- [[stripe]] — the sole provider of this API

## Sources

- [[source-stripe-fx-quotes-api]] — primary reference: preview FX rates, payment/transfer duration matrix, fee groups, versioned examples, minor-unit and expiry caveats
