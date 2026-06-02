---
title: "Przelewy24 / P24 (Stripe)"
type: concept
category: technology
tags: [stripe, p24, przelewy24, poland, eur, pln, bank-redirect, authenticated, prohibited-categories]
---

## Definition

Przelewy24 (P24) is Poland's dominant online payment **aggregator** — it aggregates multiple bank transfer methods and other payment types, not just a single bank redirect. API enum: `p24`. Customer-authenticated redirect, immediate notification.

**Currency**: EUR or PLN (dual currency — unlike BLIK which is PLN-only). **Customers**: Poland only. **Business**: 40 countries.

## Key Properties

- **Type**: Payment aggregator (multiple underlying payment methods)
- **Recurring**: No
- **Disputes**: No chargebacks (customer authentication)
- **Refunds**: 180 days
- **Checkout**: Not in subscription/setup mode; Invoicing: invite-only

## Prohibited Business Categories

P24 prohibits (in addition to Stripe's general prohibited list):

1. Dropshipping
2. Automotive sales, services, and rentals
3. Specialty food retail
4. Pawn shops
5. Higher education and vocational training
6. Healthcare providers and medical services
7. Entertainment and event promotion
8. IT and telecommunications services
9. Advertising agencies and marketing services
10. Real estate management and brokerage

P24 can **suspend or terminate** access for violations.

## Website Requirements

P24 requires your website to publicly display:

- Products/services list with prices
- Company legal details: address, tax number, registration number
- Refund policy and privacy policy links

## vs BLIK

| | P24 | BLIK |
| --- | --- | --- |
| Currency | EUR or PLN | PLN only |
| Type | Aggregator (multiple methods) | Single 6-digit code |
| Recurring | No | Private preview |
| Redirect | Yes | No redirect |
| Prohibited categories | 10 specific | None listed |
| Website requirements | Extensive | None listed |

## Integration

**Checkout**: `payment_method_types: ['p24']`, EUR or PLN. **Email required** in billing details.

**Statement descriptor**: max 14 chars; format `/OPT/X/////P24-XXX-XXX-XXX {descriptor}` on bank statement.

**iOS**: `STPPaymentMethodPrzelewy24Params()` + `billing_details.email` + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createP24(billingDetails)` + `PaymentLauncher.confirm()`.

**React Native**: `confirmPayment(clientSecret, { paymentMethodType: 'P24' })` + deep linking.

## Sources

- [[source-stripe-p24]] — primary source: properties, prohibited categories, website requirements, disputes, refunds
- [[source-stripe-p24-accept-payment]] — integration guide: Checkout + iOS + Android + React Native + Elements legacy, email required, 14-char descriptor
