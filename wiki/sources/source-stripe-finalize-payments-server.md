---
title: "Stripe — Finalize Payments on the Server"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/finalize-payments-on-the-server"
raw_files:
  - "stripe-finalize-payments-server-2026.md"
tags: [stripe, payment-element, confirmation-token, server-side, payment-intent, setup-intent, subscription, handle-next-action]
---

## Overview

The 2026-11-07 canonical capture describes rendering the Payment Element before creating a PaymentIntent or SetupIntent and confirming the Intent on the server. It is a variant index for web payment, setup, and subscription pages, not a full implementation capture. The detailed flow below is retained from the 2026-05-11 combined guide; the November index does not establish that its examples, SDK minimums, payment-method support, or account access conditions remain current.

## 2026-05-11 payment variant

The dated web example configures Elements with `mode: 'payment'`, amount, currency, and `paymentMethodCreation: 'manual'`, then renders the Payment Element. On submit, the client calls `elements.submit()` and `stripe.createConfirmationToken({ elements, params })` and sends the token ID to the server. The guide says to use the token immediately; an unused token expires after 12 hours. The server decides the charge amount in a trusted environment and calls `stripe.paymentIntents.create({ confirm: true, amount, currency, confirmation_token })`. Its sample returns `client_secret` and `status`. This `manual` setting belongs to the shown variant; the guide's general Elements options table labels `paymentMethodCreation` optional. See the old raw at lines 82-103, 429-466, 491-536, and 647-676.

If the PaymentIntent has `requires_action`, the client uses `stripe.handleNextAction` for authentication or redirect. **Example mismatch:** the payment and setup server samples return a `client_secret` field, but their next-action samples read `response.clientSecret`; the guide does not reconcile those names. Inspect the actual response shape before adapting the sample. A browser response or next-action callback alone is not durable proof of completed payment: the May guide directs post-payment work from `payment_intent.succeeded` events rather than a client callback. See old raw lines 689-720 and 1399-1429.

The May guide lists ConfirmationToken SDK minimums as stripe-node v14.22.0, stripe-python v8.8.0, stripe-php v13.15.0, stripe-ruby v10.13.0, stripe-java v24.21.0, stripe-go v76.22.0, and stripe-dotnet v43.20.0. These are dated guide values, not updated by the November index (old raw lines 635-645).

## 2026-05-11 setup variant

The setup path uses Elements `mode: 'setup'`, a ConfirmationToken, and server `stripe.setupIntents.create({ confirm: true, confirmation_token, customer })` in the shown Customer example. A SetupIntent saves a method for future payment without an immediate charge. The method must attach to a customer-representing object: either a customer-configured Account through Accounts v2 or a Customer. In the May guide, Accounts v2 was generally available to Connect users and in public preview for other Stripe users; preview participants needed a preview API version. This is a dated access statement, not current eligibility advice. A later off-session charge is a separate PaymentIntent; authentication can fail and require the customer to return. See old raw lines 734-738, 808-815, 1118-1128, 1374-1402, and 1486-1537.

## 2026-05-11 subscription variant

The subscription path requires a customer and a recurring Price, with invoice settings and supported payment methods aligned to Payment Element settings. Elements uses `mode: 'subscription'`; the displayed amount should reflect the immediate charge, including zero for a trial. The example creates a Subscription with `payment_behavior: 'default_incomplete'`, then separately confirms its latest-invoice PaymentIntent using the ConfirmationToken and handles that PaymentIntent's next actions. Creating the Subscription or receiving the server response does not itself demonstrate a successful invoice payment or access entitlement. See old raw lines 1592-1598, 1647-1658, 2024-2028, 2163-2165, and 2446-2532.

## Dated limits and detail locators

The May guide says this integration path does not support BLIK or ACSS pre-authorized debits. It also says a client-created deferred Intent cannot use `customer_balance` with dynamic payment methods because that PaymentIntent needs a customer-configured Account or Customer; for that case it directs creating the PaymentIntent on the server with that object and returning its `client_secret` (old raw lines 27-31). This warning is scoped to the stated path and date. For saved-method consent, CustomerSession examples, optional Elements controls, layout, address collection, off-session error handling, and disclosure, inspect the corresponding variant sections in the May raw rather than inferring a current product guarantee from the November index.

## Related

- [[stripe]] — provider context
- [[stripe-payment-intents]] — PaymentIntent lifecycle and related source routes
- [[source-stripe-accept-payment-deferred]] — client-confirmed deferred Intent variant
- [[source-stripe-two-step-confirmation]] — separate review step

## Related raw API references

- [[raw/stripe-payments-finalize-payments-on-the-server-2026-11-07|Stripe 2026-11-07 canonical variant index]] — navigation only; links to web payment, setup, and subscription variants. Their detailed November content was not pinned here.

## Raw Sources

- [[raw/stripe-finalize-payments-server-2026|Stripe 2026-05-11 combined web payment, setup, and subscription guide]]
