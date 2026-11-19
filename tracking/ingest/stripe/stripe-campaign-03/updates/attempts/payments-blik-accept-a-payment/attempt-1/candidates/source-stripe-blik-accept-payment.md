---
title: "Stripe: Accept a BLIK Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/blik/accept-a-payment"
raw_files:
  - "stripe-blik-accept-payment-2025.md"
tags: [stripe, blik, poland, pln, checkout, elements, ios, android]
---

## Overview

The November 7, 2026 capture of this Stripe URL is a **variant index** for Checkout, Direct API, iOS and Android. It supplies no variant body, new prerequisite, state transition, SDK version or availability conclusion. The details below remain attributed to the May 3, 2026 combined guide, whose four sections already cover those routes. The index's lack of a separate Elements link does not establish removal of the older Checkout Session `ui_mode: "elements"` example. See [[stripe]] and [[stripe-blik]].

## Key takeaways from the May 3 guide

- BLIK is a single-use method: the customer obtains a six-digit code in a banking app and enters it in the payment form. The code is valid for **two minutes**. After payment initiation, the bank asks the customer to authorize in that app within **60 seconds**; expiration requires a new code. See raw lines 18–20, 202–204.
- The dated Checkout compatibility table lists PLN as supported and presentment currency, `payment` mode as supported, and `setup` and `subscription` modes as “Not yet.” All Checkout line-item Prices must be PLN. The guide illustrates distinct Stripe-hosted, `embedded_page`, and `elements` Session UI modes, using `payment_method_types: ["card", "blik"]` in the examples. See raw lines 22–38, 48–130.
- Direct API creates a PLN `PaymentIntent` on the server with `blik` in `payment_method_types` and passes its client secret to the client. The client collects the BLIK code in its own form and sends it during confirmation, not during Intent creation. The React `Elements` provider in this guide is optional infrastructure for other payment methods, not the BLIK code input. See raw lines 219–239, 308–310, 358–408, 449–457.
- `stripe.confirmBlikPayment` is awaited in the May React example. The guide says it waits for confirmation success or failure and permits `handleActions: false` to disable Stripe.js polling; that return is **not itself proof of a paid PaymentIntent**. After valid confirmation, the Intent can be `requires_action` with `next_action.type: blik_authorize` while the customer completes bank-app approval. The guide recommends a timer. Fulfill on `succeeded`/`payment_intent.succeeded`; failure sends `payment_intent.payment_failed` and returns to `requires_payment_method`. See raw lines 478–522, 535–566, 673–685.
- In the iOS sample, `STPConfirmBLIKOptions(code:)` feeds `STPPaymentHandler.confirmPayment`; a `.succeeded` handler status can arrive while the Intent remains `requires_action`. In the Android sample, `PaymentMethodOptionsParams.Blik(code)` and `PaymentLauncher.confirm` can call `onPaymentResult` with `PaymentResult.Completed` while the Intent remains `requires_action`. Both paths recommend polling for the Intent's later `succeeded` status; native callback completion is not payment completion. See raw lines 863–918, 1079–1149.

## May 3 detail and qualifications

**Checkout display.** In the banking app, an optional Checkout `payment_intent_data.description` occupies the first two lines (up to 70 characters), an optional `statement_descriptor` the third (up to 22), and the website URL the fourth. The analogous Direct API `description` and `statement_descriptor` are set on the PaymentIntent. See raw lines 133–139, 228–234, 675–681.

**Browser action.** The method prose describes code entry in the payment form followed by banking-app push approval. Generic comments in the older Direct API React examples say a customer will be redirected away (raw lines 573–574, 641–642), while the method prose and `requires_action/ blik_authorize` step describe bank-app authorization (raw lines 18–20, 673–685). Treat browser navigation as unresolved from this capture; neither confirmation call completion nor a generic sample comment proves the final payment outcome.

**Refunds and disputes.** The May Checkout section says refunds are available up to 13 months after payment and bank disputes may be raised within 13 months, with **no appeal process**. These are dated guide statements, not a November update to eligibility or legal timing. See raw lines 151–157.

**Sandbox only.** The guide's success test accepts any six-digit code in a sandbox. Its ten billing-email patterns simulate two immediate invalid/expired-code failures, five delayed bank/provider declines, and three timeouts. These test fixtures do not describe live approval. See raw lines 145–149, 159–188, 687–726, 1163–1190.

**Version examples.** The older web snippet loads Stripe.js from `js.stripe.com/dahlia/stripe.js`; its Android Gradle snippet uses `stripe-android:23.5.0`. Those are captured examples, not evidence of current recommended versions or merchant access. See raw lines 344–353, 1001–1011.

## Related

- [[stripe-blik]] — provider concept and related BLIK sources.

## Related raw API references

- [[raw/stripe-payments-blik-accept-a-payment-2026-11-07|November 7, 2026 variant index]] — navigation only: Checkout, Direct API, iOS and Android variant links; linked bodies were not read.

## Raw Sources

- [[raw/stripe-blik-accept-payment-2025|May 3, 2026 full guide]] — detailed Checkout, Direct API, iOS and Android variants; 1,190 lines.
