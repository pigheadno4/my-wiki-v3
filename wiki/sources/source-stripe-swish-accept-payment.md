---
title: "Stripe: Accept a Swish Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/swish/accept-a-payment"
raw_files:
  - "stripe-swish-accept-payment-2025.md"
tags: [stripe, real-time-payments, swish, sweden, sek, checkout, elements, direct-api, ios, android, react-native, qr-code]
---

## Summary

Swish is a single-use payment method for customers in Sweden. The 2026-05-06 [[stripe]] guide describes Swish and Swedish BankID authorization and immediate payment outcome notification. It covers Checkout, web Elements, Direct API, and custom iOS, Android and React Native flows. The 2026-11-07 capture is a navigation selector for the same six variants. The version-specific details below come from the May guide.

## Key Details

- **Checkout.** The May guide lists Europe as the business location and SEK as the supported and presentment currency. The customer and business location descriptions have different scopes. Use payment mode with all line items in SEK. The guide excludes setup and subscription modes for this Checkout path. It shows dynamic and manual payment method selection, including Stripe-hosted and fully embedded Session examples (lines 8–113).
- **Elements.** Create the PaymentIntent on the server and confirm it on the client with `stripe.confirmPayment` and a `return_url`. Mobile web redirects to Swish. Desktop shows an inline QR code that closes automatically after successful authentication and can be refreshed up to 20 times. Use PaymentIntent status for return-page messaging and Stripe's `payment_intent.succeeded` event for fulfillment. App or browser return and QR modal closure alone do not establish payment success. The automatic-method USD sample is generic. The Swish-specific manual Elements example uses SEK (lines 191–227, 450–452 and 546–683).
- **Direct API.** The merchant creates and confirms a SEK PaymentIntent on the server and supplies a return URL. The optional `payment_method_options.swish.reference` appears in the customer's Swish app. The confirmation example shows `requires_action` with `next_action.swish_handle_redirect_or_display_qr_code`, including `hosted_instructions_url` and QR data, PNG and SVG fields. Redirect to or embed the hosted instructions, which offer desktop QR and mobile app handoff. The phone-number fallback that lets a customer open Swish manually is described as invite-only beta (lines 748–775 and 866–932).
- **Required notice.** Before authorization, the May Direct API and custom iOS, Android and React Native guides require an on-screen localized notice stating that Stripe Technology Europe Limited acquired the payment claim and receives the payment. Stripe displays the notice for Stripe-hosted forms and UI components such as Checkout and Payment Element. See the English and Swedish text and equivalent translation instruction at lines 727–735, 998–1012, 1284–1298 and 1519–1527.
- **Custom mobile.** The May native and React Native flows use a backend SEK PaymentIntent. Native iOS offers a custom scheme or universal link for automatic webview dismissal. The distinct React Native iOS return setup uses a custom scheme and excludes universal links. React Native confirms client-side with `confirmPayment` and `paymentMethodType: 'Swish'` (lines 1103–1197, 1364–1394, 1601–1658 and 1662–1759).
- **Payment outcome and expiry.** The May guide gives customers three minutes to act on a Swish PaymentIntent in `requires_action`. Decline or no action by expiry detaches the PaymentMethod and returns the intent to `requires_payment_method`. Direct API describes `payment_intent.payment_failed` when the customer does not pay and `payment_intent.succeeded` after completed payment. Merchant cancellation of an unexpired PaymentIntent is a separate operation (lines 151–157, 711–717, 914–927, 978–988, 1264–1274, 1499–1509 and 1787–1797).
- **Testing.** May Checkout and Elements distinguish test-page approval and decline from live Swish-app approval and decline. The Direct API test scenarios simulate success after about one minute for an ordinary email, success within seconds with `succeed_immediately`, failure within seconds with `expire_immediately`, and expiry after about three minutes with `expire_with_delay` (lines 137–149, 697–709 and 953–976).

## Related Pages

- [[stripe-real-time-payments]] — Swish and other real-time payment methods
- [[source-stripe-swish]] — separate Swish payment method overview

## Raw Sources

- [[raw/stripe-swish-accept-payment-2025|Swish acceptance guide, captured 2026-05-06]] — full 1,797-line capture with italic formatting fixes to Prices, webhook, client secret, fulfillment, confirm, PaymentMethod and require.

## Related raw API references

- [[raw/stripe-payments-swish-accept-a-payment-2026-11-07|Swish acceptance variant selector, captured 2026-11-07]] — navigation for Checkout, Elements, Direct API, iOS, Android, and React Native.
