---
title: "Przelewy24 / P24 (Stripe)"
type: concept
category: technology
tags: [stripe, p24, przelewy24, poland, eur, pln, bank-redirect, authenticated, prohibited-categories]
---

## Definition

Przelewy24 (P24) is a Poland-based **aggregator** of bank transfers and other payment methods. Stripe's May 3, 2026 snapshot labels its family authenticated bank debit. The November 7, 2026 snapshot calls P24 a single-use bank redirect with immediate confirmation, instant provisional access and settlement up to T+2 business days. API enum: `p24`. See [[source-stripe-p24]] for the dated scopes and timing.

**Currency**: EUR or PLN (dual currency — unlike BLIK which is PLN-only). **Customers**: Poland only. **Business**: 40 countries.

## Key Properties

- **Type**: Payment aggregator (multiple underlying payment methods)
- **Recurring**: No
- **Disputes**: No chargebacks (customer authentication)
- **Refunds**: Submit full or partial refunds within 180 days of the original payment. November documents asynchronous refund completion, up to three business days. See [[source-stripe-p24#Refunds and payment references]].
- **Checkout and Invoicing**: May and the November [[source-stripe-bank-redirects|Bank Redirects matrix]] exclude Checkout setup and subscription modes and list Invoicing as invite-only. The November [[source-stripe-p24|P24 overview]] marks Billing and Invoicing supported and prints a `send_invoice` collection note after its matrix. The captures leave individual Invoicing access unresolved.

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

The May 3, 2026 overview says P24 can **suspend or terminate** access for category or site/app violations. The November 7, 2026 overview retains the broad categories and adds a separate MCC table. Some restricted codes overlap with broad prohibitions, for example pawn shops (5933) and car and truck dealers (5511). The capture leaves precedence and individual approval unresolved. Connect marketplace account-type support is separate from the prohibited marketplace MCC (5262). See [[source-stripe-p24#Eligibility and website requirements]].

## Website Requirements

The May 3, 2026 overview requires a publicly accessible website or app displaying the items below. The November 7, 2026 overview adds terms of service and return-policy wording and omits the public-access and priced-list wording without expressly withdrawing it. See [[source-stripe-p24#Eligibility and website requirements]].

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

**Checkout**: The 2026-05-03 acceptance guide lists EUR and PLN compatibility for payment-mode Sessions with same-currency, one-time line items. Its manual `p24` setup instructs using EUR for all line items.

**Statement descriptor.** The May 3, 2026 [[source-stripe-p24-accept-payment|acceptance guide]] specifies a 14-character limit. The bank statement format is `/OPT/X/////P24-XXX-XXX-XXX {descriptor}`. The November overview says to set a custom descriptor on the PaymentIntent before confirmation, with the account-level descriptor as fallback. After completion, expand `latest_charge` to retrieve the payment's P24 reference at `latest_charge.payment_method_details.p24.reference`. The November overview gives no descriptor length. See [[source-stripe-p24]].

**iOS**: `STPPaymentMethodPrzelewy24Params()` + `billing_details.email` + `STPPaymentHandler.confirmPayment()`.

**Android**: `PaymentMethodCreateParams.createP24(billingDetails)` + `PaymentLauncher.confirm()`.

**React Native**: The 2026-05-03 example uses `confirmPayment(clientSecret, { paymentMethodType: 'P24' })`. Its deep-link section describes return handling for methods that require a return URL.

## Sources

- [[source-stripe-p24]] — primary source: properties, prohibited categories, website requirements, disputes, refunds
- [[source-stripe-p24-accept-payment]] — 2026-05-03 acceptance guide for Checkout, iOS, Android, React Native, and legacy Elements, with a 2026-11-07 variant index.
