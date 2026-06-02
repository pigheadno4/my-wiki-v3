---
title: "PayPal Foreign Exchange as a Service (FXaaS)"
type: concept
category: technology
tags: [paypal, fxaas, foreign-exchange, currency-conversion, multi-currency, rate-locking, fx-risk]
---

## PayPal Foreign Exchange as a Service (FXaaS)

PayPal FXaaS is a contract-based currency conversion service that lets merchants display prices and accept payments in buyers' local currencies, with locked exchange rates applied at settlement.

## What it is

FXaaS sits between the merchant's pricing layer and PayPal's Orders v2 API. The merchant requests a rate, PayPal locks it, the buyer pays in their local currency, and PayPal settles in the merchant's base currency using the locked rate.

Key differentiator: **rate locking** — the exchange rate is guaranteed from the moment the merchant requests it until the payment is captured (within the contract's expiration interval), protecting against FX volatility.

## Key Numbers

- **100+** local currencies for display pricing
- **25** currencies for holding funds
- Rate refresh time and expiration interval defined by **contract** (varies by merchant)

## How It Works

```text
Merchant requests rate (base/quote pair)
→ PayPal locks rate + includes FX fee + optional merchant markup
→ Merchant caches locked rate
→ Buyer sees price in local currency
→ Buyer pays → Merchant submits to PayPal
→ PayPal verifies locked rate → converts → settles in merchant's base currency
```

## Eligibility

- **Not self-serve** — requires contract with PayPal
- New merchants: contact PayPal sales
- Existing merchants: contact Account Manager
- Contract defines: rate expiration interval, rate refresh time, FX fees

## Compatible Payment Methods

Any Orders v2 API payment method:

- PayPal wallet
- Advanced credit/debit cards (Expanded Checkout)
- Apple Pay
- Google Pay

## Partner Considerations

Partners can implement **immediate or delayed disbursement** payout models with FXaaS.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-paypal-fxaas-overview]] — FXaaS overview: workflow, eligibility, compatible payment methods
