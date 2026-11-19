---
title: "Stripe: Set Up Future Amazon Pay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/amazon-pay/set-up-future-payments"
raw_files:
  - "stripe-amazon-pay-set-up-future-payments-2025.md"
tags: [stripe, wallets, amazon-pay, setup-intent, recurring, off-session, mandates, ios, android]
---

## Overview

The May 7, 2026 guide describes saving Amazon Pay details for later charges through hosted Checkout, Direct API, iOS, and Android. The November 7 capture is only a four-route variant index; it supplies no refreshed setup, mandate, SDK, or payment behavior. See [[stripe]] and [[stripe-amazon-pay]].

## Key takeaways from the May 2026 guide

- **Permission and identity:** The guide calls for customer permission, opt-in terms, and a record of written agreement before saving a method. For later off-session payments, the terms cover permission, frequency/timing, amount determination, and subscription cancellation policy where applicable. Saved details attach to a customer identity: the dated Accounts v2 examples use a customer-configured Account and `customer_account`, while Customers v1 uses a Customer and `customer`. The May text describes Accounts v2 as generally available for Connect and public preview for others, with a preview version for participants; this is historical account guidance, not a current eligibility assertion.
- **Hosted Checkout versus Direct API:** Checkout creates a Session in `setup` mode; its Customers v1 example includes `amazon_pay`, a Customer ID, and `success_url`, then sends the customer to the Session URL for authorization. Direct API can create a SetupIntent for saving without an immediate charge, with `usage` described as `off_session` or `on_session`; the example chooses `off_session`. Its client example calls `stripe.confirmAmazonPaySetup` with the SetupIntent client secret, `return_url`, and online `mandate_data`. A distinct pay-now route creates a PaymentIntent with `setup_future_usage: off_session`; its prose says to provide `mandate_data` if needed, and the examples include it.
- **Later charge and state boundary:** After obtaining the saved PaymentMethod, the later server PaymentIntent uses the same PaymentMethod ID; `off_session: true` applies when the customer is not in that checkout flow. The Checkout test describes a SetupIntent moving from `requires_action` to `succeeded`. A completed setup or browser return does not prove that a later PaymentIntent was confirmed or paid. In the optional manual PaymentIntent redirect branch only, check `requires_action` and `next_action.type: redirect_to_url`; after return, verify payment status, for example through a webhook.
- **Authorization notice:** For a custom form, the May guide requires a written authorization notice before confirming a SetupIntent or PaymentIntent and recommends example words; the exact sample text is not stated as mandatory. Its line saying to show authorization “after the first time” conflicts with its before-confirmation line and the Android first-save wording. Keep that timing ambiguity visible rather than interpreting it as permission to omit first-save notice.
- **Mobile and detach:** The iOS example calls `STPPaymentHandler.confirmSetupIntent` with a SetupIntent client secret and app return URL; the Android example uses `PaymentLauncher.confirm` and `PaymentMethodCreateParams.createAmazonPay()`. iOS 13+ and Android 23.7.0 are May SDK statements. Server-side PaymentMethod detach deactivates the reusable method and is described as emitting `mandate.updated` and `payment_method.detached`.

## Detail locators

- Consent, Accounts v2 versus Customers v1, hosted Checkout setup, and test SetupIntent transition: [[raw/stripe-amazon-pay-set-up-future-payments-2025|May full guide]], lines 29–120.
- Direct API consent/notice, SetupIntent, client confirmation, optional manual PaymentIntent redirect, and pay-now saving: same raw, lines 149–530.
- Later PaymentIntent with saved method and detach events: same raw, lines 532–578.
- iOS setup, first-save notice, `STPPaymentHandler`, later charge, and detach: same raw, lines 580–841.
- Android setup, first-save notice, `PaymentLauncher`, later charge, and detach: same raw, lines 843–1143.

## Related

- [[source-stripe-amazon-pay-accept-payment]] — one-time acceptance guide.
- [[source-stripe-subscriptions-amazon-pay]] — separate subscription integration guide.
- [[stripe-amazon-pay]] — concept and reciprocal source route.

## Raw Sources

- [[raw/stripe-amazon-pay-set-up-future-payments-2025|Amazon Pay future-payment full guide, fetched 2026-05-07]] — dated factual authority.

## Related raw API references

- [[raw/stripe-payments-amazon-pay-set-up-future-payments-2026-11-07|Amazon Pay future-payment variant index, fetched 2026-11-07]] — navigation-only links for Checkout, Direct API, iOS, and Android. Linked bodies were not fetched in this packet and do not revise the May guide here.
