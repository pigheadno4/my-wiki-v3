---
title: "Stripe: Accept a Multibanco Payment"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/multibanco/accept-a-payment"
raw_files:
  - "stripe-multibanco-accept-payment-2025.md"
tags: [stripe, vouchers, multibanco, portugal, eur, checkout, direct-api, ios, android, entity-reference, expiry]
---

## Summary

The 2026-05-07 guide documents Checkout, web Direct API, iOS and Android for businesses in Europe or the United States accepting Multibanco from customers in Portugal. The customer receives an entity and reference and pays the EUR voucher outside checkout via online banking or an ATM. Transfer delays can push payment confirmation back several days, especially over weekends.

The 2026-11-07 base capture is a directory to the same four variants. The integration details below come from the May guide. Current variant compatibility, account eligibility and SDK requirements are unresolved by the directory.

## Integration details from 2026-05-07

- **Checkout** uses payment mode with one-time, same-currency EUR line items. The guide describes dynamic payment method presentation and separately shows how to list `multibanco` in `payment_method_types`. The Stripe-hosted example sets `success_url` and the full embedded example sets `return_url` with `ui_mode: embedded_page`. For Multibanco, successful form submission redirects to `hosted_voucher_url`. `checkout.session.completed` signals form submission and voucher creation. Fulfill after `checkout.session.async_payment_succeeded`, when the associated PaymentIntent succeeds. `checkout.session.async_payment_failed` covers expiry or other failure and the associated PaymentIntent returns to `requires_payment_method`.
- **Direct API** creates an amount-and-EUR PaymentIntent on the server. The browser calls `stripe.confirmMultibancoPayment()` with its client secret and the required billing email. Stripe.js displays the voucher in a modal by default. With `handleActions: false`, the integration can display the voucher with entity, reference, expiry date, amount and EUR. In the optional server-confirmation path, Stripe creates and uses a PaymentMethod from the supplied `payment_method_data` including billing email. On `requires_action` with `next_action.type` of `multibanco_display_details`, the server can redirect to `next_action.multibanco_display_details.hosted_voucher_url`.
- **iOS and Android** use the server-created EUR PaymentIntent's client secret and the customer's billing email. iOS uses `STPPaymentHandler.confirmPayment()` with `STPPaymentMethodMultibancoParams`. Android uses `PaymentLauncher.confirm()` with Multibanco payment method parameters. Each displays the voucher in a webview. The iOS `.succeeded` and Android `PaymentResult.Completed` callbacks in these examples indicate voucher display.
- **PaymentIntent events** apply independently of Checkout Session events and client callbacks. `payment_intent.requires_action` indicates a voucher was created and exposes the link at `next_action.multibanco_display_details.hosted_voucher_url`. The same details contain `entity`, `reference` and `expires_at`. The May Direct API and mobile guides identify `payment_intent.succeeded` as the server-observed payment signal for fulfillment.

## Expiry, cancellation and testing in the May guide

- A voucher can be paid until its `next_action.multibanco_display_details.expires_at` Unix timestamp, seven days after creation. On expiry an intent awaiting voucher payment moves from `requires_action` to `processing`, with `payment_intent.processing`. The voucher can no longer be paid. The processing window lasts up to four days for delayed notification of an already initiated transfer. If payment fails to complete within the window, the intent moves to `requires_payment_method` and Stripe sends `payment_intent.payment_failed`.
- Cancel the PaymentIntent to cancel the voucher. Stripe sends `payment_intent.canceled`. Canceling a pending payment invalidates its original voucher instructions, so inform the customer. If funds arrive after the buffer or against a canceled voucher, Stripe automatically initiates a refund for the mispaid amount.
- Successfully reconfirming a `requires_action` PaymentIntent generates new instructions and a new `hosted_voucher_url`. Give the customer the replacements.
- The `fill_never` sandbox scenario delivers `payment_intent.payment_failed` after 11 days and is described as mimicking live behavior. The voucher expiry and the subsequent processing window are separately defined.

## Detail locators

- May raw lines 8–191 cover Checkout compatibility, hosted and embedded examples, voucher redirect, events and tests.
- May raw lines 193–612 cover the Direct API, including client confirmation at 307–385, optional server confirmation at 387–458 and manual presentation at 460–524.
- May raw lines 614–893 cover iOS and lines 895–1166 cover Android, including platform-specific SDK setup, webview callbacks and post-payment events.

## Related

- [[stripe]]
- [[stripe-vouchers]]
- [[source-stripe-multibanco|Multibanco product overview]]

## Raw Sources

- [[raw/stripe-multibanco-accept-payment-2025|2026-05-07 Multibanco acceptance guide]] — verbatim webpage content (1,166 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*webhooks*` ×1, `*fulfillment*` ×1, `*client secret*` ×3, `*PaymentMethod*` ×1, `*webhook*` ×3, `*sandbox*` ×2, `*confirm*` ×2.

## Related raw API references

- [[raw/stripe-payments-multibanco-accept-a-payment-2026-11-07|Multibanco acceptance variant directory]] — 2026-11-07 navigation for Checkout, Direct API, iOS and Android.
