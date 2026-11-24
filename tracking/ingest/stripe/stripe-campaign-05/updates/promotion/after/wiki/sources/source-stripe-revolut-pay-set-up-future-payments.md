---
title: "Stripe: Set Up Future Revolut Pay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/revolut-pay/set-up-future-payments"
raw_files:
  - "stripe-revolut-pay-set-up-future-payments-2025.md"
tags: [stripe, wallets, revolut-pay, recurring, setup-intent, off-session, mandate, accounts-v2]
---

## Overview

The May 7, 2026 guide documents how a merchant obtains permission to save Revolut Pay for later charges. It covers hosted Checkout, Direct API, iOS and Android. The November 7, 2026 capture links those variants without including their implementation instructions.

## Permission and customer identity

Obtain the customer’s opt-in before saving, and retain their written agreement. For off-session charges, the May terms cover which payment or series of payments the merchant may initiate, anticipated timing and frequency, how amounts are determined and the cancellation policy when setting up a subscription.

The May web and native sections instruct merchants to show a written authorization notice on a custom form before confirming a SetupIntent or PaymentIntent. The next sentence in each branch says to display it “after the first time you save,” leaving conflicting guidance about the first save. The sample authorization text is recommended wording, with the actual business, terms and revocation conditions scoped to the merchant. See May lines 29–40, 151–162, 210–218, 754–762 and 1007–1015.

Attach the payment method to the object representing the customer. The May guide distinguishes the customer-configured Account used in Accounts v2 examples (`customer_account`) from the Customer used in Customers v1 examples (`customer`). It describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users, with a preview version required for enrollees. The hosted Checkout example specifically uses `customer: customer.id`.

## May setup and saving paths

- **Hosted Checkout.** The server creates a Session in `setup` mode. The example lists card and `revolut_pay` with a Customer ID and `success_url`. Send the customer to the returned Session URL for authorization. In the successful test, the SetupIntent moves from `requires_action` to `succeeded`. See May lines 88–120.
- **Direct API SetupIntent.** Create the SetupIntent server-side with the matching customer identity and `revolut_pay`. May prose describes `usage` values `on_session` and `off_session`. The shown web and native requests use `off_session`. The web client uses the SetupIntent client secret with `stripe.confirmRevolutPaySetup()`, `return_url` and `mandate_data`. The example infers online customer acceptance from the client. See May lines 227–268 and 355–377.
- **iOS and Android SetupIntent.** The iOS example uses `STPPaymentMethodRevolutPayParams` and `STPPaymentHandler.confirmSetupIntent()` with a return URL and setup completion, cancellation or failure outcomes. Android uses `PaymentMethodCreateParams.createRevolutPay()` and `PaymentLauncher.confirm()` with `ConfirmSetupIntentParams`, then reports the setup result to the callback. See May lines 722–801 and 975–1062.
- **Direct API charge and save.** The separate PaymentIntent create-and-confirm path attaches the matching customer identity and uses `setup_future_usage: 'off_session'`, `return_url` and `mandate_data` if creating a mandate. See May lines 440–523.

The May “handle the redirect manually” passage sits inside the Direct API SetupIntent material but demonstrates a **PaymentIntent**. It creates and confirms a payment. If the PaymentIntent status is `requires_action` and `next_action.type` is `redirect_to_url`, the merchant redirects the customer to `next_action.redirect_to_url.url`. Stripe recommends confirming payment status through a webhook. The example provides neither a SetupIntent manual confirmation nor a save flag or mandate. See May lines 379–437.

## Later payments and revocation

A successful setup prepares the saved method for use. The merchant creates and confirms a separate PaymentIntent with the saved PaymentMethod ID and matching customer identity for a later charge, and sets `off_session: true` when the customer is outside checkout. May’s Direct API and native sections explicitly say on-session Revolut payments still redirect to the Revolut app for confirmation even with a saved method. The generic examples about avoiding later authentication do not establish an exemption from that redirect. See May lines 134, 224, 443, 525–567, 585, 803–845, 863 and 1064–1106.

Detaching the PaymentMethod deactivates the reusable method. The May guide lists both `mandate.updated` and `payment_method.detached` events for detach. See May lines 569–571, 847–849 and 1108–1110.

## Related Pages

- [[stripe-wallets]] — Revolut Pay wallet and related payment routes
- [[source-stripe-revolut-pay]] — Revolut Pay method overview
- [[source-stripe-subscriptions-revolut-pay]] — separate subscription setup guide
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-revolut-pay-set-up-future-payments-2025|May 7, 2026 full Revolut Pay future-payments guide]] — 1,110 lines with the original Markdown formatting fixes

## Related raw API references

- [[raw/stripe-payments-revolut-pay-set-up-future-payments-2026-11-07|November 7, 2026 Revolut Pay future-payments variant index]] — hosted Checkout, Direct API, iOS and Android navigation
