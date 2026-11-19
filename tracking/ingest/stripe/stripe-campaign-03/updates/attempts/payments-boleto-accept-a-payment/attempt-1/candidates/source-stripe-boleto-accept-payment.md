---
title: "Stripe: Accept a Boleto Payment"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/boleto/accept-a-payment"
raw_files:
  - "stripe-boleto-accept-payment-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, checkout, elements, direct-api, webhooks, expires-after-days]
---

## Overview

The 2026-05-07 Boleto guide covers four ways to create and display a Brazil/BRL cash voucher: hosted or embedded Checkout, Elements with the Checkout Sessions API, Elements with the Payment Intents API, and Direct API. Voucher creation, customer payment, later payment notification, and funds availability are separate states. The 2026-11-07 capture at the canonical URL is a variant navigation index with no integration instructions; the behavior below remains dated May evidence. See [[stripe]] and [[stripe-vouchers]].

## Key details from the 2026-05-07 guide

- **Compatibility and expiry:** The Checkout and Checkout Sessions API variants list supported business location Brazil, currency and presentment BRL, payment and subscription modes, but no setup mode. Their line items must use one currency. The Direct API section says Stripe users in Brazil can accept Boleto from customers in Brazil. Checkout and Direct API allow optional `payment_method_options.boleto.expires_after_days` from 0 to 60 calendar days, default 3, with expiry at 23:59 America/Sao_Paulo; the account default can be adjusted in Dashboard. Those are May-capture rules, not current account eligibility findings.
- **Hosted or embedded Checkout:** The server creates a Checkout Session with BRL line items and Boleto enabled, either by the illustrated manual `payment_method_types` list or a dynamic-method integration. After submitting the form, the Boleto customer goes to `hosted_voucher_url`, not `success_url`. `checkout.session.completed` means the voucher was generated and the merchant can resend its link; it does not mean the customer paid. `checkout.session.async_payment_succeeded` follows payment and supports fulfillment. `checkout.session.async_payment_failed` covers expiry **or another failure** and the PaymentIntent returns to `requires_payment_method`.
- **Elements with Checkout Sessions API:** The server creates a Checkout Session with `ui_mode: 'elements'` and returns its client secret. The client uses the Checkout Elements SDK or React provider, collects a valid email and payment details, and calls Checkout `confirm`. The old web example names `@stripe/stripe-js` 7.0.0 or later for its HTML/JS module path, and React Stripe.js 5.0.0 or later with Stripe.js loader 8.0.0 or later for the React path; these are dated example requirements. In the old guide's live-mode description, Pay redirects to the Boleto website; its sandbox path redirects to a test page with approval or decline controls.
- **Elements with Payment Intents API:** The server determines the BRL amount and creates a PaymentIntent; the dated examples show `customer_account` for Accounts v2 and `customer` for Customers v1 when saving/retrieving methods. The client uses the Payment Element, `elements.submit()`, then `stripe.confirmPayment({elements, clientSecret, confirmParams: {return_url}})`. The live-mode test section likewise says Pay redirects to the Boleto website. The old generic client snippet mentions an iDEAL intermediate redirect as an example; it does not define Boleto's final paid state. The guide advises Stripe payment events instead of relying on client callbacks for business actions.
- **Direct API:** The merchant creates a BRL Boleto PaymentIntent server-side and collects the customer's name, email, CPF or CNPJ `tax_id`, street address, city, two-letter Brazilian state and postal code. The old guide specifies formats and an ASCII character condition for name, street and city; see raw lines 1331-1345. Its recommended client path passes the PaymentIntent client secret and details to `stripe.confirmBoletoPayment()`, which opens a voucher modal by default. `handleActions: false` lets the client display the number, expiry and PDF itself; `next_action.boleto_display_details` also contains a `hosted_voucher_url` for optional emailing. A separate optional server path creates and confirms the PaymentIntent with `confirm: true` and Boleto payment method data. Voucher creation yields `requires_action`, not a paid intent.
- **Delayed outcome and limits:** For a voucher the customer actually paid, the dated Direct API guide says Stripe sends `payment_intent.succeeded` on the next business day, Monday-Friday excluding Brazilian holidays; funds are not immediately available. For nonpayment by expiry, it says `payment_intent.payment_failed` is sent after one business day. Boleto payments cannot be refunded or disputed by the customer. A Boleto voucher cannot be canceled before expiry; afterward the PaymentIntent returns to `requires_payment_method`, allowing another payment method or cancellation.

## Optional and test details

The May guide describes voucher branding through Dashboard Branding Settings and opt-in payment instruction emails through Dashboard Email Settings; in test environments those emails go only to addresses linked to the Stripe account. Its test email patterns simulate payment after about three minutes, immediate success, immediate or delayed expiry, and never paid. CPF `000.000.000-00` and CNPJ `00.000.000/0000-00` are sandbox validation-bypass values, not production tax identifiers. These simulations do not establish live payment success or settlement.

## Detail locators

- Old raw lines 8-36, 44-106, 171-197: Checkout compatibility, Session settings, voucher redirect and distinct webhooks.
- Old raw lines 251-290, 367-394, 492-543, 658-742: Elements with Checkout Sessions API, email identity alternatives, SDK versions, client confirmation and live/sandbox redirect.
- Old raw lines 744-771, 975-1109, 1150-1157, 1252-1274: Elements with Payment Intents API, Accounts v2/Customers v1 examples, `return_url`, event handling and redirect.
- Old raw lines 1288-1345, 1412-1483, 1518-1625: Direct API prerequisites, client modal and manual actions, voucher and payment states, optional server confirmation, expiry and cancellation.
- Old raw lines 199-244 and 1485-1516: sandbox tests, refunds, disputes and instruction emails.

## Related raw API references

- [[raw/stripe-payments-boleto-accept-a-payment-2026-11-07|2026-11-07 variant navigation index]] — links Checkout, Elements/Checkout Sessions API, Elements/Payment Intents API and Direct API variants. Their current bodies were not captured in this order.

## Raw Sources

- [[raw/stripe-boleto-accept-payment-2025|2026-05-07 full four-variant guide]] — dated factual authority for the flow, limits and examples above.
