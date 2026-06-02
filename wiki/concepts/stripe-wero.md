---
title: "Wero (Stripe)"
type: concept
category: technology
tags: [stripe, wero, germany, eur, bank-redirect, authenticated]
---

## Definition

Wero is a pan-European authenticated bank transfer payment method. Customers connect their bank accounts to a Wero wallet and approve payments via the Wero App. API enum: `wero`. Currently available to German customers only.

**Note**: Wero is distinct from [[stripe-ideal]] (iDEAL|Wero) — iDEAL|Wero is the Netherlands' iDEAL method rebranding to Wero infrastructure; this page covers Wero as a standalone German payment method.

**Currency**: EUR only. **Min**: 0.50 EUR. **Max**: varies by customer's bank. **Customers**: Germany. **Business**: 30 European countries.

## Payment Flow

1. Customer selects Wero at checkout
2. Stripe redirects to Wero authentication page
3. Customer scans QR code → launches Wero App on phone
4. Customer approves payment in-app
5. Payment completes (typically under 10 seconds) → customer redirected back

## Key Properties

- **Recurring**: No
- **Disputes**: No
- **Manual capture**: No
- **Refunds**: Full and partial; up to 2 years; multiple partial refunds allowed
- **Connect**: Yes
- **Checkout**: Payment mode only (not subscription or setup mode)
- **Payment Links**: Yes
- **Elements**: Yes (ECE not supported)
- **Onboarding**: Interest form required — not self-serve

## Integration

**Checkout**: `payment_method_types: ['wero']`, `currency: 'eur'`, `mode: 'payment'` only. Listen for `checkout.session.completed`.

**Elements**: `stripe.confirmPayment()` with Payment Element + `return_url`.

**Direct API**: `stripe.confirmWeroPayment(clientSecret, { payment_method: { billing_details: { name, email } }, return_url })` → redirect to Wero auth page.

**Server-side manual**: create PaymentMethod (`type=wero`) + confirm PI → `requires_action` + `next_action.redirect_to_url`.

**Auth session**: expires after **1 hour** → PI reverts to `requires_payment_method`. Always offer `card` as fallback.

**Key error codes**: `payment_intent_invalid_currency`, `payment_method_customer_decline`, `payment_intent_redirect_confirmation_without_return_url`.

## Sources

- [[source-stripe-wero]] — primary source: payment flow, properties, business countries, refunds, limits, product support
- [[source-stripe-wero-accept-payment]] — integration guide: Checkout + Elements + Direct API (confirmWeroPayment), server-side manual path, error codes, 1-hour auth expiry
