---
title: "EPS (Stripe)"
type: concept
category: technology
tags: [stripe, eps, austria, eur, bank-redirect, authenticated]
---

## Definition

EPS (Electronic Payment Standard) is Austria's dominant online bank redirect payment method. All Austrian banks support it. API enum: `eps`. Customer-authenticated, redirect-based, immediate notification.

**Currency**: EUR only. **Customers**: Austria only. **Business**: 40 countries.

## Payment Flow

1. Customer selects EPS at checkout
2. Selects their bank → redirected to bank's login page
3. Enters bank credentials
4. Completes scanner or SMS authorization
5. Immediate payment confirmation
6. Optional return to merchant site

## Key Properties

- **Confirmation**: Customer-authenticated, immediate notification
- **Recurring**: No — single-use only
- **Disputes**: No chargebacks (customer authenticates with bank)
- **Refunds**: Up to 180 days
- **Checkout restrictions**: Not in subscription or setup mode
- **Invoicing**: Invite-only; ECE: not supported

## Integration

**Checkout**: `payment_method_types: ['eps']`, `eur`, payment mode only.

**iOS**: `STPPaymentMethodEPSParams()` + billing name + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createEps(billingDetails)` + `PaymentLauncher.confirm()`.

**React Native**: `confirmPayment(clientSecret, { paymentMethodType: 'Eps' })` + deep linking required.

**Note**: EPS PaymentMethods are single-use — cannot be saved or reused.

## Sources

- [[source-stripe-eps]] — primary source: properties, payment flow, disputes, refunds
- [[source-stripe-eps-accept-payment]] — integration guide: Checkout + iOS + Android + React Native + Elements (legacy)
