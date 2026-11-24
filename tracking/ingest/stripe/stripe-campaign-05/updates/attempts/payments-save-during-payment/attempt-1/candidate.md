---
title: "Save a Customer's Payment Method During Payment"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/save-during-payment"
raw_files:
  - "stripe-save-during-payment-elements-2025.md"
tags: [stripe, checkout-sessions, payment-intents, save-payment-method, customer-session, allow-redisplay, off-session, sepa-debit]
---

## Overview

The April 21, 2026 guide covers saving a payment method during a web payment using Elements with Checkout Sessions or Payment Intents. The November 7, 2026 capture links to the two implementations.

For later redisplay or charging, the April guide tells merchants to obtain explicit consent for that purpose and retain the written agreement. Explain the intended payments, timing and frequency, how the amount is determined, and the cancellation policy for subscriptions. Use the payment details only for the agreed purpose. Saving card-present payment methods uses the separate Terminal process.

## Checkout Sessions API with Elements

The April guide limits saved methods in this integration to cards and ACH Direct Debit. Its new-customer example sets `ui_mode: elements`, `saved_payment_method_options.payment_method_save: enabled` and `customer_creation: always` on the Session. For an existing customer, authenticate them before passing the Customers v1 ID as `customer` or the customer-configured Accounts v2 ID as `customer_account`. The April guide describes Accounts v2 as generally available for Connect and in public preview for other Stripe users, with a preview API version required for the latter.

The April guide says that with saved payment methods enabled on the Session, the then-latest Stripe.js defaulted `enableSave` and `enableRedisplay` to `auto`. In the custom UI examples, set both options to `never` and collect consent explicitly. Pass `savePaymentMethod` when confirming a new method or `paymentMethod` with the selected saved ID. The guide’s `savedPaymentMethods` list exposes methods with `allow_redisplay: always` in this route. Show only methods the customer authorized for this use.

## Payment Intents API with the Payment Element

For the April saved-method UI, create the PaymentIntent and a CustomerSession on the server using the same customer identity, enable the CustomerSession’s `payment_element` component and pass both client secrets when creating Elements. The CustomerSession secret grants access to the customer’s saved methods. If CustomerSession creation fails, the guide says to handle the error and omit that secret. This fallback does not supply the saved-method UI.

At confirmation, Stripe.js uses the customer’s save-checkbox selection to set `setup_future_usage` on the PaymentIntent and `allow_redisplay` on the PaymentMethod. Do not explicitly set both the Intent’s `setup_future_usage` and the CustomerSession’s `payment_method_save_usage` for the same transaction. A server-set `setup_future_usage` overrides the built-in checkbox behavior. The merchant still needs consent, and the guide instructs the merchant to disable the Intent setting on the server if the customer declines. Its per-method example sets `payment_method_options.card.setup_future_usage` for cards when only some offered methods can be saved.

> [!warning] Subscription removal
> The April CustomerSession examples enable `payment_method_remove`. The separate April 21 [[source-stripe-payment-element-saved-pms#Subscription Removal Warning|Payment Element saved-methods guide]] says removing a method through **Saved** also removes it from an ongoing subscription that uses it. Stripe recommends disabling removal there and managing changes on an account settings page that shows subscriptions.

## Later payments and testing

A later off-session attempt uses a separate PaymentIntent with the saved PaymentMethod ID and the corresponding `customer` or `customer_account`. The April examples set `off_session: true` and `confirm: true`. Confirmation can fail if a payment partner requests authentication and the exemption is unavailable.

When set up for reuse, the April guide says Bancontact, iDEAL and Sofort generate a reusable `sepa_debit` PaymentMethod. Use that type when listing saved methods. The documented SEPA Debit payment can enter `processing` before it reaches `succeeded` or `requires_payment_method`. The email and token fixtures in the April guide’s **Test charging a saved SEPA Debit PaymentMethod** section simulate those outcomes, including delayed and insufficient-funds cases.

## Related

- [[stripe-saved-payment-methods]] — Stripe saved-payment methods
- [[source-stripe-checkout-save-during-payment]] — Checkout-specific save-during-payment guide
- [[source-stripe-payment-element-saved-pms]] — Payment Element display and management
- [[stripe-payment-intents]] — PaymentIntent lifecycle
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-save-during-payment-elements-2025|April 21, 2026 save-during-payment guide]] — full Checkout Sessions and Payment Intents implementations.

## Related raw API references

- [[raw/stripe-payments-save-during-payment-2026-11-07|November 7, 2026 save-during-payment variant index]] — navigation to Checkout Sessions API and Payment Intents API.
