---
title: "Enable Currency Conversion Using the FX Quotes API"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-fx-quotes-api-2025.md"
tags: [stripe, fx-quotes, currency-conversion, localization, payment-intents, exchange-rate, preview]
---

## Summary

Preview API for getting current or time-locked exchange rates to set localized prices. Works with Payment Intents (pass `fx_quote` param). Separate from Adaptive Pricing — FX Quotes gives merchants control over rates and fee pass-through. Gated — requires access request and preview API version.

## Key Facts

- **Preview**: requires API version `2025-03-31.preview` or `2025-07-30.preview` + beta SDK
- **Endpoint**: `POST /v1/fx_quotes` with `to_currency`, `from_currencies[]`, `lock_duration`
- **Available**: 33 countries (all EU + CH, GB, CA, NO, US)
- **Not supported** for certain MCCs; terms of use apply

## Response Fields

| Field | Description |
| --- | --- |
| `rates[currency].exchange_rate` | Rate with FX fee embedded |
| `rates[currency].rate_details.base_rate` | Rate without fee |
| `rates[currency].rate_details.fx_fee_rate` | Fee percentage (e.g. 0.02 = 2%) |
| `rates[currency].rate_details.duration_premium` | Additional fee for locked duration |
| `lock_expires_at` | When the rate expires (Unix timestamp) |
| `lock_status` | `active` or `expired` |

## Lock Durations

| Duration | Cost | Use when |
| --- | --- | --- |
| `none` | Free | Display only; live rate |
| `five_minutes` | Group 1: 0.07%, Group 2: 0.12% | Short checkout flows |
| `hour` | Group 1: 0.10%, Group 2: 0.15% | Standard checkout |
| `day` | Group 1: 0.20%, Group 2: 0.30% | Pre-set prices per day |

**Group 1**: Major currencies (USD, EUR, GBP, JPY, AUD, CAD, CHF, SGD, etc.)
**Group 2**: Emerging market currencies (BRL, CNY, INR, KRW, MXN, PLN, etc.)

If one currency is Group 2, the Group 2 rate applies.

## Price Calculation

```
# Pass FX fee to customer (they pay more)
localized_price = your_price / exchange_rate   # e.g. 100 USD / 1.06053 = 94.29 EUR

# Absorb FX fee yourself
localized_price = your_price / base_rate        # e.g. 100 USD / 1.08295 = 92.34 EUR
```

## Integration with PaymentIntents

```bash
curl /v1/payment_intents \
  -d amount=125 \
  -d currency=usd \
  -d fx_quote=fxq_...   # attach the quote
```

Expired quote → `payment_intent_fx_quote_invalid` error.

## Webhooks

- `fx_quote.expired` → rate drift exceeded threshold; create new quote and update prices
- Mid-market rate fallback: used when extended quote expires for non-card PMs taking >24h

## Important Restrictions

- Disputes/refunds: converted at **current** rate, NOT original locked rate
- Cannot selectively use locked rates only when favorable
- Stripe may add/remove supported currencies without notice
- Not for speculative FX use — must be tied to commercial transactions

## Related Pages

- [[stripe-fx-quotes-api]] — concept page
- [[source-stripe-checkout-local-currency]] — hub page (Adaptive Pricing vs FX Quotes vs Manual)
- [[stripe-adaptive-pricing]] — alternative: automatic currency conversion with 0% merchant fee

## Raw Sources

- [[stripe-fx-quotes-api-2025]] — verbatim FX Quotes API guide
