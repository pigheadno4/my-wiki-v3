---
title: "Wero (Stripe)"
type: concept
category: technology
tags: [stripe, wero, germany, eur, bank-redirect, authenticated]
---

## Definition

Wero (`wero`) is a standalone pan-European authenticated bank transfer method. Customers connect a bank account to their Wero wallet and approve in the app. The May 5, 2026 method overview listed German customers. November 7 lists Belgium, France, Germany, Luxembourg and the Netherlands, separately from the unchanged 30 listed Stripe account countries. The cross-method overview labels Wero public preview. The separately documented [[stripe-ideal|iDEAL/Wero]] route uses `ideal` and has its own dated migration guidance.

**Amount and currency.** EUR only, with a EUR 0.50 minimum and a maximum that varies by the customer's bank. See [[source-stripe-wero]].

## Payment Flow

1. Customer selects Wero at checkout
2. Stripe redirects to Wero authentication page
3. Customer scans QR code → launches Wero App on phone
4. Customer approves payment in-app
5. Payment completes (typically under 10 seconds) → customer redirected back

## Key Properties

- **Recurring**: No
- **Disputes**: No
- **Manual capture.** The May method overview says No and November says Yes. The November overview gives no capture procedure or authorization window.
- **Refunds.** Full and partial refunds are documented, with multiple partial refunds up to the original amount. May states up to two years and November specifies 730 days from payment.
- **Connect.** Both method overviews list support. November also lists prohibited or restricted categories, including payment facilitators processing for sub-merchants.
- **Checkout**: Payment mode only (not subscription or setup mode)
- **Payment Links**: Yes
- **Elements**: Yes (ECE not supported)
- **Onboarding.** Both guides describe Dashboard enablement. May invites contact via an interest form and November omits the invitation. The separate November cross-method overview lists public preview.

## Integration

**Checkout**: `payment_method_types: ['wero']`, `currency: 'eur'`, `mode: 'payment'` only. Listen for `checkout.session.completed`.

**Elements**: `stripe.confirmPayment()` with Payment Element + `return_url`.

**Direct API**: `stripe.confirmWeroPayment(clientSecret, { payment_method: { billing_details: { name, email } }, return_url })` → redirect to Wero auth page.

**Server-side manual**: create PaymentMethod (`type=wero`) + confirm PI → `requires_action` + `next_action.redirect_to_url`.

**Auth session** — The May 2026 acceptance guide gives one hour for authentication. A failed or expired PaymentIntent returns to `requires_payment_method`. Offer another payment method for retry, with card given as an example. See [[source-stripe-wero-accept-payment]].

**Key error codes**: `payment_intent_invalid_currency`, `payment_method_customer_decline`, `payment_intent_redirect_confirmation_without_return_url`.

## Sources

- [[source-stripe-wero]] — primary source: payment flow, properties, business countries, refunds, limits, product support
- [[source-stripe-wero-accept-payment]] — May 2026 Checkout, web Elements and Direct API guide with return-path and retry details. The November 2026 selector links six implementation routes.
