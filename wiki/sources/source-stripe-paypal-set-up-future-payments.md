---
title: "Stripe: Set Up Future PayPal Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-set-up-future-payments-2025.md"
tags: [stripe, wallets, paypal, recurring, setup-intent, off-session, mandate, billing-agreement, fraudnet, accounts-v2]
---

## Summary

Guide to saving PayPal payment details and charging customers later via Stripe. Covers Checkout (setup mode), Direct API, iOS, and Android. Includes off-session and on-session charging with saved PayPal methods, Fraudnet/Magnes risk library integration, and mandate/billing agreement lifecycle.

## Key Details

**Recurring payments enablement**: auto-enabled at PayPal activation for most users. Manual path: Dashboard → Payment methods → PayPal → Enable (Recurring payments). Shows as **pending** for up to 5 business days. Enabled by default in test environments.

**Checkout path**: `mode: 'setup'` + `payment_method_types: ['paypal']` + `customer` ID → `checkout.session.completed` webhook → extract `setup_intent` ID → retrieve SetupIntent → get `payment_method` ID.

**Direct API — save**: `stripe.confirmPayPalSetup(clientSecret, { return_url, mandate_data })` → customer approves PayPal billing agreement → `setup_intent.succeeded` webhook. Server-side alternative: create+confirm with `mandate_data` (IP + user agent) + `confirm: true` → `next_action.redirect_to_url`.

**Mandate fields** (`Mandate.payment_method_details.paypal`): `payer_email`, `payer_id`, `billing_agreement_id` (BAID).

**Off-session charging**: create PaymentIntent with `off_session: true` + `confirm: true` + saved `payment_method` + `customer`.

**On-session charging** (Direct API): `confirmPayPalPayment(clientSecret, { payment_method })`. `return_url` **not required** when PM was previously set up via SetupIntent or PaymentIntent with `setup_future_usage`. Required for all other cases.

**setup_future_usage**: set `off_session` on PaymentIntent to save + charge simultaneously.

**Fraudnet/Magnes risk libraries**: required for server-side on-session payments with a saved PM. Pass `payment_method_options.paypal.risk_correlation_id` (Client Metadata ID). Missing it → `paypal_risk_correlation_id_missing` error. Stripe.js handles Fraudnet automatically — server-side manual confirmation requires explicit integration.

**Mandate cancellation**: customer cancels billing agreement via PayPal → `mandate.updated` webhook emitted. All subsequent PIs with that PM fail. For Subscriptions: status changes per automatic collection settings. Fix by charging with a different PM.

**Detach**: `stripe.paymentMethods.detach()` revokes mandate and calls PayPal API to cancel billing agreement.

**Accounts v2 API**: use `customer_account` instead of `customer` on SetupIntent; in public preview for non-Connect users.

## Integration by Platform

**Checkout**: setup mode → Checkout Session → webhook → SetupIntent → PaymentMethod ID.

**Direct API**: `confirmPayPalSetup()` client-side with `mandate_data.customer_acceptance.online.infer_from_client: true`. Off-session: PaymentIntent with `off_session: true`. On-session: `confirmPayPalPayment()` with saved PM (no `return_url` needed).

**iOS**: `STPPaymentMethodPayPalParams` → `STPPaymentMethodParams` → `STPPaymentHandler.confirmSetupIntent()` with return URL.

**Android**: `PaymentLauncher.confirm()` with `ConfirmSetupIntentParams`.

## Raw Sources

- [[stripe-paypal-set-up-future-payments-2025]] — verbatim multi-platform guide (1,124 lines); 18 italic fixes
