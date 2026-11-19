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
- **Refunds**: Submit full or multiple partial refunds within 180 days; total partial refunds cannot exceed the payment. Submission cannot be canceled. EPS refunds are separate bank credits, typically received in 1–3 days but without a guaranteed maximum. Track `Refund.status` and `refund.updated`/`refund.failed`; after failure, Stripe returns funds to the Stripe balance and the business must refund by another method. See [[source-stripe-eps]] (November 2026).
- **Checkout restrictions**: The May 2026 EPS page excluded Checkout subscription/setup modes; the November 2026 page marks recurring, SetupIntents and off-session payment support unavailable. A `send_invoice` route is not automatic recurring EPS charging.
- **Invoicing**: May 2026 called it invite-only; November marks it supported and adds a `send_invoice`-only footnote whose row attachment is unclear in the text capture. Neither capture proves current account entitlement. Express Checkout Element is unsupported. See [[source-stripe-eps]] for the dated comparison.

## Integration

**Checkout**: `payment_method_types: ['eps']`, `eur`, payment mode only.

**iOS**: `STPPaymentMethodEPSParams()` + billing name + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createEps(billingDetails)` + `PaymentLauncher.confirm()`.

**React Native (dated 2026-05-03 guide)**: The example uses `confirmPayment(clientSecret, { paymentMethodType: 'Eps', paymentMethodData: { billingDetails } })` after collecting a name. Its StripeProvider sample marks `urlScheme` required for 3D Secure and bank redirects, including this EPS bank-redirect path (old raw lines 623-627). A separate section headed “Optional: Handle deep linking” describes a custom URL scheme, forwarding with `handleURLCallback`, and unsupported universal links for that return setup (old raw lines 768-828). This does not establish the same React Native scheme setup for Checkout, iOS, Android, or every payment path. See [[source-stripe-eps-accept-payment]].

**Note**: EPS PaymentMethods are single-use — cannot be saved or reused.

## Sources

- [[source-stripe-eps]] — primary source: properties, payment flow, disputes, refunds
- [[source-stripe-eps-accept-payment]] — 2026-05-03 detailed EPS acceptance guide for Checkout, native SDKs, and legacy Elements, with scoped name collection and outcome checks; the 2026-11-07 base capture is a five-variant navigation index.
