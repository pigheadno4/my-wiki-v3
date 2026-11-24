---
title: "Stripe: Set Up Future UPI Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/upi/set-up-future-payments"
raw_files:
  - "stripe-upi-set-up-future-payments-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, setup-intent, e-mandate, recurring, off-session, upi-autopay]
---

## Overview

The May 6, 2026 guide describes saving UPI payment details for future use through hosted Checkout or the Direct API. The merchant obtains customer permission and sets up a mandate up front. The full May guide supplies the implementation details below. The November 7, 2026 capture gives links to the Checkout and Direct API variants.

## Customer identity and authorization

Attach the payment method to the object representing the customer and associate its ID with the merchant's customer record. The May Direct API samples use `customer_account` for an Accounts v2 customer-configured Account and `customer` for a Customers v1 Customer. The guide describes Accounts v2 as generally available to Connect users and in public preview for other Stripe users, with a preview version required for enrollees. See May lines 14, 29–44, 136–148 and 180–194. For India e-mandate rules, see [[source-stripe-upi-autopay]].

## May setup and payment paths

- **Hosted Checkout setup.** Create a server-side Checkout Session in `setup` mode and send the customer to its returned hosted URL to authorize UPI for future payments. The sample uses `payment_method_types: ['card', 'upi']`, `customer: customer.id` and `success_url`. The test instructs the customer to choose UPI and shows mobile redirect or desktop QR to reach the test approval page. See May lines 75–107.
- **Direct API SetupIntent.** Create a SetupIntent with `upi`, the matching customer identity and `usage` of `on_session` or `off_session`. The samples use `off_session`. Pass the SetupIntent client secret to the client and call `stripe.confirmUpiSetup()` with `return_url` and `mandate_data`. The example uses online customer acceptance with `infer_from_client: true`. See May lines 191–363.
- **Direct API payment and save.** Create a UPI PaymentIntent for the current INR payment with the matching customer identity, `confirm: true`, `setup_future_usage: 'off_session'`, `return_url` and optional `mandate_data`. Confirming initiates the payment attempt. The resulting PaymentIntent can still require customer action. See May lines 365–462 and 506–567.

The Direct API samples show a billing name and an Indian address with `line1`, `line2`, city, state, postal code and country. The May text does not specify requiredness for each sample field. See May lines 202–248, 383–459 and 519–540.

## Later payment and revocation

Create and confirm a new PaymentIntent with the same PaymentMethod ID from the previous SetupIntent or PaymentIntent. Set `off_session: true` when the customer is outside checkout. On-session UPI payments still redirect to the UPI app for confirmation even when the payment method is saved. Detaching the PaymentMethod deactivates it for reuse and emits `mandate.updated` and `payment_method.detached`. See May lines 119–121, 464–504 and 569–571.

The optional manual PaymentIntent flow checks for `requires_action` and `next_action.type` of `upi_handle_redirect_or_display_qr_code`. The May response example shows `hosted_instructions_url` and a nested `qrcode` object with `image_url_png`, `image_url_svg` and `expires_at`. Its prose at line 567 leaves out the `qrcode` level on the image paths. The response shape is dated to the example. See May lines 506–567.

## Related Pages

- [[stripe-real-time-payments]] — UPI and other real-time payment methods
- [[stripe]] — Stripe company page
- [[source-stripe-upi]] — UPI method overview
- [[source-stripe-upi-accept-payment]] — UPI acceptance paths
- [[source-stripe-upi-autopay]] — UPI AutoPay and e-mandate guidance

## Raw Sources

- [[raw/stripe-upi-set-up-future-payments-2025|May 6, 2026 full future UPI payments guide]] — 571 lines, with Markdown emphasis fixes

## Related raw API references

- [[raw/stripe-payments-upi-set-up-future-payments-2026-11-07|November 7, 2026 future UPI payments variant index]] — Checkout and Direct API navigation
