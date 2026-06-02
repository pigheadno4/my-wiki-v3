---
title: "PayPal Foreign Exchange as a Service (FXaaS): Overview"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-fxaas-overview.md"
  - "paypal-fxaas-get-started.md"
  - "paypal-fxaas-integrate.md"
  - "paypal-fxaas-reference.md"
tags: [paypal, fxaas, foreign-exchange, currency-conversion, multi-currency, orders-api, pricing]
---

## PayPal Foreign Exchange as a Service (FXaaS): Overview

Overview of PayPal's FXaaS — a currency conversion service allowing merchants to display prices and accept payments in buyers' local currencies, with rate locking and FX risk protection. Requires contract approval.

Source URL: <https://developer.paypal.com/docs/checkout/fx-as-a-service/>

Last updated: 2025-10-27

## Key Takeaways

### What it is

FXaaS is a **contract-based** currency conversion service integrated into PayPal's Orders v2 API flow. Merchants request an exchange rate, PayPal locks it, and the locked rate is applied when the buyer pays — protecting merchants from FX volatility between rate request and payment capture.

### Key capabilities

- Display prices in **100+ local currencies**
- Hold funds in **25 different currencies**
- Rate locking: exchange rate locked at request time, verified at payment time
- FX markup: merchants/partners can add their own markup on top of PayPal's FX fee
- FX risk protection: locked rate insulates merchant from volatility

### How it works (8-step flow)

1. Merchant requests exchange rate for a currency pair (base → quote)
2. PayPal returns the rate (including FX fee + optional merchant markup) and **locks the rate**
3. Merchant caches the locked rate
4. Buyer visits the purchase page
5. Merchant displays price in buyer's local currency using cached rate
6. Buyer selects product, proceeds to checkout, pays in local currency
7. Merchant sends transaction details to PayPal
8. PayPal: verifies locked rate is still valid → applies locked rate → converts → deducts fees → settles in merchant's base currency

### Eligibility

- **Requires contract approval** — not self-serve
- New merchants: contact PayPal to request FXaaS
- Existing merchants: contact Account Manager
- Contract defines: rate expiration interval, PayPal rate refresh time, FX fees, other terms

### Compatible payment methods

FXaaS works with any payment method that uses the Orders v2 API:

- PayPal wallet
- Advanced credit and debit cards (Expanded Checkout)
- Apple Pay
- Google Pay

### Partner-specific

Partners can choose between immediate and delayed disbursement payout models with FXaaS.

### Currency type definitions

| Term | Definition | Hold balance? | Use as base? | Use as quote? |
| ---- | ---------- | ------------- | ------------ | ------------- |
| **Primary currency** | Default settlement currency | Yes | Yes | Yes |
| **Holding currency** | Currencies merchant can hold | Yes | Yes | Yes |
| **Presentment currency** | Display-only currencies | No | **No** | Yes |

Key rule: **base currency must be a holding currency** — presentment currencies can only be quote (buyer-side).

### Currency reference

**Settlement (base) currencies**: 24 — AUD, BRL*, CAD, CNY*, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY, MXN, MYR*, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD, USD, CHF

*BRL, CNY, MYR: in-country accounts only — outside-country auto-converts to primary currency

**Quote (presentment) currencies**: ~100+, including many emerging-market currencies (full table in raw file)

Notable edge cases:

- **BGN deprecated Jan 1, 2026** → use EUR for Bulgaria
- **MGA (Malagasy Ariary)**: 2-decimal format but amounts must be multiples of 0.20 — auto-rounded

### Integration: 4-step API flow

1. **`POST /v2/pricing/quote-exchange-rates`** → get `fx_id` + locked rate
2. **`POST /v2/checkout/orders`** with `payment_instruction.payee_receivable_fx_rate_id: fx_id` → create order in quote currency
3. **Buyer approves** via HATEOAS `approve` link
4. **`POST /v2/checkout/orders/{id}/capture`** (empty payload) → PayPal applies locked rate, settles in base currency

**Rate validity**: valid until `rate_refresh_time`; `expiry_time` adds a 3-hour grace period (standard; negotiable). Without `payee_receivable_fx_rate_id` in the create order request, `expiry_time` grace period is ignored.

**PayPal fee currency**: charged in the **buyer's (quote) currency**, not the merchant's base currency.

**Market-moving event**: `422 FX_RATE_CHANGE_DUE_TO_MARKET_EVENT` with HATEOAS `rel: new_fx_id` link → fetch new quote, re-display prices, re-create order. Edge case: subsequent Create order with old `fx_id` silently returns 200 with the new `fx_id` applied.

### Account configuration (production)

- Primary currency: Account Settings → Money, Banks, and Card → Currency Management
- Holding currencies: same location — add/remove as needed
- Payment receiving preferences: if buyer pays in a non-holding currency, payment stays **pending** until manually approved unless auto-convert to primary is enabled

## Raw Sources

- [[paypal-fxaas-overview]] — verbatim webpage content with FXaaS workflow diagram
- [[paypal-fxaas-get-started]] — key terms (primary/holding/presentment/base/quote currencies), account configuration steps, payment receiving preferences
- [[paypal-fxaas-integrate]] — integration: /v2/pricing/quote-exchange-rates API, fx_id → payee_receivable_fx_rate_id, rate validity rules, capture response breakdown, FX_RATE_CHANGE_DUE_TO_MARKET_EVENT handling
- [[paypal-fxaas-reference]] — currency code tables: ~100 quote currencies, 24 settlement currencies; BGN deprecated (Jan 2026 → EUR); MGA multiples-of-0.20 rule; BRL/CNY/MYR in-country restriction

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout (one of the compatible payment methods)
- [[source-paypal-expanded-checkout-eligibility]] — country/currency eligibility for Expanded Checkout
